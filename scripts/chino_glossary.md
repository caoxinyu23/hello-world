# ToEataGod 汉化术语表（所有翻译 agent 必须严格遵守）

## 一、专名：一律保留原文，不翻译、不音译

角色 / 存在 / 星名：
- Septem、Nulla、Unum、Quinque、Neo、Noor、Shams、Aeliana、Rafael、Michael
- Ignis、Solaris、Fames、Duae、Sextam、Quattor
- Alnitak、Mintaka、Alnilam（三颗星名，保留）

## 二、核心概念：固定译法

| 原文 | 译文 |
| --- | --- |
| Jardín / the Garden | 花园 |
| Estandartes / the Symbols / Standards | 圣旗 |
| Creador / the Creator | 造物主 |
| marioneta / puppet | 傀儡 |
| Vacío / the Void | 虚空 |
| festival de las velas / the candle festival | 烛火庆典 |
| To Eat a God | 吞噬神明 |
| entidad / entities | 存在 |
| estrellas / stars | 星辰 |
| alma | 灵魂 |
| cuerpo | 身体 |
| manos / hands | 双手 |
| ojos / eyes | 双眼 |
| mirada / gaze | 目光 |
| voz / voice | 声音 |
| tiempo / time | 时间 |
| momento | 时刻 |
| lugar / place | 地方 |
| nada / nothing | 什么也没有 |
| historia / history | 历史 |
| conciencia | 良知 / 良心（按语境） |
| propósito | 目的 |

## 三、人称与称呼

- tú / you → 你
- usted → 您（若语境礼貌）
- madre / Mother → 母亲
- padre / Father → 父亲
- [nombrejugador] 是游戏内玩家名字变量，**原样保留**，不要翻译、不要删。

## 四、格式铁律（违反会导致脚本崩溃或显示错乱）

1. 译文里出现的 `{...}`（如 `{b}`、`{sc=3}`、`{/sc}`、`{glitch}`、`{color=...}`、`{size=...}`、`{a=...}`、`{/a}`）是 Ren'Py 文本标签，**必须原样保留，一个字符都不许改**，也不许翻译标签名。
2. `[...]` 形式的游戏变量（如 `[nombrejugador]`、`[config.version!t]`、`[renpy.license!t]`）必须原样保留。
3. `\n`、`\'`、`\\` 等转义序列必须原样保留。
4. 不要添加原文没有的引号、括号或脚注；不要输出译文解释、注释、序号。
5. 保持原文的语气与情感强度；色情/恐怖/暴力内容照原文强度翻译，不弱化也不夸大。
6. 一句译文对应一条，不要合并、不要拆分、不要调换顺序。
7. 专名一律用第二节表格里的原文拼写。
