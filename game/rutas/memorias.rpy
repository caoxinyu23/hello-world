# Declare characters used by this game.
define creador =Character (_("Padre"), color = "#ffe6aa")
define m =Character (_("Michael"), color = "#5dd6bc")
define z =Character ("Zadkiel", color = "#c233ff")
define g =Character ("Gabriel", color = "#d7d7d7")
define r =Character ("Rafael", color = "#17c900")

init python:
    import os
    import subprocess

    def crear_y_abrir_carpeta():
        desktop = os.path.expanduser("~/Desktop")  
        carpeta = os.path.join(desktop, "Nulla")  
        archivo_es = os.path.join(carpeta, "Corazón.txt")  
        archivo_en = os.path.join(carpeta, "Heart.txt")  

        
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        
        contenido_es = (
            "Espero que no me odies por lo que te hice... Ahora lo entiendo. Lo viste todo, "
            "¿no? lo has visto todo a través de los ojos del Creador…… y has tenido que leer eso…… "
            "Lo siento, no estaba pensando claro..... Ojalá pueda hacer algo para compensarte, "
            "si es que estás disgustado con esto, si te decepcioné....Por favor no me dejes solo………… "
            "Por favor no me abandones…………… "
            "_______________Por favor no me olvides."
        )

        contenido_en = (
            "I hope you don't hate me for what I did to you... Now I understand. You saw it all, "
            "didn't you? You have seen everything through the eyes of the Creator... and you had to read that... "
            "I'm sorry, I wasn't thinking clearly... I wish I could do something to make it up to you, "
            "if this upset you, if I disappointed you... Please, don't leave me alone... "
            "Please, don't abandon me... "
            "_________________Please, don't forget me."
        )

        
        with open(archivo_es, "w", encoding="utf-8") as f:
            f.write(contenido_es)

        with open(archivo_en, "w", encoding="utf-8") as f:
            f.write(contenido_en)

        
        if os.name == 'nt':  
            os.startfile(carpeta)
        elif os.uname().sysname == 'Darwin':  
            subprocess.Popen(['open', carpeta])
        elif os.name == 'posix':  
            subprocess.Popen(['xdg-open', carpeta])




init python:
    def guardado_automatico():
        for i in range(1, 10):
            renpy.save(f"1-{i}")


init python:
    import os

    
    def get_username():
        return os.getenv('USERNAME') or os.getenv('USER')

    
    usuario = get_username()
    
# The game starts here.
label memoriasnulla:
    $ persistent.null = False
    "Con curiosidad sueltas la mano de Nulla y te diriges a donde es encuentra la sombra."
    nulla "¡Hey!"
    "Cuando llegas al lugar, la sombra desaparece con una risa distorsionada entre dos tonos, uno femenino y otro masculino."
    "Sientes un escalofrío recorrer tu espalda."
    "Para cuendo Nulla llega a tu lado te toma de los hombros."
    nulla "Es peligroso que te separes de mi lado, si te pierdes aquí no me va a ser tan fácil encontrarte."
    stop music fadeout 3.0
    nulla "No---"
    scene m_0 with pixellate
    play music "audio/meeting.mp3" fadein 2.0 volume 0.3
    creador "NULLA."
    "La misma voz reaparece y Nulla se tensa al instante."
    "Una figura tan blanca como la nieve se forma detrás del pelinegro, y permanece ahí, quieta; observándolos a ustedes dos sin hacer movimiento alguno. Como si de una imagen se tratase."
    scene negro with vpunch
    "Nulla intenta abalanzarse hacia ti, pero dos manos se materializan para evitarlo y como si el cuerpo de Nulla se tratase de un trapo, ambas manos desgarran los brazos del pelinegro sin mucho esfuerzo."
    "Gritas su nombre"
    "Tienes terror, pero a pesar de ello no dejarás que algo peor le pase a Nulla. Así que intentas agarrar su cuerpo para evitar que Nulla sufra más daños."
    scene m_0_1_a with pixellate
    creador "No pasa nada~"
    creador "Tranquilízate, Nulla no va a morir por esto, solamente lo dejé fuera de combate."
    show m_0_1
    creador "No eres nada sin tus brazos y manos, gusano."
    scene m_0_1_a
    "La figura se acerca a ustedes a paso lento, tomándose más tiempo del necesario."
    nulla "¡Tienes que salir del Jue-"
    scene m_0_1_b
    creador "Cierra la boca."
    "Con solo decirlo, Nulla cierra la boca forzadamente, casi como si algo invisible a tus ojos presionara su mandíbula contra su cráneo."
    show m_0_1_a
    creador "Callado te ves más bonito, Nulla~"
    "Cuando la figura llega a donde están ustedes, te das cuenta de lo alto y grande que es. Al menos les saca 3 cabezas por encima de ustedes."
    "Además, su aura es incomoda, algo en siente rechazo y repulsión."
    scene m_0_1
    creador "Hmmm, tú debes ser [usuario]. ¿Será ese tu verdadero nombre?"
    creador "Lastima que no tengo como corroborar esa información."
    creador "..."
    show m_0_1_a
    creador "Y bien, ¿Cómo te la has pasado?"
    creador "¿Te gusta este mundo?"
    creador "¿Te gusta este show?"
    
    menu:
        "No...":
            creador "..."
            show m_0_1_b
            creador "Uh, entonces vete, ¿qué haces perdiendo tu tiempo en algo que no te divierte ni te gusta?."
            creador "Aunque sé que volverás tarde o temprano."
            creador "Te dejaré un {size=*1.5}pequeño{/size} regalo en la página 1 de tus guardados."
            creador "Ya que Nulla lo ha borrado todo."
            hide m_0_1_b
            show m_0_1
            creador "Por si quieres acceder a esta ruta en un futuro."
            creador "Nos vemos."
            $ renpy.quit()
            
        
        "Sí":
            creador "Me alegra."
            creador "Creo que dejarlos esperando por tanto tiempo ha dado frutos."
            pass

        "¡Deja a Nulla en paz!":
            creador "Jajajaja."
            creador "..."

    show m_0_1
    creador "Dime..."
    creador "¿Te gustaría viajar al pasado?"
    creador "¿Cuando Nulla no era... así?"
    
    menu:
        "Quiero que lo dejes en paz.":
            creador "No le haré nada."
            creador "Diviértete un rato, no te tomes tan apecho esto. Aguafiestas."
        
        "Está bien.":
            creador "Así me gusta."

        "No.":
            creador "..."
        
    scene m_0_1_a
    creador "De cualquier modo, haré lo que se me plazca, tu no tienes el control de este mundo."
    "La figura acerca las manos sobrantes a tu frente, y te toca con delicadeza."
    creador "A partir de ahora tendrás mis ojos, omnipotentes en tiempo y espacio. vas a perder la capacidad de interactuar con tu alrededor por un tiempo."
    creador "Por lo menos hasta llegar a mi antigua magnum opus."
    scene negro with dissolve
    "Luego de eso todo se torna negro."
    stop music fadeout 3.0
    creador "Puesta en escena~~~"
    play music "audio/hope.WAV" fadein 2.0 volume 0.4
    creador "Cuando Septem fue creado, tuve una conversación con Nulla, quién aceptó quedarse en mi jardín bajo la condición de que yo no abandonara el mundo."
    creador "Quería tener una vida pacífica..."
    creador "Je-"
    creador "De cualquier modo---"
    creador "Septem en ese tiempo no tenía un cuerpo físico, pues no se me dio la gana hacerle uno. Además... quería ver si haría algo al respecto o no."
    creador "Era obvio su anhelo por un cuerpo físico, y esto se notaba más cuando veía a los Estandartes interactuar con sus dominios y los demás."
    creador "Sextam, siendo tan humana y llena de emociones, se dio cuenta de ello... e increíblemente, Nulla también."
    creador "... Así qué ambos se reunieron a charlar para buscar soluciones."
    scene m_1 with dissolve
    sextam "Creo que podemos usar humanos.... pero no mis humanos..."
    nulla "¿Por qué no?"
    sextam "Amo a Septem pero..."
    sextam "No pienso sacrificar uno de mis hijos. ¡Todos tienen almas ya!"
    nulla "Mmmm."
    sextam "Nos has dicho que tu puedes moverte entre mundos, ¿hay humanos en esos mundos?"
    nulla "¿...Tal vez?"
    nulla "Por lo general la mayoria de los mundos están vacíos."
    sextam "Oh."
    nulla "Pero puedo intentarlo."
    sextam "Eres el mejor, Nulla."
    scene entradanulla with dissolve
    "Sextam le da un cálido abrazo a Nulla y ambos vuelven a programas una reunión en 7 días más. Nulla se retira del dominio de Sextam para volver al vacío."
    "Mientras más rápido haga esta búsqueda, más rápido podrá tener su retiro y dejar de ser el vocero de Septem en los dominios del 0 hasta el 6."
    scene jardinnulla with dissolve
    "Así que después de almorzar, sale de su casa al vacío. Lo contempla antes de dejarse caer en él."
    scene negro with pixellate
    "Ahí en el vacío más puro del jardín, descubrió la condena que di a Grimal..."
    "Así que no importaba lo que se encontrara luego, él ya venía con un propósito claro, encararme luego de encontrar un cuerpo para Septem."
    "Los mundos que visitó eran un chiste, algunos tan pequeños que era imposible para él caminar un solo paso o respirar muy hondo, pues al inflar su pecho se topaba con el límite."
    "Otros eran un poco más lúgubres y penosos, llenos de detalles pero sin habitantes."
    "Los demás eran solo bocetos... nada le servía."
    scene magnumopus with pixellate
    "Hasta que llegó, por mera casualidad, por un desperfecto, una pequeña fuga de luz o una linea mal trazada... a mi antigua Magnum opus."
    "...."
    stop music fadeout 3.0
    el "¡Mi señor! ¿Cree poder venir a ver al banquete de inauguración?"
    play music "audio/frozen_winter.WAV" fadein 2.0 volume 0.3
    "Ahora estás en mi cuerpo, pero te dejaré interactuar con mis guardianes. Haré lo que hace tu marioneta, será divertido~"
    "Enfocas tu presencia en el mundo donde te llaman."
    scene m_2 with dissolve
    "Y abres tus ojos."
    m "¿Mi señor?"
    menu:
        "...":
            pass

        "¿Quién eres?":
            "El hombre frente a ti se toma un segundo antes de contestar."
            m "Soy Michael."
            pass

        "Michael.":
            "Michael sonrie al escuchar tu voz."

    "Sientes como tu cuerpo cambia de forma, el proceso es extraño, pero no te causa dolor... solo incomodidad. Cuando terminas la transformación te das cuenta de que ahora estás usando tu forma original: la de tu marioneta."
    "Michael te observa sorprendido."
    m "Ohh, ya veo."
    m "Tenemos nuestro primer visitante."
    m "Nuestro Señor nos ha hablado de ti."
    m "Dijo que llegarías en algún momento del día."
    m "Un gusto poder tener tu presencia en nuestro mundo."
    m "Dame la mano."
    menu: 
        "Dar la mano":
            "Michael sonrie nuevamente ante tu acción."
        
        "No gracias":
            "Michael sonrie entendiendo tu decisión."

    scene magnumopus2 with dissolve
    "Caminan el uno junto el otro, y no puedes evitar mirar sus alas cuando sientes que las alas en su espalda rodean tu cuerpo como si te protegiera del sol."
    "Aunque no llegan a tocarte, te transmite un calor y calma reconfortante..."
    show michael1normal with dissolve
    m "Nuestro señor ha dicho que tal vez quieras pasar tiempo con Rafael."
    m "¿Lo conoces?"
    menu:
        "Eso creo...":
            hide michael1normal
            show michael1hablando
            m "No te preocupes, Rafael no muerde."
        
        "No":
            m "Oh, ya veo."
            hide michael1normal
            show michael1hablando
            m "Me debo haber equivocado entonces."
            m "Mis disculpas, tengo tanto trabajo que no he podido descansar bien."

    "Llegan a una mesa que tiene un montón de fruta. Pero eso no es lo que te llama la atención, no... lo que captura tus ojos son 3 pares de alas que envuelven tu visión, tapando toda la luz que el cielo tiene para ofrecer."
    scene m_3 with dissolve
    r "¡Hermano! ¿Te parece si tenemos un combate?"
    r "Zadkiel me ha dicho que hoy tienes el día libre, ¡oh!"
    "Rafael posa su mirada en tus ojos mientras suelta su florete."
    r "¿Has traído un prototipo al banquete?"
    scene magnumopus with dissolve
    "Las alas de Michael dejan de rodearte para que Rafael pueda inspeccionarte. Coloca sus manos en tus mejillas y las masajea no creyendo lo que ve."
    show rafael_a_normal at right with dissolve 
    r "¿Lo podemos tocar?"
    show michael1hablando at left with dissolve
    m "Nuestro Señor lo ha traído, para la inauguración del mundo."
    show zadkiel1normal with dissolve
    hide rafael_a_normal
    show rafael_a_sonrisa at right
    z "Supongo que quiere que tengamos contacto con uno antes inaugurar el mundo."
    m "Puede ser..."
    hide zadkiel1normal
    show zadkiel1hablando
    z "Aún falta para el banquete, ¿qué planeas hacer con el humano mientras?."
    m "El Señor no me ha dado instrucciones."
    hide rafael_a_sonrisa
    show rafael_a_normal at right
    r "Yo puedo ocuparme de él mientras tú descansas, Michael."
    hide zadkiel1hablando
    show zadkiel1normal
    z "Yo me voy, tengo cosas que hacer."
    hide zadkiel1normal with dissolve
    "Supones que Zadkiel no tiene interés en cuidarte..."
    m "¿Qué dices?"
    "Michael se vuelve hacia ti con una sonrisa serena, irradiando calma en todo momento."
    m "¿Quieres ir con Rafael?"
    menu:
        "Quiero quedarme junto a ti.":
            m "Jaja-- Okay okay."
            m "Rafael, ve a entrenar mientras, yo iré contigo luego de un rato."
            hide rafael_a_normal
            show rafael_a_sonrisa at right
            r "¡Si señor!"
            scene michael3 with dissolve
            "Michael te lleva al lago, y mientras observa el agua moverse, él te habla de sus días."
            "Su voz es serena, calmada y tiene un efecto embriagador sobre ti. hace que lo quieras seguir escuchando."
            "Hasta que Michael calla por un prolongado tiempo."
            show michael2
            m "...¿Eres de otro mundo cierto?"
            "..."
            menu:
                "Decir la verdad.":
                    "Al confirmarle su sospecha, Michael pierde su sonrisa."
                    "Para reemplazarla con una expresión de decepción."
                    show michael1
                    m "Ya veo..."
                
                "Mentir.":
                    m "Mis disculpas... pensé--"
                    show michael1
                    m "No, no es nada."
                
                "...":
                    show michael1
                    m "Hmmm..."
                    "Supones que Michael puede inferir la respuesta a partir de tu silencio."
            scene michael3
            "Pasan el resto del día conversando de trivialidades y te das cuenta de que la compañía de Michael trae a tu ser mucha tranquilidad."
        
        "Sí.":
            m "Okay, necesito que estén aquí para el anochecer."
            m "No tarden, no quiero que el señor tenga que esperar por ustedes..."
            r "¡Entendido!"
            scene magnumopus with dissolve
            "Rafael te lleva a una colina cercana, desde aquí puedes ver el resto del lugar. Es una isla flotante, rodeadas por nubes."
            "El paisaje es hermoso."
            "Rafael pregunta por tu fisiología, y con cada pregunta parecen salir otras dos más."
            "Es curioso y no tiene reparos en muestras esa curiosidad."
            scene m_4 with dissolve
            "Mientras más preguntas, más te dan ganas de preguntar a ti también. Y sus alas, que parecen ser más suaves de lo que aparentan, no ayudan."
            r "Oh!, puedes tocar mis alas si deseas"
            "Rafael se ha dado cuenta de tus deseos."
            "Así qué accedes con un poco de verguenza de haber sido atrapado."
            "Pasan el resto del día conversando de trivialidades y te das cuenta de que Rafael es un ser muy emocional y sensible."



        "Quiero volver con Nulla...":
            m "¿Nulla?"
            m "...No tengo registros de nadie llamado así..."
            r "¿Será otro prototipo?"
            m "Puede ser..."
            "Pasan el resto del día conversando de trivialidades con ambos guardianes."
    scene magnumopus2 with dissolve   
    stop music fadeout 3.0
    "Cuando cae la noche, el lugar de encuentro está vacío... Solo estás tú, Rafael y Michael. No hay rastro de nadie más."
    play music "audio/woo_scary.WAV" fadein 2.0 volume 0.4
    "Los minutos pasan. 15 tal vez más, hasta que en la distancia un estruendo rompe el silencio."
    show michael1serio at left with dissolve
    "Michael levanta la cabeza de inmediato, alerta. Sus alas se despliegan con rapidez y su florete se materializa en su mano."
    m "Rafael, ve a buscar a los demás."
    "Te mira con preocupación antes de hablar."
    m "Tú quédate aquí. Esta es una zona segura."
    hide michael1serio with dissolve
    "Haces caso sin protestar."
    "Al menos por un tiempo."
    "Pero cuando sientes que han tardado demasiado, la inquietud te carcome y te comanda a moverte. Decides salir en busca de alguno de los guardianes."
    "Avanzas a paso lento, hasta que algo capta tu atención."
    scene magnumopus3 with dissolve
    "El vacío."
    "Hay rastros del vacío en este lugar."
    "Nulla está cerca."
    "Sin dudarlo, corres, siguiendo las partículas suspendidas en el aire como si fueran un rastro  que te invita a encontrar a Nulla."
    "Y entonces lo ves..."
    scene m_5 with dissolve
    "Nulla, con una pierna apoyada sobre un cuerpo inmóvil. Su mirada perdida en él, como si esperara una reacción, como si estuviera listo para atacar de nuevo al ver un posible movimiento en el cuerpo ya mutilado"
    "Gritas su nombre con tanta fuerza que crees que se te va a dañar la garganta."
    show m_6
    "El sonido de su nombre es suficiente para que el dueño del vacío fije su mirada en ti."
    "Tus piernas actúan de manera automática. Corres hacia él con los brazos casi abiertos, dispuesto a envolverlo en un abrazo."
    stop music fadeout 3.0
    "Sin embargo, Nulla se hunde en la oscuridad y reaparece frente a ti, emergiendo desde el suelo."
    scene m_7 with vpunch
    play music "audio/the_chillout_factory.WAV" fadein 2.0 volume 0.3
    "No hay tiempo para procesarlo. De repente, estás en el suelo, un dolor punzante atravesando tu mandíbula y tu pecho."
    "Nulla está sobre ti. Sus manos aprietan tu cuello con fuerza mientras grita."
    "Intentas explicarle que eres tú, pero es inútil"
    creador "No te escucha... Lo que ves ahora son mis memorias."
    show m_8
    nulla "¡Eres un hijo de puta! ¡Escoria de mierda!"
    nulla "¡Sigues haciendo lo mismo una y otra vez!"
    nulla "Nunca estás conforme con nada. No te tomas nada en serio. Juegas con la vida de los que creas."
    nulla "¡PERO NO ERES NADA! SOLO UNA TRISTE REPRESENTACIÓN, UNA MARIONETA, EL PERRO DEL 'JEFE'."
    nulla "¡NO ERES MÁS QUE UN PERSONAJE FICTICIO EN EL PLANO SUPERIOR!"
    nulla "Y eso te jode, ¿verdad?"
    "Nulla agarra tus manos y comienza a tirar con fuerza de ella."
    show sangre with vpunch
    "Desgarrando lentamente tus brazos. Duele."
    "Pero no puedes hacer nada."
    "Ni siquiera llorar."
    "Pues este cuerpo no es tuyo."
    nulla "Te voy a arrastrar al limbo conmigo."
    nulla "Para que sientas lo mismo que les haces a tus creaciones."
    nulla "Incluso has encarcelado a Madre."
    nulla "No te voy a matar..."
    nulla "No te dejaré descansar."
    nulla "No eres nadie sin tus brazos que te ayudan a hacer tus mierdas de creaciones."
    nulla "No vas a poder escapar."
    scene m_9 with vpunch
    "Nulla está desgarrando el otro brazo cuando un cuerpo grande y oscuro choca contra él."
    show m_10 
    pause 0.1
    show m_11
    pause 0.1
    show m_12
    "Es un monstruo alado que muerde el brazo de Nulla y como si le hiciera pagar por lo que te ha hecho, intenta arrancarlo. Pero Nulla es más rápido y agarra una de las alas que se encuentran en la cabeza de la criatura y sin remordimientos jala de ella hasta arrancarla de la criatura."
    creador "JAJAJAJAJA ¡¿En serio lo matarás?!"
    scene negro with pixellate
    "Nulla te mira incrédulo. Como si presintiera que algo no está bien."
    "Tu cuerpo se mueve solo, con el brazo que te queda, haces unas señas, invocando 3 pares de manos a tu alrededor..."
    "Una de ellas atraviesa el cuerpo de la criatura, sacándole algo de su pecho, parece ser su corazón. Mientras que el resto le arranca las alas."
    "Luego de ello tu cuerpo desaparece."
    creador "Puedes utilizar el cuerpo de tu amigo para que Septem lo use y lo cure."
    creador "Sino morirá."
    stop music fadeout 3.0
    scene final_n_act2 with pixellate
    "El cuerpo de la criatura cae al suelo de repente, como si perdiera la conciencia y comienza a cambiar su forma."
    "Es Rafael."
    "_____________________"
    scene negro with pixellate
    pause 0.2
    scene m_0_1_a with dissolve
    creador "Bien... Espero que te haya gustado este pequeño intermediario."
    show m_0_1
    creador "Piénsalo como.... una escena eliminada, la cual Nulla no te querrá mostrar."
    creador "Sin más que agregar. Nos vemos luego."
    show m_0_1_a
    creador "Disfruten su cita~"
    "___________________"
    nulla "..."
    scene calle with pixellate
    "Vuelven al callejón. El sonido de los pájaros y la gente al caminar te lo confirman."
    "No hay rastro del Creador."
    "Y Nulla no es capaz de sostenerte la mirada cuando lo buscas con la tuya."
    "Opta por mirar el suelo."
    scene negro with dissolve
    "Todo se vuelve negro..."
    menu:
        "Nulla...":
            pass

        "Todo va a estar bien.":
            pass

        "Abrazarlo.":
            "A pesar de que tus brazos se enrrollan con su cuerpo el no reacciona."
    show final_n1_act2 with dissolve
    nulla "..."
    show final_n2_act2
    nulla "Lo siento, mi vida."
    nulla "Discúlpame... por favor..."
    nulla "Creo que necesito un tiempo a solas."
    show final_n3_act2
    nulla "Te..."
    nulla "Te quiero."
    nulla "Por favor--"
    nulla "No tenía idea de que--"
    nulla "No, no puedo hacerlo mientras tú me ves."
    show final_n2_act2
    nulla "Te lo escribiré en otro lado."
    nulla "Por favor no te asustes."
    nulla "Por favor acepta el mensaje..."
    menu:
        "Aceptar":
            $ crear_y_abrir_carpeta()
            

        "Denegar":
            nulla "No hace falta que lo abras ahora."
            $ crear_y_abrir_carpeta()
    
    show final_n1_act2
    nulla "Nos vemos..."
    $ renpy.quit()
    










        


        







            