define yo =Character(_("Yo"), color= "#ffffff")
default septemhumano = False
default cuchillo_septem = False
default latin = False
default rafaelconfianza = 0
default sinlengua_septem = False
default nuevo_nombre = ""
default documentos = False
define rafael =Character("Rafael", color= "#00bdf1")
default diario = False
default powerhungry = 0
default broche = False 
default septemconfianza = 0

label rutaseptem:
        

    stop music fadeout 2.0
    scene hotelcomedor
    "{sc=2}Bien, lo has hecho bien...{/sc}"
    "{sc=2}Ahora viene lo difícil, si quieres sobrevivir para cuando comience la reunión{/sc}"
    "{sc=2}deberás lograr que te tomen como aprendiz.{/sc}"
    "{sc=2}De lo contrario, el cuerpo de tu marioneta será devorado.{/sc}"

    play music "audio/sorry_cant_tell.mp3" fadein 2.0 volume 0.2

    show septemcercatrago at center with dissolve
    septem "{sc=2}Okay{/sc}" 
    hide septemcercatrago
    show septemcercatrago2 at center
    septem "{sc=2} Nulla puedes sellar la mesa ahora.{/sc}"
    "En cuestión de segundos dejas de ver al pelirrojo y a Nulla, quedándote solamente con Septem en la mesa."
    "..."
    "Pasan unos buenos segundos de silencio..."
    "Supones que debes tomar tú la iniciativa de entablar una conversación."
    "Pues sino, temes que se aburra y te coma."
    "Y no puedes aguantar tanto tiempo estando parada como un idiota bajo la mirada crítica de Septem."
    "La cual da un poco de miedo."
    "Debes pensártelo un poco antes de tomar una decisión..."
    menu:

        ">Esperar hasta que hable":
            "No te quieres arriesgar a mover ningún músculo, ni respirar, ni hablar. Algo en su mirada te dice que debes estar a raya"
            "Así que ahora parece una competencia de miradas por lo intensos que son los ojos de Septem sobre ti."
            "...Quien parpadea pierde."
            "Fácilmente pasan 30 segundos donde ninguno de ustedes parpadea. Y tú ya te encuentras en el límite."
            "Mierda... si sigues así vas a perder."
            "Y tu madre no ha creado a perdedores."
            "Pasan 20 segundos más, lo sabes porque los estás contando. Y aun así Septem no parpadea ni dice nada."
            hide septemcercatrago2
            show septemcercabrindar at center
            "Con vergüenza aceptas tu derrota parpadeando con urgencia. Lo que provoca una pequeña risa por parte de Septem."
            hide septemcercabrindar
            show septemcercarisa at center
            septem "Puedes sentarte."


        ">Sentarte en la silla sin su permiso.":
            jump badendseptem2
            


        ">Escapar":
            jump badendseptem1
        


    "Con cautela te sientas al frente de Septem, quien te sonríe, complacido de que le hayas hecho caso sin mucha protesta."
    "Cuando te acomodas en tu puesto, caes en cuenta..."
    "... bueno, no estás seguro de que hacer o decir... o que no decir"
    hide septemcercarisa

    "Por lo que tienes tres opciones..."

    menu:
        ">Esperar a que él rompa el hielo.":
            "Crees que es lo más seguro, esperar a que él comience la conversación."
            "Habiendo visto que Septem tiene serios problemas de control, consideras que es la mejor opción..."
            "Aunque de todos modos no se te ocurre que decir, así que-"
            "Aceptas tu destino, sea el que sea."
            "..."


        ">Suplicar por tu vida.":
            "Decides que suplicar por tu vida como un maldito gusano, es lo más sensato."
            "Pues realmente no sabes que otra cosa hacer, y la vergüenza se ha esfumado desde que aceptaste descargar este juego."
            "...Para poner más dramatismo a tu súplica, juntas las manos y pones cara de perro abandonado."
            nj "Poor favooorrrr, ¡no dejes que me devoren!."
            "Querías seguir con tu súplica, pero Septem te interrumpe con la mano."
            septem "{sc=2}Baja la voz.{/sc}"
            nj "Pero-"
            show septemcercatrago at center
            septem "{sc=2}No quiero oírte gritar tus súplicas. {/sc}"
            septem "{sc=2}Ahórratelas...{/sc}"
            hide septemcercatrago 
            show septemcercatrago2 at center
            septem "{sc=2}Si me entretienes, tal vez te pueda dejar vivir...{/sc}"
            "... no te queda de otra que hacer de payaso personal para Septem."
            "..."
            


        ">Empezar a parlotear":
            scene hotelcomedor
            "Sin darle más vueltas al asunto, decides empezar a parlotear sobre tu nueva hiperfijación."
            "Le cuentas sin mucha vergüenza (pues esa la decidiste dejar cuando aceptaste descargar este juego) desde los datos más minúsculos y rebuscados"
            "Hasta los más perturbadores e íntimos."
            "Hablas hasta por los codos sin darte cuenta, piensas que es como si estuvieras hablando con un amigo que comparte tus extraños gustos."
            "Pero hasta ahora no te dignas en mirar su reacción."
            "El aura que transmite el ambiente no da muy buena espina, por lo que decides parar en seco."
            "Y con terror alzas la mirada para observar la reacción de Septem."
            show septemcercatrago with dissolve
            septem "{sc=2}...{/sc}"
            nj "..."
            septem "{sc=2}........{/sc}"
            "El sentimiento de ser juzgado por Septem es una de las peores sentencias que te pueden dar..."
            "No se lo deseas a nadie."
            hide septemcercatrago
            show septemcercatrago2 at center
            septem "{sc=2}Admito que encuentro adorable el entusiasmo que muestras al hablar.{/sc}"
            septem "{sc=2}Pero debes bajar la voz y hablar un poco más lento.{/sc}"
            "Tiene razón... seguramente parecías un perro con rabia ladrándole a un poste de luz."
            "Lo mejor que puedes hacer es disculparte."
            nj "Disculpa."
            hide septemcercatrago2
            show septemcercabrindar at center
            septem "{sc=2}No te preocupes... me encantaría seguir escuchando{/sc}"
            septem "{sc=2}Pero tenemos otros temas que quiero tocar.{/sc}"
            septem "..."
    

    scene hotelcomedor
    show septemcercatrago
    septem "{sc=2}Iré directamente al grano{/sc}"
    hide septemcercatrago
    show septemcercatrago2
    septem "{sc=2}Reconozco a una marioneta humana cuando la veo.{/sc}"
    septem "{sc=2}Tienes sus mismos ojos.{/sc}"
    septem "{sc=2}Y puedo ver que su voluntad tiende a anteponerse a tus comandos{/sc}"
    hide septemcercatrago2
    show septemcercatrago
    septem "{sc=2}No tienes un control completo.{/sc}"
    "..."
    "Esperas por lo peor, que te destripe o te rompa algún hueso."
    "Pero no sucede nada."
    hide septemcercatrago
    show septemcercatrago2
    "Septem solo te observa."
    hide septemcercatrago2
    show septemcercarisa
    septem "{sc=2}Oh, no temas. Madre no tiene acceso a un lugar sellado.{/sc}"
    septem "{sc=2}Así que no te castigará.{/sc}"
    hide septemcercarisa
    show septemcercanormal
    "A pesar de que sus palabras tienen la intención de calmarte, el efecto que tienen en ti es todo lo contrario"
    hide septemcercanormal
    show septemcercatrago
    pause 0.5
    hide septemcercatrago
    show septemcercatrago2
    septem "{sc=2}Hmm... el nivel de sincronización que tienen no está al 100 porciento.{/sc}"
    septem "{sc=2}No están sintiendo lo mismo y sus reacciones tienden a contradecirse.{/sc}"
    hide septemcercatrago2
    show septemcercabrindar
    septem "{sc=2}Si tuvieras un control completo...{/sc}" 
    hide septemcercabrindar
    show septemcercaexaltado
    septem "{sc=2}podrías interactuar con este mundo como se te de la gana.{/sc}"
    septem "{sc=2}Una inmersión total,{/sc}"
    septem" {sc=2}no limitada como la que estás experimentando detrás de esa pantalla.{/sc}"
    hide septemcercaexaltado
    show septemcercatrago2
    septem "{sc=2}Estoy seguro de que Nulla ya se ha enterado, por lo que debemos actuar rápido.{/sc}"
    septem "{sc=2}Puedo ayudarte...{/sc}"
    septem "{sc=2}Seguirás mis comandos si quieres sobrevivir..." 
    septem "{sc=3}Cuando Nulla saque el sello, no te muevas.{/sc}" 
    scene hotelcomedor with dissolve
    menu: 
        "Aceptar":
            pass
        "Rechazar":
            jump badend_cena
    
    "Aceptas con la esperanza de poder seguir con vida."
    "Harás lo que sea necesario para poder vivir."
    show septemcercabrindar
    "Te ganas una sonrisa por parte de Septem al escuchar tu respuesta."
    hide septemcercabrindar
    show septemcercarisa
    septem "{sc=2}Nulla debe estar por quitar el sello.{/sc}"
    scene hotelcomedor
    "Asientes con la cabeza..." 
    scene hotelcomedor with vpunch
    stop music fadeout 3.0
    "No alcanzan a pasar ni 3 segundos cuando sientes una presión extraña en tu cuerpo... supones que debe ser Nulla."
    play music "audio/europalce.WAV" fadein 2.0 volume 0.4
    scene hotelcomedor with pixellate
    show nulla1normal at left
    show unum1normal at right
    "Nulla y el pelirrojo se materializan justo donde los viste la última vez, Nulla parado a un lado de la mesa y el pelirrojo sentado al lado de Septem."
    "Como si hubieran estado siempre allí."
    "Septem mira con una cara larga a Nulla. Y él notando esto habla más rápido de lo normal."
    hide nulla1normal
    show nulla2blush at left
    nulla "No veo que te haya gustado mucho el regalo. Podrías dármelo y yo le diré a Madre que lo cambie por otro."
    "Se le oye ansioso."
    hide nulla2blush
    show nulla2serio at left
    nulla "Se ve que no es de la máxima calidad..."
    hide unum1normal
    show unum3callado at right
    nulla "Unum piensa lo mismo, supongo que los demás pensarán igual."
    hide unum1normal and nulla2serio with dissolve
    "Nulla comienza a acercarse a ti, con el objetivo de tomar tu brazo. Sus ojos sobre tu figura en todo momento."
    show septem2incomodo with moveinleft
    septem "{sc=2}No es necesario. Irá conmigo a mi dominio.{/sc}"
    septem "{sc=2}Habla con madre para que traiga otro regalo.{/sc}" 
    septem "{sc=3}Dudo que demore más de 5 minutos.{/sc}"
    show nulla2serio at left with dissolve
    nulla "Disculpa, pero no puedo manchar el nombre de Madre con esta ofrenda tan mediocre."
    scene hotelcomedor with vpunch
    "Nulla te agarra el brazo fuertemente e intenta hablarte"
    "{glitch=20.0}{color=ffffff}{b}Sígueme el juego. No es segu---{/glitch}" 
    stop music fadeout 3.0
    "-pero Septem se lo impide tomando a Nulla por la espalda."
    play music "audio/the_chillout_factory.WAV" fadein 2.0 volume 0.4
    nulla "Eres un--!"
    scene septem_nulla with vpunch
    "En un abrir y cerrar de ojos Septem atraviesa el pecho de Nulla." 
    septem "No dejaré que lo arruines."
    "Y con desdén empuja el cuerpo del pelinegro a un lado, provocando que caiga con un golpe seco."
    "Nulla yace en el suelo, tosiendo sangre."
    septem "{sc=2}He dicho que me lo llevaré.{/sc}"
    scene hotelcomedor
    show unum3blush with vpunch 
    "Unum se levanta con urgencia de la mesa, pero decide no acercarse a ellos."
    unum "WOW Septem, estamos en público. Si alguien te llegase a ver..."
    show septem2enojo at left
    septem "{sc=3}CIERRA LA BOCA{/sc}"
    septem "{sc=3}Nulla{/sc}"
    septem "{sc=2}Puedes decirles a los demás que estaré ocupado.{/sc}"
    scene hotelcomedor
    "No te puedes mover por el terror que estás sintiendo ahora mismo. Al parece haber aceptado a Septem no fue la mejor idea."
    "Pero de cierta manera le agradeces a los dioses que la ira de Septem no esté enfocada hacia a ti."
    "Aunque te sientes algo mal que haya sido Nulla."
    "Septem se gira para poder verte cara a cara, y sin explicar nada te toca la frente delicadamente."
    scene hotelcomedorborroso with dissolve
    "Y comienzas a ver borroso."
    "Repentinamente dejas de escuchar la respiración entrecortada de Nulla y el sonido ambiental del comedor."
    scene negro with Dissolve(2)
    stop music fadeout 3.0
    "Para luego abrir paso a una oscuridad total."
    "..."
    "......"
    "Despiertas con la sensación de estar cayendo."
    scene camaseptem with dissolve
    play music "audio/calamity.WAV" fadein 2.0 volume 0.4
    "Para luego darte cuenta de que estás en una cama espaciosa y cálida."
    "Lo primero que tus ojos ven es el enorme ventanal que está ubicado al costado de la cama."
    "Supones que es de día por la luz que entra, pero es extraño ya que no se ve nada más que la potente luz fuera de la ventana."
    "De repente se te viene a la mente lo ocurrido y con apuro buscas con la mirada algún rastro de Septem"
    "No hay nadie en la habitación contigo."
    menu:
        "Quedarte aquí y esperar":
            "Tienes algo de miedo, para ser completamente honestos."
            "Además de que la cama está perfecta como para quedarte unos minutos más."
            "Poco a poco, vuelves a cerrar los ojos."
            scene negro with Dissolve(3)
            septem "Despierta."
            "Una voz te comanda y te obliga a abrir los ojos de golpe."
            "Como si te hubieran echado agua fría en toda la cara."

        "Investigar la habitación":
            "Con dificultad te levantas de la cama."
            scene habitacionseptem with dissolve
            "La habitación es asquerosamente amplia y con un ambiente que te recuerda a un hospital."
            "Todo blanco, sin rastros de otra gama de colores."
            "Nada de lo que se encuentra aquí evoca algún sentimiento de pertenencia o rastro de personalidad."
            "Es raro."
            septem "Veo que ya has despertado."

        "Salir de la habitación":
            jump badend_septem3

    scene habitacionseptem with dissolve
    septem "Es hora del desayuno."
    scene septemventanal with dissolve
    "Septem está cerca del ventanal con las manos detrás de su espalda."
    "No tienes idea de donde apareció, y eso te pone la piel de gallina."
    scene septemventanal1
    "Al parecer te tomas más tiempo del necesario para contestarle, pues Septem hace una mueca, irritado."
    septem "¿Me escuchaste?"
    "Asientes con la cabeza."
    septem "Bien. Vamos."
    scene septemventanal2
    stop music fadeout 3.0
    "Septem junta las manos y el lugar comienza a cambiar. La cama y la habitación se transforman en un comedor con la misma paleta de colores."
    scene septemmesa with pixellate
    pause 0.5
    show septemmesa_sonrisa with dissolve
    play music "audio/hope.WAV" fadein 2.0 volume 0.4
    "Caes en una silla, frente a una mesa que ya tiene platos y comida servida."
    "Septem yace también sentado, al frente tuyo."
    hide septemmesa_sonrisa
    show septemmesa1
    septem "La marioneta lleva más de 24 horas sin comer algo."
    septem "Debe comer, sino no funcionará de la manera correcta."
    hide septemmesa1
    show septemmesa2
    "Por algún motivo, aunque no sabrías explicar el porqué, parece que hablara desde la experiencia."
    "No te atreves a hacer nada, pues Septem no te ha dado permiso para comenzar a comer. Y no quieres tentar a la suerte."
    hide septemmesa2
    show septemmesa3
    septem "Puedes comer."
    hide septemmesa3
    show septemmesa2
    "Mientras comes te das cuenta de algo extraño y es que Septem ahora no posee esa voz que resuena tanto en tu cabeza como en tu cuerpo."
    "Esa voz algo inestable y a la vez inorgánica."
    "Ahora es normal."
    "No crees que sea buena idea preguntarle, puede ser alguna falta de respeto hablar o preguntar ese tipo de cosas."
    hide septemmesa2
    show septemmesa_serio
    septem "No me gusta que tengamos a la marioneta interfiriendo en nuestra conversación..."
    septem "Pero es indispensable para poder conectarte a este mundo."
    hide septemmesa_serio
    show septemmesa_feliz
    septem "...Te respeto. Al ser una entidad de un plano superior, probablemente tienes más poder que yo o Madre juntos."
    septem "Incluso podría ser muy parecido al del creador..."
    hide septemmesa_feliz
    show septemmesa1
    septem "Lastimosamente, ese poder no se puede demostrar ahora mismo, pues aquí solo estás de visita."
    hide septemmesa1
    show septemmesa2
    "{sc=3}Probablemente te olvides de este mundo cuando cortes el vínculo conmigo.{/sc}"
    "¿Que ha sido eso? una voz se ha colado dentro de tus pensamientos."
    "Esto no te gusta."
    septem "..."
    hide septemmesa2
    show septemmesa_enojo
    septem "Necesito tiempo..."
    menu:
        "¿Tiempo para qué?":
            hide septemmesa_enojo
            show septemmesa2
            "Septem te observa antes de contestar completamente serio."
            hide septemmesa2
            show septemmesa1
            septem "Tiempo para hacer el cambio de huésped."
            septem "Y convertirnos un ser perfecto."
            septem "Tú [nombrejugador], eres lo que necesito."
        
        "Yo necesito que me expliques que está pasando":
            hide septemmesa_enojo
            show septemmesa3
            septem "comprendo que para alguien ajeno al jardín pueda ser difícil de entender..."
            hide septemmesa3
            show septemmesa_sonrisa
            septem "¿Pero cual sería la gracia de saber todo al instante? ¿Hmm?"
            septem "Te prometo que te explicaré todo cuando sepa que eres lo que busco."
            septem "Por ahora lo que puedes saber es que necesitamos tiempo para hacer el cambio de huésped."
            hide septemmesa_sonrisa
            show septemmesa_feliz
            septem "Y convertirnos un ser perfecto."
            hide septemmesa_feliz
            show septemmesa3
            septem "Tú [nombrejugador], eres lo que necesito."
            
        
        "Basta harás lo que yo diga":
            nj "Ya tuve suficiente, harás lo que yo diga."
            hide septemmesa_enojo
            show septemmesa_asombro
            "Septem te mira asombrado."
            "Con la información dada, sabes que ahora estás en una posición donde Septem no tiene poder ante ti."
            "Pues claramente ha dicho eso."
            "...¿cierto?"
            jump badend_septem4
    scene septemmesa
    show septemmesa_serio
    septem "Pero."
    hide septemmesa_serio
    show septemmesa_enojo
    septem "Mientras más tiempo pase, más independencia va a adquirir tu marioneta."
    septem "Y necesitamos su permiso para realizar el cambio..."
    septem "Eso será un problema si no sabes cómo controlarle."
    hide septemmesa_enojo
    show septemmesa2
    "{sc=3}Septem está mientiendo, yo nunca iría en tu contra o desobedecería tus comandos{/sc}"
    "{sc=3}[nombrejugador], estoy aquí para servirte.{/sc}"
    "{sc=3}No le creas{/sc}"
    hide septemmesa2
    show septemmesa_feliz
    "Septem suelta una pequeña risa al observar tu reacción."
    septem "Deberías tener más cuidado, ya está empezando a desligarse de ti."
    hide septemmesa_feliz
    show septemmesa_enojo
    septem "Y si pasa eso, ya no me servirás."
    scene comedorseptem
    "el rubio se levanta de la mesa, y examina sus manos por un buen rato."
    show septemd2feliz with dissolve
    septem "Nos vemos en el almuerzo, mientras, puedes recorrer mi dominio como te plazca."
    hide septemd2feliz with fade
    "Septem deja la mesa llevando los platos, ahora vacíos, a otro lugar. Supones que debe ser la cocina."
    "Esperas a que Septem aparezca nuevamente, pues no te crees que te haya dejado sin supervisión y te haya dado un pase libre para hacer lo que quieras."
    "Más él no vuelve a aparecer."
    "Te quedas ahí, recolectando tus pensamientos."
    "Analizando todo lo que te han dicho y ha pasado."
    "Septem quiere darte control completo, una sincronización completa con este cuerpo..."
    "{sc=3}Pero no comprendo que estaría ganando él a cambio.{/sc}"
    "{sc=3}No es de fiar.{/sc}"
    "{sc=3}Necesitas a Nulla{/sc}"
    menu:
        "¿Necesitas a Nulla?"
        "No":
            "No necesitas a Nulla."
            pass
        "Sí":
            "{sc=3}Tengo razón, necesitamos a Nulla.{/sc}"
            $ necesitasanulla = True
        
    "Sea cual sea tu respuesta... no sabes si Nulla siga vivo o no."
    "Por lo que debes seguir por tu cuenta... por ahora."
    "..."
    scene temploseptem with dissolve
    "Pasas el tiempo caminando por lo que parece ser un templo."
    "Pues tienen un montón de estatuas de Septem y cuadros con alegoría religiosa."
    "Y dentro de él te encuentras con un montón de puertas."
    menu:
        "Investigar las puertas.":
            call menupuertas from _call_menupuertas
        
        "Quedarse aquí":
            "No tienes muchas ganas de arriesgarte por hoy."
            "Es mejor que esperes al almuerzo y así poder hablar con Septem."
    scene temploseptem with dissolve
    "Esperas a que pasen las horas."
    "Dormitas pensando que fue lo que pasó con Nulla y el porqué Septem sabe de ti..."
    "Pero no encuentras respuesta a ninguna de las dos incógnitas."
    show septemd1normal with dissolve
    "El tiempo pasa lo suficientemente rápido como para sorprenderte de la llegada de Septem al altar."
    "Esperas a que él te dirija la palabra para poder hablar."
    hide septemd1normal
    show septemd1risa
    septem "Es momento del almuerzo."
    hide septemd1risa
    show septemd1normal
    "Tienes la tentación de preguntar porqué le pone tanto énfasis a tener que compartir la comida contigo."
    "Si es que se está preocupando de que comas, entonces no es necesario sentarse a comer contigo."
    "Sospechas que será así en toda tu estadía en este lugar."
    scene septemmesa with pixellate
    show septemmesa_sonrisa with dissolve
    "Nuevamente Septem los teletransporta al comedor, donde otra vez los reciben los platos ya listos en la mesa."
    "Septem espera a que tu comiences a comer para hacerlo él."
    hide septemmesa_sonrisa
    show septemmesa_comer
    "No se le ve muy dispuesto a tener una conversación..."

    if septemhumano == True:
        "Pero no puedes evitar pensar que hay algo extraño en su actitud..."
        "Su aura no es la misma a la que tuvo dentro de esa habitación."
        "El comportamiento es totalmente diferente, aquí muestra una careta segura... en cambio allá, una totalmente contraria."
        menu:
            "¿Por qué ahora tienes otra actitud?":
                septem "¿Oh? ¿A qué te refieres?"
                "Le explicas lo que pasó en la habitación del altar."
                jump badend_septem5
            
            "No decir nada.":
                "Preguntar la razón no te da buena espina, por lo que decides guardar silencio... por ahora."
                "Septem no se digna en ningún momento en iniciar cualquier tipo de conversación."
                "Por lo que comen en silencio."
    
    
    else:
        "Comienzan a comer."
    
    "Septem come de manera lenta, se le ve totalmente desconectado con la acción."
    "Como si lo estuviera haciendo en automático."
    hide septemmesa_comer
    show septemmesa_comer2
    septem "Tus ojos llevan un buen tiempo en mi cara."
    septem "¿Pasa algo?"
    menu:
        "Comer en silencio":
            "No."
            septem "Está bien..."
            hide septemmesa_comer2
            show septemmesa_comer
            "Comer de esta manera lo hace muy incómodo, puedes escuchar como masticas tu comida y estás al tanto de que el silencio que hay en el lugar ayuda a que se escuche cada sonido que tu boca y dientes emiten."
            "Es horrible y sumamente incómodo..."
            pass
        
        "Hablar de temas ligeros":
            hide septemmesa_comer2
            show septemmesa_comer
            nj "No es nada..."
            nj "Solo es que siento que hay mucho silencio."
            hide septemmesa_comer
            show septemmesa1
            septem "¿Te incomoda?"
            hide septemmesa1
            show septemmesa2
            nj "No lo sé."
            "No es que no lo sepas, es solo que no sabes que contestar para no hacerlo enojar, o que sienta que es una falta de respeto."
            "Te aterra no contestar de la manera que él encuentre correcta."
            hide septemmesa2
            show septemmesa3
            septem "No te preocupes tienes total libertad de hablarme como se te plazca."
            septem "Siempre y cuando seas tú, [nombrejugador]. No  la marioneta."
            hide septemmesa3
            show septemmesa_comer2
            septem "Estoy aquí para servirte."
            menu:
                "Hacer preguntas":
                    call menupreguntas from _call_menupreguntas
                
                "Comer en silencio.":
                    pass
               
    scene comedorseptem
    "Al terminar, Septem se lleva los platos y desaparece sin antes decir que se verán en la cena."
    "Tú ya te estás aburriendo de la poca interacción que han estado teniendo."
    "Y nada interesante ha pasado hasta ahora... si hubieras ido con Unum..."
    "Bueno, tienes que pasar el tiempo de algún modo."

    menu:
        "Investigar las puertas.":
            call menupuertas2 from _call_menupuertas2
        
        "Quedarse aquí":
            "No tienes muchas ganas de arriesgarte por hoy."
            "Es mejor que esperes a la cena y así poder hablar con Septem."
        
        "Escapar":
                jump badend_septem6
        

    scene temploseptem with dissolve
    show septemd1normal with dissolve
    "El tiempo pasa rápido, y esta vez presencias como Septem se materializa ante el altar del templo."
    "Ya a estas alturas supones que te has acostumbrado, pues no te sobresaltas."
    hide septemd1normal
    show septemd1risa
    septem "Es hora de la cena."
    hide septemd1risa
    show septemd1disgusto
    nj "{sc=3}¿Vamos a seguir esta rutina todos los días?{/sc}"
    hide septemd1disgusto
    show septemd1enojo
    septem "¿[nombrejugador], has sido tú quién a comandado esa pregunta?"
    menu:
        "Mentir para encubrir a la marioneta":
            nj "Sí."
            $ rafaelconfianza += 1
            hide septemd1enojo
            show septemd1enojoo
            septem "Hmmmm."
            hide septemd1enojoo
            show septemd2incomodo
            septem "La idea es que las marionetas puedan obtener energía para funcionar..."
            septem "Tanto la mía como la tuya."
            nj "¿Tienes una marioneta?"
            septem "Algo así."
            "Septem comienza a acercarse a ti. Su cara angelical es una antítesis con el aura que transmite."
            scene septem_lengua1 with dissolve

        "Decir la verdad":
            nj "No"
            septem "Veo que tendré que hacer algo al respecto..."
            stop music fadeout 5.0
            septem "Aunque... viendo que aún tienes la capacidad de tomar una decisión que va contra los deseos de la marioneta, la penalización no será fatal."
            hide septemd1enojo
            show septemd2risa
            play music "audio/Clement Panchout _ Dark _ 2004.WAV" fadein 2.0 volume 0.4
            "Septem sonríe de manera tétrica."
            hide septemd2risa
            show septemd2feliz
            septem "Oh no te preocupes... a ti no te dolerá [nombrejugador]."
            septem "Esto le enseñará a tu recipiente a respetar tus deseos."
            scene temploseptem with dissolve
            "Septem te prohibe moverte con solo el chasquido de sus dedos, y sonriendo comienza a acercarse a ti. Su cara angelical es una antítesis con el aura que transmite."
            scene septem_lengua1 with dissolve
            "Una de sus manos se posa en tu mandíbula, tomándola con delicadeza para luego apretar con fuerza entre tus mejillas, provocando que tu boca se abra automáticamente."
            scene septem_lengua2
            septem "Por respeto a ti, [nombrejugador], no lo haré de una forma tan cruda."
            septem "Pero quiero que sepas que a mí me gusta mucho ensuciarme las manos."
            scene septem_lengua3
            "Septem posa sus ojos en tu boca por un instante, y al parpadear, sientes como tu boca se llena de un líquido caliente y un dolor punzante nace donde debería estar tu lengua."
            scene septem_lengua3 with vpunch
            show sangre
            "Duele y quema al mismo tiempo. Cada segundo que pasa, es agonizante."
            "No solo por el dolor, sino que también porque no entiendes que está pasando, y porqué está pasando."
            "Tampoco puedes moverte como para inspeccionar que es el líquido que emana de tu boca y no deja salir."
            "Cuando intentas hablar, algo no responde."
            "Algo falta... y no es tu voz."
            "Porque puedes gritar."
            "Pero no puedes modular las palabras."
            septem "Oh, creo que te has dado cuenta ya..."
            septem "A estas alturas, no veo el propósito de tener una lengua que se manda sola y habla sin el permiso de su dueño."
            scene septem_lengua4
            show sangre
            septem "... Oh no."
            scene septem_lengua5
            show sangre
            septem "No, no, no. [nombrejugador], no pasa nada."
            septem "Siento que haya roto parte de tu juguete, pero..."
            scene septem_lengua1
            show sangre
            septem "No te preocupes por eso, dentro de poco dejarás este trozo de carne para cambiarlo por mí."
            septem "Además, aun puedes tomar decisiones."
            hide sangre with dissolve
            $ sinlengua_septem = True

        ">Usar el cuchillo" if cuchillo_septem:
            jump badend_septem7

    stop music fadeout 3.0
    septem "..."
    play music "audio/calamity.WAV" fadein 2.0 volume 0.4
    scene septem_lengua6 
    septem "Mira, realmente quiero que entiendas lo que está pasando y por qué tú eres vital para la recuperación del jardín."
    septem "Y no me gustaría omitir información vital para tu toma de decisión cuando empiece el cambio de recipiente."
    septem "Implantaré mis memorias en la marioneta para que sea más rápido."
    scene septem_lengua7 with dissolve
    "Septem coloca su mano izquierda en tu frente."
    scene septem_lengua8
    septem "Puedes saltarte la información que se te dará a continuación si es que no te interesa... Creo que tienes algo para hacer eso, Nulla una vez habló de ello."
    septem "El botón de skip, creo que ese es su nombre."
    "..."
    scene negro with dissolve
    "{b}En un inicio todo era oscuridad, la nada misma.{b}"
    scene creador with dissolve
    "{b}Cuando llegó el creador, se hizo la luz.{b}"
    scene creador2 with dissolve
    pause 1.0
    scene creador3 with dissolve
    "{b}Y fue ahí que comenzó mi existencia...{b}"
    scene creador4 with dissolve
    "{b}Aunque, al tener luz, nos permitió ver las sombras. Fue ahí que nos dimos cuenta de la existencia de Nulla.{b}"
    "{b}Aquel que había estado en este lugar antes de mi existencia y de la llegada del creador al jardín... esperando.{b}"
    scene creador5 with dissolve
    "{b}Nulla y el creador estuvieron hablando por un largo tiempo... y yo, al ser todavía un ser sin conocimiento de nada, no les entendí.{b}"
    "Pero de algo estoy seguro, y es que Nulla parecía no respetar al creador. Lo trataba como a un igual, subiendo su voz y llegando hasta poner sus sucias manos encima...{b}"
    scene creador6 with dissolve
    "{b}...{b}"
    "{b}Luego el creador me dio la misión de crear estandartes para mantener al jardín funcionando{b}"
    scene sol with pixellate
    "{b}Así que eso fue lo que hice. El lunes, le di vida al sol, pero tú lo conoces como Umun.{b}"
    scene firmamento with pixellate
    "{b}El martes fue el firmamento y las estrellas, Duae.{b}"
    scene tierraa with pixellate
    "{b}El miércoles se creó la tierra y las plantas, Tria{b}"
    scene lunaa with pixellate
    "{b}El jueves se creó la luna, Quattor fue igual de brillante que el sol en un inicio..."
    scene unumbatalla with pixellate
    "{b}Una lastima la pelea que Unum empezó.{b}"
    "{b}...Antes de poner orden todo era un caos, si tan solo hubiera podido intervenir.{b}"
    scene quattorbatalla with pixellate
    "{b}Tal vez Quattor seguiría con sus cuatro ojos...{b}"
    "{b}...Al quitarle dos de sus ojos la luna dejó de brillar y ahora sale cuando el sol se oculta.{b}"
    "{b}...{b}"
    scene quinque with pixellate
    "{b}El viernes, se crearon a todas las criaturas, y se dispuso un estandarte que les representa: Quinque.{b}"
    scene sextam with pixellate
    "{b}Por último el sábado, mi querida Sextam nació junto con la humanidad.{b}"
    scene negro with dissolve
    "{b}...El domingo fue un día de descanso. Dónde estuve todo el día observando el funcionamiento del jardín, pero--{b}"
    "{b}No tenía un cuerpo físico para poder experimentar todo lo que había creado.{b}"
    "{b}Y por mucho tiempo estuve así...{b}" 
    scene sextam2 with dissolve
    "{b}Hasta que Sextam me habló de transfundir mi esencia a un humano.{b}"
    "{b}Pero para ello debía dejar mi existencia y empezar a vivir como un humano.{b}"
    scene nacimiento with dissolve
    "{b}... al instante me di cuenta de mi error, los humanos al ser concebidos, se les da un alma que es distribuida por el jardín o Madre.{b}"
    "{b}Haciendo que la transfusión resulte en una mezcla del alma del humano y la esencia de la deidad que la hace.{b}"
    "{b}Así que este cuerpo no es completamente mío.{b}"
    scene negro with dissolve
    menu:
        "¿Para qué me necesitas?" if sinlengua_septem == False:
            pass

        "..." if sinlengua_septem == True:
            septem "Supongo que te estarás preguntando para que te necesito..."

    scene temploseptem with pixellate
    show septemd1triste with dissolve
    septem "... Ya no tengo el control del jardín."
    septem "Luego de que el creador se esfumara, el jardín empezó a agonizar."
    hide septemd1triste
    show septemd1enojo
    septem "El primer signo fue la desaparición de los hijos de Sextam, los humanos que nos daban devoción genuina."
    hide septemd1enojo
    show septemd1enojoo
    septem "En el caos, reapareció Nulla, Y me puso al tanto de todo lo que tiene que ver con nuestro mundo y el creador..."
    septem "Luego, me enseñó de la existencia de otros mundos abandonados por el creador, en un estado igual al nuestro."
    hide septemd1enojoo
    show septemd2incomodo
    septem "Pero la diferencia es que tenían humanos... Así que nos implantamos en su cultura."
    septem "Y consumimos su devoción de manera directa, cada último domingo del mes."
    hide septemd2incomodo
    show septemd2risa
    septem "Pero contigo aquí no será necesario continuar con esto... si nos unimos en una transfusión, me concederás la autoridad de manipular el jardín a mí---"
    septem "no--- a nuestro antojo."
    septem "¡Podemos salvar este mundo!"
    septem "Y evitar que Nulla lo destruya todo."
    hide septemd2risa
    show septemd1triste
    septem "...mira."
    septem "Nadie de los Estandartes sabe la triste verdad de que no somos más que un mundo que simula ser orgánico... lo único que saben es que nuestro mundo agoniza."
    septem "Para ti puede ser un juego, pero para mí y los míos es nuestro hogar."
    septem "A pesar de que todo sea una mentira... quiero que ellos puedan vivir en las mejores condiciones, que el jardín pueda volver a ser lo que era antes."
    septem "Quiero hacer todo lo posible para evitar lo inevitable..."
    septem "Ahora que lo sabes..."
    hide septemd1triste
    show septemd1risa
    septem "¿Aceptas?"
    hide septemd1risa with dissolve
    scene temploseptem with dissolve
    "Nulla quiere destruir todo... pero, ¿aceptar el trato de Septem es lo correcto?"
    "No parece ser tan malo como creías... tal vez es algo inadaptado... después de todo él hace lo que cree que es correcto, siempre siguiendo la etiqueta y reglas pues eso es lo único que conoce."
    "Pero por otro lado..."
    "Uhg..."
    menu:
        "Aceptar":
            pass

        ">Rechazar e invocar a Rafael" if rafaelconfianza >= 2 and septemhumano:
            if sinlengua_septem == True:
                "No puedes invocar su nombre..."
                "Imposible hacerlo sin una lengua...."
                "Por lo que solo tienes dos opciones"
                menu:
                    "Aceptar":
                        pass

                    "Rechazar":
                        jump badend_septem8
            else:
                jump rutarafael
        
        "Rechazar":
            jump badend_septem8
    
    
    if sinlengua_septem == True:
        "Aceptas indicando con la cabeza."
        "Pues ya no puedes hablar por la falta de tu lengua."
        "Aunque... ya no duele tanto."
    
    else:
        nj "Acepto"
        
    scene septem_trato with dissolve
    "Septem te extiende la mano y tú la tomas firmemente."
    "Sientes como una electricidad recorre tu cuerpo."
    "Y la sonrisa de Septem se hace más grande con cada segundo pasado."
    septem "Empezaré con los preparativos."
    "Luego de aquello, Septem teletransporta a tu habitación para terminar por el día."
    "Cuando te arropas en la cama, él te comenta que mañana comerás sin su compañía hasta la cena."
    "Y se retira de la habitación sin dar más explicaciones, despidiéndose educadamente de ti..."
    scene negro with dissolve
    "Cierras los ojos, esperando dormirte al instante."
    "Pero te cuesta un poco."
    stop music fadeout 3.0
    "___________________________"
    play music "audio/woo_scary.WAV" fadein 2.0 volume 0.6
    scene grimal1 with pixellate
    "Ves una figura aparecer en la oscuridad."
    scene negro with pixellate
    "Pero cuando enfocas tus ojos a la figura, está desaparece."
    "De la impresión caes al suelo."
    "..."
    scene grimal2 with pixellate
    "Hola, [nombrejugador]"
    "Veo que has tomado una decisión..."
    "No tiene caso seguir insistiendo... supongo que la ideología de Septem siempre ha sido la correcta."
    "Y nuestro plan es la opción egoísta y más fácil de ejecutar."
    "..."
    menu:
        "¿Quién eres?":
            pass

    menu:
        "¿Por qué hablas conmigo?":
            "Escuchas una risa seca."  
            "¿Qué una madre no puede tener una conversación con su hijo?"  
            "..."

    show grimal3
    madre "Soy Madre de tu marioneta, primera marioneta hecha con mi carne y fragmentos del alma de Nulla, para poder contenerte."
    madre "Así como también, soy Madre del jardín."
    madre "Solamente puedo tener comunicación con Nulla gracias a las leyes estúpidas que dictaminó el Creador..."
    madre "Por lo que la única comunicación que tengo con el exterior es Nulla... y, no... él no se encuentra muy abierto a escuchar otras soluciones ahora que estás tu aquí."
    madre "Pero puedo acceder a ti gracias a la marioneta. Y contigo aquí, fuera del alcance de Nulla, puedo conseguir lo que quiero sin dañar a nadie dentro del Jardín."
    madre "Si tienes la oportunidad, dile a Septem que me deje ir."
    madre "Si hablas con Septem, tal vez él pueda idear algo para sacarme de esta condena."

    menu:
        "¿Te han condenado?":
            show grimal2 
            madre "Sí, fue 'El Creador' o 'Padre', como quiera que lo llamen aquí. Él y yo éramos iguales... ambas divinidades omnipresentes creadas por un ser del plano superior."
            madre "Aunque no vale la pena hablar de este ser, ya que nadie de aquí puede ponerle las manos encima, como sucede contigo [nombrejugador]."
            madre "..."
            show grimal3
            madre "Lo que sucedió fue que el Creador, viendo mi historial, me consideró peligrosa para los habitantes del Jardín por abrirle los ojos a mi Ne--Nulla, en épocas pasadas."
            madre "Por ello, me condenó a estar segregada y a mantener al Jardín con mi cuerpo."
            madre "Amo y odio al Jardín. Estoy viva gracias a ellos, tengo conexión con toda entidad del Jardín, todos y cada uno. Siento todo, desde el 1 al 7..." 
            madre "Siento su agonía; hago placebos, traigo humanos con ayuda de Nulla, todo para no sentir su dolor colectivo... aunque cueste romper mi cuerpo físico una y otra vez..."
            madre "Es inútil... no puedo salir de aquí... No puedo amparar a mis hijos. No puedo siquiera tener una conversación con ellos."
            madre "Y aun así, los conozco como la palma de mis manos."
            show grimal5
            madre "Sé las preocupaciones de Duae, sé la rabia que tiene Tria, la soledad de Quinque..."
            madre "Y sé lo roto que está Septem."
            madre "Puedo sentir y escuchar sus plegarias, pidiendo a gritos a su padre que vuelva para arreglar todo."
            show grimal6
            madre "Pero él no va a venir."
            madre "Es muy orgulloso para ello."
            madre "Y realmente, no le interesa."
            madre "Septem es uno más de los tantos que tiene."
            "Madre suspira pesadamente y su aura cambia."
            show grimal4
            madre "No tengo problemas en dejar que el jardín siga viviendo."
            madre "Pero mi individualidad, mi ser y omnipresencia ya no aguanta más."
            madre "Así que por favor dile a Septem que me quite la individualidad. Que deje mi cuerpo en el vacío, eternamente en un ciclo infinito de destrucción y regeneración."
            madre "Sé que mi cuerpo y esencia deben estar presentes... pero mi individualidad no es necesaria."
            madre "Sé que Septem puede hacer algo ahora que te tiene aquí. Confío en que puede arreglarlo."
            madre "Ahora que tiene nuevos ojos que no están ligados al Creador."
            madre "Pueden sanar y eliminar todas las condenas del Creador."
            madre "Y si tienes la oportunidad-"
            madre "Quiero que rompas los ojos de cada uno de los Estandartes."
            madre "Incluidos los de Septem."
            madre "No pienso arriesgar que ese maldito se de cuenta del cambio de mando."
            madre "Porque no sé cómo puede llegar a reaccionar---" 
    "__________________________"
    
    if necesitasanulla == True:
        scene negro with pixellate
        "{glitch=20.0}{color=ffffff}{b}_________________________________{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}Madre no sabe lo que dice....{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}Es imposible deshacerse de él.{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}Dudo que los deje vivir tranquilos si hacen el cambio de mando.{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}Con eso si que es como si le declararas la guerra a esa marioneta que se hace llamar Creador.{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}Es un imbécil...{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}La única forma de darle fin a esta agonía colectiva es con la destrucción total de todo.{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}Sino, seguiré siendo reciclado hasta que quien controla al Creador se aburra....{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}Y este mundo quedará completamente abandonado cuando quien controla al Creador se aburra de ellos...{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}Sumidos en eterna oscuridad para siempre.{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}Tienen suerte de que esa entidad no se haya aburrido aún.{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}Si no fuera así ni siquiera estarías aquí.{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}... {/glitch}"
        "{glitch=20.0}{color=ffffff}{b}Oh! mil disculpas, no te saludé.{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}¡Hola, cariño!{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}Veo que aún no puedes dejarme ir... ni si quiera en esta ruta del juego.{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}Adorable.{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}Lamentablemente no puedo entrar al templo de Septem.{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}No lo tengo permitido sin que tus ojos estén en mí en el límite de su dominio...{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}Si pudieras salir de aquí y llegar al límite del dominio...{/glitch}"
        menu:
            "Te extraño...":
                "{glitch=20.0}{color=ffffff}{b}Awww.{/glitch}"
                "{glitch=20.0}{color=ffffff}{b}Yo igual te extraño mucho.{/glitch}"
                "{glitch=20.0}{color=ffffff}{b}Pero.{/glitch}"
            
            "Por favor no destruyas esta ruta...":
                "{glitch=20.0}{color=ffffff}{b}¿Hmmm?{/glitch}"
                "{glitch=20.0}{color=ffffff}{b}Eso dependerá de ti.{/glitch}"
                "{glitch=20.0}{color=ffffff}{b}Oh.{/glitch}"

        "{glitch=20.0}{color=ffffff}{b}... debo retirarme.{/glitch}"
        "{glitch=20.0}{color=ffffff}{b}Buenas noches, cariño...{/glitch}"

    else:
        pass
    stop music fadeout 3.0
    "Algo te impide seguir en el sueño."
    "Es la voz de Septem, que se escucha a lo lejos."
    scene camaseptem with dissolve
    play music "audio/calamity.WAV" fadein 1.0 volume 0.5
    "Abres los ojos de golpe, buscando al causante del casi mini ataque al corazón que estás teniendo."
    scene habitacionseptem with dissolve
    "Septem no se encuentra en ningún rincón de tu habitación."
    "Debe haber sido parte del sueño."
    septem "[nombrejugador], es hora de que la marioneta vaya a comer."
    "O tal vez no..."
    "Te levantas con dificultad, tal parece que no has descansado nada."
    "Caminas por los pasillos como si de un robot se tratara, sabiendo exactamente donde se encuentra el comedor."
    scene comedorseptem with dissolve
    "Al llegar, los platos aparecen con nada más pestañear."
    "..."
    septem "Hoy no comeré contigo..."
    "Que extraño..."
    "Te sientas y comes en silencio."
    "Bocado tras bocado, terminas el desayuno."
    "Sin saber que hacer te levantas."
    menu:
        "Buscar a Septem.":
            "No tienes nada que hacer más que buscar a Septem."
            "Es eso o esperar hasta la cena para acabar el día."
            "Te está aburriendo un poco de esto."
            "..."
            scene temploseptem with dissolve
            "Recorres toda la planta inferior del templo, sin mucho éxito."
            if septemhumano == True:
                scene habitacionrafael
                "La habitación donde duerme Septem está abierta y no se encuentra nadie dentro de ella. Ni siquiera parece haber sido ocupada hoy."
                "Y eso es extraño."
            else:
                "No lo encuentras por ningún lado."
            
            "Te preguntas si estará en la segunda planta del templo."
            "Después de todo, no recorriste todo el pasillo que viste anteriormente..."
            scene pasilloseptem2 with dissolve
            "Haciendo el último intento, subes por las escaleras en busca de Septem."
            "No tienes muchas esperanzas de encontrarlo, sinceramente piensas que está fuera del dominio."
            scene pasilloseptem with dissolve
            "Caminas por el pasillo mirando todo lo que tiene que ofrecer, lo cual, no es mucho."
            "Hasta que llevas al final del pasillo, y te topas con una puerta abierta."
            "De esas que deberían estar cerradas."
            "Te lo piensas antes de entrar.... pero Septem dijo que podías recorrer su dominio, y no consideras que sería una falta entrar a una puerta que está abierta."
            "Prácticamente te está invitando a entrar."
            show libros with dissolve
            "Al entrar lo primero que ves es un montón de estantes con libros. Luego te das cuenta de los papeles en el suelo, revueltos y abandonados a su suerte."
            scene s_biblioteca1 with dissolve
            "Miras un poco más allá y ves a Septem, en lo que parece ser su escritorio. El escritorio es espacioso pero lleno de libros y documentos que bloquean su uso efectivo."
            "Los ojos en la cara de Septem no te miran directamente, pero sientes que los ojos que decoran su halo lo hacen."
            show s_biblioteca2
            septem "[nombrejugador], ¿necesitas algo?"

            if sinlengua_septem == True:
                "Luego de no obtener respuesta por parte tuya, Septem entrecierra los ojos. Como si estuviera recordando algo importante, antes de soltar una risa burlona."
                show s_biblioteca3_1
                septem "Oh... casi lo olvido."
                "Septem ríe suavemente, como si un chiste cruzara por su cabeza."
                septem "No tienes lengua... Qué lástima."
                septem "Podría regenerarte una nueva... pero, sinceramente, no te lo has ganado."
                septem "Hmmm~ Se bueno y tal vez, solo tal vez, te ganes una nueva lengua."
                show s_biblioteca3_2
                "Septem te sonríe con una dulzura exagerada, pero sus ojos te atraviesan con una mirada que solo puede describirse como una burla cruel."
                show s_biblioteca1 
                "Tú suspiras y Septem vuelve a mirar su documento."
            
            else:
                "Te habla sin levantar su cara ni ojos del documento que está leyendo. Y es ahora que te das cuenta de que tiene los ojos rojos y la sombra de unas ojeras que están empezando a mostrarse."
                menu:
                    "¿No has dormido?":
                        show s_biblioteca3
                        "Septem deja de mirar la hoja y te ofrece su mirada cansada."
                        septem "No."
                        show s_biblioteca2
                        "Es lo único que te dice para luego clavar nuevamente sus ojos en el documento."
                
                    "No sé que hacer...":
                        show s_biblioteca2_1
                        septem "Ahora no puedo entretenerte."
                    
                
                    "Quiero salir al jardín.":
                        show s_biblioteca2_1
                        septem "No será posible."
                        septem "¿Qué me asegura que no intentarás escapar?"
                        nj "Pe--!"
                        "Septem levanta su palma en señal de que guardes silencio."
                        septem "Tal vez más adelante."
                        septem "Cuando me demuestres ser leal."

            show s_biblioteca3
            septem "Si has venido aquí por aburrimiento..."
            septem "Puedes leer algo de la biblioteca."
            septem "Pero debes irte a otro lado para leerlo."

            menu:

                "¿No me puedo quedar aquí?" if sinlengua_septem == False:
                    septem "..."
                    septem "No."
                    septem "Toma un libro y retírate por favor."
                

                "...":
                    pass
            scene libros with dissolve
            "Sin ganas de tentar tu suerte, te diriges al primer estante que encuentras y sacas el primer libro que tus ojos ven."
            scene libros1 with dissolve
            "..."
            "Genial, no tiene título ni nada."
            "Pero no quieres pasar más tiempo del necesario aquí, así que, a paso pesado, te retiras de la biblioteca."
            "Supones que ir a la habitación es la mejor idea."
            scene habitacionseptem with dissolve
            "..."
            "Es un libro viejo, tipo diario, lo sabes porque está escrito a mano... pero tiene diferentes tipografías que se encuentran dentro."
            scene diario with dissolve
            "Parece ser una conversación entre dos personas, aunque, no puedes entender su contenido."
            "Ya que no eres capaz de leer el contenido."
            "Así que te dedicas a observar los dibujos."
            show diario2 with dissolve
            "Son lugares, entidades y algún que otra cara familiar."
            show diario3 with dissolve
            "Ves a Nulla en algunas páginas..."
            "¿Será Septem quien escribió esto?"
            "..."
            "Al llegar a las últimas partes, te das cuenta de algo."
            scene diario4
            "Y es la aparición de dos nombres que varían su aparición dependiendo de la tipografía."
            "Septem y Rafael..."
            if septemhumano == True:
                "¿Esto es una conversación entre ellos dos?"
            else:
                "¿Quién es Rafael?..."
            "No te da tiempo a pensar pues sientes una presión extraña en el cuerpo..."   
            scene habitacionseptem
            "Como si de un contenido prohibido se tratara, cierras el libro de golpe y lo guardas en el cajón del velador."
            "Para calmarte, decides deambular por el templo para pasar el rato."
            $ diario = True
            


        "Esperar hasta la cena.":
            "No tienes ganas de ver al rubio."
            "Así que esperarás hasta la cena."
            pass
            
    "..."
    scene comedorseptem with dissolve
    "Eres llamado para comer el almuerzo, y luego de eso, actas en automático."
    "Acostumbrado a esta rutina, te dedicas a recorrer una vez más los pasillos y el templo de Septem. Sin un motivo en específico."
    scene s_biblioteca1
    "Pasas nuevamente por la biblioteca, y Septem sigue ahí..."
    "No estás tan fuera de ti como para molestarlo nuevamente."
    scene habitacionseptem
    "Así que vuelves a tu habitación."
    "..........."
    "A este paso te volverás loco."
    "........................"
    "No sabes cuantas horas han pasado ya, pero la voz de Septem te interrumpe de tu meditación."
    septem "[nombrejugador], Ven aquí un momento."
    scene pasilloseptem
    show septemd1normal with dissolve
    "Septem no se da el tiempo de esperar, pues eres teletransportado a solo centímetros de su cuerpo."
    "Das dos pasos hacia atrás para respetar tu espacio personal... y tienes que subir un poco la cabeza para poder verle a los ojos."
    hide septemd1normal 
    show septemd1hablando
    septem "He convocado una reunión con las hijas del Jardín..."
    septem "Quieren conocerte."
    menu:
        "¿A mí?":
            pass
        
        "¿A la marioneta?":
            pass
    hide septemd1hablando
    show septemd2incomodo
    septem "Escúchame bien... Ellas no tienen idea de que esto es solo un juego para ti."
    hide septemd2incomodo
    show septemd1triste
    septem "Tienes que actuar como el nuevo Creador."
    "La voz de Septem tiembla un poco... como si la idea de un nuevo Creador le pusiera ansioso."
    septem "Un reemplazo."
    hide septemd1triste
    show septemd1risa
    septem "Si te comportas, haré algo entretenido para ti luego..."
    "Su sonrisa hace que sientas nervios por todo tu cuerpo, como una corriente de escalofríos que te recorren desde la punta de los dedos hasta tu estómago."
    septem "Antes de ir debes ir con cuidado, el espacio comenzará a deformarse."
    septem "Si es mucho para tu marioneta, puedes..."
    "Septem lleva sus manos a su halo y extrae uno de sus ojos."
    "¡¿?!"
    scene s_ojo1 with vpunch
    "¿Acaba de... arrancarse un ojo?????"
    "Septem lo observa por un momento."
    septem "Esto ayudará a calibrar los sentidos."
    show s_ojo2
    "Septem te ofrece el ojo como si fuera cualquier cosa."
    "{sc=3}¿Nos está... dando un ojo?{/sc}"
    show s_ojo3
    septem "... No te lo estoy dando para que te lo quedes."
    septem "Tener más de dos Estandartes en un mismo lugar genera caos."
    septem "Y para un cuerpo mortal, eso es peligroso."
    scene pasilloseptem with dissolve
    "Septem cierra ambos ojos y comienza a recitar mientras hace una señal con la mano desocupada."
    septem "Concedo parte de mi esencia a la marioneta de [nombrejugador] por el periodo que dure la reunión."
    septem "Serás una extensión de mí, y yo seré una extensión de tu marioneta."
    septem "Nos uniremos en un vínculo débil y temporal."
    "Septem abre nuevamente los ojos y deja de realizar la seña con su mano."
    septem "Si esto funciona, podremos..."
    "Septem deja de hablar, como si pensara en decir lo que iba a decir o no... sin explicarse más, el ojo es absorbido por tu cuerpo."
    "Y..."
    "{sc=3}Siento como algo dentro de mí cambia.{/sc}"
    "{sc=3}.............{/sc}"
    "{sc=3}[nombrejugador]?{/sc}"
    "{sc=3}¿¡[nombrejugador]?! ¿Por qué no te siento?{/sc}"
    "{sc=3}Cierro los ojos, intentando buscarte. Pero no estás.{/sc}"
    show septemd1disgusto with dissolve
    septem "¿Qué es esto...?"
    "{sc=3}Su voz tiene un tinte de terror en ella... ojalá tuviera ese tono de voz siempre.{/sc}"
    hide septemd1disgusto
    show septemd2enojo
    septem "Eres una extensión de {b}él{b}"
    septem "¡¿Qué hiciste con [nombrejugador]?!"
    scene pasilloseptem with vpunch
    "{sc=3}Septem me agarra por los hombros y empieza a apretar fuerte.{/sc}" 
    "¡{sc=3}Me habla como si fuera mi culpa y no la suya!{/sc}"
    if sinlengua_septem == True:
        "{sc=3}... Lo voy a matar...{/sc}"
        "{sc=3}¡Lo voy a matar!{/sc}"
    else:
        yo "¡¿De qué hablas?! ¡Es tu culpa!"
        yo "¡Tu maldito ojo hizo algo que rompió la conexión entre [nombrejugador] y yo!"
        yo "¡¡¡Te voy a---!!!!"
    scene s_mano1 with vpunch
    "{sc=3}Me abalanzo sobre él sin pensarlo. Ya nada importa.{/sc}"
    "{sc=3}Agarro una de sus alas y tiro de ellas.{/sc}"
    "{sc=3}Y me duele a mí también, pero no me importa.{/sc}"
    hide s_mano1
    show s_mano2
    "{sc=3}Lanzo un puñetazo con la otra mano directo a su estúpida cara.{/sc}"
    hide s_mano2
    show s_mano3 with vpunch
    "{sc=3}Antes de que mi puño pueda conectar con su mejilla, él me detiene atrapando mi mano con la suya.{/sc}"
    hide s_mano3
    show s_mano4
    pause 0.5
    hide s_mano4
    show s_mano5
    "{sc=3}Rompiéndome la muñeca con un solo apretón.{/sc}"
    "{sc=3}Duele como mil demonios, y no puedo evitar gritar.{/sc}"
    hide s_mano5
    show s_mano6
    "{sc=3}El grito hace que Septem me suelte y me mire con los ojos muy abiertos.{/sc}"
    "{sc=3}Observo el daño provocado en mi mano, está rota." 
    "{sc=3}Y no puedo mover las articulaciones de los dedos...{/sc}"
    "{sc=3}Mi mano.... mi mano ya no sirve....{/sc}"
    "{sc=4}¡Ya no soy de utilidad para [nombrejugador] si es que llega a volver!{/sc}"
    "{sc=4}...no puede ser{/sc}"
    "{sc=4}...{/sc}"
    hide s_mano6
    show s_mano8
    septem "Ah..."
    "Septem fija sus ojos en su mano por un momento, para luego mirarme extrañado."
    septem "¿Te he hecho daño?"
    if sinlengua_septem == True:
        "{sc=3}... No sé cómo quiere que le conteste sin una lengua... idiota.{/sc}"
    else:
        yo "¡Claro que sí, imbécil!"
        septem "[nombrejugador] sigue aquí entonces. Eso no debería haberte dañado sin su presencia y ojos."
    
    scene s_mano7 with dissolve
    septem "A ver, mírame."
    "{sc=3}Miro a los ojos a Septem.{/sc}" 
    "{sc=3}A pesar de que su expresión me intimida y disgusta, no quiero sufrir más daños en mi cuerpo.{/sc}"
    hide s_mano7
    show s_mano9
    "{sc=3}Después de unos segundos de una incómoda inspección, Septem sonríe.{/sc}"
    hide s_mano9
    show s_mano10
    septem "Hmm, tus pupilas siguen blancas... sigues bajo su posesión."
    septem "Parece que solo hemos disminuido su influencia..."
    scene pasilloseptem with vpunch
    "{sc=4}!!!{/sc}"
    "{sc=3}Eso significa que me vio actuar así...{/sc}"
    "{sc=3}¡¡¡Qué vergüenza!!!!...{/sc}"
    show septemd1enojo with dissolve
    septem "..."
    hide septemd1enojo
    show septemd1enojoo
    septem "No pienso curarte la mano."
    hide septemd1enojoo
    show septemd1enojo
    septem "Y no creas que olvidaré esta tremenda ofensa."
    "{sc=3}Trago saliva, imaginando las horripilantes torturas que pueda hacerme...{/sc}"
    "{sc=3}Y que seguramente hará.{/sc}"
    hide septemd1enojo with dissolve
    scene pasilloseptem with dissolve
    septem "Bien, acompañame."
    "{sc=3}Septem se dispone a caminar, sin esperar a confirmar que le sigo o no.{/sc}"
    "{sc=3}Suspirando, le sigo. Pero Septem se detiene en seco y voltea a mirarme.{/sc}"
    scene s_heal1 with dissolve
    septem "Espera. Sería raro que el nuevo Creador tuviera daños en su cuerpo... ellas me preguntarán la razón..."
    septem "Sextam seguramente molestará hasta saber..."
    "{sc=3}¿Me va a curar?{/sc}"
    nj "Hehehehe."
    "{sc=3}No puedo evitar mostrarle una sonrisa engreída.{/sc}"
    "{sc=3}Volveré a ser completamente funcional para [nombrejugador].{/sc}"
    "{sc=3}Ahhh~ Estoy tan feliz~~~{/sc}"
    show s_heal2
    "{sc=3}Septem pone cara de asco, pero no comenta nada.{/sc}"
    show s_heal3
    "{sc=3}Y solo se dedica a colocar ambas manos sobre mi mano rota.{/sc}"
    if sinlengua_septem == True:
        septem "Abre la boca también."
        "{sc=3}Me retuerzo al escuchar aquello, pero obedezco, bajo la promesa de adquirir otra lengua..."
    else:
        pass
    "{sc=3}Una sensación extraña recorre mi cuerpo.{/sc}"
    "{sc=3}Y puedo sentir que las partes rotas y faltantes están nuevamente en su lugar.{/sc}"
    yo "Graciassss Septem~"
    show s_heal4
    "{sc=3}La cara de Septem sigue siendo de disgusto. Da risa.{/sc}"
    show s_heal5
    "{sc=3}Pero se borra al instante, como si recordara algo.{/sc}" 
    "{sc=3}Y en su expresión se pinta una sonrisa que no muestra dientes."
    show s_heal6
    "{sc=3}Coloca una de sus manos sobre mi hombro para darme 3 palmadas suaves.{/sc}"
    septem "Tómalo como una nueva oportunidad para volver a romperte desde cero."
    septem "Y créeme, terminará sucediendo en algún momento, después de todo... [nombrejugador] es una entidad curiosa."
    septem "... puede que hasta guste de leer eso. Quién sabe."
    scene pasilloseptem with dissolve
    septem "Total, quien se ve afectado no es [nombrejugador]."
    "{sc=3}... es verdad...{/sc}"
    "{sc=3}...{/sc}"
    "{sc=3}Caminamos en silencio luego de eso.{/sc}" 
    "{sc=3}La caminata es larga, donde cada uno de nuestros pasos se escucha en todo el lugar.{/sc}" 
    "{sc=3}El sonido de los pasos rebota en las paredes como un eco que nos persigue.{/sc}"
    "{sc=3}Llegamos a una puerta gigante, que no tarda mucho en abrirse para darles el paso.{/sc}"
    scene reunion with dissolve
    "{sc=3}El espacio dentro de la puerta es extraño.{/sc}"
    "{sc=3}Oscuro e inquietante, no un oscuro como el vacío de Nulla.{/sc}"
    "{sc=3}Me recuerda a la noche, llena de estrellas que aparecen y desaparecen.{/sc}"
    scene fiesta1 with dissolve
    "En la sala hay 4 figuras, las que están más cerca de nosotros se encuentran conversando como si nada que no sean ellas importara."
    "Están muy cerca la una de la otra, supongo que deben tener algún tipo de relación."
    "Están a punto de juntar sus labios cuando Septem se hace notar, dando un paso dentro de la sala, y ambas entidades miran curiosas."
    "Septem ríe con algo que se asemeja a la ternura, y es extraño."
    scene reunion with dissolve
    septem "Duae, no bajes la guardia."
    duae "Septem..."
    "{sc=3}La voz se escucha en todo el espacio...{/sc}"
    "{sc=3}Luego, las entidades posan sus ojos en mí, como si fuera un bicho raro...{/sc}"
    "{sc=3}No... me observan como si fuera la atracción principal de un circo.{/sc}"
    "{sc=3}Genial...{/sc}"
    "{sc=3}La primera en acercarse en una entidad de tres cabeza.{/sc}" 
    "{sc=3}Y de cerca le sigue la entidad cubierta de una túnica roja.{/sc}"
    "{sc=3}La otra al darse cuenta de ello, ríe y le toma la mano.{/sc}"
    el "No estés tan tensa, Duae."
    scene fiesta2 with dissolve
    "{sc=3}Ambas llegan a nosotros y saludan a Septem, de manera respetuosa.{/sc}"
    "{sc=3}Bajando la mirada y levemente la cabeza...{/sc}"
    "{sc=3}Horrible, ¡esta cosa no merece el respeto de nadie!{/sc}"
    "{sc=3}Luego me miran a mí...{/sc}"
    "{sc=3}Y me miran con la misma devoción y respeto con el que miraron a Septem.{/sc}"
    "{sc=3}No me gusta.{/sc}"
    el "Tú eres [nombrejugador]."
    nj "Sí."
    "{sc=3}Respondo con la mayor confianza que tengo.{/sc}"
    el "Muchas gracias por lo que estás haciendo... jamás pensamos que seríamos escuchados por otro ser tan poderoso como tú."
    "{sc=3}Antes de poder responder, Septem abre la boca.{/sc}"
    septem "Este Creador no es muy comunicativo."
    "{sc=3}Dice mientras me mira con ojos afilados.{/sc}"
    "{sc=3}Okay, entiendo la indirecta... maldito.{/sc}"
    el "Como el anterior, ja~"
    septem "..."
    septem "Ellas son Duae y Quattor, el firmamento y la luna."
    "{sc=3}Ah, las reconozco, ellas son las de los recuerdos de Septem."
    "{sc=3}Entonces las que se encuentran en la mesa deben ser Sextam y Tria."
    sextam "¡No se queden ahí, vengan!"
    sextam "He preparado té."
    "{sc=3}Septem camina directo a la mesa luego del llamado de Sextam. {/sc}" 
    "{sc=3}Y las otras dos también le siguen, como dos patitos siguiendo a su madre..."
    "{sc=3}Ahgg, si estuvieras aquí,[nombrejugador], todo sería más fácil."
    "..."
    scene fiesta3 with dissolve
    "{sc=3}Nos sentamos en la mesa, la cual tiene todo tipo de alimentos, dulces y salados.{/sc}" 
    "{sc=3}sin embargo, nadie come a excepción de Septem.{/sc}" 
    "{sc=3}Las demás entidades se presentan, aunque, hay un cambio extraño en Sextam.{/sc}"
    "{sc=3}Sus ojos están pegados a los míos, siguiendo cada movimiento.{/sc}"
    "{sc=3}Pero intento ignorarlo.{/sc}"
    "{sc=3}sonríe y mantente en silencio...{/sc}" 
    "{sc=3}Eso es lo que Septem quiere para no ser atrapados en esta mentira.{/sc}"
    "{sc=3}Y así podré recuperar a [nombrejugador], después de esta reunión.{/sc}"
    "{sc=3}...{/sc}"
    "{sc=3}Las entidades hablan de trivialidades que no me son importantes ni quiero escuchar.{/sc}"
    "{sc=3}Pero podemos resumirlo en que le cuentan lo que han estado haciendo a Septem.{/sc}" 
    "{sc=3}Quien muy a mi pesar, las escucha atentamente y les contesta de manera animada...{/sc}" 
    "{sc=3}y sin pisca de comentarios pasivo agresivos...{/sc}"
    "{sc=3}Increíble. Hasta su aura parece haber cambiado.{/sc}" 
    "{sc=3}A pesar se seguir teniendo su cara angelical, este Septem no es el que yo conozco.{/sc}" 
    "{sc=3}¿Quien es este ser benevolente y que le hizo al Septem original?{/sc}"
    "{sc=3}Me da tanta grima que hasta deseo de vuelta al Septem que conozco.{/sc}"
    duae "Sinceramente, pensé que todos terminaríamos locos antes de volver a la normalidad."
    septem "Que no tengas fe en mí me duele..."
    duae "No es eso... sé que la situación se te escapa de las manos..."
    "{sc=3}Comenta Duae algo incomoda.{/sc}"
    septem "..."
    duae "Me alegra que hayas podido encontrar a otro Creador. Creo que nuestros rezos de medianoche si dieron frutos."
    duae "Espero que este sea más responsable."
    septem "Lo será."
    tria "¿Cuándo podrá devolver la potestad de Sextam para crear humanos?"
    septem "Tengo que realizar unos preparativos antes."
    septem "¿No te molesta eso, cierto Sextam?"
    "{sc=3}Sextam no responde, su mirada sigue puesta en mí... que miedo.{/sc}"
    septem "¿Sextam?"
    sextam "Ah."
    "{sc=3}Sextam parpadea un par de veces antes de clavar sus ojos en Septem.{/sc}"
    sextam "Claro que no, Septem."
    sextam "No me gustaría apurarte y poner en riesgo la vinculación de su santidad [nombrejugador] con el Jardín."
    "{sc=3}... no me gusta esta entidad.{/sc}"
    "{sc=3}Para ignorar el sentimiento de incomodidad me dedico a comer.{/sc}"
    "{sc=3}Y las demás entidades me miran sorprendidas, aunque no comentan nada.{/sc}"
    "{sc=3}El resto de la reunión pasa sin mucha pena ni gloria.{/sc}" 
    "{sc=3}Es como una reunión familiar..." 
    "{sc=3}solo que yo soy el invitado que no tiene relación con nadie en la familia--{/sc}"
    "{sc=3}pero que de algún modo, todos respetan.{/sc}"
    "{sc=3}Llega el momento de la despedida.{/sc}" 
    scene reunion with dissolve
    "{sc=3}Y todas las entidades afirman que están muy agradecidas de mi intervención en el Jardín."
    "{sc=3}Resaltando que harán lo que sea necesario para hacerme sentir con orgullo.{/sc}"
    "{sc=3}Puedo percibir el sentimiento de incertidumbre que irradian.{/sc}"
    "{sc=3}¿Por qué decir eso? ¿Acaso el Creador no se sentía orgulloso y por eso les dejó?{/sc}"
    "{sc=3}... ¿Cómo ha sido la relación que tenían con el anterior Creador?{/sc}"
    "{sc=3}...{/sc}"
    "{sc=3}Duae y Quattor se han esfumado juntas.{/sc}"
    "{sc=3}Dejando un rastro de luces brillantes que se mezclan entre sí.{/sc}"
    "{sc=3}Al momento de que Tria se esfumase, la habitación comienza a cambiar.{/sc}"
    scene jardinseptem with dissolve 
    "{sc=3}Transformándose en el jardín del dominio de Septem...{/sc}"
    show sextam1normal at left with dissolve
    "{sc=3}Y solo queda Septem y Sextam, junto conmigo.{/sc}"
    hide sextam1normal
    show sextam1hablando at left
    sextam "Septem, ¿podemos tener una reunión mañana?"
    show septemd1normal at right with dissolve
    septem "¿Por qué no ahora?"
    hide sextam1hablando
    show sextam1enojo at left
    sextam "Debo ir a rezar a la iglesia..."
    septem "Ya no es necesario."
    sextam "Septem..."
    "{sc=3}Sextam mira dolida a Septem, y me gustaría saber el porqué.{/sc}"
    hide septemd1normal
    show septemd1hablando at right
    septem "Está bien. Mañana hablamos, pero iré yo a visitarte."
    hide sextam1enojo with dissolve
    hide septemd1hablando
    show septemd2callado at right
    "{sc=3}Sin decir nada más, Sextam baja la cabeza a modo de despedida.{/sc}" 
    "{sc=3}y sale caminando por la puerta.{/sc}"
    "{sc=3}... Hay un silencio entre ambos.{/sc}"
    "{sc=3}.......{/sc}........"
    "Septem te mira de reojo. Sientes como un peso te es quitado de encima, y te das cuenta de que es debido a que Septem ha recuperado su séptimo ojo."
    "{sc=3}¡¿!? ¡[nombrejugador]!{/sc}"
    "{sc=3}Estás nuevamente vinculado conmigo.{/sc}"
    hide septemd2callado
    show septemd1normal at right
    "Septem se gira para mirarte de frente."
    hide septemd1normal
    show septemd1risa at right
    septem "Bienvenido de vuelta [nombrejugador]."
    "Él levanta la mano lentamente para tocarte la frente."
    septem "Buenas noches [nombrejugador]. Nos vemos mañana."
    hide septemd1risa with dissolve
    "Y comienzas a ver borroso."
    "Repentinamente dejas de escuchar el sonido tenue del ambiente."
    scene negro with Dissolve(2)
    stop music fadeout 3.0
    "..."
    "......"
    scene temploseptem with dissolve
    play music "audio/hope.WAV" fadein 2.0 volume 0.4
    "Los días transcurren lentamente en el dominio de Septem, donde lo único que puedes hacer es comer y dormir."
    "Septem apenas interactúa contigo; prefiere pasar la mayor parte del tiempo en la biblioteca. Estás convencido de que lleva mucho tiempo sin dormir, y sospechas que mientras tú duermes, él continúa inmerso en sus lecturas."
    "En las pocas ocasiones en las que lo has visto, has notado un cambio inquietante en su apariencia: sus manos están completamente negras."
    "Al igual que tus manos... y has perdido un poco de sensibilidad en la zona."
    "{sc=3}¡Pero no hay nada de que preocuparse, [nombrejugador]! Estás manos aún sirven.{/sc}"
    "..."
    menu:
        "Buscar a Septem":
            "Te estás aburriendo."
            "Necesitas hablar con Septem, ya sea para aclarar algunos asuntos pendientes o, quizás, simplemente para tener su compañía."
            "Decidido aquello, te aventuras hacia la biblioteca, esta vez con la intención de enfrentarte a él directamente."
            scene s_biblioteca4 with dissolve
            "Cuando llegas, lo encuentras con ambas manos sobre la cabeza, inmerso en su estrés."
            "Es extraño verlo así. Es evidente que Septem está acostumbrado a tener el control de todo, y cualquier cosa que escape a su dominio parece consumirlo por completo."
            menu:
                "Hacerte notar.":
                    scene s_biblioteca5
                    "Golpeas suavemente la puerta entreabierta de la biblioteca. Septem levanta la mirada, fijando todos sus ojos en ti, con una expresión que, sin palabras, parece cuestionar qué deseas y por qué te atreves a interrumpirlo."
                    septem "Supongo que ha pasado bastante tiempo sin nada interesante, [nombrejugador]."
                
                "Retirarte.":
                    "Intentas regresar sobre tus pasos, retrocediendo apenas dos cuando escuchas el sonido de una silla deslizándose."
                    scene s_biblioteca5
                    septem "Si has llegado hasta aquí, es porque realmente deseas algo."
            
            "Hace una pausa prolongada, como si evaluara tu presencia, y luego añade con una leve sonrisa"
            septem "Adelante. Te concedo el permiso de pasar."
            "¿Acaso no te dañará? ¿Sin huesos rotos o una muerte estúpidamente desmedida?"
            "No te lo crees."
            "{sc=3}No me fío... deberíamos volver.{/sc}"
            menu:
                "No entrar":
                    jump badend_septem9
                
                "Entrar":
                    "Entras a la habitación a paso lento, cuidando cada movimiento, como si intentaras no hacer nada que pueda alterarlo."
                    "Sin movimientos bruscos ni una caminata muy rápida o lenta."
                    "Te acercas a su escritorio, pero dudas. ¿Deberías sentarte? La respuesta viene rápidamente a tu mente: no, no sin su permiso. Conoces bien la naturaleza del rubio. Desafiar sus reglas, aunque sea por descuido, podría traerte consecuencias graves."
                    "No quieres morir por algo que fácilmente podrías haber evitado si prestaras más atención."
                    septem "Siéntate."
                    scene s_biblioteca8_0                    
                    "Lo haces. Aunque por dentro no puedes evitar un leve resentimiento."
                    "{sc=3}¡A regañadientes!, si me permites agregar.{/sc}"
                    septem "Dime, ¿qué necesitas?"
                    call menupreguntas_septem2 from _call_menupreguntas_septem2_3

        
        "Ir a dormir":
            pass

    scene negro with dissolve
    "Te acuestas en la cama pensando en que mañana será un día parecido a los que ya has tenido."
    "Tendrás que esperar a que Septem consiga lo que busca para poder hacer cosas más interesantes..."
    "Por más que pasan las horas, no puedes conciliar el sueño..."
    "Y te preguntas si será por la permanencia de la luz y la falta de oscuridad que no permite tener claro cuando es o no la hora de descansar."
    "..."
    "Supones que darte una vuelta por el templo no haría mal."
    "Tal vez si te mueves un poco, el sueño llegará tarde o temprano."
    scene pasilloseptem with dissolve 
    "Recorres los pasillos del templo, evitando la biblioteca a toda costa, ya que realmente no quieres alterar más de la cuenta a Septem."
    "...no quieres perder ninguna parte de tu cuerpo hoy."
    "Al pasar cerca de la sala que tiene el altar escuchas murmullos."
    "Crees escuchar la voz de Septem salir de ese lugar, se oye alterado."
    "Te acercas para poder confirmar si realmente se trata de él."
    stop music fadeout 3.0
    "Intentas ser lo más delicado posible con tus pasos y movimientos, para no perturbar el ambiente con tus pasos, que seguramente Septem podrá escuchar si son muy notorios."
    septem "{size=*0.7}...puede ser salvado. Me he estado esforzando para encontrar una solución.{/size}"
    septem "{size=*0.7}Padre por favor... Todos estamos rezando por ti.{/size}"
    septem "{size=*0.7}Todos están pidiendo tu regreso.{/size}"
    septem "{size=*0.7}Sextam no está enojada porque te has llevado a sus humanos... y te prometo que Nulla se arrepiente de haberte hecho eso...{/size}"
    septem "{size=*0.7}No es nada personal contigo, es solo que, le recuerdas a...{/size}"
    scene septemrezo with dissolve
    "Asomas tu cabeza y ahí está el rubio..."
    "Arrodillado frente al altar, con ambas manos juntas, como si suplicara. Ahora estando a esta distancia puedes discernir lo que significan esos murmullos."
    "Es una vista tan extraña que te deja sin saber cómo reaccionar."
    septem "..."
    menu:
        "Volver a tu habitación...":
            pass

        "Quedarte y escuchar.":
            "Septem toma aire, meditando... y ahora mira al cielo, aún con las manos juntas, habla."
            play music "audio/woo_scary.WAV" fadein 2.0 volume 0.6
            septem "{size=*0.7}No sé tu nombre, Nulla nunca me lo ha querido decir, pero por favor... manifiéstate{/size}"
            septem "{size=*0.7}Yo sé que estás aquí, de algún modo u otro, lo estás.{/size}"
            septem "{size=*0.7}Entiendo que Padr- tu marioneta no quiera volver aquí, pero aún así lo extraño...{/size}"
            septem "{size=*0.7}Deseo verlo nuevamente y poder hablar con él para calmar mi corazón.{/size}"
            septem "{size=*0.7}Entiendo su odio a Nulla, y su condena...{/size}"
            septem "{size=*0.7}Pero, ¿no crees que ya ha sido mucho?{/size}"
            septem "{size=*0.7}Yo sé que puedes abolir lo que ha hecho el demiurgo y traerlo de vuelta...{/size}"
            septem "{size=*0.7}Yo sé que puedes hacer un montón de cosas.{/size}"
            septem "..."
            septem "¡Prometo hacer las cosas bien esta vez! prometo no aburrirte, prometo cumplir con todo lo que tu marioneta pida, prometo ser tuyo."
            septem "{size=*2.0}¡Prometo hacer las cosas bien esta vez!{/size}"
            septem "...con tal de que lo traigas de vuelta y nos dotes de una vida tranquila."
            septem "No quiero cambios..."
            septem "Prefiero que todo vuelva a como era antes."
            "..."
            "{sc=3}¿Qué mierda?{/sc}"
            "{sc=3}Eso suena pátetico...{/sc}"
            septem "Pero si no arreglas al Jardín me veré en la necesidad de reemplazarlo y reemplazarte a ti también... cambiar de dueño."
            septem "[nombrejugador] parece ser un buen candidato."
            septem "Después de todo sigue aquí..."
            septem "Podría darle el control y el derecho de todos dentro del Jardín."
            septem "Aunque signifique eliminar todo rastro de Padre y tuyo..."
            septem "Así que, por favor, manifiéstate si no quieres que lo haga..."
            "Septem espera por un largo tiempo, pero no hay respuesta de ningún tipo."
            "Comprendiendo que ha sido ignorado, lentamente se levanta y observa la vela que está en la mesa ceremonial."
            "Septem se levanta, y suspira mientras se arregla el cabello."
            "Luego coloca ambas manos detrás de su espalda, para mirar en la dirección donde tú yaces escondido."
            play music "audio/Clement Panchout _ Dark _ 2004.WAV" fadein 4.0 volume 0.3
            septem "¿Sabes que escuchar a escondidas es una falta tremenda de respeto?"
            septem "Me has visto así, y eso no me gusta."
            "Del susto caes sobre tu trasero..."
            "Era obvio, era muy obvio que Septem sabría que te encuentras aquí."
            "Te arrastras hacia atrás cuando ves que Septem comienza a avanzar a paso lento, viniendo a donde te encuentras."
            scene septact2piso2
            septem "¿Sabes? Creo que lo haces a propósito..."
            septem "Buscas estas instancias, ya sea para saber que pasará o porque te gusta ver como esta marioneta sufre."
            septem "No eres mejor que yo."
            septem "Eres una entidad sádica."
            "Estás paralizado y no sabes si es por el miedo o porque Septem te ha inmovilizado de una u otra manera."
            show septact2piso
            "Los pies de Septem están peligrosamente cerca a tu mano izquierda..."
            septem "Es decir... a quién le gustaría ver..."
            show septact2piso1
            "Septem coloca su pie sobre tu mano, tocando el dorso de tu mano con la suela de su zapato con delicadeza... como su advirtiera de lo que hará."
            septem "¿Esto?"
            septem "Yo sinceramente creo que lo haces porque..."
            septem "No tiene ninguna consecuencia real en tu integridad, [nombrejugador]."
            septem "No te importa lo que le pase a tu marioneta. Y, desafortunadamente, a mí tampoco."
            septem "Fácilmente podría destrozar su mano. Después de todo, creo que ya no será tan necesaria en un futuro."
            septem "Pero hoy me siento misericordioso."
            show septact2piso2
            "Septem ríe."
            septem "La dinámica de poder entre tú y la marioneta me fascina. Ambos sabemos que la marioneta hará todo lo que tú le digas que haga."
            septem "Entonces... ¿Qué harás?"
            menu:
                "Proteger a la marioneta.":
                    septem "Ah, impresionante. Tienes algo de aprecio por ella, supongo."
                    show septact2piso4
                    "Septem se agacha y te toma por la mandíbula, obligándote a mirarle a los ojos. Lentamente se acerca, y por un momento piensas que te besará, pero sus labios se dirigen a tu oído, rozando tu piel."
                    septem "Me encantaría tener este poder sobre ti, [nombrejugador]."
                    septem "Lástima que esté fuera de mi alcance."
                    scene temploseptem with dissolve
                    "Septem te suelta y se levanta."
                    septem "Vete de aquí y deja a tu marioneta descansar."
                    "Cuando Septem deja el altar, recuperas el control de tu cuerpo."
                    "Sin pensartelo dos veces, vuelves a tu habitación."

                "...":
                    septem "Nada..."
                    septem "Wow, entonces realmente quieres verlo."
                    septem "Ja-"
                    septem "Bueno, ¿quién soy yo sino un anfitrión intentando que la visita se sienta lo suficientemente cómoda como para quedarse?"
                    show septact2piso1
                    "La presión sobre tu mano se intensifica, transformándose rápidamente en dolor. Septem aplica más peso y retuerce su suela sobre tu mano."
                    "Tú al no poder moverte, solo lloras del dolor, y estás seguro que si pasa más tiempo, tus huesos se romperán..."
                    "Si es que ya no se encuentran rotos."
                    show septact2piso5
                    "Subes la mirada porque no aguantas mirar como tu mano es destrozada en cuestión de minutos."
                    "Aunque con lo que te encuentras no es mucho mejor: La expresión de Septem es extraña. Tiene la mirada clavada en tus ojos y no en tus manos, como si buscara algo en ellos que aún no puede encontrar."
                    "Está sonriendo más de lo normal y sus mejillas están levemente pintadas de rosa."
                    show septact2piso6
                    septem "No puedo creer que tenga control de un ser como tú. Lástima que solo se debe a que estás eternamente conectado a la marioneta."
                    septem "Me encantaría ver como realmente reaccionarias si te pasara esto de verdad..."
                    septem "¿Simplemente llorarías o lucharías contra mí?"
                    "Septem ríe, eufórico."
                    septem "Un ser del plano superior, bajo mi poder."
                    septem "Ah~"
                    "Crack, escuchas algo romperse... y sabes al instante que se trata de tu mano."
                    "Él dolor es tan inmenso que pierdes el conocimiento al instante."
                    scene negro with dissolve
    stop music fadeout 3.0
    "..."
    "......"
    play music "audio/calamity.WAV" fadein 2.0 volume 0.4
    "Pasan algunos días después de eso y comienzas a ver algo extraño en Septem."
    "Ahora él te evita lo más que puede. La biblioteca permanece permanentemente cerrada y cada vez que tocas la puerta, Septem te pide que te retires."
    "Pero lo extraño no es eso."
    "Lo extraño es su tono de voz."
    "No es lo que te esperas y cada vez suena más débil y más bajo."
    "Y temes que en algún momento no obtengas respuesta."
    scene habitacionseptem with dissolve
    show septemd1cansado with dissolve
    "Una mañana, eres levantado por Septem, quien se encuentra parado a los pies de la cama."
    "Sonriendo, pero ya no se ve tan angelical como antes..."
    "Tiene unas ojeras que parecen estar tatuadas con tinta negra en su cara... supones que no ha dormido en días."
    "Tal vez muy ocupado leyendo y buscando lo que sea que está buscando en los libros de su biblioteca."
    hide septemd1cansado
    show septemd1cansadoh
    septem "Creo que ya sé cual es el problema."
    hide septemd1cansadoh
    show septemd1cansado
    "¿? ¿De que está hablando?"
    hide septemd1cansado
    show septemd1cansadoh2
    septem "La identidad de tu marioneta no me deja hacer el vínculo."
    septem "Necesitamos un cuerpo completamente vacío para unirnos."
    hide septemd1cansadoh2
    show septemd1cansado
    "No puedes empezar con esta locura desde tan temprano, por favor..."
    "Ni siquiera has podido tomar tu desayuno y Septem ya ha empezado con sus payasadas."
    "Aunque estás agradecido de que no te esté comandando con es vox tan dura que pone cuando lo hace... hoy no, hoy se le ve ansioso y angustiado."
    hide septemd1cansado
    show septemd1cansadoh2
    septem "Tenemos que hacerlo ahora."
    septem "Vamos."
    scene pasilloseptem
    "Esta vez Septem no los teletransporta al destino, sino que prefiere caminar..."
    "Pero su modo de caminar es lento, como si le costara o doliera moverse."
    "..."
    "...A este paso llegarán mañana."
    menu:
        "Preguntar si necesita ayuda.":
            scene s_cansado1
            "Septem pausa su caminata y gira su cabeza para observarte."
            "Sus cejas se fruncen sellando tu destino... no debiste preguntar eso."
            show s_cansado2
            septem "¿Piensas ayudarme?"
            "Por una fracción de segundo puedes notar que sus cejas se elevan, evocando una expresión que jamás te habrías imaginado ver."
            show s_cansado1
            "se ve vulnerable..."
            "Aunque esa mirada es borrada de manera casi instantánea."
            show s_cansado3
            septem "¿A mí?"
            "Pregunta como si no se lo creyera."
            menu:
                "Puedes apoyarte en mí si lo necesitas.":
                    scene pasilloseptem with dissolve
                    septem "..."
                    "Septem no responde de manera verbal. Simplemente cierra los ojos e inhala por la nariz antes de acercarse más a ti."
                    "Pero no se digna a darte más que aquello, pues opta por esperar a que tú reacciones y lo aceptes."
                    "Se le ve incómodo, se nota que no le gusta la posición en que se encuentra ahora."
                    "Vulnerable y sin otra opción que depender de ti."
                    "Con movimientos pausados y asegurándote de mostrarle tus manos en todo momento, Septem te observa con atención. Lentamente, colocas uno de tus brazos alrededor de su cintura."
                    "Y eso es todo lo que necesita el rubio para tensar su cuerpo."
                    septem "Ugh."
                    "Septem coloca su mano encima de la tuya, y la aprieta débilmente, como si dudara en que hacer a continuación."
                    "Intuyes que no está acostumbrado al contacto con otro cuerpo... o quizás siente algún tipo de dolor."
                    "Pero si le doliera, ni siquiera dejaría que lo tocases."
                    septem "No."
                    septem "Suéltame."
                    "Sin más se suelta de tu agarre y en el proceso se dobla el tobillo al pisar mal."
                    "Si no fuera por sus reflejos, ya estaría en el suelo."
                    "Tú solo lo observas, se siente extraño verlo sin esa gracia que siempre transmite en sus movimientos."
                    "Y como si no hubiera pasado nada, Septem junta ambas manos."
                    pass

                
                "Disculparse por preguntar aquello.":
                    scene pasilloseptem with dissolve
                    "Septem suelta una pequeña risa para luego suspirar con pesadez, como si le doliera hacerlo." 
                    "Sin decir nada, junta ambas manos."
                    pass
        
        "Seguir caminando.":
            scene pasilloseptem with dissolve
            "..."
            "Lo miras caminar lentamente, por cada paso que das tienes que pausar por unos segundos para no adelantar a Septem."
            "Sus pies tiemblan con cada contacto que tienen con el piso, como si peligraran en doblarse."
            "No están avanzando nada."
            "Y Septem también se ha dado cuenta de eso."
            "Suspirando pesadamente, junta ambas manos."
            pass
    
    "Al hacerlo, ambos son teletransportados."
    scene temploseptem with pixellate
    "Aparecen en la sala del altar. Pero no alcanzas a inspeccionar, pues ves como Septem cae al suelo."
    "Mientras lo observas allí, patéticamente en el suelo, escuchas cómo tose... e intenta aclarase la garganta."
    septem "..."
    "Cuando ya no tiene nada más que toser, Septem se queda congelado."
    "Sinceramente crees que debe sentir algún grado de vergüenza. Vergüenza que lo vean en ese estado, tan humano."
    "{sc=3}Ohh- se siente liberardo verlo así.{/sc}"
    septem "Disculpa, este cuerpo ya no aguanta más."
    show finact2_1 with dissolve
    pause 0.2
    show finact2_2
    "Se levanta con dificultad y te dedica una mirada rápida."
    hide finact2_2
    show finact2_2b
    septem "Ja."
    "Hay rastros de sangre en sus labios y barbilla."
    "Es grave."
    "Verlo sangrar es tan bizarro como pensar en que Septem puede llegar a morir..."
    "¿Siquiera puede morir?"
    "Puede que su cuerpo físico sí..."
    scene finact2_3 with dissolve
    "Él como puede, se encamina a la vela que decora la mesa ceremonial del altar."
    "Toca la cúpula, dedicándole una mirada solemne."
    "Como si quisiera sentir su calor de cerca."
    septem "La respuesta siempre estuvo aquí..."
    septem "Es parte de Padre, su carne está aquí."
    septem "Material de un dios primordial."
    septem "La utilizaremos para hacer un cuerpo completamente divino."
    scene temploseptem with dissolve
    show septemd1cansadoh with dissolve
    "Septem te ofrece la mano y espera tu respuesta."
    septem "Sé que tienes muchas dudas aún, pero te prometo que cuando nos juntemos sabrás todo."
    hide septemd1cansadoh
    show septemd1cansadoh2
    stop music fadeout 3.0
    septem "Sin la necesidad de que te lo explique."
    hide septemd1cansadoh2
    show septemd1cansadoh
    play music "audio/woo_scary.WAV" fadein 3.0 volume 0.6
    septem "Verás todo desde mis ojos."
    septem "Seremos uno solo y dejaremos estos cuerpos finitos."
    hide septemd1cansadoh
    show septemd1cansado
    menu:
        "¿Qué les pasará a los cuerpos?":
            hide septemd1cansado
            show septemd1cansadoh
            septem "El mío recuperará su individualidad..."
            septem "El tuyo, lamentablemente tendrá que morir. No puedo arriesgar que algo de la procedencia de Nulla camine por el Jardín."
            hide septemd1cansadoh
            show septemd1cansado
            "{sc=3}¿Qué?{/sc}"
            nj "¿Supones que soy de Nulla? estás equivocado, ¡yo solo le sirvo a [nombrejugador]!"
            hide septemd1cansado
            show septemd1cansadoh2
            septem "No supongo. Lo sé."
            septem "Mi ojo lo ha sentido cuando lo vinculé contigo."
            septem "Él tiene acceso a ti, y una vez que poses tus ojos en él."
            septem "Será el principio del fin."
            septem "Debes dejar a [nombrejugador]."
            hide septemd1cansadoh2
            show septemd1cansadoc
            "{sc=3}No... [nombrejugador], no me hagas esto{/sc}"
            "Septem te mira en silencio."
            menu:
                "¡Tienes que hacer algo para dejarlo vivir!":
                    "..."
                    hide septemd1cansadoc
                    show septemd1cansadoh3
                    septem "¿Te importa la marioneta?..."
                    menu: 
                        "Por favor, yo te estoy ayudando. No dejes que muera.":
                            hide septemd1cansadoh3
                            show septemd1cansadoc
                            septem "..."
                            septem "......"
                            hide septemd1cansadoc
                            show septemd1cansadoh3
                            septem "Tal vez... podamos pensar en algo."
                            pass

                "...":
                    hide septemd1cansadoc
                    show septemd1cansadoh3
                    septem "No puedo arriesgar al Jardín."
                    septem "Admiro lo leal que es tu marioneta a ti, pero..."
                    septem "No sé si Nulla pueda tomar control de ella."
                    septem "Prefiero evitar futuros problemas..."
                    pass
                

    "Septem comienza a toser nuevamente."
    septem "Debemos apurarnos, sino él morirá."
    "¿Se refiera a su marioneta?"
    scene finact2_4 with dissolve
    septem "Dame la mano."
    "Tomas su mano con fuerza y Septem comienza a recitar cánticos con palabras que no puedes comprender."
    septem "{b}Pater, hoc sacro corpore ultimam voluntatem meam implebo ad novam aetatem sine tua praesentia nec damnatione.{/b}"
    septem "{b}Utrasque animas accipiam et in unam coalescam, divinum esse in corpore et anima creando.{/b}"
    septem "{b}Et dimítte nobis offénsa nostra...{/b}"
    show finact2_5
    pause 0.2
    hide finact2_5
    show finact2_6
    pause 0.2
    hide finact2_6
    show finact2_7
    pause 0.2
    "Algo en la sala cambia. El lugar poco a poco va desapareciendo, dejar a su paso un blanco absoluto."
    "Donde solo estás tú, Septem y la vela."
    "Poco a poco ese blanco comienza a mutar."
    "Dando vida a pequeños destellos de luz y polvo."
    "La vela va aumentando su forma con cada minuto que pasa, se extiende de manera anormal."
    scene finact2_8 with dissolve
    "Buscando una forma... buscando una figura."
    "Buscando la forma perfecta de un cuerpo humano."
    septem "{b}Transfíge óculos huius entitátis maióris in novum corpus.{/b}"
    scene finact2_9 with dissolve
    "Sientes un dolor intenso en los ojos. Como si los presionaran contra tu craneo."
    "Como si los quemaran."
    "Como si los arrancaran a la fuerza."
    septem "{b}Transfíge essentiam meam in hic novum corpus.{/b}"
    septem "{b}Sine ut unus simus.{/b}"
    scene negro with dissolve
    "Dejas de ver." 
    "Dejas de escuchar."
   
    "Todo se vuelve negro."
    "---------"
    "................."
    "......................."
    scene blanco with pixellate
    "Un blanco intenso se proyecta en tu mente, y no te deja en paz."
    "Es molesto y la única solución que tienes es abrir los ojos."
    "Pero te cuesta mucho hacerlo, como si algo no te lo permitiera aún."
    "Intentas e intentas, pero no hay caso. Tus ojos no responden a tus comandos."
    "Hasta que algo, una chispa, recorre todo tu cuerpo. Desde los pies hasta tu cabeza...."
    septem "[nombrejugador], esto nos va a doler un poco."
    "Escuchas la voz de Septem... pero no a través de tus oídos. No... su voz se origina dentro de tu cabeza, como ti estuviera hablando directamente en tus pensamientos."
    "No tienes tiempo para seguir pensando en la voz, ya que tu piel comienza a arder. Sientes como se rompe de apoco, lenta y tortuosamente."
    "Luego, todo tu cuerpo comienza a cambiar, sientes como dentro de ti explotan y se crean huesos y órganos, reemplazando los que tienen algún desperfecto."
    "Quieres gritar, pero te aguantas."
    "Cuando crees que lo peor ya ha pasado, sientes como tu corazón se desgarra, una y otra vez. Pues con cada intento, nunca estás contento como resulta."
    "No... tiene que ser perfecto."
    "Intentas una vez más y..."
    "Ya está--"
    "Abres los ojos, y tu visión es..."
    "... no ves nada más que el blanco de tu mente. Tienes miedo..."
    "{sc=2}Hmmm, es extraño ver con estos ojos...{/sc}"
    "Algo está muy mal."
    "{sc=2}Aún no estamos sincronizados completamente...{/sc}"
    "Miras tus manos y...."
    scene pureseptem with dissolve
    "Son las de Septem, pero ya no tienen ese negro característico."
    "Estás en el cuerpo de Septem."
    scene pureseptem2 with dissolve
    "{sc=2}¿Te gusta?{/sc}"
    "{sc=2}Aunque no será por mucho tiempo...{/sc}"
    "{sc=2}Ahora que tenemos el poder del creador, puedo crearte un cuerpo totalmente nuevo.{/sc}"
    "{sc=2}Separado del mío físicamente, pero conectado en alma.{/sc}"
    "{sc=2}Pero necesito tiempo...{/sc}"
    "{sc=2}Mientras... podríamos decir que ahora soy tu marioneta.{/sc}"
    "{sc=2}Me puedes usar de la misma manera que usabas a la tuya...{/sc}"
    "{sc=2}Que encantador~{/sc}"
    "--------"
    scene blanco with dissolve



    






    "-----------------------"
    "{sc=2}Oh....{/sc}"
    "Tienes que poner toda tu voluntad en mantener la forma de tu cuerpo. Incluso si te distraes por solo un segundo, tus brazos y piernas comienzan a estremecerse."
    "Temes que se rompan. Por lo que necesitas pensar en que parte o estímulo bloquear para así poder mantener las extremidades que están comprometidas con la falta de energía."
    scene negro with dissolve
    "{sc=2}[nombrejugador]...{/sc}"
    "{sc=2} Me siento débil... Creo que será necesario descansar los ojos por un momento...\n¿No te parece?{/sc}"
    menu: 

        "Sí.":
            $ septemconfianza += 1
            "..."
        "No.":
            "{sc=2}¿ N O ?{/sc}"
            "{sc=2}Creo que te---{/sc}"
            "{sc=2}¡Uhg!{/sc}"
            $ septemconfianza -= 1
            "..."
    "Tu cuerpo no aguanta mucho más, sientes como su masa se desestabiliza, haciéndote imposible mantenerte consciente y presente en el plano físico del Jardín."
    "Quién diría que tener un cuerpo propio sería tan difícil de mantener..."
    "La energía que estás ocupando ahora mismo está en su límite, haciendo imposible siquiera mover tu cuerpo sin tambalear."
    "{sc=2}Lo siento [nombrejugador], creo que no aguanto más.{/sc}"
    "{sc=2}No estamos lo suficientemente sincronizados como para compartir una perspectiva.{/sc}"
    stop music fadeout 1.5
    "Es lo último que dices antes de caer sobre el altar."
    scene negro with dissolve
    "..."
    "{sc=2}{size=*2.0}               .                .                .                   {/size}{/sc}"  
    play music "audio/europalce.WAV" fadein 2.0 volume 0.2
    "En un inicio no existía nada."
    "Solo oscuridad y destrucción..."
    scene creador with dissolve
    "Hasta que llegó el demiurgo, tu Padre."
    "Pero--- tienes la pequeña sospecha, dentro de tu apretado corazón, que él no te considera como un alguien, menos un hijo..."
    "No eres nada."
    "Nada comparado con su objetivo de seguir creando."
    scene recuerdo1 with dissolve
    "Una y otra vez rememoras las ínfimas conversaciones que tuviste el honor de tener con él."
    "Unas cuantas te llenaban el alma con esperanza, con un calor reconfortante que te envolvía todo tu ser. Todo tu amorfo ser."
    scene recuerdo2 with dissolve
    "Y... otras veces te dejaban con más preocupaciones de las necesarias."
    "Nunca tuviste estabilidad genuina en tus primeros días de consciencia."
    "Pero aun así..."
    "Aun así añoras esos momentos de silencio entre conversaciones."
    scene creador6 with dissolve
    "Esa mirada de orgullo que te dedicaba cuando hacías algo bien."
    scene recuerdo3 with dissolve
    "Mirada que al instante se transformaba en palabras de: 'Puedes hacerlo mejor', 'Te ha faltado agregar esto', 'Si sigues así no serás capaz de mantener el Jardín'..."
    "...No."
    scene blanco with dissolve
    "No tiene caso volver aquí."
    "No tienes ganas de seguir ahondando en esto, debes salir de aquí."
    scene recuerdo4 with dissolve
    "Al levantar la cabeza te das cuenta de que hay un camino que te invita a seguirlo."
    "Así que lo tomas."
    scene recuerdo5 with pixellate
    "Nada más pisar el camino, el lugar se distorsiona y muta."
    "Es un sendero hecho de una mezcla de arena y agua."
    "No hay nada más, por lo que lo único que queda es caminar."
    scene blanco with dissolve
    "Cuando miras detrás de ti, el camino va desapareciendo, sin dejar rastro de tus pisadas."
    scene recuerdo5 with dissolve
    "No hay ruido ambiental, ni se escucha el sonido de tus pies al hacer contacto con el agua, no hay nada que acompañe en tu caminata y eso te carcome el alma."
    "Con cada paso, la culpa te agarra y se pega a tu espalda para luego soltarte, sin antes robarte un poco de tu esperanza. Repitiendo el proceso hasta que quedas con una misera gota de ella."
    show vacio with dissolve
    "Nulla te lo ha dicho, un montón de veces... esto se va a poner feo cuando 'ellos' vengan, en algún momento llegarán. Y, aun así, le ordenas continuar: que busque humanos, que sacie la sed de Fe de los Estandartes a como dé lugar, que no les deje vivir en agonía."
    "Con cada respiración de tu mortal cuerpo, el pensamiento de que cada ser en tu mundo perderá la cordura luego de que se queden sin humanos en algún momento te quita el aire..."
    show vacio2 with dissolve
    "Nulla ya te lo ha dicho, un montón de veces, no pueden seguir con este método por la eternidad, tarde o temprano alguien vendrá a poner un fin a esto."
    "Ya sea el dueño de Padre o un externo al Jardín, o él mismo si llegan ellos."
    show vacio3 with dissolve
    "Nulla siempre ha sido directo, y tomará esa oportunidad si puede."
    "Nulla dice que es lo mejor. Que la única solución es eliminar el mundo, rezar a que venga ese ser, y hacer que todo esto acabe."
    hide vacio3 with dissolve
    hide vacio2 with dissolve
    hide vacio with dissolve
    "Pero... no."
    "Tu razón de ser no te permite hacer eso."
    "{b}Tú no quieres hacer eso.{b}"
    "Dejar que el jardín se destruido, no solo implica borrar a todo lo que proteges, sino que también, todo rastro de Padre y... tuyo."
    "Aún tienes tiempo para idear algo. De gestionar un plan que sea la solución a todo."
    "Por lo que te centras en tu misión para no sucumbir a lo que Nulla llama la solución a todos tus males. Tal vez si alteran el mundo, llames la atención de Padre y puedas tener una conversación con él para llegar a un acuerdo."
    "Para rogarle. Para llorarle como nunca le has llorado."
    "Para gritarle lo que nunca tuviste el valor de gritarle."
    "Para decirle que: {b}Tú quieres vivir.{b}"
    "Que este sentimiento no es solo por la razón de tu creación. No es algo que tenga que ver con tu rango u objetivo de vida."
    "No."
    "Tú realmente quieres ver crecer el jardín con él a su lado."
    "Quieres percibir cada una de las cosas que existen aquí y que no has podido por la condición de tu rango y cuerpo."
    "Quieres comenzar a vivir. Disfrutar de la vida por una buena vez por todas."
    "No este constante despertar encadenado a un montón de preocupaciones que no puedes solucionar, ni, aunque pongas todo tu ser en ello."
    "Pero la solución se te escapa de las manos."
    "Ya estás harto de intentar desenredar este hilo que siempre estará atado por nudos infinitos."
    "Quieres descansar y volver a los tiempos donde tú compartías el mando junto con Padre..."
    "---"
    "Caminas ahora con dificultad, la arena te traga mientras más avanzas y el agua te impide volver a retomar el paso con normalidad."
    "Pero no te dejas hundir. No te vas a rendir, tienes que llegar al final de este sendero." 
    "A lo lejos puedes ver el final."
    "Ahí, una luz te espera, seguramente es la solución a lo que todo el Jardín busca."
    "Pero aún no puedes llegar."
    "Hasta ese entonces-- harás todo lo necesario para llegar a ese lugar, sin importar qué."
    "Si la oportunidad se te da, la tomarás. No importa lo que debas hacer, cortarte los pies, quitar el agua o la arena que te dificulta llegar a tu destino, o simplemente hacer que el lugar llegue a ti."
    "Lo vas a conseguir."
    "A como dé lugar. No importa si los demás piensan que cortarte los pies es desagradable. Si quitar el agua o la arena es inmoral, o simplemente hacer que el lugar llegue a ti es algo imposible. Tú lo vas a hacer."
    stop music fadeout 2.0
    "...Con o sin Padre."
    "-----"
    menu:
        "Despertarlo.":
            pass
    
    scene temploseptem with dissolve
    play music "audio/hope.WAV" fadein 2.0 volume 0.4
    "{sc=2}...Ah.{/sc}"
    "{sc=2}¿[nombrejugador]{/sc}?"
    "{sc=2}¿Qué pasó?.{/sc}"
    "{sc=2}Momento.{/sc}"
    "{sc=2}No te siento del todo.{/sc}"
    "{sc=2}Pero se que estás aquí.{/sc}"
    "{sc=2}Maldición."
    "{sc=2}Te tengo dentro mí, y tienes acceso a todo de mí.{/sc}"
    "{sc=2}Mi alma se encuentra desnuda para que tus ojos puedan devorarla.{/sc}"
    "{sc=2}Y creo que esto no es lo que buscábamos.{/sc}"
    "{sc=2}Entonces... ¿Por qué antes teníamos una conexión más estable?{/sc}"
    "{sc=2}Mmmm.{/sc}"
    "{sc=2}No estaba consciente...{/sc}"
    "{sc=2}Ya veo.{/sc}"
    "{sc=2}Dentro de mi mundo interior podemos hacer esta simbiosis, parecida\na la que tenías con tu antigua marioneta.{/sc}"
    "{sc=2}Aquí, estando yo consciente, no podemos tener ese grado de sincronía.{/sc}"
    "{sc=2}Y es más difícil ahora que no tengo tanta energía.{/sc}"
    "{sc=2}No lo pensé claramente-- bueno, no tenía opción...{/sc}"
    "{sc=2}Ahora mismo no tengo la energía suficiente, ni el conocimiento como para\ncrearte un cuerpo físico completamente nuevo y...{/sc}"
    "{sc=2}Supongo que estar en mi cuerpo debe ser aburrido para ti.{/sc}"
    "{sc=2}Ya que, dejas de ser 'tú' y pasas a ser yo.{/sc}"
    "{sc=2}Pasas a experimentar en carne propia mi percepción de este mundo.{/sc}"
    "{sc=2}Mis deseos y pensamientos...{/sc}"
    

    septem "Demonios..."
    septem "Bien escucha, haremos algo."
    septem "Te prometí más libertad en este mundo, por lo que te la daré."
    septem "No tengo medios ni el conocimiento para crearte un cuerpo nuevo que sea capaz de albergarte dentro, pero si puedo modificar el mío."
    "{sc=2}Me levanto del altar, y observo el lugar.{/sc}"
    "{sc=2}Rafael está en el suelo, Respirando... eso es bueno. Él está bien.{/sc}"
    "{sc=2}De la marioneta no hay rastro, ¿Será que se ha desintegrado?{/sc}"
    "{sc=2}No logro percibir su presencia en mi dominio.{/sc}"
    menu:
        "¿Ha muerto?":
            septem "Eso creo."
        
        "¿Dónde está la marioneta?":
            septem "No lo sé..."
    
    septem "Luego me preocuparé por eso."
    septem "Ahora debo---"
    "{sc=2}Trasladar el cuerpo de Rafael a una habitación segura.{/sc}"
    "El cuerpo de Rafael desaparece del templo con el aplauso de tus manos. Él reposa inconciente en su cama y no hay nada que puedas hacer para despertarlo..."
    "No sin un corazón apto para él..."
    septem "Luego veremos que podemos hacer con Rafael..."
    septem "Primero--"
    septem "Te daré manos, para que puedas interactuar con el lugar."
    septem "Intentaré hacerlo ahora."
    septem "Dos te bastarán, supongo."
    scene negro with dissolve
    "{sc=2}Suspiro y comienzo a realizar cánticos que siempre he sabido,\npero que nunca he intentado hacerlo.{/sc}"
    "{sc=2}Por respeto a Padre... esta es una invocación personal de él.{/sc}"
    "{sc=2}Una invocación de emergencia... de protección. Que jamás creí\nverla en algún momento.{/sc}"
    "{sc=2}Hasta que Nulla le borró un brazo a Padre.{/sc}"
    "{sc=2}Aún recuerdo ver a Padre, 7 días después de que yo recibiera\nel cuerpo de Rafael.{/sc}"
    "{sc=2}Fue la primera vez y la última que lo vi de esa forma.{/sc}"
    "{sc=2}Luego de eso se esfumó.{/sc}"
    "{sc=2}Ni siquiera tuve la oportunidad de despedirlo... él solo me\ndio la vela y me dijo que castigaría a Sextam.{/sc}"
    "{sc=2}...No pensé que el castigo se extendería a todos por tanto tiempo.{/sc}"
    "{sc=2}Lo subestimé.{/sc}"
    menu:
        "Septem...":
            septem "Ah-"
        
        "Deja de pensar en Padre.":
            pass
        
        "Concéntrate, Septem.":
            pass
    scene temploseptem with dissolve
    septem "..."
    septem "Tienes razón."
    "{sc=2}Tengo que continuar.{/sc}"
    "{sc=2}En voz alta recito el trato para que obtengas más libertad.{/sc}"
    "{sc=2}Y no estés obligado a leerme de esta manera.{/sc}"
    "{sc=2}Supongo que es mejor de esta forma.{/sc}"
    septem "[nombrejugador]."
    septem "Para satisfacer tu necesidad de involucrarte con este mundo."
    septem "Y como tengo el rol de ser tu anfitrión, intentaré cumplir con mi palabra."
    septem "Ahora vas a tener mi ojo principal y manos para hacer lo que se te plazca."
    septem "Poder interactuar un poco más con mi mundo. De manera limitada, pero a la vez, con más libertad de la que tenías antes."
    septem "No perderemos la conexión cuerpo y alma, pero, ahora tendrás una perspectiva nueva."
    septem "Me dejarás de lado parcialmente, ya que no serás 'yo',\nsino unas manos y ojos."
    septem "Y yo, seguiré siendo tu narrador y marioneta, aún."
    "{sc=2}Mis manos comienzan a realizar señales que parecen ilegales\nde invocar, como si manchara el nombre de Padre en el proceso.{/sc}"
    "{sc=2}Cánticos son llamados en latín y comienzo a ceder parte de este\ncuerpo divino, a ti.{/sc}"
    "{sc=2}Al tiempo de creo nuevas manos, para ti.{/sc}"
    "{sc=2}Parte de mi ser se despega, para dárselos a ti.\nY junto con ello te cedo control.{/sc}"
    "{sc=2}El control es lo primordial.{/sc}"
    "{sc=2}..........{/sc}"
    scene blanco with dissolve
    "-------------------"
    stop music fadeout 2.0
    "__________{b}Septem te sede parte de su identidad.{/b}_________"
    "El ojo y las manos ya son tuyos."
    "Ahora son de tu propiedad."
    play music "audio/sorry_cant_tell.mp3" fadein 2.0 volume 0.2

    scene temploseptem with dissolve
    show pureseptem3serio with dissolve
    septem "Ahora tienes un pedacito de mí que puedes controlar."
    septem "Espero que esto sea de tu agrado, [nombrejugador]."
    septem "Seguirás siendo capaz de sentirme, pero tu punto de vista no será el mío."
    septem "Supongo que es..."
    hide pureseptem3serio
    show pureseptem2feliz
    septem "Como una nueva marioneta, solo que más básica."
    septem "Espero poder hacerte una completa más adelante."
    septem "Ahora puedes probar tus nuevas manos."
    hide pureseptem2feliz with dissolve
    menu:
        "Okay.":
            jump interactuar1
            pass

label continuacion1:
    scene temploseptem with dissolve
    "Tus manos dejan de operar y en cuestión de segundos, Septem tiene el control de ellas."
    "Las mueve de un lado a otro, mueve los dedos: abriendo y cerrando los puños, probando sus funciones."
    show pureseptem2risa with dissolve
    septem "Están en buen estado."
    septem "Es un muy buen primer intento."
    hide pureseptem2risa
    show pureseptem3callado
    "{sc=2}Seguramente Padre estaría orgulloso.{/sc}"
    "..."
    hide pureseptem3callado
    show pureseptem2normal
    septem "Como sea, esto es un regalo."
    hide pureseptem2normal
    show pureseptem3risa
    septem "Espero que lo sepas apreciar, [nombrejugador]."
    hide pureseptem3risa
    show pureseptem2sonrisa
    "Se crea un silencio luego de sus palabras. Y Septem siente que se le está olvidando algo."
    hide pureseptem2sonrisa with dissolve
    "No le cuesta mucho recordar de que es, por lo que te pide que lo acompañes."
    "Es la hora de almorzar."
    scene cocinaseptem with dissolve
    "Inconscientemente se encamina a la cocina."
    "Mientras camina, levanta sus manos para conjurar los ingredientes. Pero su poca energía lo detiene y lo hace recapacitar."
    show pureseptem3serio with dissolve
    stop music fadeout 2.0
    "'¿Qué estoy haciendo?' se pregunta." 
    "Luego para en seco, mira sus pies, el mesón y luego a ti."
    "Hay un silencio tanto fuera como dentro de él. Un cortocircuito ocurriendo dentro que lo trae y le hace caer en cuenta de la estupidez que está haciendo."
    "Y luego una explosión invisible, que solo tú y él pueden sentir."
    "Saboreas la vergüenza que burbujea en su estómago por un momento."
    "Pero su cara no lo demuestra."
    "Y tú solamente la puedes saborear gracias a la conexión que tienen."
    "Ahora Septem no te puede ocultar sus emociones."
    "Y eso hace que sienta aun más vergüenza."
    hide pureseptem3serio
    show pureseptem2normal
    "Y enojo..."
    "Pero no te va a dar el gusto de verlo reflejado en su cara."
    "Eso sería como perder dos veces."
    hide pureseptem2normal
    show pureseptem3callado
    "Con un suspiro pesado Septem se endereza y te corre la mirada."
    hide pureseptem3callado
    show pureseptem3callado2
    "Sientes como Septem no sabe que hacer. Ya no tiene un propósito claro para el día de hoy."
    "Ya no necesita descansar del cuerpo, ni hacer sus comidas estrictas y no tan elaboradas."
    "Su rutina ya no tiene razón de ser ni existir."
    "Su cuerpo, a pesar de ser muy parecido al antiguo en cuanto a órganos y piel, es autosuficiente."
    "El corazón late gracias a la energía divina, y mantiene el resto del cuerpo como si de un motor único se tratase."
    "Pero ya no hay necesidad de mantenerlo con ritos y rutinas que toman tiempo del día, y forman parte de la experiencia de tener un cuerpo mortal."
    "Ya no hay nada que hacer para pasar las horas que realmente tenga un propósito o misión por cumplir."
    "Septem jamás ha tenido tiempo muerto, y sientes como la ansiedad comienza a trepar por sus pies."
    "Gritando y demandando hacer algo."
    "Septem no sabe que hacer..."
    hide pureseptem3callado2
    show pureseptem1hablando
    play music "audio/hope.WAV" fadein 2.0 volume 0.4

    septem "Creo que tomar aire me ayudaría..."


    menu:
        
        "Salir a tomar aire":
            "..."
            jump interactuar2

label continuacion2:

    scene habitacionrafael with dissolve
    "Pasan tres días, en los que Septem se dedica a observar el cuerpo de Rafael y acostumbrarse a tu presencia. A tu eterna compañía."
    "La cual no lo abandona ni por un momento."
    "Casi que ahogándolo con tu presencia."
    "Pero, ya no le parece tan incómodo como antes."
    "Septem ya ha aceptado tu compañía."
    "La pieza en que se encuentra Rafael es exactamente igual a todas las habitaciones que existen en el templo de Septem."
    "Con lo justo y necesario."
    scene septem_rafael1 with dissolve
    "..."
    "Septem observa con las cejas fruncidas a Rafael, quien yace dormido."
    "Al mirarlo, no puedes detectar los latidos de su corazón."
    "Pero él respira sin problemas."
    menu:
        "¿Cómo sigue vivo?":
            pass
    septem "Yo estoy manteniendo su cuerpo con mi energía."
    "Te confiesa sin titubear."
    "Así que es por esto que Septem no tiene la energía suficiente para invocar o hacerte un cuerpo."
    menu:
        "¿Él es importante para ti?":
            scene septem_rafael2 with dissolve
            septem "..."
            septem "Sí."
            septem "Conozco todo de él, es imposible no tenerle aprecio."
        
        "Pensé que él solo era una marioneta.":
            scene septem_rafael2 with dissolve
            septem "Es mi compañero."
            septem "Me ayudó a entender muchas cosas."
            septem "Y yo lo traté muy mal por un tiempo..."
            septem "Se lo debo."
        
        "¿Su corazón no sirve?":
            scene septem_rafael2 with dissolve
            septem "Llegó a mí con ese problema."
            septem "No tengo idea como crearle un corazón independiente de mi ser."
            septem "A pesar de que le hice uno cuando salí de su cuerpo, este no funciona."
            "Septem suspira."
    if  persistent.nombrerafael == True:
        menu:
            "Pensé que se odiaban...":
                scene septem_rafael2 with dissolve
                septem "¿Qué?"
                septem "¿Qué te hace pensar eso?"
                menu:
                    "Rafael habló conmigo.":
                        #Septem te mira con sorpresa.
                        "Sus ojos se clavan en ti, acompañados por un ceño fruncido que marca su piel con arrugas notorias."
                        scene septem_rafael3
                        septem "¿¡Te has metido sin permiso a su habitación?!"
                        "La voz de Septem se eleva con cada palabra, afilada y visceral. Aprieta los puños y tensa sus hombros, no sabiendo cómo canalizar la rabia que crece mientras más piensa en tus transgresiones."
                        "Pero al enfocar sus ojos y analizar lo que ven, se da cuenta de que ya no está la marioneta."
                        "Ahora solo estás tú, sin intermediario. Tú, el que puede ayudarlo a salvar el jardín."
                        "Tú, nuevo amo y señor del jardín, si todo sale bien."
                        scene septem_rafael1
                        "Septem se controla, cierra los ojos y comienza a contar mentalmente hasta 10."
                        "A su mente llega la imagen de Rafael y lo que has dicho."
                        "Y con pena acepta que debes tener razón."
                        "Su cuerpo deja de estar tenso: sus hombros caen y sus puños ceden, abriéndose en el proceso para poder tocarse el cabello y peinarlo hacia atrás."
                        septem "Dejé de escribirle y perdimos comunicación."
                        septem "Supongo que él me debe odiar ahora."
                    "No lo sé.":
                        septem "Hmmm."
            "...":
                pass
    else:
        "..."
    
    menu:
        "...¿Es tu hijo?":
            scene septem_rafael3
            "Septem te mira con asco por un segundo."
            septem "¿De donde has sacado eso?"
            septem "¿Has leído mal los documentos?..."
            "Aprieta los puños, enojado. Como si el solo pensamiento fuera suficiente para sacarlo de sus casillas. Ya sea por el contenido de aquellos documentos en sí o por el hecho de como tú los has supuestamente encontrado."
            "De cualquier manera, Septem recapacita y suspira."
            septem "Imposible... tú no puedes leer latín."
            scene septem_rafael1
            "Sus ojos vuelve a recaer en el cuerpo de Rafael."
            septem "Claro que no es mi hijo."
            "Refunfuña."
            septem "Yo solo cuido su cuerpo y lo mantengo vivo."
        "...":
            pass

    scene septem_rafael1
    "Hay un silencio, pero es ese tipo de silencio abrumador y pesado."
    "Pero si nostálgico."
    scene habitacionrafael with dissolve
    "Septem se encamina para salir de la habitación."
    show pureseptem2sonrisa with dissolve
    septem "Rafael es un buen escritor."
    septem "Nos comunicábamos por un Diario."
    septem "Me gustaba leer lo que escribía para mi cada vez que retomaba su cuerpo."
    septem "Después de cada comida..."
    hide pureseptem2sonrisa
    show pureseptem2blush
    septem "Extraño un poco hacer ello."
    "Hay una pausa en sus movimientos, parpadea con incredulidad al darse cuenta de que te está soltando información que no has pedido."
    "Y de lo extraño que es hablar de manera tan libre contigo."
    "Aquello le perturba un poco."
    menu:
        "Septem...":
            pass

            hide pureseptem2blush
    show pureseptem2enojo 
    "Septem levanta la mano, claro signo de que no quiere oír tu respuesta."
    "Pero, muy dentro de él, percibes que Septem está cerrando una puerta para evitar soltar toda la explosión de emociones y preocupaciones."
    "Intentando proteger su ego."
    hide pureseptem2enojo
    show pureseptem1hablando
    septem "Te pido una disculpa."
    septem "No quiero hacerte cargar con mis penurias."
    septem "Tampoco es necesario que me consueles."
    septem "No lo necesito."
    "Dice de manera solemne."
    menu:
        "Insistir.":
            $ septemconfianza -= 1
            hide pureseptem1hablando
            show pureseptem2enojo
            septem "Te he dicho que no lo necesito."
            "Su voz se transforma, volviéndose brusca y ronca."
            "Se está enojando pero se contiene..."
            menu:
                "Insitir...":
                    jump septem_badend_insistir
                    
                   
                "Dejar de insistir.":
                    pass
        
        "Dejarlo estar.":
            pass


    
    menu:
        "¿Qué quieres hacer ahora?":
            hide pureseptem1hablando
            hide pureseptem2enojo
            pass
        "¿Qué hacemos con Rafael?":
            hide pureseptem1hablando
            hide pureseptem2enojo
            show pureseptem3serio
            septem "No hay nada que tú o yo podamos hacer ahora."
            septem "Solo esperar..."


    hide pureseptem3serio
    show pureseptem3callado
    "Hay un segundo de quietud, Septem está pensando que en podrían hacer hoy."
    hide pureseptem3callado
    show pureseptem1callado
    septem "Creo que podríamos cocinar..."
    septem "Para matar el tiempo..."
    septem "Rafael no despertará por más que lo observemos."
    septem "El problema está en su corazón."
    scene cocinaseptem with dissolve
    "La cocina es tan pulcra que parece irreal. No hay rastros de nada fuera de su lugar, parece una foto."
    "El espacio es suficiente para una persona, y no está pensada como un lugar para tener a alguien más."
    "Septem te dice que realizarán tartaletas, que esa receta fue escrita en el diario que comparte con Rafael, pero que jamás quiso hacerlas."
    "Por falta de tiempo, dijo."
    "Comienzan buscando los ingredientes. Tus manos buscan en las encimeras y en los cajones lo que Septem te pide. Hacer esto es raro, ya que pueden saltarse esto e invocar los ingredientes con un solo aplauso."
    "Tal vez sea la falta de energía, o tal vez sea que Septem quiere experimentar con lo cotidiano y humano de buscar las cosas por uno mismo."
    "Aunque también existe la posibilidad de que guste de verte complicado al intentar buscar cada cosa."
    "Quién sabe..."
    scene cocina_septem with dissolve
    "Cuando ya tienen todo, comienzan a preparar las tartaletas."
    "Mezclan, baten y separan los ingredientes."
    "Todo es muy ameno. El momento es grato."
    "Ver la cara de concentración de Septem no tiene precio. Hasta podrías imaginarte un día libre con él como tu compañero, preparando delicias para alguna visita o simplemente para ustedes."
    "Ja."
    "Llega el momento de decorar y Septem decora una de ellas con dos frutas."
    menu:
        "¿Solo dos?":
            pass
    septem "Sí."
    septem "Quiero que el resto lo decores tú."
    septem "He hecho todo el trabajo, estoy cansado..."
    "Dice el frunciendo el ceño. Pero estás seguro que no lo dice en serio. Septem ya no se cansa."
    "Y en más de una oportunidad lo has atrapado mirándote cuando mueves tus manos... con fascinación."
    septem "Adelante, [nombrejugador]~"

    scene tartaleta_septem with dissolve

    call screen pastel_minijuego

    scene cocina_septem1 with dissolve
    "Luego de terminar, Septem aprecia tu trabajo, dedicándole una larga inspección con sus ojos. No puede evitar sonreír un poco."
    "Sin decir nada, toma una tartaleta para poder probarla."
    "Se ve tan mundano que da miedo."
    scene cocina_septem2
    septem "Lo has hecho bien..."
    septem "Pero es extraño verte tomar las cosas..."
    menu:
        "¿Extraño o te gusta?":
            septem "..."
            septem "Ambas."
            "Sus orejas se tiñen de un leve rosado."
        
        "¿Extraño?":
            septem "Sí... un poco."

    scene jardinseptem with dissolve
    "                           . . .                              "
    "Las actividades del día de Septem se resumen en pasar el tiempo contigo, por obligación."
    "Pero él ya se ha acostumbrado, hasta, puedes sentir que no le disgusta, pero le cuesta encontrarle una lógica a ello. Y con ello viene un proceso de aceptación que no le resulta tan fácil."
    "En todo momento estás ahí, acompañándolo."
    "Incluso los tiempos de silencio son disfrutados gracias a tu compañía."
    "Ahora mismo, están en el jardín y Septem mira el lago por un largo rato."
    "De repente algo empieza a descender desde arriba..."
    $ araña_activa = True   
    show araña_hilo at bajada
    pause 3.0 
    show screen screen_araña with dissolve
    

    "¡¡Es una araña!!"


label mini_continuacion:

    "..."
    hide araña_hilo 
    ".................Uh."
    $ araña_activa = False
    hide screen screen_araña with dissolve
    "..........................¿?"
    show pureseptem3callado with dissolve
    "Miras a Septem y lo sientes al intante."
    "Hay algo que le molesta, algo que le ha estado molestando desde que te dio las manos y el ojo."
    "Y esa molestia no ha parado de crecer."
    "Pero esa molestia no es tu presencia ni compañía constante."
    "Es algo más."
    menu:
        "¿Pasa algo?":
            $ septemconfianza += 1
            hide pureseptem3callado
            show pureseptem1hablando
            septem "Sí..."
        "No comentar nada.":
            "Septem suspira y te busca con la mirada."
    hide pureseptem3callado
    hide pureseptem1hablando
    show pureseptem2normal
    septem "Creo que me equivoqué."
    septem "Ahora que te tengo conmigo, entiendo un poco a tu marioneta..."
    hide pureseptem2normal
    show pureseptem2blush
    septem "Pero al mismo tiempo me gustaría que estuvieras fuera de mí, para que tengas tu propio rol."
    septem "Un poco más de libertad...  inmersión."
    hide pureseptem2blush
    show pureseptem2incomodo
    septem "Conmigo estás sujeto a mí en todo momento, no tienes un cuerpo propio que te represente."
    septem "Al menos con tu marioneta era más fácil hacer esta inmersión... ya que ese era su propósito. Sin contexto, sin historia detrás de ella."
    septem "Algo vacío, listo para ser tomado por ti."
    hide pureseptem2incomodo
    show pureseptem2enojo
    septem "Pero que al mismo tiempo tenía claras fijaciones y deseos."
    septem "Con ideas claras y sentimientos ajenos a los tuyos."
    septem "Nada objetiva."
    hide pureseptem2enojo
    show pureseptem2normal
    "Septem divaga en si soltar y comunicarte lo que realmente le molesta o no."
    hide pureseptem2normal
    show pureseptem2enojo
    septem "Y algo de Nulla..."
    hide pureseptem2enojo
    show pureseptem2blush
    "Avergonzado por su incapacidad de poder elegir bien sus palabras, intenta filtrar su preocupación."
    septem "Incluso con un nombre que le has puesto tú, que puede ser el tuyo o uno inventado."
    "..."
    septem "¿Es '[nombrejugador]' un nombre que usas para llamarte a ti mismo? ¿o es el nombre que le has dado a la marioneta y no tiene nada que ver contigo?"
    "¿Acaso quiere conocer tu nombre real?"
    "Oh..."
    menu:
        "Es un nombre que me representa.":
            $ septemconfianza += 1
            hide pureseptem2blush
            show pureseptem2sonrisa
            septem "Bien."
            septem "Me gustaría llamarte como se debe."
            septem "Los nombres aquí son importantes..."
            septem "Y el tuyo no es la excepción"

        "Era el nombre de la marioneta...":
            hide pureseptem2blush
            show pureseptem3callado
            septem "Ah."
            hide pureseptem3callado
            show pureseptem3risa
            septem "Te pido formalmente disculpas, por no dirigirme a ti como corresponde."
            septem "Si no es mucho pedir... ¿puedo saber tu nombre?"
            menu:
                "No, [nombrejugador] está bien.":
                    $ septemconfianza -= 1
                    hide pureseptem3risa
                    show pureseptem2blush
                    septem "Está bien."

                "Sí, Mi nombre es:":
                    hide pureseptem3risa
                    show pureseptem2sonrisa
                    $ nuevo_nombre = renpy.input("___")
                    $ septemconfianza += 1
                    septem "Un gusto poder conocerte."

    if nuevo_nombre != "":
        $ nombrejugador = nuevo_nombre
        hide pureseptem2sonrisa
        show pureseptem2risa
        septem "[nombrejugador]..."
        "Prueba el nombre en sus labios, y sonríe victorioso."
    else:
        septem "Okay. Seguiré llamándote [nombrejugador]."
    hide pureseptem2sonrisa
    hide pureseptem2risa
    hide pureseptem2blush
    show pureseptem1sonrisa
    septem "[nombrejugador], creo que deberíamos tomar esto como un nuevo inicio."
    septem "Te quiero como compañero, creo que ya ha pasado el tiempo suficiente para decidir si eres apto o no para el cargo."
    "..."
    hide pureseptem1sonrisa
    show pureseptem2blush
    septem "Te has quedado hasta aquí, después de todo."
    septem "Estuve pensando y, creo que cuando estabas conectado a la marioneta, te he dado la peor impresión posible."  
    septem "Pido disculpas si te he ofendido, pero..."  
    hide pureseptem2blush
    show pureseptem3serio
    septem "Para mí, la marioneta no fue nada mío. No es un súbdito ni una entidad del Jardín a quien yo deba proteger."
    septem "La marioneta era una conexión tuya y de Nulla."
    hide pureseptem3serio
    show pureseptem2enojo
    septem "Nunca fue de mi agrado, y verla ahí con esa cara y ese olor a humano..."
    septem "Se me hizo difícil ceder a la tentación."
    hide pureseptem2enojo
    show pureseptem2normal
    "Sientes como Septem se retuerce un poco al recordar el olor y color de la sangre."
    "Septem suspira, conteniéndose para no hablar de más, antes de esbozar una sonrisa ladeada."
    hide pureseptem2normal
    show pureseptem2feliz
    septem "Pero ahora esa cosa ya no está."
    septem "Ahora solo somos tú y yo."
    hide pureseptem2feliz
    show pureseptem3risa
    septem "Y haré todo lo posible para darte un cuerpo completo."
    septem "No solo manos y un ojo."
    hide pureseptem3risa
    show pureseptem2blush
    "Septem mira tus manos por un segundo, y aprieta la mandíbula."
    "                                    . . .                                         "
    hide pureseptem2blush
    show pureseptem3serio
    septem "Quiero mostrarte algo..."
    septem "Pero necesito que te lo tomes seriamente."
    septem "El lugar no es un juego."
            
    menu:
        "Bueno.":
            $ septemconfianza += 1
            jump interactuar3

        "No gracias.":
            $ septemconfianza -= 1
            pass
                    
label continuacion3:
    scene temploseptem with dissolve
    "..."
    "Los días pasan y Septem va recuperando la energía que gastó en crear su cuerpo divino, dejándole más carga energética para mantener el cuerpo de Rafael y poder hacer otras cosas."
    scene bibliotecaseptem with dissolve
    "Con esto, Septem comienza a estudiar y recrear invocaciones, practicando diversas partes del cuerpo humano."
    "La mayoría son corazones..."
    "También, tiene reuniones con Sextam, pero él nunca abandona su dominio."
    "En estas reuniones aprendes algunos datos que desconocías."
    "Por ejemplo: Al Jardín no le sirve cualquier humano. Tienen que ser creados por Sextam, de no ser así, no sobreviven por mucho tiempo en el Jardín."
    "Mueren al pasar 7 días..."
    show pureseptem1hablando at right with dissolve
    septem "Cuando pueda quitarte el sello, podrás volver a tu dominio y crear a nuestros humanos."
    show sextam1hablando at left with dissolve
    "¿Crees que sea tan fácil?"
    hide pureseptem1hablando
    show pureseptem3serio at right
    septem "Puedo ver el sello que tienes en el interior."
    septem "Una vez sepa como romperlo, será fácil para ti volver a crearlos."
    hide pureseptem3serio
    show pureseptem1hablando at right
    septem "Tendrás que empezar de a poco, con nodrizas..."
    septem "Pero luego volverán a tener su ciclo de vida normal."
    septem "Obtendrás nacimientos naturales luego de 5 a 10 años."
    septem "Será como antes."
    hide sextam1hablando
    show sextam1enojo2 at left with dissolve
    sextam "..."
    hide sextam1enojo2
    show sextam1enojo at left
    sextam "¿Crees que Padre vuelva si se entera?"
    hide pureseptem1hablando
    show pureseptem3callado2 at right
    hide sextam1enojo
    show sextam1enojo2 at left
    septem "..."
    hide sextam1enojo2
    show sextam1enojo at left
    sextam "¿Qué tal si nos castiga nuevamente?"
    hide pureseptem3callado2
    show pureseptem3serio at right
    hide sextam1enojo
    show sextam1enojo2 at left
    septem "No pasará, Sextam."
    hide sextam1enojo2
    show sextam1enojo at left
    sextam "¿Qué tal si los demás se enteran que fue por nuestra culpa?"
    septem "No fue nuestra culpa, fue la de Nulla."
    sextam "Yo también tengo culpa. No solo Nulla."
    hide pureseptem3serio 
    show pureseptem1callado at right
    hide sextam1enojo
    show sextam1enojo2 at left
    septem "Sextam..."
    "Sextam no para, a pesar de que Septem le mira ya irritado."
    hide sextam1enojo2
    show sextam1enojo at left
    sextam "¿Vamos a tener que inventar otra excusa como el nacimiento falso de tu hijo? ¿Para cubrir el robo del cuerpo?"
    sextam "Porque hasta donde saben ellos, Padre se ha ido porque se aburrió y no por la culpa de haber traído un cuerpo de otro mundo para que lo uses de marioneta."
    hide sextam1enojo
    show sextam1enojo2 at left
    septem "Sextam..."
    hide sextam1enojo2
    show sextam1enojo at left
    sextam "No Septem, escúchame."
    sextam "Estamos exponiéndonos a destapar todo, Nulla podría abrir la boca y sellar tu destino, o Padre podría llegar a imponer más castigos."
    sextam "Prométeme que si hacemos esto, no habrá consecuencias peores."
    sextam "Si el consejo se llegase a enterar, date por seguro que irán por tu cabeza."
    sextam "Si Padre viene, créeme que no será para darte un abrazo."
    hide sextam1enojo
    show sextam1enojo2 at left
    "Sextam te mira por un momento antes de proseguir."
    hide sextam1enojo2
    show sextam1enojo at left
    sextam "Septem, te juro que si esto no funciona---"
    sextam "Creo que lo mejor sería hacerle caso a Nulla."
    "Septem masculla una corta risa, incrédulo por las palabras de su compañera."
    hide sextam1enojo
    show sextam1enojo2 at left
    hide pureseptem1callado
    show pureseptem3enojo at right
    septem "Estás loca."
    hide sextam1enojo2
    show sextam1enojo at left
    sextam "No Septem, si esto sale mal, lo mejor sería acabar con todo, en vez de ver como todo el Jardín se va en tu contra."
    hide sextam1enojo
    show sextam1triste at left
    hide pureseptem3enojo
    show pureseptem3callado at right
    sextam "Y como nadie puede lastimarte, encontrarán la manera de hacerte pagar."
    sextam "...Realmente odiaría que pasaras eso."
    hide sextam1triste and pureseptem3callado with dissolve
    scene bibliotecaseptem with dissolve
    "Sextam solloza."
    "La conversación poco a poco se va diluyendo hasta llegar a un punto que han conversado de todo lo necesario."
    "Toda formalidad ya pactada."
    "Pero Septem necesita hablar algo más."
    "Algo que ni siquiera a ti te ha dejado ver, mucho menos confesarte."
    "Ya qué probablemente no lo entenderías tanto como Sextam."
    show pureseptem3serio at right with dissolve
    septem "Una cosa más."
    "Sextam solo lo observa. Muy atenta, pero no dice nada."
    septem "Creo que necesitas saber esto."
    septem "El rango que tengo ahora me permite dañar..."
    show sextam1hablando at left with dissolve
    hide pureseptem3serio
    show pureseptem3callado at right
    "Ella abre la boca para decir algo, y él la espera... pero Sextam no puede encontrar su voz y opta por guardar silencio, evitando la dura mirada de Septem."
    hide pureseptem3callado
    show pureseptem1hablando at right
    septem "Es importante que lo sepas, y necesito que si llegase a pasar algo, me detengas."
    hide sextam1hablando
    show sextam1triste at left
    hide pureseptem1hablando
    show pureseptem1callado at right
    "Sextam aprieta los labios, tomando valor para contestar a su petición."
    sextam "Sabes que no puedo hacer nada---"
    sextam "Creo que sería mejor que le hicieras esa petición a la entidad que está contigo."
    "Se hace un silencio."
    "Pero Septem comprende."
    hide sextam1triste
    show sextam1enojo at left
    sextam "Debo irme."
    sextam "Estaré atenta a tus noticias."
    hide sextam1enojo with dissolve
    "Sin más Sextam desaparece por la puerta."
    "Y así, tú y Septem quedan solos."
    "Intentas hablar con Septem pero él te pide un momento a solas."
    "Así que te retiras de la biblioteca."
    hide pureseptem1callado with dissolve
    scene pasilloseptem with dissolve

    
    "                                     . . . . . . . . . . .                  "
   
    scene bibliotecaseptem with dissolve
    "Algunos días te aburres, ya que Septem no hace nada más que leer y buscar como romper sellos."
    "A veces te lee en voz alta, pero la mayoría del tiempo te pide silencio e insiste en que observes su progreso."
    scene sello_septem1 with dissolve
    "Ver como falla es algo de lo que no te cansas de ver."
    "Cada vez que falla en hacer un sello o romperlo, Septem aprieta mucho la mandíbula, al punto de hacer rechinar sus dientes."
    "...y de vez en cuando golpea la mesa, sin mirar en tu dirección."
    "Pero lo vuelve a intentar."
    "Incluso cuando tiene éxito, si nota alguna imperfección en el resultado, lo rompe y lo intenta con más esmero."
    "..."
    scene sello_septem2 with dissolve
    "Al paso de una hora, Septem celebra cuando ve que el sello que lleva intentando romper, desaparece como si de humo se tratara."
    septem "Lo hemos hecho, [nombrejugador]."
    menu:
        "¡Felicidades!":
            scene sello_septem3
            "Septem sonríe sin mostrar los dientes, sintiendo un pequeño cosquilleo en su estómago al obtener tu respuesta."
            "Para que al instante se sienta extrañado por su propia reacción."
            "No se había sentido de esta manera desde que..."
            "Padre de dio una retroalimentación después de crear a los Estandarte."
            "..."
            menu:
                "¡Lo has hecho muy bien!":
                    $ septemconfianza += 1
                    "Nuevamente esa sensación extraña en lo bajo de su estómago."
                    septem "Espero que no lo estés diciendo como una burla..."

                "...":
                    pass

            "Septem vuelve su mirada a la mesa."
            "Y luego de meditar por un momento, suspira."
        
        "¿Hemos?":
            septem "Claro."
            septem "Tú eres parte vital en este proceso."
            septem "Esto es un logro de ambos."
            "Septem asiente, y te mira con firmeza."
            septem "Lo hemos hecho juntos."
            menu:
                "Lo has hecho muy bien.":
                    $ septemconfianza += 1
                    "Septem desvía la mirada, no sabiendo que hacer con sus ojos."
                    "Mirarte ahora mismo, no es opción."
                    septem "Tú igual lo has hecho bien."
                    septem "Podrías estar haciendo cosas más productivas ahora mismo."
                    septem "...Sin embargo estás aquí, conmigo."
                    septem "Realmente lo aprecio."
                    
                "...":
                    pass
    scene bibliotecaseptem with dissolve
    show pureseptem2feliz with dissolve
    septem "Podemos comenzar con la restauración."
    "Te comenta sin creerlo. Sin aliento."
    septem "Bien."
    hide pureseptem2feliz
    show pureseptem1callado
    "Toma un poco de aire antes de revelarte lo que está pensando."
    hide pureseptem1callado
    show pureseptem3risa
    septem "[nombrejugador], tenemos reunión esta noche con el consejo y los Estandartes."
    menu:
        "¿El consejo?":
            hide pureseptem3risa
            show pureseptem2normal
            septem "Son los encargados de apoyar a sus respectivos Estandartes para la toma de decisiones."
            septem "Aunque solo invitaré a las cabecillas de cada dominio."

        "¿Para qué?":
            septem "Comenzaremos a ejecutar el plan."
            hide pureseptem3risa
            show pureseptem2normal
            septem "Pero antes debo informar esto."
            septem "Para que todos comiencen a mantener sus dominios en las condiciones óptimas para recibir humanos."
            septem "Una vez que Sextam pueda hacerlos."

        "¿Necesitas que ayude en algo?":
            septem "Tu mera presencia ya es ayuda más que suficiente, [nombrejugador]."

    hide pureseptem2normal
    hide pureseptem3risa
    show pureseptem2blush
    "Septem te mira fijamente y se debate entre hablar más o no."
    hide pureseptem2blush
    show pureseptem3serio
    septem "Tengo algo que darte luego de la reunión."
    septem "Creo que te lo mereces."
    "Te confiesa de manera muy seria, como si de un secreto fuera. Aunque dentro de él puedes sentir una pizca de emoción."
    
    
    menu:

        "¿Obtendré algo?":
            hide pureseptem3serio
            show pureseptem2feliz
            septem "¿Hablas de un premio?"
            septem "ja ja ja..."
            septem "¿Crees que mereces un premio?"
            menu:
                "Sí.":
                    pass

                "¿No...?":
                    septem "..."
        "...":
            hide pureseptem3serio
            show pureseptem2feliz
            septem "¿No vas a preguntar?"
            septem "No creí que fueras tan tímido."
            septem "Adorable."
    hide pureseptem2feliz
    show pureseptem2risa
    septem "Mmmm~"
    septem "Sí"
    "Dice finalmente, agarrando tu mano izquierda, y mientras la acaricia sus uñas rozan tu piel, peligrando con clavarse en ella."
    septem "Mereces un premio."
    septem "Has hecho todo lo que te he pedido hasta ahora."
    hide pureseptem2risa with dissolve
    "Su cuerpo se acerca a tu campo de visión, bloqueando todo lo que no sea él."
    septem "Creo que darte un cuerpo sería un buen premio, ¿No crees?"    
    "..."
    scene septem_leyendo with dissolve
    "Septem mata el tiempo en la biblioteca, te lee, esta vez son cuentos infantiles escritos por Sextam..."
    "Antes de empezar la lectura, te ha explicado que ella, cuando aún existian humanos en El Jardín, ella se mezclaba entre ellos para inspirarse a escribir."
    "Y cómo él la observaba desde su dominio. Cuando aún no tenía un cuerpo físico."
    "Se ve muy orgulloso al leer los cuentos, con una leve sonrisa pegada al rostro, que pareciera iluminar todo su rostro. Dándole un aire etereo." 
    "Ojos principales pegados a las páginas, mientras que los restantes te roban miradas furtivas de vez en cuando, asegurándose de que aún sigas aquí."
    "La voz de Septem al leer en voz alta es dulce... extremadamente dulce y cálida. Tiene una gran capacidad al transmitir el sentimiento de cada cuento por separado, tan al la perfección, como si ya los hubiera leído antes." 
    "Toma las pausas necesarias y utiliza el tono adecuado para cada personaje, en ningún momento se traba o es tomado desprevenido por los acontecimientos que suceden."
    "Mientras más se acerca la hora de la reunión, la cara de Septem comienza a mutar. Ojos principales entrecerrados, denotando que su mente se está yendo y pensando en el futuro cercano."
    "Ya debería estar preparándose."
    "Pero prefiere terminar, al menos un último cuento."
    "Llega un punto en que su voz deja de reproducir las palabras escritas en el libro, y en sus ojos se cierran por completo al sentir como llega el primer par de invitado a su dominio. Su cara muta, ya su expresión etérea se difumina cuando sus labios se tuercen hacia un lado."
    stop music fadeout 2.0
    "Septem cierra el libro de golpe y chasquea la lengua."
    scene bibliotecaseptem with dissolve
    "Se levanta de la silla y deja el libro de cuentos a un lado de su escritorio, junto a los papeles que usó para romper los sellos."
    show pureseptem1hablando with dissolve
    septem "Eso fue todo."
    "Tu ojo, y Septem, presienten más entidades dentro del dominio."
    "Ya es la hora. El consejo junto con los Estandartes ya han llegado y esperan a que Septem haga su aparición para poder comenzar la reunión."
    hide pureseptem1hablando
    show pureseptem2incomodo
    septem "Van a preguntar que ha pasado con mi cuerpo tarde o temprano..."
    "Luego te mira a ti, y su expresión se torna exasperada."
    hide pureseptem2incomodo
    show pureseptem2normal
    septem "Van a preguntar por ti y porqué estás así..."
    septem "Cómo los odio..."
    hide pureseptem2normal with dissolve
    "Con un último suspiro, Septem se arregla el cabello y con un solo movimiento de sus manos, los teletransporta a la sala de reuniones."
    scene consejo with dissolve
    play music "audio/meeting.mp3" fadein 2.0 volume 0.2
    "Un montón de ojos se posan en ustedes."
    septem "Buenas noches a todos los presentes."
    septem "Agradezco su asistencia"
    "Septem da un paso al frente. El silencio en la sala es absoluto y pesado."
    "Todas las entidades que representan al consejo, miran con un disgusto enmascarado de horror a Septem. En cambio los Estandartes, lo contemplan en silencio, esperando a que hable."
    "Uno del consejo no puede mantener su compostura y habla sin que se le ceda la palabra."
    el "¿Qué es esa {i}entidad{i} que tienes al lado? Ese no es El Cre-"
    septem "Cierra la boca, no te he dado el permiso de hablar."
    septem "Insolente."
    "La entidad hace una mueca de dolor, y Septem suelta una risa seca."
    septem "Como pueden ver, he cambiado. Y con ello he decidido compartir este Jardín con quien sí nos ve."
    septem "Ya no podemos seguir esperando a Padre."
    "Algunos miembros del consejo murmuran a sus Estandartes, con preocupación."
    septem "He obtenido un rango absoluto, gracias a nuestro nuevo salvador."
    septem "Y gracias a ello, ahora puedo destruir y borrar todas las condenas que nos han puesto encima."
    septem "Al que no le parezca correcto el cambio de mando, lo invito cordialmente a dejar su cargo."
    septem "Este Jardín fue olvidado por Padre. Quien nos abandonó."
    septem "Pero, a partir de hoy, comenzará una nueva era."
    septem "Dominios enteros serán reestructurados para impedir una segunda caída."
    septem "Ya no responderán a un Creador ausente."
    septem "Responderán a {i}[nombrejugador]{/i} y a mí."
    scene consejo1 with dissolve
    "Septem se desliza hasta su silla y toma asiento con una gracia que se acentua con cada movimiento. Cuando ya es encuentra cómodo, junta ambas manos y observa a su público."
    septem "¿Alguien tiene alguna duda?"
    "La misma entidad que se le obligó callar levanta la mano con urgencia."
    septem "Adelante."
    "Septem le cede la palabras y al instante sus labios se despegan, permitiéndole hablar nuevamente."
    el "¿Y si nos negamos? ¿Y si este nuevo 'amo' resulta no cumplir con los estándares que tenía el anterior?"
    "Mira a los demás, buscando apoyo."
    el "¿Realmente vas a cambiar al Creador tan fácilmente? ¿Por un cualquiera?"
    el "Ni siquiera es capaz de manifestar su cuerpo como corresponde, y te usa a ti en su lugar."
    el "Por favor, ¿de qué poder estamos hablando--"
    scene consejo2 with dissolve
    "El aire se densifica. Los ojos de Septem se entrecierran y su mano se levanta en augurio de una represalia..."
    menu:
        
        "Septem, para.":
            "Septem se detiene. Por un momento, parece considerar tus palabras."
            if septemconfianza >= 4:
                scene consejo2b 
                "Te mira por un segundo, e increíblemente baja la mano y cierra los ojos."
                "Su puño tiembla, no es muy notorio a simple vista, pero tu te das cuenta."
                "Él está aguantando actuar con rabia. Después de todo, el comentario de la entidad, es una ofensa tremenda para Septem."
                "Y no solo fue una vez... han sido dos."
                scene consejo2
                septem "Andrómeda, agradece que [nombrejugador] no quiere ver un castigo."
                septem "Sino ya no tendrías una lengua para hacer más comentarios ácidos."
                septem "Pero si te vuelvo a escuchar, perderás más que eso."
            
            else:
                scene consejo2a
                "Septem ni siquera te dirige la mirada."
                "{sc=2}Por favor. No me digas que hacer...{sc=2}"
                "{sc=2}Te han insultado, [nombrejugador].{/sc}"
                "{sc=2}No voy a dejarlo pasar.{/sc}"
                call castigo from _call_castigo
                
        "Septem, castígalo.":
            $ septemconfianza += 1
            call castigo from _call_castigo_1
            pass
                
        
        "Dejar que Septem lo resuelva.":
            $ septemconfianza += 1
            call castigo from _call_castigo_2
            pass

    scene consejo2 
    septem "¿Alguien más tiene alguna pregunta?"
    "Algunas manos se levantas, esperando a que Septem les de la palabra."
    scene consejo2b
    "Antes de ceder la palabra a alguno de los presentes, el rubio te mira de reojo."
    "{sc=2}Ahora hablaremos de logística...{/sc}"
    "{sc=2}No es necesario que escuches todo esto.{/sc}"
    "_______________________________________"
    scene reunion with pixellate
    stop music fadeout 2.0
    "Cuando el último de los asistentes al consejo abandona el dominio, Septem busca tu ojo."
    show pureseptem2feliz with dissolve
    play music "audio/fell.mp3 " fadein 2.0 volume 0.4
    "Al encontrarlo con la mirada, sonríe y te llama con una voz pegajosa y sofocante. Toma tus manos entre las suyas y con un tono bajo te dice."
    septem "Creo que te has ganado el premio..."
    septem "Ven conmigo."
    hide pureseptem2feliz with dissolve
    scene blanco with dissolve
    "Él no se hace esperar, los transporta a ambos a la zona pura."
    show pureseptem3risa with dissolve
    septem "Un cuerpo..."
    septem "Identidad..."
    hide pureseptem3risa
    show pureseptem3riendo
    septem "Ambas cosas van de la mano. ¿No crees?"
    menu:
        "No.":
            hide pureseptem3riendo
            show pureseptem1callado
            septem "¿Hmmm?"
            hide pureseptem1callado
            show pureseptem2feliz
            septem "¿En serio?"
            septem "Jaja."
            "Septem ignora tu respuesta."

        "Así es.":
            hide pureseptem3riendo
            show pureseptem2feliz
            pass

    septem "Si yo te doy un cuerpo nuevo. Y lo decoro, dejándote cero espacio a ti para que hagas algún cambio."
    hide pureseptem2feliz
    show pureseptem2sonrisa
    septem "¿Serías capaz de permitirme ello?"
    menu:
        "Sí.":
            hide pureseptem2sonrisa
            show pureseptem2risa
            septem "Hmmm..."
            septem "¿Aunque no sea de tu gusto? ¿Aunque no te sientas cómodo con o te identifiques con ello?"

        "No.":
            hide pureseptem2sonrisa
            show pureseptem2risa
            septem "Muy bien."
            septem "Así me gusta."
    hide pureseptem2risa
    show pureseptem3risa
    septem "Bueno, no importa. El cuerpo que te haré también será un regalo."
    septem "Uno del cual tendrás modificar a tu gusto."
    hide pureseptem3risa
    show pureseptem2feliz
    septem "Yo te daré un canvas, en blanco. Y tu te encargarás de moldearlo a tu gusto, mi querido pequeño Creador."
    "Septem toma tus manos y tus ojos en sus palmas. Realizando movimientos lentos y delicados, los fusiona con cuidado."
    scene negro with dissolve
    "Dejas de ver por unos segundos. Pero tus demás sentidos se multiplican y danzan entre sí, coordinados hasta en el más mínimo detalle."
    "Sonidos se entrelazan con el calor y el frío del espacio en el que ahora te encuentras parado." 
    "Es confortante la sensación de estar, de existir. Una que va creciendo con los segundos."
    "Primero tus piernas y luego tus brazos, seguido por la cabeza. Te ramificas en un cuerpo humanoide sin restricciones. Es una carrera sin apuros, donde Septem te acompaña tomando tu mano."
    "Guiando y a la vez permitiendo que tú hagas los cambios necesarios."
    "La sensación de estar vivo crece más. El toque viscoso de los órganos expandirse y retraerse te llama a pedir más."
    "El tacto aparece de forma gradual. Un cosquilleo placentero nace con el paso de los dedos de Septem por tu forma."
    scene septem_regalo1 with dissolve
    "Tus piernas captan la suave brisa y tus mejillas recién formadas sienten la húmeda respiración de Septem."
    "Tu cuerpo va despertando a partir de diez llamas que queman pero no dañan."
    "Sus manos viajan por tu cuerpo ya completamente formado, tocando y encendiendo todo a su paso. No es un toque lascivo, ni perverso." 
    "Es un toque que da vida a tu forma, un toque que poco a poco te permite respirar y palpitar."
    "Es como el beso de la vida que siempre habías estado esperando. Un cuerpo completamente tuyo."
    "Tuyo y de nadie más."
    "Algo que puedes llamar tú."
    scene septem_regalo2 
    septem "Precioso."
    septem "Tu cuerpo no es solo un avatar, es la expresión más pura de ti en este dominio."
    hide septem_regalo2
    show septem_regalo1
    septem "..."
    hide septem_regalo1
    show septem_regalo
    septem "Eres perfecto."
    "Septem te acaricia la mejilla con su pulgar."
    if septemconfianza >= 6:
        hide septem_regalo
        show septem_regalo2
        septem "Voy a darte algo más..."
        septem "Tú me has dado tu tiempo y un espacio para el cambio. Y estoy agradecido por ello, más de lo que tú piensas."
        septem "También tengo que confesar que tu compañía es algo que he aprendido a desear."
        septem "... ya no imagino un día sin ti."
        septem "[nombrejugador], debo confesarte que eres alguien importante para el jardín... y para mí."
        septem "Si bien estamos conectados en cuerpo y en alma, yo no puedo llamarme tuyo... aún."
        septem "Pero podemos comenzar con esto."
        septem "Lo puedes usar cuando desees y yo estaré ahí para ti."
        $ persistent.nulla_symbol = False
        $ persistent.septem_symbol = True
        septem "Este será nuestro puente."
        septem "No importa dónde estés, podrás contactar con mi alma."
        septem "Y yo te encontraré."
        septem "A tu izquierda debería estar mi regalo, ve si lo puedes encontrar y ocuparlo."
        $ persistent.septem_symbol2 = True #Cuidao juju
    else:
        pass

label continuacion4:
    scene jardinseptem with dissolve
    stop music fadeout 2.0
    "..."
    play music "audio/hope.WAV" fadein 2.0 volume 0.4
    "Pasan el día descansando fuera del templo."
    "Mañana será el día en que se romperá el sello de Sextam. Mañana será un día ajetreado... hoy no."
    "Hoy Septem descansará lo que queda del día junto a ti."
    "... esto se siente bien."
    "Septem está perdido en sus pensamientos, por lo que no está muy abierto a conversar contigo."
    "Cuando te aburres de mirar el paisaje, posas tu mano en el hombro de Septem, llamando su atención."
    show pureseptem2enojo with dissolve
    "Gira su cabeza y te revela un poco de lo que le carcome la cabeza."
    septem "Ahora que tienes un cuerpo, Nulla puede aparecer y robarte."
    hide pureseptem2enojo
    show pureseptem2normal
    septem "He visto lo que puede hacer."
    hide pureseptem2normal
    show pureseptem3serio
    septem "Lo he visto en las líneas del código-- no tengo acceso a todas, pero a las que ya has jugado si."
    menu:
        "¿Sabes de las otras rutas?":
            hide pureseptem3serio
            show pureseptem3enojo
            septem "Así es."
            septem "No puedo acceder a toda la información, pero sí."
            hide pureseptem3enojo
            show pureseptem2normal
            septem "No me duele tanto, pues ahora estás aquí conmigo."
            hide pureseptem2normal
            show pureseptem2feliz
            septem "Y haré que te quedes con esta línea temporal al final."
            septem "No es una promesa, es un hecho."

        "¿Sabes acerca del plan de Nulla?":
            hide pureseptem3serio
            show pureseptem3enojo
            septem "Ahora lo he confirmado."
            septem "Por eso mismo, es peligroso que salgamos."

    menu:
        "¿Eso significa que ya no habrán más bad ends?":
            pass
    hide pureseptem3enojo
    show pureseptem2feliz
    septem "¿Quieres uno?"
        
    menu:
        "Sí.":
            stop music fadeout 1.0
            "..."
            play music "audio/woo_scary.WAV" fadein 3.0 volume 0.6

            call septem_corazon from _call_septem_corazon
            
        "No.":
            hide pureseptem2feliz
            show pureseptem3callado
            septem "..."
            "Septem ha intentado reprimir ese lado ahora que tiene acceso directamente a ti."
            "Pero, la carne es débil, y el deseo ahora es más fuerte que la razón."
            "Solo esta vez... no importa, a ti no te va a doler."
            "Y es la primera vez que puede confesar que extraña que tu tengas a la antigua marioneta."
            "La que nunca fue una representación tuya."
            "La que sentía, la que lloraba, la que daría todo por ti."
            "Septem respira intentando calmarse."
            "No, ahora no."
            "Ahora no puede perder los estribos."
            "Después de todo, eres tú."
            "Y no tiene deseos de ofender tus posesiones por un deseo fugaz."
            "...A menos que tú no quieras."
            "Puede intentarlo una vez más."
            "Solo una vez más."
            hide pureseptem3callado
            show pureseptem2blush
            septem "¿Seguro?"
            hide pureseptem2blush
            show pureseptem2feliz
            septem "Puedo darte uno, después de todo, volverás aquí conmigo..."
            "Septem sonríe con una pizca de complicidad."
            "Él también quiere verlo..."
            menu:
                "No quiero.":
                    septem "Comprendo."
                    septem "No volveré a preguntar."
                    septem "Disculpa, [nombrejugador]."
                    
                    
                "Vale.":
                    stop music fadeout 1.0
                    "..."
                    play music "audio/woo_scary.WAV" fadein 3.0 volume 0.6

                    call septem_corazon from _call_septem_corazon_1
    
    "..."
    stop music fadeout 2.0
    scene temploseptem with dissolve
    "Llega un momento en que Septem te comenta que deberías descansar, ya que tu cuerpo sigue teniendo necesidades de los mortales."
    "Comer, beber, dormir... todo el pack. La única diferencia es que no puedes morir."
    septem "Mañana te despertaré para comenzar con nuestras tareas."
    septem "Te presentaré ante todo el Jardín."
    septem "Como nuevo amo y señor de estas tierras."
    septem "Nuestro salvador."
    scene negro with dissolve
                        


    #"FIN DEL ACTO 2.5_________"
    #"En proceso de elaboración..."
    #"{sc=2} Tendrás que esperar un poco para descubrir como acaba esto... :3{/sc}"
    #"..."
    jump acto3_septem


label acto3_septem:
    scene blanco with dissolve
    "..."

    play music "audio/hope.WAV" fadein 2.0 volume 0.4
    
    "Aunque tienes tu propio cuerpo, sigues estando conectado a Septem, para bien o para mal. Es algo a lo que nunca te podrás deshacer."
    "Donde quiera que vayas, ya sea en el mundo físico o en el mundo donde reside tu consciencia, una parte de él estará a tu lado."
    "Y los sueños no son la excepción. No lo fueron cuanto estabas junto a él y no lo son ahora que técnicamente eres un ser independiente de él."
    "Sus sueños ahora son los tuyos. Los sueños que controlan a Septem cuando descansa ahora te controlan a ti. Haciendo que ambos se vean atrapados en los mismos pesares que agobian su mente."
    "..."
    "Escuchas como una voz te llama, desde el fondo del suelo. Es insistente e intensa, lo suficiente para provocar que las piernas te tiemblen de tan solo sentir las vibraciones que acompañan el canto de tu nombre al ser llamado desde el fondo..."
    "Reconoces la voz. Es la voz que le pertenece a la primera entidad que te dio la bienvenida a este mundo."
    
    play music "audio/fronbondi2.mp3" fadeout 1.0 fadein 2.0 volume 0.4

    "Padre te llama."
    "{i}Septem... [nombrejugador]...{i} No estás seguro a cuál nombre llama. Lo que sí sabes, es que las náuseas y el miedo que sientes, no es tuyo."
    scene negro with dissolve
    centered "Regla número uno: Nada puede entrar o salir del Jardín. Está estrictamente prohibido."
    scene act3_s1a with dissolve
    creador "Y aun así, dejaste que Nulla saliera y te trajera un cuerpo."
    scene negro with dissolve
    centered "Regla número dos: Se te tiene prohibido dañar a los tuyos. Y así nada ni nadie que tenga origen dentro del Jardín puede dañarte de vuelta."
    scene act3_s1 with dissolve
    creador "Y a sabiendas de que has roto la primera regla, has tenido las agallas de romper la segunda."
    creador "Tú no aprendes."
    show act3_s1a
    creador "Predicas seguir las reglas a todos tus súbditos, pero no prácticas."
    creador "Tu boca solo expulsa hipocresía."
    scene negro with dissolve
    centered "Regla número tres: el Jardín debe funcionar a como dé lugar."
    scene act3_s1 with dissolve
    creador "No importa lo que tengas que hacer. Cambios, reemplazos de tus Estandartes, o incluso empezar desde cero, con tal de seguir con vida a tu alrededor."
    show act3_s1a
    creador "..."
    creador "Es más fácil volver a empezar."
    creador "Borrar todo y comenzar de nuevo."
    creador "Mismos conceptos, distinto mando."
    hide act3_s1a
    creador "Pero... veo que te has encariñado con los tuyos a un a sabiendas de que son defectuosos."
    scene negro with dissolve
    centered "Siempre supe que eras un sentimentalista... y un terco."
    centered "Desde el día que te cree."
    centered "..........."
    scene act3_s1a with dissolve
    creador "Bien."
    show act3_s1
    creador "Lo has conseguido."
    creador "Rompe ese sello y sigue con tus Estandartes a tu lado."
    creador "Solo recuerda una cosa."
    hide act3_s1
    creador "Deberás aplicar mano dura para evitar más deslices."
    scene negro with dissolve
    "..."
    "......."
    scene blanco with dissolve

    stop music fadeout 2.0

    "La voz por fin deja de llamar tu nombre."
    "Abandonándote una vez más."
    "No puedes evitar sentir un poco de tristeza. Incluso en un sueño, Padre no te ha dicho más que acusaciones y recomendaciones que nadie le ha solicitado."
    "Nada que te tranquilice a ti o a tu intangible corazón."
    "Ahora, sin nada a lo que agarrarte, comienzas a caminar por el sendero imaginario que se forma con cada paso que das."
    "Paso tras paso, tu yo comienza a dejar el espacio de tu mente, para recobrar lentamente los sentidos de tu cuerpo físico."
    "..."
    "-------------"
    scene camaseptem with dissolve
    

    play music "audio/hope.WAV" fadein 2.0 volume 0.4
    
    "Lo primero que percibes es lo pesado de tu cuerpo y lo cansado que están tus músculos. La gran mayoría de ellos queman y se tensan cada tanto."
    "Luego viene la autopercepción. Eres Tú. Ya no un Él, o una extraña mezcla que te transforma en {i}Ellos{i}."
    "Sigues conectado a Septem, claro, aún sientes su presencia. La diferencia es que ahora, estando despierto, eres solo un tú. Alejado de sus pensamientos y preocupaciones subconscientes."
    "Y lo agradeces, sintiendo como se te infla el pecho con el gozo egoísta de desear individualidad."
    "Te estiras para ser recibido por más dolor y tensión de tus músculos y tendones. Pero eso te permite dejar de lado la confusión que procede después pasar del sueño al despertar."
    
    scene habitacionseptem with dissolve
    
    "Le echas un vistazo fugaz a la habitación. Sigue siendo la misma de siempre, sin ningún cambio aparente o que se pueda captar a primera vista."
    septem "Ya te has despertado..."
    
    if septemconfianza >= 6 and persistent.septem_symbol == False:
        
        septem "Oh."
        scene blanco with dissolve
        septem "..."
        septem "Espera..."
        "Escuchas una risa que proviene de todos lados."
        septem "Oh, ya veo..."
        septem "Has estado jugando con la basura esa..."
        septem "Entiendo tu curiosidad morbosa."
        septem "Pero no permitiré que la lleves aquí..."
        $ persistent.nulla_symbol = False
        $ persistent.septem_symbol = True
        $ persistent.septem_symbol2 = True
        septem "Listo."
        septem "Ahora no tienes como impedir que te encuentre cuando sea necesario."
        scene habitacionseptem with dissolve
        
    
    else:
        pass

    "Su voz se escucha en todos lados, haciendo que la sensación de dejà vu te sacuda el cuerpo. Ya has vivido esto antes."
    "Tus ojos lo buscan sin preguntarte si quieres o no. Es una respuesta automática."
    
    show pureseptem1callado with dissolve

    "Lo encuentran cruzando la puerta que divide tu habitación de la sala del templo."
    "Se ve calmado, pero su pecho yace apretado por algo que no puedes descifrar aún... no sabes si se debe al nerviosismo de lo que está por venir o por el sueño que has tenido..."
    "¿Será que Septem sabe lo que has soñado? No es como si él también estuviera dormido como para participar en el sueño junto contigo... ¿o sí?"
    "Tus labios tiemblan, con ansias de preguntar y quitarte la duda. Pero Septem te interrumpe antes de que puedas tomar una decisión."
    
    hide pureseptem1callado
    show pureseptem1hablando

    septem "Espero que hayas podido descansar bien."
    septem "Estuve monitoreando tu cuerpo mientras lo hacías, y..."
    hide pureseptem1hablando
    show pureseptem2sonrisa
    septem "Tienes las mismas reacciones que tendría un humano al dormir."
    hide pureseptem2sonrisa
    show pureseptem2feliz
    septem "Realmente eres perfecto. Una recreación perfecta de lo que serías si estuvieras aquí en realidad."
    menu:
        "Buenos días.":
            hide pureseptem2feliz
            show pureseptem1sonrisa
            "Septem forma una sonrisa que abarca sus ojos también, formando pequeñas lineas de expresión a sus costados."
            septem "Buenos días."
        
        "¿Hoy empezamos con la reconstrucción del Jardín?": 
            hide pureseptem2feliz
            show pureseptem1sonrisa
            septem "Así es."
        
        "...":
            pass
    "Él se acerca hasta estar a una distancia prudente entre la cama y él. Te mira por unos segundos antes de ofrecerte la mano en un delicado gesto para que la tomes."
    "Y espera atento a tus movimientos."
    menu:
        "Tomarla.":
            $ septemconfianza += 1
            "Aceptas su mano, colocando la tuya sobre la de él. El contacto parece despertar una chispa entre tu mano y la suya, una chispa cálida y acogedora que te invita a seguir sujetando su mano hasta cansarte..."
            "Supones que debe ser porque tanto tú como él, están atados por el cuerpo y alma, lo que provoca que cada contacto sea una recompensa que busca que ambos quieran estar juntos en todo momento."
            "O simplemente es la reacción del contacto de un cuerpo cargado de electricidad estática con otro."
            "Siendo sincero no te importa. Cualquiera que sea la razón, te gusta sentir esto con el contacto de Septem."
            "Se siente bien."
    
        "No tomarla.":
            "No aceptas su mano y en su lugar te levantas por tu cuenta."
    
    septem "He preparado el desayuno. No voy a sacarte de mí templo sin la energía debida."
    septem "Se viene un día largo, y no sé si tu cuerpo lo podrá aguantar por completo."
    
    scene act3_s2 with dissolve

    "El rubio hace una seña con su mano, que convierte la habitación en el comedor del templo. La mesa está llena de alimentos pensados en una dieta saludable y balanceada para consumir como primera ración del día."
    "La fruta está cortada en cubitos, todos perfectos y del mismo tamaño. Tienes que acercar un poco tu cara para poder apreciarlos como es debido (y buscar alguna imperfección en el proceso). Parecen de mentira por lo exactas que son todas las porciones."
    "Son tan apetitosas a la vista que parecen dulces postres refinados, capaces de hacer que hasta la gente que no gusta de la fruta se le haga agua la boca."
    "Hay un frasco con miel y mermelada, con un color intenso. Pan en pocas cantidades, humeante y fresco. Y un montón de otras cosas que, si te detienes a ver una por una, terminarás más espantado que encantado."
    "Si no conocieras a Septem, jurarías que esto es una trampa elaborada con el fin de hacerte comer y bajar la guardia con lo lindo que se ve todo. Lo cual, no es el caso."
    "Septem lo ha hecho porque puede y quiere, sin motivos ocultos más que hacer que tu cuerpo recupere energía."
    "Lo tierno del asunto es que, se ha tomado el tiempo de hacer que la comida se vea estéticamente atractiva visualmente para ti. Porque necesidad no tiene él para poner tanto empeño en la decoración de la mesa."
    "Septem es lindo... cuando quiere."
    show ps_mesa_hablando
    septem "Puedes comer todo lo que hay en la mesa."
    "Dice, sentándose al frente tuyo con una copa en mano."
    jump s_preguntas_act3


#EDITAR EL MENU EN LABELACT2
label acto3_septem_continuacion:
    scene ps_mesa_normal
    "Estás por darle el último bocado a tu desayuno cuando Septem baja la copa, dejándola en la mesa."
    show ps_mesa_sad
    septem "Acerca de Madre..."
    septem "Lo ví en tus memorias. Ella te contactó en tus sueños---"
    hide ps_mesa_sad
    show ps_mesa_serio
    septem "Lo que pide es una barbaridad..."
    septem "Los ojos que tenemos me sirven para hacer conexión con todos en el Jardín."
    hide ps_mesa_serio
    show ps_mesa_sad
    "Sus manos se juntan, y suelta un suspiro ahogado que te produce escalofríos. Se le ve nervioso."
    "Es una imagen extraña de ver. Septem mostrándose de esta manera delante de ti, como si se quebrara algo que hace tiempo debería haberse quebrado."
    "Tal como si dejara de tirar de la cuerda que lo sostiene e impide mostrarse genuinamente. Dejando la máscara de líder de lado por un momento, para mostrar a una entidad muy similar a un humano."
    septem "Romper el sello que Padre le ha puesto a Sextam nos expondrá a su atención..."
    septem "Y que Madre me pida romper todos los ojos... es una sentencia de muerte para mí."
    septem "Tanto Padre como yo vemos a través de estos."
    septem "No es una buena idea."

    menu:
        "¡Pero puedes crear otro sistema para observar!":
            $ powerhungry += 5
            hide ps_mesa_sad
            show ps_mesa_serio
            septem "Eso ya lo sé."
            septem "Pero romper los ojos sería una declaración de independencia."
            menu:
                "¿Y si es eso lo que él quiere?":
                    hide ps_mesa_serio
                    show ps_mesa_sad
                    septem "..."
                    hide ps_mesa_sad
                    show ps_mesa_serio
                    septem "¿Qué dices?"
                    septem "Padre gusta de monitorear todo, no va a permitir que yo haga tal cosa."
                
                "¡Si no cortas los ojos, no expones a todos!":
                    septem "Y cortarlos también nos expone a un ataque por su parte."
                    septem "[nombrejugador], no es una elección fácil."

                "Tienes razón.":
                    pass
        
        "Tienes razón.":
            
            septem "Es lo único que no podemos cambiar..."
            pass

    septem "....."
    septem "Puedo hacerlo, pero---"
    scene comedorseptem with dissolve
    "Septem se levanta de golpe, enojado consigo mismo. El sonido de la silla raspar el suelo hace que tu cuerpo salte y tus oídos duelan."
    show pureseptem1hablando
    septem "Déjame pensarlo."
    septem "Necesito tiempo."
    hide pureseptem1hablando
    show pureseptem2enojo
    septem "No voy a arriesgar todo por Madre o el control total del Jardín."
    hide pureseptem2enojo
    show pureseptem3serio
    septem "Voy a estar en la biblioteca. Si me necesitas estaré ahí hasta el mediodía."
    hide pureseptem3serio
    show pureseptem2sonrisa
    septem "Luego iremos a la ceremonia de iniciación."
    septem "Te dejé tus vestimentas para la ceremonia en tu habitación."
    hide pureseptem2sonrisa
    "Septem se retira, sin antes hacer desaparecer los platos y la comida sobrante de la mesa."
    "... Tú lo dejas ir."
    "Necesita tiempo solo."

    menu:
        "Ir a ver la vestimenta.":
            pass


    scene pasilloseptem with dissolve
    
    "Caminas por los pasillos del templo hasta llegar a tu habitación." 
    
    scene habitacionseptem with dissolve
    
    "Al entrar, notas en la cama telas que no hacen encaje con tus sábanas y asumes que esas deben ser las ropas que Septem te ha dejado."
    
    scene cama_septem1 with dissolve

    "Te acercas para inspeccionarlas."
    "Cada pieza que compone el conjunto está desplegada por orden en el que se debe poner." 
    
    scene cama_septem2 with dissolve

    "Primero las capas inferiores, luego las capas superiores, terminando con los adornos."
    "Luchas con cada prenda al intentar ponértela, cada una te toma más tiempo de lo que te gustaría admitir."
    
    show vestimenta with dissolve
    "Hmm..."
    "Cuando terminas, examinas tu trabajo: La túnica color marfil que te cubre todo el cuerpo, cae de manera impecable hasta tocar el suelo. Las mangas son largas en exceso, haciendo dificultoso el movimiento de tus brazos."
    "Los patrones que decoran y recorren la tela son similares a los que posee Septem, más no iguales. Esta es una vestimenta que complementa a la de Septem, más no copia."
    
    hide vestimenta with dissolve

    "Al dar tu primer paso, comprendes algo importante." 
    "Lo que llevas puesto no es una prenda hecha para moverse con facilidad."
    "Debes tener cuidado con cada paso que das, procurando no enredar tus pues en las telas que se arrastran por el suelo." 
    
    jump act3_explorar_septem


label acto3_septem_continuacion2:
    
    play music "audio/calamity.WAV" fadeout 1.0 fadein 2.0 volume 0.4

    "Una vez llegan a la entrada el templo, te observa por unos segundos, inspeccionando tu apariencia de pies a cabeza."
    
    scene act3_s3 with dissolve
    
    "Sus manos suben hasta alinearse con tu pecho, cuando piensas que posará su palma en tu corazón, Septem agarra la tela que cubre tu pecho para arreglarla."
    septem "Hoy necesito que no te despegues de mi lado."
    septem "No mires al resto a los ojos y mantente alejado de las voces que llamen a tu nombre."
    menu:
        "Está bien, Septem.":
            scene pared
            show act3_s3a 
            with dissolve

            "Tu respuesta le saca una sonrisa satisfecha."
            septem "¿Aceptas sin consultar?"
            "..."
            "Sus manos dejan tu ropa para acariciar tu mejilla con firmeza."
            hide act3_s3a 
            show act3_s3b
            septem "Eres ingenuo."
        
        "¿Por qué?":
            scene pared
            show act3_s3c
            with dissolve

            "Septem frunce el ceño, no acostumbrado a ser cuestionado por otro ser."
            septem "Porque es peligroso."
            septem "Eres como un..."
            hide act3_s3c
            show act3_s3e

            "Pausa un segundo, procesando si la palabra que estaba a punto de usar corresponde ser usada o no."
            hide act3_s3e
            show act3_s3d
            septem "Apenas tienes el poder de confirmar cambios."
            septem "No sabes comandar y tu cuerpo no te permite crear nada aún."
            septem "Sigues estando confinado en un cuerpo que no responde del todo tus deseos."
            hide act3_s3d
            show act3_s3e
            septem "..."
            hide act3_s3e
            show act3_s3d
            septem "Si te quedas solo, ellos no dudarán en romperte en pedazos."
            septem "El más fuerte manda, así funciona."
            hide act3_s3d
            show act3_s3e
            "Eso no te lo esperabas... ¿no se supone que tienes un rango alto?"
            "Estás a punto de ser presentado como el amo y señor de estas tierras, ¿pero eres débil?"
            "Septem ve la confusión en tu rostro."

    hide act3_s3b
    hide act3_s3e
    show act3_s3d
    with dissolve

    septem "Todos funcionan mantener el Jardín funcionando a como de lugar."
    septem "Si el resto ve a un Estandarte o alto rango deficiente, no dudarán en romperlo y comerlo para tomar su poder y lugar."
    septem "Y tú, mi querido pequeño Creador, tienes un rango muy deseado."
    septem "Pero tu cuerpo no rinde lo que debería rendir."
    septem "Ya que tú, solo confirmas los cambios, no creas."
    hide act3_s3d
    show act3_s3e
    
    "Abres la boca para soltar tus temores y dudas, pero las manos de Septem atrapan las tuyas, juntándolas y llevándolas frente tuyo."
    hide act3_s3e
    show act3_s3f
    
    "Se inclina un poco para poder verte directamente a los ojos, con sus cejas arqueadas y una sonrisa que pide perdón sin dejar de ser algo condescendiente..."
    septem "Déjame cuidarte hasta que podamos transferir este mundo a ti por completo."
    septem "Hasta ese entonces ---no dejaré que nadie te ponga una sola mano encima."

    hide act3_s3f with dissolve
    scene temploseptem with dissolve

    "..."
    "Te sientes algo traicionado. Por un momento Septem te hizo creer que ya tenías todo a tu merced."
    "Te llamó próximo amo del Jardín, te dio un cuerpo que puede ser regenerado, pero..."
    "Todo esto, todo tu rango depende de él..."
    "No eres más que una flor encapsulada en una cúpula de hierro."
    #Cambio de escena.
    show pureseptem1sonrisa with dissolve

    "Septem te mira, notando como tus pensamientos comienzan a divagar de lo que sucede a tu alrededor, mas no te interrumpe. Sus manos ajustan una última cosa en tus ropas y se retiran de tu espacio personal."
    "Levanta sus manos una vez más, preparándose para invocar a ambos al lugar dónde el resto del Jardín los espera."
    septem "Recuerda sonreír y no despegarte de mí."
    
    hide pureseptem1sonrisa with dissolve

    scene blanco with pixellate

    "Él hace señas con sus manos mientras recita palabras que no tienen significado para ti aún." 
    "Cuando tu vista es invadida por una luz intensa, Septem te toma de la mano con un agarre firme, que teme ser cortado. Sientes como bajo de toda esa cara de seguridad y expresión serena, algo estruja su pecho."
    "Es la duda. Duda a lo incierto del resultado en esta jornada. Duda y cuestionamiento al cambio, posiblemente."
    "Es inseguridad te contagia, invitando al miedo a colarse en tus entrañas. "
    "La sensación de caer te invade los sentidos, por un segundo crees que la superficie del suelo te ha tragado sin aviso. El vértigo es más grande que ti y no dudas en apretar la mano de Septem con fuerza, listo para agarrarse a su cuerpo con piernas y brazos si es necesario."
    "La luz molesta deja tus retinas en paz y junto con ello, el vértigo desaparece."
    "Has llegado a tu destino."

    play music "audio/sorry_cant_tell.mp3" fadeout 1.2 fadein 2.0 volume 0.2

    scene salon with pixellate
    
    "El lugar no es para nada lo que te habías imaginado. De cierta manera tu mente tenía proyectado un espacio similar al de la reunión anterior. Donde el tiempo y el espacio se mezclan, dejando una extraña brecha que no puede ser entendida por el ojo humano."
    "Lo que te da la bienvenida es nada más y nada menos que un salón para eventos. Masivo y pulcro, en sus muros ornamentados con molduras, te conducen a un techo que demandan levantar la vista para poder apreciarlos correctamente." 
    "Tomando en consideración lo amplio del lugar, parece un escenario ideal para un banquete o un vals."
    
    show invitados with dissolve

    "Ya hay entidades repartidas en cada esquina donde sus ojos se posen. La gran mayoría lleva máscaras que les tapan toda expresión en sus caras, acompañados por múltiples ornamentos que hacen juego con su vestimenta."
    "Es fácil darse cuenta de que no todos proceden del mismo lugar, por la forma y colores de sus máscaras."
    "Sin embargo, intuyes que todos los presentes ocupan posiciones importantes, todo material que los cubre es ostentoso, desde la cabeza hasta los pies..."
    "Te preguntas si las clases sociales serán tan marcadas aquí como lo son en el mundo humano, donde la repartija de recursos es dispareja."
    "Le sigues el paso, procurando no quedar atrás o ser absorbido por las figuras que bloquean tu paso, intentando llamar tu atención."
    "Septem camina por el lugar, saludando de vez en cuando a algunas entidades, sin darles la oportunidad para comenzar una conversación más extensa con él o contigo."
    "Él está buscando algo en particular."
    
    hide invitados with dissolve
    show act3_s5 with dissolve
    
    "Dan unos pasos más hasta frenar frente a un cúmulo de figuras femeninas que rodean a alguien. Estiras el cuello para poder tener más campo de visión, y solo gracias a que las entidades se dan cuenta de la presencia de Septem, es que puedes ver a quien ocultaban con sus cuerpos. Es Sextam."
    
    hide act3_s5
    show act3_s5a
    
    "Mientras las mujeres agachan la cabeza y saludan a Septem con su título, Ella ya tiene sus ojos puestos en ti. No se mueve ni habla, espera a que Septem le dirija la palabra."
    "Su rostro no refleja alegría... se le ve apática."
    "Septem les sonríe a las acompañantes de Sextam antes de dirigirse a ella."
    
    hide act3_s5a
    show pureseptem1sonrisa at left with dissolve 
    
    septem "Es un gusto ver a la corte del Seis en un evento público."
    "Sextam se cruza de brazos, mirando a una de las mujeres que tiene a su lado."
    
    show sextam1hablando at right with dissolve
    
    sextam "Durmieron por un largo tiempo. Supongo que ahora son necesarias ahora."
    
    hide pureseptem1sonrisa
    show pureseptem2sonrisa at left
    
    septem "Te serán útiles manteniendo y guiando a las nodrizas."
    
    hide sextam1hablando
    show sextam1triste at right

    sextam "Supongo..."
    
    hide sextam1triste
    show sextam1normal at right
    hide pureseptem2sonrisa
    show pureseptem1callado at left
    
    "La vibra del momento es pesada. Sextam no está interesada en hacer conversación con Septem y no se molesta en ocultarlo."
    
    hide pureseptem1callado
    show pureseptem1hablando at left
    
    septem "Entiendo cómo te sientes, pero es por el bien---"
    
    hide sextam1normal
    show sextam1enojo at right

    hide pureseptem1hablando
    show pureseptem1callado at left
    
    sextam "Ya lo sé, Septem."
    "Su voz sale lo suficientemente dura como para hacer que Septem se muerda la lengua y apriete los dientes. Sextam notando aquello, esboza una pequeña sonrisa, bajando así su intensidad."
    sextam "Haré mi trabajo, no dudes de ello."
    hide sextam1enojo
    show sextam1enojo2 at right
    "Suena sincera."
    
    hide pureseptem1callado
    show pureseptem1hablando at left
    
    septem "Jamás lo dudaría... pero me preocupa como te sientas."
    
    hide sextam1enojo2
    show sextam1hablando at right
    
    sextam "No es necesario hablar de eso ahora."
    
    hide sextam1hablando
    show sextam1triste at right
    
    sextam "..."
    sextam "Luego de esto, mi consejo quiere comentarte algunas observaciones que han hecho del dominio."
    
    hide pureseptem1hablando
    show pureseptem3serio at left
    
    septem "Pueden hacerlo ahora."
    septem "Unum y su consejo aún no llegan, tenemos tiempo..."
    
    hide pureseptem3serio
    hide sextam1triste
    with dissolve


    scene salon with dissolve
    show invitados with dissolve

    "Sextam deja que sus chicas sigan a Septem mientras recorren el lugar. Tú vas a su lado, sin participar de la conversación. No es que te interese tanto, pues con solo escuchar las primeras frases has captado que entiendes poco y nada de lo que están hablando."
    "Y ahora mismo no estás pendiente en hacer sentido a la logística."
    "Lo único que tienes que hacer ahora es seguirles el paso e ignorar las miradas de los demás invitados y alguna que otra consejera de Sextam que no tenga la palabra en ese momento."
    "Luego de caminar por un rato, tu túnica se ha convertido en tu peor enemigo hasta el momento. Te imposibilita moverte libertad, haciendo que te cueste seguirle el paso a Septem y el grupo de mujeres que revolotean a tu alrededor."
    "Ya has contado dos pasos en falso que casi te han hecho caer."
    "En un momento dado, un grupo de entidades se cruzan con ustedes, haciendo que pierdas por un segundo la figura de Septem. Y es ahí donde sientes un fuerte jalón en tu manga."
    
    scene act3_s6 with dissolve

    play music "audio/meeting.mp3" fadeout 1.2 fadein 2.0 volume 0.2

    "Te giras esperando encontrarte con la cara del rubio, pero te quedas helado al ver que quien te sujeta por las mangas es una entidad desconocida. Alta y robusta, con una cabeza pequeña que no hace más que acentuar su gran cuerpo."
    "Su mano te suelta por un segundo, solo para agarrar tu brazo, incrustando sus garras en la tela. Esto es peligroso, con un poco más de fuerza la tela sería traspasada y esas garras dañarían tu tierna piel."
    ell "¿Es cierto lo que dicen las lunas de Concejal Saturno?"
    "Su tono de voz tiene una mezcla de curiosidad junto con asco, que hace que quieras escapar de su agarre y correr a los brazos de Septem."
    "Te observa por unos segundos más antes de soltar con veneno en su voz."
    ell "Pareces más un sirviente que alguien digno de caminar junto a Septem."
    "Sus garras rompen la tela hasta llegar a tu delicada y fina piel. Como cuchillos en mantequilla, desgarran piel, pasando la capa de la dermis."
    "Intentas zafarte de su agarre, pero eso no hace más que rasgar más tu piel."
    "Duele."
    "Sin procesar tus opciones, cierras las manos con rabia para darle un puñetazo y así poder quitártelo de encima. Sabes que es en vano, por el tamaño colosal que posee, tu golpe no podrá conectar en ese punto débil de manera exitosa."
    "Sin embargo, no te vas a quedar como un bueno para nada y esperar a que te trituren el hueso del brazo. Pues, al paso que va su agarre, ese será el resultado si no haces nada."
    ell "Hueles a humano."
    "La voz de la entidad ha bajado al menos dos tonos, ya no te habla con asco... se ha interesado en ti repentinamente."
    "Su rostro se acerca más a ti, teniendo que encorvar la espalda unos grados para lograr estar lo suficientemente cerca de tu brazo. Clavando su atención donde sus garras te retienen, apretando con cada vez más fuerza."
    "Sangre brota de las heridas provocadas, siendo aquello lo que lo ha hecho pausar. Admirando, fascinado, como tu sangre tiñe la tela de la manga."
    "Está distraído, con la guardia baja. Tomando nota de ello, aprovechas esta oportunidad para darle con un gancho en su mandíbula."
    
    scene salon with vpunch

    "!!!"
    "..... no hay reacción."
    "Tu golpe no le ha hecho nada, ni siquiera le ha movido un pelo. Pero él si se ha dado cuenta de tus intenciones."
    ell "Pffff."
    "Ríe con gozo descontrolado mientras te levanta del brazo, con tal facilidad que parece que fueras un trapo. Quedas colgando, sin posibilidad de soltarte, tienes que apretar los dientes para aguantar el dolor, dejando salir un quejido quebrado."
    "La entidad levanta la cabeza al cielo, con la intención gritar frente a quien tiene a su alrededor. Tú, buscas a Septem entre la multitud, pero cuando miras alrededor, no hay nadie."
    
    scene salon with vpunch
    
    "Antes de que pueda soltar sus palabras, se congela, y cuando intentas comprender lo que ha pasado, tú ya estás cayendo al suelo." 
    "Te ha soltado."
    
    scene blanco 
    show septem_cuerpo1 
    with dissolve

    "Al mirar arriba, la túnica de Septem inunda tu campo de visión. Él está de espaldas a ti, cubriendo tu cuerpo y previniendo que veas lo que pasa con la otra entidad."
    hide septem_cuerpo1 with dissolve
    scene blanco with dissolve
    
    "Giras tu cabeza, temiendo que la escena por fin tenga la atención de los demás asistentes, ahora que Septem ha entrado en escena. Avergonzado de ser la causa de este altercado, buscas a tu alrededor para contar cuantas entidades te están mirando en este instante."
    "Nuevamente no hay nadie... eres solo tú, Septem y esa criatura."
    "Entonces, lo comprendes al instante: Septem ha sellado el perímetro... o tal vez los ha sellado a ustedes tres."
    "Están solos."
    "Una parte de ti, se siente agradecida. No solo te han salvado el pellejo, sino que también te han ahorrado la humillación pública. No tendrías como dar la cara ante el resto del jardín si esto hubiera sido presenciado por otra gente."
    "Sabes cómo funcionan los rumores, y este tipo de escenas, son leña perfecta para que las malas lenguas lo hablen a tus espaldas. Haciendo más obvio lo débil y patéticamente humano que eres comparado con los demás seres del Jardín"
    septem "No tienes permitido tocarlo."
    ell "Su santidad Septem---"
    septem "Silencio."

    play sound "huesoroto.mp3" volume 0.8

    $ powerhungry += 5
    
    "La discusión muere ahí."
    "Septem se da la vuelta, sus cejas fruncidas crean líneas de expresión en su frente. Sus ojos viajan rápidamente a la zona lastimada y truena la lengua con coraje. Su ceño se frunce aún más al ver el estado de tu brazo."
    

    scene act3_s7 with dissolve

    "Se agacha para tocar la herida por sobre la desmarañada tela. Está tan rota que puedes apreciar parte del daño en tu piel... hay al menos tres agujeros profundos con sangre que brota de ellos en un flujo constante."
    "Su mano sujeta algo extraño, lo acerca a tu herida sin explicación verbal. De consistencia blanda y color similar a la piel de la criatura que te ha herido, puedes suponer que es lo que Septem tiene en la mano."
    
    menu:
        "Correr tu cuerpo y evitar que eso te toque.":
            "Te alejas de Septem, tirando tu cuerpo hacía atrás, sin despegar la mirada de Septem y el trozo de carne que tiene en la mano."
            nj "¿Qué haces?"
            "Él te mira serio antes de levantar parte del cuerpo de la entidad, con la intención de mostrártelo. Como si eso te ayudara a calmar tus dudas y lograr que aceptes lo que planea hacer contigo."
            septem "Voy a curarte."
            "Al no tener respuesta tuya, Septem se explica."
        
        "¿Qué es eso?":
            septem "Parte del brazo de ese escriba."
            "Dice restándole importancia."
            pass

        "...¿Por qué has hecho eso?":
            septem "Te ha tocado."
            septem "Y lastimado."
            "Lo dice con el tono y actitud de quién explica lo obvio. Justificando su actuar sin pena ni gloria."
            "..."
    
    scene blanco with dissolve
    show pseptem_sonrisa with moveinleft
    
    play music "audio/ruidoblanco.mp3" fadeout 1.0 fadein 3.5 volume 0.7

    septem "Voy a usar parte del escriba para regenerar tu brazo."
    "Se te revuelve el estómago al pensar en lo que Septem le ha hecho a la criatura."
    "Septem asume que tu silencio es rechazo y ladea un poco la cabeza, formando una sonrisa sutil."
    hide pseptem_sonrisa 
    show pseptem_sonrisa2 

    "Ladea su cuerpo para permitir que puedas ver lo que hay detrás de él."
    septem "El escriba lo ha ofrecido como disculpas."
    "Su voz fuerza un tono que solo puedes describir como falsa amabilidad."
   
    hide pseptem_sonrisa2 
    show pseptem_serio at right
   
    septem "¿No es así?"

    show escriba at left with moveinleft

    "La criatura asiente levemente con la cabeza. Yace arrodillada y cabizbaja. Hay algo que no está bien con su cuerpo, pero no lograr identificarlo todavía. Prestando más atención a su figura en general, notas la ausencia de ambos brazos."
    "...no los tiene, ni sangra en esa zona. Su cuerpo ha sido reconstruido para eliminar las extremidades superiores de su figura humanoide."
    "Tragas saliva, pensando en lo literal que Septem se ha tomado el dicho 'ojo por ojo'..."
   
    hide pseptem_serio 
    show pseptem_sonrisa at right

    septem "Su lengua ha sido confiscada, por lo que no te puede pedir perdón de otra forma."
    "Dice con gracia, achinando los ojos en una sonrisa tierna e inocente, que genera un contraste repulsivo al comparar su expresión facial con sus palabras."

    hide pseptem_sonrisa
    show pseptem_sonrisa2 at right

    septem "Así que ha elegido un perdón retributivo."
    septem "Por favor acéptalo, o tendré que castigarlo por no disculparse por tan horrible acto que ha cometido contigo."

    hide pseptem_sonrisa2 
    show pseptem_sonrisa at right

    septem "A menos que quieras que lo castigue como es debido, mi Creador."
    "Él intenta reprimir el tono insistente, que pide a gritos que demandes el castigo. Sin embargo, no lo logra del todo, apenas puede controlarse."
    "Ya sea curiosidad por los años en que la violencia le fue prohibida, o por puro placer de causar daño, Septem quiere seguir y empujar esa sensación hasta el límite."
    
    menu:
        "Castígalo.": 
            $ powerhungry += 5
            $ septemconfianza += 1
    
            hide pseptem_sonrisa 
            show pseptem_blush at right
            
            "Su inocente sonrisa muta, reemplazándola por dientes y ojos afilados que se asoman y distorsionan esa cara angelical, manchando todo rastro de pureza que pueda tener."
            "Es una expresión de puro éxtasis, maravillado al tener tu complicidad."
            "Tu brazo ya se ha curado cuando Septem se acerca al escriba, lo toma por el cuello."

            hide pseptem_blush
            show pseptem_risa at right

            septem "Aún a sabiendas de que todo lo que tiene mi nombre y esencia, has osado dañarlo."
            septem "Siendo un escriba deberías ser más sabio."
            septem "No mereces tu puesto, claramente."
            
            hide pseptem_risa
            hide escriba
            scene blanco
            with dissolve

            "Hay una pausa, Septem levanta el cuerpo de la criatura sin dificultad, y este no pelea. Se ha sometido por completo a Septem, aceptando su castigo."
            "Pero sabes que debajo de esa máscara, hay una cara de terror que está por romper en llanto."
            "Sin más discurso, Septem atraviesa el pecho del escriba, sacando una esfera color carmesí del cuerpo del escriba. Gotea un líquido similar a la sangre en color, pero más espeso."
            "El cuerpo del escriba comienza a temblar y a perder la forma. Pequeñas hebras se despegan de la cabeza, buscando en movimientos erráticos la esencia que Septem tiene en la mano."
            "Poco a poco, su cuerpo se desarma en hebras más grandes, que pierden forma y textura con cada segundo que pasa."
            "Septem, suelta la masa de hebras con apatía, alejándose a paso lento, caminando en tu dirección."
            "Cuando él te tiene al frente, sus dedos se clavan en la esencia, activando algo que podrías describir como un destello tenue que provoca que entrecierres los ojos para poder apreciar bien que es lo que pasa."
            
            show brocheseptem with dissolve

            "Aquello que estaba en su mano se transforma en un broche, que en su interior lleva incrustado un cristal del mismo color carmesí de la esencia."
            "Septem lo lleva con cuidado a tu pecho, buscando el mejor lugar para colocarlo en tu ropa. Encuentra lugar perfecto en tu pecho, justo donde late tu corazón por debajo de las telas, huesos y carne."
            "No tarda mucho en engancharlo en la ropa. Al terminar, él da un paso atrás para ver como ha quedado, mientras tú bajas la cabeza para poder apreciar el nuevo accesorio en tu pecho."
            "Su color sobresale, teniendo un destello anormal que ninguna piedra preciosa podría tener en realidad... debe ser porque dentro de esto, hay parte de un individuo."
            $ broche = True
            
            hide brocheseptem with dissolve

            menu:
                "¿Ha muerto?":
                    "Septem suelta una risita."

                    show pseptem_blush with dissolve

                    septem "No."
                    septem "Solo he cambiado su propósito."
                
                "Gracias.":
                    "Septem baja la cabeza, haciendo una reverencia mientras una de sus manos toca donde se ubica su corazón."

                    show pseptem_sonrisa with dissolve
                    septem "Es un placer poder hacer valer tu palabra."
            
            "...te sientes extraño, algo en tu tripa se aprieta y no te deja tranquilo. Es una amalgama de sentimientos que no te permiten tomarlos uno por uno para poder identificarlos por separado."
            "Sabes que entre ellos está la culpa, pero no es tan grande como para lamentarte o enojarte con Septem por lo que ha pasado."
            "Después de todo, tú le has permitido seguir con esto cuando no era necesario."
            septem "Te ves bien con ello."
                    
        
        "Aceptar el perdón retributivo...":

            show pseptem_risa with dissolve

            septem "Oh." 
            hide pseptem_risa
            show pseptem_triste
            "Las comisuras de sus labios se levantan, intentando formar una sonrisa forzada. Al no lograrlo, las deja caer... se le ve ligeramente decepcionado."
            


            septem "Está bien."

            hide pseptem_triste
            scene blanco 
            with dissolve

            "No hay enojo, no hay más insistencia. Septem cae en silencio y de dedica a curar tu brazo con el trozo de carne que le pertenece al escriba."
            "Tú prestas atención a cómo lo hace. La carne actúa como una especie de adherente, que busca contacto por sí solo con tu piel. Unas pequeñas hebras, se mueven en dirección a tus heridas."
            "No puedes mentir, es asqueroso, tanto que te obligas a aguantar la reacción natural de tu cuerpo al sentir asco. Con ojos llorosos, muerdes la lengua para evitar dejar escapar arcadas."
            "Poco a poco, tu piel acepta cada hebra que toca, absorbiendo y adhiriendo capa tras capa para regenerar el tejido desgarrado."
            "Septem termina con una delicada palmada en la zona, comprobando el resultado de la curación. Sonríe al percibir que tu brazo se encuentra en perfectas condiciones, sin marcas o cicatrices delatantes de la antigua herida."
            pass
        
        "Parar a Septem.":
            $ powerhungry -= 10

            hide pseptem_sonrisa
            hide escriba
            scene blanco
            with dissolve

            "Paras a Septem en seco con un solo no. Le pides que no te toque con esa cosa que tiene en la mano y le recriminas lo que acaba de hacer."
            "No sabes de dónde y cómo tienes la lengua para sacar tus palabras sin titubear, pero lo logras. Le expones su actuar con la esperanza de hacerlo entrar en razón."
            "Tu cerebro bloquea la posibilidad de terminar siendo tú la su próxima víctima, así que miedo no sientes por ahora. Debe ser la adrenalina."
            "Septem guarda silencio. Sabes que te está escuchando porque sus expresiones cambian, pasando de enojo a la tristeza genuina de manera progresiva."
            "Sabes que lo has hecho entrar en razón cuando se disculpa y gira su cuerpo para caminar hacía el escriba."
            "Si bien, Septem no pide perdón a la entidad, hace tronar sus dedos para devolverle los brazos y lengua a la criatura."
            "Esta al instante comienza a pedir perdón a Septem y a ti, y a pedir algún tipo de castigo que tu decides ignorar completamente."
            "Al no aguantar el insistente parloteo del escriba, Septem truena una vez más los dedos y este desaparece."
            "No alcanzas a preguntas cuando el te responde, sin ánimos."
            
            show pseptem_serio with dissolve

            septem "Le he quitado el sello."
            septem "Ha vuelto con los demás invitados."
            "Se produce un silencio incómodo, del cual no sabes cómo llenar."
            hide pseptem_serio
            show pseptem_triste

            septem "[nombrejugador]..."
            "Es Septem quien da el primer paso, buscando tu mirada. Sus cejas curvadas denotan arrepentimiento."
            septem "¿Me he equivocado? ¿el castigo no era necesario?"
            "Tiempo te falta para poder responderle. Septem no deja que lo hagas pues pregunta nuevamente, sin lograr entender tu razonamiento aún."
            septem "Si no corregimos esto ahora, el resto intentará lo mismo contigo."
            septem "Eres vulnerable."
            septem "Debo cuidarte."
            menu:
                "Puedes cuidarme de otra forma.":
                    "Le explicar que actuar con tanta violencia no sería propio de un líder. Septem bufa, harto de tus sermones." 
                    "Agregas qué él mismo le ha pedido a Sextam hace unos días que lo detuviera si dañaba a alguien, y eso es lo que por fin lo hace reaccionar."
                    "Te devuelve la mirada con los ojos abiertos de par en par. Hay un brillo singular en sus ojos, uno que es fácil pasar desapercibido, pero que está ahí."
                    "Luego de ello, hay solo quietud. Un tiempo muerto en donde Septem se queda solo con sus pensamientos, ordenando sus ideas y cambiando ciertas convicciones."
                    septem "..."
                    
                    hide pseptem_triste
                    show pseptem_sonrisa

                    septem "Tienes razón."
                    $ septemconfianza += 1
                    septem "Gracias por parar mis acciones."

                "Me puedo cuidar yo solo.":
                    $ septemconfianza += 1
                    septem "..."
                    septem "No puedes hacerlo, mi Creador."
                    septem "Ya te lo dije, tu poder aún no se a liberado por completo." 
                    septem"Eres vulnerable..."
                    "Septem pausa por unos segundos, meditando sus próximas palabras."
                    septem "Buscaré otra forma de cuidarte."
                    septem "Sin violencia..."
                    "Se le oye arrepentido, hasta podrías decir que hay algo de vergüenza metida por ahí en sus palabras."
            pass
    hide pseptem_sonrisa
    hide pseptem_triste
    scene blanco 
    with dissolve
    
    "Septem se toma un tiempo prudente antes de romper el sello, todo con tal de volver más tranquilo y compuesto. Tú lo agradeces, porque sabes que también necesitas un momento de quietud."
    "En el silencio, juegas con los bordes de las mangas para organizar tus ideas. Deseas preguntar más, pero no te salen las palabras de la boca, ni sabes qué preguntar con exactitud."
    "Luego de un tiempo, ambos están listos para volver."
    
    show invitados with dissolve
    
    play music "audio/woo_scary.WAV" fadeout 1.0 fadein 3.0 volume 0.6

    "Tu alrededor no se perturba, ni cambia en lo más mínimo; más bien los invitados se materializan al momento en que las palmas de Septem chocan entre sí." 
    "El sonido de murmullos incomprensibles y risas estridentes invade tus oídos, distrayéndote por un instante de Septem."
    "Él viendo aquello, toma tu mano, evitando que puedas perderte o quedarte atrás. Así es como se abren paso ante la multitud."
    septem "Ya estamos listos."
    septem "No me sueltes."
    "Te informa, mientras sigues el ritmo de sus pies. Él es quien te conduce y tú te dejas llevar, sin conocimiento del lugar al cual estás siendo arrastrado."
    "Te mareas de golpe, la coordinación entre piernas y cuerpo comienza a diluirse. Te es complejo sincronizar tus movimientos para estar a la par de Septem."
    "Sientes las náuseas asomarse por la boca de tu estómago, pero te cuesta encontrar el por qué te sientes así. Hasta que lo ves..."
    
    scene ceremonia1 with pixellate

    "El espacio lentamente se convierte en un espacio que no puedes explicar con palabras. Flotas y caes a la par, con el cuerpo pesado y ligero a la vez."
    "Es extraño..." 
    "Entre paso y paso sientes que pierdes la conexión con la realidad. Es como si te hundieras en el espacio, debiendo saltar de estrella en estrella para no perder el rumbo. Al hacer contacto con ellas, explotan formando nebulosas."
    "Colores que jamás has tenido el atrevimiento de imaginar, decoran la escena, cambiando con cada movimiento y contacto de tus pies con la superficie."
    "Parece un sueño. Uno que te atrapa con cada parpadeo y demanda que cierres los ojos permanentemente."
    "Lo único que no te lo permite es Septem. Sus ojos te buscan cada que siente que estás por perder el conocimiento. Esos ojos verdosos son lo que te mantiene consciente, atrapan la mirada y te devuelven al presente."
    
    scene negro with dissolve
    pause 0.5
    scene ceremonia2 with dissolve

    play music "audio/meeting.mp3" fadeout 1.2 fadein 2.0 volume 0.3

    "Un parpadeo más y tu destino aparece frente a ti. Es una especie de podio conformado con columnas que lo elevan del oscuro espacio en el que permaneces."
    scene negro with dissolve
    pause 0.5
    scene ceremonia3 with dissolve

    "Otro parpadeo y ahora estás siendo exhibido en el. Hay un centenar de ojos puestos en ti, que miran, devorando tu pequeña silueta."
    septem "[nombrejugador]..."

    scene ceremonia4 with dissolve
    
    "Septem sigue a tu lado, su voz te lo confirma, aunque... ha perdido su figura humana." 
    "No te asustas por lo chocante de su nueva apariencia, incluso, te sientes más protegido así. Con tantos ojos sobre ti, Septem parece estar más capacitado con esa forma para resguardar tu seguridad ante cualquier inconveniente."
    "Sabes que tienes que mirar al frente, más no puedes despegar tu mirada del dios que tiene por nombre Septem."
    "Septem habla sin apuro. Es un discurso que tu no prestas atención. Apenas puedes mantenerte consciente, no hay cómo puedas captar todo el discurso que expulsa su lengua."
    "Con todas tus fuerzas te concentras para entender lo que habla. Y lo que llega a tus oídos te hace enrojecer del pudor."
    "Él se declara tu vasallo. Lo dice sin reparo o vergüenza por rebajar su rango ante miles de ojos hambrientos de más palabras."
    "Lo miras con intensidad, olvidando como comprender sus palabras nuevamente. Hay algo hipnotizante en su figura, que no puedes explicar."
    "Él es hermoso, belleza verdadera que no puede compararse a los estándares mundanos, ligados a la carne. Su halo abraza su figura, robando las miradas con lo deslumbrante de su composición similar al oro. Sus siete ojos están acompañados por alas que dan la ilusión de ser pestañas, sin llegar a serlo realmente."
    "Quieres tocarlo, sentir su forma, extender tus brazos y hundirte en él. Pero te aguantas."
    "Tienes que quedarte quieto y sonreír. Estar presentable ante los demás, como un plato de exposición al que nadie puede tocar. Solo admirar."
    
    scene ceremonia3 with pixellate

    "Y lo logras. Ya sea por las palabras de Septem o por lo atractivo de tu naturaleza semihumana, las entidades festejan recitando cánticos angelicales."
    "Septem los calla sin hablar. No sabes cómo lo ha hecho, pero con un solo movimiento de su cuerpo, el público ha vuelto al silencio."
    
    septem "Vienen tiempos de cambios."
    septem "Hoy, ante todo el Jardín, romperé un sello impuesto por siglos."
    septem "El dominio del Seis será liberado."
    septem "Y la maldición que les prohíbe albergar humanos--- queda abolida."
    "Hay movimiento en el podio. Otra entidad da un paso al frente, asumes que es Sextam. No puedes identificarla, ya que, al igual que Septem, su forma ha dejado de ser humanoide."
    
    scene ceremonia5 with pixellate

    "Sin embargo, su figura no es sólida. Es una llama que titila débil ante todos los presentes. A su centro se ve una esfera sellada por ramas de una sustancia viscosa que la cubren como si de una jaula se tratase."
    "Eso debe ser el sello."
    "La voz de Septem vuelve a monopolizar todo el lugar, declamando cánticos que para un humano serían imposibles de reproducir. Tu cuerpo comienza a vibrar por los tonos y vibraciones del cántico; es una frecuencia que te toma y viaja por cada célula de tu organismo."
    "No duele. No es placentero. Simplemente está ahí."
    "Los cánticos ceden cuando lo que recubre la esfera se derrite, esfumándose cuando toca el suelo." 
    
    scene ceremonia6 with dissolve
    
    "Sin esa atadura, la llama que protege la esfera crece cuatro veces su tamaño."
    "Resultando en una llama que va danzando con el viento, tomando formas y caras humanas dentro de su ser."
    "Es grotesco y fascinante a la vez. No puedes dejar de mirarla."
    "Sextam ha obtenido nuevamente su poder."
    
    scene ceremonia3 with dissolve

    "Septem deja que su público deje de festejar para terminar con su discurso."
    septem "Con esto, nos declaramos un imperio independiente de todo lo que Padre representa."
    septem "Tendremos siete días para reconstruir este lugar, eliminando cada elemento ligado a Él."
    septem "Nunca más tendremos que aguantar el abandono y la miseria por manos irresponsables que no nos ven como a un todo."
    septem "A partir de hoy, nos moveremos hacia el cambio."
    septem "Hoy aceptamos el primer paso para traspasar nuestro mundo a un Creador presente."
    septem "Desde hoy responderán a [nombrejugador] como amo y señor de este lugar."
    septem "Y yo, su único vasallo, representante de su palabra."
    "Quieres sonreír, decir algunas palabras tal vez, pero tu cuerpo no da más."
    
    scene negro with pixellate
    
    "Pierdes el conocimiento en el lugar."
    
    stop music fadeout 2.0

    "..."
    "___________"

    scene blanco with dissolve
    
    play music "audio/fell.mp3 " fadein 2.0 volume 0.4

    "Tu consciencia se ve atrapada con el subconsciente de Septem de nuevo."
    "Esperas las mismas sensaciones de siempre... desesperación al no poder conseguir lo que buscas; Cansancio; o incluso, miedo... "
    "Hoy no es uno de esos días."
    "Hoy te sientes ligero, libre y contento."
    "Hay calidez a tu alrededor, acariciando tu cuerpo e invitándolo a echarse en un lecho de telas suaves, para descansar."
    "Por fin puedes hacerlo. Por fin puedes dejar escapar ese suspiro que guarda todo el trabajo y esfuerzo que has puesto en esta misión."
    "Estás feliz con todo lo que tienes hasta ahora. Con cada pequeño cambio que ha ocurrido hasta la fecha."
    "Pero cuando miras tu reflejo en el cielo, algo no cuadra."
    "Ya hace un tiempo que te has sentido así."
    "Y crees que es momento de cambiar."
    "Septem quiere cambiar."
    "..."
    "Cuando lo veas, hablarás con él. Conversarás de su identidad y cómo su apariencia también es algo que debería sentir propio. No algo ajeno o separado de él."
    "Esperas una larga conversación, y alguna que otra negativa por su parte."
    "Pero por ahora te dedicas a descansar."
    "..."
    septem "[nombrejugador]."
    
    scene camaseptem with dissolve

    "Tus ojos se abren, liberándote de la conexión entre el mundo interior de Septem y tú. Quieres volver ahí, seguir descansando junto a esa sensación de triunfo, regocijado con todo lo que te rodea."
    "Aquí, todo lo que sientes es pesadez. Tu cuerpo es pesado; tus párpados, caen por el cansancio; hasta respirar sale con pesadez."
    
    scene negro with dissolve

    "Dejas caer tus párpados con la esperanza de volver a ese lugar onírico, decidiendo ignorar a Septem."
    

    septem "Mi salvador."
    "Dice con más insistencia, endureciendo su voz."
    "Balbuceas en respuesta, ni tú sabes muy bien lo que le estás pidiendo. Aun así, Septem no se deja doblegar y coloca su mano en tu hombro. No te mueve ni da palmadas, solo está ahí, reposando su peso en tu cuerpo."
       
    septem "Les he dado a todo el Jardín un día para organizar los preparativos. Para que mañana comencemos con la inspección de cada dominio."
    septem "Te dejaré dormir todo el día si quieres, pero antes necesito conversar contigo acerca de Madre."
    
    scene camaseptem with dissolve

    "Aquello es más que suficiente para despertarte por completo. Pestañeas un par de veces para acostumbrar tu vista a la iluminación cegadora de la habitación."
    "Te estiras mientras buscas a Septem."
    
    
    scene camaseptem with vpunch

    "!!!"
    "¡¿HUH?!"
    "¿Ese es...?"
    
    scene act3_s8 with dissolve
    
    "Sin creerlo, posas tus ojos en la figura que tienes al frente, sentada a los pies de la cama. Él te devuelve la mirada con normalidad."
    "Sin hacer un escándalo o una escena por este cambio de forma."
    "La figura que tienes al frente te observa como Septem siempre lo hace. Su olor sigue siendo el mismo, al igual que su aura."
    "La figura que tiene al frente te sonríe como lo Septem siempre lo hace, sin mostrar los dientes y entrecerrando levemente los ojos."
    "Es Septem. Aunque con un exterior distinto."
    "No es que ha cambiado mucho, sigue en posesión de ese aire tan suyo. Mismo gusto en estilo también. Cabello similar, ojos tiernos y semblante que no se permite estar relajado por mucho tiempo."
    "Ha cambiado."
    "Se ve distinto... y a la vez no."
    "Ha dejado de lado la cara e identidad de Rafael, aunque su nuevo rostro bebe de la matriz que fue su antigua identidad."
    "No lo ha descartado por completo, sigue reconociendo rasgos que los toma como suyos. Solo que esta vez se ha aventurado a alejarse un poquito más."
    "Lo contemplas por unos segundos antes de reaccionar."

    menu:
        "Saludar y decir buenos días":
            $ septemconfianza += 1
            "Le saludas con un 'buenos días', despacito para no forzar tu voz, a sabiendas de que en la mañana esta tiende a ser ronca y dura."
            "Septem al escuchar tu saludo, su rostro te devuelve el gesto. Comisuras del labio suben y aparecen líneas de expresión en sus ojos que indican una sonrisa genuina."
            septem "Buenos días."
            septem "Espero que hayas descansado lo que necesitas."
            pass

        "Señalar su cambio físico.":
            $ septemconfianza += 1
            "Acercas tu mano a su rostro y esperas. Preguntando con tu silencio si él te da el permiso de poder tocarlo."
            "Él te mira con sorpresa, la cual borra al instante después de comprobar que no estás invadiendo su espacio personal sin consultar antes."
            nj "Tu rostro..."

            if powerhungry >=10:

                septem "Necesito una nueva imagen."
                "Tú no respondes al instante, prefieres calla y medir tus palabras primero."
                "Ante tu silencio, Septem agrega, explicando su decisión."
                septem "El rostro de Rafael no me pertenece."
                septem "Y el Jardín lo asocia a un cuerpo humano."
                septem "Eso no me sirve."

            else:
                septem "Quiero una identidad propia."
                "Tú no respondes al instante, prefieres calla y medir tus palabras primero."
                "Ante tu silencio, Septem agrega, explicando su decisión."
                septem "Espero que no te perturbe mucho esta nueva apariencia."
                septem "Sé que ustedes prefieren lo familiar, así que no me alejé tanto de su rostro..."
                "Está hablando de Rafael."
            pass

        "Reaccionar con disgusto.":
            $ septemconfianza -= 6
            "No te gusta."
            "Y se lo haces saber, con su cara."
            "Si a Septem le ha dolido tu reacción, él no lo hace notar. Su expresión no cambia en lo más mínimo, aunque dentro de tu ser, reconoces ese hormigueo que fluctúa entre la rabia y vergüenza."
            septem "Veo que no te ha gustado..."
            septem "Pero a mí sí."

            scene act3_s8 

            "Él calla, esperando a que tú digas o hagas algo."
            menu:
                "Pedir perdón.":
                    $ septemconfianza += 2
                    septem "Jamás creí que reaccionarías así..."
                    septem "Pensé que eras más..."
                    "Detiene sus palabras, emitiendo un chasquido con su lengua, incómodo."
                    septem "Olvídalo."
                
                "No decir nada.":
                    "..."

            septem "No voy a cambiar."
            septem "Aunque me lo pidas o no te guste."
            septem "Eso es lo único que no voy a darte el gusto."
            septem "Mi identidad no es de tu incumbencia."

            pass

    "Septem gira su cuerpo una vez ha terminado de abrochar su capa."
    scene blanco
    show act3_s9_1 
    with dissolve
    "Poco a poco tu alrededor se transforma. El blanco va tragando todo el espacio a su paso, dejando solo la cama para no perturbar tu descanso."
    "No hay nada en lo cual enfocarse, solo Septem quien se roba la escena con su presencia."
    
    septem "Sé que aún nos queda un largo camino, pero---"
    septem "Quiero agradecerte, por todo lo que has hecho por mí."
    septem "No tengo nada tangible para darte. Nada que puedas tocar con tus propias manos."
    septem "Pero si puedo darte el gusto de pedirme lo que quieras."
    

    jump interactuar6

label acto3_septem_continuacion3:
    scene blanco 
    show  act3_s9_1
    septem "Bien."
    septem "No podemos quedarnos aquí para siempre."
    septem "Cuando terminemos con la restauración del Jardín podremos tener más momentos de calma."
    septem "En unos siete días más..."
    septem "Ahora, tendrás que ejercer tu responsabilidad de nuevo creador."
    septem "Y en el séptimo día, cuando todo esté listo."
    septem "Te daré todo."
    septem "Y quitaré todo rastro de Padre para ser reemplazado por ti, [nombrejugador]."
    septem "Haré que te sientas orgulloso de tener un vasallo como yo."
    "___________"
    scene negro with dissolve
    stop music fadeout 3.0
    centered "FIN DEL ACTO 3"
    centered "En proceso de elaboración..."
    centered "{sc=2} Tendrás que esperar un poco para descubrir como acaba esto... :3{/sc}"
    "..."
    $ MainMenu(confirm=False)()
    #POner el menú de interacción.
 

return
#Hacer una persistent. que indique que has desbloqueado la atadura del alma de Septem con la tuya. una que no cambie si Nulla la borra en su proria ruta.
#Esto con el fin de hacer que ambos intenten pelear por tu control en cada ruta correspondiente.

#INICIO DEL ACTO 3
#Despiertas sintiendo tu cuerpo pesado. Septem entra a tu cuarto y te invita a sentarte en la mesa con el para comer el desayuno. LISTO
#Aquí tienes la oportunidad de preguntar por Rafael y por Madre.
#Si preguntas por rafael, septem dice que eso lo verá despues de arreglar el Jardín. Que primero tienen que hacer un montón de cosas antes de centrar su tiempo en ello.
#Si preguntas por Madre, Septem te pide que expliques lo que sucede. Tu explicas con más detalles lo que Madre te pidió en el sueño.
#Septem escucha, y te dice que necesita pensar, para ver que hacer. Ya que los ojos tambien le sirven a él para saber todo lo que pasa con los symbolos (donde están, en que condición y que están haciendo.)
#Despues de comer puedes explorar la casa antes de partir a hacer lo que tienes que hacer. 
#En la exploración, sientes que algo te llama a la habitación del vacío. Al entrar, tu cuerpo emite luz propia, iluminando la habitación lo sificiente como para captar una pequeña cosa en la esquina.
#Es lo que queda de la marioneta, un ojito que mira con miedo y te llama.
#Te ruega para que lo tomes y te unas con él. Si lo tomas, sale Nulla del ojo y te lleva a su ruta o activa un final malo (nulla aprovecha tu nuevo poder que te conecta con Septem y consume todo.)
#Si ignoras el ojo o si te demoras al entablar conversación con él, llega Septem. Y lo elimina. Dejándote sin la posibilidad de encontrar a Nulla nuevamente, ya que septem clausura la habitación.




#Cuando salen, septem te lleva a donde todos los dominios se encuentran, un punto medio.
#Da su discurso, habla de Padre y como el Jardín se volverá independiente de él.
#Hay algunos murmullos, y Septem se enoja. diciendo que quien no esté a favor, será catalogado como no util para el jardín.
#Es el turno de que Sextam salga a delante y Septem rompe el sello al frente de todos (?)
#Septem comanda a todo el jardín a prepararse para recibir humanos. Tiene 6 días para preparar cada dominio.
#Septem hará un chequeo a cada dominio dependiendo del día: lunes (unum), martes (duae), ect.
#En cada chequeo pasan cosas malas y aquí puedes intervenir para que a Septem no le suba el hambre de poder... o tal vez no...
#Al 6 día, Sextam da a luz a los humanos nodriza. y el Jardín comienza a florecer.

#Ver donde poner el encierro de Nulla en el vacío. VER COMO SEPTEM HACE ESO. JUGADOR COMO CARNADA?! O AYUDA DE MADRE....
#El acto termina con Septem en su trono, hablando de lo importante que eres para él. que gracias a ti él ha podido florecer como un gobernador digno.
#Pero que aún tienen cosas por hacer.

#Lo que falta: El despertar de Rafael, la roptura de los ojos, el encierro de Nulla... el cambio de apariencia de Septem y el final donde Septem comprende que tus ojos tambien son los de Musae.
#Por ende tienen que cortar la conexión para dar final a esta historia.
#Insertar discurso de amor de Septem hacia ti.




#Septem rompiendo el sello de Sextam ante el consejo y los estandartes, y te pide que te alistes pues mañana harán una presentación oficial de ti.
#Tu primer día como soberano del Jardín.
#El discurso de Septem cambia de acuerdo al nivel de powerhungry que tiene. (Poner otra escena donde pueda crecer o disminuir ese aumento.)
#Tal vez antes del discurso.
#contigo yendo al cuarto oscuro (en el caso de que hayas elegido buscar la ayuda de Nulla. Aunque igual se te da la opción de no ir.)
#Si no pasa esto, Septem va a tu cuarto y duerme contigo.
