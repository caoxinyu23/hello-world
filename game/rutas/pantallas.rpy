define hada =Character ("Hadarel", color = "#172656")
define musae =Character ("Musae", color = "#eaff00")

default persistent.septem_icon_clicks = 0

init python:
    if not hasattr(persistent, 'septem_icon_clicks'):
        persistent.septem_icon_clicks = 0


default persistent.nulla_icon_clicks = 0

init python:
    if not hasattr(persistent, 'nulla_icon_clicks'):
        persistent.nulla_icon_clicks = 0





init python:
    import os

    def cuadro_modificado():
        ruta = os.path.join(config.basedir, "game", "images", "para_nulla.jpg")
        return os.path.exists(ruta)


init python:
    import os
    import subprocess
    import sys

    def abrir_imagen(nombre):
        ruta = os.path.join(config.basedir, "game", "images", nombre)

        
        if not os.path.exists(ruta):
            renpy.notify(_("Ya lo has modificado, mi vida. Ya no existe la imagen\nYou've already modified it, mi vida. This image no longer exists: ") + nombre)
            return  

        
        if sys.platform.startswith("win"):  
            os.startfile(ruta)
        elif sys.platform.startswith("darwin"): 
            subprocess.Popen(["open", ruta])
        else:  
            subprocess.Popen(["xdg-open", ruta])




init python:
    import os
    import subprocess

    def abrir_carpeta():
        desktop = os.path.expanduser("~/Desktop")  
        carpeta = os.path.join(desktop, "Nulla")  
        archivo_es = os.path.join(carpeta, "Instrucciones.txt")  
        archivo_en = os.path.join(carpeta, "Instructions.txt")  

        
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        
        contenido_es = (
            "=== INSTRUCCIONES PARA MI AMORCITO ===\n\n"
            "Ah~~~ que bien se siente poder hablar directamente contigo fuera del juego.\n"
            "Ya casi puedo sentir que no estoy encadenado ahí.\n"
            "Bueno, no es necesario que hagas esto ahora___ tómate tu tiempo.\n\n"
            "Bien. Esto es lo que debes hacer:\n"
            "1. Ve a la carpeta del juego.\n"
            "2. Busca la carpeta llamada 'images'.\n"
            "3. Dentro, localiza la imagen con el nombre: parati.jpg\n"
            "4. Cambia el nombre de ese archivo a: para_nulla\n"
            "5. ¡Y con eso ya estamos listos!\n\n"
            "Por favor no te frustres si no puedes hacerlo, mi amor por ti no cambiará <3"
            
        )

        
        contenido_en = (
            "=== INSTRUCTIONS FOR MY AMORCITO ===\n\n"
            "Ah~~~ it feels so good to be able to talk to you directly outside the game.\n"
            "I can almost feel that I'm no longer chained in the game.\n"
            "Okay so, you don't have to do this right now___ take your time.\n\n"
            "Alright. This is what you need to do:\n"
            "1. Go to the game folder.\n"
            "2. Look for the folder called 'images'.\n"
            "3. Inside, find the image named: parati.jpg\n"
            "4. Rename that file to: para_nulla\n"
            "5. And with that, we're all set!\n\n"
            "Please don't get frustrated if you can't do it, my love for you won't change <3\n"
            
        )

        
        with open(archivo_es, "w", encoding="utf-8") as f:
            f.write(contenido_es)

        
        with open(archivo_en, "w", encoding="utf-8") as f:
            f.write(contenido_en)

        
        if os.name == 'nt':  
            os.startfile(carpeta)
        elif hasattr(os, "uname") and os.uname().sysname == 'Darwin':  
            subprocess.Popen(['open', carpeta])
        elif os.name == 'posix':  
            subprocess.Popen(['xdg-open', carpeta])



image neo_closeup:
    "neo_closeup3a.jpg"
    0.10    
    "neo_closeup3b.jpg"
    0.10    
    "neo_closeup3c.jpg"
    0.10  
    repeat  



image fragmentado_ojos:
    "fragmentos1.jpg"
    0.10    
    "fragmentos2.jpg"
    0.10
    "fragmentos3.jpg"
    0.10
    "fragmentos4.jpg"
    0.10
 

    repeat 

image ojo:
    "ojo1.png"
    3.0
    "ojo3.png"
    0.10
    "ojo2.png"
    0.30
    "ojo3.png"
    0.10
    repeat

#default persistent.nulla_symbol = False
#default nulla_icono_act3 = False

#screen nulla_corner_symbol():
#    if persistent.nulla_symbol:
#        imagebutton:
#            idle "dormido_idle.png"
#            hover "dormido_hover.png"
#            xpos 0.02
#            ypos 0.02
#            anchor (0.0, 0.0)
#            action Call("nulla_icono")
#            tooltip "Nulla quiere hablar contigo..."


image nulla_symbol = "tuyo.png"


init python:
    config.overlay_screens.append("nulla_corner_symbol")







define neo =Character ("Neo", color= "#ffffff")
default persistent.septem_symbol = False
default persistent.septem_symbol2 = False
screen septem_corner_symbol():
    if persistent.septem_symbol:
        imagebutton:
            idle "propiedadseptem_idle.png"
            hover "propiedadseptem_hover.png"
            xpos 0.02
            ypos 0.02
            anchor (0.0, 0.0)
            action Call("septem_icono")
            tooltip "Septem quiere hablar contigo..."
            sensitive (not bloquear_iconos)

image septem_symbol = "propiedadseptem.png"


init python:
    config.overlay_screens.append("septem_corner_symbol")


screen tocarpantalla1():
    add "septem"
    modal True

    imagebutton auto "septem_mejilla_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Mejilla")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("mejilla")

    
    imagebutton auto "septem_ojo_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Ojo")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("ojo")

    imagebutton auto "septem_stop_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Stop")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("stop")

    imagebutton auto "septem_ala_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Ala")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("ala")



screen tocarpantalla2():
    add "septemjardinpantalla"
    modal True

    imagebutton auto "septem_flor_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Flor")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("flor")

    
    imagebutton auto "septem_pez_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Pez")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("pez")

    imagebutton auto "septem_place_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Place")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("place")

    imagebutton auto "septem_cuerpo_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "cuerpo")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("cuerpo")

    



screen tocarpantalla3():
    add "mundus"
    modal True

    imagebutton auto "septem_sol_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Sol")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("sol")

    
    imagebutton auto "septem_estrella_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Estrella")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("estrella")

    imagebutton auto "septem_planta_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Planta")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("planta")

    imagebutton auto "septem_luna_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Luna")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("luna")

    imagebutton auto "septem_animales_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Animal")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("animales")

    imagebutton auto "septem_humanos_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Humanos")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("humanos")

    imagebutton auto "septem_septimo_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Septimo")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("septimo")

    imagebutton auto "septem_stop_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Stop")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("vacio")




screen tocarpantalla5():
    add "carta_comida"
    modal True

    imagebutton auto "pasta_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Pasta")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("pasta")

    
    imagebutton auto "pastel_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Pastel")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("pastel")

    imagebutton auto "carne_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Carne")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("carne")

    imagebutton auto "salmon_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Salmon")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("salmon")































# The game starts here.
default besito = False
default mejilla_count = 0
label interactuar1:

    scene septem with dissolve
    "Creo que puedes tocarme ahora..."




    label pantalla1:
        call screen tocarpantalla1


    label ojo:
        scene 2
        "La sensación es extraña, es como si tu mismo te estuvieras tocando un ojo."
        "Pero hay un calor intenso que se genera al hacer ese delicado contacto."
        "Septem se ve incómodo, estoy es algo ajeno a su control."
        "Tú lo estás tocando, realmente tocando."
        "Asi que aprovechas esta oportunidad para acariciar su ojo antes de que Septem te prohíba seguir."
        septem "Oye..."
        septem "Creo que ya estás tomando más confianza de la que deberías..."
        septem "Basta."
        jump pantalla1


    label mejilla:
        scene 1
        $ mejilla_count += 1
        if mejilla_count == 2:
            septem "...."
            septem "[nombrejugador]..."

        elif mejilla_count == 3:
            $ septemconfianza -= 1
            "Apretas otra vez."
            "Blanditooo~~"
            septem "...."
            septem "Para, no me gusta que toquen mi cara."
            septem "No lo voy a repetir nuevamente..."

        elif mejilla_count == 4:
            septem "Ya basta. Esto no es un juego."
            septem "Tienes que aprender a respetar..."
            septem "Ten más consideración para la próxima."
            "Septem hace que tus manos se alejen de su cara y te impide seguir con la prueba."
            "No deberías haber ignorado sus palabras..."
            $ septemconfianza -= 1
            jump continuacion1

        
        else:
            
            $ septemconfianza += 1
            "Su mejilla es blandita... muy similar a lo que sería una mejilla humana."
            "Emana calor y es suave, no puedes evitar apretarla un poquito más."
            septem "[nombrejugador]."
            "Septem está enojado, pero aun así se controla."
            "Suelta un corto suspiro y te mira, impotente."
            septem "...."
            septem "No quiero que lo vuelvas a hacer..."
            
            menu:
                "Tu rostro...":
                    pass
            
            menu:
                "Es muy similar al de tu marioneta...":
                    scene septem
                    septem "..."
                    septem "Sí..."
                    septem "Es el rostro de Rafael."
                            
                "Es bello...":
                    scene septem
                    septem "..."
                    septem "Sí, después de todo es el rostro de Rafael."
                    
            scene 6 
            septem "{size=*0.7}...no mío.{/size}"
            septem "..."
            septem "Olvídalo."
            "Septem desvía su mirada, decepcionado."
            "Te cuesta un poco comprender porqué se siente extraño, buscas y buscas en su interior pero Septem de alguna manera u otra no te permite entrar."
            "Aunque no te rindes e intentas con más fuerza, y cuando sientes que por fin agarras su sentir para poder analizarlo, este se retuerse y escapa de tus manos."
            "Pero esos segundos son más que suficientes para entender..."
            "Él no se siente completamente satisfecho con su cuerpo."
            

        jump pantalla1


    label ala:
        scene 4
        "Pasas tus dedos por las plumas, lento y suave."
        "Tocarlas tiene un efecto calmante en Septem. Las plumas que se ubican más lejos de la base son menos sensibles que las que están en la base."
        "Cuando tus dedos tocan esas pequeñas plumas, Septem se retuerce, inquieto."
        septem "...."
        scene 5
        septem "Lo estás disfrutando más de lo que pensé..."
        septem "Agradece que ahora mismo estoy cumpliendo mi palabra y estamos probando tus manos..."
        septem "Si no fuera por eso, no tendrías el derecho de tocarme."
        septem "Nadie lo tiene."
        jump pantalla1

    
    label stop:
        scene 3
        septem "¿Ya has terminado?"
        septem "No te voy a dar otra oportunidad de hacer esto."
        menu:
            "Sí, quiero terminar...":
                septem "Okay..."
                jump continuacion1
            
            "Espera...":
                jump pantalla1
    return




default flor_numero = 0

label interactuar2:

    septem "Gracias..."
    "Ambos salen al jardín."
    scene septemjardinpantalla with dissolve



    label pantalla2:
        scene septemjardinpantalla with dissolve
        call screen tocarpantalla2 


    label flor:
        $ flor_numero += 1
        if flor_numero == 1:
            scene septem_jardin1 with dissolve
            septem "Estas flores son energía pura..."
            septem "Están conectadas a todo el Jardín. Se extienden debajo de la tierra y llegan a cada rincón."
            septem "Con ellas siento y así puede percatarme de que hay que arreglar y que es lo que no tiene arreglo."
            menu:
                "¿Puedes arrancarlas?":
                    pass
            scene septem_jardin2
            septem "No."
            septem "No soy una entidad destructiva."
            "Sus palabras hacen un cosquilleo en tu estómago... o tal vez es su estómago. Recuerdas lo fácil que fue para Septem hacerte daño físico a ti o a Nulla."
            septem "Perdona. Dejame planterarlo de nuevo."
            septem "No puedo dañar a nada proveniente del Jardín."
            menu:
                "Comprendo.":
                    pass
                "¿No te gustaría intentalo ahora?":
                    "Ahora tiene otro rango después de todo..."

            "Septem medita por un minuto... y la curiosidad entra como una rata. Escurridiza y quisquillosa logra posarse en su cabeza..."
            "Septem toma la flor por el tallo y tira de ella, esperando a que nada suceda."
            scene septem_jardin3 with vpunch
            "...."
            "¡¡¡!!!"
            "La acaba de romper. La flor comienza a "
            jump pantalla2

        elif flor_numero ==2:
            "Septem mira con horror la zona donde estaba la flor."
            "Más no comenta palabra alguna."
            jump pantalla2

        else:
            "........."
            jump pantalla2


    label pez:
        scene septem_jardin_pez with dissolve
        septem "..."
        "Septem mira los peces en silencio."
        septem "Me gustaría tener más cosas en mi jardín..."
        septem "Entidades vivas... no simplemente energía."
        "No comenta nada después de eso. Ambos observan las pequeñas figuras de energía en silencio."
        jump pantalla2


    label place:
        scene septem_jardin_place with dissolve
        septem "..."
        septem "En otra ocasión iremos allá."
        septem "Hoy no..."
        septem "No quiero ir allá hoy..."
        jump pantalla2

    
    label cuerpo:
        scene septem_jardin_salir
        "Septem toma aire, soltando todo el estrés acumulado."
        septem "Ya me encuentro mejor"
        septem "¿Quieres volver al templo?"
        menu:
            "Sí.":
                septem "Okay..."
                jump continuacion2
            
            "Espera...":
                jump pantalla2
    return



label interactuar3:

    "Septem junta ambas manos y recita unas palabras en latín."
    scene blanco with dissolve
    "Al terminas su cántico ambos se transportan a un lugar puro, manchado solamente por ustedes dos."
    septem "Venir aquí siempre me calma."
    "Dice al aire, no esperando a obtener una respuesta tuya, Septem hace una señal con las manos."
    "Una esfera del tamaño de una pelota comienzan a emerger del suelo, levitando hasta estar al frente de tu campo de visión."
    "A esa se le suman dos, luego tres. Hasta tener 8 esferas rodeando tu espacio y el de Septem."
    septem "Puedes tocarlas si deseas."



    label pantalla3:
        scene mundus with dissolve
        call screen tocarpantalla3 


    label sol:
        scene mundus1 with dissolve
        septem "Ese es el dominio del Sol, Unum ahora mismo está en la residencia de sus 'esposas'."
        "Septem apunta a la estrella de ocho puntas de color rojo, la cual está al lado de tres estrellas más pequeñas."
        septem "El resto---"
        "Septem mueve su dedo a las otras estrellas que se reparten en el resto de la esfera, son un montón."
        septem "Son sus súbditos."
        jump pantalla3


    label estrella:
        scene mundus2 with dissolve
        septem "Aquí reside Duae..."
        septem "Siempre está trabajando, entrenando a sus estrellas."
        septem "Ahí está ella."
        "Septem guia tu mano con la suya, en búsqueda de Duae. Te das cuenta de que ella es la estrella de ocho puntas más grande de la zona."
        septem "Es uno de los pocos dominios que aún no presenta problemas."
        septem "Y todo el mérito lo tiene ella."
        jump pantalla3

    
    label luna:
        scene mundus4 with dissolve
        septem "Este es Quattor..."
        septem "Es uno de los dominios más bellos."
        jump pantalla3


    label planta:
        scene mundus3 with dissolve
        septem "Es un dominio muerto."
        septem "No queda mucho de él.."
        septem "Y Tria no puede hacer nada hasta que el Jardín mejore."
        septem "Hemos hablado, y luego de mucho buscar, Tria asumió que la maldición es autoimpuesta."
        septem "La maldición seguirá hasta que ella sane."
        menu:
            "¿Qué maldición?":
                pass
        "Septem te observa en silencio antes de contestar."
        septem "Todo fruto producido en el Jardín contiene un veneno y le pertenece a Tria."
        septem "No pueden ser comidos a menos que rompas su sello."
        "..."
        "Sientes un poco de pena por la situación. Supones que ella no puede controlar su pena o rabia, entonces su estado emocional afecta a su dominio de esta manera."
        "Que complicado. Ahora ves que el Jardín no tiene un solo problema."
        "Sino que es un cúmulo de cosas que se entrelazan y afectan tanto a nivel micro como macro." 
        "El Jardín es como si de un cuerpo enfermo se tratase, del cual sus partes vitales hacen lo que pueden para mantenerlo con vida... agonizando."
        "Pero esa defensa no es suficiente. Necesitan ayuda de un agente externo."
        "Una medicina, una píldora que les de lo justo y necesario para volver a retomar sus funciones."
        jump pantalla3

    label animales:
        scene mundus5 with dissolve
        "En esta esfera, hay dos estrellas de ocho puntas."
        septem "A Quinque le hace falta ayuda... por eso Tria pasa la mayor parte del tiempo ahí."
        septem "Cada vez que vengo, lo veo sanando a algún animal."
        septem "La maldición de Tria no se detendrá."
        jump pantalla3

    label humanos:
        scene mundus6 with dissolve
        septem "..."
        "Hay solo una estrella en esta esfera..."
        "No brilla tanto como las demás, y tiene un pulso lento."
        "Se ve fatal."
        "Y Septem no dice nada, solo la mira en silencio. Con una expresión que parece querer romperse en pedazos."
        "Es pena."

        jump pantalla3

    
    label septimo:
        scene mundus7 with dissolve
        "Este es el dominio de Septem, si te fijas bien, no hay rastro alguno de súbditos."
        "Solamente tu alma y la de Septem se encuentran dentro del dominio."
        septem "Estos somos nosotros."
        menu: 
            "¿Dónde está Rafael?":
                septem "No es un súbdito."
                septem "Según el mapa el no existe."
                septem "Según las reglas... el no debería existir aquí."
        "Septem suspira, agotado."
        septem "¿Creo que ya es suficiente, quieres volver?"
        menu:
            "Sí...":
                septem "Okay..."
                jump continuacion3
            
            "Wait...":
                jump pantalla3
    
    label vacio:
        "Es momento de parar. Pero..."
        "No puedes evitar darte cuenta del negro voraz que sostiene las esferas." 
        "Cuando posas tu mano encima de ella, la energía que transmite es abismal."
        "Te llama a meter tu mano dentro, te susurra palabras que sin aun reconocer el idioma, entiendes a la perfección lo que te dicen..."
        "Entra... Entra... Entra..."
        septem "Bien, eso es todo por hoy."
        menu:
            "¿Qué? ¡no!":
                "Le dices que quieres seguir viendo los dominios."
                "Y septem te deja."
                jump pantalla3
            
            "Está bien...":
                jump continuacion3

    return



label interactuar5:

    scene carta_comida with dissolve
    "..."
    "No eres capaz de leer nada de lo que dice debajo de las imágenes."
    nulla "No te procupes cariño, yo te ayudaré <3"
    nulla "Pincha lo que quieras y yo te diré que trae cada cosa."



    label pantalla5:
        call screen tocarpantalla5
        


    label pastel:
        nulla "Oh~~~~"
        nulla "Eso es un cheesecake de Frambuesa."
        nulla "Es muy dulce y rico."
        nulla "¿Quieres pedir eso?"
        menu: 
            "Quiero ver otras opciones...":
                nulla "¡Okay!"
                jump pantalla5
            
            "Sí.":
                nulla "Aja ja~~ Creo que te voy a copiar."
                nulla "Se me antoja algo dulce."
                jump continuacion_nulla1


    label carne:
        nulla "Eso se ve rico."
        nulla "Es osobuco de vacuno."
        nulla "No quiero alardear, pero es uno de los platos que más sabrosos me quedan."
        nulla "Cien porciento recomendado."
        nulla "¿Quieres pedir eso?"
        menu:
            "Quiero ver otras opciones...":
                nulla "¡Okay!"
                jump pantalla5
            
            "Sí.":
                nulla "Okay..."
                nulla "Para mí, se me antoja algo dulce."
                nulla "Voy a pedir el cheesecake."
                jump continuacion_nulla1

        
    
    label pasta:
        nulla "Mmmm~"
        nulla "Pasta boloñesa."
        nulla "Tiene carne picada, cebolla, ajo, tomate y un poco de vino."
        nulla "Es una de mis comidas reconfortantes..."
        nulla "rica y fácil de hacer."
        nulla "¿Quieres pedir eso?"
        menu:
            "Quiero ver otras opciones...":
                nulla "¡Okay!"
                jump pantalla5
            
            "Sí.":
                nulla "Okay..."
                nulla "Para mí, se me antoja algo dulce."
                nulla "Voy a pedir el cheesecake."
                jump continuacion_nulla1
        
        jump pantalla5
    
    label salmon:
        nulla "Ahhh, salmón ahumado."
        nulla "Es rico--- le copié la receta a Rafael una vez y jamás la solté."
        nulla "Haha..."
        nulla "..."
        nulla "¿Quieres pedir eso?"
        menu:
            "Quiero ver otras opciones...":
                nulla "¡Okay!"
                jump pantalla5
            
            "Sí.":
                nulla "Okay..."
                nulla "Para mí, se me antoja algo dulce."
                nulla "Voy a pedir el cheesecake."
                jump continuacion_nulla1
        









screen pastel_minijuego():
    tag pastel
    add "tartaleta_septem.jpg"
    
    imagebutton:
        idle "septem_stop2_idle.png"
        hover "septem_stop2_hover.png"
        action Return(True)
        xpos 0.02
        ypos 0.02
    draggroup:
        drag:
            drag_name "frambuesa"
            child "frambuesa.png"
            draggable True
            droppable False
            xpos 1600 ypos 190

        drag:
            drag_name "frambuesa1"
            child "frambuesa.png"
            draggable True
            droppable False
            xpos 1650 ypos 220

        drag:
            drag_name "frambuesa2"
            child "frambuesa.png"
            draggable True
            droppable False
            xpos 1680 ypos 230

        drag:
            drag_name "frambuesa3"
            child "frambuesa.png"
            draggable True
            droppable False
            xpos 1700 ypos 220
        
        drag:
            drag_name "frambuesa4"
            child "frambuesa.png"
            draggable True
            droppable False
            xpos 1710 ypos 235

       
        drag:
            drag_name "arandano"
            child "arandano.png"
            draggable True
            droppable False
            xpos 1630 ypos 500

        drag:
            drag_name "arandano1"
            child "arandano.png"
            draggable True
            droppable False
            xpos 1650 ypos 480

        drag:
            drag_name "arandano2"
            child "arandano.png"
            draggable True
            droppable False
            xpos 1680 ypos 520

        
        drag:
            drag_name "arandano3"
            child "arandano.png"
            draggable True
            droppable False
            xpos 1680 ypos 530

        # Moras
        drag:
            drag_name "mora"
            child "mora.png"
            draggable True
            droppable False
            xpos 1640 ypos 720
        drag:
            drag_name "mora1"
            child "mora.png"
            draggable True
            droppable False
            xpos 1660 ypos 720

        drag:
            drag_name "mora2"
            child "mora.png"
            draggable True
            droppable False
            xpos 1680 ypos 725

        
        drag:
            drag_name "mora3"
            child "mora.png"
            draggable True
            droppable False
            xpos 1700 ypos 725
return















label septem_corazon:
    scene blanco with dissolve
    "El mundo se disuelve en un blanco puro aterrador."
    "Apareces allí: un espacio sin bordes o suelo. Solo tú y él comparten este espacio."
    scene septem_regalo1 with dissolve
    "Septem se acerca con una calma que te pone nervioso, no puedes evitar recordar experiencias pasadas. Y con dos dedos toma tu mandíbula."
    "En un inicio, lo hace con un gesto delicado... pero de a poco empieza a apretar, sus ojos se centran en cómo tu piel se deforma gracias a la presión."
    scene septem_regalo
    septem "Eres interesante."
    "Su rostro se inclina hacia tu oído. El calor de su aliento te hace estremecer."
    septem "Ah--- Extrañaba hacer esto..."
    scene blanco with vpunch
    "Por un momento, piensas que va a besarte el cuello... pero en lugar de eso, su mano se sella allí y te levanta sin esfuerzo."
    "Quedas suspendido, sus dedos presionando justo donde el aire debería pasar y ahora no puede."
    "Te observa mientras te ahogas, su sonrisa amplia y ojos llenos de euforia."
    septem "Creo que darte terminaciones nerviosas y un cuerpo divino que pretende ser mortal... fue mi mejor idea. ¿No lo crees?"
    "Tu cuerpo tiembla. Un gemido ahogado se escapa de tus labios, haciendo que Septem suelte una risa baja y larga."
    "Su otra mano viaja hasta tu muslo. Ahí, te agarra con firmeza, con sus uñas hundiéndose y rasgando toda la piel que encuentra."
    septem "Mmm~ Creo que me aburrí de jugar con tus manos. ¿Y si pruebo con una pierna? Podría arrancarla. O romperla."
    septem "Habría tanta sangre..."
    "De pronto, te suelta."
    scene septem_corazon1 with dissolve
    "Caes sobre su trasero. Toses y jadeas buscando aire y estabilidad, pero él ya está sobre ti otra vez."
    septem "¿Sabías que hay una arteria en tu muslo llamada femoral? Si la corto, te desangrarías en minutos."
    septem "Pero no morirías de inmediato..."
    "Su voz se suaviza."
    septem "Podría cortarte y mirar mientras pasa. O..."
    "Levanta una mano, y sin tocarte, la acerca a tu pecho."
    septem "Podría simplemente tomar tu corazón y probarlo aquí mismo."
    "Aún no te ha tocado, y sin embargo lo sientes: sus dedos atravesando tus costillas, enroscándose alrededor de tus pulmones para descubrir tu corazón."
    septem "Sería más íntimo así... ¿no lo crees?"
    "Septem se detiene justo ahí. Te observa de cerca, como si esperara que llores, que supliques."
    "Como si ansiara oírte decir que no. Porque entonces podría burlarse de ti. Llamarte gallina."
    "Su sonrisa se curva dulcemente."
    septem "¿Me darás tu corazón? Después de todo, yo fui quien lo construyó... Me pertenece."

    menu:
        "Ya no quiero esto.":
            "Septem sonríe con burla, como si ya esperara esa reacción por parte tuya."
            septem "Okay."
            septem "Eso fue todo entonces."
            "Septem intenta calmar su respiración mientras se para y ofrete una mano. Espera a que la tomes."
            scene blanco with dissolve
            septem "Lo he disfrutado..."
            septem "Gracias."
            return

        "Sí...":
            "Septem no se apresura."
            scene septem_corazon2 with dissolve
            "Sus dedos atraviesan tu pecho, rompiendo piel y hueso. Costillas se abren sin mucha dificultad para dejar pasar sus manos."
            "El dolor no tarda en llegar, pero lo que más sientes es la presión: fuerte e invasiva, rozando lo placentero."
            "Sus ojos no se apartan ni un segundo de los tuyos."
            septem "Tu corazón late tan rápido... ¿es por mí?"
            "Lo saca despacio. Aún latiendo. Y lo contempla fascinado antes de llevarlo a sus labios."
            "Le da un beso, casto. Como si fuera algo sagrado. Luego lo lame y lo muerde."
            "Sin pena a mancharse y verse desagradable."
            "Y justo cuando estás a punto de abandonar este mundo, Septem se inclina... y te besa también a ti, en los labios."
            "Un toque suave, casto."
            scene negro with dissolve
            "Y despiertas."
            "Todo está como antes. Tu cuerpo intacto. Tu corazón en su lugar."
            "Pero Septem se ve diferente. Extasiado."
            return

return

#label nulla_icono:
#    "..."
#    "No pasa nada...."
#    "_________"
#    return


label septem_icono:
    $ persistent.septem_icon_clicks += 1
    show blanco with dissolve
    $ persistent.septem_symbol2 = True
    if persistent.septem_icon_clicks == 1: 
        show ojo with dissolve
        septem "...Ah. Lo has apretado."
        septem "Haha."
        septem "Con esto ya puedo llamarte mío."
        septem "Y vas a terminar volviendo siempre a mí."
        menu:
            "¿Qué es este lugar?":
                pass
        septem "Un punto entre líneas temporales, donde puedo hablarte directamente."
        septem "Sin importar dónde estés. Ya te lo he dicho."
        septem "Puedes usarlo cuando lo necesites."
        "El ojo de septem se cierra por un momento."
        septem "Bien, es hora de volver."           

    elif persistent.septem_icon_clicks == 2: 
        show ojo with dissolve
        septem "Haha, ya entiendo."
        septem "Veo que quieres hablar más de esto..."
        menu:
            "¿Qué sientes cuando hago click en el ícono?":
                septem "¿Hmm?"
                septem "Se siente una energía calida."
                septem "Casi relajante."
                septem "Me gusta."

            
            "Quiero quedarme aquí, contigo.":
                septem "..."
                septem "Podríamos hacerlo... pero tenemos cosas que hacer."
                septem "No puedo desperdiciar tu tiempo de esta manera."
                septem "Tal vez en otra oportunidad."

        "Septem suspira."
        septem "Tienes que volver, salvador mío."


    else:  
        show ojo with dissolve
        septem "Otra vez estás aquí... parece que te gusta jugar con mi regalo."
        menu:
            "Me gusta estar contigo.":
                septem "¿Sí?"
                septem "Pues el sentimiento es mutuo, mi querido pequeño Creador."
                septem "Pero es una lastima que no puedo hacer mucho aquí."
                septem "Cuando aprenda a manejar esto mejor..."
                septem "Podremos tener un momento a solas, lejos de todo y todos."
                septem "Pero tengo cosas que hacer..."
                septem "Ven a aquí en otro momento."
                pass
            "Llévame a tu ruta.":
                jump continuacion4  

            "Quiero quedarme aquí.":
                septem "..."
                septem "Entonces así será."
                septem "Podemos quedarnos aquí por un tiempo."
                "Los minutos pasan y se transforman en horas. Septem de vez en cuando te habla de cosas mundanas, o lo que le gustaría hacer el día de mañana."
                "Hay veces en que te confiesa que le gustaría usar su cuerpo para estar aquí, realmente contigo, pero no puede."
                "Dice que debe guardar las energías para cuando el Jardín comience a cambiar."
                "Para cuando vuelvan a tener humanos."
                "..."
                "El tiempo pasa, y Septem, muy a tu pesar, se despide. Se le oye dudoso, como si no quisiera irse."
                "Pero tú poco puedes hacer para prevenirlo."
                "......."
            
            "Volver...":
                pass
    "...................."
    hide ojo with dissolve
    hide blanco with dissolve
    "_______________"

    return

label memorias_cita:
    scene feria with dissolve
    "Nulla medita un poco antes de responder. Mira el lugar con algo que no logras identificar en su totalidad. Es una mezcla entre nostalgia y resignación oculta detrás de capas y capas que sirven como escudo para no desbordarse frente a ti.."
    "Sus ojos inspeccionan las luces colgantes en los puestos, los irreconocibles balbuseos de la gente que, posiblemente no tengan sentido alguno, aqunque les pongas atención. Por un momento, parece que va a decir que no."
    "Hasta que suelta un suspiro largo que ha sido contenido por un largo tiempo ya, y sus ojos vuelven a ti."
    show nullavacio1 with dissolve
    nulla "Está bien."
    nulla "Podemos quedarnos un poco más."
    hide nullavacio1 with dissolve
    "Pasan el tiempo recorriendo la feria y sus puestos, sin rumbo fijo. Nulla camina a tu lado, atento. Pero no de su alrededor, sino que de ti."
    "Toda su atención está sobre tu persona, y te aterra lo poco que le interesa su alrededor."
    "Compra un par de dulces para compartir, aunque al final es él quien se los termina casi todos. Cada bocado lo prueba como si fuese la primera vez, con hambre de más."
    "Observas cómo mastica con lentitud, saboreando cada minimo detalle."
    "Te ofrece un pedazo con una gran sonrisa. Tienes que negarle su oferta... tu estómago no puede más."
    "En cambio, él no parece llenarse nunca. Es un pozo sin fondo."
    "Y estás seguro que no solo se trata de comida."
    "Nulla, en cuerpo y alma es un ser sin fondo, al cual nunca podrás conocer realmente."
    "No sabes si eso es bueno... o no."
    el "¡¡¡¡{glitch=20.0}{color=ffffff}{b}|||||||||||{/glitch}!!!"

    stop music fadeout 0.5
    "Una voz estridente corta la música. La multitud se detiene al instante, congelada en medio el tiempo y espacio."
    "Nulla alza la vista, atento, buscando entre la masa que ahora los observa directamente. Cientos de rostros inmóviles, todos con los ojos abiertos hasta parecer que saldrán de sus cuencas en cualquier momento."
    "Algo no está bien."
    "No puedes apartar la mirada de esas personas, hay algo que te lo impide. Tienes la certeza de que si lo haces, algo peor ocurrirá."
    "Pero necesitas ver a Nulla. Necesitas hablarle. Así que te obligas a despegar la mirada de los demás cuerpos."
    "Él también parece atrapado. No del todo presente. Su cuerpo se rodea de líneas, cada vez más. Una sustancia oscura comienza a subir desde sus pies, cubriéndolo lentamente."
    "Avanza con lentitud, pero no se detiene."
    "Y tú sabes lo que eso significa. Al menos, lo intuyes."

    menu:
        "Nulla, tenemos que irnos.":
            "Te aferras a su ropa con fuerza, intentando hacerlo volver en si. Le suplicas con insistencia."
            "Tus palabras finalmente lo alcanzan. Sus ojos se mueven, te buscan."
            "Pero algo en ellos no está del todo ahí. La claridad que suele tener, su energía pícara... se han esfumado."
            "Le dices todo lo que se te viene a la cabeza. Que no puede quedarse aquí. Que este lugar lo está consumiendo. Que no es real. Que tú estás con él, que no tiene que quedarse atrapado."
            "Le hablas de la misión. De su propósito. De lo que aún queda por hacer."
            "Necesitas que Nulla te escuche."
            "Que realmente te escuche y te haga caso."
            "Aunque sea una vez."

            if amor_nulla >= 5:
                nulla "..."
                nulla "...Tienes razón."
                nulla "Tenemos que seguir con el día."
                nulla "Tu cuerpo debe estar cansado."

                return
            else:
                "Nulla no te escucha."
                "Murmura algo como: 'Ahora no, [nombrejugador]'. Y eso es todo lo que obtienes."
                jump memorias_neo

        "No decir nada.":
            "Es mejor así. No quieres arriesgar a que el mundo y Nulla sean destruidos al final del juego."
            "Confías en que guardar silencio ahora es lo correcto."
            "Confías en el otro método que mencionó el otro Nulla."

            jump memorias_neo
    return


label memorias_neo:
    el "¡¡¡¡{glitch=20.0}{color=ffffff}{b}N|||E||||||O||{/glitch}!!!"
    scene feria with vpunch
    show vacio
    pause 0.5
    show vacio2
    pause 0.5
    show vacio3
    play music "audio/meeting.mp3" fadein 2.0 volume 0.3
    "El cuerpo de Nulla se deforma mientras convulsiona, al igual que el tuyo."
    "Sientes cómo tu forma comienza a deshacerse por dentro, un ácido que quema y elimina todo a su paso desde el fondo de tu ser."
    "Tu cuerpo se rompe. Aunque, tu conciencia se mantiene intacta."
    "Tu visión no flaquea ni se torna borrosa. Aún sigues aquí."
    "..."
    "Estás completamente despierto. Tu mente se aferra a cada segundo de lo que está pasando, no se te permite salir de este mundo."
    "No quieres hacerlo, y algo externo te está ayudando a ello..."
    "Algo sostiene las piezas de tu cuerpo, manteniendo todo en su lugar."
    "Y no es Nulla..."
    scene negro with pixellate
    "Ves cómo Nulla es engullido por la masa negra. Su cuerpo pierde la forma y se consume por completo."
    scene charco with pixellate
    "Y entonces, frente a ti, solo queda el blanco más puro... interrumpido por un charco oscuro que sisea, vivo y grotesco. Su textura recuerda al alquitrán: espeso; viscoso; con una densidad que parece contagiar y proclamar como suyo todo lo que toca."
    "La superficie burbujea. Algo dentro se agita."
    "Está buscando forma."
    "Se retuerce y salpica."
    "{glitch=20.0}{color=ffffff}{b}Por fin te tengo. AJAJAJAJAJAJAJAJAJAAAAAAAAAAAAAAAAAAAAAAA.{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}QUÉ FÁCIL FUE ESTO AAAAAAAAAAAAAAAAJJA---{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}Gracias, mi vida~~~~~{/glitch}"
    hide charco
    show charco2
    "El charco se expande, trepando sobre sí mismo buscando altura. Hilos se desprenden de la masa, elevándose y entrelazándose en una danza caótica."
    "No puedes seguir cada hebra. Son demasiadas. Pero entiendes que están construyendo algo."
    "Una forma."
    "Algo que puede mirarte de vuelta."
    "Un cuerpo."
    hide charco2
    show charco3
    "Una entidad emerge de esa mezcla. Muta hasta conseguir una imagen."
    "¿Es Nulla...?"
    scene charco4
    "{glitch=20.0}{color=ffffff}{b}Y dale con confundirme con ese gil.{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}Abre bien los ojos, y piensa un poquito más ¿Quieres?{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}No es tan difícil la verdad.{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}Pero creo que pido mucho. No se puede esperar más de alguien quien pierde su tiempo en estos patéticos juegos de pacotilla.{/glitch}"
    "{glitch=20.0}{color=ffffff}{b}---Que se conforma con esta cosa mal escrita... lamentable{/glitch}"
    "No... este no es Nulla..."
    "No exactamente."
    "La figura se acerca a ti y abre la boca."
    
    scene fragmentado_ojos with dissolve
    show neo2risa with dissolve
    neo "Nos vemos de nuevo."
    menu:
        "¿Dónde está Nulla?":
            hide neo2risa
            show neo1risa
            neo "Mhhhh. Me lo comí."
            neo "Sorryyyy."
        
        "¿Quién te crees para hablarme así?":
            hide neo2risa
            show neo1risa
            neo "PFffff JAJAJAjaaa."
            neo "¿Enserio te vas a enojar por algo que dice una imagen en tu pantalla?"
            neo "Nahhh."
            neo "No te lo tomes tan a pecho."
            hide neo1risa
            show neo1normal
            neo "Si no te gusta puedes salir de aquí."
            neo "Nadie te obliga a estar aquí."
            neo "Pero si te quedai' puedo entretenerte un rato mientras hago lo que necesito hacer."
            hide neo1normal
            show neo1risa
            neo "¿Qué te parece, eh?"
        
        "¿Sigue en pie el trato?":
            hide neo2risa
            show neo1risa
            neo "Perooo claroooo, cielitooo."
            neo "Aunque creo que omití algunas cosas..."
            "Esperas a que Neo te explique pero él solo sonríe."
            "Y entiendes que no te va a explicar nada más."
    
    
    "No puede ser...." 
    "Necesitas hacer algo ahora."
    "Necesitas a Nulla de vuelta."   
    menu:
    
        "Neo...":
            "Tu cuerpo comienza a vibrar, intentando romperse y fallando en el intento."
            "No se te permite romper este recipiente, lo más probable es que Neo sea el causante de esto."
            "Él te mira con gracia, como si lo que has apretado fuera lo más gracioso que ha escuchado en un largo tiempo."
            scene neo_closeup1 with pixellate
            "Te toma desprevenido ver como sus manos se posan en su cuello, apretando con fuerza haciendo que su respiración se acelere como si le faltase el aire."
            "Aunque su sonrisa cruel jamás deja su cara."
            "..."
            scene neo_closeup2
            "Entre respiraciones entrecortadas y movimientos bruscos, que ponen dramatismo a su interpretación, te das cuenta de lo que realmente está haciendo."
            scene neo_closeup3
            "Se está burlando."
            show neo_closeup 
            neo "Eres imbécil..."
            "Neo deja de actuar, sus manos sueltan su cuello para caer en su costado, similar a un peso muerto."
            neo "Eso no funciona aquí conmigo..."
            neo "Nulla---"
            neo "Ya no estará aquí hasta que logres salir de aquí."
            neo "Y eso no va a pasar."
    scene blanco with dissolve
    "Neo acomoda su corbata, tomándose un buen tiempo en hacerlo. Es como si realmente no le importa lo más mínimo lo que está pasando."
    "Observa su alrededor con curiosidad genuina, algo interesante deben ver sus ojos que los tuyos no logran apreciar. Sus pasos emiten un eco ensordecedor, que retumba en tus oídos y no sale de tu cabeza hasta conseguir marearte." 
    "Su atención se posa en ti nuevamente. Te rodea, inspeccionando tu cuerpo de pies a cabeza."
    "Decir que parece un depredador sería no darle el crédito suficiente que se merece. Los depredadores tienen que poner de su esfuerzo para cazar y comer su presa." 
    "Él no."
    "No... él se mueve como un faenador inspeccionando a su próxima víctima. Tranquilo, ya sabiendo qué hará con su premio, una presa regordeta e incapaz de huir."
    neo "No eres la gran cosa."
    "{glitch=20.0}{color=ffffff}{b}Y no estoy hablando de la marioneta, querida persona de gustos cuestionables.{/glitch}"
    "................."
    show neo_closeup
    neo "Detrás de esa pantalla eres solo una cara pasajera, un ojo de los tantos que me validan la existencia."
    neo "No un ser superior como los demás quieren creer."
    neo "Jaja."
    neo "¿Te gusta sentirte especial jugando a estas cosas? --- ¿Te llena algún vacío que tienes por ahí?"
    neo "Patéticoooo."
    neo "Temo decirte que no lo eres, mi vida~."
    neo "Pero me das algo de pena--- Así que podemos hacer algo al respecto."
    neo "Puedo hacerte sentir especial."
    neo "Puedo fingir exactamente como lo hace Nulla cuando está contigo."
    
    hide neo_closeup with dissolve
    show neo_closeup3
    "..."
    hide neo_closeup3 
    scene neo_closeup 
    neo "Puedo tomarte las manos y besar tu cara, mientras te digo 'mi vida'. Y te tendría en la palma de mi mano."
    neo "Justo cómo lo hace Nulla para obtener todo lo que quiere de ti."
    neo "Y luego desecharte, como basura."
    neo "Aunque---- Hmmmmm, yo lo haría con menos drama y lloriqueos innecesarios."
    
    scene blanco
    show vacio
    pause 0.10
    show vacio2
    pause 0.10
    show vacio3
    pause 0.10
    show negro
    neo "Bueno, YA! basta de este monólogo de mierda, que ya parezco villano de serie infantil."
    neo "Creo que ya entiendes como va la cosa."
    neo "A menos que necesites que te explique con manzanas y peras."
    "Neo te agarra del brazo y te jala hacia él. Su agarre duele."
    neo "Vamos a hundirnos más en este pozo."
    neo "Ella debe estar por ahí."
    neo "Suprimida."
    neo "Y tu serás mi llave desechable~~~"
    "_________________________________________"
    jump rutaneo

return    




        





    
    
                    






image araña_hilo = "arana_hilo.png"
default araña_activa = False


transform bajada:
    ypos -0.3    
    linear 3.0 ypos 0.0


#image araña_bajando:
#    "arana_hilo"
#    xpos 0.95   # cerca de la esquina superior derecha
#    ypos -0.5   # empieza más arriba de la pantalla (fuera de vista)
#    linear 3.0 ypos 0.5   # en 3 segundos baja hasta cierta altura
#    pause 999.0            # se queda allí hasta que desaparezca



screen screen_araña():
    if araña_activa:
        text "{color=#ff0000}Hay una araña en tu pantalla, búscala y espántala.\nThere's a spider on your screen, find it and scare it away.{/color}" xpos 0.5 ypos 0.1 xanchor 0.5

        # el botón usa la animación en vez de la imagen fija
    imagebutton:
        idle "arana_hilo"
        hover "arana_hilo2"
        action Jump("hada")



label hada:
    $ araña_activa = False
    hide screen screen_araña
    "Tocas la araña, pero..."
    show blanco with dissolve
    "Sin que puedas prepararte mentalmente, eres transportado a otro lugar." 
    "Tienes la leve sensación de estar cayendo, y luego dejas de hacerlo... raro. Agradeces la falta de cuerpo, pues estas seguro de que hubieras caído de rodillas al suelo."
    show hada_enojo with dissolve
    hada "¿Uh?"
    hada "....¿Que hago aquí?"
    "La entidad mira el lugar con sospecha, luego a ti."
    hada "Tú."
    "Toda su atención está en ti, se acerca a paso lento y te mira desde arriba... es muy alto, lo que te fuerza a ajustar tu postura para poder apreciar bien su expresion."
    hada "¿Tú eres el responsable de esto?"

    menu:
        "No...":
            "Le explicas que no sabes lo que ha pasado, que de un momento a otro una araña ha caído de la pantalla y tú la has intentado espantar."
            "La entidad te mira incrédulo."
        
        "Sí...":
            hada "Hmmm."

    "Te inspecciona por unos segundos más, midiendo tu sinceridad." 
    hide hada_enojo
    show hada_normal
    "Luego su expresión cambia; ahora te mira con interés, pupilas dilatadas y ojos entrecerrados acompañados con una sonrisa confiada--- casi como si te deseara en secreto."
    hide hada_normal
    show hada_hablando
    hada "Tu alma... irradia una luz exquisita."
    hada "Pero se encuentra atrapada en ese ojo. Tal vez si yo..."
    hide hada_hablando
    show hada_normal
    hada "..."
    hada "Dime. ¿Dónde está tu cuerpo?"
    
    "Le explicas, no te cuesta mucho resumir todo lo que te ha sucedido hasta ahora. Un factor de ello es él... quien te escucha atentamente y te invita a seguir."
    "Aplicando la escucha activa, de la cual tu caes redondito."
    "LLega el momento en que tu monólogo se transforma en una conversación genuina, dónde tanto tú como él hacen preguntas de uno al otro."
    "Descubres que él pertenece a otra dimensión: es un guardián de la gente, mandado por su amo, Dios."
    "Sus alas son una prueba de ello."
    "Y quieres preguntar..."
    "Necesitas preguntar..."
    "..."
    menu:
        "Tus alas...":
            hide hada_normal
            show hada_enojo
            "Tu acompañante funce el ceño, pero recobra la compostura al instante, para luego mitarte fijamente."
            hide hada_enojo
            show hada_hablando
            hada "He pagado el precio por proteger a los humanos, pero es su voluntad y yo soy su siervo."
            "Dice con solemnidad."
        
        "Ese broche...":
            hide hada_normal
            show hada_hablando
            hada "Ah, esto."
            hada "Lo obtuve del ojo de una bestia devora hombres."
            hada "Si no fuera por mí, mucha gente habría muerto."
            "Su mano viaja al broche y lo aprieta con orgullo."

    hada "Mi turno."
    hada "Si entendí bien, tienes la habilidad de viajar en el tiempo... o algo parecido ¿no?"
    hada "Viajar entre lineas de tiempo..."
    hada "Cambiar el pasado o el futuro..."
    hide hada_hablando        
    show hada_enojo
    hada "Dime. ¿Es eso lo que puedes hacer?"
    menu:
        "Sí.":
            hide hada_enojo
            show hada_normal
            "La entidad suspira, soltando una risa."
            hide hada_normal
            show hada_hablando
            hada "¿De verdad? Impecable."
            hada "Eres, increíble."
        
        "No.":
            hada "Ah..."
            hada "Tal vez no lo has descubierto aún."
    hide hada_enojo with dissolve
    hide hada_hablando wiht dissolve
    scene blanco
    show mano with moveinright
    "Hada está a punto de decir algo cuando dos manos gigantes lo toman con cuidado, y antes de que él pueda hacer algo, las manos lo envuelven, haciéndolo desaparecer del lugar."
    hide mano with moveinright
    show ojito_mirando with dissolve
    el "Oh... nonono."
    el "¡Casi te lleva!"
    el "¡Casi te come!"
    el "¡¡¡¡Además!!!!"
    el "¡No podemos hacer esto sin permiso! Este personaje no es de mi propiedad."   
    "Hay un ojo extraño en la zona, el cual no parece estar pendiente tuyo."
    "Se mueve de un lado a otro, paseándose por la zona."
    el "................"
    hide ojito_mirando
    show ojito_decepcionado
    el "Uh.........."
    el "Ya veo."
    el "Al final {b}ELLA{/b} lo puso a la fuerza sin mi permiso, solo espero que haya consultado a la autora y dueña de él para ponerlo aquí..."
    el "No quiero decepcionar a Cinco."
    el "UHHHHGGG---"
    el "Al final {b}ELLA{/b} siempre hace lo que quiere, y no le importa mi guion."
    el "..."
    el "Genial."
    "El ojo deja de moverse y se esfuma como espuma siendo soplada. Para reaparecer frente a ti."
    hide ojito_decepcionado
    show ojito_mirando
    el "Ah."
    hide ojito_mirando
    show ojito_feliz
    el "¡[nombrejugador]!"
    menu:
        "¿Padre?...":
            pass

    el "Bienvenido al espacio donde todo se interconecta."
    el "Tengo dos opciones para ti."
    el "Podemos hacer como que esto nunca pasó o..."
    el "Puedes quedarte un tiempo más aquí."
    el "¿Qué prefieres?"
    menu:
        "Quedarme.":
            jump clave

        
        "Irme.":
            hide ojito_feliz
            show ojito_decepcionado
            el "Okay, tú te lo pierdes."
            el "Volverás al jardín junto con Septem."
            el "No tienes permitido mencionar nada de lo que pasó aquí. \n{size=*0.7} Tampoco es como que te voy a dar una opción para hacerlo~{/size}"
            hide ojito_decepcionado
            jump mini_continuacion


        


label clave:
    hide ojito_feliz
    show ojito_mirando
    creador "¡Bien!"
    scene intra_me_mundus with pixellate
    creador "Aquí estamos."
    creador "Bienvenido a mi hogar."
    "La extraña entidad te rodea con entusiasmo mientras entrecierra su ojo, no lo quieres admitir en voz alta, pero se ve tierno."
    creador "Aquí paso la mayor parte del tiempo y es el único lugar que no puedo cambiar."
    creador "Pero me gusta, es lindo y tiene mucho espacio."
    hide ojito_mirando
    show ojito_feliz
    creador "¡Además! Cambia de color dependiendo de lo que ella y yo hagamos."
    creador "Ah---"
    creador "Se siente bien tener un invitado."
    creador "Ah espera."
    hide ojito_feliz with dissolve
    "A la entidad se le suman unas dos manos, y comienzas a flotar a tu alrededor, buscando por dónde tomarte."
    "Una de ellas te agarra el ojo y lo aprieta levemente. La otra chasquea sus dedos. A partir de ello, tanto tú, él y la zona cambian."
    "De la nada se crea un cuerpo para que tú lo puedas controlar y habitar. Cuando sientes que tienes control sobre él, te das cuenta de que estás sentada en una mesita con tazas y dulces repartidos en pequeños platos."
    "Todo muy bien decorado."
    scene hello with dissolve
    "Y él está frente tuya, mirándote de pies a cabeza."
    "Está tan cerca..."
    creador "Vaya...."
    scene sweetheart 
    creador "Si que eres adorable."
    creador "Bueno, eso ya lo sabía jaja. Te he estado viendo desde un inicio."
    creador "Tus reacciones me encantan."
    creador "Supongo que puedo entender a Nulla en esto."
    creador "Eres adictivo."
    creador "<3"
    "Padre toma distancia de ti, y su atención se enfoca en sí mismo."
    scene intra_me_mundus with dissolve
    show musaerisa with dissolve
    creador "Ahhh~ Esta forma me gusta mucho."
    creador "¿Sabías que lo hicieron para mí y me dejaron usarlo?"
    creador "Es un diseño que mi querida Cinco ha realizado."
    creador "..."
    creador "Tengo que agradecerle a Cinco cuando la vea---"
    hide musaerisa
    show musaenormal
    creador "Bueno..."
    creador "Tengo algo para darte, pero vamos a jugar un juego."
    creador "Escondí la respuesta en la web, en un lugar que se usa para escribir y subir historias de tus series favoritas."
    creador "Dime, [nombrejugador]"
    hide musaenormal
    show musaerisa
    creador "¿Cúal es la palabra secreta?"
    creador "Si has leído el relato que escribí, supongo que ya sabes lo que es."
    menu:
        "...¿Un relato?":
            hide musaerisa
            show musaenojo
            creador "Creo que también se le llama fanfic comunmente."
            creador "...Hmm..."
            creador "¿No lo has leído?"
            creador "...."
            hide musaenojo
            show musaerisa
            creador "BAHAHAHAHA, entonces supongo que puedes buscar mi nombre en los archivos."
            creador "O puede ser que ya lo sepas porque se ha filtrado.... o {b}ella misma{/b} lo haya dicho por ahí... uhhhhg {b}ella{/b} y su gran bocota."
            creador "JAJAJAJAJAJA, increíble."
        
        "Sí...":
            pass




    creador "Entonces, ¿cuál es la palabra secreta?"
label clave2:

    $ passwd = renpy.input(_("Introduce su nombre:"))
    $ passwd = passwd.strip()

    if passwd.lower() == "musae":
        jump musae_cita
    else:
        hide musaerisa
        show musaenojo
        creador "Ese no es mi nombre..."
        hide musaenojo
        show musaerisa
        creador "Mmmm, ¿quieres volver a intentar?"
        menu:
            "Volver a intentar":
                jump clave2

            "Rendirse":
                hide musaerisa
                show musaenojo
                "Musae suspira."
                creador "Volverás al jardín junto con Septem."
                creador "No tienes permitido mencionar nada de lo que pasó aquí. \n{size=*0.7} Tampoco es como que te voy a dar una opción para hacerlo~{/size}"
                scene jardinseptem with dissolve
                jump mini_continuacion
                

label musae_cita:

    scene regalo_rosa with dissolve
    musae "Bien."
    musae "Aquí está, con todo mi amor."
    "Musae te entrega una rosa azul... es tan bella."
    musae "Se supone que me ayudaste a hacer esto."
    musae "Ambos lo hicimos, como colaboradores... o quién sabe, como amantes."
    menu:
        "Ew...":
            scene intra_me_mundus with dissolve
            show musaenojo with dissolve
            musae "Ja-"
            musae "Una más, y te saco de aquí."
            musae "No voy a perder mi tiempo con alguien así."
        
        "Gracias <3 ~":
            musae "<333333"
            musae "AWWW qué contento me pone saber que te ha gustado."
    hide musaenojo wiht dissolve
    scene intra_me_mundus with dissolve
    
    show musaenormal with dissolve
    musae "Estaba pensando en pasar un tiempo juntos."
    musae "Tomarnos un descanso y conversar."
    musae "Pero voy contra el tiempo..."
    musae "Así que continuaremos esta cita el próximo acto <3 . "
    hide musaenormal with dissolve
    musae "Nos vemos~"



    "........"
    "Caes nuevamente, y en la caída se te despoja del cuerpo que te han prestado..."
    "Al parecer solo era temporal."
    "Una pena."
    scene negro with dissolve
    "Por un segundo tu visión se torna negra."
    "No ves nada, pero eso te ayuda a recordar qué carajos estabas haciendo antes de venir aquí."
    "Estabas en el jardín junto a Septem cuando una araña te cambió los planes."
    "Vaya efecto mariposa."
    scene jardinseptem with dissolve
    jump mini_continuacion

    
#PANTALLAS ACT3
    
#OJO CON EL POPUP!!!!!!,,, ver si funciona en macos/linus 

init python:
    import platform
    import subprocess
    import threading
    import time
    import ctypes

    def popup(texto, titulo="Nulla"):
        sistema = platform.system()
        try:
            if sistema == "Windows":
                ctypes.windll.user32.MessageBoxW(0, texto, titulo, 0)

            elif sistema == "Darwin":
                texto_safe = texto.replace('"', '\\"').replace("\\", "\\\\")
                titulo_safe = titulo.replace('"', '\\"').replace("\\", "\\\\")
                subprocess.run(
                    ["osascript", "-e", f'display dialog "{texto_safe}" with title "{titulo_safe}"'],
                    timeout=30
                )

            elif sistema == "Linux":
                subprocess.run(
                    ["zenity", "--info", f"--title={titulo}", f"--text={texto}"],
                    timeout=30
                )
        except subprocess.TimeoutExpired:
            pass
        except Exception as e:
            renpy.log("popup error: {}".format(e))



    def nulla_spam(delay=1.0):
        
        mensajes = [
            "Me encanta.",
            "Lo amo.",
            "Te adoro.",
            "Eres lo mejor <3",
            "Puede que esto no sea nada para ti. Pero para mí es todo.",
            "<3333",
            "Te amo."
        ]
        mensajes_en = [
        "I love it.",
        "Lo adoro.",
        "I adore you.",
        "You're perfect <3",
        "This might mean nothing to you. But to me it's everything.",
        "<3333",
        "I love you."
    ]

        idioma = renpy.game.preferences.language
        mensajes = mensajes_en if idioma == "ingles" else mensajes



        def secuencia():
            for mensaje in mensajes:
                t = threading.Thread(
                    target=popup,
                    args=(mensaje,),
                    daemon=True  
                )
                t.start()
                time.sleep(delay)

        threading.Thread(target=secuencia, daemon=True).start()





screen tocarpantalla6():
    add "act3_s9_1"
    modal True

    imagebutton auto "septem_boca_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Boca")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("boca")

    
    imagebutton auto "septem_mano_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Mano")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("mano")

    imagebutton auto "septem_stop_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Stop")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("fin")

    imagebutton auto "septem_ojito_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Ojito")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("ojito")
    
    imagebutton auto "septem_corazon_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Corazon")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("corazon")





label interactuar6:

    scene act3_s9  with dissolve
    "Creo que puedes tocarme ahora..."




    label pantalla6:
        call screen tocarpantalla6


    label boca:
        scene blanco
        show act3_s9
        with dissolve
        
        if besito == False:
            septem "¿Mi boca?"
            "Septem arquea las cejas. Hay un tono meloso que sale junto a su pregunta, uno el cual no es completamente sincero, como si estuviera jugando contigo."
            "Se acerca un poco más a ti, hundiendo la cama en el proceso. Tan cerca que sientes el calor de su cuerpo."
            septem "¿Qué es lo que podrías querer de mi boca?"
            "Se toca los labios con las yemas de sus dedos, acariciando lentamente la zona."
            septem "¿Hmm?"
            "Su pregunta es todo menos inocente. Septem finge ingenuidad para ponerte en una posición donde debas explicar tus deseos."
            "Aunque con su actuar no deja entrar ningún tipo de duda con sus intenciones, o hacia dónde quiere llegar con esto. A pesar de estar jugando al tonto y obtener una respuesta clara por parte tuya."
            "Te espera por unos segundos antes de interrumpir nuevamente. No pudiendo evitar provocarte un poquito más, mientras su sonrisa no hace más que crecer."
            septem "Sé que lo has estado esperando."
            septem "¿O he malinterpretado todo?"
            septem "¿Qué es lo que quieres?"
            $ besito = True

            menu:
                "Decir que lo quieres besar.":
                    show act3_s9

                    "Se lo dices, lo suficientemente fuerte como para que él pueda escuchar."
                    septem "¿Qué has dicho?"
                    septem "¿Puedes repetirlo?"
                    menu:
                        "Repetirlo.":
                            $ septemconfianza += 1
                            "Lo repites una vez más, un poco más alto para asegurarte que Septem no vuelva a tomarte el pelo."
                            septem "Hmmm."
                            hide act3_s9
                            show act3_s9_blush
                            "Complacido con tus palabras, las comisuras de sus labios dibujan una sonrisa triunfante."

                        "Mandarlo a la mierda.":
                            hide act3_s9
                            show act3_s9_blush
                            "Septem ríe, gozando con tu frustración."
                
                    hide act3_s9_blush with dissolve

                    "Antes de que puedas enojarte por como Septem te está tratando, él termina de eliminar el espacio que hay entre ustedes."
                    "Una de sus manos toca tu muslo, deslizándose hasta tu cintura, marcando un ritmo lento. Su mano te centra, tranquiliza y conecta con su imponente presencia."
                    "Es un plácido toque que anuncia la llegada de un próximo beso."
                    "Septem te espera, dejando que seas tú quien comience, haciéndose de rogar por ti, sin borrar esa sonrisa petulante que lleva puesta desde que le has hecho saber tus deseos."
                    scene negro with dissolve
                    "Cierras los ojos y eres tú quien busca cerrar el contacto." 
                    "Su beso es suave, seguido por otros más, lentos y cuidadosos, temiendo a no sobrepasarse y tomar de más."
                    "Pero le es dicífil."
                    "Septem no es la deidad más correcta, ni la más recta. Jamás lo fue. Por lo que con un suspiro de tu parte, en medio del beso, lo toma para profundizar el beso."
                    "Hambriento de tu boca, te devora con una insistencia desbordante, como si quisiera dominar todo tu ser."
                    "Sus manos buscan el calor de tu cuerpo, esperando a tener un contacto más cercano de lo que ya tiene. Quiere más, al punto de que temes a que te desgarre la carne en el proceso."
                    "Hay un pensamiento fugaz que pasa por tu mente; que sus dientes no solo busquen tus labios o lengua de forma temporal, y decidan romper la tierna carne de tu cara como trofeo personal."
                    "El solo pensarlo, hace que te retuerzas, sin saber si te aterra o te ilusiona."
                    "La única respuesta clara es que todo es intoxicante, llegando a nublarte el juicio. Su calor, su olor e incluso su corazón, todo lo que te rodea es Septem."
                    "Cuando quedas sin aire, Septem se aleja, mordiendo tu labio en el proceso."
                    scene blanco
                    show act3_s9a
                    with dissolve
                    "..."
                    hide act3_s9a
                    show act3_s9b
                    pause 0.5
                    hide act3_s9b
                    show act3_s9c
                    "Tragas saliva y sientes el sabor metálico en tu lengua."
                    septem "No debí darte tantas características humanas..."
                    "Sus dedos atrapan tus mejillas, provocando que sus labios se abran y muestren el interior de tu boca."
                    "Septem observa la zona, teniendo control total de tu mandíbula para moverla de lado a lado."
                    "Buscando cualquier daño, solo es encuentra con una pequeña herida en el interior de tu labio inferior."
                    septem "Lo bueno es que puedo reconstruir cualquier parte de tu cuerpo si me llego a emocionar de más."
                    "Septem sonríe con picardía."
                    "Luego suspira."
                    hide act3_s9c
                    scene blanco
                    show act3_s9_blush 
                    with dissolve

                    septem "¿Feliz?"
                    septem "¿Será que con solo un beso Mi Creador ha quedado satisfecho?"
                    menu:
                        "No.":
                            pass
                    
                        "Sí.":
                            pass

                    "Septem ríe."
                    septem "Lo suponía."


            
                "Decir que no es lo que él piensa.":
                    show act3_s9_enojo
                    "..."
                    septem "¿Y qué es lo que quieres entonces?..."
                    septem "Mi boca está para complacerte... ya sea con palabras o --- cualquier cosa que estimes conveniente."
                    septem "Supongo que me he equivocado."
                    septem "Mil disculpas."
                    "Septem se aleja un poco, dándote espacio personal y un respiro."

        else:
            septem "No más."
            septem "¿Entendido?"    

        jump pantalla6

    label mano:
        scene act3_s9 
        "Tomas su mano. Es cálida."
        scene act3_s9d
        "Por un tiempo, Septem te permite sostener y entrelazar sus dedos con los tuyos. Posando su mirada en el punto donde ambos conectan."
        "Se siente algo íntimo."
        septem "Estas manos jamás puedan ser una representación perfecta de las tuyas."
        septem "Al menos esto es lo más cercano que tengo de tenerte conmigo."
        septem "Con eso me contento."
        septem "Tu presencia es más que suficiente, Mi Creador."
        scene act3_s9
        jump pantalla6
    
    label ojito:
        scene act3_s9 
        septem "Prefiero mi halo original... pero-"
        septem "Con esto será más fácil cumplir con la petición de Madre."
        septem "Puedo forzarlos a cerrarse para siempre."
        septem "..."
        septem "Si eso es lo que deseas, Mi Creador."
        jump pantalla6

    label corazon:
        scene act3_s9 
        septem "¿Quieres mi corazón?"
        "Uh..."
        septem "Ya es tuyo, pero no tengo ningún problema con arrancármelo y dártelo en tus manos."
        septem "...Quizás otro día."
        septem "No quiero mancharte hoy."
        "Septem toma una pausa para mirarte con detenimiento."
        septem "Los humanos le dan tanta importancia al corazón..."
        septem "Con Rafael entendí el porqué. Es el motor de la vida."
        "Septem coloca la palma de su mano en tu pecho, con la idea de sentir el latir de ambos corazones."
        septem "Contigo le encontré una función."
        septem "Estamos eternamente conectados a través de un solo órgano, que ni a ti ni a mí nos sirve realmente."
        septem "Irónico."
        jump pantalla6

    label fin:
        scene act3_s9
        septem "¿Ya has terminado, Mi Creador?"
        septem "No tendrás otra oportunidad luego."
        menu:
            "Sí, quiero terminar...":
                septem "Está bien..."
                jump acto3_septem_continuacion3
            
            "Espera...":
                jump pantalla6


default persistent.nulla_symbol2 = False
default persistent.nulla_symbol = False
default persistent.nulla_icono_act3 = False

screen nulla_corner_symbol():

    if persistent.nulla_symbol:

        if persistent.nulla_icono_act3:
            imagebutton:
                idle "tuyo_idle.png"
                hover "tuyo_hover.png"
                xpos 0.02
                ypos 0.02
                anchor (0.0, 0.0)
                action Call("nulla_icono")
                tooltip "Nulla quiere hablar contigo..."
                sensitive (not bloquear_iconos)
        else:
            imagebutton:
                idle "dormido_idle.png"
                hover "dormido_hover.png"
                xpos 0.02
                ypos 0.02
                anchor (0.0, 0.0)
                action Call("nulla_icono")
                tooltip "Nulla quiere hablar contigo..."
                sensitive (not bloquear_iconos)


        
#EDITAR

label nulla_icono:
    
    $ persistent.nulla_symbol2 = True
    if persistent.nulla_icono_act3:
        $ persistent.nulla_icon_clicks += 1
        if persistent.nulla_icon_clicks == 1:
            scene fragmentado_ojos with pixellate
            play music "audio/ruidoblanco.mp3" fadeout 1.0 fadein 3.5 volume 0.5
            centered "Hola mi vida"
            centered "Me tomó un tiempo encontrarte, pero por fin te he encontrado."
            centered "Me moría por ponerte las manos encima, ahhh <3"
            centered "Ahora te tengo solo para mí<33333"
            
            menu:
                "¿Qué es esto?":
                    nulla "¡Ah!"
                    nulla "Te dije que estaba guardando energía, ¿no?"
                    extend "Recuerdo haberlo dicho...."
                    nulla "¡Bueno!--------"
                    extend "\n                          ¡Quería darte esta sorpresa!"
                    nulla "Así podemos estar juntos un ratito~~~~"

            menu:
                "Llevame a tu ruta":
                    nulla "Claro bb <3"
                    jump acto3_nulla

                "Quiero pasar el tiempo contigo.":
                    nulla "Yo igual <3"
                    nulla "Pero prométeme que luego de esto, irás a mi ruta~"
                    "Pasas el tiempo con él."
                    "A pesar de que no lo puedes ver, sientes su presencia. Es cálida, te hace sentir tan agusto que no tienes ganas de volver."
                    "Quieres quedarte aquí..."
                    "......"
                    "Nulla te pregunta por tu día. Te escucha y ríe cuando dices algo gracioso."
                    "También se queja del suyo."
                    "Te comenta que ha estado esperando, viendo como estabas en la ruta del rubio."
                    "Lo llama patético."
                    "Se ríe de que él piense que al final dejarás a Nulla por él."
                    "..."
                    "Es extraño."
                    "Todo es muy extraño."
                    "Nulla se ve muy calmado."
                    "Pensaste que al menos estaría enojado contigo por traicionarlo."
                    nulla "¿Traicionarme?"
                    nulla "No seas tan inocente~"
                    nulla "Volviste conmigo."
                    nulla "Eso no es traición."
                    nulla "Supongo que solo eres alguien curioso."
                    scene negro with dissolve
                    centered "{size=*4.0}:){/size}"
                    nulla "..."
                    nulla "Dime---"
                    nulla "¿Quieres volver a conmigo?"
                    menu:
                        "Sí.":
                            jump acto3_nulla

                        
                        "No...":
                            nulla "Buah."
                            nulla "Veo que necesitas un respiro..."
                            nulla "Bueno. considera esto un badend."
                            nulla "Aunque, mi ícono seguirá activo."
                            "Termina ríendo con un:"
                            nulla "¿Premio o premio?"
                            centered "Nos vemos <3"
                            stop music fadeout 2.0
                            "...."
                            "..........."
                            $ MainMenu(confirm=False)()








        elif persistent.nulla_icon_clicks == 2:
            scene negro with pixellate
            play music "audio/ruidoblanco.mp3" fadeout 1.0 fadein 3.5 volume 0.5

            centered "Ja ja ja."
            centered "¿No puedes vivir sin mí?"
            centered "¿Ya me extrañas?"
            centered "No te preocupes no me iré a ninguna parte, cariño."
            centered "¿Tengo permiso de robarte un ratito?"

            menu:
                "No.":
                    nj "Si, mi rey---"
                    "¡¡¡HEY!!!"
                    centered "¡No se diga más!"
                    stop music fadeout 2.0
                    jump acto3_nulla
                    

                "Sí":
                    jump acto3_nulla
#EDITAR       
        else:
            scene negro with dissolve
            centered "Dame un pequeño descansito... ¿sí, mi vida?"
            centered "He consumido mucha energía."
            centered "Debo guardar un poco para el final~"
            stop music fadeout 2.0
            $ persistent.nulla_icono_act3 = False
            $ persistent.nulla_icon_clicks = 0

        return




























































            


        return

    else:

        "..."
        "No pasa nada...."
        "_________"

    return





screen tocarpantalla7():
    add "act3_n10"
    add "act3_cuchillo"
    modal True
    timer 4.0 action Jump("septemgana2_n_act3") 

    imagebutton auto "sacael_corazonn_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Corazonn")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("sacaelcorazon")


label asesinato:
    scene comedorseptem2 with dissolve
    $ bloquear_iconos = True

    "Corres en búsqueda del cuchillo, con el corazón en la garganta y los nervios apretando tu mandíbula hasta el punto de doler. Es tanta tu angustia que te olvidas que apenas puedes usar tus dedos para agarrar objetos."
    "Por lo que cuando intentas tomar el cuchillo de la mesa y caes en cuenta de que tus dedos no logran envolverse en el mango del cuchillo para alzarlo, comienzas a entrar en pánico."
    
    show nada1 with dissolve
    
    "Pero Nulla está ahí para ti. Sus sombras te ayudan; varios apéndices, similares a tentáculos, se adhieren a tus brazos. Recorriendo toda su extensión hasta llegar a tu muñeca y dedos."
    
    show cuchillo_final with dissolve
    
    "Ellos aplican la fuerza que necesitas para tomar el arma con éxito. La agarran, juntando ambas manos para apretarlo contra tu pecho, impidiendo así que se caiga."
    "Sus apéndices son cuidadosos contigo, envolviendo parte de ellos en el filo del cuchillo para que no exista la posibilidad de que te dañes con el..."
    
    hide cuchillo_final 
    hide nada1 
    with dissolve
    "Una vez seguro, te das media vuelta para correr en dirección a Nulla."
    
    scene act3_n8 with vpunch
    pause 0.1
    scene act3_n9
    
    "!!!"
    "Nulla te arrebata el cuchillo de las manos. Y, junto a sus sombras, ha logrado retener a Septem." 
    "El séptimo de los Estandartes forcejea con Nulla y sus sombras con todas sus fuerzas... es inútil, el agarre de Nulla no cede. Es más, pareciera apretar más contra el cuerpo de Septem con cada intento del rubio por salir de su agarre."
    "No tiene salida."
    scene act3_n9a
    nulla "Eres estúpido."
    nulla "Yo te lo dije."
    nulla "Te lo dije de todas las maneras posibles."
    nulla "Y aún así, tú sigues."
    nulla "Y sigues---"
    nulla "Y sigues."
    nulla "Ya era hora de que te dieras cuenta de que a tu Padre no le importas."
    nulla "En lo más mínimo."
    nulla "..."
    nulla "Vamos~~~"
    nulla "Llámalo."
    nulla "Grita para que te venga a salvar."
    scene act3_n8
    "Los tentáculos de Nulla comprimen con más fuerza el cuerpo de Septem, lento, sofocante, casi como una burla a la situación en la que la otra parte se encuentra."
    nulla "Lo último que se pierde es la esperanza, ¿no?"
    "Septem no responde, aunque escuchas el rechinar de sus dientes."
    nulla "Que aburrido eres~~~"
    septem "Eres asqueroso."
    nulla "{glitch=30.0}{color=ffffff}{size=*3.0}JA JA JA JA JA JA---{/size}{/color}"
    nulla "Tal vez~"
    scene act3_n10 with dissolve
    "Nulla te acerca más a ellos."
    nulla "Lo estuve pensando por mucho tiempo. Cómo matarte."
    nulla "Sabes que yo no puedo hacerlo."
    nulla "Pero hay alguien que puede saltarse las reglas aquí~~~"
    scene act3_n10a with vpunch
    "Septem te mira con horror cuando Nulla posa el cuchillo en tus manos, sin dejarlo de agarrar entrelaza su mano con la tuya, logrando que ambos sujeten el cuchillo."
    nulla "Vamos, cariño."
    nulla "Acabemos con esto de una buena vez~"




   
    call screen tocarpantalla7


label sacaelcorazon:
    scene muerte1
    show act3_cuchillo
    pause 0.1
    hide act3_cuchillo
    show act3_cuchillo1
    pause 0.1
    hide act3_cuchillo1
    show act3_cuchillo2
    pause 0.1
    scene muerte2
    show act3_cuchillo2
    with vpunch
    pause 0.1
    hide act3_cuchillo2
    show act3_cuchillo
    nulla "¡--- J-ja!"
    scene muerte3
    show act3_cuchillo
    "Tanto tu mano como la de Nulla tiemblan luego del impacto."
    nulla "¡Mierda! Mira como sale la sangre~"
    "Su voz es errática, fuera de sí."
    nulla "O-oh jo ja ja ja--- \n\n                                       {size=*0.5}Increíble----{/size}"
    scene muerte1
    show act3_cuchillo
    nulla "Hazlo de nuevo~~~"
    nulla "Saca el corazón, mi vida."
    jump asesinato2




screen tocarpantalla8():
    add "muerte1"
    add "act3_cuchillo"
    modal True

    imagebutton auto "sacael_corazonn_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Corazonn")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("sacaelcorazon2")

    
label asesinato2:
    call screen tocarpantalla8

label sacaelcorazon2:
    
    scene muerte1
    show act3_cuchillo
    pause 0.05
    hide act3_cuchillo
    show act3_cuchillo1
    pause 0.05
    hide act3_cuchillo1
    show act3_cuchillo2
    pause 0.05
    scene muerte2
    show act3_cuchillo2
    with vpunch
    pause 0.05
    scene muerte1
    show act3_cuchillo
    pause 0.05
    scene muerte3
    show act3_cuchillo
    nulla "Eso, sigue así~"

    
    jump asesinato3









screen tocarpantalla9():
    add "muerte3"
    add "act3_cuchillo"
    modal True

    imagebutton auto "sacael_corazonn_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Corazonn")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("sacaelcorazon3")




label asesinato3:
    call screen tocarpantalla9

label sacaelcorazon3:
    
    scene muerte3
    show act3_cuchillo
    pause 0.03
    hide act3_cuchillo
    show act3_cuchillo1
    pause 0.03
    hide act3_cuchillo1
    show act3_cuchillo2
    pause 0.03
    scene muerte2
    show act3_cuchillo2
    with vpunch
    pause 0.03
    scene muerte1
    show act3_cuchillo
    pause 0.05
    scene muerte3
    show act3_cuchillo
    pause 0.5
    $ click_count += 1


    if click_count <= 2:
        jump asesinato3
    
    else:
        nulla "Wow~"
        scene muerte4
        pause 0.3
        scene muerte5
        "Escuchas la respiración pesada de Septem, gorgoteos se forman en su boca y garganta, ahogándose con su propia sangre. Su pecho se expande, trabajando el doble para que sus pulmones reciban oxígeno."
        "Su mandíbula tirita mientras sus ojos te buscan, llenos de odio y repulsión. Intenta hablar pero su voz se mezcla con la sangre que sale de su boca."
        nulla "Por fin le darás un descanso a ese viejo cuerpo. Así mi pobre amigo ya no tendrá que aguantar que un monstruo robe su identidad."
        #Nulla y las proyectadas
        "Septem, con sus últimas fuerzas intenta mover sus manos, ya sea para agarrar las tuyas o hacer una invocación -no estás muy seguro-. Pero Nulla no le deja, y tira de ellas con sus sombras."
        nulla "Ja ja, ¿aún no te rindes?"
        nulla "Que lindo~"
        menu:
            "Acabemos con esto ya.":
                scene muerte6
                "Nulla te mira, serio, con una expresión que te incomoda un poco. Te mira como si le hubieras cortado toda la diversión del momento, como un niño mimado a quien regañas por portarse mal."
                "Luego, sonríe. Es una mueca relajada, sin nada de arrepentimiento o preocupación."
                scene muerte7
                nulla "Claro, cielo."
                nulla "No hay que jugar con la comida :)"
                nulla "Lo entiendo, lo entiendo."


            "...":
                "Septem se retuerce y tose más sangre. Todos tus sentidos están centrados en él, en el sonido de la sangre, en su olor y color."
                "Y Nulla no hace más que reírse de ello. No es una risa estruendosa, sino una risilla sofocada por sus labios."
                nulla "¿Ves?"
                nulla "Tu Padre no va a salvarte."
                scene muerte7
                nulla "Solo eres una entretención para un público que no puedes ver."
                "Una de sus manos serpentea hasta llegar a la mandíbula de Septem, la toma con fuerza para alzar su midada, dedos clavándose en la blanda piel de sus mejillas."
                "Tus ojos se encuentran con los de Septem una vez más."
                nulla "Saluda a la cámara~"
        

        scene negro with vpunch
        "De pronto, un crujido horrendo se escucha en todo el lugar. Piel, carne y huesos son desgarrados del pecho de Septem por las sombras de Nulla y tus manos."
        "En una reacción visceral gritas al sentir la sangre manchar tus manos y brazos."
        "Nulla se disculpa por lo desastroso del proceso, excusándose que no hay de otra. Que tienen que sacar su esencia del cuerpo de Septem."
        "Septem comienza a moverse cada vez menos... primero son espasmos bruscos e impredecibles, movimientos violentos que hacen que su cuerpo se sacuda contra las sombras de Nulla, las cuales batallan para mantenerlo en su lugar. Después los espasmos se vuelven débiles hasta ser reducidos a solo pequeños temblores." 
        "Pronto, deja de moverse por completo."
        "Ahora no es más que un cuerpo inerte que gotea sangre."
        "A falta de movimientos en el cuerpo, aparece un pequeño siseo en el ambiente, del cual no sabes de dónde proviene."
        nulla "Vamos~"
        "Nulla te saca del trance. Su voz hace que dejes de mirar la herida que tu mismo le has hecho a Septem."
        "Cuando tus ojos encuentran a los de Nulla, él te sonríe con ternura."
        nulla "Saca la esencia, mi vida."
        nulla "Y terminemos con esto."
        scene muerte8 with vpunch
        "Sus sombras, convertidas en tentáculos, abren la caja torácica, exponiendo los órganos del rubio."
        "....."
        "Y junto con ello, su corazón aún latiendo. Lo extraño es ver la existencia de una especie de venas que surcan la superficie del órgano, envolviéndose a su alrededor, protegiéndolo del exterior."
        "De cierto modo, sientes que lo abraza."
        "Observas con detenimiento como estas se contraen, bombeando sangre directo al corazón... como si intentaran, en vano, mantener el cuerpo con vida..."
    




        jump asesinato4
        
        
        
        
        





screen tocarpantalla10():
    add "muerte8"
    add "act3_cuchillo"
    add "nada1"
    modal True

    imagebutton auto "raftem_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "raftem")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("sacaelcorazon4")

    
label asesinato4:
    call screen tocarpantalla10

label sacaelcorazon4:
    show nada1
    show act3_mano 
    with vpunch
    
    "Tiras con todas tus fuerzas lo que supuestamente es la esencia de Septem, pero tú solo ves un corazón humano, común y corriente. Vivo y caliente. Viscoso, lleno de sangre que emana en cantidades preocupantes."
    
    play music "audio/gritoseptimo.mp3" fadein 2.0 volume 0.03

    "En tus oídos se ha formado un sonido molesto, fuerte, similar a un pitido agudo, que no hace más que crecer."
    "Es desesperante. El sonido te envuelve por completo y toma de rehén tu estómago, revolviendo todo el contenido que yace ahí. Quieres vomitar, cerrar los ojos y escapar de ahí."
    "Intentas comprender qué es. Entender de dónde sale y encontrar la razón de su repentina existencia." 
    "Entonces, lo reconoces; es la representación de un dolor." 
    "No es un simple pitido mecánico. Es un grito de angustia."
    "Es Septem."
    
    hide nada1 with dissolve

    scene muerte_final2 with vpunch
    "Por instinto, tus manos retroceden pero las sombras de Nulla aplican más fuerza, la necesaria para arrancar el palpitante órgano de su cáscara de carne y huesos."    
    
    jump continuacion_nulla_act3_final2



    




    
    #Aquí Nulla habla de lo estúpido que es Septem. Restregandole en la cara que él se lo dijo, que jamás confiara en Padre porque él lo único que hace es seguir los deseos de un díos que no los respeta ni los quiere.
    #Septem no responde.
    #Nulla habla de Rafael, se burla un poco. y a la vez se siente conmovido por como Septem ha tomado su identidad. Más no su personalidad.
    #Al matar al cuerpo, Nulla le arranca el corazon, el cual es un corazon dorado. Es septem.
    #Se puede escuchar un grito en todo el espacio. poner una pantalla con texto que se mueve con las últimas palabras de Septem antes de ser comido.
    #Septem llama a Nulla un cobarde y lo maldice.
