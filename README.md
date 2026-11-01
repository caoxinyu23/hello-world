# To Eat a God 3.0 → Android APK（GitHub Actions 云构建）

把 `ToEataGod-3.0-pc` 这份 Ren'Py 8.5.3 桌面版打包成 Android APK。
**不做翻译**，游戏语言保持原作（西班牙语，含官方英化）。

构建在 GitHub 的 x86_64 runner 上跑，因为 Ren'Py 官方的 Android 工具链
（gradle + aapt2 + RAPT）只提供 x86_64 宿主二进制，手机（aarch64）本地编不了。

---

## 一、这个仓库里有什么

| 路径 | 说明 |
| --- | --- |
| `game/` | 游戏本体（740 MB，1282 个文件），来自 PC 发行版，**未改动** |
| `renpy/` | 同版本（8.5.3）的 Ren'Py 纯 Python 引擎代码，RAPT 打包时需要 |
| `ToEataGod.py` | PC 发行版的启动脚本，RAPT 会把它变成 `main.py` |
| `game/android_compat.rpy` | **唯一新增的文件**：Android 兼容层，见第六节 |
| `android.json` | RAPT 的应用配置：包名、应用名、版本、权限、横屏 |
| `scripts/rapt_build.py` | 驱动 RAPT 的脚本（等价于 launcher 的 "Build" 按钮，但无 GUI） |
| `.github/workflows/android.yml` | 流水线本体 |
| `scripts/make-payload.sh` | 游戏更新时，用它重新铺 `game/` + `renpy/` |

没进仓库的：`lib/`（103 MB 的 PC 版 CPython，Android 上由 `librenpython.so` 替代，
带进去只会白涨 100 MB 包体）、`ToEataGod.exe`、`ToEataGod.sh`。

---

## 二、为什么不需要 NDK

RAPT 包里已经带了**预编译好的** `librenpython.so`：

```
renpy-8.5.3-rapt/prototype/renpyandroid/src/main/jniLibs/
├── arm64-v8a/librenpython.so
├── armeabi-v7a/librenpython.so
└── x86_64/librenpython.so
```

所以整条流水线只需要：JDK 21（java 本身是跨架构的）、Android SDK
（`platforms/android-36` + `build-tools/36.0.0`）、Gradle 9.1 + AGP 8.13。
这些 runner 上全都预装了，**一个额外 SDK 包都不用下载**。

---

## 三、怎么跑

### 1. 建仓库并推上去

```bash
cd toeatagod-android
git init -b main
git add -A
git commit -m "To Eat a God 3.0 android port scaffold"
git remote add origin https://github.com/<你的账号>/<仓库名>.git
git push -u origin main      # 约 740 MB，第一次推会慢，需要有耐心
```

> 单文件最大 21 MB（`audio/the_chillout_factory.wav`），远低于 GitHub 的
> 100 MB 单文件限制，仓库总量 ~750 MB 也在允许范围内。**不要**开 LFS。

### 2. 触发构建

推送后自动跑；也可以 `Actions → Build Android APK → Run workflow`。

一次完整构建约 **15–25 分钟**（首次含 Gradle/AGP 依赖下载；Ren'Py SDK
走 Actions 缓存，二次构建省 ~2 分钟）。

### 3. 拿到 APK

构建产物有两条路，谁先就绪用谁：

- **Release**（推荐，稳）：仓库 `Releases → android-build-<run号>`，
  APK + `.sha256` 都在那里。Release 单文件上限 2 GB，700 MB 的包没问题。
- **Artifact**：Actions 运行页面 → `toeatagod-apk-<run号>`。

---

## 四、装到手机上

```bash
adb install -r ToEataGod-3.0-*.apk
```

或者把 APK 丢到手机存储里点安装（需允许"未知来源"）。

- 包名：`org.toeatagod.port`（要改就改 `android.json` 里的 `package`）
- 应用名：`To Eat a God`
- 最低系统：Android 5.0（minSdk 21）/ 目标 API 36
- 方向：横屏

**首次启动会解压 ~740 MB 资源到应用私有目录，要留出 1.5 GB 空闲空间，
第一次进游戏会卡 1–3 分钟，之后正常。**

---

## 五、签名（想"覆盖安装"就必须看）

默认每次构建**生成一把临时钥匙**，结果是：
不同 run 出的包装不进同一台手机（除非先卸载），存档也会跟着丢。

要固定签名，做一次就行：

```bash
# 在任意装了 JDK 的机器上生成（别名和密码必须就是这两个值，RAPT 写死了）
keytool -genkeypair -keystore android.keystore -alias android \
  -keyalg RSA -keysize 2048 -validity 20000 \
  -storepass android -keypass android \
  -dname "CN=ToEataGod port,O=Port,C=CN"

base64 -w0 android.keystore   # Linux；macOS 用 base64 -i android.keystore
```

把输出存进仓库 secret `ANDROID_KEYSTORE_B64`，之后每次构建都复用同一签名。

⚠️ 这把钥匙丢了，你的应用就永远无法再升级（只能换包名重发）。

---

## 六、对原作动了什么（以及没动什么）

原始 `.rpy` **一行没改**。新增的 `game/android_compat.rpy` 只做三件事：

1. **兜住 `xdg-open`**：原作三处（`rutas/memorias.rpy`、`rutas/pantallas.rpy` ×2）
   用 `subprocess.Popen(['xdg-open', ...])` 打开文件夹/图片。Android 上没有这个
   可执行文件，`Popen` 会抛 `FileNotFoundError` → Ren'Py 弹异常界面 → **卡死**。
   兼容层把这类调用静默降级（并弹一个提示）。
2. **补上用户名**：原作在 `init` 阶段读 `os.getenv('USERNAME')/USER`，Android 上
   是空的，导致"tú debes ser [usuario]"这句台词变成空白。兼容层兜底为 `el visitante`。
3. **给 `HOME` 一个可写落点**：原作会往 `~/Desktop/Nulla/` 写 `Corazón.txt`、
   `Instrucciones.txt`，Android 没有桌面目录。

### 已知限制（不修也能玩，但要说清楚）

原作有一段核心的第四面墙谜题：它让你**退出游戏、进 `game/images/`、把
`parati.jpg` 改名成 `para_nulla.jpg`**，再进游戏时 `cuadro_modificado()` 检测到
文件存在，才走进"Nulla 认得出你"的分支。

APK 里的 `game/` 是只读资产，**玩家改不了**。所以：

- 游戏不会崩（`cuadro_modificado()` 只是恒为 `False`）；
- 但那条"被你改过名字"的分支永远不会触发，属于**丢了一条可选剧情**；
- 那两封信仍会写进应用私有目录，只是打不开、也找不到。

要真正修好，需要改成共享目录 / SAF 文件选择器 / 游戏内交互三选一，
这会改动原作者的叙事设计 —— 属于另一件事，不在"只做 APP"的范围里。

---

## 七、版权

`To Eat a God` 是 itch.io 上已有作者的独立作品。**自己留着自己玩没问题；
分发、上架、商用都需要原作者授权**，这一条与技术无关，也没法用钱绕过去。

Ren'Py 自身部分库是 LGPL，若对外分发，描述里建议带上 Ren'Py 官方文档
要求的那段声明（见 <https://www.renpy.org/l/license/>）。

---

## 八、排错

| 现象 | 原因 / 处理 |
| --- | --- |
| `Compile game scripts` 失败 | 看同一步打印的 `log.txt`；多半是脚本语法或 `game/` 不完整 |
| `android_compat.rpyc` 不存在 | `--keep-orphan-rpyc` 漏了会把 `tl/espanol/*.rpyc` 删掉，西语文本随之消失 |
| Gradle 报 `sdk.dir` | `rapt/sdk.txt` 没写对，或 `ANDROID_HOME` 不是宿主的 SDK |
| 报 `key.store` 相关错误 | `android.keystore` 不存在，或 secret 里那把的别名/密码不是 `android` |
| APK 装上后闪退 | 多半是首次解压资源时空间不足（要 1.5 GB） |
| 每次都要 Gradle 从头下依赖 | `actions/cache` 只缓存了 SDK；要更快就再挂 `~/.gradle` 缓存 |
