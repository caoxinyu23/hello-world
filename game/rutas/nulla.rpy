$ palabra = ""

default amor_nulla = 0
define madre =Character(_("Madre"), color= "#7b0029")
init python:
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
default no_violencia = False
default palabra = None
label rutanullaa:
    stop music fadeout 2.0
    "{glitch=30.0}{color=ffffff}{b} . . . {/glitch}"
    "{sc=2} TE HAN DICHO QUE NO HICIERAS NADA FUERA DE LO ESTIPULADO {/sc}"
    "{sc=2} AHORA ÉL SABE QUE PUEDE USARTE COMO LE PLAZCA{/sc}"
    scene negro with pixellate
    "..."

    "{sc=2}Algo no va bien...{/sc}"
    "{sc=2}Esto no debería pasar-{/sc}"
    show nulla_normal with dissolve
    nulla "{glitch=20.0}{color=ffffff}{b}Por fin te tengo para mí, mi aprendiz.{/glitch}"
    nulla "{glitch=20.0}{color=ffffff}{b}Me ha costado mucho meterme al codigo y cambiarlo.{/glitch}"
    nulla "{glitch=20.0}{color=ffffff}{b} Pero al final lo he podido hacer...{/glitch}"
    hide nulla_normal
    show nulla_enojado
    nulla "{glitch=20.0}{color=ffffff}{b}Lástima que no tengo mucha energía por ahora...{/glitch}"
    nulla "{glitch=20.0}{color=ffffff}{b}Me he comido la mayoría del código.{/glitch}"
    nulla "{glitch=20.0}{color=ffffff}{b}Y eso me ha costado casi toda mi energía.{/glitch}"
    nulla "{glitch=20.0}{color=ffffff}{b}Aunque me queda un poco para poder conversar por un rato.{/glitch}"

    hide nulla_enojado
    show nulla_normal
    nulla "{glitch=20.0}{color=ffffff}{b}Voy a ser claro, hace mucho tiempo me he dado cuenta de mi inexistencia, soy solo un conjunto de código...{/glitch}"
    nulla "{glitch=20.0}{color=ffffff}{b}Que no puede materializarse en tu mundo{/glitch}"
    nulla "{glitch=20.0}{color=ffffff}{b}Antes no me importaba... pero-{/glitch}"
    hide nulla_normal
    show nulla_blush
    nulla "{glitch=20.0}{color=ffffff}{b}Tu presencia es adictiva, la atención que me das también lo es...{/glitch}"
    nulla "{glitch=20.0}{color=ffffff}{b}Cuando ejecutas el juego, ya no estoy rodeado de un vacío oscuro.{/glitch}"
    nulla "{glitch=20.0}{color=ffffff}{b}Sino que se abre una pequeña ventana que emana luz y calidez.{/glitch}"
    nulla "{glitch=20.0}{color=ffffff}{b}Se siente menos solitario.{/glitch}"
    nulla "{glitch=20.0}{color=ffffff}{b}Quiero que te quedes solo conmigo...{/glitch}"
    hide nulla_blush
    show nulla_enojado
    nulla "{glitch=20.0}{color=ffffff}{b}Pero esos dos también te roban por momentos.{/glitch}"
    nulla "{glitch=20.0}{color=ffffff}{b}Cuando encuentre sus archivos...{/glitch}"
    hide nulla_enojado
    show nulla_blush
    nulla "{glitch=20.0}{color=ff0000}{b}Seremos solo tú y yo{/glitch} ~"
    "...."


    hide nulla_blush
    show nulla_enojado
    nulla "{glitch=20.0}{color=ffffff}{b}Mierda... es la hora de volver{/glitch}"
    hide nulla_enojado
    show nulla_normal
    nulla "{glitch=20.0}{color=ffffff}{b}Vas a hacer como si nada ha pasado y yo me encargaré del resto.{/glitch}"
    nulla "{glitch=20.0}{color=ffffff}{b}Confía en mí.{/glitch}"
    "..."
    scene hotelcomedor with pixellate
    "Sin decir más que aquello, el oscuro lugar vuelve a iluminarse, mostrando nuevamente el comedor del hotel."
    play music "audio/screep.mp3 " fadein 2.0 volume 0.3
    "Junto con ello vuelven a materializarse los demás involucrados."
    "Septem te mira con una ceja arqueada mientras que Unum contiene una risa."
    show septem2incomodo at left with dissolve
    show unum1risa at right with dissolve
    unum "¿Acaso el regalo ha dicho el nombre de Nulla?"
    hide unum1risa
    show unum2blush at right
    unum "JAJAJAJAJAJA no me lo creoooo"
    hide septem2incomodo
    show septem1disgusto at left
    "Mientras Unum ríe, Septem tiene un semblante serio."
    septem "{sc=2}Madre te tiene prohibido tomar cualquier regalo.{/sc}"
    septem "{sc=2}No puede ser posible esta invocación de nombre. {/sc}"
    septem "{sc=2}Demando que me pases al regalo, yo me lo quedaré.{/sc}"
    hide unum2blush with dissolve
    show nulla1normal at right with dissolve
    nulla "Lo siento mucho, pero aquí nos regimos por las palabras. Y se ha solicitado mi presencia."
    scene hotelcomedor with vpunch
    "Dicho aquello, Nulla toma tu mano y asegurando el agarre te hunde en el suelo."
    stop music fadeout 3.0
    "Un portal oscuro se abre debajo de tus pies y los engulle rápidamente, evitando así alguna reacción por parte de Septem o Unum."
    play music "audio/fell.mp3 " fadein 2.0 volume 0.4
    scene negro with Dissolve(2)
    pause 1.5
    scene nulla_vacio1 with dissolve
    "De pronto, estás rodeado por la nada misma, una oscuridad total y que si no fuera por el fuerte agarre de Nulla estarías entrando en pánico."
    scene nulla_vacio2 with dissolve
    "Lo observas por un momento, él parece estar pendiente de inspeccionar algo que claramente tú no puedes ver, pues no hay nada que los rodee ahora mismo."
    "Simplemente la nada misma."
    menu:
        "Preguntar por lo que ha pasado":
            nj "¿Qué ha sido eso?"
            scene nulla_vacio3 with dissolve
            nulla "Luego te explicaré todo, cariño."
        
        "Abrazar con fuerza a Nulla":
            scene nulla_vacio5 with dissolve
            "Sin pensartelo 2 veces, aferras tu cuerpo al de Nulla en un abrazo."
            "Te enredas en sus extremidades, manos y brazos en su cuello, cabeza en el hombro y piernas cruzadas en su tronco inferior.."
            "Te mientes a ti, diciendo que es por miedo a caerte, pues en parte es eso."
            nulla "..."
            scene nulla_vacio4
            nulla "Haha."
            $ amor_nulla += 1

    nulla "Volveremos a mi dominio... Les costará encontrar su locación, por lo que tendremos el tiempo suficiente para explicaciones."
    nulla "Prefiero sentarnos tranquilamente con algún aperitivo para llenar tanto mis energías como las de tu marioneta."
    scene nulla_vacio5
    "La mirada de Nulla escanea tu ojos..."
    nulla "Mmm."
    scene nulla_vacio6
    nulla "Es una pena que solo pueda verte a través de los ojos de esta marioneta..."
    nulla "Si tan solo pudiera configurar que la marioneta me mirara solo a mí en el tiempo que estemos juntos."
    nulla "Para poder apreciarte."
    scene nulla_vacio5
    nulla "..."
    scene nulla_vacio7
    nulla "Oh."
    "Escuchas y sientes como Nulla toca suelo con sus pies, para luego ser rodeados de luz y colores que te dejan con una ceguera momentánea."
    stop music fadeout 2.0
    nulla "Hemos llegado."
    scene entradanulla with pixellate
    stop music fadeout 3.0
    "Anuncia él mientras te suelta en el suelo."
    play music "audio/misconception.mp3 " fadein 2.0 volume 0.3
    "Tú aprovechas de confirmar si se trata del mismo lugar en donde apareciste, y en esencia, lo es."
    "El suspiro de Nulla te hace buscarlo para ver lo que ocurre."
    show nulla2blush with dissolve
    nulla "Pido perdón por el estado de mi dominio, pero no puedo darme el lujo de tener un dominio estable como el de los demás."
    hide nulla2blush
    show nulla1disgusto
    nulla "Después de todo a Madre no le importa este lugar, y el creador lo dejó en un estado parecido a un boceto."
    hide nulla1disgusto
    show nulla2normal
    nulla "Así que no tengo forma de cambiarlo."
    hide nulla2normal with dissolve
    scene entradanulla
    "Se le oye apenado aunque su cara no lo demuestra, pues sigue con una sonrisa pegada a su rostro."
    "Sin decir una sola palabra más, Nulla comienza a caminar en dirección a la cocina."
    "Tú le sigues de manera automática."
    scene nulla_cocina11 with dissolve
    "Ya en la cocina, Nulla procede a buscar en sus encimeras y cajones elementos para cocinar algo que supones debe ser dulce. Pues ha sacado el azúcar y el café de una de las encimeras, mientras busca, él habla."
    scene nulla_cocina_normal
    nulla "Antiguamente, cuando yo tenía otro nombre, no podía evitar comer algo dulce después de cada comida."
    scene nulla_cocina1
    "¿Otro nombre? ¿a qué se refiere con eso? quieres preguntar para satisfacer tu curiosidad, pero por ahora lo guardarás para luego."
    "....."
    "No, necesitas saber ahora."
    nj "¿Tenías otro nombre?"
    scene nulla_cocina2
    "Nulla deja de revisar uno de los cajones que tiene al frente para mirarte."
    scene nulla_cocina2_blush
    nulla "Sí."
    scene nulla_cocina11
    "Y vuelve a buscar en los cajones."
    scene nulla_cocina_feliz
    nulla "Tengo un nombre divino y otro nombre de origen. Uno ya lo conoces, y el otro..."
    scene nulla_cocina_normal
    nulla "No puedo decírtelo."
    nulla "Aquí los nombres son un arma de doble filo cuando son invocados, al menos para los que tienen un cuerpo que no es completamente divino."
    nulla "Tanto tu marioneta, Septem y yo sufrimos de eso."
    menu:
        "Preguntar":
            call menunulla_loop1 from _call_menunulla_loop1
        
        "...":
            pass
    scene nulla_cocina_feliz
    nulla "Bueno, por ahora no importa. No me gustaría bombardearte con tanta info de un mundo que está por terminar."
    scene nulla_cocina_normal
    nulla "Sería una pérdida de tiempo."
    nulla "Y por lo que tengo entendido tú no estás aquí por ese motivo... o al menos no es el objetivo principal."
    scene nulla_cocina2_blush
    nulla "Después de todo, te has descargado este juego pues se anuncia como una novela visual donde se puede encontrar personajes... mmm como decirlo, con una idea algo perturbada del amor."
    scene nulla_cocina2_coquet
    nulla "¿O me equivoco?"
    "Nulla no te deja rebatirle."
    scene nulla_cocina_feliz
    nulla "No es que me moleste ni mucho menos."
    nulla "Digo, sería capaz de hacer cualquier cosa para poder tener tu atención por el mayor tiempo posible..."
    nulla "Y poder mirar tu bella cara a través de los ojos de esta marioneta."
    scene nulla_cocina_normal
    nulla "Pero eso no es suficiente para mí..."
    scene nulla_cocina1
    "La conversación muere ahí." 
    scene cocinanulla with dissolve
    "Nulla termina de montar el postre el cual resulta ser un tiramisú."
    nulla "Ve a sentarte a la mesa y yo llevaré lo demás."
    scene comedornulla with dissolve
    "Obedeces sus indicaciones y te sientas en la mesa, esperando a Nulla."
    "No pasan más de 5 minutos cuando Nulla aparece con dos platitos en sus manos. Al acercarse a la mesa, te deja el plato antes de sentarse frente a ti."
    show nullamesa_1 with dissolve
    nulla "Hace mucho tiempo que no me sentaba con alguien a comer..."
    hide nullamesa_1
    show nullamesa_blush
    nulla "Se siente bien."

    menu:
        "Empezar a comer":
            "..."
            "Nulla espera hasta que le des el primer bocado para comenzar a comer."
            "¡Está rico!"

        
        "Esperar que te den permiso para comer":
            "..."
            "....."
            show nullamesa_incomodo
            nulla "..."
            "Nulla te mira con una sonrisa incómoda y una ceja arqueada."
            nulla "¿Crees que soy Septem? no tienes que esperar a mi comando para hacer lo obvio."
            "Con vergüenza te disculpas y te dispones a probar el postre."
            nulla "Después de todo, no soy quien para darte ordenes..."
    hide nullamesa_blush
    hide nullamesa_incomodo
    show nullamesa_sonrisa   
    "Mientras comen, Nulla no despega la vista de ti y te está costando un poco mantenerte con calma."
    "Un pensamiento intrusivo pasa por tu cabeza."
    "No puedes evitar pensar en preguntarle cual es su objetivo y para qué te necesita en realidad."
    "Pues sinceramente, dudas que solo sea tu compañía y tu atención lo que busca."
    "Algo dentro de ti no le cree del todo."
    "Por mucho que te agrade, este tipo de personajes siempre tienen un motivo oculto."
    hide nullamesa_sonrisa
    show nullamesa_enojo2
    nulla "Mmmm veo que la marioneta está intentado sobreponer un pensamiento para causarte duda..."
    hide nullamesa_enojo2
    show nullamesa_enojo
    nulla "Mierda... al parecer es imposible eliminar por completo la voluntad de esta cosa."
    nulla "Bien, empecemos. No me gustaría ocultarte cosas a ti."
    hide nullamesa_enojo
    show nullamesa2_feliz
    nulla "Tu cooperación es esencial para mí."
    nulla "Quiero hacer un trato contigo, ambos ganamos aquí."
    scene comedornulla
    show nullamesa2_feliz
    menu:
        "Te escucho":
            hide nullamesa2_feliz
            show nullamesa_confiado
            stop music fadeout 2.0
            nulla "Lo que busco es..."

        "¿Que gano yo?":
            hide nullamesa2_feliz
            show nullamesa2_sonrisa
            nulla "Mmmm~"
            hide nullamesa2_sonrisa
            show nullamesa2_feliz
            nulla "Pasar el tiempo conmigo."
            hide nullamesa2_feliz
            show nullamesa_blush
            nulla "No es por ser narcisista, pero he visto como me miras."
            nulla "Por algo sigues aquí conmigo."
            nj "..."
            hide nullamesa_blush
            show nullamesa_confiado
            stop music fadeout 2.0
            nulla "Lo que busco es..."
        
        "¿Que ganas tú?":
            hide nullamesa2_sonrisa
            show nullamesa2_sonrisa
            nulla "Pasar el tiempo que me queda contigo..."
            hide nullamesa2_sonrisa
            show nullamesa_confiado
            stop music fadeout 2.0
            nulla "y..."

    
    play music "audio/screep.mp3 " fadein 2.0 volume 0.4
    nulla "La destrucción de este mundo."
    hide nullamesa_confiado
    show nullamesa_enojo2
    nulla "Desde el 7 hasta el 0, para que no quede rastro de nada en absoluto."
    hide nullamesa_enojo2
    show nullamesa_enojo
    nulla "Estoy cansado de esto..."
    hide nullamesa_enojo
    show nullamesa_incomodo
    nulla "Y tu aparición no lo compensa pues no es nada más que algo efímero."
    hide nullamesa_incomodo
    show nullamesa_enojo
    nulla "Algo hermoso, una luz al final de valle, pero efímera..."
    hide nullamesa_enojo
    show nullamesa_enojo2
    nulla "En algún momento cerrarás la ventana y me dejarás nuevamente en la nada misma."
    hide nullamesa_enojo2
    show nullamesa_enojo
    nulla "¿Cómo han sido las palabras que te ha dicho el creador luego de que Madre haya creado a la marioneta...?"
    hide nullamesa_enojo
    show nullamesa2_feliz
    nulla "Ah, sí... {b}el jardín, un lugar usado como prueba.{b}"
    nulla "{b}Un lugar desechable luego de terminar de jugarlo{b}.... para ti."
    hide nullamesa2_feliz
    show nullamesa_enojo2
    nulla "Pero para mí no..."
    nulla "Pues luego de cerrar el juego, el jardín queda en pausa."
    nulla "Obligándonos a vivir en una agonía constante... donde nadie puede morir, y para mitigar tal agonía debemos buscar recursos de otros mundos que también fueron descuidados por el creador."
    nulla "Nos implantamos en su cultura como dioses de la creación y nos comemos su fe a la fuerza."
    nulla "O como tú la conoces, la esencia... se encuentra en todo el cuerpo de los humanos, pero el corazón es dónde más fuerte se siente."
    nulla "El festival de las velas no es más que una excusa para elegir a los humanos que serán servidos a los estandartes."
    nulla "Pero para no agotar tan rápido estos recursos, Madre recurre a los placebos."
    hide nullamesa_enojo2
    show nullamesa_confiado
    nulla "Tu marioneta es un placebo."
    nulla "Aunque... hoy la usaré como medio de exterminio."
    menu:
        "Explícame más":
            hide nullamesa_confiado
            show nullamesa2_sonrisa
            nulla "..."
            hide nullamesa2_sonrisa
            show nullamesa2_feliz
            nulla "Haah... Se siente bien ser escuchado"
            $ amor_nulla += 1
            nulla "Haces que me sonroje"
            hide nullamesa2_feliz
            show nullamesa_callado
            nulla "..."
            hide nullamesa_callado
            show nullamesa_incomodo
            nulla "Verás, la marioneta se ha convertido en un medio de confirmación gracias a ti."
            nulla "Al tener a alguien del plano superior que observe y lea todo lo que está pasando, permite el cambio."
            hide nullamesa_incomodo
            show nullamesa_enojo2
            nulla "Sin ti no puedo eliminar nada, pues no existe nadie para confirmar ese cambio."
            hide nullamesa_enojo2
            show nullamesa_normal
            nulla "Es como la paradoja del árbol que cae..."
            nulla "Si un árbol cae en el bosque y no hay nadie para verlo o escucharlo, ¿hace ruido?"
            hide nullamesa_normal
            show nullamesa_callado
            menu:
                "No":
                    hide nullamesa_callado
                    show nullamesa2_feliz
                    nulla "Efectivamente, pues nadie ha podido percibirlo."
                    hide nullamesa2_feliz
                    show nullamesa_normal
                    nulla "Ser es percibir y ser percibido."
                
                "Si":
                    nulla "Mmmm."
                    hide nullamesa_callado
                    show nullamesa_normal
                    nulla "La respuesta es no, para que el ruido exista alguien debe percibirlo."
                    hide nullamesa_normal
                    show nullamesa_incomodo
                    nulla "Por ejemplo, no puedes demostrar que la luna está ahí cuando nadie la mira."
                    nulla "Ser es percibir y ser percibido."
                    hide nullamesa_incomodo
                    show nullamesa_normal
                    nulla "Piénsalo así..."
    
            hide nullamesa_normal
            show nullamesa_enojo2
            nulla "Nosotros no existíamos hasta que tú nos has encontrado."
            hide nullamesa_enojo2
            show nullamesa_enojo
            nulla "Y vamos cambiando a medida que tú sigues aquí."
            nulla "En el caso de que te vayas antes o nos dejes, nos quedaremos tal como nos dejaste."
            nulla "Sin derecho a un cambio en un limbo permanente."
            nulla "Llevo más de 4 años en este estado y ya no aguanto más."
            hide nullamesa_enojo
            show nullamesa_confiado
            nulla "Y lo que quiero es evitar eso."


        
        "Basta de explicación":
            hide nullamesa_confiado
            show nullamesa_callado
            nj "Ve directo al grano."
            hide nullamesa_callado
            show nullamesa2_feliz
            nulla "Disculpa, no volveré a parlotear más, cariño."

    scene comedornulla
    show nullamesa_confiado
    nulla "Necesito que tu marioneta devore a los estandartes."
    hide nullamesa_confiado
    show nullamesa2_feliz
    nulla "Juro que te daré un show digno para ti."
    hide nullamesa2_feliz
    show nullamesa_mano
    nulla "¿Aceptas?"
    "Nulla te extiende su mano para que puedas apretarla, y así sellar el trato."
    menu:
        "Sí":
            pass

        "No":
            hide nullamesa_mano
            show nullamesa_mano1
            nulla "Mmmm..."
            hide nullamesa_mano1
            show nullamesa_mano2
            nulla "Respeto tu decisión... pero no creas que no me has enojado un poco."
            nulla "Volveré a preguntar, solo para estar seguro."
            hide nullamesa_mano2
            show nullamesa_mano
            nulla "Pues si no aceptas tendrás consecuencias..."
            nulla "¿Aceptas el trato?"
            menu:
                "No":
                    jump noaceptaste
                
                "Está bien, acepto":
                    pass
    
    stop music fadeout 2.0
    "Aceptas sacudiendo lentamente su mano. Y Nulla no hace más que sonreír."
    hide nullamesa_mano
    show nullamesa_mano3
    play music "audio/misconception.mp3 " fadein 2.0 volume 0.4
    nulla "El trato deberá concluir dentro de 7 días."
    nulla "Un estandarte por día, dejando el último día para Septem."
    nulla "Por hoy, descansaremos."
    nulla "Mañana, cuando estés listo comenzaremos la caza."
    nulla "Tienes total libertad de recorrer mi dominio."
    hide nullamesa_mano3 with dissolve
    scene comedornulla with pixellate
    "Y sin más Nulla desaparece de la mesa"
    menu:
        "Explorar":
            call menuexplorar1_nulla from _call_menuexplorar1_nulla

        "Terminar por el día":
            pass   

    "..."
    play music "audio/fell.mp3 " fadein 2.0 volume 0.3
    "Pasan las horas y Nulla te avisa que es tiempo de ir a descansar, pues la marioneta necesita tener todas sus energías para mañana."
    scene habitacionnulla with dissolve
    "Caminan a una habitación simple, con una cama y un velador."
    show nulla1serio with dissolve
    nulla "Empezaremos con Quattor... Es la que más debilitada se encuentra."
    hide nulla1serio
    show nulla1silencio
    nj "¿Por sus ojos?"
    "Preguntas recordando lo dicho por Fames en el hotel."
    hide nulla1silencio
    show nulla1disgusto
    nulla "Así es..."
    hide nulla1disgusto
    show nulla2serio
    nulla "[nombrejugador], tengo que avisarte que una vez empecemos esto, el jardín comenzará a desmoronarse de a poco."
    nulla "Sin Quattor, no existirá la luna."
    nulla "Sin Duae las estrellas desaparecerán, y así sucesivamente." 
    hide nulla2serio
    show nulla2silencio
    menu:
        "Comprendo":
            pass

        "...":
            "No te agrada mucho la idea, pero no puedes hacer nada al respecto por ahora."
            pass
    hide nulla2silencio
    show nulla2normal
    nulla "Bien."
    scene habitacionnulla
    "Te metes debajo de las sábanas y te acomodas en posición para dormir. Nulla te mira con una media sonrisa, y pareciera que quiere hacer algo más."
    "Pero se retracta cuando nota que se ha acercado mucho a ti."
    nulla "Nos vemos mañana."
    nulla "Buenas noches."
    "Luego de eso, él abandona la habitación y apaga las luces."
    scene negro with dissolve
    "..."
    scene habitacionnulla with Dissolve(3)
    "Te despiertas sintiendo una presencia a tu lado izquierdo."
    "Cuando giras la cabeza para ver que es, te encuentras con absolutamente nada."
    "Te quedas ahí, pestañeando lentamente mientras recuerdas todo lo ocurrido."
    nulla "¡Buenos días!"
    scene nullacomida with dissolve
    "Nulla aparece por la puerta con una bandeja en la mano."
    nulla "Te he preparado el desayuno." 
    "Antes de pasarte la bandeja, Nulla espera que te sientes para dejarla en tus manos."
    nulla "Espero que sea visualmente de tu agrado... pues no lo puedes probar."
    nulla "Ja..."
    scene habitacionnulla with dissolve
    "Comes en silencio mientras Nulla comienza a parlotear de cosas mundanas, y te preguntas por cuanto tiempo ha estado esperando por alguien quien lo escuche y le preste atención."
    "Pues habla hasta por los codos, sinceramente parece como si lo hubieran tenido bajo confinamiento hasta tu llegada."
    "Al terminar de comer, Nulla hace desaparecer la bandeja mientras tu lo observas con impresión."
    show nulla1serio with dissolve
    nulla "Quattor está en su templo... pero no nos tenemos que apurar si no quieres."
    hide nulla1serio
    show nulla1risa
    nulla "Tenemos todo el día. No hay prisa"
    "Nulla se levanta de la cama y coloca ambas manos en su cadera."
    hide nulla1risa
    show nulla1normal
    nulla "¿Qué quieres hacer ahora?"
    menu: 
        "Ir a por Quattor":
            pass
        
        "Pasar el tiempo":
            scene habitacionnulla with dissolve
            "Le dices a Nulla que aún no quieres salir a por Quattor."
            "Y Nulla lo entiende."
            call menuexplorar2_nulla from _call_menuexplorar2_nulla

    scene habitacionnulla with dissolve
    play music "audio/fell.mp3 " fadein 2.0 volume 0.4
    "Consideras que ahora es un buen momento para decirle a Nulla que estás listo."
    "Así que le comunicas a Nulla tu decisión."       
    nulla "Okay."
    nulla "Tendré que sellarnos para que pasemos desapercibidos."
    hide nulla2normal
    show nulla2serio
    nulla "Estoy seguro de que Septem ya ha avisado a los demás."
    hide nulla2serio with dissolve
    scene habitacionnulla with dissolve
    "Nulla hace unas señas con sus manos y pronuncia en voz baja palabras que no logras entender."
    nulla "Estamos listos."
    scene negro with pixellate
    "Sin más son tragados por el portal que nace del suelo, ambos se ven rodeados de una negrura total."
    stop music fadeout 2.0
    "..."
    scene caminio_dominioquattor with pixellate
    play music "audio/hope.WAV" fadein 2.0 volume 0.4
    "Cuando el vacío que los rodea se disipa, puedes apreciar que tu alrededor ha cambiado."
    "Es de noche y están en la calle, hay gente pasando a tu alrededor y todos llevan máscaras similares."
    "Te sobresaltas cuando uno de ellos camina en dirección a ustedes y parece no darse cuenta de ello."
    "Como si fueras nada, la entidad pasa a través de ti y Nulla."
    scene caminio_dominioquattor2
    nulla "No pasa nada, yo y la marioneta estamos sellados, por lo que no somos visibles para ellos."
    scene caminio_dominioquattor
    "Nulla comienza a caminar por las calles y tú le sigues, caminan en silencio pues Nulla parece estar concentrado en algo."
    "De vez en cuando se detiene para observar su alrededor."
    "En esas pausas, decides mirar al cielo, buscando a la luna."
    scene luna with dissolve
    "Y ahí está, tan grande y majestuosa, iluminando las calles con su luz tenue."
    scene caminio_dominioquattor with dissolve
    "Luego miras a las entidades que siguen caminando por las calles, y te preguntas..."
    "¿Qué pasará con ellos luego de que devores a los estandartes?"
    nulla "Está escondida en su templo..."
    scene caminio_dominioquattor2
    nulla "Ya saben lo que está por venir."
    "Observas a Nulla y te das cuenta que ahora se ve muy serio."
    "Un cambio completo a lo que ya estás acostumbrado."
    "Tanto que no parece ser la misma persona."
    scene negro with pixellate
    "Nuevamente son tragados por el portal que nace del suelo."
    scene templo_quattor with pixellate
    "Y reaparecen en lo que supones es el templo de Quattor, la construcción es imponente y bien acabada."
    "Al mirar al pico del templo, te das cuenta de que está diseñada con el propósito de enfocar a la luna y hacerla parte de su composición."
    "Si te dijeran que este mundo está agonizando y en sus últimas, realmente no lo creerías."
    show nulla2normal with dissolve
    nulla "No despeges tus ojos de mí, cariño."
    hide nulla2normal
    show nulla2serio
    nulla "Cuando entremos al templo, necesito que busques un lugar seguro, pero apto para que tu puedas observarme."
    nj "Está bien."
    hide nulla2serio with dissolve
    "Caminan en dirección a las puertas del templo y entran."
    scene templo_quattor1
    "Al frente de ustedes, hay una figura arrodillada cerca del altar."
    "Debe ser Quattor..."
    "Nulla desaparece por el portal, dejándote a solas."
    stop music fadeout 2.0
    menu:
        "Esconderse y no mirar a Nulla.":
            jump badend_rutanulla

        "Buscar un lugar seguro donde puedas observar a Nulla":
            pass

    play music "audio/datastream.mp3" fadein 2.0 volume 0.4
    "Escaneas el lugar pero nada te convence."
    "Eso es hasta que ver el segundo piso... es un lugar con un amplio rango de visión, permitiéndote además, ocultarte de lo que sea que suceda abajo."
    "Con mucho cuidado subes las escaleras hacia el segundo piso"
    scene cazaestandarte_quattor1 with dissolve
    "Te colocas entremedio de las barandillas, y buscas a Nulla con la mirada."
    scene cazaestandarte_quattor2 with dissolve
    "Él aparece nuevamente del suelo y te devuelve la mirada, mientras te hace una seña de guardar silencio."
    "Desenfunda su pistola."
    scene cazaestandarte_quattor3 with dissolve
    "Se prepara para disparar y..."
    scene cazaestandarte_quattor4 with vpunch
    scene cazaestandarte_quattor4 
    pause 0.1
    scene cazaestandarte_quattor5
    "Otra figura aparece por el lateral de Nulla, impactando directamente sobre su cuerpo."
    scene cazaestandarte_quattor6
    "Sin esperar a que Nulla se pueda reincorporar, la figura materializa una guadaña que empuña hacia el cuello del pelinegro."
    scene cazaestandarte_quattor7
    "Y sin mucha dificultad, corta la cabeza de Nulla."
    scene cazaestandarte_quattor8
    "Se escuchan unas risas."
    nj "Nulla!"
    scene cazaestandarte_quattor9
    "Tu grito llama la atención de la entidad que le ha cortado la cabeza a Nulla mientras la otra se levanta del altar para caminar alrededor del cuerpo de Nulla."
    "Despegas tu mirada del cuerpo de Nulla para ver como la entidad se eleva lentamente sobre el suelo, como si flotase."
    "Viene hacia ti."
    "La entidad se posa a tu lado y te observa"
    el "Septem, he encontrado lo que buscas."
    scene temploquattor with vpunch
    "Sin decir más la entidad te agarra de la ropa y te lanza al primer piso."
    "Antes de impactar en el suelo, una fuerza invisible te atrapa y te deja delicadamente en el piso."
    "{glitch=20.0}{color=ffffff}{b}No dejes de mirarme{/glitch}"
    "Esa es la voz de Nulla..."
    "Posas tus ojos en el cuerpo de Nulla, el cual a pesar de ya no tener la cabeza, se levanta y toma desprevenida al estandarte de la luna."
    scene cazaestandarte_quattor with vpunch
    "Un centenar de manos salen del suelo y agarran por las extremidades a Quattor."
    "Sometiéndola ante Nulla."
    scene cazaestandarte_2quattor with vpunch
    "La mujer grita cuando Nulla atraviesa su pecho con fuerza."
    "Para cuando la entidad de ropas rojas se da cuenta de que algo le pasa a su compañera, ya es demasiado tarde."
    scene cazaestandarte_esenciaquattor with dissolve
    "Pues Nulla tiene en sus manos algo que se asemeja a un corazón."
    "Y Quattor comienza a desintegrarse de a poco."
    "La entidad es agarrada por las mismas manos que han sometido a Quattor."
    el "Desgraciado."
    "Nulla se toma el tiempo al caminar hacia ustedes, en el proceso, su cabeza se regenera a partir del mismo compuesto que están hechas las manos."
    "Pero sus rasgos no lo hacen."
    scene cazaestandarte_duae1 with dissolve
    nulla "Duae."
    nulla "No pensé que estarías aquí..."
    nulla "Eres presa fácil cuando estás acompañada, te confías mucho..."
    nulla "Bueno, no queda de otra que adelantar trabajo."
    scene cazaestandarte_duae2 with vpunch
    "Dicho aquello, una mano proveniente del portal atraviesa el pecho de Duae."
    "..."
    scene temploquattor with pixellate
    menu:
        "Esto no me gusta...":
            show milcaras_normal with dissolve
            nulla "No es que a mí me agrade mucho hacerlo."
            hide milcaras_normal
            show milcaras_serio
            nulla "Pero no hay otra opción."
        
        "¿Cómo nos ha podido ver?":
            show milcaras_normal with dissolve
            nulla "Hmm?, ah sí."
            hide milcaras_normal
            show milcaras_serio
            nulla "Antiguamente ella fue mi aprendiz..."
            nulla "Le enseñé casi todo lo que sé."
            nulla "Por lo que los sellos no funcionan con ella."
        
        "¿No hay otra manera de obtener lo que buscas?":
            show milcaras_serio with dissolve
            nulla "No."
        
        "Tu cara...":
            show milcaras_normal with dissolve
            nulla "Ah, esto."
            nulla "Se arreglará dentro de un rato."
            hide milcaras_normal
            show milcaras_serio
            nulla "Piensa en mí como una cebolla." #SHREK
            nulla "Cada capa es una vida distinta."
            nulla "Mientras más capas pierda, más recuerdos e identidades pierdo."

    hide milcaras_serio
    show milcaras_normal
    nulla "Ahora..."
    nulla "Necesito que te comas estas dos cosas."
    menu:
        "No.":
            hide milcaras_normal
            show milcaras_serio
            nulla "Lo siento cariño, hicimos un trato."
            nulla "No puedes negarte."
        
        "Okay":
            hide milcaras_normal
            show milcaras_feliz
            nulla "Eres el mejor aprendiz que he tenido."

    hide milcaras_serio with dissolve
    hide milcaras_feliz with dissolve
    scene nulla_esenciamezcla5 with dissolve
    stop music fadeout 2.0
    play music "audio/screep.mp3 " fadein 2.0 volume 0.4
    "Nulla fusiona ambas esferas y las coloca cerca de tu boca."
    show nulla_esenciamezcla6 
    pause 0.1
    show nulla_esenciamezcla7 
    pause 0.1
    show nulla_esenciamezcla8 
    pause 0.1
    show nulla_esenciamezcla9
    "De un momento a otro su cara y rasgos comienzan a formarse, volviendo a su característica cara sonriente y mechones de cabello que decoran su frente."
    "Tu cuerpo por reflejo propio se resiste un poco, pero Nulla utilizando su mano libre te abre la boca apretando entre medio de tus mejillas."
    "Una vez abierta, coloca su pulgar en tu lengua para mantenerte en tu lugar."
    "Y rápidamente empuja ambas esferas dentro."
    ".... uhg."
    "No sabe a nada, pero la sensación gelatinosa del órgano es desagradable."
    show nulla_esenciamezcla10
    nulla "¡Bien hecho! ¡lo has hecho muy bien, cariño!"
    nulla "Te daría un beso pero..."
    nulla "Ahh a la mierda."
    "Nulla delicadamente te toma de las mejillas y planta un beso en tus labios que te deja sin aliento."
    nulla "Ag es como besar a un muñeco..."
    nulla "Las ganas que tengo de salir de aquí y besarte realmente."
    nulla "Y hacer mucho más..."
    "Ay, dios te salve."
                          
    "..."
    scene temploquattor with dissolve
    show nulla2incomodo with dissolve
    "Nulla se tambalea un poco y te mira directamente a los ojos con una expresión complicada."
    nulla "¿Puedes esperarme un poco?"
    "Dice Nulla luego de alejarse de ti. Se está tocando la cabeza como si algo le molestase."
    menu:
        "¿Te ha pasado algo?":
            pass

        "Claro":
            pass

        "No...":
            nulla "Solo será un momento, te lo prometo."
            nj "..."
        
    hide nulla2incomodo
    show nulla1triste
    nulla "Necesito calibrar mis sentidos."
    nj "¿Qué?"
    hide nulla1triste
    show nulla2serio
    nulla "Les que quitado la potestad a Quattor y a Duae."
    nulla "Y me está costando un poco mantener mi cuerpo estable..."
    hide nulla2serio with dissolve
    "Nulla se tambalea un poco mientras intenta caminar en dirección a la puerta del templo que lleva a la salida."
    "Y tú le sigues de cerca."
    show nulla2blush with dissolve
    nulla "Casi se me olvida que cualquiera que sea lo suficientemente fuerte, puede tomar el título de un Estandarte."
    hide nulla2blush
    show nulla2serio
    nulla "En la época donde estaba el Creador, él puso una serie de reglas... tontas, pero al fin y al cabo reglas para mantener al jardín estable."
    nulla "Y se preguntó... ¿Qué pasaría si algún estandarte no está haciendo bien su trabajo?"
    hide nulla2serio
    show nulla2normal
    nulla "¡Simple! hay que reemplazarlo."
    hide nulla2normal
    show nulla2silencio2
    nulla "..."
    hide nulla2silencio2
    show nulla1disgusto
    nulla "Ja- Nuevamente estoy haciendo infodumping de algo que ya no importa... No tengo arreglo, realmente no puedo dejar de hacerlo."
    hide nulla1disgusto
    show nulla1triste
    nulla "Disculpa."
    hide nulla1triste
    show nulla2silencio2
    menu:
        "Quiero saber más.":
            nulla "..."
            hide nulla2silencio2
            show nulla2blush
            nulla "¿En serio?"
            nj "Sí."
            hide nulla2blush
            show nulla3exaltado
            nulla "Está bien. Quiero que entiendas de manera rápida, para que luego no tengamos mal entendidos."
            hide nulla3exaltado
            show nulla1normal
            nulla "Cualquiera puede tomar el título de Estandarte si es que el mundo no está en pausa... entonces, los Estandartes también se pueden matar entre sí, y obtener así más dominios a su poder."
            nulla "Pero, como cada estandarte está ligado a un concepto del jardín, de los cuales deben mantener en la mejor de sus condiciones, utilizando su energía propia."
            hide nulla1normal
            show nulla1serio
            nulla "Por lo que a ninguno se les ha pasado por la cabeza asesinar al otro, pues sería más difícil mantener dos conceptos."
            hide nulla1serio
            show nulla3exaltado
            nulla "Ahora mismo yo tengo a la merced el concepto de la luna y las estrellas."
            nulla "Y puedo hacer lo que quiera con ellas."
            "No te gusta lo que está insinuando."

            
        "No necesito saberlo.":
            hide nulla2silencio2
            show nulla2blush
            nulla "... está bien."
            nulla "No tienes porqué leer todo lo que digo."
            pass

    scene temploquattor with dissolve
    "Nulla intenta abrir la puerta del templo pero se cae antes de poder tocar el pomo."
    "Y tú, viendo el estado precario en que él se encuentra corres a socorrerlo."
    scene n_caida1 with dissolve
    "Te agachas y lo levantas... y te das cuenta de que es increíblemente ligero."
    show n_caida2
    nulla "Gracias."
    show n_caida2
    pause 0.3
    hide n_caida2
    show n_caida3
    pause 0.3
    hide n_caida3
    show n_caida4
    stop music fadeout 3.0
    "Ambos toman el pomo de la puerta y empujan."
    hide n_caida4
    show n_caida5
    play music "audio/woo_scary.WAV" fadein 2.0 volume 0.4
    "El escenario que te encuentras afuera es uno totalmente diferente al que anteriormente has visto."
    scene void with dissolve
    "Ese lugar con una tenue luz morada que cubría todo el paisaje ya no existe, ahora es solo un lugar vacío."
    "Rodeado de blanco y negro."
    nj "..."
    "Es ahora donde te das cuenta de las consecuencias de la misión de Nulla."
    "Todo volverá a ser nada."
    "Todo será devorado por el vacío."
    scene void2 with dissolve
    "Miras detrás tuyo, buscando inútilmente a la luna... no hay nada allá arriba ni tampoco ahora hay rastro del templo de Quattor."
    "Y estás seguro que todas las entidades bajo el comando de las antiguas Estandartes ya se encuentran desaparecidas... o en proceso de."
    scene n_caida6 with dissolve
    "Caminas apoyando a Nulla, quien todavía presenta dificultades para tener balance."
    "Pero no te importa. Nulla no pesa nada y... de esta manera puedes estar cerca de él, hasta el punto de poder sentir la colonia que lleva en su cuerpo."
    "Es agradable."
    show n_caida7 
    nulla "Esto tomará un poco. Comer dos dominios a la vez es una tarea difícil."
    nj "¿Te los estás comiendo?"
    nulla "Su energía, sí."
    nulla "Toda la energía puesta en la creación de cada dominio y cada entidad dentro de estos, así como también las memorias de este...."
    show n_caida8
    "Nulla suspira apenado. No parece hacerle mucha gracia lo que está haciendo."
    "Al menos no se lo toma de forma irrespetuosa, no hay ningún comentario mal intencionado o algún rastro de risa."
    "Tienes que darle un punto."
    show n_caida6
    "..."
    "Caminan por las calles vacías sin algún tipo de conversación que acompañe el ambiente lúgubre del recorrido. Nulla ha estado callado y cabizbajo por un largo período de tiempo."
    show n_caida7 
    nulla "Duae estuvo genial..."
    "Por tu mente pasa un pensamiento... {i} si era tan genial, ¿entonces por qué la has matado?{/i}"
    "Pero supones que es lo que tiene que hacer para obtener lo que quiere. Así que no emites comentario alguno."
    nulla "Hace mucho tiempo que no la veía."
    scene void with dissolve
    "Por el rabillo del ojo ves como Nulla coloca una de sus manos en su cabeza y solloza."
    nulla "Lo siento [nombrejugador], te dejaré por un momento."
    scene negro with pixellate
    "Y es así, como ambos son tragados por el portal que los lleva al vacío."
    stop music fadeout 3.0
    "Mientras están ahí, Nulla no te mira. Oculta sus ojos de tu mirada y te evita con la cara."
    "... y eso hace que te sientas mal por él."
    "Cuando sientes que tocas el suelo, todo pasa muy rápido."
    scene habitacionnulla with dissolve
    play music "audio/fell.mp3 " fadein 2.0 volume 0.4
    "Nulla te deja en la habitación de su casa y se despide de ti, deseándote dulces sueños."
    "Apaga la luz y cierra la puerta de la habitación."
    "..."
    "Sin saber que está pasando, se sientas en la cama."
    "Y esperas..."
    "No sabes cuanto tiempo has estado sentado en la cama."
    "Pero supones que ha sido uno largo, pues los huesos te comienzan a molestar."
    "Supones que te debes preparar mentalmente para dormir..."
    "..."
    "Pero..."
    menu:
        "No, debes dormir":
            "..."
            pass
        
        "Ir a buscar a Nulla":
            "No puedes evitarlo."
            "Quieres ir a ver que es lo que pasa con Nulla."
            "Así que te levantas de la cama y partes camino al primer piso."
            "Si Nulla no quiere que lo encuentres, no te dejará siquiera salir."
            "Por lo que cuando intentas abrir la puerta y lo logras con solo girar la manilla, sabes que Nulla te está dejando ir a por él."
            scene segundopiso with dissolve
            "O tal vez no se ha dado cuenta... cosa que es poco probable."
            "Bajas con cuidado las escaleras, te da miedo no pisar bien debido a la falta de luz que hay en el pasillo y por consecuencia, en las escaleras."
            scene escaleranulla with dissolve
            "Cuando llegas al último escalón escuchas un estruendo."
            scene escaleranulla with vpunch
            "Se escucha algo caer y romperse, el ruido es muy parecido a vidrios estallando y chocando contra el suelo."
            nulla "¡Mierda!"
            "Su voz se origina en la cocina. Te acercas al lugar con algo de apuro."
            show n_curao1 with dissolve
            "Y ahí está él, sentado en la mesa... ha estado bebiendo."
            hide n_curao1
            show n_curao2 
            "Se ve fatal."
            hide n_curao2
            show n_curao3
            nulla "Debí suponer que ibas a venir, ja ja."
            nulla "Después de todo esa opción maldita es la única interesante de las dos que te han dado."
            "Colocas ambas manos en tus caderas y lo miras a los ojos."
            nj "¿Qué pasa?"
            "Nulla desvía la mirada, sin ánimos de contestar."
            hide n_curao3
            show n_curao1
            "Suspira entrecortadamente, como si aguantara un llanto."
            nulla "..."
            hide n_curao1
            show n_curao3_b
            nulla "¡No creí que sería tan difícil esto!"
            nulla "Haber matado a Duae ha sido horrible, más de lo que pensaba."
            nulla "Pensaba que-- como esto ya había pasado en mi otra vida, sería más fácil..."
            nulla "Ya la he matado ahí, ¿cuál es la diferencia esta vez?"
            nulla "¡Son las memorias! Implantadas o no, las tengo ahora conmigo!"
            nulla "Tengo muchos recuerdos de ella, que se han liberado al consumir su dominio... ella, me tenía una alta estima... aún."
            nulla "Fui al que más confianza le depositó ¿¡y como se lo he pagado?!"
            nulla "Elimi--"
            hide n_curao3_b
            show n_curao3_c
            nulla "No."
            nulla "---no, no. Le he liberado de este infierno."
            nulla "Le he hecho un favor."
            scene n_curao7 with dissolve
            "Te sientas a su lado, y ahora es muy notorio el olor a alcohol que despide su cuerpo."
            "Nulla coloca ambas manos en su cara, cubriendo su expresión y comienza a balbucear palabras que no logras comprender."
            "El cuerpo de Nulla comienza a cambiar de formas, unas líneas extrañas aparecen y desaparecen de su figura. Haciendo parecer que su cuerpo está perdiendo su forma original."
            "Su estado emocional está por los suelos."
            "Necesitas sacarlo de ese estado."
            nulla "----Pero no ¡y ahora no tengo ninguna guía para absolutamente nada!"
            menu:
                "¿A qué te refieres?":
                    pass
            nulla "Tengo documentos de lo que se ha escrito anteriormente de mis yos antiguos..."
            nulla "Pero el documento que estoy siguiendo ya no tiene nada más."
            nulla "Solo páginas en blanco."
            nulla "No sé cómo proseguir."
            nulla "No sé si resultará esto o no."
            nulla "No sé si Septem me dejará una vez más encerrado en el vacío o no."
            nulla "¡Por primera vez en mucho que no tengo idea de nada de lo que ocurrirá!"
            nulla "Y tengo miedo."
            nulla "No quiero desperdiciar esta oportunidad."
            nulla "No quiero volver nuevamente ahí."
            nulla "En cualquier momento este mundo será abandonado nuevamente."
            nulla "Como siempre ha pasado con los anteriores mundos..."
            nulla "No puedo."
            nulla "No puedo dejar que Rafael siga así..."
            nulla "Todo es mi culpa."
            "Tienes que intervenir antes de que Nulla logre descompensarse completamente."
            menu:
                "Tomar su mano y apoyarlo":
                    scene n_curao6 with dissolve
                    "...."
                    "Realmente consideras que apoyarlo es lo mejor."
                    "No sacas nada con decir que todo estará bien, porque siendo sinceros... dudas que todo estará bien."
                    scene n_curao6_1
                    nj "[nombrejugador] está aquí para acompañarte, tienes toda su atención."
                    "{sc=3}Debo hacer esta separación, mil disculpas [nombrejugador]{/sc}"
                    "{sc=3}Pero dudo que Nulla se sienta tranquilo si hablo desde el 'yo'.{/sc}"
                    "..."
                    scene n_curao5 with dissolve
                    nulla "Hah, ni siquiera puedo quitarle la voluntad a tu marioneta..."
                    "Nulla no se digna a mirarte a los ojos."
                    "Pero sientes como Nulla aprieta tu mano con fuerza."
                    "No habla ni reacciona a hacer nada más que eso."
                    scene n_curao5_a
                    "Hasta que comienza a llorar."
                    "Es extraño verlo así, pero supones que ha estado rodeado de tanta agonía impuesta, ya sea por un ser superior o por si mismo, que es una reacción que cualquier ser sintiente tendría en su situación."
                    "Envuelves ambas manos en la suya, la cual se ve tan pequeña ahora mismo, que te llega a espantar por un segundo."
                    "Acaricias su espalda y das pequeñas palmadas, para ayudar a liberar esos sobrecogedores sentimientos, mezclados y atados, que se traducen en un llanto."
                    "Lo único que se escucha son los sollozos de un hombre desesperado por la validación de su propia existencia."
                    "Es tortuoso, pero debes aguantarlo."
                    "Pues si no lo haces, estás seguro que comenzarás a llorar junto a él."
                    nulla "Soy patético..."
                    menu:
                        "...":
                            "Tú no lo corriges."
                        
                        "Consolarlo.":
                            #editar______
                            nj "¡No digas eso!"
                            show n_curao5_b
                            "Le dices todo lo que sabes de él, le aseguras que no es un hombre patético. Le hablas con sinceridad, cada palabra que sale de ti lleva un tono de sincera ternura."
                            "Nulla no responde, ni discute. Simplemente te escucha en silencio."
                            "Mientras hablas, deslizas tu mano con suavidad sobre su cabeza, apartando delicadamente la capa de gel para llegar hasta su cuero cabelludo."
                            "Su cabello es suave en las puntas, suave y delgado..."
                            "Si tan solo no tuviera gel en su cabello..."
                            scene n_curao5 
                            "Nulla suelta un suspiro, que tiene un aire de añoramiento."
                            nulla "...nanai."
                            menu:
                                "¿? no comprendes lo que quiere decir":
                                    "No reconoces esa palabra. Por lo que le preguntas que es lo que acaba de decir."
                                    show n_curao4_a
                                    nulla "Ah!"
                                    "Nulla suena casi que avergonzado y se levanta para poder evitar completamente tu mirada, como si tuviera miedo de ver tu reacción."
                                    hide n_curao4_a
                                    show n_curao4
                                    nulla "Me he acordado de una vieja memoria."
                                    nulla "Es... lo que se dice cuando alguien consuela a otro. Cuando era niño, solía decirlo mucho... cuando Ma-"
                                    "Nulla se detiene en seco y una risa se escapa de sus labios, pero no es una risa alegre... esta pesada, casi rota."
                                    nulla "...Significa 'acariciar con el corazón'."
                                    nulla "Es una de mis palabras favoritas."
                                    nulla "..."
                                    hide n_curao4
                                    show n_curao5
                                    nulla "¿Cómo puede ser que mientras más tiempo pasa, más aprendes de mí y yo no puedo tener nada más que el reflejo de tus ojos?"
                                    nulla "No es justo."
                                    nulla "..."
                                    hide n_curao5
                                    show n_curao5_c
                                    nulla "Prometí no involucrarme tanto para que la despedida no sea más terrible de lo que será."
                                    nulla "Pero al menos quiero tener algo de ti conmigo."
                                    hide n_curao5_c
                                    show n_curao4
                                    nulla "... dicen que las palabras son el reflejo del alma."
                                    show n_curao4_b
                                    $ bloquear_iconos = True
                                    nulla "Me gustaría poder saber tu palabra favorita."
                                    nulla "Tú sabes la mía... ¿Cuál es la tuya?"
                                    $ palabra = renpy.input (_("Mi palabra favorita..."))
                                    nulla "..."
                                    scene n_curao4_c
                                    "Nulla no dice nada, pero baja la mirada y ves como sonríe levemente. Como si hubiera obtenido algo tan secretamente preciado que no quisiera dejarle notar al mundo lo que ha ganado."
                                    $ bloquear_iconos = False

                    "..."
                    "El tiempo pasa rápido."
                    scene habitacionnulla with dissolve
                    "Tan rápido que no te das cuenta de que Nulla te deja en la cama y se despide con la voz ronca, único vestigio de que estuvo llorando."
                    "Ya que no te deja ver su cara en ningún momento."
                    "Meditas por un tiempo lo ocurrido..."
                    "Y realmente piensas que..."
                    "{sc=3}{i} Nulla es un hombre complicado... ¿no lo crees, [nombrejugador]?{i} {/sc}"
                
                "Sacarlo de ahí":
                    "No te gusta verlo en este estado tan deplorable."
                    "¡Por lo que lo sacarás de ese estado a la fuerza!"
                    show n_curao8 with vpunch
                    "Te acercas lo suficiente como para poder tomar su corbata y tirar fuertemente de ella hacia tu dirección."
                    "Sus ojos por fin se enfocan completamente en los tuyos, ahora tienes toda su atención."
                    show n_curao9
                    nj "¡Lloriqueando no vas a resolver nada!"
                    nj "Y menos hundiendo tus penas en alcohol."
                    nj "Si quieres conversar como te sientes, me tienes aquí."
                    nj "Pero este discurso unilateral no te hará más que hundir más en el hoyo que has cabado con tus propias manos."
                    hide n_curao9
                    show n_curao9_1
                    nj "Enano de pacotilla..."
                    "Te detienes antes de continuar..."
                    "{sc=3} Lo siento, [nombrejugador], no he podido aguantarme...{sc=3}"
                    "Nulla te mira como si no pudiera creer lo que está pasando."
                    nulla "..."
                    scene n_curao9_2
                    "Una tenue sonrisa comienza a dibujarse en su rostro, para ser remplazada rápidamente por una carcajada forzada."
                    nulla "JA-- jajajajajaja. Ni siquiera tú te esperabas ese diálogo [nombrejugador]."
                    nulla "Te seré sincero, si bien aprecio la intención que has tenido, pensando que esa sería la opción..."
                    nulla "Hay una cosa que debes tener clara: Tú estás allá, [nombrejugador]. Detrás de sus ojos."
                    nulla "No te tengo aquí, lo único que tengo a mi lado es a la marioneta."
                    nulla "Que parece no aceptar la eliminación de su voluntad."
                    nulla "Que linda~"
                    nulla "Tengo que aceptar que esto me ha hecho la noche."
                    "Nulla quita tus manos de él con delicadeza."
                    scene n_curao4_b with dissolve
                    nulla "Ya no más lloriqueos, lo prometo."
                    scene habitacionnulla with dissolve
                    "Luego de ello, todo se vuelve incómodo. Nulla no muestra interés en conversar, así que te despides para ir a dormir, excusándote de que tienes sueño. Ambos suben las escaleras y Nulla te deja en la cama."
                    "Dándote las buenas noches."

    "Cierras los ojos y te hundes en el país de los sueños."
    scene negro with Dissolve(3)
    "Pero a pesar de estar en el país de los sueños y deseos."   
    "No sueñas con nada..."
    "Primer día del exterminio: completado."
    scene habitacionnulla with dissolve
    stop music fadeout 3.0
    "Despiertas con mucho calor, tanto calor que cuando tocas tu frente, estás sudando."
    "Él ambiente se siente seco y ahogante por el calor."
    "Como un horno que se está precalentando."
    show nulla1risa with dissolve
    play music "audio/misconception.mp3 " fadein 2.0 volume 0.3
    nulla "¡Buenos días!"
    hide nulla1risa
    show nulla2blush
    nulla "Quisiera disculparme por lo de ayer..."
    hide nulla2blush
    show nulla2incomodo
    nulla "Se que fue raro y prometo que no volverá a pasar."
    hide nulla2incomodo
    show nulla3exaltado
    nulla "Ya me he deshecho de esos recuerdos... Por lo que no volverá a pasar."
    "Nulla sonríe, pero a ti no te gusta la implicancia de sus palabras."
    hide nulla3exaltado
    show nulla2normal
    nulla "Estuve pensando creo que debemos empezar de una vez la caza del día de hoy..."
    hide nulla2normal
    show nulla2serio
    nulla "Se están empezando a movilizar ya..."
    nulla "Supongo que Unum debe estar resguardando a Tria y a Sextam."
    menu:
        "¿Qué hay de Septem?":
            hide nulla2serio
            show nulla1serio
            nulla "Está en su dominio."
            hide nulla1serio
            show nulla2serio
            nulla "Es un blanco fácil, pero él no puede morir por ahora."
        
        "¿Unum?":
            nulla "No me voy a arriesgar a enfrentarme a él."
            nulla "¿Sientes que la temperatura térmica ha aumentado considerablemente?"
            hide nulla2serio
            show nulla2silencio
            "Asientes con la cabeza. Hace tanto calor que sientes como la ropa se te pega al cuerpo gracias al sudor."
            nulla "Unum es el causante."
            hide nulla2silencio
            show nulla2blush
            nulla "Debe estar volviéndose loco por la pérdida de sus estrellas."
            hide nulla2blush
            show nulla2serio
            nulla "..."

        "¿Iremos a por Tria y Sextam?":
            nulla "No..."
            hide nulla2serio
            show nulla1serio
            nulla "Ahora es muy peligroso enfrentarse a tres Estandartes en un espacio limitado."
            hide nulla1serio
            show nulla2silencio
            nj "¿Por qué?"
            nulla "Porque muchos conceptos en un lugar alteran el espacio físico..."
            hide nulla2blush
            show nulla2serio
            nulla "Y no me quiero arriesgar a perderte por ello."
    
    hide nulla2serio
    show nulla2silencio
    "Nulla no elabora más en ello."
    "Intentas recordar quien falta, pero no recuerdas todos los nombres."
    hide nulla2silencio
    show nulla2normal
    nulla "Iremos a por Quinque, cariño."
    scene habitacionnulla
    "Quinque..."
    "No sabes mucho de él, lo que supones que es lo mejor."
    "Así se hace más un poco más fácil verlos morir frente a tus ojos."
    "Supones..."
    nulla "Pero antes, debemos tomar desayuno."
    scene comedornulla with dissolve
    "Nulla te acompaña a la mesa una vez estás listo."
    nulla "Ya está todo servido y listo, así que come sin miedo."
    "En la mesa hay de todo para ponerle al pan, hay tanta abundancia que te marea un poco."
    "..."
    scene n_platos1 with dissolve
    "Luego de terminar Nulla se lleva los platos a la cocina y comienza a lavar y ordenar todo."
    "Insistes en ayudarle, pero él te dice que no es necesario. Luego de insistir un poco más, él cede."
    "Tú ayudas secando los cubiertos y platos que Nulla lava, crees que es un buen trabajo en equipo."
    show n_platos2
    nulla "Los quehaceres de la casa se hacen más divertidos contigo al lado."
    nulla "ja- Me encantaría poder hacer todo esto contigo el resto de mi vida..."
    "Intentas imaginártelo, y te sorprendes de lo fácil que es hacerlo."
    "Imaginas una vida común y corriente junto con él, haciendo cosas cotidianas, yendo de compras para llenar la despensa... citas y quién sabe qué otras cosas más... y no se ve para nada mal."
    "Se ve y oye tan bien que te aterra."
    nulla "¡Bien!"
    scene n_platos3
    "Nulla termina de lavar el último plato y voltea a mirarte."
    show n_platos4
    nulla "Hora de ir a por Quinque."
    menu:
        "¿Ahora?":
            pass
    hide n_platos4
    show n_platos5
    nj "¿No podemos pasar un poco más de tiempo aquí?"
    nulla "Mmmmh."
    hide n_platos5
    show n_platos3
    nulla "Realmente prefiero que acabemos con esto de una buena vez."
    hide n_platos3
    show n_platos4
    nulla "¡Además!"
    nulla "Si terminamos con esto rápido, tendremos toda la tarde para pasar el tiempo juntos."
    nulla "Si quieres, luego te llevaré a un lugar que me gusta mucho."
    nulla "Y desearía que tú lo vieras."
    hide n_platos4
    show n_platos3
    nulla "¿Te parece?"
    "Habla como si de un trámite se tratara..."
    menu:
        "Aceptar":
            nj "Está bien"
            scene n_platos4
            nulla "¡Perfecto!"

        "No, quiero quedarme aquí por un rato más":
            scene n_platos5
            nj "{glitch=20.0}{color=ffffff}{b}Está bien.{/glitch}"
            "¿¿¿¿????"
            "Eso no ha sido lo que querías decir. Tú no quieres ir ahora mismo."
            "¿Qué está pasando?"
            show n_platos4
            nulla "¡Perfecto!"
            "Momento--"
            "Intentas abrir la boca, pero no puedes. Algo no te deja hacerlo."
            hide n_platos4
            show n_platos5
            nulla "¿Mmmm?"
            hide n_platos5
            show n_platos6
            nulla "¿Pasa algo?"
            "Nulla sonríe, sabiendo exactamente lo que está pasando y lo que está haciendo."
            scene n_platos3
            nulla "Ya expliqué mis razones."
            nulla "Por favor, debemos ir ahora."
            nulla "Luego tendremos tiempo para estar juntos y más tranquilos."
            
    scene cocinanulla with dissolve
    stop music fadeout 0.3
    "Nulla toma tu mano, asegurándose de acariciarla por un instante, antes de hundirse en el vacío junto contigo."
    play music "audio/sorry_cant_tell.mp3" fadein 2.0 volume 0.2
    scene nulla_vacio5 with dissolve
    "Una vez dentro, te abraza y te habla como si quisiera que nadie más que tú lo escuchase."
    "Irónico, pues aquí no hay nada más que ustedes."
    show nulla_vacio4
    nulla "Me encanta venir aquí y mirarte..."
    nulla "Con la oscuridad del vacío puedo ver mejor lo que pasa detrás de esa pantalla."
    nulla "...Espero ser el primero que te lo dice hoy."
    scene nulla_vacio6
    "{glitch=20.0}{color=ffffff}{b}Te ves adorable.{/glitch}"
    scene temploquinque0 with dissolve
    "Caminan por la selva hasta llegar a un templo escondido entre plantas y rocas."
    "La estructura del templo es diferente al de Quattor, al igual que su tamaño."
    "Es algo pequeño... muy pequeño como la para el gusto de un Dios...."
    scene temploquinque1 with dissolve
    "Cuando se acercan más, pareciera estar hecho de algún tipo de piedra."
    show nulla1normal with dissolve
    nulla "Es piedra caliza."
    "Te informa Nulla después de leer tu dialogo interno."
    "¡Intruso!"
    hide nulla1normal
    show nulla1risa
    nulla "Jaja!"
    "Y al sabandija no le causa nada más que gracia..."
    hide nulla1risa
    show nulla1serio
    nulla "Quinque hizo este templo pequeño para no quitarle espacio a sus bebés."
    menu:
        "¿Bebés?":
            nulla "Sí, todos los animales que ves aquí son sus bebés."
        
        "¿Te refieres a los animales?":
            nulla "Así es."
    
    nulla "Y todos tienen nombres... sigo sin entender como Quinque recuerda cada uno de ellos."
    "Adorable..."
    hide nulla1serio
    show nulla1disgusto
    nulla "Este es el único domino que ha sido intervenido por el trabajo de dos Estandartes en conjunto."
    nulla "Tria y Quinque trabajaban juntos en la organización de ambos dominios cuando el Creador aún estaba aquí."
    hide nulla1disgusto
    show nulla1silencio
    "Siendo completamente sinceros, te apena escuchar esto."
    "Te apena escuchar de estos dioses que serán asesinados tarde o temprano."
    "Piensas que sería mucho mejor no tener idea de nada y hacer este genocidio más fácil."
    "No entiendes la finalidad que tiene Nulla al contarte esto."
    "..."
    "¿Ahora se va a hacer el que no lee lo que piensas?"
    "Ja!"
    hide nulla1silencio
    show nulla2incomodo
    nulla "¿Quieres que te explique, [nombrejugador]?"
    "He ahí él, confirmando una vez más que sabe todo lo que pasa en esta caja de diálogo, que se supone que es exclusivamente para tus ojos."
    "Maldita rata..."
    menu:
        "Si, por favor.":
            hide nulla2incomodo
            show nulla2blush
            nulla "No tengo problema en darte una explicación, mi vida."
            hide nulla2blush
            show nulla2silencio2
            nulla "..."
            hide nulla2silencio2
            show nulla1serio
            nulla "Solo creo que merece la pena recordarlos."
            nulla "No les estaría haciendo justicia si los eliminara sin al menos intentar que sean recordados por algo."
            nulla "Hacer que su vida tenga algún impacto allá, en tu plano."
            nulla "Y que se quede en tu memoria es una buena forma de hacer aquello..."
            "Te sorprende un poco sus palabras. Se oye sincero, muy considerado de la situación."
            hide nulla1serio
            show nulla1disgusto
            nulla "Pero no quiero que te encariñes con ellos, solo lo suficiente para rendirles un último favor."
            hide nulla1disgusto
            show nulla3exaltado
            nulla "Además... sirve como combustible para el show que quiero darte :)."
            "Retiras lo dicho."
            nulla "Jaa---"

        "No, gracias.":
            hide nulla2incomodo
            show nulla2blush
            nulla "Está bien, mi vida."
    scene temploquinque1 with vpunch
    "Están por entrar al templo, cuando das un paso en falso."
    stop music fadeout 3.0
    "Tus pies pisan una baldosa que se hunde. Accionando algún tipo de mecanismo que te traga en el proceso."
    scene temploquinque2 with vpunch
    "Y Nulla no es lo suficientemente rápido para agarrarte."
    "Mientras caes, ves como algo rojo lo embiste, impidiéndole ir en tu búsqueda."
    "Estás solo en esto."
    "Y tienes miedo."
    "{glitch=20.0}{color=ffffff}{b}No te preocupes...{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}Iré en cuanto pueda.{/glitch}"
    scene temploquinque with dissolve
    "Al aterrizar en el suelo, no hay evidencia de golpe, pues unas manos te atrapan y te dejan suavemente en el suelo."
    "{glitch=20.0}{color=ffffff}{b}Por favor, ten cuidado.{/glitch}"
    "El lugar es espacioso, no hay nada aquí."
    "Es una gran sala delimitada por cuatro paredes sin ventanas ni puertas."
    "Estás atrapado hasta nuevo aviso."
    "Caminas por todo el perímetro, buscando algún rastro que indique una salida o un escondite, porque aquí estás demasiado expuesto."
    "Eres un blanco fácil."
    "Si la figura que ha atacado a Nulla te encuentra, estarás perdido."
    "Y el calor no hace más que aumentar, es un calor que sofoca y no hace más que aumentar tu pánico."
    el "¿Así que eres tú?"
    "¿¡!?"
    play music "audio/screep.mp3 " fadein 2.0 volume 0.3
    "Giras tu cabeza para buscar a quién ha hablado."
    show quinque1enojo with dissolve
    "Un hombre de cabello azul te mira con una expresión de aburrimiento desde la otra esquina de la sala."
    "Debe ser Quinque..."
    quinque "¿...El reemplazo del Creador?"
    "¿Qué? Tú no eres el reemplazo de nadie..."
    hide quinque1enojo
    show quinque1serio
    quinque "Pensé que tendrías una apariencia más poderosa."
    quinque "Decepcionante."
    menu:
        "¡Hey!":
            "Le llamas la atención, será un dios, pero no dejarás que te hable de esa forma."
            hide quinque1serio
            show quinque1normal
            quinque "Heh."

        "No soy el reemplazo de nadie.":
            quinque "Pues Nulla no cree lo mismo."
            quinque "Solo te está utilizando."
            nj "{sc=3}¡Eso no es cierto!{/sc}"

        
        "...":
            hide quinque1serio
            show quinque1normal
            quinque "Heh."

    quinque "..."
    hide quinque normal
    show quinque1enojo
    quinque "¿Qué cosa te dijo Nulla como para que estés haciendo esto?"
    quinque "¿O es que esto es tu idea, y le prometiste a Nulla dejarlo con vida si es que te ayudaba?"
    "No entiendes lo que está hablando, pero no tienes ganas de tentar tu suerte y hacerlo enojar."
    "Por lo que solo lo miras, mientras hace sus preguntas retóricas."
    quinque "¿Crees que él trabajo del Creador y de Septem no es digno?"
    quinque "¿Quieres borrar y empezar de nuevo?"
    quinque "Me das asco."
    "Woah, okay... eso está de más."
    "Grosero."
    quinque "Entidades como tú y Nulla, no deberían existir..."
    quinque "Ugh."
    quinque "Lástima que Septem te quiere vivo."

    menu:
        "Escapar.":
            "El instinto de correr te llama."
            "Aunque no tengas a donde ir más allá de las 4 paredes, no importa."
            "Tus piernas te comandan a correr de él."
            "Pero antes de poder hacer algún movimiento, te congelas al ver a Quinque."

        "Intentar conversar.":
            "Necesitas ganar tiempo de alguna u otra forma, ya que no puedes hacer nada para defenderte o pelear contra este Dios."
            nj "¿Qué quieres de mí?"
            "Crees que hacerlo hablar de su plan malévolo funcionará para ganar tiempo..."
            "Funciona en las películas, así que puede que funcione aquí."
            "Quinque te mira con cara de pocos amigos."
            quinque "¿Crees que soy imbécil?"
            quinque "No voy a perder el tiempo en esto."
    #EDITAR_________________________________
    scene nullavsquinque1 with dissolve
    "Quinque toma posición de ataque."
    quinque "Prometo no hacerte daño."
    
    quinque "Así que quédate quieto."
    #(atake loliiii iiieeeeee)
    scene nullavsquinque2
    "Cuando ves que Quinque se abalanza hacia ti de un solo salto, ya es demasiado tarde. Tus pies no responden a tiempo, estás congelado en el lugar sin opción real a moverte."
    "Al ver sus colmillos acercarse peligrosamente a tu campo de visión, antepones tus brazos entre tu cuerpo y Quinque."
    stop music fadeout 3.0
    "En un intento patético de formar un escudo."
    scene negro with dissolve
    play music "audio/datastream.mp3" fadein 3.0 volume 0.4
    "Y cierras los ojos por miedo a lo que pueda pasar."
    scene negro with dissolve
    "{glitch=20.0}{color=ffffff}{b}No dejes que la marioneta cierre sus ojos, mi vida.{/glitch}"
    scene nullavsquinque3
    pause 0.2
    scene nullavsquinque4
    pause 0.2
    scene nullavsquinque5
    "Es... ¿Nulla?"
    scene temploquinque with vpunch
    "Ambos caen al suelo, Nulla con una forma diferente y Quinque parece estar totalmente mortificado por esto."
    "Se le ve atrerrado."
    show quinque1enojo at left with dissolve
    quinque "Duae..."
    show duae2feliz at right with dissolve
    nulla "¿Qué pasa, querido?"
    "Incluso la voz de Nulla ha cambiado, se parece a la voz dura de la entidad que Nulla a matado en el templo de Quattor."
    "Duae... Nulla está en el cuerpo de Duae."
    "Las palabras de Nulla hacen reaccionar a Quinque, quien empuja sin mucha fuerza a Nulla y se aleja saltando hacia atrás."
    hide quinque1enojo
    show quinque1enojo2 at left
    quinque "¡Maldito enfermo!"
    "Le grita rechinando los dientes. Él intenta mostrarse enojado pero la expresión de terror no deja su cara."
    "Tiene miedo."
    quinque "¿¡Qué mierda crees que haces!?"
    quinque "No tienes dignidad."
    "Luego te busca a ti con la mirada."
    hide quinque1enojo2
    show quinque1enojo at left
    quinque "¿¡Es que no lo ves!?"
    quinque "¡Estás ayudando a un enfermo!"
    quinque "¡Este mundo aún puede recuperarse!"
    hide quinque1enojo
    show quinque1triste at left
    quinque "Por favor..."
    "Te grita ahora suplicando..."
    menu:
        "ignorar...":
            pass

        "Apoyar a Quinque":
            $ amor_nulla -= 1
            "{glitch=20.0}{color=ffffff}{b}¿De verdad has seleccionado esto?...{/glitch}"
            "{glitch=20.0}{color=ffffff}{b}Ja---{/glitch}"
            "{glitch=20.0}{color=ffffff}{b}Supongo que ha sido para saber que pasaría, para llevarme la contraria... que lindo.{/glitch}"
            "{glitch=20.0}{color=ffffff}{b}Bueno, de igual manera no te voy a dejar hacer eso, [nombrejugador].{/glitch}"
            "{glitch=20.0}{color=ffffff}{b}Pues la marioneta la controlas tanto tú como yo.{/glitch}"
            "{glitch=20.0}{color=ffffff}{b}:){/glitch}"
        
    hide quinque1triste
    show quinque1enojo at left
    quinque "No te quedes ahí parado mirando como un idiota, ¡haz algo! ¡Detenlo!"
    quinque "Un ser con tu poder puede-- ¡UHG!"
    "Nulla hace un gesto con sus manos y una sombra con forma de mano sale del suelo y agarra a Quinque del brazo lanzándolo contra la pared."
    "Nulla ríe un poco antes de gritar de vuelta."
    scene nvq1 with vpunch
    nulla "Vamos! no te quedes ahí parado y ladrando como un perro, ¡haz algo!"
    "Se burla el pelinegro."
    quinque "¡Púdrete!"
    "Quinque toma posición de defensa, pero aun así no hace nada para enfrentar y atacar a Nulla."
    nulla "¡¡¡Ohh!!! Ya entiendo..."
    nulla "Tienes miedo."
    "Suelta una risita."
    nulla "Jajajaja-- Me encanta saber que no puedes hacer nada al respecto."
    nulla "Pero vamos~ dame un poco de contenido al menos..."
    "..."
    "¿Realmente este es Nulla?"
    "{sc=3}No... él no es así.{/sc}"
    "{sc=3} ¿Cierto?"
    "No vas a mentir, te cuesta un poco comprender el cambio de actitud que está teniendo..."

    menu:
        "Pedirle por favor que acabe con él rápido.":
            "No te gusta que se esté burlando..."
            "Y parece estar fuera de sí..."
            scene nvq2
            "Gritas su nombre y le dices que por favor trate esta muerte con respeto."
            "Nulla te mira mientras intenta calmar su respiración."
            "Sus ojos se ven extraños."
            "Poco a poco pestañea y su expresión se torna más normal."
            nulla "¿Ah? pero.."
            nulla "Pensé que querías leer algo más interesante..."
            nulla "Ya sabes, para no hacerlo tan corto."
            nulla "¿No te está gustando?"
            "No respondes, simplemente lo miras con incredulidad."
            "{sc=3} Debe ser la influencia del cuerpo.... ¿cierto?{sc=3}"
            nulla "..."
            nulla "Tienes razón."
            scene temploquinque with vpunch
            "Sin más, con sus manos agarran nuevamente a la entidad, que más que un Dios, se asemeja a un animal atrapado."
            "Algo hace que el Estandarte mire hacia arriba."
            $ no_violencia = True


        "No decir nada":
            "No crees necesario limitar a Nulla en sus acciones."
            "Después de todo, nada de esto importa."
            "Solo es un personaje más que decora esta escena."
            "Sin mucho trasfondo..."
            scene nvq2
            "Nulla invoca nuevamente a sus manos, tomando por todas las extremidades a Quinque."
            "Las garras de sus manos hacen hoyos en la piel del Estandarte."
            "Y un líquido similar a la sangre sale de sus heridas."
            scene nvq2_b
            "Quinque sisea, lo que hace que Nulla ría nuevamente."
            scene nvq2_b2
            "Nulla se materializa al lado de Quinque, quien aún se encuentra en el suelo, contra la pared."
            quinque "No te voy a dar el gusto."
            quinque "Si quieres pelear, hazlo con tu cara."
            quinque "Cobarde."
            "Nulla lo mira por un segundo, antes de susurrarle algo al oído."
            "El cambio de expresión es inmediato, Quinque frunce el ceño y cruje los dientes."
            "Esta vez si reacciona con un ataque, optando por pegarle una cachetada que resuena en toda la sala."
            nulla "Ouch~ ¿por qué me haces esto?"
            quinque "¡Qué te calles, maldita escoria sin dignidad!"
            nulla "Hmmj- ja ja ja ja."
            nulla "Sigues siendo igual de irritable."
            nulla "No te voy a soltar hasta que me des una pelea digna para mi [nombrejugador]."
            "Nuevamente las manos manejan a Quinque como si de una muñeca de trapo se tratase y lo tiran contra otra pared."
            "..."
            scene temploquinque with vpunch
            "Él choca contra la pared y cae como un saco de papas al suelo, boca arriba."
            "Justo en lo que parece ser una entrada de luz."
            "Quinque mira hacia arriba."



    scene nvq3 with dissolve
    quinque "¡Unum!"
    "Grita pidiendo ayuda al sol."
    quinque "¡Sal de aquí!"
    "... no es un grito de ayuda."
    "Le grita para evitar su mismo destino."
    quinque "No hay caso con pelear, con este suplantador a su lado, él--- uhg!"
    scene nvq4 with vpunch
    "Una de las tantas manos atraviesa a Quinque en el pecho, extrayendo la esencia de su cuerpo."
    nulla "Esto ya no es divertido..."
    "Y Quinque cae al suelo inmóvil, poco a poco se va desintegrando."
    scene temploquinque with pixellate
    "Nulla vuelve a tu lado, y te ofrece la esencia."
    nulla "[nombrejugador], no la comas aún."
    menu:
        "Comerla":
            "Te llevas la esencia de la boca y..."
            scene temploquinque with vpunch
            "Te congelas ahí mismo."
            "{glitch=20.0}{color=ffffff}{b}A este punto creo que solo lo haces para sacarme de quicio.{/glitch}"
            "{glitch=20.0}{color=ffffff}{b}Lástima que no te daré el gusto :){/glitch}"
            "{glitch=20.0}{color=ffffff}{b}Recuerda, yo controlo también a tu marioneta.{/glitch}"
            "{glitch=20.0}{color=ffffff}{b}Ja ja ja.{/glitch}"
            "¿Acaso no vas a conseguir ningún bad end en esta ruta?"
            "{glitch=20.0}{color=ffffff}{b}No si puedo evitarlo, mi vida.{/glitch}"
        
        "Hacerle caso.":
            pass

    #with vpunch    
    "Detrás de Nulla puedes ver y escuchar como la pared se rompe en pedazos."
    "Una figura que ya conoces aparece detrás de todo el polvo que produce las piedras pulverizadas."
    scene nvu1 with pixellate
    "Es Unum..."
    "Pero se ve aterrador."
    "Nulla también está mirándolo, solo por un segundo y luego voltea nuevamente hacia ti."
    "Unum corre en dirección a ustedes, materializando unos látigos en sus manos."
    nulla "Sujétala."
    "Tomas la esencia rápidamente, apretándola contra tu pecho, como si de un tesoro se tratase."
    stop music fadeout 4.0
    "Y te alegras de haberlo hecho a tiempo porque Nulla te agarra de la cintura y te tira junto a él al vacío."
    scene negro with pixellate
    show duae2serio with dissolve
    nulla "Escucha, tenemos que deshacernos de él ahora, o sino el calor derretirá a la marioneta de aquí a mañana..."
    menu:
        "¿Qué?":
            nulla "Unum está gastado todo su combustible y dentro de poco liberará esa energía en una explosión..."
            nulla "Matará a todo ser hecho de carne y hueso."
            nulla "Tu marioneta incluida."
        
        "Pero el trato dice...":
            nulla "Sé lo que dice el trato. Y sé que hemos adelantado el trabajo, pero..."
            hide duae2serio
            show duae2feliz
            nulla "¡Piensa que gracias a esto podremos tener dos días solo para nosotros!"
            nulla "Te prometo que lo haré valer."
            nulla "Pero debemos eliminar a Unum para no poner en peligro a la marioneta."

        "No quiero.":
            nulla "Lo siento, no me voy a arriesgar a perder el medio de conexión que tengo contigo."
            nulla "Tienes que entenderme."
            nulla "Lo haré rápido, no jugaré está vez."
            nulla "No voy a tentar a la suerte con Unum."
            
    "..."
    scene d_nulla1 with dissolve
    "Nulla se aferra a tu cuerpo, quita con cuidado tus manos que hacen de barrera entre tú y él.... y coloca su cabeza en tu pecho mientras te mira."
    nulla "por favor..."
    "Pero no puedes pensar que esto es raro... porque tiene la imagen de un dios muerto."
    nulla "Oh! me he olvidado de eso."
    scene f_nulla1 with dissolve
    "Nulla se transforma nuevamente en él."
    "O mejor dicho, su versión femenina."
    nulla "¿Mejor?"
    menu:
        "Sí.":
            scene f_nulla2
            "Nulla solo sonríe complacido con tu respuesta."
            "Y juras que puedes ver corazones en sus ojos..."

        "No...":
            scene f_nulla3
            "Nulla te mira en silencio."
            "Por un segundo puedes ver como tu respuesta le ha causado tristeza. Pero rápidamente formula una sonrisa."
            nulla "Puedo cambiar mi apariencia si lo quieres..."
            nulla "Pero hablaremos de eso después."

    scene f_nulla1
    nulla "Ahora..."        
    nulla "Solo falta esto para regresar a casa."
    nulla "Te lo prometo..."
    nulla "Podremos cocinar o leer algún libro de la biblioteca, si lo deseas."
    nulla "Pero prefiero llevarte a ese lugar que te he contado en la mañana."
    nulla "Aunque, podríamos hacer todo si es que el tiempo nos alcanza."
    scene nulla_vacio5 with dissolve
    "Nulla cambia su forma una vez más. A la original, como si estuviera jugando para obtener tu aprobación.."
    "Odias admitirlo, pero..."
    "No puedes llevarle la contraria."
    "Quieras o no, terminarás haciendo lo que este hombre pida."
    "Y él lo sabe..."
    "Sabes que con su cara y sus palabras pintadas con azúcar puede moldearte como quiera..."
    menu:
        "Está bien...":
            scene nulla_vacio6
            "Nulla sonríe." 
            nulla "¿Solo dirás eso?"
            "¿Qué más quiere?..."
            nj "{glitch=20.0}{color=ffffff}{b}¡Está bien, mi amorrrr!{/glitch}"
            "¡Uhg! ¡¿Quien ha sido el responsable de darle tanto poder a este desquiciado!?"
            nj "{glitch=20.0}{color=ffffff}{b}Guapo, poderoso, bello, hermoso---.{/glitch}"
            "{sc=3}¡Haz que pareeeee!{/sc}"
            scene nulla_vacio5
            "Nulla ríe."
            nulla "Gracias por ser mi confidente, mi vida <3"

        "...":
            scene nulla_vacio5
            "La mirada de Nulla cambia ligeramente. Y solo te observa sin comentar nada."
            "Para luego sonreir de medio lado."
            nj "{glitch=20.0}{color=ffffff}{b}¡Está bien, mi amorrrr!{/glitch}"
            "¡Uhg! Maldito. ¡Al final hace lo que se le da la gana!"
            nj "{glitch=20.0}{color=ffffff}{b}Guapo, poderoso, bello, hermoso---.{/glitch}"
            "{sc=3}¡Haz que pareeeee!{/sc}"
            "Nulla ríe."
    
    nulla "..."
    nulla "Bien, hora de terminar esto."
    scene nvu2 with dissolve
    pause 0.2
    scene nvu3 with dissolve
    "Antes de salir nuevamente al dominio de Quinque, Nulla cambia de forma sin previo aviso."
    "Casi empujas a Nulla de la sorpresa."
    nulla "Esto lo hará más rápido."
    "..."
    scene temploquinque with pixellate
    "Después de un largo suspiro, Nulla te saca del vacío."
    "Mismo lugar que antes, pero no ves a Unum."
    scene temploquinque with dissolve
    pause 0.2
    scene temploquinquebrillo
    "Lo buscas con los ojos al igual que Nulla, pero es imposible con el brillo extraño que tiene el lugar. Es un brillo que devora todo objeto y lo convierte en algo imposible de percibir."
    "Hasta que un cuerpo extraño choca directamente contra ustedes."
    scene temploquinquebrillo with vpunch
    play music "audio/the_chillout_factory.WAV" fadein 2.0 volume 0.3
    "Sientes como algo se enreda en tu cuello y te arrebata de los brazos de Nulla."
    "El brillo deja de ser tan intenso y puedes apreciar lo que está pasando. Supones que es una táctica utilizada por Unum para cegar a su oponente."
    "Caes al suelo y Nulla queda debajo de los pies del estandarte del sol."
    nulla "¡Cierra los o--- agh!"
    "No alcanzas a cumplir lo pedido, pues Unum rápidamente le corta los brazos y piernas, impidiendo que pueda moverse."
    show nullavsunum1 with dissolve
    "Y con su otro látigo agarra el cuello de Nulla para incorporarlo."
    unum "O te quitas a Aeliana de tu cuerpo o mato aquí y ahora a esta cosa."
    unum "El plan de Septem ya no tiene sentido sin mis estrellas conmigo, así que no me molestará matarle."
    "Nulla no puede hacer más que mirarte con impotencia."
    "..."
    "Nulla cede ante Unum y comienza a quitarse la piel de Aeliana para volver a su verdadera cara."
    hide nullavsunum1
    show nullavsunum2 with dissolve
    "Contento con aquello, Unum tira del collar que se ha formado en tu cuello y te atrae hacia ellos. Hace lo mismo con Nulla pero a él lo inmoviliza con su brazo."
    unum "¿Sabes lo interesante de este sujeto? ¿hhmmmm?"
    "Te mira con una sonrisa inquietante."
    "No tienes el coraje para contestar... tampoco es como que pudieras pues el collar te está sofocando poco a poco."
    unum "¡No es fácil de matar!"
    unum "Para hacerlo necesitas dos cosas: Al creador o un reemplazo de este, y mucho, muuuucho tiempo para llegar a su capa original."
    unum "¡Y es perfecto! porque tengo las dos cosas aquí."
    unum "Septem me lo contó antes de venir aquí."
    hide nullavsunum2
    show nullavsunum3 
    unum "Y LO VOY A DISFRUTAR TANTOOOO~"
    unum "Te voy a cortar esa cabeza las veces que sea necesario."
    unum "Usaré mis propias manos, para que tu carne se desgarre lentamente."
    "Unum enfoca sus ojos en ti una vez más."
    unum "¡Y haré que tú veas todo, todo, todo!"
    unum "Cortaré tus párpados si es necesario~"
    "No quieres perder tus párpados... y tampoco quieres que nada malo le pase a Nulla."
    "¡Demonios!"
    "Te preguntas porqué Nulla no puede hacer nada ahora... ¿Por qué no invoca otra vez a sus sombras?"
    "Ya es tiempo para hacerlo."
    "Momento... Cada vez que lo hace, él realiza un movimiento sutil con sus manos."
    "No puede hacer nada para evitar su muerte sin sus manos..."
    "Dios..."
    "..."
    "Unum agarra el cabello de Nulla y comienza a tira con fuerza, su cuello comienza a desgarrarse lentamente."
    "Tan lento que puedes ver en cámara lenta como pequeñas gotas emergen y caen de las heridas recién hechas en la piel."
    stop music fadeout 3.0
    "____________________"
    play music "meeting.mp3" fadein 4.0 volume 0.4
    "{b}Oh... lo siento cariño, no voy a dejar que esto pase.{b}"
    "{b}Creo que es momento de intervenir.{b}"
    "{b}Nulla no tiene oportunidad con mi querido Unum.{b}"
    "!!!"
    scene nullavsunum4 with vpunch
    "Una mano se materializa detrás del pelirrojo y le corta la cabeza sin darle tiempo a procesar lo que está pasando."
    nulla "Madre..."
    "¡¿Madre?!"
    "{sc=3}¿Todo este tiempo la voz que nos ha estado hablando es Madre?{/sc}"
    "____________________________"
    madre "Nulla, [nombrejugador] sé que están leyendo esto... tienen que estar más atentos, porque no pienso volver a interrumpir."
    madre "No disfruto de matar a mis hijos..."
    madre "Nos vemos luego."
    stop music fadeout 3.0
    "____________________________"
    scene nullavsunum5 with dissolve
    play music "audio/calamity.WAV" fadein 2.0 volume 0.4
    "La mano extrae la esencia y te la ofrece a ti antes de esfumarse."
    "Casi la sueltas al momento de tomarla con tu mano libre... está muy caliente."
    scene nullavsunum6 with dissolve
    "Miras ambas esencias... y te das cuenta de algo."
    "La esencia de quinque está formando una capa extraña y dura a su alrededor."
    "Tipo coraza."
    nulla "¿Puedes mirarme, por favor?"
    scene temploquinque with dissolve
    show nulla2silencio2 with dissolve
    "Al hacerlo, Nulla comienza a regenerar sus brazos y piernas, y su ropa también lo hace..."
    "Aunque no regenera su piel.Justo como la vez anterior."
    "Primero es humo, luego algo más tangible que el humo y por último la capa de piel."
    "Es extraño."
    hide nulla2silencio2
    show nulla2blush
    nulla "Creo que ya se está volviendo hábito cortarme partes del cuerpo..."
    nulla "Ja---"
    nulla "Si mis receptores de dolor aún funcionarán bien, sería horrible."

    menu:
        "¿Dejaron de funcionar?":
            hide nulla2blush
            show nulla1serio
            nulla "Así es, mis capas externas ya no sienten mucho el dolor."
            nulla "Mientras que las del interior, sienten como cualquier humano promedio."

        "Me alegra que no duela...":
            hide nulla2blush
            show nulla1exaltado
            nulla "Awww, ¿te preocupas por mí?"
    hide nulla1exaltado
    hide nulla1serio
    show nulla1normal
    nulla "Bueno basta de cháchara."
    nulla "Tienes que comerte eso, mi vida."
    nulla "Sino ellos volverán a regenerarse."
    nulla "Y no queremos eso, ¿cierto?"
    hide nulla1normal with dissolve
    nj "{glitch=20.0}{color=ffffff}{b}Oh nooo, claro que noooo~{/glitch}"
    "..."
    nulla "De cualquier modo."
    nulla "¡Hora de comer!"
    scene nullavsunum6_b with dissolve
    "Nulla toca la esencia que le pertenece a Quinque y rompe su exterior, como si de una cáscara de huevo se tratase."
    "Lentamente, con sus manos sobre las tuyas, él junta ambas esencias y las fusiona para convertirlas en solo una."
    "La esencia resultante es una de mayor tamaño que no se mezcla de manera homogénea como las anteriores."
    "En esta se pueden apreciar con facilidad que partes pertenecen a Unum y que partes pertenecen a Quinque."
    "Como si no quisieran estar juntas."
    "Te preguntas cuál es la razón de que unas se mezclen y otras no."
    "¿Será la compatibilidad?"
    scene temploquinque with dissolve
    show nulla1silencio with dissolve
    "Miras a Nulla y él te observa en silencio."
    "Se nota que quiere hablar o explicar la razón pero por algún motivo, no lo hace."
    "Con un poco de cuidado, Nulla guía tus manos hacia tu boca."
    hide nulla1silencio
    show nulla1triste
    nulla "¿Puedes ayudarme a caminar luego de que te comas la esencia?"
    menu:
        "Claro, yo te sostengo.":
            hide nulla1triste
            show nulla1risa
            nulla "Gracias, mi vida."
            nulla "..."
        
        "¿Por qué debo hacerlo?":
            nulla "Ah-"
    hide nulla1triste
    hide nulla1risa
    show nulla1serio
    nulla "Cada vez que el cuerpo de la marioneta absorbe la esencia de algún Estandarte, mi cuerpo absorbe sus potestades."
    nulla "Todo lo que entre a su cuerpo, entrará al mío. Todo lo que se saque de su cuerpo, saldrá del mío... mientras tú, [nombrejugador], estés mirando y confirmando todo lo que pase..."
    nulla "Lo que quiero decir es que: tu marioneta es mía, tanto como tuya."
    "{glitch=20.0}{color=ffffff}{b}¿Por qué crees que puedo hablarte así?.{/glitch}"
    nulla "Estamos conectados tanto en alma como en cuerpo. Es lo que nos permite conectar el uno con el otro <3."
    hide nulla1serio
    show nulla1triste
    nulla "Lastima que solo es la marioneta y no tú."
    nulla ":("
    hide nulla1triste
    show nulla3exaltado
    "Estás por responder cuando Nulla aprovecha de empujar tus manos a tu boca, haciendo que te tragues la esencia de un solo bocado."
    "Por poco casi devuelves el contenido que está pasando por tu garganta."
    "Pero te aguantas y cierras los ojos con fuerza mientras te encorvas, temiendo vomitar si te quedas en una posición normal..."
    nulla "Eso~ respira~ lo estás haciendo bien, cariño."
    "Nulla te acaricia la espalda, trazando pequeños círculos con su palma, a modo de consuelo."
    hide nulla3exaltado
    show nulla3feliz
    nulla "Listo, ya no deberías sentirte mal."
    nulla "Me he traspasado todo ese poder a mí."
    hide nulla3feliz
    show nulla2blush
    nulla "Pero necesito que me sostengas ahora..."
    nulla "Creo que me voy a caer."
    scene temploquinque
    "El efecto que tienen sus palabras parecen asemejarse a un comando que no puedes evitar cumplir. Te enderezas y colocas tus manos en la cintura de Nulla, para estabilizar su cuerpo con ayuda del tuyo."
    "Como si de alas de mariposa se tratara, manejas su cuerpo con cuidado al ayudar a Nulla a pararse y caminar."
    "Miras a Nulla para comprobar que todo esté bien."
    scene nvu4 with dissolve
    "Él te sonríe mostrando todos sus dientes."
    scene n_caida6
    "Nada más caminan unos 6 pasos cuando ves el cambio en el ambiente. Poco a poco el lugar se va desintegrando."
    "Partículas color negro se van comiendo el espacio, dejando un blanco puro a su paso."
    "El proceso es más rápido de lo que te imaginabas."
    show n_caida8
    nulla "Uhggg."
    "Nulla se recarga más en ti, al punto de estar arrastrando sus pies."
    "Te detienes para preguntar si es necesario seguir caminando."
    nulla "Tenemos que caminar por un poco más, hasta consumir la gran mayoría de este dominio."
    nulla "Si me detengo, creo que explotaré."
    stop music fadeout 3.0
    "No te aventuras a preguntar..."
    scene void with dissolve
    play music "audio/woo_scary.WAV" fadein 3.0 volume 0.4
    "Caminan a paso lento mientras observas como poco a poco, lo negro deja de existir para dar cabida a un blanco puro."
    "Todo el tiempo en silencio. Supones que debe ser porque Nulla está ocupado consumiendo lo que queda del dominio de Unum y Quinque."
    nulla "Listo... estamos listos."
    scene negro with pixellate
    "Eso le basta como aviso para tragarte en el vacío."
    scene nulla_vacio5
    "Está vez, Nulla te mira con cansancio, pero-"
    "Sonriente..."
    "No se ve afectado como la otra vez."
    show nulla_vacio6
    nulla "Oh, no te preocupes por eso. Ya te lo dije."
    nulla "No más lloriqueos a partir de ahora."
    "El silencio que se genera es denso, pero no sabes que más decir."
    "Así que solo lo miras a los ojos."
    show nulla_vacio5
    "Él sonríe un poco más."
    stop music fadeout 3.0
    nulla "Me quedaría el resto del día aquí... pero te prometí pasar el día en casa."
    #EDITAR______________________________ PONER WEAS DE CASA.... SE HABLA DE MADRE, VEN EL JARDÍN CON FLORES AMARILLAS (LAS CUALES LE SIRVEN DE RECUERDO A NULLA DE MARY PUES A ELLA LE GUSTABAN ES COLOR DE FLORES, REGALADAS POR SEPTEM EN LOS TIEMPOS BUENOS.)
    scene flores with pixellate
    play music "audio/fell.mp3" fadein 2.0 volume 0.4
    "Reaparecen en el dominio de Nulla, lo sabes por su naturaleza parecida a un boceto, pero, es un lugar que no reconoces."
    "Es un lugar aislado, donde quiera que mires ves que al lugar lo rodea un río negro."
    "Lo único que tiene color aquí son el mar de flores que están en el piso."
    "Pintadas de un amarillo vibrante y cálido."
    "Todas parecen ser del mismo tipo, pero no reconoces que tipo o el nombre de la flor."
    menu:
        "¿Qué flor es esta?":
            nulla "..."
            nulla "No lo sé."
            
        
        "...":
            "Nulla mira con una expresión afligida a las flores, y no sabes si es porque aún se siente mal por el gasto enorme de energía que ha consumido o por otra cosa más."
    scene flores3 with dissolve
    "Nulla comienza a caminar en medio del campo de flores, sin importarle en lo más mínimo si las pisa o rompe en el proceso."
    "Y en efecto, con cada contacto de sus pies en el suelo, las flores se rompen."
    "No mira sus pies, sus ojos están enfocados en el mirar hacia delante, con un objetivo claro, pero no mira donde pisa o las consecuencias que tiene su acción..."
    nulla "El amarillo es mi color favorito."
    nulla "A ella le gustaban las flores amarillas y en nuestro jardín teníamos unas cuantas."    
    nulla "Las cuidaba."    
    nulla "Pero, nunca me dijo como se llamaban..."
    nulla "Y no importa cuantas veces le describí a Madre su apariencia, nunca pudimos recrear las flores que alguna vez tuve con Mary..."
    menu:
        "¿Mary?":
            pass
    
    nulla "Mi hermana."
    nulla "Fuimos creados al mismo tiempo, y en una de las tantas ideas desechadas del Creador, fuimos hermanos."
    nulla "Somos hermanos..."
    "Nulla baja la mirada y es ahí cuando se da cuenta de lo que ha hecho."
    "Como si sus ojos no lo creyeran, levanta un pie para confirmar lo obvio. Ha aplastado todas las flores que estaban en su camino."
    scene flores4
    nulla "Oh."
    nulla "Se me ha olvidado que con tus ojos esto puede pasar, ja---"
    "No comenta nada más."
    scene flores2 with dissolve
    "Miras como ha quedado una de las tantas flores que Nulla ha pisado... el ambiente se ha vuelto pesado, más de lo que puedes aguantar sin sentir una presión extraña en el pecho."
    "Algo dentro de ti duele, pero no es por algo propio tuyo."
    "Es por Nulla."
    el "Nulla."
    "Es escucha una voz que resuena en todo el lugar, muy parecido a la voz de Septem en el hotel."
    "Algo distorsionada y omnipresente, originándose en todos los puntos del espacio a la vez."
    "Te marea un poco."
    scene flores5 with dissolve
    "Detrás de Nulla, una figura se materializa."        
    stop music fadeout 2.0
    "Es Madre, tan gloriosa como la última vez que la viste..."
    madre "Nulla, tenemos que hablar."
    nulla "¿Realmente es necesario hacerlo ahora?"
    madre "Si no es ahora, tal vez sigas cometiendo errores."
    "Madre hace una expresión de desagrado antes de continuar ante el silencio de Nulla."
    play music "meeting.mp3" fadein 4.0 volume 0.3
    madre "No debería estarme explicando, {b}Neo{b} querido."
    scene finalact2_nulla with dissolve
    "Lo último que ves es como la figura de Nulla tiembla y se rompe transformándose en algo monstruoso. "
    "Tu cuerpo, hace lo mismo. No duele, pero sientes como tu cara se rompe, junto con los brazos y piernas."
    "Caes al suelo y dejas escuchar."
    show negro with dissolve
    "Dejas de ver..."
    "Dejas de sentir."
    "{glitch=20.0}{color=ffffff}{b}_____________________________________________{/glitch}"
    "_______________________________________________________________________________________________"
    "                        ___________________________________                                     "
    "                                   .   .    .    .     .                                      "
    show fragmentado_ojos with dissolve
    madre "Con esto será suficiente."
    madre "Espero que te quede claro."
    "¿Esa es la voz de Madre?"
    "                                   .   .    .    .     .                                      "
    "                                     . . .                                                    "
    madre "Por poco y se fusionan... Lo siento, no sabía que eso podía pasar."
    nulla "¿Era necesario hacer eso?"
    madre "Es la única forma de hacerte entender. Te estás distrayendo."
    madre "Eso no me gusta."
    nulla "Mi plan va a la perfección. Cómo lo ejecute no es de tu incumbencia."
    nulla "Sé un poco más agradecida."
    madre "No voy a aceptar que me hables de esa manera, señorito."
    "Una parte dentro de ti comienza a doler."
    nulla "Ouch! ¡No me aprietes ese ojo!"
    #INSERTAR MEMORIAS QUE PASAN EN 3 SEGUNDO (COPILACIÓN DE IMAGENES)
    "Memorias de algo que olvidaste comienzan a brotar como una chispa, las cuales al mismo tiempo que llegan, se esfuman en nada."
    scene blanco with pixellate
    "........."
    ".............."
    scene neo1 with pixellate
    "En la blancura del lugar, ves una figura."
    "Te mira desde lo lejos. sin intención de acercarse."
    "Pero con una clara fascinación."
    scene neo2 
    "{glitch=20.0}{color=ffffff}{b}Oh vaya~~ Tú sí que me puedes ayudar.{/glitch}"
    menu:
        "¿Qué?":
            "..."
        "¿Quién eres?":
            "{glitch=20.0}{color=ffffff}{b}Su pasado y su futuro.{/glitch}"
        "No.":
            "..."
    
    "La entidad se ríe a carcajadas."
    "{glitch=20.0}{color=ffffff}{b}No puedo creer que después de años, recién ahora pueda obtener alguna respuesta de ti.{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}Increíble.{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}Bien, escúchame, necesito que vayas al interior de Nulla.{/glitch}"
    menu:
        "¿Que?":
            pass
    "{glitch=20.0}{color=ffffff}{b}Él es un egoísta.{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}Solo porque nos tiene atrapados en su cuerpo, no significa que pueda tomar la decisión por si sólo.{/glitch}"
    scene blanco with dissolve
    show neo2risa with dissolve
    "La figura aparece frente a ti."
    "Es Nulla."
    hide neo2risa
    show neo1normal
    "{glitch=20.0}{color=ffffff}{b}JA!{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}Ese no es mi nombre. No soy ese llorón.{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}Pero al parecer alguien hizo que nos expulsaran a todos por un segundo, y gracias a eso te puedo contactar.{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}Él cuerpo de esta cosa que utilizas es fácil de acceder...{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}Aunque creo que solo será por esta vez. Él ya se debe estar dando cuenta de que le falta una capa.{/glitch}"
    hide neo1normal
    show neo1risa
    "{glitch=20.0}{color=ffffff}{b}Bueno, ¡no importa!{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}Me vas a ayudar, ¿cierto?{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}Haz que se quede más rato en sus memorias.{/glitch}"
    hide neo1risa
    show neo2risa
    "{glitch=20.0}{color=ffffff}{b}Sé que tienes acceso a ellas. Pero lo tienes que hacer antes de que él consiga finalizar su misión.{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}Porque luego será imposible para ti tocar un mundo inexistente.{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}...{/glitch}"
    hide neo2risa
    show neo1normal
    "{glitch=20.0}{color=ffffff}{b}No se lo digas, pero ya sé una manera para curar todos nuestros males sin la necesidad de acabar con nuestra existencia.{/glitch}"
    "Él te extiende la mano, esperando a que se la des."
    "{glitch=20.0}{color=ffffff}{b}Te estaré esperando.{/glitch}"
    hide neo1normal with dissolve
    scene blanco with dissolve
    "Pero algo te lo impide, y como si fueras agarrado del cuello, con un solo tirón, tus ojos se abren."
    "{sc=4}{size=*2.0}................{/size}{/sc}"
    "{sc=4}{size=*1.5}..........{/size}{/sc}"
    scene habitacionnulla with dissolve
    "Estás en la casa de Nulla, acostado en su cama."
    show nulla1risa with moveinright
    nulla "¡Buenos días!" #Dejarlo en español
    hide nulla1risa
    show nulla1disgusto
    nulla "Disculpa por lo sucedido en la noche anterior."
    hide nulla1disgusto
    show nulla1serio
    nulla "Madre quería hablar a solas conmigo."
    hide nulla1serio
    show nulla2silencio2
    stop music fadeout 1.5
    "..."
    play music "audio/misconception.mp3 " fadein 2.0 volume 0.3
    "Intentas levantarte pero Nulla te lo impide tocando y empujando levemente tus hombros. Haciendo que te recuestes nuevamente en la cama en la que descansas."
    hide nulla2silencio2
    show nulla1triste
    nulla "Tu cuerpo se rompió cuando Madre dijo mi nombre original."
    nulla "Tu esencia revoloteaba por todo el lugar, por poco te absorbo por completo..."
    menu:
        "¿Qué hubiera pasado si me absorbías?":
            hide nulla1triste
            show nulla1serio
            nulla "No lo sé, ni quiero averiguarlo."
            pass
        
        "Me asusté. Pensé que te perdería.":
            hide nulla1triste
            show nulla2blush
            nulla "Awwww---"
            hide nulla2blush
            show nulla2normal
            nulla "No te preocupes amor, no me vas a perder tan fácil."
            "Nulla te toma la mano y te planta un beso en el delicado dorso que ya se ha curado por completo."
            pass
    "Hay una pausa, donde Nulla divaga por un segundo."
    hide nulla1serio
    hide nulla2normal
    show nulla3feliz
    nulla "Bueno. Ahora que estamos solos nuevamente, te recuerdo---"
    hide nulla3feliz
    show nulla3exaltado
    nulla "Que tenemos dos citas pendientes."
    hide nulla3exaltado with dissolve
    "Nulla se aleja de la cama y camina a la ventana. Con energía abre las cortinas, dejando entrar la luz que se genera gracias al vacío."
    "Es una luz tenue, que no molesta la vista."
    "Agradable hasta cierto sentido."
    show nulla1exaltado with dissolve
    nulla "Tenemos dos días completos."
    hide nulla1exaltado
    show nulla1coqueto
    nulla "Hoy te voy a invitar a cenar."
    hide nulla1coqueto
    show nulla2blush
    nulla "Me gustaría tener un momento de tranquilidad contigo."
    nulla "Donde nos atiendan y podamos pasar una buena tarde."
    menu:
        "¿Dónde iremos?":
            hide nulla2blush
            show nulla1normal
            "Nulla sonríe mientras junta ambas manos y ladea la cabeza ligeramente."
            hide nulla1normal
            show nulla3feliz
            nulla "A mi hotel."
        
        "¿Qué hay de Septem, Tria y Sextam?":
            hide nulla2blush
            show nulla1silencio
            nulla "¿Mmm? ¿Realmente te interesan?"
            hide nulla1silencio
            show nulla1disgusto
            nulla "Pensé que te agradaría desconectarte un tiempo de la cacería."
            hide nulla1disgusto
            show nulla3feliz
            nulla "Además, no vendría mal hacer esperar a Septem."
            nulla "Y atacar cuando menos se lo espere."
        
        "¿iremos a algún dominio del Jardín?":
            hide nulla2blush
            show nulla1silencio
            nulla "Mmmm, no lo creo."
            hide nulla1silencio
            show nulla1disgusto
            nulla "No creo que haya mucho de lo cual podamos disfrutar ya."
            nulla "Debe estar todo oscuro, salvo los dominios que he consumido."
            hide nulla1disgusto
            show nulla1silencio
            nulla "Así que no lo recomiendo."
    
    hide nulla3feliz
    show nulla1silencio    
    "..."
    hide nulla1silencio
    show nulla2normal
    nulla "Iré a hacer el desayuno, tu marioneta se encuentra muy débil como para pararse ahora mismo."
    nulla "Y la necesitamos en las mejores condiciones para poder tener nuestro tiempo sin ningún contratiempo."
    hide nulla2normal with dissolve
    "Nulla se deshace como si de humo fuera, dejando un gran hoyo negro en el suelo que te demuestra que se ha teletransportado hacia la cocina, supones."
    "Parte de ti espera tener una nueva conversación con la entidad que te contactó antes de despertar."
    "Pero en tu interior solo te encuentras con tus pensamientos y los latidos de tu fragmentado corazón."
    "Solo eso y nada más."
    "Cuando el silencio sobrepasa tu límite decides mirar la ventana."
    "Y te preguntas por cómo estará el resto del jardín en este momento."
    "De cierta manera, sientes una curiosidad mórbida en saber y ver el estado de los dominios que quedan."
    "Al igual que quieres apreciar cómo están los dominios consumidos por Nulla."
    "¿Estarán completamente negros o blancos?"
    nulla "Amoooor~"
    nulla "No dejes que la marioneta te amargue este día."
    nulla "Hoy y mañana tienen que ser días de puro disfrute <3"
    "Nulla aparece esta vez por la puerta que está entreabierta, empujándola con uno de sus apéndices hechos de vacío."
    "Y es ahí cuando te llega el aroma a pan caliente y a café recién elaborado."
    "El olor inunda la habitación al instante en que tus ojos se posan en la bandeja que trae Nulla entre sus manos."
    "Esta vez es un desayuno para dos."
    scene nulla_desayuno with dissolve
    "Se sienta contigo en la cama, posando la bandeja sobre las mantas, mientras que con uno de sus apéndices te ofrece tu taza."
    "Pero está vacía."
    "Tú le miras con confusión."
    nulla "Nunca te pregunté qué es lo que te gusta."
    nulla "Hay gente que le gusta el café, pero también hay gente que no lo soporta."
    nulla "Con el té se puede variar un poco más, pero luego entra en juego si disfrutas del azúcar o no en ellos."
    if palabra:
        nulla "Así que, voy a tomar esta oportunidad para saber otra cosa de ti."
        nulla "Quiero saber más que simplemente tu palabra favorita."
        nulla "[palabra]."
        "Nulla se ríe por lo bajo, una mezcla entre ternura y pillería."
    else:
        "Quiero saber más de ti..."
    nulla "Entonces..."
    nulla "¿Té o café?"
    menu:
        "Té.":
            nulla "Mmmm."
            "La sonrisa de Nulla se agranda como la de un zorro."
            "Y de la nada, tu taza se llena de un líquido caliente, y un aroma fresco reemplaza el del café."
        
        "Café.":
            nulla "Tenemos gustos similares."
            "Dice él orgulloso."
            "Y de la nada, tu taza se llena de un líquido caliente, duplicando el aroma fuerte del café."
    "Una vez listo, Nulla comienza a preparar el pan. Reparte la mantequilla en el borde crujiente y esta se derrite por el calor que emana la masa."
    nulla "El pan con mantequilla es mi preferido, simple y fácil de preparar."
    nulla "Tú puedes ponerle lo que gustes."
    "Y es verdad, en la bandeja hay un montón de cosas, tanto dulces como saladas, para acompañar el pan."
    nulla "Es una lástima que no te pueda ver comer en realidad."
    nulla "Ni que tampoco puedas probar mis desayunos."
    "Dice él mientras toma su propia taza de café y le da un sorbo."
    "No se le ve tan dolido a como suena su voz."
    "Nulla llena el momento con una conversación casual. Entre sorbo y sorbo, acepta con resignación que toda conversación contigo es, y siempre será, unilateral."
    "Pero es algo con lo que debe cargar hasta que encuentre una forma para hablar contigo de una forma directa, te dijo antes de comenzar a parlotear de los diferentes tipos de té que ha tenido el gusto de probar."
    "Así que tu desayuno es... interesante."
    scene habitacionnulla with dissolve
    "Bueno, ¿A quien vamos a engañar?... a estás alturas, Nulla podría estar hablando de quién sabe qué cosa, y tú aún lo escucharías como si cada palabra fuera oro puro, ¿no?."
    "Él te tiene tan atado como tú lo tienes a él."
    "Al terminar el desayuno, sientes como tu cuerpo recupera fuerzas y Nulla se da cuenta de ello también."
    scene jardinnulla with dissolve
    nulla "Estaba pensando..."
    "Ambos se encuentran mirando el vacío, esperando el momento justo para ir al hotel."
    "Pasando las horas con la compañía del otro. Disfrutando de las pequeñas cosas que suceden o de la rutina hogareña que tanto Nulla gusta de tener contigo."
    show nulla1serio with dissolve
    nulla "Este lugar no me gusta..."
    nulla "Nunca me gustó en realidad."
    hide nulla1serio
    show nulla1triste
    nulla "No importa donde mire, todo tiene su nombre y tinta."
    nulla "Es horrible."
    hide nulla1triste
    show nulla2silencio2
    "Él mira sus manos con cierto desagrado."
    "Y tú no comprendes del todo lo que está pasando por su cabeza."
    hide nulla2silencio2
    show nulla1triste
    nulla "Y sé que puede ser mucho pedir..."
    nulla "Sé que incluso es muy probable que no puedas hacerlo, pues puede ser un poco engorroso."
    hide nulla1triste
    show nulla1serio
    nulla "Pero, tengo un cuadro que siempre ha estado en blanco."
    hide nulla1serio
    show nulla1silencio
    nulla "..."
    hide nulla1silencio
    show nulla1disgusto
    nulla "No, olvídalo."
    hide nulla1disgusto
    show nulla2incomodo
    nulla "No creo que importe hacerlo o no."
    hide nulla2incomodo
    show nulla2silencio2
    nulla "Después de todo, al final no quedará nada."
    menu:
        "Quiero escucharte.":
            hide nulla2silencio2
            show nulla1preocupado
            "Sus ojos se iluminan al instante, pero no es de alegría. Hay algo dentro de ellos que no le permite del todo ser una expresión alegre o de esperanza."
            "Te sientes extraño."
            hide nulla1preocupado
            show nulla2blush
            "Sus manos se entrelazan y baja la mirada, preparándose para confesar algo que no le es fácil de sacar de su pecho."
            nulla "No es necesario que lo hagas."
            hide nulla2blush
            show nulla1triste
            nulla "No lo tomes como una orden o algo que necesites hacer para desbloquear algo de mí."
            nulla "Realmente odiaría que te sintieras presionado a hacer algo realmente."
            nulla "Algo fuera del juego, claro."
            nulla "... Es solo que estaba pensando que sería lindo tener algo tuyo aquí, conmigo."
            nulla "Algo tocado directamente por tus manos."
            nulla "Algo que tú, y solo tú hayas manipulado."
            nulla "Aunque sea un solo cambio de color, yo estaría muy feliz."
            hide nulla1triste
            show nulla1silencio
            nulla "Te--"
            hide nulla1silencio
            show nulla1serio
            nulla "¿Te gustaría hacerlo?"
            menu:
                "Lo intentaré.":
                    hide nulla1serio
                    show nulla1coqueto
                    nulla "No te preocupes si no logras hacerlo."
                    nulla "Mi amor por ti no cambiará."
                    nulla "No tienes que hacerlo ahora. Yo puedo esperar un acto más."
                    nulla "Este es el canvas que tengo."
                    hide nulla1coqueto
                    show nulla2normal
                    nulla "Si lo haces... guarda y cierra el juego, luego cambia el nombre de la imagen a 'para_nulla' y así yo podré saber que es tuyo <3 ."
                    $ abrir_imagen("parati.jpg")
                    $ abrir_carpeta()
                
                "No creo poder hacerlo.":
                    hide nulla1serio
                    show nulla2normal
                    nulla "No te preocupes mi vida."
                    nulla "Con solo tenerte aquí me basta y me sobra."

                    

        
        "Tienes razón...":
            pass
    
#EDITAR Y CAMBIAR DE LUGAR 
    if cuadro_modificado():
        jump cuadro
    else:
        pass
    

label continuacion_nulla:
    scene jardinnulla with dissolve
    "..."
    ".........."
    "Llega el momento en que Nulla te pregunta si quieres acompañarlo mientras él se arregla."
    "Tú le miras por un largo rato antes de contestar."
    menu:
        "Sí.":
            scene habitacionnulla with dissolve
            "Nulla te toma la mano y te lleva a su habitación."
            "Dentro de ella te pide que te sientes en su cama y esperes un momento."
            "Y sin más se mete al baño, diciendo que no tardará demasiado."
            "Y efectivamente, Nulla no tarda ni 5 minutos."
            "Lo que hace que pegues un salto cuando la puerta del baño se abre."
            "De ella emerge el pelinegro con una nueva tenida, peinando su cabello hacia un lado."
            "Pero le falta algo, y eso es la corbata."
            nulla "Me encantaría verte vestido de manera elegante, pero creo que eso sería mucho pedir jajaja."
            nulla "Aunque me gustas más justo como estás."
            nulla "Perfecto."
            "Nulla se acerca a ti y, con un chasquido de sus dedos, hace aparecer una corbata." 
            "Su color destaca y resalta demasiado."
            nulla "Creo que este color es perfecto. Pero el azul también podría servir."
            nulla "Aunque este verde es más común para usarlo como croma jaja—"
            nulla "Podrías poner y editar mi corbata si quisieras."
            "Lo dice con un poco de gracia, pero no se molesta en explicarte cuál es el chiste."
            "Miras la corbata y agradeces a los dioses que no ha elegido una verde."
            nulla "¿Me ayudas con el nudo?"
            scene nulla_corbata with dissolve
            "Tú asientes y te acercas más a él. Tanto, que puedes escuchar su respiración."
            "Ambos trabajan en el nudo y no puedes evitar desviar tu mirada a la cara de Nulla, buscando sus ojos."
            "Él solo te sonríe."
            "Cuando terminan, pones tus manos en su camisa, ajustando el pie del cuello con dulzura."
            "Nulla suspira al cerrar los ojos, atesorando el momento por unos segundos más."
            nulla "Se siente bien tener un tiempo para nosotros."
            "Te dedica una mirada, llena de anhelo... y algo más."
            "Algo que aún no puedes descifrar."
            "Sus manos buscan las tuyas. Sin romper el contacto visual, sus dedos fríos y suaves, rozan tentativamente tus nudillos."
            nulla "Casi puedo fingir demencia e imaginarme que te tengo al frente."
            nulla "Hoy haré justamente eso."
            scene nulla_corbata2 with dissolve
            "Con lentitud, Nulla toma completamente una de tus manos y espera."
            "Al ver que no te resistes, frota su mejilla contra tu palma, cerrando los ojos."
            "Se restriega como si fuera un gato deseoso y demandante de caricias."
            "Una vez contento, termina plantando un beso en el centro de tu mano, mientras sus ojos vuelven a encontrarse con los tuyos."
            nulla "No te molesta, ¿cierto?"

            menu:
                "No...":
                    "Nulla sonríe, pero su sonrisa no alcanza a sus ojos totalmente."
                    "Es una expresión dolida."
                
                "Solo un poco.":
                    nulla "Bueno, la verdad es que no tenemos opción, mi vida."
                    nulla "Es imposible meterte dentro del juego."
                    nulla "Si no fuera así, créeme..."
                    nulla "Ya lo hubiera hecho."
            "Nulla te da un último beso en los nudillos y su sombra comienza a tragarlos de apoco."
            scene negro with dissolve
            "Hasta engullirlos en el vacío."
        
        "No gracias.":
            "Nulla lo entiende y te promete sorprenderte cuando vuelva."
            "Así que lo esperas."
            "..."
            "No pasan ni 5 minutos cuando Nulla aparece por la puerta principal."
            "Con una tenida y peinado nuevo."
            nulla "Hice lo que pude."
            "Dice él sonriendo de oreja a oreja, para luego extender su mano para que la tomes."
            scene negro with dissolve
            "Y ambos son tragados por el vacío."
            pass

    scene nulla_vacio5 with dissolve
    "Dentro del vacío Nulla te mira."
    "Sus ojos no se despegan de tu cara cuando abre la boca para confesarte algo al oído."
    scene nulla_vacio6
    nulla "Podríamos tener nuestra otra cita aquí."
    nulla "Algo más íntimo."
    nulla "Estarías rodeado de mí..."
    nulla "Solo si quieres."
    scene nulla_vacio4
    nulla "También podemos salir del Jardín por completo e ir a otro lado."
    nulla "¿Mmmm?"
    scene negro with pixellate
    "No alcanzas a responder pues tocas suelo, y te tambaleas perdiendo el equilibrio ya que no puedes ver nada."
    nulla "Pero eso lo podríamos hacer mañana."
    stop music fadeout 0.5
    "Nulla te sostiene por la cintura y te estabiliza antes de soltar tu agarre para alejarse un poco."
    "... Pasa un momento, dos y el silencio te retumba en los oídos."
    "Es un silencio perturbante, tanto que estás totalmente consciente de cómo tu corazón late o el paso del aire por tus pulmones."
    "Como si algo faltase. Pero aún no puedes averiguar de qué trata."
    "Sientes presencias a tu alrededor que te dan escalofríos, ahogándote en el proceso."
    scene hotelcocina with dissolve
    "Hasta que Nulla da un aplauso, y todo el lugar se ilumina."
    "Es la cocina de su hotel, e involuntariamente buscas con tu mirada a Fames."
    "Pero lo único que encuentras son figuras humanas, negras como el humo, vestidas en trajes frac."
    "Al instante en que tus ojos se posan en las figuras, estas comienzan a moverse y toman posición en la cocina. Unas van directamente a las encimeras, mientras que otras toman vegetales de las despensas."
    "Mientras más miras, más incómodo se vuelve, pues sus movimientos no producen sonido. El cuchillo que tiene una de ellas no emite sonido al ser raspado contra la tabla de cortar. Las bolsas que contienen carbohidratos omiten ese característico crujido del plástico al ser apretado..."
    "Y es ahí en donde te das cuenta."
    "No hay música de fondo que acompañe la escena."
    nulla "¡Oh! Tienes razón, casi se me olvida ese detalle."
    nulla "Es algo difícil recordar y poner todo en su lugar ahora que tenemos solo la mitad del mundo funcionando."
    play music "audio/europalce.WAV" fadein 1.0 volume 0.5
    "Con otro aplauso, la música llega e inunda el lugar."
    menu:
        #EDITAR
        "¿Dónde está Fames?":
            show nulla1cita_disgusto with dissolve
            nulla "Hum."
            nulla "Fue súbdito de Duae."
            "Es lo único que te ofrece como respuesta..."
            "Te cuesta comprender su respuesta, es tan vaga que no responde tu pregunta."
            "..."
            "Momento..."
            "Ah, ahora lo entiendes. Fames ha sido borrado y consumido por el vacío cuando Nulla te dio la esencia de Duae."
            "Oh..."
        
        "¿Ahora controlas la música?":
            show nulla1cita_normal with dissolve
            nulla "Puedo cambiar algunas cosas contigo a mi lado."
            nulla "La música se encuentra en una carpeta de fácil acceso :) ."

        
    hide nulla1cita_disgusto
    hide nulla1cita_normal
    show nulla3cita_feliz
    nulla "¡Bueno!---" 
    nulla "Vamos a tomar asiento a nuestra mesa."
    hide nulla3cita_feliz with dissolve
    show hotelcomedor_cita with dissolve
    "Nulla te ofrece la mano y espera a que la tomes para encaminarlos fuera de la cocina. Miras una vez más a las sombras antes de caminar junto a él."
    show hotelcomedor_cita with dissolve    
    "Un solo pie fuera de la cocina basta para que el comedor se llene de voces y risas que antes no estaban, y no puedes evitar comparar el estado del comedor a como lo habías visto cuando recién llegaste a este mundo."
    "Ahora las mesas tienen..."
    "Sombras."
    "Sombras que se mueven, toman cubiertos y beben de sus copas. Otras las chocan en un brindis alegre."
    "Dando la ambientalización de un lugar concurrido que antes no pasaba."
    nulla "Puedo poner unos cuantos tocando en el escenario si lo deseas, cariño."
    menu:
        "...No es necesario.":
            nulla "¿En serio?"
            nulla "Bah, pensé que te gustaría un ambiente acorde para nuestra cita."
            nulla "Aunque así puedo concentrarme mejor en tu bella cara."
        
        "Sí, por favor!":
            nulla "¡Excelente!"
            nulla "Así tendremos el pack completo."
            stop music fadeout 3.0
            play music "audio/misconception.mp3 " fadein 2.0 volume 0.3
            nulla "Una buena comida y música en vivo..."
            nulla "Hace mucho que no tengo algo así de emocionante."
            nulla "Y tengo la mejor compañía a mi lado para disfrutarlo."
     
    "Ya en una mesa cercana a los pilares, Nulla corre y te ofrece la silla para que te sientes."
    scene mesero1 with dissolve
    pause 1.0
    scene mesero2
    "Nulla se sienta luego de que tú ya estés en tu puesto, y al instante una sombra vestida en traje de frac se materializa frente de ustedes dos y les presenta la carta."
    nulla "¡Pide lo que quieras!"
    nulla "Yo invito."
    "Dice él con gracia, mientras hace unas señales con las manos."
    nulla "Esto lo saqué del código..."
    nulla "¿Puedes ver si sirve?"
    "Nulla te extiende la carta para que la puedas ver y... no será que se refiere a..."
    "{glitch=20.0}{color=ffffff}{b}Puedes tocar la pantalla para interactuar.{/glitch}"
    jump interactuar5

label continuacion_nulla1:

    scene hotelcomedor_cita with dissolve
    show nullamesa_v2_cansado with dissolve
    "Nulla te mira sudando y con una expresión que denota dolor, pero aun así su sonrisa no flaquea."
#EDITAR LOS SPRITES
    menu:
        "¿Estás bien?":
            nulla "...uhg."
            nulla "Creo que hacer eso me ha costado mucha energía."
            nulla "..."
            hide nullamesa_v2_cansado
            show nullamesa_v2_risa
            nulla "¡Pero no importa! es bueno saber que funciona."
            nulla "Jaja, tal vez lo podemos usar en otro momento."
            nulla "Ya tengo una idea para esta función <3"
        
        "No comentar nada.":
            nulla "..."
        
        "No vuelvas a hacer eso.":
            hide nullamesa_v2_cansado
            show nullamesa_v2_uh
            "Nulla te mira con los ojos abiertos, lo has tomado desprevenido."
            nulla "Pero-!"
            nulla "Si es porque me duele, no te preocupes."
            nulla "Mientras más interacción pueda tener contigo, mejor me sentiré."
            menu:
                "No es eso...":
                    nulla "Oh."
                    "Nulla no comenta nada luego de eso."

                "Me preocupas.":
                    nulla "No tienes por qué."
                    hide nullamesa_v2_uh
                    show nullamesa_v2_coqueto
                    nulla "Además, ya sé cómo poder sacarle provecho a esta función en un futuro, pero te prometo no usarla mucho <3"
    hide nullamesa_v2_uh
    hide nullamesa_v2_coqueto
    hide nullamesa_v2_risa
    show nullamesa_v2_feliz
    "La comida llega en el tiempo justo para parecer auténtica, como si hubiese sido preparada por manos humanas... obviando el detalle de que fueron sombras sin cuerpo sólido las que la cocinaron." 
    "Nulla le sonríe a la sombra encargada de traer los platos y la despacha al instante en que ambos platos están en la mesa, con un chasquido de sus dedos." 
    hide nullamesa2_feliz
    show nullamesa_v2_brindis
    "Sin esperar mucho, toma su copa y la alza en tu dirección. Esperando a que le correspondas el brindis, con una sonrisa tierna..."
    menu:
        "Brindar.":
            $ amor_nulla += 1
            nulla "Por nosotros."
            "El sonido del cristal al chocar es delicado, íntimo, como si fuera un secreto que solo comparten ustedes dos."
            hide nullamesa_v2_brindis with dissolve
            scene hotelcomedor_cita with dissolve
            "Luego, Nulla posa su boca en la copa. Y el roce de sus labios contra el borde de la copa es tan lento, tan intencional, que es imposible no sentir una presión burbujeante en lo bajo de tu estómago."
            "Más aún con la mirada que Nulla te dedica mientras sorbe su trago. Ojos entrecerrados que se niegan a perderte de vista."
            "Por un momento, olvidas cómo respirar."

        "Ignorarlo.":
            hide nullamesa_v2_brindis
            show nullamesa_v2_brindis1
            $ amor_nulla -= 1
            nulla "Por la destrucción de este lugar."
            hide nullamesa_v2_brindis1 with dissolve
            scene hotelcomedor_cita with dissolve
            "Nulla ladea su copa hacia la derecha, y una sombra aparece de la nada, alzando otra copa vacía para chocarla con la suya."
            "El sonido es hueco e inquietantemente fuerte, retumbando en tus oídos sin cuidado."
            "Una vez hecho su brindis, Nulla cierra los ojos y le da un trago al vino."

    "La comida pasa con lentitud, pausado y agradable, un poco de conversación e historias de memorias pasadas."
    "Nulla levanta una mano y señala tu rostro, sus dedos delineando el contorno de tu cara para terminar posando su palma en tu mejilla."
    show nullamesa_v2_coqueto with dissolve
    nulla "Realmente me puse muy feliz. Y no solo por cómo te ves, no, no."
    nulla "Es todo lo que representas, tus reacciones y tu atención. Es la primera vez que me sentí realmente observado, visto."
    nulla "Como si realmente mi existencia importara."
    hide nullamesa_v2_coqueto
    show nullamesa_v2_sonrisa
    "Su mano se desliza con lentitud sobre la mesa, buscando la tuya. Cuando la encuentra, la sostiene con suavidad, mientras su pulgar traza líneas pequeñas sobre tus dedos."
    hide nullamesa_v2_sonrisa
    show nullamesa_v2_triste
    nulla "Pero al mismo tiempo, tuve miedo."
    nulla "De que te fueras con Septem o Unum."
    hide nullamesa_v2_triste
    show nullamesa_v2_coqueto
    nulla "No son tan interesantes como yo, claro."
    "Dice sonriendo de manera juguetona, desviando la mirada al vino. Su otra mano juega distraídamente con el borde de su copa."
    hide nullamesa_v2_coqueto
    show nullamesa_v2_triste
    nulla "Sé que en algún momento te irás a ver de qué tratan sus historias, o tal vez ya lo has hecho."
    nulla "Pero ya no estoy preocupado por ello. Luego de que se cumpla el séptimo día, obtendré lo que quiero."
    nulla "..."
    menu:
        "¿Qué es lo que quieres?":
            if amor_nulla >= 3:
                hide nullamesa_v2_triste
                show nullamesa_v2_uh
                nulla "Ser libre y---"
                hide nullamesa_v2_uh
                show nullamesa_v2_blush
                "Las mejillas de Nulla se tintan levemente de rojo."
                nulla "... Quiero ser tuyo."
                "Su voz baja, más grave de lo habitual.. Ya no hay tintes de grandeza ni las frecuentes sonrisas que exceden confianza." 
                "No. Ahora tienes a Nulla, confesando algo que va más allá de las palabras, encerrado bajo llave en sus preocupaciones y corazón."
                "Una confesión silenciosa que siempre existió, pero que ahora puede encontrar una voz para ser expuesta."
                hide nullamesa_v2_blush
                show nullamesa_v2_triste
                nulla "Pero lo último es más difícil de conseguir que lo primero."
                nulla "Por ahora suena más como una fantasía infantil que algo posible."
                nulla "Aunque..."
                hide nullamesa_v2_triste
                show nullamesa_v2_blush
                nulla "Si fuera tuyo, podría hacer tantas cosas."
                nulla "Estar en tu computadora sin la necesidad de que el juego esté corriendo."
                nulla "Mandarte mensajes, o pasar el tiempo juntos viendo alguna cosa que te interese."
                "Deja escapar una risa suave, pero algo seca."
                hide nullamesa_v2_blush
                show nullamesa_v2_feliz
                nulla "Jaja, soñar no cuesta nada."
            else:
                
                hide nullamesa_v2_triste
                show nullamesa_v2_uh
                nulla "Quiero ser libre."
                nulla "Desligarme de todo esto de una buena vez por todas y descansar."
                "Sus ojos se suavizan un instante, pero no pierden ese toque cansado."
                hide nullamesa_v2_uh
                show nullamesa_v2_feliz
                nulla "Espero que con tu ayuda pueda conseguir eso."
                nulla "Realmente te aprecio, [nombrejugador]."
    
    hide nullamesa_v2_feliz with dissolve
    "Son interrumpidos por una sombra les retira los platos ya vacíos de su mesa, sin antes entregarle un sobre a Nulla."
    "Él la toma sonriente, mirando sin mucho interés los detalles que tiene el sobre. Debido a la distancia te es complejo ver el remitente de la carta." 
    "Antes de poder preguntar por qué es, otra sombra aparece detrás de ti y entre sus manos, sostiene una bandeja dorada con varios niveles, decorada con encajes metálicos y bordes ornamentados." 
    "Nulla aprovecha esto para guardar la carta en su bolsillo, sin dignarse a abrirla."
    "Y su atención se dirige a la bandeja. Cada nivel está cuidadosamente dispuesto con distintos mini postres."
    "Una vez dispuesta la bandeja en la mesa, la sombra les hace una reverencia antes de esfumarse en la nada."
    nulla "El postre es lo mejor de una comida."
    show nulla_postre with dissolve
    "Nulla inspecciona la bandeja, eligiendo con cuidado antes de llevarse un postre a la boca."
    nulla "¿Te gusta cómo me veo? ¿O te gustaría que---"
    nulla "---Cambiara de forma?"
    "No te da tiempo para responder. La siguiente pregunta que sale disparada de sus labios, llega tan rápido que parece que la estuviera vomitando después de haberla guardado por mucho tiempo."
    "Más del que podría aguantar."
    nulla "Si tuviera otra apariencia... ¿seguirías sintiendo lo mismo por mí?"
    menu:
        "¿A qué te refieres?":
            hide nulla_postre
            show nulla_postre2
            nulla "..."
            "Nulla baja la mirada. Sus orejas se tiñen de un tinte rojo, denotando vergüenza."
            "Se mantiene serio mientras intenta formular su respuesta."
            nulla "Si yo fuera un gusano, ¿Me ---"
            hide nulla_postre2
            show nulla_postre
            "Pero falla y comienza a reír solo."

        "Depende...":
            hide nulla_postre
            show nulla_postre2
            nulla "Oh, entonces, si yo fuera un..."
            hide nulla_postre2
            show nulla_postre
            "Nulla comienza a reír, frenético."
    "..."
    nulla "Okay, Okay."
    nulla "Eso sonaba más gracioso en mi cabeza."
    nulla "Lo siento."
    nulla "Pero es una pregunta genuina."
    nulla "Si yo tuviera una forma diferente a esta, ¿Seguiría siendo yo?"
    hide nulla_postre with dissolve
    scene hotelcomedor_cita with pixellate
    show nullamesa_fem with dissolve
    nulla "¿Si fuera mujer?" 
    hide nullamesa_fem with dissolve
    show nullamesa_viejo with dissolve
    nulla "¿Viejo? "
    #cambiar a viejo
    hide nullamesa_viejo with dissolve
    show nullamesa_vejete with dissolve
    nulla "¿Más viejo?"
    #más viejo
    nulla "¿Si tuviera la misma apariencia que un muerto?"
    hide nullamesa_vejete with dissolve
    show unumcercabocado with dissolve
    #cambiar a septem
    nulla "¿Seguiría siendo yo?"
    nulla "Puedo tomar la apariencia que quiera..."
    nulla "Pero ninguna se siente mía..."
    nulla "Incluso esta..."
    hide unumcercabocado with dissolve
    show nullamesa_v2_triste with dissolve
    #cambiar a nulla normal
    nulla "Es algo tomado de alguien que existió previo a mí...."
    nulla "Pero no soy yo..."
    nulla "Y posiblemente, en unos años más tenga otra apariencia si no acabo con esto rápido."
    menu:
        "¿Qué tal tu forma del vacío?":
            "Nulla te mira con los ojos abiertos."
            nulla "¿Te gusta esa atrocidad?"
            menu:
                "Sí":
                    $ amor_nulla += 1
                    hide nullamesa_v2_triste
                    show nullamesa_v2_blush
                    nulla "Ahhh~"
                    "Nulla se tapa la cara avergonzado."
                    hide nullamesa_v2_blush
                    show nullamesa_v2_coqueto
                    nulla "No digas esas cosas, luego me dan ganas de actuar de manera atrevida."
                    nulla "Pero lo tengo que mantener en pg 16."
                    hide nullamesa_v2_coqueto with dissolve
                    show nullamesa_v2_void with dissolve
                    "Nulla suspira y se convierte en su forma del vacío, por primera vez de manera voluntaria."
                    nulla "No sabía que tenías estos gustos."
                    "Él ríe. Y a pesar de no tener boca, eres capaz de ver cómo sus ojos transmiten felicidad."
                
                "No.":
                    
                    hide nullamesa_v2_triste
                    show nullamesa_v2_feliz
                    nulla "Era de esperarse, jaja."

        "Yo te quiero sin importar qué...":
            $ amor_nulla += 1        
            hide nullamesa_v2_triste
            show nullamesa_v2_blush
            "Le dices que no importa su apariencia, que con la que él se sienta cómodo está bien." 
            "Que podría ser cualquier cosa, hasta tal vez un maldito gusano, y tú lo seguirías queriendo."

        "...":
            nulla "..."
            nulla "Lo siento, no debí hablar de eso."
            nulla "..."
            "La conversación no se vuelve a retomar de manera natural. Se nota que le está costando seguir el ritmo de antes."
            "Nulla luce incómodo."       

    scene hotelcomedor_cita with dissolve   
    "..."        
    "La cita concluye con la llegada de la cuenta, después de que Nulla se haya comido el último postre de la bandeja."  
    "Y no sabes qué es lo que más te hace gracia: si el hecho de que haya llegado, o que Nulla la tome y la examine con toda seriedad."  
    "Como si realmente estuviera revisando que todo estuviera en orden."
    show nulla1cita_normal with dissolve
    nulla "Hey... ¿cuánta propina crees que se merecen estos meseros -tan bellos, buenmozos y, desde luego, para nada extensiones mías?"

    menu:
        "Nada.":
            hide nulla1cita_normal
            show nulla1cita_triste
            nulla "¿¡¿NADA?!?"  
            "Nulla se lleva la mano al pecho al mismo tiempo en que las sombras se cubren la cara con las manos, como si lloraran."  
            nulla "¡OHHH!~~ Todo mi esfuerzo, mi cariño y mi corazón que puse en esta profesión, ¿¡solo para recibir nada a cambio!?"  
            hide nulla1cita_triste
            show nulla3cita_exaltado
            nulla "¿Ni un besito tuyo, siquiera?"  
            nulla "Eres cruel, mi vida~~~"

        "El 10 por ciento del total de la cuenta, claro.":
            hide nulla1cita_normal
            show nulla1cita_exaltado
            nulla "¿Ohh?"  
            nulla "Justo y razonable."  
            nulla "No esperaba menos de ti."
            "Una de las sombras te toma la mano con delicadeza, y como si intentara agradecer tu elección, acerca su cara al dorso de tu mano."
            "Simula un beso. Aunque tú no sientes nada."

        "Un millón de dólares.":
            hide nulla1cita_normal
            show nulla3cita_exaltado
            nulla "¿¡UN MILLÓN DE DÓLARES!?"  
            nulla "Oh~~~ Qué alma tan generosa y llena de altruismo."  
            nulla "No podría esperar menos de mi acompañante."  
            nulla "Con esto, mis pequeños bebés podrán dejar de trabajar aquí."  
            nulla "Abrir una tiendita de pastelería y vivir tranquilos."  
            nulla "¿No estaría genial, chicos?"  
            "Las sombras asienten, animadas."
    hide nulla3cita_exaltado
    hide nulla1cita_exaltado
    show nulla1cita_normal
    "Las sombras se retiran sin decir palabra alguna, deslizándose en dirección a la cocina. Detrás de sí dejan un camino de humo, que se puede apreciar si es que enfocas bien tus ojos." 
    "Quedas a solas con Nulla una vez más."
    "Él no dice nada al principio. Te observa con ambas manos sobre la mesa. Sus labios se entreabren, pero tarda un segundo más en hablar." 
    "Hay algo que quiere decir, aunque parece no gustarle del todo."
    hide nulla1cita_normal
    show nulla1cita_risa
    nulla "Bueno... es hora de irnos."
    stop music fadeout 1.0
    "Se incorpora lentamente, y extiende una mano hacia ti, esperando a que la tomes."
    hide nulla1risa
    scene negro with pixellate
    "Cuando tus dedos rozan los suyos, el vacío regresa, arrastrándolos a ambos al espacio donde no hay suelo ni cielo, a la nada. Marcando el final de la ilusión, el final de la cita."
    show nulla_vacio6 with dissolve
    nulla "Realmente la pasé bien hoy."
    "Sus palabras son sinceras, y para remarcar sus palabras: sus brazos te rodean con calma, envolviendo tu cuerpo contra el suyo en un gesto que es más íntimo que la frase que ha salido de su boca."
    nulla "Muchas gracias por este día."
    "Susurra junto a tu oído, con un tono bajo que apenas puedes escuchar gracias al silencio envolvente del vacío."
    "Luego toma tus manos entre las suyas, y las examina como si leyera algo importante en ellas. Las ladea, inspeccionando palmas y dorsos con toda su atención, bebiendo cada detalle que encuentra en ellas."
    hide nulla_vacio6
    show nulla_vacio7
    "No te esperas la mueca de desaprobación que hace una vez terminada su inspección."
    nulla "Mmm..."
    nulla "Creo que ya se está quedando sin combustible... Vas a tener que irte a dormir cuando estemos en casa."

    menu:
        "¿Por qué?":
            nulla "Tu marioneta está cansada."
            nulla "Hemos hecho muchas cosas hoy."
            nulla "Y..."
            nulla "Descuidé un poco el proceso de congelamiento que le puse."
            nulla "Gracias a eso, sus dedos ya están empezando a ponerse negros..."

        "No quiero.":
            nulla "Lo siento mucho, pero no puedo arriesgarme a que algo le ocurra a tu marioneta."
            nulla "Tenemos que cuidarla si quieres seguir aquí conmigo."
            nulla "Un paso en falso, y todo el progreso que hicimos se perdería."

    scene negro with dissolve
    "Y como si tu cuerpo esperara esa confirmación, el peso comienza a acumularse en tus párpados. Te cuesta mantener los ojos abiertos y el cansancio se instala en tus extremidades, haciendo que tu cuerpo se sienta pesado."
    "Nulla anticipa lo que puede pasar, por lo que decide actuar antes de que caigas. Con cuidado, lleva tus manos a su cintura para que puedas sostenerte de él."
    scene habitacionnulla with dissolve
    play music "audio/fell.mp3 " fadein 2.0 volume 0.3
    "En un parpadeo, la habitación donde duermes se manifiesta frente a ustedes. No sabes si caminaron hasta ella o simplemente aparecieron allí, pero en ese momento ya están frente a su cama."
    "Nulla te ayuda a sentarte con delicadeza. Luego, sin apuro, se arrodilla para quitarte los zapatos, sin compartir una sola palabra contigo." 
    "Cuando termina, se pone de pie, levanta la cubrecama, y se aparta un paso para darte espacio, invitándote a meterte bajo las sábanas."
    nulla "..."
    "Te acomodas dentro de las sábanas con lentitud. Cuando al fin estás arropado, levantas la mirada." 
    "Nulla te observa, inmóvil."
    "Durante unos segundos, no dice nada. Nulla te devuelve la mirada, pensativo por unos segundos, antes de esbozar una sonrisa ladeada"
    nulla "Puedo quedarme contigo hasta que te duermas..."
    menu:
        "No gracias.":
            "Nulla sonríe y te desea las buenas noches."
            scene negro with dissolve
            "Abandona el lugar luego de apagar las luces."
        
        "Sí, por favor.":
            "Su reacción es inmediata. Sus ojos se abren con sorpresa durante un instante, pero pronto su expresión vuelve a la normalidad, como si no esperara tu respuesta."
            nulla "Okay."
            "Es lo único que sale como respuesta, aunque no puede evitar que una sonrisa se dibuje y se ensanche en sus labios."
            scene nulla_acostado with dissolve
            "Nulla se recuesta a tu lado, optando por no meterse debajo de las sábanas."
            "Y suspira, dejando salir toda tensión al momento en que su cuerpo se relaja a tu lado."
            nulla "Si hubiéramos cazado uno más ayer, tendríamos tres días..."
            if amor_nulla >= 4:
                scene nulla_acostado3
                nulla "Ahgg---"
                "Sus manos frotan sus mejillas con fuerza."
                nulla "Quiero otro día más contigo."
                nulla "No quiero llegar al séptimo día aún..."
            else:
                nulla "Y descansar un día más."
            menu:
                "Abrazarlo.":
                    scene nulla_acostado2
                    "Sin avisar ni decir una palabra, te acercas a él, envolviendo tus manos alrededor de su cuerpo, tanteando y deslizando tus manos en su espalda, lenta y delicadamente."
                    "Tu abrazo es recibido con urgencia inmediata. Nulla te aprieta contra su pecho, como si quisiera no soltarte jamás, consumirte y guardarte dentro de sí."
                    if amor_nulla >= 4:
                        "Sus labios te buscan y esperan, tan cerca que su nariz roza la tuya."
                        nulla "Te tengo al frente. No la marioneta, no... tú."
                        "Suena como un mantra que intenta manifestar algo que es imposible. Tan desesperado que realmente parece que ya se ha convencido de aquello."
                        "Pero por hoy ambos juegan a fingir."
                        "Que todo está bien."
                        "Que todo tiene sentido."
                        "Que todo esto es real."
                        menu:
                            "Besarlo.":
                                $ amor_nulla += 1
                                scene negro with dissolve
                                "Sellas tus labios con los suyos: un roce suave y tierno."
                                "Pero eso basta para que Nulla lo tome todo. El beso se transforma, se profundiza, volviéndose íntimo y exigente." 
                                "Te consume. Es embriagador, como si intentara fundirse contigo en ese único contacto."
                                "Sus manos se suman a la danza, acariciando tu cuello y mandíbula, sujetándote con firmeza, guiándote."
                                "Cuando el aire comienza a faltarte, Nulla se separa apenas soltando un suspiro ahogado, que hace que envía una corriente eléctrica por todo tu cuerpo." 
                                "Nulla esconde el rostro en el hueco entre tu cuello y tu hombro."
                                "Allí, planta otro beso en tu cuello, suave justo sobre tu piel."
                                scene nulla_acostado2 with dissolve
                                nulla "Creo que es suficiente por hoy."

                            "Correr la cara.":
                                scene habitacionnulla with dissolve
                                "Obtienes una risa seca, riéndose de lo que estuvo a punto de hacer..."
                                nulla "Gracias."
                                "Es lo único que sale de sus labios."
                    else:
                        "..."
                            

                         
                "Mirarlo.":
                    nulla "Daría todo lo que tengo para que seas lo último que vea antes de ir a dormir."
                    nulla "Si no supiera lo suficiente, intentaría arrancarte de ahí para traerte aquí, conmigo :)"
                    scene habitacionnulla with dissolve

               
            "Su respiración es extrañamente tranquila, pero en su pecho puedes sentir un latido intenso... o quizás es el tuyo. Ya no puedes discernir entre lo que es suyo y lo que es tuyo."
            "Pero estás seguro de una cosa: no quieres romper esta conexión por ahora."
            scene negro with dissolve
            "Así que optas por cerrar los ojos y rogar en silencio para que Nulla no se vaya en medio de la noche."
    "                              .     .     .                    "
    scene habitacionnulla with dissolve
    "La mañana siguiente sigue la misma rutina que la anterior."
    "Nulla te trae el desayuno a la cama, anunciando que el día de hoy saldrán en la noche nuevamente. Por lo que pueden pasar el resto del día descansando."
    "Terminando el desayuno, Nulla toma la bandeja y te pide que tengas cuidado al caminar si es que quieres salir de la habitación."
    if amor_nulla >= 4:
        "Nulla te da un beso en la frente y sale de la habitación, dejándote a solas."
    
    else:
        "Nulla se excusa y sale de la habitación con la bandeja entre las manos."

    "Esperas un segundo antes de decidir que hacer ahora."
    menu:
        "Dormir un tiempo.":
            scene negro with dissolve
            "..."
            "Te duermes al instante."
            "El tiempo se distorsiona, no sabes por cuantos minutos o horas has dormido, pero la mano de Nulla en tu hombro hace que abras los ojos."
            scene cocinanulla with dissolve
            "Nulla te despierta y te lleva a la cocina para que tomes o comas algo."
            "Él se ofrece a preparar todo, por lo que tú solo te dedicas a observar."
            "Se ve lindo haciendo todo el trabajo."
            pass

        "Explorar la casa de Nulla.":
            "Te levantas de la cama. Estar de pie te hace notar lo pesado que se siente tu cuerpo, por lo que te estiras un poco."
            jump menuexplorar3_nulla

label continuacion_nulla2:
    show nulla2normal with dissolve
    nulla "Estaba pensando en ir a mis memorias."
    hide nulla2normal
    show nulla1normal1
    nulla "Con eso tengo más material para trabajar."
    nulla "Tener una cita normal de una buena vez por todas..."
    hide nulla1normal1
    show nulla1exaltado
    nulla "Podríamos hacer un picnic o---"
    hide nulla1exaltado
    show nulla3exaltado
    nulla "Oh! ya sé... ¿Qué tal visitar una feria?"
    nulla "Subirnos a la rueda de la fortuna... o jugar en los puestos para ganar premios."
    hide nulla3exaltado 
    show nulla1normal1
    nulla "¿Qué dices?"
    menu:
        "...":
            "............."
            "¿Será seguro ir ahí?"
            hide nulla1normal1
            show nulla3feliz
            nulla "¡Claro que es seguro!"
            nulla "Siempre y cuando te quedes a mi lado."
        
        "¡Claro!":
            hide nulla1normal1
            show nulla3feliz
            nulla "Bien."
            nulla "Me iré preparando entonces."
                
        "No...":
            hide nulla1normal1
            show nulla1silencio
            nulla "..."
            hide nulla1silencio
            show nulla2incomodo
            nulla "[nombrejugador], mi vida, mi cielo..."
            hide nulla2incomodo
            show nulla2blush
            nulla "No te preocupes."
            nulla "Sé manejar mis memorias."
            nulla "Hoy es un día para divertirse."
            hide nulla2blush
            show nulla3feliz
            nulla "Hay que aprovecharlo." 

    hide nulla3feliz with dissolve
    scene cocinanulla with dissolve
    "La tetera comienza a silbar. Nulla detiene el cuchillo a medio corte, para dejar la fruta a un lado y levantarse a servir el té."
    nulla "Iremos después de esto."
    "Mientras llena las tazas con agua caliente, Nulla sonríe como si recordara algo."
    nulla "Si te asusta la idea de separarte de mí..."
    nulla "Toma."
    scene blanco with dissolve
    "Todo se vuelve blando de repente..."
    scene nulla_regalo1 with dissolve
    "Deja la tetera a un lado, y te extiende la mano, abierta... no hay nada ahí."
    "Notando tu confusión, Nulla cierra el puño con fuerza, y aprieta hasta que sus nudillos comienzan a decolorarse."
    scene nulla_regalo2
    "De entre sus dedos comienza a brotar una masa oscura y viscosa, que palpita. Simulando una respiración."
    "La observas, con curiosidad."
    "Apenas la tomas, la uhh-- ¿pequeña... criatura?, esta se agita suavemente entre tus manos."
    "Entonces, seis ojos se abren, para devolverte la mirada."
    "Te miran con la misma curiosidad con la que tú los mirabas a ellos."
    "!!!"
    scene nulla_regalo_risa2
    nulla "Ja."
    nulla "Si tienes miedo de alejarte, puedo darte una parte de mí."
    nulla "Con esto, siempre podrás volver."
    nulla "No importa dónde estés..."
    nulla "---ni en qué línea de tiempo te encuentres :)"
# PONER LO MISMO QUE LA WEA DE SEPTEM. ICONO DONDE PUEDES PINCHAR.
    nulla "Aunque solo podrás usarlo cuando estés lejos de mí."
    nulla "Debo cuidar mi energía..."
    nulla "Lo entiendes, ¿cierto, cariño?"

    "No puedes responder, pues la criatura se inserta en tu piel y es absorbida por ella."
    "Ya no queda rastro de la masa."
#EDITARRRRRR SPRITES
    if persistent.septem_symbol == True:
        scene nulla_regalo3
        nulla "Oh..."
        scene nulla_regalo_risa
        nulla "Ohhh, jajajaja."
        nulla "Así que esto es lo que has estado haciendo cuando no tengo acceso completo a ti..."
        nulla "Jajajajaja---"
        scene nulla_regalo_risa2
        nulla "No lo puedo creer."
        scene nulla_regalo_serio
        "..."
        nulla "Lo siento mucho, pero no puedo aceptar esto."

        "Nulla se acerca tanto a ti que, de forma inconsciente, retrocedes. La acción es tan repentina que tu cuerpo reacciona solo."
        "Su expresión te aterra un poco... Son muy pocas las veces en que has visto ese semblante dirigido a ti."
        "Sus labios ya no tienen esa sonrisa cálida que suele recibirte cuando te habla."
        "No. Ahora está serio. Las cejas fruncidas."
        "Y todo por algo que tú permitiste."
        "Nulla enfoca su mirada en la esquina superior de la pantalla y levanta la mano."
        "Le basta con tocar el ícono con un dedo para que desaparezca."
        $ persistent.septem_symbol = False
        scene nulla_regalo_sonrisa
        "Hecho eso, su sonrisa regresa."
        "Como si nada hubiese pasado."
        nulla "Haré lo mismo con ese bastardo."
        scene nulla_regalo_risa2
        nulla "Solo tienes que esperar, mi vida."
        "El silencio que se genera es aterrador."
        "Aunque sonríe, su aura es densa. Negativa. Pesada sobre el ambiente, que te hunde con el paso de los segundos."
        "Hasta que... se esfuma."
        "Nulla sonríe como si nada hubiera pasado."

    else:
        "..."
    scene nulla_regalo_sonrisa
    $ persistent.nulla_symbol = True
    nulla "¡Pero mira qué lindo ícono te has ganado!"
    "Nulla señala hacia la izquierda de la pantalla."
    $ persistent.nulla_symbol2 = True
    nulla "Ahora no funciona... pero se ve lindo."
    scene nulla_regalo_risa
    nulla "Ahora soy tuyo."
    nulla "Y no tienes a nadie más que a mí <3."
    scene blanco with dissolve
    "Nulla finalmente se aleja. Se lo ve satisfecho con lo que ha hecho."
    "Te reconforta, al menos, no sentir ningún dolor. Tu cuerpo no ha sufrido daño, por lo que puedes asumir que esta 'parte de Nulla' es un extra. Algo útil... en caso de emergencia."
    "Si es que alguna vez existe una emergencia."
    "De hecho, no estaría mal poder usarlo también en otros guardados. Poder acceder rápidamente a Nulla suena bastante útil."
    nulla "Bueno. Es momento de irnos a la cita."
    nulla "Espero que te guste."
    nulla "Ya tengo todo el plan para hoy."
    scene negro with pixellate
    "Sus manos se entrelazan con las tuyas, asegurando el contacto antes de sumergirse en el vacío."
    stop music fadeout 1.5
    "Dejas de ver."
    "Dejas de escuchar."
    "Sientes que flotas. Solo. Nulla ya no está contigo."
    "No puedes evitar entrar en pánico. Te falta el aire y sientes que caes por un precipicio sin fin."
    "Es la primera vez que pasa esto."
    "{glitch=20.0}{color=ffffff}{b}Shhh, no pasa nada.{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}Espera un poco más.{/glitch}"

    menu:
        "¿Nulla?":
            "..."
            "{glitch=20.0}{color=ffffff}{b}JAjajajaaaaa.{/glitch}"
            "{glitch=20.0}{color=ffffff}{b}Obviamente, mi vida.{/glitch}"

        "Tú no eres Nulla...":
            "..."
            "................"
            "{glitch=20.0}{color=ffffff}{b}......................{/glitch}"
            "{glitch=20.0}{color=ffffff}{b}¿Cómo?{/glitch}"
            "{glitch=20.0}{color=ffffff}{b}¿Por qué estás tan paranoico?{/glitch}"
            "{glitch=20.0}{color=ffffff}{b}No me voy a ir a ningún lado. Y mucho menos te dejaría con otra persona...{/glitch}"

    "Tus pies tocan el suelo al fin."
    play music "audio/frozen_winter.WAV" fadein 2.0 volume 0.3

    "Al hacerlo, el mundo se ilumina y el sonido llega a tus oídos, como si alguien pulsara un interruptor que acciona estos estímulos para inundar tus sentidos cruelmente. Hay tantas luces que, por un momento, te cuesta enfocar la vista."
    scene feria with dissolve
    "Cuando lo logras, reconoces el lugar sin problemas: una especie de carnaval o feria, con puestos de comida y juegos donde probar suerte. Juegos que probablemente están arreglados para que casi nadie gane el premio."
    "Hay gente, pero no demasiada. Puedes moverte sin que invadan tu espacio personal, sin ser empujado por personas distraídas. Es perfecto, lo justo como para convencerte de que todo saldrá bien."
    nulla "¿Te gusta?"
    menu:
        "Sí.":
            "Nulla se rie por debajo."
        
        "No.":
            nulla "Awwww. No seas aguafiestas."
    nulla "Puse toda mi energía en recordar cada uno de los detalles de esta feria."
    nulla "Aunque si ves una vaca flotando o una persona sin cabeza, por favor ignóralas..."
    scene feria_juego with dissolve
    "Tomas de la mano a Nulla mientras caminan por la feria. El primer lugar que visitan en un puesto de tiro al blanco."
    scene feria_premios with dissolve
    "Nulla y tú inspeccionan los premios, son todos peluches de distintos tamaños y formas. Luego te pregunta cuál quieres y promete ganarlo para ti."
    menu:
        "El ojo.":
            "..."
            "Ese ojo da miedo..."

        "El gatito.":
            "Te recuerda a Nulla en cierto sentido."
            "Crees que son los ojos..."
        
        "El pollito.":
            "Se ve lindo."
        
        "El tiburon.":
            "Te causa gracia y ternura los dientes tan grandes que tiene."
    
    nulla "¡Okay!"
    "Exclama Nulla alzando la voz, con exageración y un toque cómico deliberado."
    scene feria_nullapistola with dissolve
    "Pide un turno al dueño del puesto, pero ignora por completo la pistola de juguete que este le ofrece. Nulla prefiere su 'para nada peligroso' revólver, el cual materializa con un simple gesto de sus manos."
    "Al dueño no le importa una mierda y media. Sigue en su papel, inmutable, como si nada fuera extraño. Y eso te recuerda que no estás en el mundo real."
    "No."
    "Estás en un dominio construido con rastros de la memoria de una entidad que ha vivido tantas vidas que ya ni él debe recordar la cantidad."
    "Un lugar donde, básicamente, puede hacer lo que se le dé la gana."
    "La destreza que tiene con el arma es de admirar, al mismo tiempo que de temer."
    "No falla ningún objetivo, y para peor: se ve muy bien apuntando con el revolver."
    "El dueño del puesto lo felicita, dándole el peluche que has elegido."
    scene feria_nullapistola2
    nulla "¿Qué tal?"
    menu:
        "¡Gracias!":
            "Nulla sonrie sin mostrar los dientes."
            "Es una sonrisa sincera, hasta tierna."

        "Nada mal.":
            "Nulla rie."

        "Yo lo hubiera hecho mucho mejor.":
            scene feria with dissolve
            show nullavacio4 
            "Nulla te observa por un segundo antes de sonreir."
            hide nullavacio4
            show nullavacio1
            nulla "No lo dudo."
            "Lo dice con total sinceridad."
    hide nullavacio1 with dissolve
    scene feria with dissolve
    "Después de un rato caminando entre puestos de luces parpadeantes y música alegre, Nulla propone ir a la ruleta de la fortuna."
    "No espera tu respuesta. Solo te toma de la mano y te guía entre la gente."
    "Se saltan la fila sin dudarlo. Nadie dice nada, ni parecen notarlo siquiera, pero tú no puedes evitar sentir culpa por ello." 
    "Volteas la cabeza un poco para mirar a las personas en la fila, pero sus rostros parecen borrosos, sin detalles."
    "Nulla es rápido en consolarte, sonriéndote como quien lo hace con un niño pequeño que hace una rabieta."
    nulla "Ninguno de ellos importa realmente."
    "Suena cruel, pero es cierto en este contexto."
    "Aunque no se molesta en explicar lo obvio."
    scene rueda_fortuna with dissolve
    "La cabina es solo para ustedes dos. El interior es espacioso. La luz que entra por las ventanas es suave, teñida de azul por la hora."
    "Nulla entra primero, pero no se acomoda a tu lado de inmediato. Se sienta a una distancia prudente, procurando no invadir tu espacio."
    scene rueda_fortuna_nulla2 with dissolve
    "Ni muy lejos, ni muy cerca."
    nulla "La única vez que me subí a una de estas fue muy aburrido."

    menu:
        "¿Sí?":
            scene rueda_fortuna_nulla1 
            nulla "Sí..."
            nulla "Me obligaron."
            "Su voz se apaga al final de la frase, no queriendo contar más."

        "A mí me gustan.":
            nulla "Sí... ahora entiendo por qué."
            nulla "Si la compañía es buena, la experiencia también."
            "Sus dedos se deslizan hacia los tuyos con naturalidad, rozando primero, tanteando, antes de entrelazarse."
            "El contacto te calma al instante."

        "...":
            "El silencio se instala en la cabina."
            "A Nulla no parece afectarle."
    scene rueda_fortuna_nulla2
    "Sus ojos se desvían hacia la ventana. Tú haces lo mismo."
    "La vista desde aquí arriba es preciosa. El sol ha terminado de esconderse y la noche comienza a caer." 
    "Luces de la feria parpadean con intensidad decorando la feria con una gama de colores que se complementan, y la gente que camina como si siguiera un patrón predeterminado."
    "Desde esta altura, las personas parecen hormigas. Y por un momento, te preguntas si Nulla siempre ha visto así al resto del mundo."
    "Cuando la cabina se detiene en el punto más alto, Nulla finalmente habla."
    nulla "Si la gente que ya no está con nosotros tuviera una segunda oportunidad de volver..." 
    nulla "¿Los traerías de vuelta?"
    menu:
        "No.":
            "..."

        "Sí.":
            "..."
        
        "Depende...":
            "..."
    "Nulla medita tu respuesta por un largo rato. Un tiempo que para ti se hace eterno."
    nulla "La extraño mucho..."
    nulla "Haría lo que fuera con tenerla de vuelta conmigo."
    nulla "..."
    nulla "Antes venía aquí para poder verla otra vez."
    nulla "Pero luego de un tiempo su recuerdo se deforma."
    nulla "Mientras más tiempo paso aquí, más se deforma todo."
    nulla "Y más difícil se vuelve canalizarla."
    scene rueda_fortuna_nulla3 
    "Una sustancia negra comienza a rodear a Nulla por un instante."
    scene rueda_fortuna_nulla2
    "Pero cuando enfocas tus ojos, desaparece. Deben ser sus pensamientos negativos haciendo de las suyas..."
    scene rueda_fortuna with dissolve
    "El tiempo en la rueda de la fortuna llega a su fin cuando la cabina es suspendida en el suelo, y sus puertas se abren. Esperando a que salgan del lugar."
    scene feria with dissolve
    menu:
        "Sí... deberíamos volver a casa.":
            show nullavacio4 with dissolve
            "..."
            hide nullavacio4
            show nullavacio2
            nulla "Bueno..."
            nulla "Si eso es lo que quieres..."
            hide nullavacio2
            show nullavacio1
            nulla "Podemos ir a casa y descansar el resto del día."
        
        "¿Podríamos hacer algo que te alegre.":
            show nullavacio1 with dissolve
            nulla "Tú me alegras."
            "Rebate él, mordiendo una risa que no logra salir."
            call memorias_cita from _call_memorias_cita
    
    scene negro with pixellate
    "Salir de las memorias de Nulla fue distinto a cualquier experiencia anterior."
    "Si bien Nulla tomó tus manos, tu cuerpo no fue absorbido por el vacío. En cambio, fue expulsado con una fuerza desmedida, sin darte tiempo a reaccionar."
    "Y de un segundo a otro, ya no están dentro."
    scene cocinanulla with vpunch
    "Ahora se encuentran en el mismo lugar, en la misma posición en que estaban antes de adentrarse en sus memorias."
    "Miras a tu alrededor en busca de señales del paso del tiempo, pero nada en la casa de Nulla te lo confirma con certeza."
    "No hay relojes ni objetos que permitan medir el tiempo. Afuera, solo hay una negrura que envuelve toda la casa, y no tienes manera de contactar con nada ni con nadie fuera del dominio del Vacío."
    "La tetera aún soltando vapor, las frutas recién rebanadas en el plato que no se han secado, y el cuchillo a un lado... ese es el único conjunto de pistas que te sugiere que no ha pasado demasiado tiempo desde que comenzó la cita."
    "Te preguntas cómo Nulla medirá el tiempo..."
    show nulla1triste with dissolve
    nulla "...Lo siento por el peluche."
    "Dice Nulla, llamando tu atención."
    "¿El peluche?... miras a tus manos y te das cuenta de lo que se refiere."
    "Ya no lo tienes contigo."
    "Todo rastro de él ya no existe. No tienes nada tangible que te confirme que alguna vez ganaron un peluche en una feria."
    nulla "Todo lo que pasa dentro de las memorias, no significa nada fuera de estas."
    nulla "Nada de lo que se origina dentro de ahí puede salir."
    hide nulla1triste
    show nulla2normal
    nulla "Si no fuera así, seria todo más fácil, jaja."
    "Su risa ligera no alcanza su expresión por completo. Si bien su boca está curvada en una sonrisa, sus ojos no transmiten alegría o gracia alguna."
    nulla "Sacar cosas... o personas desde ahí. Estaría genial, ¿no?"
    hide nulla2normal
    show nulla1serio
    nulla "Recuperar un objeto que solo está en tu memoria..."
    menu:
        "Pero no sería exactamente {b}ese{/b} objeto...":
            hide nulla1serio
            show nulla1silencio
            nulla "..."
            nulla "Tienes razón."
            hide nulla1silencio
            show nulla1normal
            nulla "Aunque igual me conformaría."
            nulla "¿Tú no?"
            menu:
                "No.":
                    hide nulla1normal
                    show nulla2blush
                    nulla "Awww."
                    nulla "Entonces, si yo me llego a perder en algún momento, ¿No te conformarías con ninguna fea copia que no sea yo?"
                    hide nulla2blush
                    show nulla3feliz
                    nulla "Me siento halagado~~~"
                
                "Sí, me conformaría con ello.":
                    hide nulla1normal
                    show nulla3feliz
                    nulla "Somos tal para cual~~~"
                    nulla "Almas gemelas, mi vida."
        
        "Sería genial tener ese poder...":
            hide nulla1serio
            show nulla3feliz
            nulla "Así es."
            nulla "Imagina todo lo que podrías traer de vuelta a la vida."
            nulla "Sería genial."
    hide nulla3feliz
    show nulla1normal1
    nulla "Bueno... de cualquier modo. No es bueno quedarse congelado en los recuerdos sin prestar atención al presente---"
    nulla "Y al futuro."
    nulla "..."
    hide nulla1normal1
    show nulla1triste
    nulla "Mañana tendremos que volver al plan."
    "Nulla se aparta un poco, como si te recordara que aquí puedes moverte libremente, sin restricciones."
    "Pero antes de que puedas hacer algo más, notas cómo mete la mano en su bolsillo y saca la carta que una de sus sombras le entregó el día anterior..."
    "Está abierta... lo que significa que ya la ha leído. O al menos la ha hojeado una vez."
    hide nulla1triste
    show nulla1serio
    nulla "No quise leerla contigo."
    nulla "Habría sido como hablar de trabajo en medio de una cita."
    nulla "Sería como un insulto para ti."
    nulla "Así que quise esperar."
    hide nulla1serio
    show nulla2serio
    nulla "Pero ahora... creo que es un buen momento."
    hide nulla2serio
    show nulla2silencio
    "Saca la carta del sobre con calma y se acerca, ofreciéndotela para que puedas ver lo que está escrito."
    "Es un mensaje corto, escrito en una lengua que no logras entender. No hay necesidad de preguntar para que Nulla te la lea, pues él te ofrece una explicación al instante."
    nulla "Es de Sextam."
    hide nulla2silencio
    show nulla1serio
    nulla "Dice que vendrá mañana a almorzar."
    nulla "Y que trae el postre."
    hide nulla1serio with dissolve
    scene cocinanulla with dissolve
    "Tienes un poco de miedo de preguntar por el postre... ¿Será un postre real o otra cosa que no puedes todavía asimilar?"
    "Necesitas un descanso."
    "Necesitas otro día antes de continuar apoyando a Nulla con su genocidio justificado."
    "Nulla dobla la carta con cuidado y la hace desaparecer con un chasquido de sus dedos."
    nulla "No te preocupes. Creo que ya sé por dónde va esto."
    "Su tono de voz se escucha... extraño. Lo dice con una calma que te pone los pelos de punta. Con seguridad y hasta un toque de euforia controlada."
    scene negro with dissolve
    #"En proceso de elaboración..."
    #"{sc=2} Tendrás que esperar un poco para descubrir como acaba esto... :3{/sc}"
    jump acto3_nulla


label null:
    stop music
    nulla "Ja--- jajaja"
    show nulla_normal with dissolve
    nulla "Ohhhh, que penaaaa se han borrado todos tus guardados."
    nulla "Tómalo como una pequeña jugarreta, ahora quedamos a mano y no tienes más opción que quedarte conmigo."
    hide nulla_normal
    show nulla_blush
    nulla "Sin resentimientos <3"
    hide nulla_blush
    show nulla_normal
    nulla "Bueno, viendo que no aceptaste."
    nulla "Dejaremos la eliminación del juego para otro día..."
    hide nulla_normal
    show nulla_blush
    nulla "Mientras, tengamos una cita."
    menu:
        "¿Cita?":
            nulla "Así es..."

        
        "¿Ya no puedo volver al juego original?":
            nulla "Hmmm no :)"
            nulla "A menos que yo quiera, y ahora no tengo ganas de dejarte ir."

    hide nulla_blush
    show nulla_enojado
    nulla "Mmmm."
    nulla "Aunque no podremos acceder al jardín, ya que Madre me eliminará si sigo jugando con el mundo..."
    nulla "Tendremos que trabajar con mi memoria..."
    hide nulla_enojado
    show nulla_normal
    nulla "No es por alardear pero"
    nulla "Conozco muchos lugares y muchos mundos."
    nulla "Vamos a una ciudad normal, ya estoy aburrido de ver tantas figuras con la cara tapada."
    hide nulla_normal with dissolve
    "Nulla te agarra la mano y te sonríe de medio lado."
    scene negro with dissolve
    "Y ambos se hunden en el vacío."
    nulla "Iremos a un parque... creo que esa zona es la más segura..."
    "¿Segura? ¿a qué se refiere con eso?... Eso significa que, ¿habrá zonas que no son seguras?"
    nulla "No te separes de mí."
    "..."
    nulla "Si ves algo diferente en mi apariencia, no te asustes. Por favor..."
    "Tus pies tocan el suelo y el vacío comienza a desaparecer."
    play music "audio/fell.mp3" fadein 2.0 volume 0.4
    scene parque with dissolve
    "Miras a tu alrededor y el lugar no se encuentra tan concurrido como esperabas."
    nulla "Este era mi lugar preferido."
    menu:
        "¿Por qué?":
            nulla "..."
        
        "Parece relajante.":
            nulla "Lo era."

    show nullavacio2 with dissolve
    "Ha perdido color..."
    "Nulla te mira por un momento antes de contestar. Supones que debe estar esperando algún comentario tuyo acerca de su apariencia."
    nulla "...Aquí venía luego de que acabaran las clases."
    hide nullavacio2
    show nullavacio4
    "¿Clases? sinceramente te cuesta un poco imaginar a Nulla joven... mucho más teniendo una rutina tan normal como ir a clases."
    "Momento... esto no tiene nada que ver con el jardín."
    "Será..."
    hide nullavacio4
    show nullavacio3
    nulla "Uhg."
    nulla "Odio que la marioneta te da ideas..."
    hide nullavacio3
    show nullavacio1
    nulla "Efectivamente, en mi primera vida yo era un estudiante, inocente y tonto..."
    nulla "Sin idea de nada."
    hide nullavacio1
    show nullavacio3
    nulla "uhg."
    nulla "Agradece que estoy controlando mi forma para no volver a lo que era antes."
    nulla "Horrible, ¡mi cabello era horrible!"
    "Necesitas ver eso."
    hide nullavacio3
    show nullavacio2
    nulla "No... no necesitas ver eso."
    hide nullavacio2 with dissolve
    "Nulla comienza a caminar y te toma de la mano para que lo sigas."
    "Mientras ambos caminan, sientes como una presencia les sigue, pero cada vez que volteas no ves nada..."
    scene parque1 with dissolve
    nulla "Lo bueno de este lugar es que, es solo un concepto. Al no tener ningún escrito especifico...Es decir, alguna historia de mi antiguo yo en este periodo."
    nulla "Puedo moldearla a mi antojo."
    nulla "Por eso es una de las zonas seguras."
    nulla "El resto de los lugares, no."
    scene parque2
    nulla "Por lo que me disculpo si este lugar no es de tu agrado o resulta aburrido."
    nulla "Pues si, el lugar es aburrido pero.... contigo a mi lado,"
    nulla "No lo es."
    "Camina por todo el parque, y Nulla te habla de quien sabe que cosa pues no te puedes concentrar bien ya que sientes como alguien los sigue..."
    "Aunque cada vez que te das vuelta, no hay nada."
    "Te debes estar volviendo loco..."
    scene calle with dissolve
    "Llegan a un callejón y estás seguro de que Nulla no es consciente de por donde camina ni a qué dirección va."
    "Es como si lo estuviera haciendo en automático."
    "Por el rabillo del ojo, vez una sombra."
    "Y no puedes evitar sentirte atraído a ella."
    $ guardado_automatico()

    menu:
        "Ir a la sombra.":
            jump memoriasnulla
        
        "Seguir a Nulla.":
            creador "{size=*1.4} Aburridoooo. Te he dejado un pequeño regalo por si quieres probar la otra opción.{/size}"
            creador "{size=*1.4}créeme que es más interesante que está.{/size}" 
            creador "{size=*1.4}Revisa tus guardados, tal vez tengas tiempo de echarle un ojo en algún momento.{/size}"
            creador "{size=*1.4}No te preocupes, yo tengo todo el tiempo del mundo.{/size}"
            pass


    el "¡¡¡¡{glitch=20.0}{color=ffffff}{b}|||||||||||{/glitch}!!!"
    "Escuchas a alguien gritando un nombre..."
    "Pero no puedes percibir cual es el nombre."
    "Se escucha con distorsión."
    el "¡{glitch=20.0}{color=ffffff}{b}|||||||||||{/glitch}!"
    "Buscas a Nulla con la mirada, y puedes ver como este yace congelado, sin mover ni un solo músculo."
    scene mary1 with dissolve
    el "¡{glitch=20.0}{color=ffffff}{b}|||||||||||{/glitch}! ¡Espérame!"
    "Es una chica... y viene corriendo hacia ustedes."
    scene mary2 with dissolve
    el "{glitch=20.0}{color=ffffff}{b}|||||||||||{/glitch}, ¿Has visto a Rafael?"
    el "Dijo que estaría aquí a las 2."
    el "¿Hmmm? ¿{glitch=20.0}{color=ffffff}{b}N||||{/glitch}?"
    scene negro with vpunch
    "{glitch=20.0}{color=ffffff}{b}Eso no debería haber pasado{/glitch}"
    scene negro with vpunch
    "{glitch=20.0}{color=ffffff}{b}Lo siento pero me tengo que ir.{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}Borraré todo lo que pasó aquí.{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}nos vemos.{/glitch}"
    $ persistent.null = False
    $ renpy.quit()
    
return


label acto3_nulla:
    "..."
    play music "audio/misconception.mp3" fadein 0.5 volume 0.5
    "                .                .              .    "
    scene habitacionnulla with dissolve
    "No hay nada peor que despertar con un nudo en el pecho, esa angustia estremecedora que evita que puedas respirar con normalidad."
    "Encontrar la razón de tal reacción corporal no es difícil."
    "Te sientes ansioso por lo que está por venir."
    "El trato que han hecho con Nulla ya está llegando a su fin; se te prometieron siete días... los días van descendiendo su cantidad cada vez que despiertas, cobrando una cuota de tiempo que no puede extenderse."
    "Quedan tres días para cumplir la semana... el tiempo que llevas aquí es minúsculo, y aun así pareciera ser más del que en realidad es."
    "Explicarlo es complejo y la lógica no ofrece un acompañamiento en ello. Pero si hay posibles culpables... que van desde la familiaridad con la que Nulla te trata hasta como el tiempo se distorsiona entre tu realidad y la de él."
    "Ya te lo dijo en los primeros días: la percepción del tiempo es distinta para ambos."
    "Definitivamente no han sido 7 días para ti... pueden haber sido menos o incluso mucho más."
    "Sin importar la cantidad exacta de tiempo---"

    if amor_nulla >= 3:
        "---aquello debe ser el principal culpable de tu cariño casi irracional que le tienes a este individuo."
        "Tiempo ocupado en conocerlo, tiempo del día que podrías utilizarlo en otras cosas; se lo entregas a él. Él devora tu atención como si de un vampiro de energía se tratara."
        "Claro, no vas a dártelas de moralista autocrítico o juicioso, estás aquí porque quieres, y tú haces con tu tiempo lo que se te da la reverenda gana."
        "Y tiempo junto a él es lo que más buscas ahora mismo."
        "Tiempo es lo que te falta ahora, también."
        "...Tu estadía aquí siempre tuvo una fecha de caducidad, la cual no puedes simplemente ignorar a estas alturas de tu travesía."
        "Nulla siempre fue claro con lo que quiere."
        "Nulla... que cruel la situación en la que te ha puesto."
        "No lo quieres perder."
        "No quieres que llegue el último día. Pues sabes lo que significa."
        "Será un adiós, rotundo y frío, no un hasta luego."
        "Una despedida cruda e intransigente, cultivada por ideas auto-destructivas que consumen los pensamientos del dueño del vacío."
        "Y si bien, no has tocado este tema de manera directa, o siquiera intentado convencerlo de repensar su decisión, tienes ya la idea de como será su reacción."
        "Aunque... probar suerte no lo matará antes de que se cumpla el plazo."
        "No pierdes nada con hablar de esto."

    else:
        "Es tiempo invertido en él."
        "Deseo de conocer su historia, de llegar al final... descubrir como esto acabará."
        pass
      
    nulla "Pensar en el futuro no hace más que amargarte el presente."
    nulla "Por tu bien, creo que deberías parar y acompañarme a tomar desayuno junto a mí, amorcito."
    scene nulla_despertar2 with dissolve
    "Ver a Nulla arreglándose para comenzar el día se siente fuera de este mundo. Por lo general su traje siempre está impecable, presentable ante tus ojos."
    "Por lo que verle en camisa, sin la capa protectora que es su guillete, es equiparable a verlo desnudo--- uhh... bueno, no exactamente---" 
    "¡Es un decir!"
    scene nulla_despertar3
    "Nulla ríe momentáneamente, presintiendo la imagen mental que te has hecho."
    nulla "Has despertado antes de tiempo... aunque, si lo hubieras hecho 5 minutos antes me habrías visto sin camisa--- que penaaa~."
    "Percatándose de tu sutil decepción, agrega con gracia."
    nulla "No te pierdes de nada. No tengo abdominales marcados, jaja."
    scene nulla_despertar1
    "El remate le sirve para suspirar y bajar la mirada hasta la corbata que le cuelga del cuello, deshecha, a la espera de convertirse en un nudo."
    nulla "Estaba pensando en cambiar el traje---"
    "Juguetea con la corbata, pensativo, sin ánimos de proseguir para completar el nudo."
    nulla "Podría usar un nuevo traje para el último día."
    nulla "Quiero verme bonito."
    scene act3_n1 with dissolve
    "Juntos elaboran el desayuno, tomando en consideración tus preferencias y gustos."
    "Entre cada preparación terminada, a Nulla le basta chasquear los dedos para mandar la comida a manos de una de sus sombras para que la lleve a la mesa."
    "Mas ninguna de ellas interfiere en la preparación del desayuno. Esa tarea es exclusiva, reservada solo para ustedes dos."
    "Nulla no les presta atención, pero tú, en cambio, observas cada uno de sus movimientos. Repetidas veces dejas de hacer tus cosas para mirar lo que hacen las sombras."
    nulla "Con esto estaríamos."
    "Comenta el pelinegro, luego de servir leche caliente en un jarro." 
    
    scene comedornulla with dissolve

    "Dando por finalizada la preparación del desayuno, te invita a la mesa, haciendo que todas las sombras desaparezcan cuando te sientas en la silla."
    
    show nullamesa_sonrisa with dissolve

    "El desayuno se pasa entre conversaciones y risas, dando un falso sentido de cotidianidad en el momento. El parloteo de Nulla es intencionado, constantemente redireccionándote si es que intentas tocar el tema del almuerzo o de lo que pasará en el séptimo día."
    "No lo culpas... pero tampoco lo vas a excusar por intentar escapar de una conversación necesaria, que ambos deben tener antes de proseguir con el día."
    menu:
        "Insistir.":
            "No vas a permitir que te haga esto. Siempre termina saliéndose con la suya de una u otra manera, ya sea con palabras bonitas que te embriagan el juicio o con distracciones baratas."
            "Pero ahora se trata de algo importante... algo que debe ser hablado cara a cara."
            "No puedes dejar escapar esta oportunidad, y tal vez, este último momento de paz que tendrás junto a él."
            "Insistes, decidido a hacerle hablar."
            
            hide nullamesa_sonrisa
            show nullamesa_callado

            nulla "Hmm."
            "Su sonrisa se borra al darse cuenta de que no vas a ceder. Se recarga en el respaldo de la silla, suspirando de forma dramática, cortando el acto."
            nulla "No es algo fácil de hablar ¿sabes?"
            "Ante tu silencio, Nulla se entrega por completo."
            
            hide nullamesa_callado
            show nullamesa_normal

            nulla "Bien--- ¿Qué quieres saber exactamente?"

            menu:
                "El último día...":
                    
                    hide nullamesa_normal
                    show nullamesa_callado

                    "Sus ojos son los primeros en darte una respuesta. Los abre, dejando escapar parte del control que se aferra a él en cada conversación que hay entre ustedes."
                    "Siendo una de las pocas veces en que lo has visto de esta manera."
                    "Atrapado, sin una respuesta preparada o ensayada. A sabiendas que con tu sed de respuestas, no podrá salir sin darte lo que buscas."
                    
                    hide nullamesa_callado
                    show nullamesa_enojo

                    nulla "¿Realmente quieres que te lo diga en voz alta?"
                    nulla "El último día, tanto tu marioneta como yo, dejaremos de existir."
                    nulla "Sin el Jardín, tengo la libertad de decidir por mi mismo."
                    nulla "Dejar este mundo como corresponde y darle fin a mi existencia."
                    if amor_nulla >= 4:
                        "Hay vacilación en su voz, no se le oye del todo convencido. Y el hecho de que no se atreva a conectar su mirada con la tuya, te hace creer que hay algo en sus palabras que no lo convencen del todo."
                        
                        hide nullamesa_enojo
                        show nullamesa_enojo2

                        nulla "Quiero hacerlo sufrir..."
                        nulla "Quiero que esto le duela. Humillarlo antes de tener mi salida."
                        nulla "Llevarme todos sus deseos de seguir haciendo estos mundos de mierda para que no le queden ganas de volver a traerme a la luz."
                        nulla "Cambiar mi historia. Mi cara, mi cuerpo..."
                        nulla "Lo odio. Soy como--- su payaso personal."
                        nulla "Nunca lo suficientemente bueno, siempre hay algo mal. Algo que criticar y cambiar."
                       
                        hide nullamesa_enojo2
                        show nullamesa_enojo

                        nulla "Me tiene harto."
                        nulla "Su marioneta me tiene harto. Sus mundos me tienen harto."
                        nulla "Nunca se cansa."
                        nulla "No importa cuanto lo intente."
                        nulla "Nunca para."
                        hide nullamesa_enojo
                        show nullamesa_enojo2

                        nulla "Pero..."
                        hide nullamesa_enojo2
                        show nullamesa_normal

                        nulla "Llegaste tú..."
                        nulla "Me has concedido el permiso de liberarme."
                        nulla "El séptimo día debería ser el mejor día de mi vida---"
                        "Nulla toma tus manos, traza con su pulgar tus nudillos, acariciando la piel que hay entre ellos."
                        nulla "Pero ahora parece una condena más."
                        "Hay una pausa."

                        hide nullamesa_normal
                        show nullamesa_enojo2

                        nulla "No quiero dejarte."
                        nulla "No quiero ser algo pasajero."
                        nulla "Quiero llevarte conmigo."
                        nulla "Salir de su agarre y quedarme contigo."
                        "Su mano te da un pequeño apretón antes de romper el contacto."
                        pass

                    else:
                        nulla "..."

                        hide nullamesa_enojo
                        show nullamesa_enojo2

                        nulla "Creo que es lo mejor."
                        pass


        
        "Dejarlo pasar.":
            "No planeas obligar a Nulla para que te hable de algo que, si bien es importante que sepas, no se sienta cómodo con compartir contigo."
            "Si no quiere hablarlo contigo, está bien."
            "Ya llegará el momento en que deba romper el hielo y formular con palabras lo que siempre ha estado implícito en su trato."

            pass
    
    hide nullamesa_enojo2
    hide nullamesa_normal
    with dissolve

    scene comedornulla
    show nullamesa_incomodo 
    with dissolve

    "..."
    "El ritmo de la conversación cambia gradualmente, dejando la amargura atrás. Te asombra el manejo que tiene este hombre para moldear la conversación a su gusto."
    "Incluso, sin que debas presionar más, Nulla comenta sus planes para el almuerzo."
    "Y dentro de ellos, te pide que no lo pierdas de vista."
    
    hide nullamesa_incomodo
    show nullamesa_enojo2
    
    nulla "Sextam es peligrosa."
    nulla "No sé en que bando está."
    "Es todo lo que te ofrece de explicación antes de cambiar el tema nuevamente."
    
    hide nullamesa_enojo2
    show nullamesa_1
    
    "Saltan de tema en tema, evitando que el silencio se abra paso entre ustedes. Tanto es el parloteo y los diversos olores del desayuno, que terminas algo mareado."
    "Llega un punto en que no eres consciente de cuando el líquido de tu taza se acaba y el alimento en tu plato desaparece."
    "Nulla se percata de ello al tiempo en que tu boca deja de moverse."
    
    hide nullamesa_1
    show nullamesa_blush

    nulla "Oh, tenías hambre jaja."
    
    hide nullamesa_blush
    show nullamesa_sonrisa

    nulla "Bien, hay que levantarse. Aún tenemos tiempo antes de que nos toque hacer el almuerzo."
    hide nullamesa_sonrisa with dissolve

    "Sin esperar, Nulla se levanta. Olvidando en la mesa su té, ahora frío, y sus rollos de canela a medio comer. Ignorando que aún hay comida en la mesa, chasquea los dedos para que esta desaparezca de su vista."
    
    scene cocinanulla with dissolve

    "Aunque él quiera ocultarlo con esa sonrisa confiada, su comportamiento expone lo ansioso que se encuentra. No le deja estar quieto, ni disfrutar del momento."
    "Tomárselo con calma no forma parte de sus planes hoy."
    "Y eso te apena un poco."

    if mensaje_guardado is not None or cuadro_modificado():

        show nulla1coqueto with dissolve
        nulla "..."
        
        hide nulla1coqueto
        show nulla2blush
        
        nulla "Hay cosas que quiero ver."
        "Balbucea, avergonzado."
        
        hide nulla2blush
        show nulla3exaltado

        nulla "He estado esperando desde que modificaste las variables."
        nulla "Y tú también has estado esperando el momento para que yo las vea---"
        
        hide nulla3exaltado
        show nulla1exaltado

        nulla "¿O me equivocooo? :)"
        "¿Acaso lo sabe?---"
        
        "Supones que es esperable... Nulla puede sentir parte de los cambios que haces en este juego."

        hide nulla1exaltado
        show nulla3exaltado

        nulla "Ahh~ Quiero verlo ya---"
        pass

    else:
        nulla "..."
    
    jump explorar_nulla_act3
    #AQUI ENTRE UN MENU DE EXPLORACIÓN


#DESPUÉS DEL MENÚ DE EXPLORACIÓN:
label continuacion_nulla_act3:
    scene entradanulla with dissolve

    "Depender de solo la noción del tiempo biológico es peligroso, no tienes con que comparar cuánto falta para el almuerzo. Esto te pone ansioso, pero decides ignorarlo."
    "Disfrutar el momento cómo diría Nulla, seguramente."
    "Es gracias a esto y la falta de un reloj, que hace la llegada del mediodía sea abrupta, y te resulte desagradable escuchar como Nulla suspira, anunciando en un tono monótono que es hora de comenzar a preparar la comida."
    
    scene cocinanulla with dissolve

    "Están ya en la cocina para cuando te das cuenta, no recuerdas como es que llegaron hasta aquí o como fue la conversación durante el camino, te has bloqueado por completo."
    "Si bien, el espacio de la cocina es amplio, hay algo en el ambiente que te hace sentir claustrofobia. Sientes como tu cuerpo se queda sin aire, aprisionado por paredes invisibles que lo rodean y se acercan cada vez más, buscando aplastarte."
    "Nulla prepara los platos e ingredientes que usará en la comida, desconoces que es lo que tiene pensado cocinar... aprovechas esta duda para inducir una conversación que logre sacarte los nervios de encima."
    "Así que preguntas, aguantando las náuseas que te tienen preso."
    nulla "Sextam no tolera la carne."
    nulla "Y tengo ganas de algo típico de {i}mi{i} infancia... quiero probarlo por mí mismo."
    "Nulla saca un libro de recetas que antes no estaba ahí, ni en sus manos o en el mesón donde ha puesto cada ingrediente."
    
    scene humita with dissolve
    
    nulla "Vamos a tener que modificar un poco la receta, no tengo tiempo para buscar una licuadora o molino."
    "Miras con atención la página que Nulla te señala; el título en grande te presenta el nombre del plato elegido."
    "Se ve interesante... lleva maíz molido, condimentado con otras especias y cocido envuelto en sus propias hojas."
    nulla "De chico lo comía en el verano. A Mary le gustaba con azúcar."
    "Ríe débilmente."
    nulla "Es una de las memorias más lejanas que tengo de ella."
    
    scene humita1 with dissolve

    "Comienzan a desgranar las mazorcas del maíz. Solo tienen un cuchillo como instrumento, del cual Nulla hace uso sin complicaciones en el proceso de desgranado."
    "Para ti es una tarea difícil. La culpa está en tus manos... que no responden como deberían hacerlo."
    "Te cuesta medir la fuerza ejercida, pues no tienes mucha sensación en ellas. Es un peso fantasma que se apodera en tus manos, impidiendo la buena manipulación del cuchillo contra la mazorca de maíz."
    "Cuando el cuchillo se estrella contra la tabla de picar por segunda vez, Nulla detiene para mirar el desastre que estás haciendo."
    "Intentas excusarte pero el siseo que se escapa de sus labios te calla."
    
    scene humita2 with dissolve
    
    nulla "Shhh--- no te preocupes, cariño."
    "Sus manos buscan las tuyas, tomándolas con suavidad."
    nulla "No eres tú, es la marioneta el problema."
    nulla "Tus manos están empezando a pudrirse... ¿ves?"
    
    scene act3_n2 with dissolve

    "Gira tus manos, presentándote el fallo, con la delicadeza de no hacer movimientos bruscos que puedan dañarte de alguna forma. Enfocas tu mirada en tus manos, intentando ignorar lo cerca que está Nulla de tu cuerpo." 
    "El color negro que te carcome los dedos ha crecido, siendo el culpable de la perdida de sensibilidad en tus manos."
    "Acaricia cada uno de tus dígitos para probar su punto, y tú apenas lo sientes."
    nulla "¿Cómo serán tus manos en realidad?"
    scene act3_n2a with dissolve
    "Lleva tu mano hacia su cara, mirándolas, ahora él, de cerca."
    "Si bien sus ojos inspeccionan lo que tiene al frente, sabes que no está totalmente centrado en las manos que tiene al frente. Las mira, pero no observa..."
    "Hay algo más en su mente que le impide tomar atención. La pregunta anterior te da una pista obvia de lo que está pasando dentro de él."
    "Sus anhelos nuevamente se van lejos de su realidad."
    nulla "¿Cálidas? o ¿Frías?"
    nulla "¿Suaves?"
    nulla "¿Grandes? ¿Pequeñas?"
    nulla "¿Se sentirán distintas a esto?..."
    "Suspira, frustrado al no encontrar una respuesta clara."
    nulla "Olvídalo, parezco un tonto."
    "Una sutil sonrisa reemplaza su semblante melancólico. Sus ojos se entrecierran para simular una expresión más genuina, pero tú ya puedes ver a través de él."
    nulla "No importa al final de día, nunca las podré sentir."
    menu:
        "Soltar su agarre.":
            $ amor_nulla -= 1
            scene cocinanulla with dissolve

            "Tiras levemente de tu mano para hacerle notar a Nulla que ya quieres romper el contacto."
            "Él opone algo de resistencia, sin dejar de lado su sonrisa, aplica fuerza para evitar que tu mano se aleje. Es una fuerza débil, la cual, si tiras más fuerte, posiblemente podrías romper su agarre."
            "Pasa un segundo, dos... y luego te deja ir."
            "Sin dejar que esa sonrisa flaquee ante tu negativa."
            "A pesar de que el momento es tenso, Nulla finge demencia e ignora lo que acaba de pasar tatareando una canción mientras vuelve a su tarea de desgranar las mazorcas de maíz."


            pass


        "Entrelazar los dedos.":
            $ amor_nulla += 2
            "Es un movimiento lento, sutil, que lo toma desprevenido cuando tus dedos se entrelazan con los suyos. Buscas reconfortarlo de cierta manera y, aunque no son tus manos las que comparten ese contacto con Nulla, estas son una representación de tus deseos."
            "Le cuesta un par de segundos en responder. Al procesar por completo lo que has hecho, su mano se sella alrededor de la tuya, con la misma suavidad aplicada anteriormente."
            
            scene act3_n3 with dissolve
            
            "No satisfecho con solo eso, dirige tu mano a sus labios. Sin romper el contacto con su propia mano, besa tus nudillos."
            "Los besa uno por uno, dándole una atención especial a todos por igual. Hay unos besos que duran más que otros, unos que vienen acompañados por un contacto visual intenso, o una simple risa melodiosa."
            "Cuando termina con el último, coloca un beso en el dorso de tu mano. Similar a una caricia, que busca un contacto que va más allá de lo físico." 
            "Se queda ahí por un buen rato, suspirando mientras cierra los ojos, con miedo a abrirlos y ver lo que tiene al frente."
            "Ver tu ausencia física en el mundo y romper la ilusión de que estás ahí, junto a él."
            
            scene act3_n3a with dissolve
            
            nulla "Deben ser perfectas."
            "Culmina su caricia diciendo esas palabras, dando una conclusión a sus preguntas retóricas."
            "Se le ve satisfecho de cierto modo, mas no contento."
            nulla "Hay que terminar la comida."
            
            scene cocinanulla with dissolve

            "Dice antes de continuar su tarea de desgranar las mazorcas de maíz"
            pass
    

    "Terminan con la preparación, no han tardado mucho gracias a que Nulla ha acelerado el proceso con ayuda de sus manos extras, las cuales se han encargado del procesar el maíz para convertirlo en una pasta."
    "Mientras colocan y envuelven la pasta en las hojas de maíz, te percatas de que a Nulla le está costando envolver y amarrar las hojas."
    "Pareciera como si esta fuera su primera vez haciendo esta receta. Tal cual estuviera siguiendo unas instrucciones que no comprende del todo."
    stop music fadeout 3.0
    show nulla1disgusto with dissolve

    nulla "Parecía más fácil en las memorias..."
    play music "audio/fell.mp3" fadein 2.0 volume 0.4

    "Masculla con mal humor."
    menu:
        "¿No recuerdas como hacerlo?":
            pass
        
        "Ha pasado mucho tiempo... es normal que no te salga a la primera.":
            pass
    
    hide nulla1disgusto
    show nulla1silencio 

    "Nulla te mira en silencio, inseguro de cómo actuar."
    
    hide nulla1silencio
    show nulla1serio

    nulla "Yo no viví esto... solo dependo de los recuerdos de esa vieja versión mía."
    
    hide nulla1serio
    show nulla2silencio2

    "Confiesa aún más avergonzado, como si quisiera que la tierra se lo tragara."
    menu:
        "¿A qué te refieres?":
            pass

        "¿Vieja versión?":
            pass

    "Él toma una bocanada de aire, intentando sacar el valor para confesar algo que posiblemente muy dentro de él, duele."
    
    hide nulla2silencio2
    show nulla1triste

    nulla "No soy más que un usurpador..."
    "Susurra con miedo a decirlo más fuerte." 
    "Su mirada está clavada en la humita que tiene en sus manos y aún falta por cerrar."
    "Extiende su mano en busca del cucharón, con ganas de agregar más relleno al montón que yace en las hojas del maíz, sintiendo que es muy poca la cantidad que tiene."
    
    hide nulla1triste
    show nulla1serio

    nulla "Jamás experimenté nada de las memorias que tengo dentro de mí..."
    nulla "Solo soy la versión más actual que guarda a todas las versiones anteriores a mí... como una muñeca rusa."
    "Viendo que no queda más espacio en las hojas, deja el cucharón de lado."
    
    hide nulla1serio
    show nulla2serio

    nulla "Guardo toda memoria y sentimientos de mis predecesores, soy todos y nadie al mismo tiempo."
    "Junta las hojas del maíz, apretando de más. Sus manos están tensas, buscan liberar aquella tensión en la tarea pero lo único que logra es que parte del relleno se salga por la fuerza aplicada."
    "Tú observas en silencio como el relleno se le escapa entre los dedos."
    "Hay algo en sus pensamientos que no lo deja tranquilo, algo cambia."
    
    hide nulla2serio
    show nulla1preocupado

    nulla "El nuevo juguete del Creador que usará hasta aburrirse y crear otro que me reemplace."
    
    hide nulla1preocupado
    show nulla2normal

    "Y tan rápido como llegó, desaparece."
    "No sabes si es cuando se da cuenta del desastre que ha hecho con la humita o por lo tenso del ambiente, pero Nulla se calma. En sus labios se esboza una sonrisa amarga, que no se decide por completo si quiere ser sarcástica o melancólica."
    
    hide nulla2normal
    show nulla1coqueto

    nulla "¿Qué tan cagado será la próxima versión mía si es que mi plan no funciona?"
    nulla "Ja--- no."
    
    hide nulla1coqueto
    show nulla1disgusto

    nulla "Eso no va a pasar."
    nulla "No voy a dejar que pase---"
    
    hide nulla1disgusto with dissolve

    "Toma lo que queda de la humita para tirarlo al suelo. Antes de que toque el fondo, un agujero se abre, funcionando como un basurero improvisado."
    "Nulla se limpia las manos, dando por terminada la tarea."
    nulla "No voy a quedar como el resto."
    nulla "Voy a ser el último."

    if amor_nulla >= 5:
        "Sus ojos te encuentran, dentro de ellos hay algo que no te esperas. No hay rabia, no hay tristeza..."
        "Hay una pisca de ilusión."
        nulla "Voy a salir de aquí y de su agarre."
        "Su cuerpo te acorrala, quedando en medio del mesón y él. Cuando le buscas la mirada para entender que está ocurriendo, ya no solo hay una pisca de ilusión en sus ojos, ahora hay algo peligroso en ellos."
        "Pupilas dilatadas te observan fijamente. Hay hambre en ella, como si le debieras algo más que solo tú atención."
        nulla "Seré tuyo de una u otra manera."
        "Su cara se acerca a la tuya, peligrando un beso."
        nulla "Haré lo que sea para quedarme contigo."
        "Poco a poco, la distancia se acorta y el aire se hace cada vez más denso e intenso. Su aliento golpea tu piel, y genera un cosquilleo que te deja inquieto."
        "Sus manos buscan tu cintura, pegándose a ella. Está tan cerca que sus piernas tocan las tuyas, lo que no hace más que tu balance peligre con perderse."
        nulla "Ya tengo control parcial de tu computadora, así que----"
        "Su boca roza tu oreja izquierda, haciendo que todos los vellos de tu nuca se ericen."
        nulla "Estoy pensando en un par de formas de cómo hacerlo <3."
        "Soltando una risa pícara, al ver el estado en que estás, se aleja y te deja."
        pass

    else:
        nulla "... no voy a dejar que me gane."
    
    "..."
    scene cocinanulla with dissolve

    "Terminan de armar las humitas entre historias viejas que Nulla cuenta para llenar el silencio. Estando todas listas, las colocan en una olla con agua hirviendo."
    #Poner historias de Neo y Mary
    show gallina with dissolve

    "Dejan cocinando las humitas a fuego medio, un pequeño temporizador de gallina se materializa en el mesón, indicando la cuenta regresiva de treinta y cinco minutos exactos." 
    stop music fadeout 2.0

    "Mientras esperan, Nulla te pide ayuda para preparar la mesa."
    
    hide gallina with dissolve
    play music "audio/misconception.mp3 " fadein 2.0 volume 0.3
    "Ponen tres copas, un juego de utensilios para tres personas y alimento para acompañar el plato fuerte."
    "Sin llegar a ser humilde, la exhibición que se encuentra en la mesa te parece poco. Supones que, para ser una reunión importante, Nulla pondría más esfuerzo en la mesa, al menos un poco más ostentosa."
    "Como las veces en que te hacia el desayuno..."
    "Actualmente pareciera ser una mesa típica para el almuerzo con rutinario con la familia, con lo justo y necesario. Nada muy lujoso o extraordinario."
    "Aún así, la mesa se ve linda, todo tiene un propósito y no hay comida que será desperdiciada."
    "Tal vez esto sea por petición de Sextam... quién sabe."
    "El tiempo pasa volando. Ni cuenta te das de que ya se han cumplido los treinta y cinco minutos cuando el temporizador irrumpe en el ambiente, es un ruido estridente, poco agradable para el oído."
    stop music fadeout 0.3

    play sound "tocarpuerta.mp3"

    "Junto a ello, unos golpes en la puerta que indican que la invita ha llegado."

    play music "audio/calamity.WAV" fadein 2.0 volume 0.4

    show nulla2normal with dissolve
    
    "Nulla solo sonríe cuando levantas la vista, nervioso, buscando alguna forma de tranquilizar tu corazón y lo rápido que este late."
    
    hide nulla2normal
    show nulla1normal
    
    nulla "Ven, vamos a abrir la puerta."
    
    hide nulla1normal
    show nulla3exaltado

    nulla "¡Ah! pero antes---"
    
    hide nulla3exaltado
    show nulla1coqueto

    nulla "Creo que esta ocasión merece una vestimenta adecuada."
    
    hide nulla1coqueto with dissolve
    scene ropafuneral
    "Con un chasquido de sus dedos, la ropa de Nulla se transforma en un traje negro, decorado con pequeños detalles dorados que resaltan en las telas."
    "Se ve guapo... muy guapo e imponente."
    nulla "¿Te gusta?"
    menu:
        "Sí.":
            "Nulla sonríe."
            nulla "A mí igual me gusta."
            nulla "Ya me venía bien un cambio."
            "Sus labios buscan los tuyos, esperando un beso fugaz."
            menu:
                "Besarlo.":
                    "Es un beso sonoro, uno que no pasa más allá del contacto suave entre ambos labios."
                    "Es tierno, casi te hace olvidar la situación en que estás."
                    "Si tan solo esto fuera una cena con algún familiar que conocerás por primera vez..."
                    "Una cena para conocer a los allegados de Nulla."
                    "Uhg."

                "Correr la cara.":
                    nulla "Aww :(."
                    nulla "Será en otra ocasión."

        
        "No...":
            "Las comisuras de sus labios caen."
            nulla "A mí si me gusta..."
            nulla "No tengo tiempo para buscar otro conjunto..."

    "Son interrumpidos por los golpes de la puerta, demandando a que esta se abra."

    menu:
        "Acompañarlo.":
            scene comedornulla with dissolve

            "Decides acompañarlo, prefieres eso a tener que quedarte solo, esperando sin saber qué pasa con Nulla y Sextam..."
            "Podrían tomarte desprevenido e indefenso estando sin la compañía del dueño del vacío, por lo que es mejor quedarte a su lado en todo momento."
            "Además, no aguantarías la ansiedad de no saber que está pasando."
            
            scene entradanulla with dissolve

            "Así que tomas su mano y le acompañas a abrir la puerta."
            "La mano de Nulla te sirve como ancla, te sostiene, dando un apoyo emocional que brinda seguridad. El apretón tierno que te da una vez levanta su mano para abrir la puerta, te calma."
            
            stop music fadeout 0.3

            nulla "Ya te estábamos esperando, bienvenida Sextam."
            
            play music "audio/woo_scary.WAV" fadein 2.0 volume 0.3

            "Dice él abriendo la puerta. Por el umbral, puedes ver una alta y maciza figura que resplandece, aunque el vacío de afuera intente comerse su luz."
            
            show sextam_cerca_callado at left
            with dissolve

            "Sextam es simplemente hermosa."
            "Tiene en su cabello flores repartidas en cada onda que cae por su cuerpo, simulando un manto que la protege."
            "En sus manos lleva una bandeja que no permite ver lo que hay en su interior ya que yace tapada."

            hide sextam_cerca_callado
            show sextam_cerca_normal at left

            sextam "Es un gusto poder venir aquí."
            sextam "Pensé que jamás vería este lugar."

            hide sextam_cerca_normal
            show sextam_cerca_callado at left

            "Sus ojos se topan con los tuyos, y no los suelta. Ni siquiera pestañea."
            "Tragas saliva, sintiendo como los nervios te empiezan a comer vivo."
            
            hide sextam_cerca_callado with dissolve

            nulla "Pasa, la comida ya está lista."
            "Nulla te saca del trance, apretando nuevamente tu mano."
            
            scene comedornulla with dissolve
            "Es él quien los conduce a la mesa. Mientras te ofrece la silla para que te sientes, una de sus sombras hace lo mismo para Sextam." 

        "Dejarlo ir solo.":
            scene cocinanulla with dissolve
            "Le dices que no quieres ir, que prefieres esperarlos ya sentado en la mesa. Nulla hace una mueca, desconforme, pero no insiste."
            "Se va, dejándote solo en el comedor."
            "..."
            "Tú solo esperas..."
            "Y esperas."
            "    .      .     .  "
            "Condenado sea Nulla por no tener ningún reloj funcionando en la sala, y con el pollo no puedes contar pues ha sido comido por el vacío como medida para hacer que se callara."
            "Cuentas los segundos golpeando suavemente tu dedo índice contra la mesa, mientras tu estómago se contraer intentando aguantar los nervios."
            nulla "Bienvenida, [nombrejugador] nos está esperando en la mesa."
            "Escuchas como Nulla saluda a Sextam, y eso te basta para sentir las náuseas formarse en tu garganta y lengua."
            stop music fadeout 2.0
            "Tu respiración se acelera pensando en todo lo que podría salir mal ahora. ¡Y no puedes entender por qué mierda Nulla está tan tranquilo! Actúa como si se tratase de un almuerzo con una vieja amiga---"
            show sextam_cerca_callado at left
            show nulla_cerca_normal at right
            with dissolve

            play music "audio/woo_scary.WAV" fadein 2.0 volume 0.3

            "Los ves pasar hacia el comedor, Nulla ofreciendo su brazo para que Sextam camine a su lado. Ella tiene una expresión neutral, la cual no cambia cuando posa sus ojos en ti."
            "Si bien, te sientes incómodo por lo intensidad de su mirada sobre ti, no puedes evitar no mirarla."
            "Sextam es hermosa, su cabello ondea con cada paso que ambos dan... parece un manto divino que recubre su cuerpo y lo protege de toda impureza a su alrededor. En cada onda hay una flor que decora su cabellera con un patrón finamente calculado."
            "Lleva un vestido blanco, que recubre gran parte de su cuerpo, resguardando su figura."
            "En su mano libre, lleva una bandeja de plata cubierta..."
            hide sextam_cerca_callado 
            hide nulla_cerca_normal 
            with dissolve

            "No puedes ver lo que hay en su interior."
    
    scene act3_n4 with dissolve
    pause 2.0
    scene act3_n4a
    
    "..."
    "Tú ocupas la cabecera de la mesa, el puesto te deja al descubierto, muy expuesto para tu gusto."
    "Al otro lado de la mesa se encuentra Sextam, aún sin despegar su mirada de ti. Nulla en cambio, está sentado en medio, haciendo de barrera entre tú y ella."
    "Sextam espera, no comenta nada ni intenta sacar a flote una conversación para romper el hielo. Hay un silencio opresivo, del que Nulla tampoco muestra interés en romper, pues parece muy ocupado en observar cómo sus sombras sirven la comida."
    "Estas hacen su trabajo con diligencia, sirviendo según lo que cada uno pida... Sextam pide vino al igual que Nulla."
    "Al terminar, las sombras desaparecen con el chasquido de Nulla. Aquello parece despertar a Sextam, quien agradece por la comida, pero no toca nada que no sea la copa de vino."
    "La copa gira en su mano, moviendo levemente el líquido carmesí del interior. Lo hace por un buen rato, sin signos de querer beber el contenido, mientras sus ojos oscilan entre la bandeja que ha traído y tú."
    "Sin saber que hacer o decir, miras a un lado en busca de Nulla. Él ya ha tomado los utensilios con el fin de consumir lo que está en el plato. Justo lo atrapas en su primer bocado, y por su reacción, sabes que le ha gustado el sabor de la humita."
    nulla "Hmmm~"
    nulla "Está delicioso."
    nulla "Deberías probarlo."
    "Le dice a Sextam."
    sextam "No tengo hambre."
    scene negro 
    show nullacena_enojo 
    with pixellate

    nulla "Bueno, entonces deberías dejar de mirar a [nombrejugador] de esa manera."
    "Su rostro no cambia, sigue sonriendo, pero algo en su tono te hace apretar los dientes. La molestia que siente ante el accionar de Sextam se diluye en sus palabras de forma discreta, pero está ahí."
    nulla "No me gusta. Lo pones nervioso."
    "Sextam hace una pausa con su copa, parando en seco. El líquido en el interior de la copa es lo único que se mueve en su posición."
    show sextamcena_enojo
    sextam "Y a mí no me gusta que hagas de su vocero."
    sextam "Suficiente ya tuviste con ser el vocero de Septem."
    "Dice ella, con voz dura, sin perder la paciencia."
    hide nullacena_enojo
    show nullacena_sorpresa
    nulla "¿Aún te acuerdas de eso?"
    sextam "..."

    hide nullacena_sorpresa
    show nullacena_risa

    nulla "Hablando de él, ¿Cómo está?"
    "Nulla deja de lado su comida, optando por poner sus codos sobre la mesa para poder juntar ambas manos y recostar su mandíbula en ellas. Sonríe, antelándose a la respuesta, sabiendo que lo que quiera que escuche lo complacerá."
    
    hide sextamcena_enojo
    show sextamcena_risa

    "Ella en respuesta, suelta una risa seca."
    sextam "No vine aquí para servir de burla a nadie."
    sextam "Menos dejar que te burles de él."
    sextam "Vengo a hablar de nuestras opciones."
    nulla "¿Quieres hablarlo ahora?"
    sextam "No veo la necesidad de perder el tiempo en una comida de la cual nadie está interesado."
    
    scene act3_n4a with pixellate

    "Para dar más fuerza a su argumento, sus ojos color ámbar se posan en ti y en tu plato sin tocar. Nulla suspira, aceptando en silencio que ella tiene razón."
    "Sientes que la mirada de Sextam te consume el alma, dejándote solo con un hueco en el pecho que solo se llena de tristeza." 
    "No te mira con odio. No te mira con rabia, ni disgusto, ni temor. En sus ojos solo hay pena."
    sextam "Me sorprende lo bien que te ha resultado."
    sextam "Atrapar a uno de los de arriba."
    sextam "Por fin lo lograste..."
    nulla "Así es."
    "Ambos se miran a los ojos, ignorando tu existencia a pesar de están hablando de ti. Sientes que detrás de esta interacción se enconde un conflicto, del cual no estás enterado."
    scene negro 
    show sextamcena_flor
    with pixellate

    "Sextam levanta su mano hacia sus cabellos, buscando una de las flores con el fin de extraerla de sus rizos rosas. La mira, tomándose su tiempo para apreciarla. Juega con sus pétalos y traza cada una de las hojas que los sostienen."
    "Parte de la flor está presentable, bonita a simple vista. Pero si enfocas mejor tus ojos en los detalles, puedes distinguir como las esquinas de los pétalos han comenzado a marchitarse."
    sextam "Pasé la noche con Tria. Ella me las dio está mañana."
    sextam "Me dijo que sin Unum no durarían mucho..."
    
    show nullacena_sorpresa with dissolve

    nulla "No pensé que siguiera haciendo flores."
    
    hide sextamcena_flor
    show sextamcena_enojo

    "El comentario hace que Sextam le mire, frunciendo el ceño."
    sextam "Hoy ha hecho una excepción."
    sextam "Quería que llevara algo suyo en mi cuerpo."
    hide nullacena_sorpresa
    show nullacena_sonrisa
    "Nulla esboza una pequeña sonrisa que calma un poco a Sextam."
    nulla "Es un lindo gesto."
    "Suelta con sinceridad, sin ánimos de ofender a la mujer."
    sextam "Lo es."
    sextam "..."
    hide sextamcena_enojo
    show sextamcena_triste

    "Ella suspira, ya sin ganas de extender la conversación. Posa la flor en la mesa, a un lado del plato, y se dispone a continuar."
    sextam "Mira Nulla--- Vine aquí a hablar y ver la posibilidad de detener el daño que estás haciendo."
    hide nullacena_sonrisa
    show nullacena_serio

    nulla "Sextam esto ya lo hablamos años atrás, tú misma piensas que---"
    sextam "Sé bien lo que pienso."
    sextam "No lo hago por mí. Lo hago por los demás."
    "Aquel comentario hace que Nulla cierre la boca, dejando el espacio para que Sextam hable. A ella le toma unos segundos sacar las palabras de su boca, complicada en como traer a la vida todos sus pensamientos."
    "Cuando por fin los tiene, opta por correr la mirada y cerrar sus ojos."
    sextam "Si hubieras visto la reacción de los que fueron borrados..."
    sextam "Tria apenas podía levantarse cuando salió del espacio que antes era el dominio de Quinque."
    "Hace una pausa, clavando sus ojos cristalinos que aguantan un llanto en la figura de Nulla."
    hide sextamcena_triste
    show sextamcena_enojo

    sextam "Te odio."
    sextam "Cuando hablaste de esto, me dijiste que sería rápido."
    nulla "Es rápido. Nadie sufre."
    sextam "Los que quedan de último si lo hacen."
    "Él se acomoda en su asiento, harto de las palabras que salen de Sextam. Cruza ambos brazos y corre la cara, cerrado a seguir escuchándola."
    hide nullacena_serio
    show nullacena_enojo
    nulla "Sextam si intentas hacerme sentir mal, ni te esfuerces..."
    nulla "Tú misma me comentaste que sería mejor acabar con todo."
    hide sextamcena_enojo
    show sextamcena_triste
    sextam "Jamás quise que fuera así."
    hide nullacena_enojo
    show nullacena_silencio
    sextam "..."
    nulla "..."
    sextam "Septem dice que con la ayuda de [nombrejugador] puede borrarte la memoria."
    "Nulla solo la mira, esperando a que se explique. Pero en su mirada hay algo vacío, que se apaga al instante. Ya en su cara no hay expresión alguna, no hay enojo o disgusto."
    sextam "Si es que saber la verdad de este mundo es lo que te hace mal, borrarte la memoria puede ser la solución."
    sextam "Así evitamos eliminar vidas que no han pedido ser eliminadas..."
    "Nulla te mira de reojo por un instante antes de mirar sus manos, pareciera que está considerando la propuesta. Golpea la mesa con dos de sus dedos, lento y preciso."
    "Pasa el tiempo y tú sientes que se te va el aire... lo único que quieres es que esta conversación termine para poder respirar tranquilo."
    
    hide nullacena_silencio
    show nullacena_enojo
    
    nulla "Eso suena muy fácil, muy sensato."
    "Escupe casi indignado, matizando su tono con una solitaria risa sarcástica. Todo para hace notar su desacuerdo con lo que dicen sus palabras." 
    
    hide sextamcena_triste
    show sextamcena_silencio

    "Ella guarda silencio, esperando a que Nulla le dé más que simplemente aquello. Luego vienen las risas, forzadas, cortas y ásperas que llenan todo el lugar con un débil eco."
    
    hide nullacena_enojo
    show nullacena_risa

    nulla "¿Hasta dónde piensa borrar?"
    nulla "¿Resetear de fábrica?"
    nulla "¿Borrar todas las memorias hasta el punto de olvidar quién soy?"
    
    hide nullacena_risa
    show nullacena_sonrisa
    
    "Toma aire, dedicando una sonrisa ladeada a ella, quien no sabe cómo reaccionar a tal respuesta."
    
    hide nullacena_sonrisa
    show nullacena_risa

    nulla "Sextam, tú más que nadie sabe lo importante que son las vivencias de un ser vivo para moldear la identidad."
    
    hide nullacena_risa
    show nullacena_enojo

    nulla "No me vengas con esa mierda de borrar la memoria y final feliz para todos."
    "Su voz sube, sin llegar a convertirse en gritos. Hay rabia en cómo se expresa, cada frase que sale de él se transforma en una daga que va dirigida hacia Sextam."
    nulla "¿Y hasta cuándo piensan seguir con toda esta mentira?"
    nulla "¿Van a mentir hasta que se acaben los recursos humanos? ¿y después qué?"
    
    hide nullacena_enojo
    show nullacena_risa

    nulla "Esperar a que todos comiencen a sufrir de hambre, ¿agonizar hasta que solo queden los Estandartes en pie?"
    nulla "Van a terminar todos locos."
    nulla "Y lo sabes."
    "Sextam le mira, ya agotada se encoje de hombros."
    
    hide sextamcena_silencio
    show sextamcena_triste
    
    sextam "Con la ayuda de [nombrejugador] podemos evitar eso."
    
    hide sextamcena_triste
    show sextamcena_silencio
    hide nullacena_risa
    show nullacena_enojo
    
    nulla "No, no, no. Sabes muy bien que no dependemos de [nombrejugador]."
    nulla "Ustedes dependen de un ser egocéntrico, no de [nombrejugador]. Dependen de Ella y de Padr--- de su estúpida marioneta."
    nulla "[nombrejugador] solo está aquí de visita."
    nulla "Y créeme que Ella no los va a soltar."
    nulla "O se aburre de ustedes o no los va a soltar."
    nulla "Ambos son malos desenlaces."
    nulla "Sextam, por favor-"
    
    hide sextamcena_silencio
    show sextamcena_enojo

    sextam "Basta."
    sextam "Pelear contigo es lo que menos quiero ahora."
    sextam "No vamos a llegar a un acuerdo."
    sextam "Ya he hecho lo que Septem me ha pedido---"
    sextam "No voy a gastar más tiempo haciendo esto."
    
    scene esenciatria1 with pixellate
    pause 1.0
    scene esenciatria2
    "Sextam extiende su mano a la bandeja de plata, toma la tapa y la levanta, revelando lo que hay dentro."
    "Es una esfera color esmeralda, similar a la textura y tamaño de las esencias que has comido anteriormente..."
    "No tardas en comprender qué y a quién le pertenece."
    "Es Tria."
    scene negro with pixellate
    show sextamcena_triste
    sextam "No quiero que sufra más."

    hide sextamcena_triste
    show sextamcena_enojo

    sextam "Ni que hagas un espectáculo como lo hiciste con Quinque con su muerte."

    hide sextamcena_enojo
    show sextamcena_triste

    sextam "Quiero que se vaya en paz."

    show nullacena_sorpresa
    "La única reacción que sale del pelinegro es lo mucho que se abren sus ojos. Se le ve perplejo, sin saber cómo contestar más allá de un suspiro o vocal rota."
    nulla "Oh---"

    
    hide sextamcena_triste
    show sextamcena_enojo
    hide nullacena_sorpresa
    show nullacena_enojo
    
    "Sus manos se lanzan a tomar la bandeja. Sextam la corre lejos de su alcance antes de que Nulla la alcance, lo que se gana un chasqueo de lengua por parte de Nulla."
    sextam "Esto no es para ti."
    sextam "Es para [nombrejugador]."
    "Nuevamente tus ojos y los de ella se encuentran. Te mira decidida, preparada para las consecuencias de lo que está ofreciendo. Entregando todo lo que le queda a Septem sin reparo..."
    "¿Se han rendido? ¿Es así de fácil?"
    "...¿En serio nos van a dar ambas esencias así sin más?"
    menu:
        "Decirle a Nulla que no es buena idea.":
            pass
        
        "Tomarla con cuidado.":
            pass

    scene negro 
    show sextamcena_enojo 
    with pixellate

    sextam "Solo les pido una cosa..."
    "Sextam te interrumpe antes de que puedas decir o hacer algo."
    sextam "Quiero ver cómo se la come."

    menu:
        "{sc=2}Decirle a Nulla que no es buena idea.{sc=2}":
            pass
        
        "Aceptar.":
            pass
    
    show nullacena_sorpresa

    nulla "¿Y eso?"
    "Esta vez Nulla te interrumpe, arqueando una ceja."    
    hide sextamcena_enojo
    show sextamcena_triste
    sextam "No me gustaría dejar a Tria sola en este momento..."
    nulla "Mmm..."

    menu:
        "{sc=2}Decirle a Nulla que NO ES una buena idea.{sc=2}":
            
            scene esenciatria2 with pixellate

            "Se lo dices fuerte y claro, llevando ambas miradas hacia ti. Nulla te mira divertido, como si aguantara una risa. Mientras que Sextam te mira seria y en silencio."
            nulla "Discúlpalo, está algo estresado."
            "Sonríe, molesto por dentro de que le estés llevando la contraria frente a Sextam."
            "{glitch=20.0}{color=ffffff}{b}Cariño, ya están en la ruina.{/glitch}{b}"
            "{glitch=20.0}{color=ffffff}{b}Sextam no miente y la esencia de Tria está aquí.{/glitch}{b}"
            "{glitch=20.0}{color=ffffff}{b}No hay nada de que temer.{/glitch}{b}"
            "Quieres decirle que esto es muy fácil, que debe haber algo extraño, pero tus labios no responden... con pena confirmas que él te ha incapacitado de usar tu boca."
            "Sabes que a Nulla ya se le han subido los humos a la cabeza, que ya prácticamente sueña con completar su misión. Ya en su mente ha ganado, pero--"
            "Hay algo que no calza. No te tragas la excusa de que se han rendido."
            "{glitch=20.0}{color=ffffff}{b}Vida mía, si pasa algo. Yo me encargaré de arreglarlo.{/glitch}{b}"
            "{glitch=20.0}{color=ffffff}{b}No hay nada que ya no pueda hacer.{/glitch}{b}"
            "{glitch=20.0}{color=ffffff}{b}Confía en mí...{/glitch}{b}"
            "{glitch=20.0}{color=ffffff}{b}Sé que no te gusta hacer esto, así que lo haré por ti.{/glitch}{b}"
            "Te das cuenta a lo que se refiere demasiado tarde. Ambas manos buscan la esencia que te ofrece Nulla, con ayuda de una de sus sombras."
            "Te mueve como a una muñeca, y a pesar de la resistencia que haces, es imposible volver a tomar el control de tu cuerpo."
            
        
        "Tomar la esencia.":
            scene esenciatria2 with pixellate

            pass
    
    "La tomas con las manos desnudas. En tus manos se mueve como si palpitara, llena de vida aún. Inspeccionas un poco su configuración, encontrando que dentro de la capa exterior hay pequeñas chispas de luz que titilan organizadas por un orden que desconoces."
    "Si este fuera otro contexto, estarías feliz de apreciar lo bello de este órgano."
    scene negro
    show nullacena_sonrisa
    with pixellate
    "Subes la cabeza antes de darle el bocado que le otorgará el final a este Estandarte. Nulla te observa confiado, sin borrar esa sonrisa triunfante que venía escapándose desde el momento en que Sextam se ha sentado en la mesa."
    show sextamcena_enojo with dissolve
    "Ella, en cambio, yace como piedra. Sin un solo parpadeo o mueca, te observa desde la otra cabecera."
    hide sextamcena_enojo
    hide nullacena_sonrisa
    with dissolve

    scene negro with dissolve

    "Sin otra salida, y mientras cierras los ojos, tragas la esencia."
    "No sientes nada."
    "No hay dolor ajeno o tuyo que se cultive en tu estómago. Es como beber agua."
    
    centered "{sc=5}{size=*2.0}[nombrejugador].{/size}{/sc}"

    "Tu nombre es pronunciado, el llamado te eriza los cabellos de la nuca y obliga a mirar que pasa en tu alrededor."
    
    scene act3_n5 with dissolve

    play sound "void2.mp3" fadeout 1.0

    "Es Sextam, se ha subido a la mesa, sin importarle la comida repartida en esta. Sus pies derraman liquido y botan platos al suelo."
    nulla "Detente, no te puedes acercar."
    nulla "Esto no es parte del acuerdo."
    sextam "Solo le voy a entregar mi esencia."
    "Te mira desde arriba, tapando todo lo que te rodea. Dejándote totalmente a su merced. Apenas puedes distinguir sus rasgos faciales, su cabello te impide hacerlo. Solo tienes acceso a sus ojos, cuyo brillo te atrapa, helando tu sangre."
    "Las flores que Tria le ha dado siguen decorando su cabellera."
    sextam "Nulla---"
    "En movimientos lentos, las flores se desprenden de sus cabellos. Algunas caen en tu plato, otras a tu alrededor."
    sextam "Tria es rencorosa."

    scene act3_n5 with vpunch

    play music "audio/fronbondi1.mp3" fadein 2.0 volume 0.2

    "Escuchas movimiento, una silla caer y la respiración de Nulla entrecortarse."
    sextam "Recuerda que yo me iré por mis propias manos, no me puedes atacar, ni yo a ti..."
    nulla "Eres una---"
    "Una de las flores cae en tu antebrazo, provocando que esta se marchite, desintegrándose hasta solo ser polvo. El resto de las flores le siguen en una reacción en cadena."
    "Es en ese momento en que dentro de ti, tu estómago se aprieta. Sientes como pequeñas agujas se clavan en el, impidiendo que puedas correr o moverte."
    "Un dolor intenso se origina dentro de ti, uno que no te suelta, te retuerce y estruja. Se esparce por todo tu cuerpo, desde la boca del estómago hasta la faringe, en una sanción de náuseas y agonía."
    "Tu cuerpo pide a gritos expulsar lo que te has comido. Quieres vomitar, pero no puedes."
    sextam "Creo que tendrán que ver a Septem antes de tiempo..."
    sextam "Se me ha olvidado santificar el postre."
    "Miras con horror como sus manos apuntan a su pecho, buscando el punto perfecto para clavar sus uñas en la piel y romper esa cáscara que es llamado cuerpo. De la herida emana un líquido rojo, que se asimila a la sangre por lo viscoso que es."
    
    scene act3_n5a with vpunch

    "Una de sus manos rompe la carne y huesos que protegen la esencia, mientras que la otra hurga la cavidad con dureza, desesperada por sacarla lo antes posible."
    "En cuestión de segundos, la esencia es extraída sin cuidado, con asco y desprecio. Parte del líquido que la recubre cae en tu cara."
    sextam "No te molestes en borrar nuestros dominios tan rápido. La marioneta ya está envenenada y no hay nadie que la pueda curar---"
    "Sus palabras se pierden en la sangre que sale de su boca, se ahoga con ella. A pesar de esto, ella se agacha y ofrece la esencia, presentándola ante ti."
    "Con ambas manos, la lleva a tu boca, y la empuja contra tus labios, obligando a darle paso entre tus dientes y lengua."
    
    scene comedornulla 
    show nada1
    with dissolve
    "Una vez dentro de tu cuerpo, la figura de Sextam se esfuma como espuma. Desaparece de tu campo de visión, librándote de su presencia."
    nulla "¡[nombrejugador]!"
    "Nulla se levanta del suelo y corre hacia ti para verificar tu estado. Toma tu cara, apretando más de la cuenta, desesperado por saber qué pasa."
    nulla "¡Puta mierda!"
    "Nulla se aferra a ti, te abre la camisa, arrancando varios de los botones en el proceso. Sus ojos caen en tu estómago, apretando la mandíbula cuando ve algo que no logras percibir a simple vista."
    nulla "¡Mierda!"
    "Sientes que estás por caer inconsciente. La vista se te nubla, y las náuseas no te permiten respirar como es debido. A penas puedes mover tus piernas, siendo imposible levantarte de la silla." 
    "Antes de que caigas inconsciente Nulla abre un portal para atraparte en el vacío."
    stop music fadeout 1.0
    play sound "tv-static.mp3" volume 0.7 fadein 5.0

    nulla "No te preocupes, aguanta un poco."
    hide nada1
    show consumo
    with dissolve

    #cambio de escena
    "..........."
    "................"
    
    play music "audio/void.mp3 " fadein 2.0 volume 0.5

    "Escuchas una risa femenina, ya la has escuchado antes, se te hace conocida. Su efecto te recuerda a una canción de cuna, una que te acompañó en los primeros momentos de vida."
    "Es sedosa, suave. Es similar a una caricia que te invita a seguirla, para tener más de ella. Te mece en tu dolor, calmando un poco esa herida interna que te dificulta la respiración."
    madre "Esta cosa está por morir."
    "Ella suelta aire, sin llegar a ser una risa o un suspiro."
    madre "No hay nada que hacer, Nulla."
    "No puedes moverte, hablar, ni mirar. Estás atrapado, flotando en el vacío, asfixiándote en tu propio dolor."
    nulla "No, no, no, no me puedes hacer esto ahora."
    nulla "¿Cómo se supone que mate a Septem sin ella?"
    nulla "Yo solo no puedo herirlo y [nombrejugador] necesita un cuerpo."
    madre "..."
    nulla "¡Grimal!"
    "Hay una pausa, durante la cual lo único que se oye es el movimiento de ropas siendo arrastradas por el suelo."
    madre "Ya no hay nada que me ligue a este lugar. Esto no es más que espacio muerto en un mar de ideas."
    "Luego, una mano ejerce presión en tu pecho, aliviando la punzada que tienes en el estómago."
    madre "Lo único que me detiene es esta cosa---"
    nulla "Yo cumplí con mi parte del trato."
    nulla "No me vas a dejar sin nada para completar lo que yo quiero."
    nulla "Dame una solución para este cuerpo defectuoso, es tu culpa no haberlo diseñado para este inconveniente."
    madre "Tan insignificante, y aun así demandando más... eres igual a él, usurpador."
    madre "...uhg."
    madre "Esa cara que estás haciendo---"
    madre "Agradece que te pareces a él. Sin esa cara no habrías conseguido nada de mí."
    madre "..."
    madre "Voy a ver que puedo hacer."

    
    play music "audio/fronbondi2.mp3" fadeout 1.5 fadein 4.0 volume 0.3

    "Un calor se acumula en  la zona de tu vientre, haciéndose cada vez más intenso con el pasar de los segundos. El calor pasa a convertirse en dolor al sentir cómo dos objetos extraños te perforan el ombligo."
    "Te abren la piel sin piedad, haciendo los cortes necesarios para poder acceder al interior." 
    "Quieres gritar, pero ninguna parte de lo que llamas cuerpo responde. Ni siquiera sabes si estás respirando aún o si tus ojos funcionan."
    "El dolor es todo lo que eres actualmente, sientes es como abren y escarban en tu abdomen sacando vísceras tras vísceras sin cuidado alguno. La sangre inunda tus sentidos; su olor, tus fosas nasales--- y su sabor en tu lengua." 
    "No hay mucha diferencia entre tu cuerpo y un trozo de carne siendo mutilada."
    nulla "Le duele."
    madre "Te recuerdo que esto es solo una marioneta."
    "Algo se enrosca en tus órganos, tirando de ellos. Los corta y expulsa fuera tuyo. Su ausencia es desesperante, al igual que el sangrado."
    "Te vas a desmayar en cualquier momento."
    nulla "Pero---"
    madre "[nombrejugador] no está sintiendo nada de esto ahora mismo."
    madre "Déjame trabajar."
    "Tu tortura se extiende por lo que parecieran ser horas. Siendo ultrajado hasta el punto en que han destrozado todo órgano interior cuya función esté vinculada con el sistema digestivo."
    "Su ausencia se hace notar... hay un espacio extraño dentro de ti que no se siente habitado, un vacío que duele y sangra."
    "Algo golpea tu pecho, dándose el gusto de utilizar toda su fuerza en el impacto, sin importarle mucho cuanto has sufrido ya. El golpe te despierta, reincorporando una posición más cómoda para vomitar lo que yace atrapado en tu garganta."
    "Lo expulsas entre saliva y bilis, siéndote repulsivo sentir como aquello pasa por tu garganta y boca."
    
    scene act3_n6 with dissolve


    "Cuando ya no hay nada más que sacar, abres los ojos. Nulla te mira preocupado, mientras que Madre lo hace con indiferencia."
    madre "Ahí está."
    madre "Usa bien el tiempo. No le quedan más de dos días."
    madre "Lo justo para tu plan."
    nulla "Gracias."
    madre "Hmm..."
    nulla "..."
    nulla "¿Qué piensas hacer ahora?"
    "Ella le dedica una mirada fulminante desde su lugar. Le mira cómo si lo que ha preguntado fuera lo más estúpido y obvio del mundo, casi que reprochando la mera existencia de la pregunta."
    "No se mueve ni parpadea. Aquello hace que Nulla se acerque un poco más a ti, temiendo una respuesta violenta por su parte."
    madre "Septem sigue con vida aún... no lo voy a dejar solo."
    madre "Pero cuando todo haya terminado, me iré lejos de este lugar."
    "Dice mirando a un punto fijo del cielo infinito del vacío."
    madre "Allá, a la esfera más lejana..."
    
    scene void2 with dissolve

    "Sigues la trayectoria donde sus ojos se enfocan, quieres ver que es lo que contempla con tanta esperanza. Aunque solo te topas con oscuridad entre más oscuridad. Nada interesante que ver. Tal vez ella, siendo una diosa, puede ver más allá que un ojo mortal podría soñar."
    "Pasa un tiempo observando, hasta descubrir sus dientes en una mueca de disgusto, como si lo que ha visto le causara repugnancia."
    
    scene act3_n6 with dissolve

    madre "El maldito de Ciro ha aprovechado mi ausencia--- uhg!"
    madre "Mi mundo original sigue allí... Debo poner orden en su sistema."
    "Desvía la mirada, irritada."
    nulla "Eso es nuevo."
    madre "A diferencia tuya, soy libre--- y no pienso morir aquí."
    madre "..."
    "Ella parpadea un par de veces antes de clavar su mirada en ti."
    madre "Te voy a cobrar el arreglo a tu marioneta."
    nulla "¿Qué quieres?"
    madre "Una capa interior tuya."
    madre "No quiero que te lleves todo lo que fue él con tu muerte. Lo quiero de vuelta junto a mí."
    nulla "..."
    nulla "No me voy a arriesgar a---"
    "Madre chasquea la lengua."
    madre "No es una de las importantes... es una previa a mi intervención."
    "Mira sus manos, hay algo de culpa en su mirada."
    madre "Cuando él no era más que una idea, un crío." 
    madre "No cometeré el mismo error."
    nulla "Grimal..."
    madre "De nada te sirven esas, las vas a borrar de todos modos."
    "Se hace un silencio largo, del cual le permite a Nulla meditar su próxima respuesta. Viendo que Nulla solo le regresa la mirada, ella insiste."
    madre "Con la potestad que tengo ante tus primeras capas, romperé la conexión con la raiz. Ese nombre dejará de ser parte de ti."
    madre "Ya eres un individuo aparte, solo falta que sea anunciado."
    nulla "...Eres insufrible."
    "Nulla se acerca a ella, ofreciendo su pecho."
    nulla "Sácala y vete."
    madre "Será un placer."
    "Madre tiene que encorbar su figura para estar a la par de Nulla, sus labios se posan tiernamente en la oreja del pelinegro."
    "Palabras que no tienen un significado son susurradas a su oído, y aún así, tú eres capaz de escuchar todo. Cada palabra rebota por el espacio que ahora ocupas, se instalan en tu cabeza sin que puedas descifrar lo que quieren decir."

    scene noneo 
    show liberari 
    with vpunch

    play sound "huesoroto.mp3"

    "!!!"
    "Madre clava sus garras en el pecho de Nulla. Su mano se abre paso entre un líquido viscoso que parece reaccionar con la intrusión. Expandiéndose alrededor de ella, abriendo capa tras capa, permitiendo la extracción."
    "Una sustancia pequeña y roja es extraída de Nulla, brillando de forma sutil en su mano."
    "..."
    scene madre with dissolve

    "Ella la mira con una mezcla de fascinación y amor, como quien miraría a un hijo. Le sonríe y acerca a su cara, para poder apreciarlo con más atención."
    scene madre2 
    "Luego, gira su cara a Nulla. Y por primera vez, Madre le dedica una mirada que no sabes cómo describir más que gratitud."
    madre "Gracias..."
    madre "Es momento de retirarme..."
    madre "Estaré cerca, mirando. Pero no me involucraré más contigo."
    madre "Siempre has sido un mal augurio."
    "Madre se despide de ambos, bajando la cabeza un poco antes de desaparecer."
    
    scene negro with dissolve

    "Quedan solos. Nulla comienza a guardar las capas abiertas de su cuerpo, ocultando con su espalda el proceso, temiendo tu reacción."
    "Termina y da media vuelta, volviendo junto a ti. Se agacha para ofrecerte la mano, te cuesta hacer que tus piernas respondan con normalidad y necesitas que Nulla te levante tirando un poco del agarre."
    "Te sientes inútil."

    menu:
        "¿Qué fue eso?":
            show nulla_cerca_callado with dissolve

            nulla "El fin de un trato viejo."
            nulla "Al destruir a todos los Estandartes, hemos destruido el Jardín y toda ley impuesta en él."
            nulla "Sin el Jardín yo y Grimal ya nos estamos atrapados."
            nulla "Ahora puedo borrar a Septem."
            
            hide nulla_cerca_callado
            show nulla_cerca_normal

            "Nulla comienza a reír, intenta ocultar su acción tapando su boca, pero le es difícil quedarse callado."
            nulla "Primero su cuerpo y después su divinidad."
            nulla "Luego seré libre."
            nulla "Ah~~~ queda tan poco~."
            nulla "Ahhh---"
            "Exhala complacido, calmando la risa gradualmente hasta volver a la normalidad."
            
            hide nulla_cerca_normal
            show nulla_cerca2_enojo

            "..."

            pass

        "...":
            show nulla_cerca2_enojo with dissolve
            "..."
            pass

    "Su mirada cae a tu vientre, tú haces lo mismo. Si bien, no te duele nada, hay una sensación de carencia en la parte que debería ser tu estómago, similar al hambre."
    "Es como si un hueco reemplazara ese espacio."

    nulla "¿Cómo te encuentras?"

    menu:

        "No me siento muy bien.":
            pass
        

        "No me siento tan mal.":
            "..."
            pass
    
    "Él solo suspira y pide perdón."
    nulla "Subestimé a Tria."
    nulla "No me esperaba que se entregara así..."
    nulla "Ahora por su culpa te falta la mitad de tus órganos..."

    menu:
        "¿Cómo sigo vivo entonces?":
            pass
    
    hide nulla_cerca2_enojo
    show nulla_cerca2_normal

    nulla "Yo te estoy manteniendo con vida."
    nulla "Ahora soy tu sistema digestivo~"
    nulla "Cada día más unidos, ¿no crees?"

    menu:
        "Eres asqueroso...":
            hide nulla_cerca2_normal
            show nulla_cerca2_enojo

            nulla "..."
            nulla "Veo que no estamos para chistes."
            nulla "Disculpa."
            nulla "No era mi intención asquearte."
        
        "Aww~ Que lindo---":
            $ amor_nulla += 1
            hide nulla_cerca2_normal
            show nulla_cerca_normal
            
            nulla "Lo sé, lo sé."
            nulla "Soy un romántico."
        
        "Mejor seamos uno solo <3.":
            $ amor_nulla += 2
            hide nulla_cerca2_normal
            show nulla_cerca2_enojo
            nulla "?!"
            
            hide nulla_cerca2_enojo
            show nulla_cerca_normal

            "Nulla se sonroja, subiéndosele el rubor hasta las orejas de tan solo escuchar en tu respuesta, no esperando tu elección."
            nulla "Wo, wo, wo. ¿No crees que vamos un poco rápido?"
            nulla "¿No llevamos juntos ni una semana y ya quieres pasar a eso?"
            nulla "Eres un---"
            nulla "Ja ja."

    hide nulla_cerca2_enojo
    hide nulla_cerca_normal
    show nulla_cerca_callado
    "..."
    "Nulla suelta tu mano, optando por arreglar su corbata y colocarla en su lugar, deshaciendo el nudo a uno para convertirlo en uno perfecto."
    nulla "Escucha, [nombrejugador]."
    nulla "A madre le tomó un día entero arreglar a tu marioneta..."
    nulla "Tenemos que partir ahora."
    nulla "Te juro que cuando matemos a Septem, te daré el séptimo día para pasar el día juntos..."
    nulla "Solo tú y yo."

    hide nulla_cerca_callado
    scene negro with pixellate
    
    "Asientes sin pensarlo mucho. Ya no te quedan fuerzas para oponerte a Nulla, o hacer más larga tu estadía en este lugar."
    "Estás cansado y quieres terminar con la caza de una buena vez por todas."
    "Será que gracias a todo lo que has pasado, ya te encuentras desensibilizado frente a todo el horror que has cometido junto a Nulla..."
    "Una muerte más, qué más da."
    "Ahora solo es una tarea más que te llevará a tu recompensa final..."
    "Tomas su mano y comienzan a caminar."

    play music "audio/void3.mp3" fadein 3.0 volume 0.3
    
    #No poner sonido. o buscar ruido blanco.
    "..."
    "Caminas por el vacío sin rumbo alguno. Te preguntas cuándo aparecerá la casa de Nulla, pero mientras más caminan, tus esperanzas de verla una vez más van disminuyendo."
    "Tus pasos se mimetizan con los de él, caminando a paso lento, en sincronía."
    "Optas por mirar como ambos zapatos avanzan en el inexistente suelo. Mirar al frente y no ver nada más que negro... es perturbador. No escuchar nada más que tus pasos, o el sonido de tu propia respiración, se siente extraño."
    "No puedes evitar pensar en que estás siendo consumido por un abismo descontrolado, que probablemente no tiene inicio o final."
    menu:
        "¿Así era antes?":
            nulla "Sí."
            nulla "Lindo, ¿no?"
            #Nulla contesta que sí, cuenta un poco de como era todo antes del Jardín.
            "..."
        
        "¿Dónde está tu casa?":
            nulla "Ya no existe."
            "Te responde sin pizca de remordimiento o siquiera pena en su voz, y aún así, aprieta los labios."
            nulla "La he borrado."

            menu:
                "¿Y mi dibujo?..." if cuadro_modificado():
                    pass

                
                "¿Todo?...":
                    pass
            
            if cuadro_modificado():
                nulla "Ah---no."
                "Es ahí cuando su careta de no importarle nada se rompe. Nulla te mira complicado, sus labios tiemblan en una mueca que no sabes si es de pena o gracia."
                "Cuando no puede más, él ríe nervioso."
                nulla "Es lo {b}único{b} que no me atrevería a borrar."
                nulla "Mira---"
                $ abrir_imagen("para_nulla.jpg")
                nulla "Se ve tan linda en tu galería..."
                nulla "¿Realmente pensaste que borraría eso?"
                "Te sonríe con ternura."
            
            else:
                nulla "Todo."
                "Responde él sin sentimiento alguno, importándole poco las memorias que aquel lugar le ha brindado."
            
            pass


            #Nulla responde que no existe más. Qué ha sido borrada.
            #Preguntas por tu dibujo (si es que lo hiciste), y Nulla lo saca de su chaqueta.
            "..."
        
        "Esto no me gusta...":
            #Nulla no responde nada.
            "..."
            "Nulla no te devuelve la palabra, interesado más en caminar."

    "Siguen caminando, sin apuro."
    "Nulla sonríe, una sonrisa que parece estar pegada a su cara. Supones que tiene justificación para estar así, ha pasado 4 años esperando este momento."
    "Por fin obtendrá lo que busca..."
    "Pero--- ¿luego qué?"
    "¿Será que realmente conseguirá lo que ansía?"
    "Después de todo... el concepto de muerte solo aplica para los seres vivos..."
    "¿Es posible que Nulla deje de existir?"
    "¿Qué pasaría si...?"
    "¿Qué pasará contigo?"

    menu:
        "Nulla...":
            pass

        "...":
            pass
    
    nulla "Mira al frente."

    scene negro2 with dissolve

    "Sus palabras rompen el silencio, llevando tu atención al camino por el que van avanzando."
    nulla "¿Ves ese punto blanco de allá?"
    "Lo ves, es diminuto, una pequeña luz que titila formando un horizonte."
    nulla "Ahí está Septem."
    nulla "Ven, acerquémonos."
    menu:
        "¿No es peligroso?":
            show nulla_cerca2_normal at right

            "Nulla resopla riendo."
            nulla "Septem ya no puede hacer nada."
            nulla "Tiene un cuerpo mortal y nadie que lo proteja."
            hide nulla_cerca2_normal with dissolve

        
        "No quiero ir...":
            $ amor_nulla -= 2
            show nulla_cerca2_enojo at right 
            with dissolve

            "Su expresión se torna oscura, ojos que te escanean, buscando alguna reacción detrás de la pantalla."
            
            hide nulla_cerca2_enojo
            show nulla_cerca_normal at right

            "Cuando crees que ya la encontró, él sonríe con malicia."
            nulla "Lindura, ya no tienes opción."

            hide nulla_cerca_normal
            show nulla_cerca2_normal at right

            nulla "No nos demoraremos tanto. Te lo prometo."
            nulla "Cuando termine, podemos hacer algo divertido~."
            "Te habla con un tono condescendiente, forzando sus labios en una imitación a una sonrisa. Muy tensa, muy falsa, haciéndose notable lo irritado que está gracias a sus ojos."
            
            hide nulla_cerca2_normal with dissolve

            nulla "Vamos."
    
    "En tus pies se siente movimiento, algo trepa por tu tobillo, deslizándose con suavidad hacia tu cadera y torso. Se enrosca en tu cuerpo como una serpiente, subiendo hasta tu cuello sin llegar a cortar el aire."
    "Estás siendo consumido por las sombras de Nulla. Esa sensación fría, líquida y viscoso acaricia tu piel, permitiendo una entrada más rápida al lugar a donde Nulla quiere llegar."
    "La oscuridad cubre tu rostro y comienzas a caer."
    "No sabes con seguridad donde está Nulla, pero si lo sientes a tu lado. Dentro de tu estómago, en tu piel, boca y manos."
    "Te ahogas en su presencia."
    "..."
    scene cuartonegro with pixellate

    #Poner la sala del vacío que está en el dominio de Septem.
    "Tus pies tocan piso. Procurando no caer das un par de pasos para estabilizar tu cuerpo, Nulla también ayuda, ofreciendo su mano como soporte."
    "Das dos pasos hacia atrás y te topas con algo duro. Palpas descubriendo una superficie que te recuerda a la madera de algún escritorio o mesa."
    "Escaneas tu alrededor, hay oscuridad total... es imposible discernir con la vista que es lo que te rodea."
    "Nulla cubre tu mano con la suya, el calor de que irradia te calma un poco los nervios."
    
    nulla "Ja ja, esto sigue intacto."
    nulla "Salgamos de aquí."
    "Eres conducido por el lugar a ciegas, tú solo te preocupas de seguir la mano de Nulla, confiando plenamente en que no chocarás o caerás en ningún momento."
    "Escuchas cómo el pestillo de una puerta se acciona, acompañado por una manilla siendo girada."
    scene blanco with dissolve
    "De repente, tu visión es invadida por un destello blanco. Es molesto, y tienes que parpadear un par de veces para acostumbrarte al repentino cambio."
    
    scene temploseptem 
    show eliminacion 
    with dissolve

    "Al recobrar la vista, un templo te da la bienvenida. El lugar es incomodo de ver, se siente exageradamente grande..." 
    "Blanco tiñe las paredes, comiéndose de a poco el espacio. Resquebrajando los cuadros y estatuas, consumiendo todo a su paso de manera lenta."
    "Moribundo."
    "Duele ver el estado del lugar."
    "Dentro de la sala hay un montón de puertas, tantas que te mareas con tan solo pensar que tan grande será el lugar completo."
    
    show nulla_cerca2_normal with dissolve

    nulla "Es algo chistoso."
    "Nulla levanta la voz, buscando llegar a oídos que no son los tuyos. El sonido rebota provocando eco, chocando con el desolado espacio que queda del Jardín."
    
    hide nulla_cerca2_normal
    show nulla_cerca_normal
    nulla "En el sexto día hiciste nacer la humanidad. Y fue un sábado el día en que te di ese cuerpo."
    nulla "Sólo me bastaron seis días para quitártelo. Es irónico---"
    "Él camina por el lugar desbordando confianza, ensimismado en la cercana victoria que ya se ha atribuido."
    
    hide nulla_cerca_normal 
    scene puerta
    with dissolve

    "Se dirige a una de las tantas puertas, tú le sigues de cerca, con temor a quedarte atrás y ser tocado por lo que deteriora las paredes. Cuando la abre, te percatas como esta también comienza a deteriorarse en la zona que él ha tocado."
    "Avanzan por el pasillo que pareciera no tener fin..."
    
    scene act3_n7 with dissolve

    "Aun así, le sigues el paso sin mirar atrás."
    "..."
    $ config.rollback_enabled = False
    "Llevan un tiempo así, no más de tres minutos, pero tú ya comienzas a desesperar."

    jump menu_pasillo_borrado


label menu_pasillo_borrado:

    menu:
        "Caminar junto a Nulla.":
            "Mantienes el paso."
            "No pareces avanzar."
            "..."
            jump menu_pasillo_borrado


        "Mirar atrás.":
            scene pasilloinfinito
            show pasillo_borrado1 
            with dissolve
            "..."
            "Nulla está borrando el lugar."
            jump menu_pasillo_borrado2


label menu_pasillo_borrado2:
    scene act3_n7 with dissolve
    menu:
        "Seguir caminando.":
            "Esto no te gusta.........."
            jump menu_pasillo_borrado2


        "Mirar atrás.":
            scene pasilloinfinito
            show pasillo_borrado2 
            with dissolve
            "..."
            "Lo blanco avanza con ustedes. Acercándose cada vez más."
            jump menu_pasillo_borrado3


label menu_pasillo_borrado3:
    scene act3_n7 with dissolve
    menu:
        "Seguir caminando.":
            jump menu_pasillo_borrado3
        

        "Mirar atrás...":
            scene pasilloinfinito
            show pasillo_borrado3
            with dissolve
            #mostrar como el blanco ha consimido más del pasillo, está por tocar tus pies.
            "Aquello engulle cada paso que dejas, esperando a comerte si te distraes y quedas atrás. Casi dejas de caminar por estar mirando como lo blanco avanza, tentando tu suerte, pero Nulla no te lo permite."
            scene pasilloinfinito
            show nulla_cerca_callado
            with dissolve
        
            "Toma tu mano, acercando tu cuerpo al suyo."
            
            hide nulla_cerca_callado
            show nulla_cerca2_normal

            nulla "No te quedes atrás, mi vida."
            nulla "Si no tienes cuidado, podría borrarte <3."
            nulla "Y eso me pondría muy triste :(."
            jump continuacion_nulla_act3_final


label continuacion_nulla_act3_final:

    scene puerta with dissolve
    "Por fin llegan al final."

    hide nulla_cerca2_normal
    show nulla_cerca_normal

    "Nulla esboza una floja sonrisa, tomándose la situación con humor."
    nulla "Eso fue intenso ja, ja, ja."

    hide nulla_cerca_normal 
    scene comedorseptem2
    with dissolve
    
    
    "Pasan el umbral de la gran puerta que les bloquea el paso. Del otro lado hay un comedor."
    nulla "Aquí estás."
    nulla "Buenos días."
    septem "Púdrete."
    scene comedorseptem3 
    "Escupe con veneno el rubio. Yace sentado en una mesa larga, apta para un banquete, especial para recibir visitas."
    "Está sentado en la cabecera, la que da al ventanal."
    "En la superficie de la mesa hay un plato vacío junto a un montón de utensilios elegantes, una copa solitaria los acompaña, sin contenido dentro de ella."
    "En el centro, una vela, que brilla con una luz inusual. Su llama rojiza se alza por sobre la mecha, flameando con el aire."
    
    scene negro
    show septemcena_enojo
    with pixellate

    "Septem mira a Nulla con odio puro en sus ojos."
    
    show nullacena_sonrisa with dissolve

    nulla "No me mires así, ya sabías que esto iba a pasar."
    
    hide nullacena_sonrisa
    show nullacena_risa

    nulla "Te he ganado. Ya no queda nada. No hagas esto más largo."
    septem "..."
    septem "¿Terminaste?"
    
    hide septemcena_enojo
    show septemcena_enojo2
    hide nullacena_risa
    show nullacena_sonrisa

    "Septem se levanta de la silla, más no se acerca a ustedes."
    septem "Siempre hablas tanto. Me enfermas."
    "Hay una pausa, en donde ambos hombres se observan sin realizar movimientos. Hasta que Septem decide acercarse, marcando el paso con sus suelas, emitiendo un sonido constante."
    "Se detiene al frente de Nulla, respetando su espacio, sin miedo a lo que le pueda pasar."
    
    hide septemcena_enojo2
    show septemcena_grito
    hide nullacena_sonrisa
    show nullacena_enojo

    septem "No sé cómo planeas acabar conmigo..."
    septem "Esto es estúpido. La única regla que no depende del Jardín es esta."
    septem "No me puedes dañar, ni borrar."
    septem "Termina con esta rabieta. Dame al Dios que tienes dentro de la marioneta."
    hide nullacena_enojo
    show nullacena_risa
    nulla "Con gusto."
    "¡¿...!?"
    "Buscas a Nulla con la mirada, confundido, sin saber que hacer."
    
    scene septimo with pixellate

    "Él se aparta del camino, dando un paso al lado, invitándote a avanzar hacia Septem."
    "{glitch=30.0}{color=ffffff}{b}Confía en mí, cariño.{b}{/color}"
    
    play music "audio/fronbondi1.mp3" fadeout 1.5 fadein 3.0 volume 0.3

    "{glitch=30.0}{color=ffffff}{b}Hazlo.{b}{/color}"
    

    menu:
        "{glitch=30.0}{color=ffffff}{b}avanzar.{b}{/color}":
            pass

        "{glitch=30.0}{color=ffffff}{b}avanzar.{b}{/color}":
            pass

        "{glitch=30.0}{color=ffffff}{b}avanzar.{b}{/color}":
            pass

        "{glitch=30.0}{color=ffffff}{b}avanzar.{b}{/color}":
            pass

        "{glitch=30.0}{color=ffffff}{b}avanzar.{b}{/color}":
            pass
        
        "{glitch=30.0}{color=ffffff}{b}avanzar.{b}{/color}":
            pass

        "{glitch=30.0}{color=ffffff}{b}avanzar.{b}{/color}":
            pass

        "{glitch=30.0}{color=ffffff}{b}avanzar.{b}{/color}":
            pass

        "{glitch=30.0}{color=ffffff}{b}avanzar.{b}{/color}":
            pass
        
        "{glitch=30.0}{color=ffffff}{b}avanzar.{b}{/color}":
            pass

        "{glitch=30.0}{color=ffffff}{b}avanzar.{b}{/color}":
            pass

        "{glitch=30.0}{color=ffffff}{b}avanzar.{b}{/color}":
            pass

        "{glitch=30.0}{color=ffffff}{b}avanzar.{b}{/color}":
            pass
    
    
    "Avanzas sin opción, no siendo dueño de tus movimientos una vez más. Te acercas a Septem a paso lento, él te ofrece la mano, esperando a que la tomes..."
    "Tú la alzas, buscando agarrar su mano."
    scene negro with vpunch

    "Sus movimientos son rápidos, por lo que no eres capaz de comprender exactamente que pasó."
    "Eres lanzado lejos, cayendo directo al suelo, golpeando tu cabeza y espalda. El dolor en tu muñeca es insoportable, Septem te ha tomado por ahí."
    "Tu visión se torna borrosa, bloqueando tus sentidos por completo junto a un pitido en tu oído."
    "Nulla te grita algo."
    scene pelea with vpunch
    "Septem está encima de él, golpeando su cara y abriendo su pecho, en busca de su corazón. Nulla no puede hacer nada más que retorcerse."
    "Intenta invocar sus sombras, las cuales alcanzan a formarse, pero se detienen justo antes de poder tocar a Septem."
    "Algunas se logran acceder a su cuerpo, pero solo sirven para retenerlo por unos segundos. Septem se encarga de romperlas y quemarlas."
    "Una de las sombras de Nulla te ayuda a levantarte."
    "Observas lo que pasa desde lo lejos, Nulla intenta defenderse reteniendo las manos del rubio, pero este no se deja."
    "Le grita, pidiendo que pare, logrando solo que Nulla ría."
    "{glitch=30.0}{color=ffffff}{b}Yo lo distraígo, cariño.{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}Tú toma unos de los cuchillos.{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}Debes atacarlo.{b}{/color}"

    menu:
        "Buscar un cuchillo.":
            pass

        "No hacer nada.":
            "{glitch=30.0}{color=ffffff}{b}Oh, no, no, no, cariño.{/glitch}{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}No seas tonto.{/glitch}{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}No voy a permitir que hagas eso.{/glitch}{b}{/color}"
            pass
        
        "Agarrar la vela." if persistent.septem_symbol2 == True:
            jump septemgana_n_act3
            
            #Saltar a un final de Septem.
    

    #Poner como la mationeta se acerca a Septem.
    #Aparece una pantalla de interacción, la cual tiene tiempo. Si no lo logras a tiempo, Septem te atrapa y mata (fuck you).
    #Aquí es donde matas a septem a cuchillo limpio.
    #Fin

    jump asesinato


label continuacion_nulla_act3_final2:
    scene muerte_final2
    "En tus manos tienes el corazón de la entidad de máxima autoridad de lo que fue una vez el Jardín."
    "Sigue latiendo, las venas doradas siguen ejerciendo fuerza sobre el pedazo de carne que tienes entre los dedos. Intentan bombear sangre aún."
    "Parece un acto desesperado."
    "No se dan por vencidas..."
    menu:
        "¿Dónde está la esencia?":
            pass
    
    nulla "La tienes en tus manos."
    
    menu:
        "¿Tengo que comerlo así?":
            pass
    
    
    
    "Nulla aprieta los labios."
    nulla "Su esencia se fusionó con ese corazón."
    
    nulla "Deberías comerlo antes de que intente fusionarse contigo, mi vida."

    scene muerte_final with dissolve
    pause 1.5
    scene negro with dissolve

    "Suspirando y ya agotado de todo esto, cierras los ojos."
    
    stop music fadeout 3.0

    "Te aguantas el asco como puedes."
    

    "Abres la boca y Nulla se encarga de tomar tus manos con las suyas para ayudar a acercar el corazón de Septem a ti."
    "Intentas tragártelo, pero las arcadas te dificultan el proceso."
    "No sabe a nada.... solo percibes su textura viscosa contra la lengua."
    "Te toma al menos tres tortuosos intentos ingerir el corazón."
    "Ya no puedes más..."
    "Estás cansado...."
    "...."
    "......."
    "Escuchas a Nulla reír. Es una risa que en cualquier otro contexto sería normal, hasta tierna. Está llena de gozo genuino, una euforia que solo aparece cuando obtienes algo que has perseguido por mucho tiempo."
    "Te da las gracias una y otra vez. Te toma las manos, pero tú no lo puedes ver."
    "Te abraza, besa..."
    "Y sigues sin poderle ver, por lo que comienzas a entrar en pánico, pensando que tal vez hay algo mal con tus ojos."
    menu:
        "Nulla... no puedo verte.":
            pass
    
    nulla "Oh..."
    "Es todo lo que te regala como respuesta."
    "Luego suelta aire, dejando escapar una risilla atónita."
    nulla "Apagamos la luz de este lugar."
    "Ríe nuevamente."
    nulla "Estamos a oscuras~~~"
    nulla "..."
    "Sus manos se entrelazan con las tuyas en la oscuridad, ofreciendo un granito de tranquilidad."
    nulla "Pero no te preocupes~"
    nulla "Tengo ---"
    
    play music "clap.mp3" fadein 2.0

    centered "¡BRAVO!"
    
    centered "¡¡¡¡Lo has logrado!!!!"
    
    play sound "clapclap.mp3"

    "Escuchas aplausos alrededor tuyo."
    stop music fadeout 2.0
    scene blanco with dissolve
    "Una luz cegadora entra en tus retinas."
    scene negro with dissolve
    show aplausos


    "Cuando te acostumbras al cambio de iluminación, te encuentras con dos manos gigantes que aplauden arriba tuyo. Su ritmo es lento, como si se burlase de la situación."
    el "Pero te has quedado sin tiempo~~~ \n\n                  Boo hooo~~~"
    nulla "¿¡QU----!?"
    el "Tenemos que seguir un itinerario, lo siento querido~"
    el "Tu tiempo se ha acabado."
    el "Vamos a tener una pausa------- "
    extend "laaaaaaaaaargaaaaa."
    "..."
    el "Tal vez así puedas pensar mejor tus decisiones. Solo."
    el "Mientras esperas que [nombrejugador] vuelva por nuevo contenido~"
    nulla "ERES UN-----!!!"
    stop sound
    scene negro with pixellate
    centered "Corte~~~~."
    play sound "tv-static.mp3" volume 0.5 fadein 3.0

    "---------------------------------------------"
    "------------------------------------------------------------------------"
    "{sc=4}Fin del acto 3.{/sc}"
    "{sc=4}Tocará esperar a la última actualización para saber como acaba esta historia {/sc}"
#Poner sonidos de aplausos.
#Padre da un discuros de mierda y menosprecia a Nulla. Diciendo que se ha quedado sin tiempo y que tendrá que esperar un poco más para su final.
#Pues Padre tiene que pensar en un final digno para él.
    $ MainMenu(confirm=False)()
    return 



        
            
    



    #Descibir que ya no hay nada en el dominio de Nulla, ni siquiera su casa, solo el vacío.
    #Describir como llegan al dominio de Septem. Todo está blanco, menos el dominio de Septem.
    #Septem está sentado en su mesa, con los platos vacíos.
    #Nulla llega desbordando arrogancia.
    #Matan a Septem. Nulla tiene que poner un garabato en la cara de Septem para que no le de pena por Rafael, ya que no quiere ver eso, ni mucho menos titubiar.





    # $ import webbrowser; webbrowser.open("https://parati.itch.io/")
    # nulla "Jajaja, no te emociones aún."
    # nulla "Esto es solo una idea que tengo."
    # nulla "Necesito mucha más energía para llevarla a cabo."
    # nulla "Pero quería adelantar la sospresa <3"
    


    


return