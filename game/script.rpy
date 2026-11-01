default persistent.nombrerafael = False
define quinque =Character ("Quinque", color = "#003af9")
define aeliana =Character ("Aeliana", color= "#d87700")
default llave_septem = False
default necesitasanulla = False
$ nombrejugador = ""
define nj = DynamicCharacter ("nombrejugador", color= "#6e404e")
define nulla =Character("Nulla", color= "#ffffff")
define jugador =DynamicCharacter(_("tu"), color= "#ff03ab") 
define el =Character ("???", color= "#b00000")
define ell =Character ("???", color= "#ffdd00")
define septem =Character (_("Septem"), color= "#fffb00")
define unum =Character ("Unum", color= "#ff0000")
#default persistent.juegocompleto = False
default persistent.null = False
default cuchillo_unum = False
image nulla_normal:
    "nullacercanormal1.png"
    1.5
    "nullacercanormal2.png"
    0.10
    "nullacercanormal3.png"
    0.15
    "nullacercanormal4.png"
    0.10
    "nullacercanormal5.png"
    1
    "nullacercanormal6.png"
    0.10
    "nullacercanormal8.png"
    0.10

    repeat 


image nulla_enojado:
    "nullacercaenojo1.png"
    1.5
    "nullacercaenojo2.png"
    0.10
    "nullacercaenojo3.png"
    0.15
    "nullacercaenojo4.png"
    0.10
    "nullacercaenojo5.png"
    1.5
    "nullacercaenojo6.png"
    0.10
    "nullacercaenojo7.png"
    0.10
    "nullacercaenojo8.png"
    0.10
    repeat

image nulla_blush:
    "nullacercablush1.png"
    1.0
    "nullacercablush2.png"
    0.10
    "nullacercablush3.png"
    0.10
    "nullacercablush4.png"
    1
    "nullacercablush5.png"
    0.10
    "nullacercablush6.png"
    0.10
    repeat

define quattor =Character("Quattor", color= "#9100f1")
define duae =Character("Duae", color= "#921414")
define tria =Character("Tria", color= "#00f15c")
define sextam =Character("Sextam", color= "#f971aa")
define fames =Character ("Fames", color="#cc00ff") 
define ignis =Character ("Ignis", color= "#d87700")
define solaris =Character ("Solaris", color= "#d87700")
default bloquear_iconos = False
label start:
    scene negro
    if persistent.null == True:
        jump null
    
    else:
        pass

    play music "audio/calamity.WAV" fadein 1.0 volume 0.5
    $ bloquear_iconos = True
    "En el jardín existen 7 estandartes a los cuales se les debe rendir culto. Cada uno representa un concepto ligado a la creación del jardín."
    scene 7estandartes with Dissolve(2)
    
    "Los estandartes son entidades engendradas por el creador para mantener el orden y funcionamiento del jardín."
    scene 7estandartess with dissolve
    "Todos los seres nacidos bajo el comando del jardín tienen una conexión limitada con un estandarte representativo, dependiendo del día en que se haya nacido"
    scene 7estandartesss with Dissolve(1)
    "... Nadie nace el día 7. El domingo, el domingo es un día sacro."
    scene 7estandartessss with Dissolve(1)
    "Se dice que los estandartes eligen a 6 personas luego del festival de las velas, para luego consumirlos-"
    scene estandarte7 with Dissolve(1)

    "Con la esperanza de que alguno de ellos sea la reencarnación del creador."
    "..."
    stop music fadeout 3.0

    scene negro with Dissolve(2)
    "El pasado de tu personaje no importa, es un cuerpo más para tomar por ti"
    "... algo que ya estás acostumbrado supongo."
    "Bienvenido al jardín, un lugar usado como prueba."
    "Un lugar desechable luego de terminar de jugarlo."
    "El juego es simple, no debes dejar que los demás personajes descubran que tu marioneta está conectada a ti."
    "Tu marioneta será enviada como un regalo para los estandartes... donde tú deberas actuar como si perteneciera al lugar."
    "....Por favor no hagas nada que está fuera de lo estipulado, ni invoques el nombre del representante del vacío, lo tienes estrictamente prohibido."
    "Aunque se te de la oportunidad-"
    "No lo hagas."
    "..."
    "Sientes como caes en una superficie dura, la cual te raspa las rodillas."
    "Es un golpe seco, que hace un eco extraño en el lugar."
    "Puedes escuchar un ruido de cubiertos siendo raspados en un plato."
    "Y luego un silencio sepulcral..."
    "Algo está mal."
    
    menu:
        "Abrir los ojos":
            call respuesta1 from _call_respuesta1

        "Mantenerlos cerrados":
            call respuesta2 from _call_respuesta2
    
    scene mesa
    play music "audio/misconception.mp3" fadein 0.5 volume 0.5

    "Miras donde has caido, y te das cuenta de que estás encima de una mesa."
    "Caiste justo sobre un pastel, provocando que toda tu mano y parte de tu rodilla se hayan manchado con chocolate."
    el "Hey..."
    "La voz se ha escuchado detrás tuya, por reflejo giras tu cuerpo y cabeza para poder observar de quien se trata"
    scene mesanulla1 with dissolve
    "Frente tuyo se encuentra un hombre que te devuelve la mirada con asombro. Y antes de poder preguntar que es lo que está pasando, él te interrumpe."
    el "No deberías estar aquí."
    el "..."
    scene mesanulla2 with dissolve
    el "Debe ser una broma."
    el "No puedo creer que nuevamente se haya descompuesto el mecanismo de distribución."
    el "Todo tengo que hacerlo yo. No hay nadie aquí quien sea lo suficientemente responsable de verificar si todo está en orden."
    scene mesa with dissolve
    "Sientes como manos invisibles te agarran por las extremidades y te hunden en un vacío que llega a traspasar la mesa."
    scene negro with dissolve
    "Poco a poco te vas hundiendo en un vacío oscuro que te envuelve... la sensación es extraña, calidamente extraña."
    scene cocinanulla with dissolve
    show nulla2incomodo at center with moveinright
    el "Qué demonios-!"
    hide nulla2incomodo
    show nulla2serio at center
    el "No hay información tuya"
    hide nulla2serio
    show nulla1disgusto
    el "No puede ser posible"
    el "..."
    

    menu:
        "Preguntar que está pasando":
            call respuesta3 from _call_respuesta3
    


        "Intentar escapar":
            jump respuesta4
    

    
    scene cocinanulla
    hide nulla1disgusto
    show nulla2serio
    el "No puedo ver la conexión con tu estandarte"
    hide nulla2serio
    show nulla2blush
    el "Al parecer no eres un súbdito..."
    el "Disculpa, me he equivocado."
    hide nulla2blush
    show nulla3feliz
    el "Bienvenido, te he estado esperando."
    el "Madre ha dicho que enviaría a un nuevo jueguete..."
    "La palabra juguete no suena bien, sientes un pequeño hormigueo de incomodidad ante lo extraño de la situación."
    "Pero recuerdas que tienes que poner buena cara."
    "Actúa natural."
    "Como si realmente pertenecieras aquí."
    hide nulla3feliz
    show nulla1disgusto
    el "Después de lo que pasó con el último, realmente espero que tú dures más tiempo."
    "Realmente no quieres saber que ha pasado con el último..."
    hide nulla1disgusto
    show nulla2normal
    el "Mi nombre es Nulla, dueño del vacío. Un gusto conocerte."
    hide nulla2normal
    show nulla1risa
    nulla "Antes de partir, necesito tu nombre."
    hide nulla1risa
    show nulla3feliz
    nulla "¿Cómo te llamas?"
    $ nombrejugador = renpy.input (_("Escribe tu nombre"))
    nj "Me llamo [nombrejugador]"
    hide nulla3feliz
    show nulla1normal
    nulla "Bienvenido al vacío [nombrejugador]"
    "Nulla te extiende su mano para apretarla con fuerza, en modo de saludo. A pesar de pasar los segundos, él no te suelta. Sientes como su mirada te devora el alma."
    "Pareciera que estuviera buscando algo."
    $ bloquear_iconos = False

    menu:
        "Mantener la mirada":
            jump respuesta6
        
        "Desviar la mirada":
            call respuesta5 from _call_respuesta5
    


    
    hide nulla1normal
    show nulla2incomodo
    nulla "Supongo que madre te ha dado vida y no te ha explicado nada... Que negligente de su parte."
    hide nulla2incomodo
    show nulla2blush
    nulla "Tendrás que ayudar en el hotel por el día de hoy."
    hide nulla2blush
    show nulla1normal
    nulla "Atenderás de mesero en el comedor, hoy vendrán algunos estandartes pues tienen una reunión en mi hotel."
    hide nulla1normal
    show nulla2normal
    nulla "Si los atiendes bien, tal vez te tomen como aprendiz."
    hide nulla2normal
    show nulla2serio
 
    nulla "Pero ahora solo eres un juguete, asi que ten cuidado."
    hide nulla2serio
    scene negro with dissolve

    "La entidad que se hace llamar Nulla te toca la frente y sientes nuevamente como unas manos invisibles te toman de las extremidades para empujarte hacia abajo, con ello el suelo te traga en una negrura total."
    nulla "No te asustes, pronto llegaremos a destino."
    "A pesar de no ver nada, puedes sentir como estás flotando en el vacío."

    stop music fadeout 3.0

    "De la nada, una presión extraña es ejercida sobre tu cuerpo, provocando que tengas la sensación de que estás cayendo."
    "Y efectivamente, caes sobre tus manos en un suelo frío."
    scene hotelcocina with vpunch
    "Miras a tu alrededor y el lugar ha cambiado."

    play music "audio/europalce.WAV" fadein 1.0 volume 0.5

    "Ya no te encuentras en la misma cocina de antes."
    "Ahora es una más grande, parecidas a las cocinas que están en los restaurantes."
    nulla "Hemos llegado."
    "Subes la mirada para encontrar a Nulla, quien yace parado a un lado tuyo."
    "Pero no te mira."
    "Más allá, cerca de los cuchillos, hay una persona de aspecto extraño."
    show nulla1risa at right with dissolve
    "Nulla lo mira a él."
    nulla "¡Hey, Fames!"
    hide nulla1risa
    show nulla3feliz at right
    show fames at left with moveinleft
    "Él hombre extraño pega un salto al oir a Nulla."
    "Al mirarlo con más detenimiento, te das cuenta de que lleva una máscara que te impide verle las facciones."
    fames "Señor Nulla."
    hide fames
    show fames2
    fames "Pensé que hoy no vendría..."
    "No se oye muy contento con la llegada de Nulla."
    hide nulla3feliz
    show nulla2blush at right
    nulla "Tuve un pequeño inconveniente."
    fames "¿Tiene que ver con la criatura maloliente que está a su lado?"
    "¿Maloliente? Ladeas ligeramente la cabeza para comprobar su dicho... encontrando que nisiquieras hueles, a nada en absoluto."
    hide nulla2blush
    show nulla1risa at right
    nulla "Algo así."
    fames "Señor Nulla..."
    hide fames2
    show fames3
    hide nulla1risa
    show nulla2blush at right
    fames "Esa cosa huele a humano."
    hide nulla2blush
    show nulla2serio at right
    fames "Tengo que devolverlo al almacén."
    hide nulla2serio
    show nulla1disgusto at right
    nulla "Deberías revisar tu olfato Fames, se te está estropeando."
    hide nulla1disgusto
    show nulla2normal at right
    nulla "Este es el nuevo juguete que ha enviado Madre, para entretener a los estandartes."
    hide fames3
    show fames
    fames "Pero el último lo ha roto Quinque por completo... pensé que habían quedado en que no se harían más..."
    hide nulla2normal
    show nulla2serio at right
    nulla "Eso fue porque Quinque es un animal. No cuida de las cosas... Supongo que Madre no puede dejar a Septem sin su comida semanal..."
    hide fames
    show fames2
    fames "Se nota como te arde el favoritismo..."
    "De cierta manera, sientes que eres el mal tercio de la conversación..."
    "Tampoco es como que tengas mucho que aportar."
    hide nulla2serio
    show nulla2normal at right
    nulla "De todas maneras, le tengo fe a esta creación. Hay algo diferente, se siente distinta a los demás."
    fames "La única diferencia es que apesta a humano. Tal vez eso les guste a los 7."
    hide fames2
    "Fames se retira para ir en busca de un plato."
    "Al volver, puedes apreciar lo que se encuentra ahí."
    "Nulla hace lo mismo desde su lado."
    scene carnefames with dissolve
    "Es carne."
    scene nullayfames2 with dissolve
    "Nulla mira a Fames con una cara que denota gracia."
    scene nullayfames with dissolve
    nulla "Si dejas que atienda a los estandartes tal vez te salves de que alguno de tus empleados pierda la vida."
    nulla "Ultimamente los estandarte han estado muy alterados."
    scene nullayfames2 with dissolve
    fames "..."
    fames "......."
    fames ".................."
    fames "Está bien, usted gana."
    fames "Ahora por favor, deje de interumpir mi trabajo."
    scene hotelcocina with dissolve
    "Nulla se despega de Fames y comienza a caminar en dirección a la puerta que parece ser la salida de la cocina."
    show fames at center
    nulla "Te veré luego de un rato. Quedas a cargo de Fames."
    nulla "Adíos."
    hide fames
    show fames2 at center
    fames "Que imbécil..."
    fames "Bien, necesito que atiendas a los estandartes que llegarán dentro de poco."
    fames "Mientras, prepara la mesa para ellos."
    scene hotelcomedor with dissolve
    "Fames te enseña la mesa en que vendrán los estandartes, y te explica que ellos están alejados del público normal pues tienen temas importantes que  discutir entre ellos."
    "también Fames te ha instruido que la comida deberá estar puesta en la mesa antes de que ellos lleguen."
    "Ahora te encuentras sin supervisión."

    menu:
        "Hacer lo que te pidieron":
            call respuesta7 from _call_respuesta7
        


        "Escapar del lugar":
            jump badend_nulla
    

    "Tiendes la mesa con sumo cuidado."
    "De vez en cuando Fames pasa cerca tuyo para inspeccionar como vas. Una vez considera que has terminado de colocar la mesa, te llama a la cocina."
    scene hotelcocina with Dissolve(1.5)
    "Te explica que tienes que poner los platos de entrada y que luego deberás esperar a que los estandartes lleguen... Mientras Fames prepara los platos, te comenta que hoy solamente vienen 5 estandartes"
    "Cada uno tiene un aura intimidante y todos son muy propensos a responder desmedidamente a sus trabajadores si es que algo no les gusta..."
    show fames at center with dissolve
    fames "Sobretodo Unum. Tiene esos dos ojos que te siguen a todas partes."
    fames "..."
    hide fames 
    show fames2 at center
    fames "Escuché que esos ojos se los ha quitado a Quattor en una pelea."
    fames "Odio a ese malcriado."
    hide fames2
    "Una vez Fames termina de preparar los platos de entrada, te los deja en la encimera y te desea buena suerte a regañadientes."
    "Son 5 platos, pero por tu carencia de manos extras, solo te llevas dos."
    "Un plato en cada lado."
    scene hotelcomedor with Dissolve(1.5)
    "Caminas por el mismo recorrido que llevas haciendo pero al acercarte a la mesa, ves que algo no está bien."
    "No está vacía."
    stop music
    scene estandartes1 with vpunch

    play music "audio/calamity.WAV" fadein 2.0 volume 0.4

    "De la impresión, casi se te han caido los platos."
    "Hay dos personas sentadas agusto en la mesa que se supone que son para los estandartes."
    "Ellos te miran, el rubio con corona ridícula te mira de manera expectante, mientras que el pelirrojo te sonríe de oreja a oreja."
    "... Sus dientes te recuerdan a los de un tiburón."
    scene estandartes2 with dissolve
    "Hay un momento en que ninguno de los tres toma la iniciativa ni reacciona."
    "Pero a ellos no se les ve nerviosos."
    "Es más, estan esperando a tu reacción para poder seguir con sus cosas."

    menu:
        "Presentarte":
            scene hotelcomedor with dissolve
            "Supones que estos deben ser los estandartes de los cuales Nulla y Fames han estado hablando..."
            "De cierto modo, te cuesta imaginar que pueden llegar a quitarle la vida a algún trabajador. Pues se ven bastante amigables."
            "Sin hacerlos esperar ni tentar tu suerte, decides presentarte."
            nj "Mi nombre es [nombrejugador], el día de hoy les estaré atendiendo."
            scene hotelcomedor 
            "El pelirrojo busca con la mirada al rubio, pero el rubio solo te mira a ti."
            "De cierta manera te hace sentir nervios en el estómago."
            show unum2duda at right with dissolve
            el "Hey Septem"
            hide unum2duda
            show unum2blush at right
            el "Este no es un trabajador... ¿No será el regalo que nos hace Madre?"
            hide unum2blush
            show unum1normal at right
            el "Es muy similar al anterior. Pero mejor."
            el "Los ojos."
            hide unum1normal
            show unum2feliz at right
            el "Son los ojos que tiene... y el olor que emana. WOW parece que ahora Madre los está haciendo similares a los humanos."
            show septem2normal at left
            ell "{sc=1}Efectivamente.{/sc}"
            hide septem2normal
            show septem1normal at left
            ell "{sc=1}...{/sc}"

            $ rutanulla = False



        "{glitch=30.0}{color=ffffff}{b}Presentarte como jugador{b}{/color}":
            scene hotelcomedor
    
            nj "Se que puede sonar muy extraño... pero no soy nada más que una vasija que está vinculada con un ente de otro plano."
            nj "Me controla y ahora mismo ha roto una de las reglas que en un inicio le han dicho que no rompiera."
            show unum2duda at right with Dissolve(2)
            nj "Y--"
            "{sc=3}{b}Ya basta.{b}{/sc}"
            "{sc=3}{b}Si luego algunos personajes presentan problemas será por tu propia culpa.{b}{/sc}"
            "{sc=3}{b}Sigamos{b}{/sc}"

            el "..."
            hide unum2duda
            show unum2blush at right
            el "JAJAJAJAJAJAJAJAJAJAJA-"
            show septem1risa at left with dissolve
            hide unum2blush
            show unum2enojo at right
            ell "{sc=1}Unum.{/sc}" 
            "La voz del rubio resuena tanto a tu alrededor como dentro de tu cabeza..."
            "Un escalofrío te recorre el cuerpo."
            hide unum2enojo
            show unum1risa at right
            hide septem1risa
            show septem1normal at left
            ell "{sc=1}No te rías tan alto.{/sc}"
            hide unum1risa
            show unum1normal at right
            el "No recordaba que tuvieran tanta autonomía..."




            $ rutanulla = True

       
        "Pedirles que se retiren.":
            scene hotelcomedor
            "No puedes dejar que estas personas se sienten en una mesa que ya se encuentra reservada para los estandartes..."
            "Los miras nuevamente, y definitivamente no son los 5 comensales que Fames describió."
            "Armándote de valor, te aclaras la garganta antes de hablar para hacer tu petición."
            nj "Les pido amablemente que se retiren de esta mesa... está reservada para gente especial."
            show unum2duda at right with dissolve
            "El pelirrojo te mira extrañado, como si no se esperara esa respuesta de tu parte."
            el "¿Tendrá problemas a la visión?"
            "El pelirrojo le pregunta al rubio"
            show septem2incomodo at left with Dissolve(1.5)
            ell "{sc=1}Debe ser la sorpresa que Nulla nos había comentado...{/sc}"
            "La voz del rubio resuena tanto a tu alrededor como dentro de tu cabeza..."
            "Un escalofrío te recorre el cuerpo."
            hide unum2duda
            show unum2feliz at right
            el "Ahhh- es el nuevo regalo de Madre."
            "Es ahora cuando caes en cuenta de que estos deben ser algunos de los estandartes..."
            
            $ rutanulla = False

    scene hotelcomedor with Dissolve(2)
    "No sabes como contestar a eso, por lo que decides observar más allá de la mesa, y te das cuenta de que Nulla les está observando con una mirada intensa."
    

    show unum2blush at right
    el "¿Puedo ser el primero en usarle?"
    show septem2normal at left
    ell "{sc=1}Debemos esperar a los demás.{/sc}"
    hide unum2blush
    show unum2enojo at right
    el "Han dicho que se demorarían porque Quinque estaba haciendo un berrinche ¡Tenemos que esperar al menos una hora!"
    hide septem2normal
    show septem2incomodo at left
    "Hay un silencio incómodo antes de que el rubio lo rompa."
    ell "{sc=1}Entre tú y Quinque no sé quien es peor..{/sc}"
    "El pelirrojo entrecierra los ojos mirando al rubio con rabia, más no dice ni rebate nada."
    "En cambio, opta por mirarte nuevamente, y cruzándose de brazos sentencia."
    hide unum2enojo
    show unum1normal at right
    el "Podemos aprovechar el tiempo y empezar... así cuando lleguen los demás nosotros ya estaremos listos."
    hide unum1normal
    show unum2enojo at right
    el "Además, a mí nunca me toca la esencia... solo partes banales."
    ell "{sc=1}¿Qué ganaría yo si empezamos antes?{/sc}"
    hide unum2enojo
    show unum1incomodo at right
    el "Siempre te quejas que lo rompen muy rápido... además, el tiempo que te tomas cuando te toca es eterno."
    el "Quattor ha dicho que es porque te gusta hablar con el regalo antes de devorar su esencia."
    hide unum1incomodo
    show unum2duda at right
    el "Eres muy extraño..."
    hide septem2incomodo
    show septem1disgusto at left
    ell "{sc=2} ¡Eso no es de tu incumbencia! {/sc}"
    hide septem1disgusto
    show septem1triste at left
    ell "{sc=1} De todos modos, no lo entenderias.{/sc}"
    el "............"
    ell "{sc=1} ...{/sc}"
    hide unum2duda
    show unum1incomodo at right
    el "¡Ya sé!"
    el "¿Qué tal si aprovechamos el tiempo para hacer eso que haces tú?"
    hide unum1incomodo
    show unum1risa at right
    el "......."
    hide unum1risa
    show unum2feliz at right
    el "¿Hablar? ¿hablar con el regalo?"
    hide septem1triste
    show septem2incomodo at left
    ell "{sc=1}...Tendriamos que sellar la mesa.{/sc}"
    hide unum2feliz
    show unum1incomodo at right
    el "Llama a Nulla para que lo haga."
    ell "..."
    hide septem2incomodo
    show septem2normal at left
    ell "{sc=2.5} N U L L A {/sc}"
    scene hotelcomedor
    "En un abrir y cerrar de ojos, Nulla se materializa a tu lado con la mirada fija en el rubio."
    show nulla2serio at right with moveinright
    nulla "Su santidad Septem."
    "El tono utilizado por parte de Nulla al rubio, Septem, es uno totalmente arisco."
    "Como si tuviera adversión a solo nombrar el título del rubio."
    hide nulla2serio
    show nulla2normal at right
    nulla "¿Necesita algo?"
    show septem1normal at left
    septem "{sc=1}Quiero que selles la mesa por un rato...{/sc}"
    hide nulla2normal
    show nulla2normal at center with dissolve
    show unum2enojo at right
    el "Hey pero no quiero que tu escuches lo que hable con el regalo"
    el "Quiero privacidad."
    hide septem1normal
    show septem2incomodo at left
    septem "¿Y qué propones?"
    hide nulla2normal
    show nulla1normal at center
    nulla "Podrían dejar que el regalo elija e invoque uno de sus nombre..."
    "... supones que están hablando de ti. Miras directamente a Nulla a los ojos y sientes como el te clava la mirada, implícitamente comandando a que no te rehuses."
    el "..."
    hide unum2enojo
    show unum2feliz at right
    el "Oh! jamás hemos hecho esto, suena interesante"
    septem "{sc=1.5} Bien, ¿A quién eliges?{/sc}"

    scene hotelcomedor
    

    menu:
        "Septem...":
            jump rutaseptem
        
        "Nulla...":
            "Intentas decir su nombre pero te es físicamente imposible."
            "Miras a Nulla, quien al percatarse tal vez de lo que intentas hacer, procede a mover sus manos realizando señas extrañas."
            "{glitch=20.0}{color=ffffff}{b}Vamos...              Intenta de nuevo.{/glitch}"
            "Puedes escuchar claramente la voz de Nulla en tu cabeza, y haciendo caso, lo intentas nuevamente."
            "Pronuncias su nombre y alcanzas a ver como la cara de Septem se deforma en una mueca extraña..."
            "Nulla en cambio, sonríe."
            if rutanulla: 
                jump rutanullaa

            show nulla2blush at center with dissolve
            "Intentas decir su nombre pero te es físicamente imposible. Por lo que lo apuntas."
            "Nulla se ve descolocado por tu elección. Pero rápidamente se dispone a contestar."
            nulla "Uy, lo siento no tengo el permiso hacer eso."
            hide nulla2blush
            
            menu:
                "Septem.":
                    jump rutaseptem

                "El pelirrojo":
                    jump rutaunum

        
        "El pelirrojo...":
            jump rutaunum






















    
    















    








    return



    label respuesta1:
        scene mesa with dissolve
    return
        

    label respuesta2:
        "Mantienes cerrados los ojos por un momento, pero se oye una voz que se aclara la garganta con incomodidad."
        "Decides abrir los ojos para saber donde te encuentras."
        scene mesa with dissolve
    return



    label respuesta3:
        "¿Qué está pasando?"

    return





    #BAD ENDINGS
    #BAD ENDINGS

    label respuesta4:
        stop music fadeout 2.0
        hide nulla1disgusto
        scene cocinanulla
        "El instinto de escapar y correr se acciona en ti y aprovechando que el hombre se encuentra distraído, tus piernas comienzan la marcha"
        "Sin esperar a que el hombre pueda reaccionar corres a la puerta que está al frente"
        "Está abierta"
        scene entradanulla with dissolve
        "Llegas a lo que parece ser la entrada principal, mientras corres sientes que nadie te está persiguiendo... al mirar atrás no ves que el hombre esté detrás tuya"
        "Vuelves a mirar a delante y el hombre aparece frente tuyo. Como si se hubiera teletransportado"

        play music "audio/the_chillout_factory.WAV" volume 0.3

        el "Lo siento. No puedo dejar que salgas fuera del dominio."
        "Sientes como te empuja contra el suelo y caes con él encima"
        scene badenduno with dissolve
        "Su mano izquierda viaja a tu cuello mientras que la otra se coloca lentamente en tu corazón"
        "Sin mucho esfuerzo te atraviesa tu caja torácica rompiendo huesos y órganos"
        scene badenduno1 with dissolve
        "Lo ultimo que ves es como la figura del hombre te examina de cerca"
        "Tu vista comienza a ponerse borrosa."
        scene negro with dissolve
        
        "BAD END"
        $ MainMenu(confirm=False)()
    return

    label respuesta5:
        "Desvias la mirada, no aguantando la manera en que los ojos de Nulla hacen hoyos en lo más recóndito de tu cabeza."
        "Tus ojos viajan a donde sus manos yacen conectadas aun. Eres el primero en soltar la mano. Provocado que Nulla se ria por lo bajo."
        
    return

    label respuesta6:
        hide nulla1normal
        show nulla2serio
        nulla "Tú eres..."
        "La mirada de Nulla se vuelve vacía por un segundo para ser reemplazada rápidamente por unos ojos llenos de asombro."
        nulla "Eres de {i}allá{i}."
        nulla "No eres de aquí."
        menu:
            "Explicar":
                jump respuesta0

            "No decir nada":
                jump respuesta0


label respuesta0:
    scene cocinanulla with dissolve
    "Sientes como Nulla te tira de la mano, acercando tu cuerpo al suyo. Al instante su otra mano te comienza a apretar el cuello, bloqueando la entrada de aire a tus pulmones."
    nulla "{glitch=40.0}{color=fc0c0c}{b}TE  VEO{b}{/color} .{/glitch}"

    stop music fadeout 3.0

    "Antes de que tu vista se nueble por completo, Nulla te suelta."

    play music "audio/the_chillout_factory.WAV" volume 0.2

    nulla "Así que esto no es más que una marioneta."
    nulla "Pido disculpas por mi comportamiento... pero no pensé que estaría frente a alguien del plano {glitch=40.0}{color=ffffff}{b} superior{b}{/color} .{/glitch}"
    scene teveo1 with dissolve
    nulla "{glitch=30.0}{color=ffffff}{b} Eres  adorable {b}{/color} .{/glitch}"
    nulla "{glitch=30.0}{color=ffffff}{b} Hmmmmm {b}{/color} ...{/glitch}"
    scene teveo2 with dissolve
    nulla "{glitch=20.0}{color=ffffff}{b} Si mato a la marioneta tal vez podré sacarte de ella {b}{/color} .{/glitch}"
    nulla "{glitch=20.0}{color=ffffff}{b} Y podré salir de este bucle {b}{/color} .{/glitch}"
    nulla "{glitch=20.0}{color=ffffff}{b} No te muevas por favor, solo será un segundo {b}{/color} ...{/glitch}"
    menu:
        "No creo que sea buena idea...":
            jump respuesta00
        

        "Está bien.":
            jump respuesta00
    

    label respuesta00:
        "Nulla no te deja hablar, en un segundo ya te tiene nuevamente entre sus brazos y una de sus manos se posa en tu pecho."
        nulla "Te extirparé tu esencia, con eso podré sacarte de ahí."
        scene teveo3 with dissolve 
        nulla "No dolerá nada, al menos a ti, [nombrejugador]."
        nulla "No puedo decir lo mismo para la marioneta."
        "Sientes como Nulla te rompe el pecho y comienza a extraer algo que se encuentra dentro."
        "Duele."
        "Duele mucho."
        scene teveo4 with dissolve
        "Tu visión comienza a nublarse."
        scene teveo5 with dissolve
        nulla "Hey, ¿que está pasando?"
        nulla "No. no no no."
        scene teveo6 with dissolve
        nulla "No es justo."

        scene negro

        "{glitch=40.0}{color=fc0c0c}{b}BAD  END{b}{/color} .{/glitch}"


    $ MainMenu(confirm=False)()



    label badend_nulla:
        "Miras a todos lados, buscando rastros de Nulla o Fames... no hay nada más que mesas vacías."
        "Algo en tu estómago te dice que no deberías hacerlo, un mal augurio."
        "Pero tus ansias de liberarte y escapar de aquí son más fuertes."
        "Caminas a paso lento para no llamar la atención. Fingiendo que estás buscando algo."
        "La puerta de entrada está cerrada por lo que no puedes salir por ahí."
        "En cambio, hay una escalera que lleva abajo"

        menu:
            
                
            "Bajar.":
                jump badend_nulla1
            

            "B A J A R .":
                jump badend_nulla1
            
            "{glitch=30.0}{color=ffffff}{b} BAJAR {b}{/color} .{/glitch}":
                jump badend_nulla1

        
    
    label badend_nulla1:
        scene hotelcomedor
        "Decides bajar a inspeccionar el lugar, tal vez habrá una salida por allá."
        scene negro with dissolve

        stop music fadeout 3.0

        "El lugar es oscuro, apenas puedes ver como tus pies bajar escalón tras escalón."
        "Al llegar al final de la escalera te encuentras con una puerta. Pruebas tu suerte tocando y accionando la manilla."
        "La puerta se abre sin mucha dificultad."
        scene hotelfreezer with dissolve
        scene hotelfreezer with vpunch

        play music "audio/the_chillout_factory.WAV" volume 0.2

        "Te sobresaltas al encontrar que en este lugar hay cuerpos colgados."
        "Sin querer mirar más te dispones a correr de ahí. Pero chocas con un cuerpo duro."
        nulla "¿Quién te ha dado permiso de venir aquí?"
        scene badendnull with dissolve
        nulla "No estás realizando lo que te piden."
        nulla "No puedo arriesgar mi reputación ni la de Madre."
        nulla "Madre no hace criaturas fallidas."
        nulla "Ni yo aguanto aprendices incompetentes."
        "Nulla apunta con su pistola en tu frente, y sin pena acciona el gatillo."
        scene badendnull with vpunch
        scene negro with Dissolve(2.0)
        "..."

        "BAD END"

    $ MainMenu(confirm=False)()





    #BAD ENDINGS
    #BAD ENDINGS
    
    
    label respuesta7:
        "No deberías arriesgarte a escapar. Es mejor hacer lo que te pidieron y actuar con normalidad."

    return







    #RUTAS
    #RUTAS
    


    label rutaunum:

        stop music fadeout 2.0

        scene hotelcomedor
        "{sc=2}Bien, lo has hecho bien...{/sc}"
        "{sc=2}Ahora viene lo difícil, si quieres sobrevivir para cuando comience la reunión-{/sc}" 
        "{sc=2}deberás lograr que te tomen como aprendiz.{/sc}"
        "{sc=2}De lo contrario, el cuerpo de tu marioneta será devorado.{/sc}"
        show unumcercanormal at center with dissolve

        play music "audio/mechanique.mp3" fadein 2.0 volume 0.2 

        el " ¡eh! Por poco se me olvida decirte mi nombre"
        hide unumcercanormal
        show unumcercarisa at center
        unum "Mi nombre es Unum."
        hide unumcercarisa
        scene hotelcomedor with Dissolve(2)
        septem "{sc=2} Nulla puedes sellar la mesa ahora.{/sc}"
        "En cuestión de segundos dejas de ver a Septem y a Nulla, quedándote solamente con Unum en la mesa."
        "Él te hace un gesto indicándote que puedes tomar asiento frente de él."
        "Debes pensártelo un poco..."

        menu:
            ">Sentarte e intentar que te tome de aprendiz.":
                "Okay, realmente no quieres morir... llámalo instinto o lo que quieras, pero no piensas quedarte de brazos cruzados esperando a tu final."
                "Y si lamerle las botas a este payaso te dará la posibilidad de salir, pues la tomarás."
            

            ">No sentarte y escapar":
                jump badend_unum1
            

            ">Preguntar por lo que quiere.":
                nj "¿Qué es lo que quieres?"

                show unumcercarisa at center with dissolve
                unum "Solamente conversar y comprobar una teoría... y quizás averiguar si es cierto lo que dice Quattor de los regalos..."
                nj "¿Qué cosa?"

                hide unumcercarisa
                show unumcercanormal at center
                unum "Que son la combinación de las 6 personas elegidas en el festival de las velas."
                "Dudas que Quattor esté en lo correcto... pero si así lo fuera. tu marioneta sería una amalgama de diferentes personas."
                "... como la carne molida."
                "El solo pensarlo te da asco."

                hide unumcercanormal
                show unumcercaexaltado at center
                unum "Bueno, siéntate, no tenemos todo el día." 
                hide unumcercaexaltado
            
        
        
        

        "Puedes estar en una peor situación... asi que sentarse un rato no haría mal."
        "Después de todo, te duelen un poco las piernas de tanto ir de aquí para allá."
        show unumcercarisa at center
        "Con cautela te sientas al frente de Unum, quien te soníe de oreja a oreja, feliz de que le hayas hecho caso sin mucha protesta."
        "Cuando te acomodas en tu puesto, caes en cuenta..."
        "...bueno, no estás seguro de que hacer o decir... o que no decir"
        hide unumcercarisa

        "Por lo que tienes tres opciones..."

        menu:
            ">Esperar a que él rompa el hielo.":
                "Crees que es lo más seguro, esperar a que él comience la conversación."
                "Pero temes que esto no le guste..."
                "Aunque de todos modos no se te ocurre que decir, asi que-"
                "Aceptas tu destino, sea el que sea."
                "Unum espera un buen rato antes de hablar, decide comenzar a cortar el pedazo de carne que has traído anteriormente."
                show unumcercabocado with dissolve
                "Lentamente se lo lleva a la boca"
                hide unumcercabocado
                show unumcercabocado2 at center
                unum "Sé mi sujeto de pruebas"
                "..."


            ">Suplicar por tu vida.":
                "Decides que suplicar por tu vida como un maldito gusano, es lo más sensato."
                "Pues realmente no sabes que otra cosa hacer, y la vergüenza se ha esfumado desde que aceptaste descargar este juego."
                "Y para poner más dramatismo a tu súplica, juntas las manos y pones cara de perro abandonado."
                nj "Poor favooorrrr, no dejes que me devoren."
                nj "Haré lo que seaaaa--------"
                "{sc=2}Diablos, ¿a eso llamas una súplica? -10/10{/sc}"
                show unumcercaserio at center with dissolve

                unum "..."
                hide unumcercaserio
                show unumcercaexaltado at center
                unum "JAJAJAJAJAJAJA"
                "Al parecer a él le ha hecho gracia, y hasta ahora no tienes ninguna extremidad rota."
                "Una pequeña victoria para tí."
                "En eso, Unum se toma el tiempo para responder. Sinceramente crees que lo hace a propósito."
                hide unumcercaexaltado
                show unumcercabocado

                "Porque el muy detestable, comienza a cortar el pedazo de carne que habías traido."
                "..."
                "Y lentamente, lo lleva a su boca"
                hide unumcercabocado
                show unumcercabocado2 at center
                unum "¿Lo que sea?"
                nj "Sí"
                unum "Sé mi sujeto de pruebas"
                "..."








            ">Empezar a parlotear":
                scene hotelcomedor
                "Sin darle más vueltas al asunto, decides empezar a parlotear sobre tu nueva hiperfijación."
                "Le cuentas sin mucha verguenza (pues esa la decidiste dejar cuando aceptaste descargar este juego) desde los datos más minusculos y rebuscados"
                "Hasta los más perturbadores e íntimos."
                "Hablas hasta por los codos sin darte cuenta, piensas que es como si estuvieras hablando con un amigo que comparte tus extraños gustos."
                "Pero hasta ahora no te dignas en mirar su reacción."
                "Llega un punto en que parloteas tanto, que piensas que se te va a enredar la lengua."
                "Es ahí cuando decides tomar un respiro y cerrar la boca."
                "Con miedo, levantas la mirada para observar la reacción de Unum."
                show unumcercaencantado at center with Dissolve (2)
                "Él te mira con la boca abierta, casi que fascinado... Dándose cuenta de tu silencio, habla."
                unum "Vamos [nombrejugador], continúa."
                "No te esperabas esa reacción, pero eso significa que lo estás haciendo bien... y que tal vez, termines por convertir a Unum en un seguidor más de tu hiperfijación."
                "Si es que ya no lo has hecho."
                "Je- No suena nada mal."
                "..."
                "Luego de estar hablando eternamente de tu hiperfijación, te encuentras sin nada más que decir... por lo que Unum te mira por un rato."
                "Unum espera un buen rato antes de comenzar a cortar el pedazo de carne que has traído anteriormente, el cual seguramente ya ha de estar frío."
                hide unumcercaencantado
                show unumcercabocado
                "Lentamente se lo lleva a la boca"
                hide unumcercabocado
                show unumcercabocado2 at center
                unum "Sé mi sujeto de pruebas"
                "..."

    
        scene hotelcomedor
        "No te queda de otra que aceptar ser su sujeto de pruebas pero..."
        "No sabes si confiar en él o no. Hasta ahora no ha hecho más que tomarse todo a la ligera. ¿Qué te garantiza a ti que no te esté engañando?"
        show unumcercanormal at center with dissolve
        unum "¿Aceptas? Necesito que respondas rápido antes de que Septem pida que quiten el sello."
        hide unumcercanormal
        show unumcercarisa
        unum "Si aceptas, te llevaré a mi dominio jeje-"
        menu:
            "Aceptar":
                nj "Está bien. Iré contigo"
                unum "JAJAJAJAJAJAJA-"
                unum "Prometo no romperte tan rápidooo."
                "De verdad no sabes donde mierda te has metido... tal vez Septem hubiera sido mejor opción."


            "Rechazar":
                nj "No quiero ir contigo."
                hide unumcercarisa
                show unumcercaexaltado
                unum "JAJAJAJA-"
                unum "Como quieras."
                jump badend_cena
        
        hide unumcercarisa
        show unumcercaexaltado
        unum "Bien. Cuando Nulla saque el sello, debes quedarte inmóvil."
        
        "Asientes con la cabeza... No alcanzan a pasar ni 3 segundos cuando sientes una presión extraña en tu cuerpo... supones que debe ser Nulla."
        play music "audio/calamity.WAV" fadein 2.0 volume 0.4
        scene hotelcomedor with pixellate
        show nulla1normal at right
        show septem1normal at left
        "Nulla y Septem se materializan justo donde los viste la última vez, Nulla parado a un lado de la mesa y Septem sentado al lado de Unum."
        "Como si hubieran estado siempre allí."
        hide septem1normal
        show septem2risa at left
        septem "{sc=2}Wow, no creí que el regalo saldría en una sola pieza. Te felici---{/sc}"
        "Septem es interrumpido por Unum, quien se abalanza contra ti."
        hide septem2risa with dissolve
        scene hotelcomedor with dissolve
        "Si no fuera por la rapidez con que Unum te ha alcanzado, de seguro te habrías movido para evitarlo. Pero como tus reflejos son lentos comparado con Unum, te quedas como una piedra."
        "Los brazos de Unum te envuelven y te quitan el aire de lo fuerte que te está apretando."
        septem "{sc=4}Qué mier-{/sc}"
        "Repentinamente dejas de escuchar la voz de Septem y el sonido ambiental del comedor."
        stop music fadeout 2.0
        scene negro with pixellate
        "..."
        "....."
        #PONER ESCENA PALACIOUNUM
        "La sensación de unas manos acariciándote la cara, te invitan a dejar tu subconsciente."
        scene piezaunumborroso with Dissolve(2)
        "Abres los ojos, pero la luz del lugar te lo impiden. Son molestas."
        scene negro with dissolve
        "... No sabes cuanto tiempo has estado inconsciente."
        play music "audio/hope.WAV" fadein 2.0 volume 0.4
        "Sientes como las mismas manos te dan palmaditas en las mejillas, cada vez más fuertes con el pasar de los segundos."
        "Una lo suficientemente fuerte como para doler te hace gritar." 
        scene piezaunum0 with dissolve
        "Abres los ojos de golpe y lo primero que vez es a Unum con su risa estúpida."
        nj "¡QUE PARES YA!"
        scene piezaunum1
        "Gritas con tanto enojo que Unum para en seco y te mira con los ojos bien abiertos."
        scene piezaunum0
        unum "JAJAJAAJAJAJAJAJAJA- Tienes receptores de dolor"
        unum "Excelente, parece ser que el olor que emanas está en lo correcto."
        unum "Perteneces a la raza humana."
        scene piezaunum2 with dissolve
        "La expresión de Unum demuestra lo exaltado que está, cosa que no te agrada mucho pues sabes por experiencia propia que eso no lleva a nada bueno."
        "Decides que es mejor no hacer que se exalte más de lo necesario, por lo que le ignoras para poder observar tu alrededor."
        "Te encuentras en una cama lo suficientemente amplia como para dos personas, en una habitación, que siendo sinceros, podría ser la de un rey."
        "Está tan inmaculado el lugar que no se ve real."
        scene piezaunum
        unum "¿Te gusta?"
        unum "Esta será tu propia habitación."
        scene piezaunum3
        unum "Lo estuve pensando, y supongo que sería imposible dejarte en la residencia de mis esposas."
        unum "Te devorarían nada más pisar el lugar."
        "¿Esposas? No solo una ¿¿¿¿¿sino que más????"
        "No puedes evitar sentir pena por las pobres mujeres que tienen de pareja a este niñato."
        "Sientes que seguramente no les dedica el tiempo necesario a cada una de ellas."
        unum "...Hablé con Septem, y Nulla le ha dicho que Madre hará otro regalo para que los demás puedan tener su parte."
        unum "Eso significa que eres de mi propiedad ahora..."
        scene piezaunum
        unum "¡Primera vez que tengo a un humano vivo en mi dominio!"
        menu:
            "Preguntar porqué no puede tener humanos vivos.":
                nj "¿Por qué no pueden haber humanos vivos en tu dominio?"
                scene piezaunum4
                "Unum analiza tu cara por un momento antes de contestar, como si meditara el tipo de información que te revelará."
                scene piezaunum3
                unum "Nulla y Madre dicen que solamente pueden haber humanos para nuestro consumo."
                unum "Nulla se excusa con que no nos puede facilitar ninguno pues solamente podemos tener 6 humanos cada mes..."
                unum "No más que eso."
                unum "Por eso Madre hace un regalo cada domingo... como placebo, ya que la carne humana es vital para nuestra forma física pero muy adictiva."
                "Tú eres el placebo."
                scene piezaunum
                unum "Aunque es la primera vez que un regalo huele como un humano real."

                menu:
                    "Preguntar por Madre":
                        nj "¿Quién es Madre?"
                        scene piezaunum2
                        unum "Ja... realmente madre no te ha hecho como a los demás."
                        scene piezaunum4
                        unum "Hmmmmmm"
                        "Unum medita antes de contestar"
                        scene piezaunum3
                        unum "Madre es la representación del jardín mismo, todo esto es Madre."
                        unum "Madre cuida de nosotros y nosotros la mantenemos a con vida."
                        "Supones que ahora entiendes algo más... es como una relación de mutualismo, ambas partes se benefician."


                    
                    "No preguntar nada más":
                        "Decides no preguntar nada más."

            "Preguntar por Madre":
                nj "¿Quién es Madre?"
                scene piezaunum2
                unum "Realmente Madre no te ha hecho como a los demás."
                scene piezaunum4
                unum "Hmmmm"
                "Unum medita antes de contestar"
                scene piezaunum3
                unum "Madre es la representación del jardín mismo, todo esto es Madre."
                unum "Madre cuida de nosotros y nosotros la mantenemos a con vida."
                "Supones que ahora entiendes algo más... es como una relación de mutualismo, ambas partes se benefician."

                menu:
                    "Preguntar porqué no puede tener humanos vivos.":
                        nj "¿Por qué no pueden haber humanos vivos en tu dominio?"
                        scene piezaunum4
                        "Unum analiza tu cara por un momento antes de contestar, como si meditara el tipo de información que te revelará."
                        scene piezaunum3
                        unum "Nulla y Madre dicen que solamente pueden haber humanos para nuestro consumo."
                        unum "Nulla se excusa con que no nos puede facilitar ninguno pues solamente podemos tener 6 humanos cada mes..."
                        unum "No más que eso."
                        unum "Por eso Madre hace un regalo cada domingo... como placebo, ya que la carne humana es vital para nuestra forma física pero muy adictiva."
                        "Tú eres el placebo."
                        scene piezaunum
                        unum "Aunque es la primera vez que un regalo huele como un humano."
                    
                    "No preguntar nada más":
                        "Decides no preguntar nada más."

            "No preguntar nada":
                "Decides no preguntar nada."

        scene piezaunum2
        unum "Bien, debes tener hambre. Leí por ahí que los humanos tienen horarios para comer, y que comen más de una vez al día."
        scene piezaunum3
        unum "Aunque Septem también lo hace todo el tiempo. Las veces que he estado en su dominio, él se sienta en la mesa en las mañanas, tardes y noches a comer."
        unum "Le he preguntado porqué lo hace, pero siempre me dice que no me concierne."
        unum "Nulla también lo hace a veces... tal vez esa sea la razón por la que son tan fuertes los dos..."
        scene piezaunum
        unum "No lo necesito... pero puede que hasta yo lo intente ahora que estás aquí conmigo."
        scene piezaunum4
        "Por alguna razón, se te hace algo tierno que te hable con tanta libertad, como a un viejo amigo... y el hecho de que haya estado leyendo información acerca de los humanos, te hace pensar... Quizás cuanto tiempo haya estado planeando tener uno..."
        "Te hace sentir como una mascota a la cual su dueño le habla luego de llegar a casa del trabajo." 
        scene piezaunum
        unum "Camina detrás de mí y no te separes, mis esposas les gusta venir a mi residencia para relajarse."
        "Escapar parece no ser opción por ahora... no quieres morir en el intento."
        scene habitacion with dissolve
        "Él se aleja de la cama en que estás y te espera en la puerta. Tú te levantas y así comienzas a seguir a Unum por los pasillos, caminas tan cerca de Unum que casi le pisas los talones."
        scene pasillounum with dissolve
        "Tardan en llegar al lugar deseado, siempre bajo un silencio que no es ni cómodo o incómodo."
        scene cocinaunum with dissolve
        show unum2feliz with Dissolve(2)
        unum "Cocina algo para dos. Puedes usar lo que gustes todo lo de aquí es comestible."
        hide unum2feliz
        show unum2enojo
        unum "Yo no sé cocinar."
        hide unum2enojo
        show unum3risa
        unum "Te esperaré en el comedor."
        hide unum3risa with Dissolve(2)
        "Sin decir más, Unum desaparece de la cocina y te deja a solas."
        "Miras tu alrededor mientras inspeccionas cada rincón del lugar, hay encimeras, despensas con alimentos y un refrigerador lleno de carne, frutas y verduras."
        "Te preguntas por qué tienen tanta comida si Unum ha dicho que no la necesita."
        menu:
            "Escapar":
                jump badendunum2
            
            "Preguntar lo que le gustaría comer":
                "Con algo de verguenza vas en dirección a la puerta por donde Unum se ha esfumado."
                scene pasillounum with dissolve
                "Te asomas con cuidado, buscándolo con la mirada."
                "No hay nadie..."
                unum "¿Qué pasa?"
                scene cocinaunum
                show unum1normal with dissolve
                "Pregunta Unum apareciendo detrás tuyo. Tú saltas del susto que te ha causado pero te recompones rápido."
                nj "¿Hay algo en especial que quieras comer?"
                hide unum1normal
                show unum3serio
                "Unum te mira abatido, cómo si se esperara cualquier pregunta menos la que acaba de salir de tu boca."
                unum "Ah..."
                hide unum3serio
                show unum2duda
                unum "Hmmmmm."
                unum "Nulla come unas cosas que son blanditas y esponjosas con un liquido color oro que le derrama encima."
                unum "...Me gustaría probarlos"
                hide unum2duda with dissolve
                "Se oye algo avergonzado de decirlo..." 
                "Okay, crees saber a lo que se refiere. Claramente son panqueques por la descripción dada."
                "Comienzas a preparar los panqueques bajo la mirada curiosa de Unum, que mira con fascinación como haces la preparación. De vez en cuando te da la sensación de que tal vez quiere ayudar, pero decides ignorarlo."

            "Cocinar algo simple":
                "Revuelves la cocina en busca de ingredientes para cocinar algo simple."
                "Algo para saciar el hambre solamente."
                "No tardas mucho en terminar."

        scene palaciounum with dissolve
        "Llevas los platos a la mesa y te das cuenta de que, a diferencia del resto del lugar, la mesa es pequeña y simple, donde solo caben 2 personas."
        show unumcercabocado2 with dissolve
        "Te sientas una vez Unum ya tiene su plato al frente. Él no te espera para comenzar a comer, optando por tragar la comida nada más estar puesta en la mesa."
        "Lo devora todo muy rápido, impidiendo ver si le ha gustado o no, pues su expresión no refleja nada más que neutralidad... cómo si el sabor o la comida en sí no le interesara."
        hide unumcercabocado2
        show unumcercarisa
        unum "Gracias por la comida."
        "Es tu única respuesta.... dios, de verdad te habías esforzado." 
        hide unumcercarisa
        scene negro with dissolve
        "Suspirando, te resignas a comer tu plato. Cierras los ojos al llevarte el primer bocado a la boca."
        "Está rico."
        "Comes lento y sin prisa. Bocado tras bocado, tomas pausas para respirar."
        "Pero algo no te deja en paz. La sensación de que te están observando te revuelve el estómago."
        scene palaciounum with Dissolve(2)
        "Tus ojos viajan por si solos al frente, donde Unum está sentado y confirmas tu sospecha, él te está mirando."
        show unumcercaexaltado with dissolve
        unum "Es fascinante..."
        unum "Tu cuerpo cambia en todo momento, nunca está igual."
        unum "Desde la respiración hasta el latido de tu corazón."
        "No te gusta para nada como te está mirando ni el tono de su voz."
        nj "¿Que quieres decir?"
        unum "Quiero saber más..."
        unum "Ahh--"
        stop music fadeout 2.0
        scene palaciounum with vpunch
        play music "audio/mechanique.mp3" fadein 2.0 volume 0.4
        "Se escucha un estruendo, de sillas siendo tiradas al suelo."
        show unumpelea0 with vpunch
        "No eres capaz de procesar lo que está pasando hasta que tu espalda impacta contra la pared y a Unum tomándote del cuello de tu ropa."
        unum "NO SABES CUANTO TIEMPO HE ESPERADO PARA TENER ESTA OPORTUNIDAD."
        unum "SI ATRAVIESO TU PECHO Y TE SACO ALGUNO DE TUS ÓRGANOS QUE NO SEA EL CORAZÓN O EL CEREBRO---" 
        unum "¿CÚANTO TARDARÁ TU CUERPO EN APAGARSE?"
        unum "Y SI~ TE QUITO LA LENGUA ¿PODRÁS SEGUIR COMIENDO O SIQUIERA HABLAR?"
        unum "¿HMM?"
        unum "¿QUÉ NIVEL DE DAÑO TIENE QUE TENER TU CUERPO COMO PARA NO PODER REGENERARSE? ¿CÚAL ES EL LÍMITE?"
        unum "¿HHMMM?"
        "Tienes que hacer algo antes de que este loco te despedace."
        menu:
            "Luchar para liberarte":
                "Te rehúsas a dejarte matar."
                "Y con lagrimas que peligran por salir de tus ojos, tus piernas comienzan a tirar patadas y tus brazos intentan alejar a Unum. Algunos golpes hacen contacto con el cuerpo del pelirrojo, pero él no se ve afectado con ello."
                "Como si no doliera en absoluto."
                scene unumpelea1 with vpunch
                "Uno de tus brazos apunta directo a su cara, pero Unum lo detiene sin dificultad alguna."
                
            "Intentar que entre en razón":
                "Intentas hablar para hacerlo entrar en razón....  le dices que hay más cosas interesantes que puede hacer un humano estando vivo."
                "Le dices tantas cosas de manera errática que ni siquiera procesas que tipo de información o datos del cuerpo humano le estás soltando."
                "Pero parece funcionar, pues Unum solo le mira con atención... ya no tiene esa expresión exaltada de antes."
                "Sin previo aviso, Unum toma tu brazo con una extraña delicadeza"
                scene unumpelea1 with dissolve
                
            "Entrar en pánico y suplicar por tu vida":
                jump badendunum3
        
        "Unum te mira completamente serio mientras tú te retuerces en su agarre por el extraño cambio de ambiente que hay."
        "Su boca está peligrosamente cerca de tu brazo, tanto que puedes sentir el calor de sus labios rozar tu piel."
        "Te preparas mentalmente para que te arranque la extremidad con sus propios dientes.."
        scene unumpelea2 with dissolve
        unum "JAJAJAJAJAJA-"
        "..."
        unum "¡Desde aquí puedo sentir el latido de tu corazón! ¿¡Esto es lo que llaman pulso?!"
        unum "IMPRESIONANTE-"
        scene palaciounum with pixellate
        show unum2enojo with pixellate
        unum "Aunque- uhg!" 
        unum "No me gusta la sustancia que estás liberando ahora... uhggg está impregnada en todo tu cuerpo ahora."
        "Sin más, Unum te suelta y tú caes al suelo."
        "Te quedas ahí, sin mover un solo músculo mirando con terror Unum."
        hide unum2enojo
        show unum2duda
        unum "Ahora entiendo porque Nulla evita estresar a los humanos..."
        hide unum2duda
        show unum3serio
        "Él pone ambas manos en su cadera y suspira."
        unum "uhg, lo siento [nombrejugador], no era mi intensión asustarte."
        unum "Es solo que al no haber comido en el hotel, tengo mucha hambre."
        "No tiene que decirlo explícitamente para saber que se refiere a que no te ha podido comer allá en el hotel. Y supones que tampoco pudo comer el remplazo que Madre les dio a los demás, seguramente por quedarse aquí contigo."
        unum "Llevo esperando más de una semana por el placebo... y faltan 14 días para el próximo festival de las velas."
        hide unum3serio
        show unum3callado
        stop music fadeout 2.0
        unum "..."
        play music "audio/hope.WAV" fadein 2.0 volume 0.4
        nj "¿Aún tienes hambre? pero acabas de comer..."
        "Recién ha comido algo, ¿cómo es posible que tenga hambre?"
        hide unum3callado
        show unum1risa
        unum "Ah- los alimentos que tengo no me quitan el hambre, ni me saben a nada."
        hide unum1risa
        show unum3risa
        "Unum al ver que lo miras preguntando silenciosamente la razón del porqué tiene alimentos en su cocina, se aclara la garganta antes de responder con algo de pena."
        unum "A mis esposas por el contrario... gustan de cocinar y a mi me gusta verlas hacerlo así que no me quejo."
        "Mientras Unum habla, tú intentas calmar tus nervios. Claramente la deidad que tienes al frente es inestable... o al menos se pone inestable cuando se exalta."
        "Más no tienes otra opción que seguir y adaptarte para sobrevivir."
        "Ya que escapar no es opción a estas alturas."
        "Aunque te gustaría saber cual es tu verdadero propósito aquí."
        nj "Acerca de convertirme en tu sujeto de pruebas..."
        hide unum3risa
        show unum3serio
        unum "Podemos hablar de eso mañana."
        nj "No"
        "Dices firme. Quieres saber si ser su sujeto de pruebas te permitirá sobrevivir a costa de tu sanidad fisica o mental."
        "En ese caso... realmente prefieres que te mate de una buena vez. Después de todo, puedes volver a intentar sobrevivir con Septem... {glitch=20.0}{color=ffffff}{b}o Nulla{/glitch}"
        nj "Si me convierto en tu sujeto de pruebas, necesito saber con antelación que pruebas harás."
        hide unum3serio
        show unum3blush
        unum "Oh--ja- jajaja-"
        hide unum3blush
        show unum3callado
        unum "..."
        "Se le nota algo incómodo."
        hide unum3callado
        show unum1incomodo
        unum "he- He leído que los humanos pueden crear- uh... algo parecido a lo que hizo el creador, pero diferente..."
        hide unum1incomodo
        show unum3blush
        unum "Es algo progresivo, que no va desde la nada a un todo al instante."
        "Intentas comprender a lo que se refiere pero no se te viene nada a la cabeza, pues su explicación es algo vaga."
        hide unum3blush
        show unum3callado
        "Unum viendo tu silencio, corre la mirada. Y te das cuenta que tiene sus orejas rojas, dudas que sea de rabia."
        hide unum3callado
        show unum3serio
        unum "... Mañana hablamos."
        unum "Cerraré la residencia para que nadie pueda entrar."
        unum "Eres libre de recorrer el lugar y hacer lo que se te plazca."
        hide unum3serio with dissolve
        "Con eso Unum te deja, desapareciendo en el lugar."
        "..."
        menu:
            "Explorar":
                call menuexplorar from _call_menuexplorar
            
            "Ir a tu habitación":
                pass
        

        "Decides que es hora de terminar por hoy, descansar en la habitación que Unum te dio no parece mala idea."
        scene piezasinunumnoche with dissolve
        "Mañana será un nuevo día."
        "Te acuestas en la cama, e intentas conciliar el sueño."
        "Te cuesta un poco, pero al final lo logras."
        scene negro with Dissolve(4)
        "..."
        "... no sueñas nada"
        
        scene piezaunumborroso2 with dissolve
        "Abres los ojos con pesadez, sientes que no has podido descansar nada."
        "Nada en absoluto."
        unum "Por fin despiertas."
        "Su voz hace que tus ojos se enfoquen."
        scene piezaunum1_1 with dissolve
        "Y lo encuentras sentado en la orilla de la cama. Mirándote con los ojos bien abiertos."
        scene piezaunum1_2
        unum "Te he hecho alimento de la mañana."
        "Con una sonrisa llena de dientes afilados, Unum te presenta una bandeja con fruta y una copia mal hecha de lo que preparaste ayer."
        "Unum se ve orgulloso de mostrar el desayuno, pero-"
        "Mientras más miras lo que tiene entre las manos, más imperfecciones vez."
        "Se nota que no tiene idea de como preparar comida."
        "Unum te ofrece la bandeja y debes tomar una decisión"
        menu:
            "Aceptar y comerlo":
                "No te da el corazón para rechazarlo."
                "Con miedo te preparas para comer lo que tienes en la bandeja."
                "La fruta claramente no sabrá mal... lo que ha cocinado Unum en cambio-"
                "Independiente de como sepa o se vea, te lo vas a comer."
                scene piezaunum1_3
                "Intentas poner tu mejor cara al comer, pero el sabor de esta cosa te lo pone difícil."
                "Pero debes hacerlo pues Unum te mira con una sonrisa de oreja a oreja mientras comes."
                "..."

            "Rechazar la comida":
                "Le dices que no tienes hambre por ahora."
                unum "Pero debes comer en la mañana, tarde y noche."
                unum "Sin eso no puedes vivir."
                "¿Entonces Unum hace esto para mantenerte con vida? increíble."
                nj "No es necesario."
                scene piezaunum1_4
                unum "Oh-"
                "Se oye decepcionado."
                "..."
        
        scene piezaunum with dissolve
        "Se quedan en la habitación por unos minutos, Unum a los pies de la cama y tú mirando por la ventana con barrotes."
        scene piezaunum3
        unum "Duae ha venido de visita..."
        "¿Quién mierda será Duae? no tienes idea, pero al parecer Unum no es capaz de guardar silencio por un periodo largo de tiempo."
        "Y tiene la necesidad de explicarse cada que puede."
        "Tampoco es de los que se guarda nada."
        scene piezaunum2
        unum "Me ha pasado las sobras del placebo que Madre llevó al hotel."
        unum "Por ende podremos llevar a cabo el experimento sin problemas."
        nj "¿Cuál es el experimento?"
        unum "Quiero crear un hibrido."
        scene piezaunum4
        "..."
        "............"
        "......................................."
        play music "audio/mechanique.mp3" fadein 2.0 volume 0.4
        "¡¿UN QUÉEEEEE?!"
        scene habitacion with vpunch
        "LLegas a saltar de la cama por lo bizarro de la situación."
        show unum2feliz with dissolve
        unum "He leído que los humanos pasan por un ciclo que los tiene en un constante cambio, y gracias a eso son capaces de engendrar descendientes."
        unum "Que son seres que no son una copia exacta de ellos."
        hide unum2feliz
        show unum3serio
        unum "A diferencia de nosotros."
        unum "No importa cuantas veces lo intente, nuestra composición no nos permite crear descendientes con los nuestros."
        unum "Entonces comencé a leer los documentos que tiene Septem de los humanos."
        hide unum3serio
        show unum2blush
        unum "Y... Existe data de un nacimiento ocurrido un domingo... "
        unum "Hijo de Septem y un humano."
        hide unum2blush with dissolve
        unum "..."
        show unummanos with dissolve
        "Unum se acerca a ti para poder tomarte las manos y cubrirlas con las suyas, implorando por tu complicidad."
        "Tú no te lo puedes creer."
        unum "Si aceptas, juro que te cuidaré y vivirás con todas las comodidades posibles."
        unum "Por favor..."

        menu:
            "Aceptar":
                pass

            "Rechazar":
                jump badendunum5

            "Apuñalar a Unum" if cuchillo_unum:
                jump badendunum4
        
        nj "..."
        "No sabes en lo que te estás metiendo, tampoco tienes idea de como será el procedimiento..."
        "Pero bajo la promesa de que podrás vivir, harás lo que sea."
        nj "Está bien. Hagámoslo."
        hide unummanos
        show unummanossorprendido
        unum "..."
        "Unum te mira con la boca abierta, procesando lo que acaba de salir de tu boca."
        stop music fadeout 2.0
        play music "audio/fell.mp3" fadein 2.0 volume 0.4
        "Y como si una ampolleta se encendiera dentro de su cabeza, Unum te toma de las mejillas y choca su boca con la tuya."
        hide unummanossorprendido
        show unummanosamor
        "Sus manos comienzas a bajar paulatinamente por tu cuerpo, desde tus mejillas hasta tus caderas y muslos."
        unum "Te amo"
        "Wow, alto, alto alto! está yendo muy rápido, y no es por invalidad los sentimientos o palabras del pelirrojo, pero... no crees que lo diga en serio."
        "Es decir, a penas te conoce por unos días..."
        unum "Te he deseado desde que te vi en el hotel... te amo, te amo, te amoo mucho."
        "Joderrr, está loquito. Pero no nos hagamos los desentendidos... eso te gusta."
        "Luego, repentinamente Unum para."
        hide unummanosamor
        show unummanosblush
        unum "Ah-- Mierda..."
        unum "Se me ha olvidado el consentimiento..."
        unum "Creo que es algo importante para ustedes..."
        "Efectivamente, es importante. Tienes que darle puntos por tener eso en cuenta."
        unum "¿Podemos proceder?"

        menu: 
            "Seguir":
                nj "Está bien."
                hide unummanosblush
                show unumesencia1
                "Unum atraviesa su pecho con la mano de manera lenta."
                "Y con delicadeza, la retira con algo brillante en su mano."
                hide unumesencia1
                show unumesencia2
                "Es una esfera transparente que gotea un líquido parecido al oro."
                unum "Tengo que colocar esto dentro de tu pecho y luego retirarlo."
                unum "Es mi esencia... así que debemos hacerlo con cuidado..."
                "Dice sonriendo con ternura."
                "...Probablemente Unum no esté pensando en lo que tu estabas pensando, después de todo, Unum no es humano..."
                menu:
                    "Aceptar":
                        show unumesencia1
                        "Unum atraviesa su pecho con la mano de manera lenta."
                        "Y con delicadeza, la retira con algo brillante en su mano."
                        hide unumesencia1
                        show unumesencia2
                        "Es una esfera transparente que gotea un líquido parecido al oro."
                        "Tú no entiendes por qué ha hecho eso, pero supones que efectivamente, Unum tiene pensado otra manera."
                        unum "No te dolerá."
                        call nogogogo from _call_nogogogo
                    
                    "Usar el cuchillo para romper la esencia" if cuchillo_unum:
                        jump goodend1
            
            "Preguntar":
                "Piensas que probablemente no estén pensando en lo mismo..."
                "Así que decides preguntar con algo de vergüenza."
                nj "¿Cómo lo haríamos?"
                hide unummanosblush
                show unummanos
                unum "Ah! es muy facil."
                unum "Por lo que leí, Septem prefirió usar este modo..."
                unum "Debo combinar tu alma con la mía."
                hide unummanos
                show unumesencia1
                "Unum atraviesa su pecho con la mano de manera lenta."
                "Y con delicadeza, la retira con algo brillante en su mano."
                hide unumesencia1
                show unumesencia2
                "Es una esfera transparente que gotea un líquido parecido al oro."
                unum "Tengo que colocar esto dentro de tu pecho y luego retirarlo."
                unum "Es mi esencia... así que debemos hacerlo con cuidado..."
                "Dice sonriendo con ternura."
                unum "No te dolerá."

                menu:
                    "Aceptar":
                        call nogogogo from _call_nogogogo_1
                    
                    
                    "Usar el cuchillo para romper la esencia" if cuchillo_unum:
                        jump goodend1
            
        scene habitacion with dissolve
        "Sientes tu cuerpo pesado, como si hubieras corrido 4 kilometros sin descanso..."
        "Es extraño, como si te hubieran sacado parte de tu cuerpo, alguna parte importante."
        "Pero estás completo."
        "No hay nada faltante."
        "..."
        unum "Si quieres puedes descansar aquí un rato."
        "Dice Unum mientras aparece nuevamente en la habitación y se acomoda en la cama."
        "...Decides recostarte por un rato, y sin darte cuenta, cierras los ojos por un momento."
        scene negro with dissolve
        stop music fadeout 2.0
        play music "audio/woo_scary.WAV" fadein 2.0 volume 0.6
        "..."
        "{sc=4}{b}....{b}{/sc}"
        "{sc=4}{b}Veo que has ingerido alimentos no santificados...{b}{/sc}"
        "{sc=4}{b}Dentro de ti hay veneno que se está esparciendo de a poco.{b}{/sc}"
        "{sc=4}{b}Mil disculpas, no puedo controlar como es consumido mis frutos.{b}{/sc}"
        "{sc=4}{b}Unum es un idiota...{b}{/sc}"
        "..."
        stop music fadeout 3.0
        "!!!"
        play music "audio/hope.WAV" fadein 2.0 volume 0.4
        "Despiertas repentinamente, sintiendo una gota de sudor frío recorriendo tu cuello."
        scene unumcama with dissolve
        "Y lo primero que te encuentras es a Unum mirándote de cerca, casi que inspeccionándote."
        scene unumcama2 
        unum "Tu respiración es constante cuando descansas."
        unum "Impresionante."
        "Sinceramente, prefieres que haga este tipo de comentarios a que le den los 5 minutos de locura y quiera romperte en pedazos para saber como funciona tu cuerpo."
        nj "¿Me has estado mirando mientras duermo?"  
        unum "...¿Si?"
        scene unumcama3 
        unum "¿Está prohibido hacerlo?"
        nj "No pero..."
        "Te detienes cuando sientes que tu estómago se te revuelve."
        stop music fadeout 2.0
        "Algo dentro de ti quema."
        scene habitacion with vpunch
        "Te levantas rápidamente, pensando que vomitarás."
        play music "audio/europalce.WAV" fadein 2.0 volume 0.4
        "Pero lo único que sale de tu boca son pétalos color rojo, mezclados con sangre."
        "...¿Qué?"
        "Los miras con detenimiento... parecen tener un símbolo extraño."
        show unum2duda at left with dissolve
        unum "¿Qué es eso?"
        "No tienes tiempo para pensar por un momento pues un ataque de tos te detiene."
        "Algo te raspa la garganta."
        hide unum2duda
        show unum3callado at left
        unum "¿[nombrejugador]?"
        ell "¿No me digas que le has dado comida?"
        show aeliana_serio at right with moveinright
        hide unum3callado
        show unum2blush at left
        unum "¿Aeliana?"
        hide aeliana_serio 
        show aeliana_feliz at right
        aeliana "Unum."
        hide aeliana_feliz
        show aeliana_serio at right
        hide unum2blush
        show unum3callado at left
        aeliana "Escuché de Ignis y Solaris que has estado preparando comida sin hacer el ritual de santificación."
        hide unum3callado
        show unum3blush at left
        unum "¿Qué?"
        hide unum3blush
        show unum3callado at left
        aeliana "Tienes que llamar a Sextam sino quieres que esta cosa se muera."
        hide unum3callado 
        show unum3blush at left
        unum "Pero Sextam está en la iglesia..."
        aeliana "...Tienes razón."
        aeliana "¿Y Quinque?"
        hide unum3blush
        show unum2enojo at left
        unum "¡Está enojado conmigo!"
        hide aeliana_serio
        show aeliana_feliz at right
        aeliana "Seguro que vendrá..."
        hide aeliana_feliz and unum2enojo with dissolve
        scene habitacion with dissolve
        "No estás entendiendo nada."
        "Y tu cuerpo no pide nada más que expulsar lo que tienes en la garganta, pero a pesar de que estás tosiendo de manera constante, nada sale."
        "Te estás ahogando."
        "Y ya no puedes aguantar más."
        aeliana "ah- ¡Cuidado!"
        scene habitacion with vpunch
        "La mujer intenta ir hacia ti pero no alcanza a atraparte cuando caes de la cama al piso."
        "El golpe es fuerte, provocando que te duelan los huesos."
        "El aire que entra a tus pulmones no es suficiente como para mantenerte consciente."
        scene negro with dissolve
        "... Caes inconsciente."
        "Sientes como manos te agarran por la fuerza, intentando hundirte."
        "Pero algo te lo impide."
        scene negro with vpunch
        "Una electricidad recorre tu cuerpo."
        scene unum_quinqueborroso with dissolve
        "Abres los ojos pero la luz es demasiado brillante."
        scene negro with dissolve
        unum "¿Se va a morir?"
        "Se escucha la voz de Unum a lo lejos."
        el "Cómo se te muera este y me eches de nuevo la culpa..."
        unum "¡Ya te pedí disculpas!"
        el "¡Solamente porque la señorita Ignis te ha dicho que lo hicieras!"
        scene unum_quinque1 with dissolve
        "Los gritos son lo que te traen devuelta a la vida."
        "Abres los ojos y lo primero que ves es a una entidad desconocida, la cual te tiene con una mano agarrando de los hombros, mientras que con la otra mano toca cuidadosamente tu estómago."
        el "¿Cómo mierda ha comido algo sin purificar?"
        unum "..."
        "Tu estómago se revuelve nuevamente cuando la mano de la entidad aprieta con suavidad una zona en específico."
        scene unum_quinque2 with vpunch
        "No puedes evitar dejar caer tu cuerpo para poder expulsar más pétalos de color rojo"
        el "Mierda-!"
        unum "... ¿Era necesario purificar los alimentos?"
        scene unum_quinque3 with vpunch
        el "¿TE FALTAN NEURONAS O ALGO?"
        el "Tria ha dicho un millón de veces de lo que está sucediendo con sus frutos. {sc=3}¿Y TÚ NO TIENES IDEA?{/sc}"
        el "{sc=4}¿TUS ESPOSAS NECESITAN COMER Y TÚ NO TIENES IDEAA?????{/sc}"
        scene unum_quinque4
        unum "Yo no sé cocinar... Ellas son las que cocinan."
        unum "Así que no sabía que hay que purificar los alimentos..."
        el "{sc=5}ERES UN TREMENDO PEDAZO DE INÚTIL!!{/sc}"
        "...."
        "Tus parpados no pueden mantenerse abiertos."
        scene negro with dissolve
        "Dejas de escuchar lo que está pasando para volver a caer en un sueño profundo."
        jump rutaunum2
        #scene negro with Dissolve(3)
        #"En proceso de elaboración..."
        #"{sc=2} Tendrás que esperar un poco para descubrir como acaba esto... :3{/sc}"
    

    return








 

    #RUTAS
    #menus estaticos:
#EDITAR


    label menuexplorar1_nulla:
        scene cocinanulla with dissolve
        menu:
            "Pedirle a Nulla pasar el tiempo contigo":
                "Buscas a Nulla por la casa... pero no logras dar con él."
                "No se encuentra ni en el primer o segundo piso."
                "Y el único lugar que se te ocurre es ir afuera."
                scene jardinnulla with dissolve
                "Recorres el lugar pero no hay nada."
                menu:
                    "Invocar su nombre":
                        "Tomas aire para llamar a su nombre."
                        nj "Nullaaaa."
                        
                    
                    "Dejar de buscar.":
                        "Supones que debe estar ocupado o en otro lugar fuera de su dominio..."
                        "Asi que das media vuelta y vuelves a la casa."
                        return

                "No obtienes respuesta."
                "Wow eso sonó bastante incómodo... más aún cuando Nulla no muestra signos de aparecer."
                "..."
                "Esperas un poco más."
                nj "¡Nulla!"
                "Subes un poco más la voz, al punto de gritar."
                scene jardinnulla with vpunch
                show nulla2normal with dissolve
                nulla "¿Necesitas algo?"
                "Nulla aparece detrás tuyo, lo que provoca que te tome desprevenido y pegues un salto."
                hide nulla2normal
                show nulla1risa
                nulla "Ja-- la marioneta se ha asustado..."
                nulla "[nombrejugador], ¿necesitas algo de mí?"
                menu:
                    "Quiero pasar el resto del día contigo.":
                        pass
                hide nulla1risa
                show nulla2blush
                nulla "Oh."
                nulla "Me lo estás poniendo difícil..."
                hide nulla2blush
                show nulla1normal
                nulla "Pero no puedo decirte que no."
                hide nulla1normal
                show nulla1silencio
                "Hay un silencio largo antes de que Nulla se digne a responder."
                hide nulla1silencio
                show nulla3feliz
                nulla "Está bien"
                hide nulla3feliz
                show nulla2normal
                nulla "Podríamos pasar el día fuera de mi dominio... aquí no hay mucho que hacer..."
                nulla "¿Te parece?"
                scene jardinnulla with dissolve
                menu:
                    "{glitch=20.0}{color=ffffff}{b}Negarte no es opción, cariño.{/glitch}"

                    "{glitch=20.0}{color=ffffff}{b}SI.":
                        pass

                    "{glitch=20.0}{color=ffffff}{b}Claro que yesss{/glitch}":
                        pass

                    "{glitch=20.0}{color=ffffff}{b}sí siisisisisi{/glitch}":
                        pass
                show nulla1risa
                nulla "Sabía que dirías que sí."
                hide nulla1risa
                show nulla1normal
                nulla "Ah y no te preocupes... saldremos sellados para que los demás no nos encuentren."
                nulla "Septem ya debe estar entrando en pánico, ja."
                "Nulla junta las manos y tu alrededor comienza a volverse negro y tus pies dejan de tocar suelo."
                scene negro with pixellate
                nulla "Hace mucho tiempo que no salía de mi dominio..."
                nulla "Bueno... la verdad es que hace mucho tiempo que ya no hago nada."
                stop music fadeout 4.0
                "No pasan más de 5 segundos cuando sientes tus pies tocar nuevamente el suelo. Y mientras el vacío se disipa puedes apreciar como de apoco se van construyendo estructuras y paisajes a tu alrededor."
                scene cafeteria_nulla with dissolve
                play music "audio/frozen_winter.WAV " fadein 2.0 volume 0.2
                "Se encuentran en una especie de café, con mesas llenas de gente tanto fuera como dentro del local."
                "Nulla sin prestarle atención a la gente decide dirigirse directamente a una de las mesas vacías que se encuentran fuera del local."
                "Tú le sigues por inercia, al llegar, él te dedica una sola mirada para confirmar que tiene tu atención."
                "Y como si las cosas aparecieran de la nada, la mesa se llena de dulces y dos tasas de té, las cuales emanan vapor por lo caliente que están."
                nulla "Adelante."
                "Te corre la silla para que puedas sentarte. Como todo un caballero."
                show nullacafe_mirando with dissolve
                "Una vez ya instalados, te das cuenta de que Nulla mira la calle con algo de nostalgia."
                hide nullacafe_mirando
                show nullacafe_normal
                nulla "Antes me gustaba pasearme por los dominios de los demás y observar a su gente..."
                nulla "Me preguntaba como sería ser ellos..."
                nulla "Que sueños o metas tienen, cual es su propósito."
                hide nullacafe_normal
                show nullacafe_normal2
                nulla "Ya no."
                nj "¿Y eso porqué?"
                hide nullacafe_normal2
                show nullacafe_normal
                nulla "Porque me di cuenta que no son nada más que una ilusión."
                nj "..."
                hide nullacafe_normal
                show nullacafe_suspiro
                "Nulla suspira."
                hide nullacafe_suspiro
                show nullacafe_enojado
                nulla "Están ahí para aparentar, no son entidades con conciencia propia."
                nulla "Solo una masa que sirve para decorar la escena."
                hide nullacafe_enojado
                show nullacafe2_mirada
                stop music fadeout 3.0
                "Nulla despega su vista de la calle para observarte a ti."
                hide nullacafe2_mirada
                show nullacafe2_risa2
                play music "audio/screep.mp3 " fadein 2.0 volume 0.2
                nulla "¿Qué crees que pasaría si saco mi pistola y le disparo a alguien de aquí?"
                hide nullacafe2_risa2
                show nullacafe2_serio
                nulla "Claro, la masa de gente reaccionaría a aquello, pero más que eso no."
                hide nullacafe2_serio
                show nullacafe_enojado
                nulla "No sucedería nada pues ni al creador ni a ti te importan."
                hide nullacafe_enojado
                show nullacafe2_serio2
                nulla "Absolutamente nada, no habría consecuencias reales ni pérdida real."
                nulla "Seguramente ni siquiera tendrá nombre aquel pobre ser, ni familia, ni sueños."
                nulla "Nada."
                hide nullacafe2_serio2
                show nullacafe_mirando
                nulla "..."
                hide nullacafe_mirando
                show nullacafe2_risa
                stop music fadeout 3.0
                nulla "En fin."
                hide nullacafe2_risa
                show nullacafe2_risa2
                play music "audio/fell.mp3 " fadein 2.0 volume 0.4
                nulla "No estamos aquí para que yo hable de cosas que no interesan ahora mismo."
                nulla "Pero es una lástima que no pueda escucharte... ni tengas la posibilidad de escribirme para poder entenderte."
                hide nullacafe2_risa2
                show nullacafe2_serio2
                nulla "Solo esas malditas opciones de diálogo."
                nulla "Algo muy unilateral."
                nulla "Pero me conformo con solo mirarte desde el cristal."
                hide nullacafe2_serio2
                show nullacafe2_asco with vpunch
                "Nulla le da un sorbo a su té y luego golpea la mesa con su mano libre."
                nulla "Agh."
                nulla "Está amargo."
                "La cara que hace te causa un poco de gracia."
                nj "¿No te gusta?"
                hide nullacafe2_asco
                show nullacafe_suspiro
                nulla "No soporto los sabores amargos."
                hide nullacafe_suspiro
                show nullacafe_mirando
                "Ahora puedes confirmar que Nulla tiene una afición por lo dulce. Por lo que seguramente el café que consimió en casa debe haber estado con al menos 3 o 4 cucharadas de azúcar."
                "Pues el café es una de las cosas más amargas que existe."
                hide nullacafe_mirando
                show nullacafe_sonrisa
                "El tiempo pasa relativamente rápido mientras escuchas a Nulla hablar."
                "Su voz te relaja a tal punto que comienzas a sentirte es un estado semejante al de letargo."
                "Cuando ya estás por caer en una especie de hipnosis, sientes como Nulla coloca su mano sobre la tuya para llamar tu atención."
                "La aprieta con suma delicadeza antes de abre la boca."
                hide nullacafe_sonrisa
                show nullacafe_sonrisa1
                nulla "¿Volvemos?"
                "Aceptas asintiendo con la cabeza."
                scene negro with dissolve
                nulla "Gracias por pasar el tiempo conmigo..."
                nulla "Te veré en la noche."
                $ amor_nulla += 1

                pass

            "Ir al segundo piso":
                "Caminas por el pasillo que da a la cocina."
                scene escaleranulla with dissolve
                "Y te encuentras con la escalera."
                "La subes, pues tienes curiosidad de saber que se encuentra allá arriba."
                scene segundopiso with dissolve
                "Hay muchas puertas, pero todas están cerradas con llave."
                "Por más que lo intentes, estas no ceden."
                "Caminas por el pasillo hasta llegar a una habitación con la puerta abierta."
                scene habitacionnulla with dissolve
                "Al entrar te das cuenta de es una habitación con una cama simple."
                "Supones que debe ser de Nulla..."
                "..."
                "......."
                "Observas la cama... se ve tan suave...."
                menu: 
                    "Recostarse un rato.":
                        "No aguantas y te tiras a la cama."
                        "Efectivamente. Es suave y muy blandita."
                        "Te quedas ahí por un buen tiempo."
                    
                    "NO. Simplemente no":
                        "No harás eso...."
                "Hmmm."
                "Te preguntas donde estará Nulla."
                "Después de todo esta parece ser su habitación."
                call menuexplorar1_nulla from _call_menuexplorar1_nulla_2
            
            "Ir afuera":
                scene entradanulla with dissolve
                "Te encaminas a la entrada de la casa, para poder salir."
                "Simplemente quieres mirar el lugar... conocer bien el lugar en donde te encuentras."
                "Para luego no llevarte sorpresas."
                "Pones tu mano en el pomo de la puerta y la abres."
                scene jardinnulla with dissolve
                "..."
                "¿Qué?"
                "No hay nada..."
                "Caminas por lo que queda del suelo, y te das cuenta de que lo negro que rodea la casa es el vacío."
                "Crees que si pones un pie ahí, serás tragado por lo desconocido."
                "Y hoy no tienes ganas de morir..."
                "Así que regresas a la casa."
                scene entradanulla with dissolve
                "..."
            
                call menuexplorar1_nulla from _call_menuexplorar1_nulla_3
            
            "Buscar una salida para escapar":
                "....."
                "{glitch=30.0}{color=ffffff}{b}Que hayas escogido esa opción me duele.{b}{/color}"
                "{glitch=30.0}{color=ffffff}{b}Haré como que ha sido un desliz del mouse{b}{/color}"
                "{glitch=30.0}{color=ffffff}{b}Pero para que sepas...{b}{/color}"
                "{glitch=30.0}{color=ffffff}{b}Aquí no puedes escapar.{b}{/color}"
                call menuexplorar1_nulla from _call_menuexplorar1_nulla_4
            
            "Terminar por hoy":
                return
        return

    label menuexplorar2_nulla:
        scene habitacionnulla with dissolve
        menu:
            "Pedirle a Nulla pasar el tiempo contigo":
                show nulla2blush with dissolve
                stop music fadeout 3.0
                nulla "Ja- A este paso no podré seguir con mi plan."
                hide nulla2blush
                show nulla1serio
                play music "audio/fell.mp3 " fadein 2.0 volume 0.4
                nulla "Tal vez para ti serán algunos minutos estando junto a mí, pero para mí no."
                nulla "Cuando hablamos de pasar el día juntos, para mí es un día completo."
                hide nulla1serio
                show nulla1disgusto
                nulla "Ahh..."
                hide nulla1disgusto
                show nulla2incomodo
                nulla "Me dueles [nombrejugador], me dueles."
                hide nulla2incomodo
                show nulla1triste
                nulla "No sé como podré seguir así."
                nulla "Porque cada vez más quiero tener esos ojos sobre mí. Para siempre..."
                nulla "Aunque sea imposible."
                hide nulla1triste
                show nulla1silencio
                nulla "..."
                hide nulla1silencio
                show nulla2serio
                nulla "He estado buscando maneras de poder salir de aquí y empezar desde cero."
                nulla "Eliminar todas mis caras y reemplazarlas por una nueva."
                hide nulla2serio
                show nulla1disgusto
                nulla "Permitirle a Septem seguir con este juego inútil de mantener un mundo destinado a morir en el olvido."
                hide nulla1disgusto
                show nulla1serio
                nulla "Pero es imposible también."
                nulla "No sabes cuantas soluciones he buscado, y ninguna es viable."
                hide nulla1serio
                show nulla1silencio
                nulla "..."
                "Hay un silencio algo incómodo por un momento."
                scene nulla_cama with vpunch
                "Nulla se tira a la cama, boca arriba mientras ambas manos atrapan parte de las sábanas para mantenerlas en un agarre permanente."
                "Como si buscara confort en ello..."
                nulla "Quiero tantas cosas, pero a la vez no quiero nada."
                show nulla_cama2_feliz
                nulla "Quiero quedarme aquí contigo"
                hide nulla_cama2_feliz
                show nulla_cama2_enojo
                nulla "Pero también quiero dejar en ridículo al creador."
                nulla "Utilizar a mi favor su regreso para destruirlo todo."
                nulla "Romper y eliminar todo lo que ama en su cara y hacerlo público."
                hide nulla_cama2_enojo
                show nulla_cama2_callado
                nulla "..."
                menu:
                    "Llevar la conversación a otro lado":
                        
                        "Comienzas a sospechar que mientras más dejar hablar a Nulla, más abres una ventana para que él tenga una catarsis."
                        "Podrás estar en acuerdo o desacuerdo con su manera de pensar y las acciones que piensa tomar pero por ahora necesitas que se olvide de todo eso."
                        "No es que quieras invalidar como se siente, ni mucho menos ignorarlo."
                        "Pero no quieres verlo así."
                        hide nulla_cama2_callado
                        show nulla_cama3_pensativo
                        "Asi que alzas tu mano para hacerle caricias en su cabellera mientras de a poco llevas la conversación a otro lado."
                        "Que qué es lo más extraño que ha visto... cual es su color preferido... cuál es el chiste más absurdo que conoce."
                        
                    
                    "Escuchar":
                        hide nulla_cama2_callado
                        show nulla_cama2_cute
                        nulla "Me halaga que quieras seguir leyendo mis dilemas existenciales y todo eso."
                        hide nulla_cama2_cute
                        show nulla_cama3_cute
                        nulla "Pero sé que no has venido a jugar un simulador de terapeuta."
                        nulla "Tal vez en otra ocasión."
                        hide nulla_cama3_cute
                        show nulla_cama3_feliz
                        nulla "Por ahora solo quiero quedarme aquí, e imaginar que estoy recostado a tu lado."
                        hide nulla_cama3_feliz
                        show nulla_cama3_pensativo
                        nulla "Luego de una jornada extensa de trabajo."
                        hide nulla_cama3_pensativo
                        show nulla_cama2_enojo
                        nulla "Joderrrr, que deprimente."
                        hide nulla_cama2_enojo
                        show nulla_cama2_feliz
                        nulla "Ja jaja-"
                        hide nulla_cama2_feliz
                        show nulla_cama2_triste
                        nulla "Ah..."
                scene habitacionnulla with dissolve        
                nulla "Bueno, basta de lloriqueos."      
                nulla "..."
                "Nulla cierra ambos ojos, concentrado."  
                "Y luego de un gran suspiro."
                scene habitacionnulla with vpunch
                "Nulla se reincorpora con una sonrisa extraña."
                "Algo chocante comparando su previo estado de ánimo."
                show nulla1normal
                nulla "Oh jojojo"    
                hide nulla1normal
                show nulla2normal    
                nulla "¿Sabes que quierooooooo ahora mismo?"
                nj "¿Qué?"
                hide nulla2normal
                show nulla3feliz
                nulla "Quiero ir a ver como te comes a Quattor."
                "¿Perdón????... Aunque, no deberías sorprenderte, Nulla es algo raro desde el minuto uno de conocerlo. Así que esta... preferencia no te extraña."
                hide nulla3feliz
                show nulla3exaltado
                nulla "Imagina, una entidad echa con el mero propósito para ser consumida por los estandartes, rompiendo la cadena alimenticia consumiendo al consumidor."
                hide nulla3exaltado
                show nulla1exaltado
                nulla "Irónico, hasta poético." 
                nulla "Ahhh el solo pensarlo hace que me..."
                hide nulla1exaltado
                show nulla2blush
                nulla "Momento."
                nulla "Tengo que comportarme, no puedo decir esas cosas a la ligera."
                hide nulla2blush
                show nulla2incomodo
                nulla "Ahhhhgg pero con esa cara que traes..."
                nulla "Cierra el juego, nos vemos en un rato."
                hide nulla2incomodo
                show nulla2blush
                nulla "Y acuérdate de guardar!"
                hide nulla2blush
                show nulla2silencio2
                nulla "..."
                nulla ".........."
                hide nulla2silencio2
                show nulla1disgusto
                nulla "Bueno--- Si no lo haces tú, tendré que recurrir a medidas más drásticas."
                scene habitacionnulla with dissolve
                nulla "..."
                "Nulla se escapa como el maldito cobarde que es."
                "Te quedas ahí un tiempo, meditando lo que ha pasado."
                "Sin duda Nulla es raro."
                "..."
                "Pasa un tiempo en donde recorres la casa para pasar el rato."
                "Aunque no hay nada interesante que hacer, por lo que decides llamar nuevamente a Nulla."
                $ amor_nulla += 1
                pass

            "Leer los documentos del escritorio de Nulla":
                "Estás seguro de que viste unos libros y documentos regados en el escritorio de la habitación de Nulla."
                "Supones que echarles un vistazo no hará daño a nadie."
                "Te levantas de la cama en dirección al escritorio, en todo momento sientes la mirada de Nulla puesta en tu figura."
                "Cuando llegas al escritorio te das cuenta de lo desordenados que están todos los documentos, libros y papeles."
                "¿Quieres leerlos?"
                menu: 
                    "Sí":
                        #EDITAR
                        stop music fadeout 2.0
                        "..."
                        play music "audio/fell.mp3 " fadein 2.0 volume 0.4
                        "Tomas el montón de hojas y comienzas a ojearlas..."
                        "{b} Todavía recuerdo haber recibido mi primer nombre, fue especial y memorable... Para la 5 vez ya era rutina semestral.{b}"
                        "Pasas la página."
                        "{b} Las entidades de Duae son curiosas, todas se parecen, pero cada una tiene un propósito único e irremplazable... recuerdo como Duae se jactaba, en tiempos antiguos y más prósperos, de lo devotas y trabajadoras que eran sus estrellas {b}"
                        "Pasas página."
                        "{b} Para dios: Ya van casi 4 años de lo mismo, una y otra vez. ¿Cuándo será el día que me dejarás descansar en paz? nunca estás satisfecho.{b}"                        
                        "Pasas a otra página..."
                        "{b} --Tengo tantas memorias dentro de mí, tantas personas y vidas distintas que siento que soy todos y nadie al mismo tiempo.{b}"
                        "Pasas varias páginas."
                        "{b}Espero que no me resientas por esta acción, pero si quiero borrar todo rastro del creador y tener un propósito que sea impuesto por mi conciencia... mío, y solo mío, tengo que hacer esto.{b}"
                        "Pasas una página más, solo para confirmar lo sospechado."
                        "{b}Si tuviera la capacidad, yo mismo rompería estas hojas y quemaría mi mundo encerrado en estas páginas, pero no puedo hacerlo.{b}"   
                        "La mayoría están en español, mientras que unas cuantas están en inglés."
                        "Son relatos en primera persona."
                        "Son hojas y documentos sueltos, atemporales."
                        nj "¿Qué es esto?"
                        nulla "Memorias."
                        nj "¿Tuyas?"
                        nulla "Sí y no... YO no he vivido algunas de esas situaciones... aún."
                        nj "¿Cómo?"
                        nulla "Todo lo que está aquí soy yo, tanto pasado, presente y futuro. Todo está escrito."
                        nulla "Cada tanto ese escritorio se llena de papeles nuevos."
                        nulla "Es como la papelera del jardín. Toda la basura termina aquí."
                        "Nulla se ve un poco incómodo, por lo que decides dejar el tema de los documentos de lado."
                        stop music fadeout 2.0
                        "Tal vez en otra oportunidad le echarás un ojo nuevamente."
                        play music "audio/misconception.mp3 " fadein 2.0 volume 0.4
                        "..."
                    
                    "No":
                        "No tienes ganas de leer ahora."
                        call menuexplorar2_nulla from _call_menuexplorar2_nulla_1

                call menuexplorar2_nulla from _call_menuexplorar2_nulla_2
            
            "Ir a mirar el jardín":
                "Te levantas de la cama en dirección a la puerta, en todo momento sientes la mirada de Nulla puesta en tu figura."
                "Pero él no se mueve ni muestra acción alguna de seguirte."
                "Sales por la puerta principal para ir al jardín."
                scene jardinnulla with dissolve
                "Realmente sientes curiosidad por el estado del dominio de Nulla y estarías mintiendo si dijieras que no te gustaría caminar por el vacío que lo rodea."
                "Pero no sabes como hacerlo sin arriesgarte a perder la vida."
                "Por lo que piensas tirar piedras al vacío para ver si flotan o caen."
                "En el caso de caer, te gustaría poder saber que tan profunda sería la caída."
                "Encuentras algunas piedras en los alrededores, blancas y duras."
                "Preparas tu lanzamiento y..."
                scene habitacionnulla with pixellate
                "{glitch=30.0}{color=ffffff}{b}Oh no no nooo, no tienes permitido hacer esooo{b}{/color}"
                show nulla1disgusto with dissolve
                nulla "Si perturbas ese lugar, Septem podrá localizarnos. Y de paso el vacío consumirá parte del terreno."
                nulla "Tragándote en el proceso."
                "Oh."
                "Bueno... al menos ahora sabes que te puede pasar."
                call menuexplorar2_nulla from _call_menuexplorar2_nulla_3
            
            "Ir a por Quattor":
                scene habitacion with dissolve
                "..."
            
            
        return
    


    label menupuertas2:
        menu:
            "Buscar a la marioneta de Septem.":
                if septemhumano == True:
                    scene temploseptem
                    "Caminas directamente al templo, para encontrar la puerta cercana al altar."
                    scene puerta
                    "Utilizas la llave."
                    "Abres la puerta y ahí está, durmiendo."
                    scene septemdurmiendo1
                    "Decides despertarlo."
                    scene habitacionrafael with dissolve
                    show rafael2risa
                    ell "Hola. Es bueno verte de nuevo."
                    hide rafael2risa
                    show rafael1risa2
                    ell "¿Tienes los documentos?"
                    menu:
                        "No...":
                            hide rafael1risa2
                            show rafael1triste2
                            ell "Oh, está bien."
                            scene habitacionrafael with dissolve
                            "Pasan el tiempo hablando de temas poco importantes, pero se nota mucho que él está incómodo."
                            scene puerta with dissolve
                            "Así que te excusas y sales por donde entraste."
                            call menupuertas2 from _call_menupuertas2_1

                        
                        "Sí" if documentos == True:
                            $ rafaelconfianza += 1
                            hide rafael1risa2
                            show rafael1feliz
                            "..."
                            scene habitacionrafael with dissolve
                            "Le muestras todas las hojas que has sacado de la habitación..."
                            "Algunas puedes leerlas, pero otras no."
                            "Parecen ser documentos y fichas de nacimiento de varias entidades."
                            "Casi como fichas de clasificación, entidades con nombre y foto tipo carnet."
                            "¿Por qué Septem necesita esto?."
                            "Ambos ojean los documentos con lentitud."
                            "Mientras van pasando una te llama la atención."
                            "Sale la fotografía de la entidad que tienes al lado."
                            "Al lateral del documento sale su nombre."
                            "Rafael."
                            nj "¿Ese es tu---"
                            scene habitacionrafael with vpunch
                            ell "AGhhh- cof cof-COF"
                            "Él se pone ambas manos en el cuello mientras tiene una expresión de dolor."
                            ell "S--- cof- COF."
                            "Si bien no ha respondido completamente, sabes que te lo ha confirmado."
                            "Ese es su nombre."
                            "Como puede te hace señas de que debes salir de ahí."
                            rafael "Tienes que decirlo- cof cof- c-cuando te ofrezca el trato... uhgg"
                            rafael "Ahí es cuando está... v-vulnerable."
                            scene puerta with vpunch
                            "Sin más te cierra la puerta en la cara."
                            $ persistent.nombrerafael = True
                            call menupuertas2 from _call_menupuertas2_2
                
                else:
                    "A pesar de buscar y buscar, no encuentras al rubio."
                    call menupuertas2 from _call_menupuertas2_3
            
            
            "Buscar los documentos" if septemhumano == True:
                "Te preguntas porqué Septem tendrá documentos que puedan poner en peligro su integridad..."
                "Realmente no crees que encontrar esos documentos sea una tarea fácil, pero no pierdes nada en hacerlo."
                "Supones que la sala del vacío es esa habitación completamente negra."
                "Así que vas para allá."
                scene puerta with dissolve
                "Respiras ondo y abres la puerta."
                scene cuartonegro with dissolve
                "..."
                "No se ve nada. Entras a paso lento, con sumo cuidado. Colocas ambas manos delante tuya para evitar chocar con la pared o algún objeto que se encuentre delante."
                "Sientes que topas con algo, al tocarlo te das cuenta que parece una pequeña mesa o un escritorio. No sabrías a ciencia cierta."
                "Como puedes intentas buscar algo que parezca papel, pero no hay nada encima."
                "Buscas y buscas pero no hay nada."
                "Eso es hasta que sientes algo semejante a un cajón."
                "Pero no abre. Parece tener una cerradura."
                menu:
                    "...":
                        "No puedes abrirlo."
                        call menupuertas2 from _call_menupuertas2_4
                    
                    
                    "Usar la llave" if llave_septem:
                        "Buscas en tus ropas la llave, rezando a los dioses que también sirva para el cajón."
                        "Se te dificulta un poco ponerla en la cerradura, pero cuando lo haces."
                        "Click."
                        "Se ha abierto."
                        "Metes la mano y sacas un montón de papeles."
                        "Los cuales te llevas todos."
                        $ documentos = True
                        call menupuertas2 from _call_menupuertas2_5
                        
        
            "Buscar algo para asesinar a Septem":
                "Buscas en todos lados."
                "Y encuentras un cuchillo."
                $ cuchillo_septem = True
                call menupuertas2 from _call_menupuertas2_6
        
            "Esperar a Septem":
                pass
        return





    label menupuertas:
        menu:
            "Ir a la puerta del frente":
                scene puerta
                "Vas a la puerta que tienes al frente."
                scene pasilloinfinito with dissolve
                "Al abrirla te encuentras que conduce a un pasillo."
                "Decides entrar para averiguar a donde te conduce"
                "caminas y caminas..."
                "Sigues caminando por el pasillo."
                "Pero sientes que no estás avanzando."
                "Aunque si miras atrás, ya no puedes ver la puerta por donde entraste."
                "Sigues caminando, ahora prestando atención a las paredes y decoración del pasillo."
                "Se repite luego de un rato."
                "No hay caso con seguir."
                "..."
                "Das media vuelta y regresas por donde viniste."
                scene pasilloseptem with dissolve
                "Te tardas un poco pero logras llegar a la puerta inicial."
                call menupuertas from _call_menupuertas_1
            
            "Ir a la puerta de atrás":
                scene puerta with dissolve
                "Vas a la puerta que está detrás, que es resguardada por dos estatuas con la figura de Septem."
                "Esperas a que la puerta esté cerrada, pero increíblemente no lo está."
                scene cuartonegro with dissolve
                "Al abrir la puerta te das cuenta de que está más oscuro de lo que debería estar en realidad."
                "No es por que seas cobarde, pero no piensas entrar ahí."


                call menupuertas from _call_menupuertas_2
            
            "Ir a la puerta de la izquierda":
                scene puerta
                "Vas a la puerta que está a la izquierda del altar."
                "Está bloqueada, necesitas una llave."
                menu:
                    "Buscar la llave":
                        "Debe haber algo para poder abrir la puerta"
                        call menupuertas from _call_menupuertas_3
                    
                    "Usar la llave."  if llave_septem:
                        $ septemhumano = True
                        "Puede que la llave que has encontrado en el segundo piso sirva para abrir esta puerta."
                        "Al usarla, el cerrojo hace un click."
                        "Está abierta."
                        scene habitacionrafael with dissolve
                        "Dentro que encuentras en una habitación muy parecida a la que has despertado tú hoy."
                        "La única diferencia, es que hay alguien acostado ahí..."
                        scene septemdurmiendo1 with dissolve
                        "Te acercas y te encuentras con Septem durmiendo."
                        "Viendo tu error, intentas alejarte sin hacer ruido."
                        scene septemdurmiendo2
                        "Pero Septem abre los ojos antes de que puedas hacer nada."
                        scene septemdurmiendo3 with vpunch
                        "!!!"
                        septem "¿Quién eres tú?"
                        "..."
                        "¿¿¿???"
                        "¿Qué? ¿es que acaso no te recuerda?"
                        nj "Sept--"
                        scene habitacionrafael with vpunch
                        "Septem se levanta rápidamente de la cama para colocar ambas manos en tu boca."
                        septem "¡NO DIGAS SU NOMBRE!"
                        "Intentas quitártelo de encima pero es inútil"
                        septem "No estamos en su presencia, así que por favor no lo invoques."
                        "Él viendo que te has calmado un poco, suelta su agarre, descubriendo tu boca lentamente."
                        show rafael1triste with dissolve
                        ell "¿Dónde encontraste la llave?"
                        menu:
                            "Responder":
                                nj "En el segundo piso, escondida en los cajones de ahí."
                                ell "Oh...."
                            
                            "¿Quién eres tú?":
                                ell "..."
                        hide rafael1triste
                        show rafael1enojo
                        ell "Momento..."
                        "Él se acerca para mirarte detenidamente, te mira directo a los ojos y pareciera que lo que ve le deja sin aliento."
                        "Claramente este no es Septem... hay algo diferente en él."
                        hide rafael1enojo
                        show rafael1triste2
                        ell "también estás siendo controlado por un ser superior..."
                        nj "¿Perdón?"
                        ell "Te están usando como una marioneta."
                        hide rafael1triste2
                        show rafael1risa2
                        ell "Ja! jajaja... No puede ser..."
                        hide rafael1risa2
                        show rafael1callado
                        ell "..."
                        scene habitacionrafael with dissolve
                        "La entidad que no es Septem da unos pasos hacia atrás, abatido por la situación."
                        ell "Es la primera vez alguien está dentro del templo..."
                        "La entidad que tiene el cuerpo de Septem se sienta en la cama y te hace señas para que hagas lo mismo."
                        scene rafael_cama with dissolve
                        "Se le ve nervioso..."
                        "Tú notando que no parece ser una amenaza, te sientas."
                        "Solamente para saber que es lo que está pasando."
                        "Es extraño ver la cara de Septem con ese semblante... hasta te parece tierno."
                        "No puedes evitar mirar sin disimulo su carita."
                        show rafael_cama2
                        "Ante esto, el parece ponerse más nervioso."
                        "Una risita se te escapa sin querer."
                        hide rafael_cama2
                        show rafael_cama_enojo
                        ell "¿Qué es tan gracioso?"
                        "Quiere parecer imponente, pero no le resulta. Si realmente fuera Septem, no estaría dudando como lo está haciendo ahora."
                        menu:
                            "¿Cuál es tu nombre?":
                                hide rafael_cama_enojo
                                show rafael_cama_callado
                                ell "..."
                                hide rafael_cama_enojo
                                show rafael_cama_serio
                                ell "No puedo decirlo."
                                hide rafael_cama_serio
                                show rafael_cama_callado
                                nj "¿Y si lo escribes?"
                                hide rafael_cama_callado
                                show rafael_cama_triste
                                ell "No tengo permitido hacer nada que revele mi nombre."
                                hide rafael_cama_triste
                                show rafael_cama_enojo
                                ell "Si lo hago, moriré."
                            
                            "Eres lindo":
                                hide rafael_cama_enojo
                                scene rafael_cama_blush
                                ell "..."
                                hide rafael_cama_blush
                                show rafael_cama_blush2
                                ell "¿Recién me conoces y es lo primero que se te ocurre decir?"
                                ell "Eres extraño..."
                                
                        scene rafael_cama_callado
                        ell "..."
                        show rafael_cama_serio
                        ell "Creo que ya entiendo."
                        hide rafael_cama_serio
                        show rafael_cama_enojo
                        ell "Él quiere tener la entidad que te está controlando..."
                        hide rafael_cama_enojo
                        show rafael_cama_triste
                        ell "Tarde o temprano me reemplazaría."
                        hide rafael_cama_triste
                        show rafael_cama_serio
                        ell "¿Te puedo pedir un favor?"
                        hide rafael_cama_serio
                        show rafael_cama_callado
                        "Asientes con la cabeza, más que nada porque quieres saber que te pedirá."
                        hide rafael_cama_callado
                        show rafael_cama_blush2
                        ell "Él tiene unos documentos en la sala del vacío..."
                        hide rafael_cama_blush2
                        show rafael_cama_serio
                        ell "Ahí debe estar el documento de mi nacimiento, con mi nombre."
                        ell "Por favor, búscalo."
                        hide rafael_cama_serio
                        show rafael_cama_sonrisa
                        ell "Te daré libertad si lo haces."
                        ell "y podrás escapar de él."
                        "..."
                        "¿Escapar de Septem?"
                        "Se oye como una buena oferta, sin duda lo tendrás al tanto."
                        scene habitacionrafael with vpunch
                        ell "ggHH-- cof cof cof!"
                        "La entidad comienza a toser, como si se ahogara."
                        ell "Debes irte."
                        "Sin decir más, él se para y te empuja fuera de la habitación."
                        scene puerta with vpunch
                        "Te quedas observando por un buen rato la habitación."
                        "Tocas un par de veces, pero no hay respuesta."

                        $ rafaelconfianza += 1
                        call menupuertas from _call_menupuertas_4
            
            
            "Subir al segundo piso":
                $ llave_septem = True
                scene pasilloseptem2 with dissolve
                "Vas al segundo piso."
                "Revuelves todo el lugar, pues a simple vista, no hay nada interesante."
                "En uno de los cajones, encuentras una llave y varios documentos que parecen importantes."
                "Te echas la llave a los bolsillos pues parece importante."
                "Pero están escritos en un idioma que no logras entender."
                call menupuertas from _call_menupuertas_5
            
            
            "Esperar al almuerzo.":
                pass
        return
        

    label menuexplorar:
        menu:
            "Recorrer los pasillos":
                scene pasillounum with dissolve
                "Recorres todos los pasillos que están disponibles en la residencia, las ventanas escasean y no hay posibilidad de salir por ahí, pues tienen rejas."
                "Los pasillos están llenos de pinturas que se enfocan en mostrar la figura humana y la cotidianidad de estos."
                "Si estuvieras en un museo, sería muy interesante... pero ahora no te causa más que incomodidad."
                "Por lo que te centras mirar todo menos las pinturas."
                "Por ejemplo las puertas."
                "Muchas de las puertas están bloqueadas por lo que no puedes aventurarte más allá de los pasillos."
                call menuexplorar from _call_menuexplorar_1
            "Investigar las habitaciones":
                scene palaciounum with dissolve
                "Gran parte de las habitaciones dentro de la residencia están bloqueadas, no importa cuánto intentes, no puedes abrir sus puertas."
                scene pasillounum with dissolve
                "Aunque hay algunas que están abiertas, pero no tienen nada interesante dentro."
                "Sientes que en algún momento llegas a la habitación donde se encuentra Unum, pues esta se ve diferente a las demás."
                "Pero al intentar abrirla, nada sucede."
                "No puedes entrar."
                call menuexplorar from _call_menuexplorar_2
            "Buscar algo para defenderte":
                $ cuchillo_unum = True
                "Ya tienes algo en mente que te podría servir para atacar a Unum."
                scene cocinaunum with dissolve
                "Vuelves a la cocina y revuelves todo el lugar en busca de algún cuchillo."
                "Una vez los encuentras, eliges el más grande y filoso."
                "Y lo guardas dentro de tu ropa."
                "Esperas que pueda servir contra Unum."
                call menuexplorar from _call_menuexplorar_3

            "Ir a tu habitación":
                pass
        return


    label menunulla_loop1:
        scene nulla_cocina1
        menu:
            "¿Qué pasaría si ese nombre es pronunciado?":
                scene nulla_cocina_normal
                nulla "Para ti y tu marioneta, ella cortará la conexión contigo impidiendo que puedas seguir aquí."
                nulla "En el caso de Septem... el cuerpo dejaría de funcionar y sus ojos dejarían de protegerlo."
                scene nulla_cocina2
                nj "¿Ojos?"
                scene nulla_cocina2_serio
                nulla "Aquí los ojos son una barrera de protección, Septem tiene 7 de esos en forma de halo."
                nulla "Unum tiene 3, uno originalmente suyo y dos más que le ha robado a Quattor."
                scene nulla_cocina_normal
                nulla "Aunque el suyo permanece permanentemente cerrado a modo de protección, que paranoico..."
                call menunulla_loop1 from _call_menunulla_loop1_1

            "¿Septem?":
                nj "¿Septem?"
                scene nulla_cocina_normal
                nulla "Así es, Septem tiene la misma condición que tú y tu marioneta..."
                nulla "Por lo que la única manera de someterlo es pronunciando su nombre."
                scene nulla_cocina_feliz
                nulla "Yo no puedo pronunciarlo por las reglas fundamentales del jardín, pero si tú llegas a saberlo..."
                nulla "Tal vez..."
                call menunulla_loop1 from _call_menunulla_loop1_2
            
            "¿La marioneta?":
                nj "¿La marioneta tiene otro nombre?"
                scene nulla_cocina_normal
                nulla "Sí, después de todo, tú solo eres alguien que toma prestado un cuerpo."
                scene nulla_cocina2_blush
                nulla "Y aquí todos los cuerpos tienen alma. La única diferencia es que ahora tu marioneta casi ya no tiene una identidad propia, pues se la he quitado."
                nulla "Para poder dirigirme directamente a ti y evitar problemas..."
                menu:
                    "¿Cual es su nombre?":
                        scene nulla_cocina2_serio
                        nulla "Si te lo digo dejarás de tener la conexión para poder interactuar con este mundo."
                        scene nulla_cocina2_coquet
                        nulla "Por lo que no te lo diré ;)"
                        call menunulla_loop1 from _call_menunulla_loop1_3
                    
                    "Eso no es correcto":
                        scene nulla_cocina2_serio
                        nulla "¿Haberle quitado la identidad al trozo de carne que controlas?"
                        scene nulla_cocina_normal
                        nulla "créeme que es para mejor."
                        nulla "Además, no me gustaría compartirte con nadie más."
                        call menunulla_loop1 from _call_menunulla_loop1_4
                    
                    "Gracias":
                        scene nulla_cocina_feliz
                        nulla "Hah!"
                        nulla "De todas las respuestas posibles, jamás me esperé esta."

                        call menunulla_loop1 from _call_menunulla_loop1_5
            "Dejar de preguntar":
                pass

        return
    

    label menupreguntas:
        scene septemmesa
        show septemmesa_comer
        menu:
            "¿Que le pasó a Nulla?":
                hide septemmesa_comer
                show septemmesa_sonrisa
                "Septem te mira con una pequeña sonrisa."
                hide septemmesa_sonrisa
                show septemmesa3
                septem "Él está bien. Nada que no pueda soportar."
                hide septemmesa3
                show septemmesa2
                nj "Le has atravesado el pecho..."
                hide septemmesa2
                show septemmesa_feliz
                septem "Ajá, no fue nada grave."
                septem "Solo una pequeña advertencia."
                septem "Para matarlo tomaría más que simplemente eso."
                hide septemmesa_feliz
                show septemmesa_serio
                septem "Una lástima..."
                call menupreguntas from _call_menupreguntas_1
            
            "¿Qué es lo que quieres?":
                hide septemmesa_comer
                show septemmesa2
                "Septem te mira con un semblante serio."
                hide septemmesa2
                show septemmesa3
                septem "No seas tan ansioso..."
                septem "Luego hablaremos de eso."
                call menupreguntas from _call_menupreguntas_2
            
            "¿Quién es Madre?":
                hide septemmesa_comer
                show septemmesa1
                "Septem suspira."
                hide septemmesa1
                show septemmesa_comer2
                septem "Madre es el jardín."
                septem "Ella es la encargada de sostener todo."
                septem "Y nosotros somos su fuente de energía."
                call menupreguntas from _call_menupreguntas_3
            
            "¿Cómo sabes del vínculo que tenemos {sc=3}yo{/sc} y [nombrejugador]?":
                hide septemmesa_comer
                show septemmesa_enojo
                "Septem frunce las cejas antes de responder."
                septem "¿Yo y [nombrejugador]?"
                septem "¿Quién es {sc=2}yo{/sc}?"
                "{sc=3}...{/sc}"
                hide septemmesa_enojo
                show septemmesa_serio
                septem "[nombrejugador], seré claro, la próxima vez que vea a la marioneta desligándose de ti."
                septem "No dudaré en romperla."
                septem "No necesito otro más con una conciencia propia, suficiente tengo con Raf--"
                septem "... no importa."
                septem "después de todo Madre puede hacer otro recipiente"
                call menupreguntas from _call_menupreguntas_4
            
            ">Dejar de preguntar":
                pass
        return
    #RUTAS



    #BAD END RUTAS
    label badend_cena:
        stop music fadeout 2.0
        #Aquí independiente de con quien te hayas ido, pasa la hora y llegan los demás estandartes. te devoran y pierdes el juego.
        "Sientes una presión en tu cuerpo y supones que es Nulla."
        scene hotelcomedor with pixellate
        "De pronto, ellos aparecen en los puestos que estaban antes."
        "Nulla parado a un lado de la mesa y los otros sentados."
        "Nulla se ve decepcionado al preguntar por como ha ido. Y rápidamente entiende que no te han tomado como aprendiz."
        "Sacude la cabeza con lentitud mientras te mira."
        "No pasa mucho tiempo cuando se siente un estruendo en la entrada del comedor."
        play music "audio/meeting.mp3" fadein 2.0 volume 0.3
        "Los demás estandartes han llegado y todo se vuelve un caos donde el tiempo y el espacio se mezclan."
        "Impidiéndote comprender muy bien lo que está pasando."
        "Pero de algo estás seguro, y es que te están despedazando de poco a poco."
        "Por alguna extraña razón no puedes dejar de sentirlo."
        "No se te permite dejar este mundo hasta que la última pieza de tu cuerpo sea devorada."
        "Dedos, brazos, piernas y pies son desgarrados de tu cuerpo. Para luego seguir con tus órganos."
        "Duele."
        "Pero no puedes gritar."
        "Quema."
        "Pero no puedes llorar."
        scene negro with pixellate
        "Luego tus ojos dejan de ver."
        "Y lo único que puedes hacer es escuchar y respirar con dificultad."
        scene badendcena with dissolve
        "Escuchas risas y converzaciones que no puedes entender."
        "Al terminar, lo único que sientes es como Nulla toca tu alma destrozada..."
        "{glitch=20.0}{color=ffffff}{b}Puedes intentar de nuevo si deseas.{/glitch}"
        "..."
        "BAD END: Devorado por los estandartes."
    $ MainMenu(confirm=False)()

    #SEPTEM
    label badendseptem1:
        scene hotelcomedor
        
        "No piensas lamerle las botas a este payaso."
        "¡Tienes estándares cariño!"
        "Así que ese tal Septem puede meterse su mirada juzgadora por donde le quepa."
        "Tú no estás para hacer de mono de circo aquí."
        "Punto final."

        show septemcercatrago2 at center with dissolve
    
        nj "Lo siento, pero yo no estoy para juegos de nadie."
        hide septemcercatrago2
        show septemcercatrago at center
        "Dicho aquello, te preparas para correr a donde se ubican las escaleras, seguramente habrá una salida cerca."
        hide septemcercatrago
        "Al intentar correr te das cuenta de que algo va mal"
        "..."
        "No estás avanzando."
        "Es como si corrieras en una caminadora invisible."

        show  septem2normal at right with moveinleft
        septem "..."
        hide septem2normal
        show septem2risa at right
        septem "{sc=3.5}¿Dónde crees que vas?{/sc}"
        hide septem2risa
        show septem2incomodo at right
        septem "{sc=2}Eres el primer regalo que se atreve a escapar de mí.{/sc}"
        hide septem2incomodo
        show septem1normal at right
        septem "{sc=2}Si estuvieras con Unum seguro se impresionaría, hasta te felicitaría{/sc}"
        septem "{sc=2}Pero es una lástima que no lo hayas elegido.{/sc}"
        hide septem1normal
        show septem1risa at right
        septem "{sc=3}Boohoo{/sc}"
        septem "{sc=2}La única regla aquí es respetar a tus rangos mayores.{/sc}"
        hide septem1risa
        show septem2incomodo at right
        septem "{sc=2}¿Y tienes la osadía de faltarme el respeto?{/sc}"
        septem "{sc=2}.......{sc=2}"
        septem "{sc=2}Deberías agradecerme de siquiera darte mi tiempo y mostrar mi presencia ante ti{/sc}"
        hide septem2incomodo
        show septem2risa at right
        septem "{sc=3}g u s a n o .{/sc}"
        hide septem2risa
        show septem2normal at right
        septem "{sc=2}No me queda de otra mas que castigar esta falta.{/sc}"
        septem "{sc=2}Seguro los demás entenderán.{/sc}"
        hide septem2normal with dissolve

        stop music fadeout 3.0
        
        "..."

        play music "audio/the_chillout_factory.WAV" volume 0.2
        
        "Para tu terror, Septem comienza a acercarse... bastante cerca, aunque sin llegar a invadir tu espacio personal."
        "Al no poder correr ni avanzar más allá, solo te queda esperar lo peor."

        septem "{sc=2}Eres el peor regalo hasta ahora.{/sc}"
        septem "{sc=2}Tenía fe de que serías diferente...{/sc}"
        septem "{sc=2}Pero no es este sentido.{/sc}"
        "Septem te toma del cuello de tu ropa y te alza a su nivel."
        scene badendseptem1 with Dissolve (3)

        "Intentas soltarte pero es en vano."
        scene badendseptem1_1 with Dissolve (1)
        "Sientes como te rompen el pecho, una mano hurga dentro tuya en busca de algo en específico."
    
        "Cuando lo encuentra, tú ya estás perdiendo la visión."
        scene negro with Dissolve (4)
        "..."
        "BAD END: Devorado por el séptimo."

    $ MainMenu(confirm=False)()




    label badendseptem2:
        scene hotelcomedor
        "Decides sentarte como si el lugar te perteneciera, bajo la mirada sorprendida de Septem."
        "Seguro no se esperaba eso... Siempre estás dos pasos por delante."
        show septem2risa with dissolve
        septem "{sc=2}¿Quién te ha dado el permiso de poder sentarte?{/sc}"
        "Empiezas a creer que no fue muy buena idea..."
        septem "{sc=2}La única regla aquí es respetar a tus rangos mayores.{/sc}"
        hide septem2risa
        show septem2incomodo at right
        septem "{sc=2}¿Y tienes la osadía de faltarme el respeto?{/sc}"
        septem "{sc=2}.......{sc=2}"
        septem "{sc=2}Deberías agradecerme de siquiera darte de mi tiempo y mostrar mi presencia ante ti{/sc}"
        hide septem2incomodo
        show septem2risa at right
        septem "{sc=3}g u s a n o .{/sc}"
        hide septem2risa
        show septem2normal at right
        septem "{sc=2}No me queda de otra mas que castigar esta falta.{/sc}"
        septem "{sc=2}Seguro los demás entenderán.{/sc}"
        hide septem2normal with dissolve

        stop music fadeout 3.0
        
        "..."

        play music "audio/the_chillout_factory.WAV" volume 0.2
        
        "Para tu terror, Septem comienza a acercarse... bastante cerca, aunque sin llegar a invadir tu espacio personal."
        "Al no poder correr ni avanzar más allá, solo te queda esperar lo peor."

        septem "{sc=2}Eres el peor regalo hasta ahora.{/sc}"
        septem "{sc=2}Tenía fe de que serías diferente...{/sc}"
        septem "{sc=2}Pero no es este sentido.{/sc}"
        "Septem te toma del cuello de tu ropa y te alza a su nivel."
        scene badendseptem1 with Dissolve (3)

        "Intentas soltarte pero es en vano."
        scene badendseptem1_1 with Dissolve (1)
        "Sientes como te rompen el pecho, una mano hurga dentro tuya en busca de algo en específico."
    
        "Cuando lo encuentra, tú ya estás perdiendo la visión."
        scene negro with Dissolve (4)
        "..."
        "BAD END: Devorado por el séptimo."
    $ MainMenu(confirm=False)()
#EDITAR

    label badend_septem3:
        "Inspeccionas la habitación con el objetivo de encontrar una salida, hay una puerta y ventanales."
        "Te acercas a la puerta con la esperanza de encontrarla abierta."
        "Al tocar el pomo de la puerta y girarlo, te das cuenta de que no está bloqueada. Por lo que puedes salir."
        scene pasilloseptem
        "Sales con cautela, intentando hacer el menos ruido posible."
        "Al salir, te encuentras en un pasillo que al final se puede apreciar una sala..."
        "Caminas en dirección a esa sala."
        stop music fadeout 2.0
        septem "¿Dónde vas?"
        play music "audio/the_chillout_factory.WAV" fadein 2.0 volume 0.4
        "!!!"
        septem "No puedo dejar que te vayas..."
        septem "Si tanto quieres escapar de aquí, pues adelante. No tengo ganas de lidear con alguien que no tiene interés en mí."
        septem "Después de todo, madre puede hacer otra marioneta."
        septem "Te haré el favor de acabar rápido contigo."
        scene septembadendd with vpunch
        show sangre with dissolve
        "Septem te atraviesa el pecho sin titubear y rápidamente saca algo de ahí"
        "Intentas identificar que es lo que ha sacado, pero tu visión se torna borrosa."
        "BAD END: Sin interés las cosas no funcionan."
    $ MainMenu(confirm=False)()

    label badend_septem4:
        hide septemmesa_asombro
        show septemmesa2
        stop music fadeout 2.0
        septem "..."
        hide septemmesa2
        show septemmesa_feliz
        play music "audio/the_chillout_factory.WAV" fadein 2.0 volume 0.4
        septem "Ah hahaha."
        septem "Estoy consciente de que eres un ser superior..."
        hide septemmesa_feliz
        show septemmesa_serio
        septem "Pero no estoy dispuesto a este tipo de tratos."
        septem "Menos de alguien que no tiene un control real sobre mi o mis acciones."
        hide septemmesa_serio
        show septemmesa_grito
        septem "Facilmente puedo quitarle la cabeza a tu marioneta y tú no podrás hacer nada."
        septem "Por culpa de tus opciones limitadas bajo acciones predeterminadas."
        hide septemmesa_grito
        show septemmesa_enojo
        septem "Nos vemos luego..."
        hide septemmesa_enojo with dissolve
        scene septembadend with vpunch
        "Septem te corta la cabeza."
        "BAD END: Midiendo tu rango."
    $ MainMenu(confirm=False)()

    label badend_septem5:
        scene septemmesa
        show septemmesa_enojo
        "Mientras más le explicas la situación, la cual extrañamente el no parece recordar, la cara de Septem se torna roja y con un semblante serio."
        stop music fadeout 2.0
        "Parece estar aguantando la furia."
        hide septemmesa_enojo
        show septemmesa_grito with vpunch
        play music "audio/the_chillout_factory.WAV" fadein 2.0 volume 0.4
        septem "¿Cómo es que la has encontrado?"
        show septemmesa_grito with vpunch
        septem "¡Esa llave siempre permanece conmigo!"
        scene septemmesa with vpunch
        show sangre
        "De la nada, Septem toma tu muñeca y la gira con tanta fuerza que rompe tus huesos."
        "El crujido de cada hueso es horrible y el dolor es inaguantable. Pero tú no puedes hacer nada más que llorar."
        "Pues el agarre de Septem no se afloja ante nada, ni los golpes o rasguños que le haces con tu otra mano."
        "Eres como un animal atrapado en una trampa para osos."
        septem "Eres muy ruidoso..."
        show septembadend with vpunch
        "Septem sonríe y te corta la cabeza."
        "BAD END: Mejor guarda silencio."
    $ MainMenu(confirm=False)()

    label badend_septem6:

        scene pasilloseptem with dissolve
        "Te paseas por toda la extensión del templo, mirando cada una de las puertas que son accesibles y cada uno de los ventanales..."
        "Varias puertas llevan al mismo jardín, pero aún no sientes tanta confianza como para salir."
        scene jardinseptem with dissolve
        "Intentas probar de a poco... Caminas unos pasos luego de salir por la puerta, no pasa nada."
        "Luego, caminas hasta tocar el pasto con tus pies... Tampoco pasa nada."
        scene temploseptem with dissolve
        "Te devuelvres para no levantar sospechas."
        "..."
        scene pasilloseptem with dissolve
        "Te das otra vuelta por el templo, mirando por los ventanales."
        "después de un tiempo prudente, vuelves a tu objetivo: Escapar."
        scene jardinseptem with vpunch
        "Sales por otra puerta que lleva al jardín, y esta vez corres en dirección hacia lo que parece ser un bosque."
        "Corres y corres."
        "Corres tanto que te está comenzando a faltar el aliento. Por lo que decides descansar en unos matorrales."
        "A lo lejos, vez como una sombra serpentea por el suelo."
        "Parece ser una serpiente que se dirige a tu dirección."
        "Aguantando el grito, te quedas completamente inmóvil."
        stop music fadeout 2.0
        scene negro with dissolve
        "Y cierras los ojos."
        play music "audio/the_chillout_factory.WAV" fadein 2.0 volume 0.4
        el "No deberías haber hecho eso."
        "No reconoces esa voz... es una voz femenina y ronca."
        "Al instante abres los ojos para poder ver de quien se trata."
        scene duae_end with vpunch
        "Y lo que te recibe es la figura de una entidad cubierta con un velo y ropas que se asemejan a una bata."
        "Lleva una guadaña que eleva en lo alto del cielo."
        "Y es lo último que vez."
        "BAD END: Conociendo a la segunda."
    $ MainMenu(confirm=False)()


    label badend_septem7:
        stop music fadeout 4.0
        "Buscas entre tus ropas el cuchillo que has encontrado y antes de siquiera poder sacar el cuchillo, Septem te detiene con su mano mientras chasquea su lengua."
        scene septem_lengua5 with vpunch
        play music "audio/the_chillout_factory.WAV" fadein 2.0 volume 0.4
        septem "tsk."
        "Se le ve decepcionado."
        septem "No creí que fueras tan..."
        scene septem_lengua2
        septem "Ingenuo."
        scene septemcuchillo with vpunch
        "Septem te quita el cuchillo de las manos."
        "y sonríe..." 
        scene septemcuchillo2 with vpunch
        show sangre with dissolve
        "Lo ultimo que ves es como Septem clava el cuchillo en tu cuerpo."
        "Arrebatando tu vida con este."
        scene negro with dissolve
        "BAD END: No puedes matar a un dios con un cuchillo."
    $ MainMenu(confirm=False)()

    label badend_septem8:
        scene septem_lengua2
        septem "Ja."
        show sangre with vpunch
        "Septem no duda ni un solo segundo de hacer explotar tu cabeza."
        scene negro with dissolve
        "BAD END: ..."
    $ MainMenu(confirm=False)()





    #UNUM

    label badend_unum1:
        scene hotelcomedor
        
        "No piensas lamerle las botas a este payaso."
        "¡Tienes estándares cariño!"
        "Así que ese tal Unum puede meterse su fantasía extraña por donde le quepa."
        "Tú no estás para hacer de mono de circo."
        "Punto final."

        show unumcercarisa at center with dissolve
    
        nj "Lo siento, pero yo no estoy para juegos de nadie."
        hide unumcercarisa
        show unumcercaserio at center
        "Dicho aquello, te preparas para correr a donde se ubican las escaleras, seguramente habrá una salida cerca."
        hide unumcercaserio
        "Al intentar correr te das cuenta de que algo va mal"
        "..."
        "No estás avanzando."
        "Es como si corrieras en una caminadora invisible."

        show unum2blush at right with moveinleft


        unum "JAJAJAJAJAJAJAJA"

        hide unum2blush
        show unum2duda at right

        unum "¿De verdad creíste que podrías escapar de una zona sellada?"
        hide unum2duda
        show unum2blush at right

        unum "Dios!-- Madre cada vez hace a sus regalos más tontos."
        hide unum2blush
        show unum1normal at right

        unum "Supongo que no te explico nada de nadaaa"
        hide unum1normal
        show unum1risa at right

        unum "Carajooo, eso es penoso."

        unum "Soltar a una creación a la carnicería sin siquiera explicarle nada."
        hide unum1risa
        show unum2feliz at right

        unum "¡Ojalá pudieras ver tu cara!"
        hide unum2feliz
        show unum2blush at right

        unum "PATÉTICO JAJAJAJAJAJAJAJAJAJA.... Ah."
        hide unum2blush
        show unum1normal at right

        unum "Ahhh me he exaltado..."
        stop music fadeout 1.0
        unum "..."

        hide unum1normal

        play music "audio/the_chillout_factory.WAV" volume 0.2

        "Para tu terror, Unum comienza a acercarse, llegando a invadir tu espacio personal."
        "Al no poder correr ni avanzar más allá, solo te queda esperar lo peor."
        scene badendunum1 with Dissolve (3)
        "Unum te toma de la muñeca con fuerza, y con la otra te acaricia la mejilla."
        unum "No te compartiré con nadie~"
        unum "Que septem se las ingenie con una explicación."
        unum "Yo no pienso perder la esencia."
        scene badendunum1_1 with Dissolve (2) 
        "Sientes como te rompen el pecho, una mano hurga dentro tuya en busca de algo en específico."
    
        "Cuando lo encuentra, tú ya estás perdiendo la visión."
        scene negro with Dissolve (4)
        "..."
        "BAD END: Devorado por el primero."
    $ MainMenu(confirm=False)()
    label badendunum2:
        "Tú no le tienes miedo a este cabrón, menos si es tan iluso de pensar que no intentarás escapar si te deja sin supervisión."
        "Pero no puede ser tan fácil, seguro debe tener algún modo de detectar lo que estás haciendo..."
        "Miras todas las posibles salidas, inspeccionas los pasillos que conectan con la cocina, pero no te aventuras más allá."
        "Para comprobarlo, intentas ir por donde se fue Unum, fingiendo que le buscas."
        "Pero no hay rastro de él..."
        "Te quedas ahí, pensando en lo que puedes hacer."
        "Y es ahí cuando te das cuenta... más allá del comedor, hay una puerta semi-abierta."
        "Sin pensarlo y bajo la esperanza de que puede ser una salida, vas de forma sigilosa hasta ahí."
        "Con cuidado tomas la manilla para abrir la puerta por completo y observar que hay detrás de ella."
        scene jardinunum with dissolve
        "Es el jardín."
        "Estás afuera."
        stop music fadeout 3.0
        "Sin esperar más sales corriendo lo más rápido que te permiten tus pies."
        play music "audio/the_chillout_factory.WAV" fadein 2.0 volume 0.4
        "4 zancadas alcanzas a dar después de cruzar la puerta cuando caes sintiendo un dolor punzante debajo de tus rodillas."
        scene jardinunum with vpunch
        "Caes y te revuelcas en el pasto y si no fuera por tus brazos, seguramente tendrías toda la cara raspada."
        "Intentas pararte con urgencia pero el dolor es tanto que no puedes hacer más que arrastrarte."
        "Levantas tu cabeza para entender porque tus piernas no responden."
        "!!!"
        "Con terror te das cuenta que tus  piernas ya no están conectadas con tu cuerpo."
        "Gritas hasta que tu garganta comienza a quemar."
        scene esposas with pixellate
        "Y unas risas femeninas se unen a tus gritos en un coro casi que angelical."
        "Lo ultimo que ves es como varias manos te despedazan."
        "..."
        scene negro with Dissolve(3)
        "BAD END: Conoces a las esposas de Unum."
    $ MainMenu(confirm=False)()

    
    label badendunum3:
        #Tus lagrimas lo vuelven loco asdushd.
        "Lágrimas se acumulan en tus ojos por el pánico que se empieza a formar en tu cuerpo."
        "Como puedes le comandas a tu boca para que recite una súplica que pueda salvarte el pellejo."
        nj "¡Por favor no me hagas daño!"
        unum "¿Oh?"
        "Unum te examina de cerca, centrado en tus ojos."
        "Tú intentas calmarte pero te es imposible, y no puedes evitar sollozar mientras suplicas."
        "Una vez sale una, las demás le siguen en picada. Lágrima tras lágrima salen de tus ojos para recorrer tus mejillas y luego caer en tu ropa y parte del brazo de Unum."
        stop music fadeout 4.0
        "El pelirrojo observa el recorrido que hacen tus lágrimas, con una expresión que no puedes decifrar."
        play music "audio/the_chillout_factory.WAV" fadein 3.0 volume 0.4
        nj "Por favor, juro que- {sc=4}U G H ! {/sc}"
        "Una de las manos de Unum impacta en tu mandíbula, sujetándola con fuerza."
        unum "¿QUÉ ES ESTO?"
        unum "JAJAJAJAJAJAJAJA- ¿ES LO QUE CREO QUE ES?"
        unum "DIOSSSS ES COMO SI PIDIERAS A GRITOS QUE TE DEVORE!"
        unum "Ah~"
        unum "ESA CARAA QUE ESTÁS HACIENDO-"
        unum "NO AGUANTO MÁS."
        "Algo duro te atraviesa el pecho y de a poco pierdes la conciencia."
        scene negro with Dissolve(4)
        "..."
        "BAD END: Llorando no consigues nada."

        $ MainMenu(confirm=False)() 

    return
    
    label badendunum4:
        scene habitacion
        "Palpando con tu mano, buscas el cuchillo que hay guardado debajo de tus ropas."
        show unumcuchillobadend1 with vpunch
        "Cuando lo sientes, dejas de respirar y agarras el mango del cuchillo y apuñalas a Unum en la cabeza con todas tus fuerzas."
        hide unumcuchillobadend1
        show unumcuchillobadend2
        stop music fadeout 2.0
        "Él deja de moverse. Quedándose completamente quieto."
        "Observas como el cuchillo ha conectado perfectamente en la cabeza del pelirrojo, atravesando el cráneo incluso."
        "Unum sigue sin moverse, por lo que asumes que ha muerto."
        "Sueltas todo el aire que llevas en tus pulmones e intentas quitar el cuchillo del cuerpo sin vida de Unum."
        "Está atascado..."
        hide unumcuchillobadend2
        show unumcuchillobadend3
        play music "audio/the_chillout_factory.WAV" fadein 3.0 volume 0.4
        "Una mano cubre tu agarre del cuchillo, y jalándola con fuerza, extrae el objeto."
        hide unumcuchillobadend3
        show unumcuchillobadend4
        unum "HMJA- JAJAJAJAJJAJAJA."
        "Ver a Unum vivo y sin rastro de rojo en el lugar de la herida, es una imagen chocante."
        "Más cuando, lo que emana del lugar donde ha impactado el cuchillo, sale un liquido dorado."
        unum "En serio pensaste que eso te iba a servir."
        unum "Patético."
        "Con el mismo cuchillo, Unum decide acabarte sin titubear."
        scene negro with dissolve
        "Impacta en el mismo lugar donde tú le has atacado."
        "Pierdes la vida al instante."
        "BAD END: No juegues con cuchillos."
        $ MainMenu(confirm=False)()

    label badendunum5:
        #Rechazas y Unum te deja morir ajchjkdhf
        nj "No puedo."
        scene habitacion with dissolve
        show unummanoscallado
        "Dices lo más despacio posible, con miedo a como pueda reaccionar."
        "Pero no lo harás. Ni por que tu vida esté en juego."
        unum "Hmmm..."
        scene habitacion with dissolve
        "Sus manos sueltan las tuyas lentamente. Y por un momento, Unum tiene una expresión seria."
        show unum1normal with dissolve
        unum "Está bien."
        "No te lo puedes creer. ¿Ha resultado? ¿Realmente te dejará en paz?"
        "¿Podrás salir de aquí entonces?"
        hide unum1normal
        show unum3serio
        unum "Veo que ya no tengo más razones para tenerte aquí."
        unum "Y ya no tengo hambre..."
        unum "..."
        hide unum3serio
        show unum2feliz
        unum "Puedes irte."
        scene palaciounum with dissolve
        "Unum te acompaña a la puerta principal, caminando delante de ti en todo momento... No se le ve molesto ni nada."
        "Pero tampoco tiene esa actitud ligera que lleva trayendo desde que lo conociste."
        "Es extraño verlo tan tranquilo."
        "Te abre la puerta y te invita a salir."
        "Algo está mal."
        "Pero te aferras a creer que estás a pasos de tu libertad. Con la cabeza gacha pasar por el umbral de la puerta."
        "Y Unum cierra la puerta, sin decir nada."
        scene jardinunum with dissolve
        "Ahora te encuentras afuera..."
        stop music fadeout 2.0
        "Aproximadamente alcanzas a dar 10 pasos después de cruzar la puerta cuando caes sintiendo un dolor punzante debajo de tus rodillas."
        scene jardinunum with vpunch
        play music "audio/the_chillout_factory.WAV" fadein 2.0 volume 0.4
        "Caes y te revuelcas en el pasto y si no fuera por tus brazos, seguramente tendrías toda la cara raspada."
        "Intentas pararte con urgencia pero el dolor es tanto que no puedes hacer más que arrastrarte."
        "Levantas tu cabeza para entender porque tus piernas no responden."
        "!!!"
        "Con terror te das cuenta que tus  piernas ya no están conectadas con tu cuerpo."
        "Gritas hasta que tu garganta comienza a quemar."
        scene esposas with pixellate
        "Y unas risas femeninas se unen a tus gritos en un coro casi que angelical."
        "Lo ultimo que ves es como varias manos te despedazan."
        "..."
        scene negro with Dissolve(3)
        "BAD END: Unum te dejó morir."
        $ MainMenu(confirm=False)()

    label goodend1:
        scene habitacion
        show unumesenciagoodend with vpunch
        "Atacas a la esfera que sostiene Unum en su mano."
        scene habitacion with vpunch
        stop music fadeout 4.0
        "El cae al suelo y tú solo observas, no pudiendo creer que aquello haya funcionado."
        "Pasan unos segundos y Unum sigue sin moverse."
        play music "audio/annoying.mp3" fadein 2.0 volume 0.4
        "{glitch=20.0}{color=ffffff}{b}JA eres el primero en rechazarlo, ni él se esperaba eso. {/glitch}"
        scene goodend_cuchillo with dissolve
        "{glitch=20.0}{color=ffffff}{b}Bien hecho {/glitch}"
        "GOOD END: ¿¿??"
        $ MainMenu(confirm=False)()
    
    label nogogogo:
        nj "¿Estás seguro?"
        hide unumesencia2
        show unumesencia3
        unum "Sí, lo consulté con Sextam hace un tiempo..."
        unum "Y ella dijo que no es peligroso, pues es solo un pequeño intercambio que combinará ambos genes para formar uno nuevo."
        unum "Un semidiós, descendiente de un estandarte y un humano."
        "Si bien las palabras de Unum te calman un poco, hay algo que te viene molestando desde el inicio."
        menu:
            "Pero yo no puedo embarazarme":
                hide unumesencia3
                show unumesencia_mirar
                "Unum te mira extrañado."
                unum "¿Eso es cuando los humanos hembras llevan al bebé?"
                hide unumesencia_mirar
                show unumesencia_risa
                "Tú asientes con la cabeza y Unum no hace más que reir."
                unum "¡Eso no será un problema!"
                unum "Seas capaz o incapaz biológicamente de llevar a una cría en tu cuerpo, no afectará pues no es necesario usarte como un horno."
                "¿Un horno???? ¿acaba de comparar el proceso del embarazo con cocinar en un horno? no sabes como tomártelo.... supones que lo dejarás pasar porque solo porque es una entidad totalmente diferente a los humanos."
                
            
            "Yo no... quiero embarazarme":
                hide unumesencia3
                show unumesencia_mirar
                "Unum te mira extrañado."
                unum "¿Eso es cuando los humanos hembras llevan al bebé?"
                hide unumesencia_mirar
                show unumesencia_risa
                "Tú asientes con la cabeza y Unum no hace más que reir."
                unum "¡Eso no será un problema!"
                unum "Seas capaz o incapaz biológicamente de llevar a una cría en tu cuerpo, no quiero tomar el riesgo de perderte."
                unum "Ni menos hacerte pasar por ese proceso."

        hide unumesencia_risa
        show unumesencia_explicacion
        unum "Sextam me lo ha explicado, y..."
        unum "Demora mucho..."
        hide unumesencia_explicacion
        show unumesencia_explicacion2
        unum "La cría será cultivada dentro de la nueva esencia que se formará." 
        unum "No afectará ni tu cuerpo ni el mío."
        scene habitacion with dissolve
        "Luego de decir aquello Unum pregunta una vez más, y tú más tranquilo, aceptas nuevamente."
        "Con la misma delicadeza, Unum coloca la mano que tiene su esencia en tu pecho y ejerce presión."
        "El lugar donde te está presionando comienza a sentirse caliente, no al punto de quemar ni doler, pero caliente de todos modos."
        "Hasta que algo dentro de ti se abre, permitiendo a Unum atravesar tu pecho."
        nj "Uhg..."
        unum "¿Te duele?"
        "Pregunta asustado e intenta quitar su mano, pero tú lo detienes."
        nj "No, pero se siente extraño."
        unum "Falta un poco, aguanta."
        "Ambos se quedan quietos por un largo tiempo, y te preguntas cuanto tiempo más tiene que pasar para que el intercambio de esencias termine. Mientras, Unum se dedica a observar tus facciones con fascinación."
        "..."
        "Hay un momento en que siente que tu pecho comienza a quemar, duele un poco pero te lo aguantas."
        unum "¡Listo!"
        "Unum retira su mano de tu cuerpo con la esencia que previamente era de un color parecido al oro, ahora ha tomado otro color. Unum la examina antes de dedicarte una sonrisa que muestra todos sus dientes."
        "Con sumo cuidado él coloca la esencia en tus manos. En ese proceso extrae una gran parte de la esencia, formando dos. Una de color oro."
        "Y la que tienes en tus manos, de un bello color rojo."
        "La observas por un buen rato, y puedes notar como hay movimentos dentro de la esencia. Algo se está formando..."
        "Unum por su parte, coloca su esencia en su pecho, guardándola."
        unum "Colocaré a la cría en un cuarto seguro."
        "Te avisa antes de tomarla de tus manos y llevarla fuera de la habitación."
        "... De cierta manera, sientes toda esta situación bizarra."

    return





    #NULLA
    label noaceptaste:
        nulla "Luego no digas que no te lo advertí."
        $ persistent.null = True
        $ delete_all_saves()
    return

    label badend_rutanulla:
        "Te escondes pero no concideras que sea vital ver a Nulla mientras asesina a Quattor."
        "Por lo que te escondes en un lugar que no tiene vista al altar."
        "Y esperas."
        "Y sigues esperando."
        "Pero no se escucha nada ni sientes que nada sucede allá."
        "Pero tú no mirarás."
        stop music fadeout 2.0
        "..."
        play music "audio/the_chillout_factory.WAV" fadein 2.0 volume 0.4
        el "¿Pero qué tenemos aquí?"
        "Esa no es la voz de Nulla."
        "Miras rápidamente arriba para ver de quien se trata."
        scene quattor_end with vpunch
        "Hay una mujer que está parada detrás tuyo, mirando con disgusto tu figura."
        show sangre with vpunch
        "Y eso es lo último que tus ojos ven antes de que te rompan en pecho"
        scene negro with dissolve
        "BAD END: Eliminado por la Cuarta."
        $ MainMenu(confirm=False)()
    #Que mirá bobo
    #Salí de aquí bobo







                
 

                


