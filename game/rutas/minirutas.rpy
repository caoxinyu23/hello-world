default persistent.rogar = False
default persistent.juegocompleto = False


label rutaneo:
    
    play music "audio/void3.mp3" fadein 3.0 volume 0.5

    scene blanco
    show vacio3
    pause 0.10
    hide vacio3
    show vacio2
    pause 0.10
    hide vacio2
    show vacio
    pause 0.10
    hide vacio
    show blanco
    scene blanco
    neo "..."
    show neo1serio with dissolve
    neo "Por la chucha, no hay nada aquí."
    "Neo inspecciona el lugar, blanco, vacío. Y tú haces lo mismo, encontrando lo mismo que él; nada."
    "Poco importa a dónde poses tu mirada; todo el espacio está cubierto por un blanco antinatural, del cual nada parece perturbarlo. Ni siquiera las supuestas sombras que Neo o tú deberían generar."
    "No hay nada, solo ustedes en un espacio muerto, que ni sombras puede proyectar."
    neo "Este bueno para nada---"
    "Escuchas cómo Neo comienza a rabiar solo, balbucea barbaridades que agradeces que no estén dirigidas a ti. En la rabieta, se toca la cabeza pasando repetidamente sus manos entre sus cabellos, despeinándose en el proceso." 
    hide neo1serio with dissolve
    scene blanco with dissolve
    "Mientras él está distraído con maldecir al mundo, tú aprovechas para analizar el estado de tu cuerpo."
    "Lo sientes... sigues teniéndolo, pero es extraño."
    scene act3_neo0
    pause 1.5
    "La confirmación de que algo no está bien contigo llega cuando levantas tu brazo y miras las grietas que hay en él. Tu piel está rota, justo como lo estaría un ornamento de porcelana."
    "Grietas que se diversifican por toda su extensión. Algunas de ellas presentan hoyos, y estos te permiten ver lo que tu cuerpo esconde dentro."
    "Es la misma sustancia que se ha tragado a Nulla, y que ha dejado nacer a Neo."
    scene blanco with vpunch
    "Un golpe llama tu atención. Es seco y ha generado un eco antinatural."
    "Vuelves tu atención hacia tu acompañante (aunque secuestrador sería un mejor término). Y en su expresión hay algo de sorpresa, pero es borrada al instante cuando Neo golpea el piso con su pie. Provocando el mismo sonido de antes."
    "Con ello su cara muestra una mueca de súbita realización. La sonrisa ladeada que esboza, desborda una confianza que ya quisieras tener tú en este momento."
    "Neo no te deja preguntar y mirándote de reojo, él golpea nuevamente el suelo con su pie, está vez más fuerte."
    show neo1risa with dissolve
    neo "¿Escuchas eso?"
    neo "... Pfff, qué mierda estoy preguntando, claro que {b}tú{b} no lo escuchas. \n\n{size=*0.5}No hay sonidos agregados en esta porquería. Solo las mismas canciones que se repiten en un loop.{/size}"
    neo "Ja ja."
    hide neo1risa with dissolve
    scene act3_neo1 with dissolve
    pause 1.0
    "Neo se agacha y levanta su mano derecha, abriendo la palma completa."
    neo "Estamos en la misma memoria aún."
    neo "Para pasar a otra, solo tenemos que romper esta capa."
    scene act3_neo1a with vpunch
    "Sin más, golpea el suelo con la mano que previamente estaba en el aire y desgarra su superficie, que se rompe como lo haría un papel. Neo Rasga lo blanco para dejar pasar luces que se reflejan desde el otro lado."
    "Te cuesta comprender lo que está pasando, e inconscientemente te acercas al agujero creado a la fuerza por la manos de Neo. Echas un vistazo, procurando no invadir el espacio del hombre que aun está de cuclillas mirando a lo que se encuentra del otro lado."
    "Su cuerpo te impide ver bien lo que hay dentro."
    menu:
        "Acercarte más.":
            scene act3_neo1b with dissolve
            neo "..."
            show act3_neo1
            neo "Tienes agallas."
            
            pass
        
        "Decirle a Neo que se corra.":
            neo "_____"
            scene act3_neo1b with dissolve
            "Él te devuelve la mirada, entrecerrando los ojos, serio por un instante. No es hasta que ves como su boca se curva hacia arriba, mostrando una sonrisa amplia que enseña más diente que labios."
            neo "¿Y el por favor no te lo enseñaron?"
            neo "¿Tú crees que te voy a hacer caso? \n¿A ti?: ¿una persona que prefiere estar sentada aquí intentando obtener cariño de personajes que se encuentran en una pantalla? ¿Con la {b}edad{b} que tienes?"
            "Neo suelta una risa genuina luego de lanzar ese ácido comentario, realmente le ha hecho gracia su propio comentario."
            show act3_neo1c
            neo "Por favoorrrr."
            neo "No me voy a correr. Pero tú si lo harás."
        
        "Quedarte donde estás.":
            
            scene act3_neo1b with dissolve
            neo "_____"
            "Neo te mira por un momento."
            pass

    scene blanco with vpunch     
    "Neo te toma desprevenido cuando agarra tu muñeca y te jala a su lado, obligando a tu cuerpo a arrodillarse para estar al nivel de la abertura que está en el suelo."
    scene hoyo with dissolve

    "Ahora que estás frente a frente con la gran grieta que refleja el otro lado, eres capaz de observar lo que hay dentro. Agua con ocasionales ondas te saluda del otro lado, el reflejo de las luces hace un efecto de resplandor que tintinea cada cierto tiempo, como si del otro lado hubiera movimiento."
    "Mientras más miras, más te das cuenta de que hay algo detrás del agua, lo que te hace recordar a un acuario, siendo tú el pez."
    scene act3_neo1c with dissolve
    neo "Bueno"
    "Dice Neo contento con la situación y su descubrimiento que oh, tan amablemente ha tenido el corazón de compartir contigo. Te mira por un par de segundos, con esa fastidiosa sonrisa que parece no quitarse nunca." 
    neo "Los perdedores primero."
    "La mano que aún sujeta tu muñeca tira nuevamente de ella, ahora con el propósito de hacerte caer por el agujero. Solo alcanzas a respirar hondo para agarrar el último aliento antes de sumergirte en el agua fría que te recibe con los brazos abiertos, sin mucha resistencia."
    scene negro with dissolve
    "Abres los ojos, pero no hay nada que ver y eso te desespera un poco. Esto es muy diferente a cuando entrabas al vacío con Nulla, pues ahí te sentías acompañado y seguro... aquí no." 
    "Tienes la sensación de estar hundiéndote bajo el agua, aunque falta el hecho de estar mojándose, cosa que ni tu cabello ni ropa lo está."
    "Con cada segundo que pasa, sientes una presión en tu pecho que crece y crece cada vez más. La presión te está aplastando vivo."
    "Cuando estás apunto de perder el conocimiento por la presión, una mano te agarra por el collar de tu camisa."
    "Tiempo para un respiro y recolección de lo que pasó no tienes, Neo no te deja. Y lo que te trae a tierra son palmadas que golpean tu mejilla izquierda, no son tan duras como para doler pero si provoca que la zona se entumezca."
    show neo2risa with dissolve
    neo "Vamos no es para tanto. No pensé que fueras tan delicado~"
    "Te da unas palmadas más lentas cuando ve que ya estás alerta y en sintonía con tu propio cuerpo. Para luego cesar el movimiento y mantener el contacto por un momento antes de terminar con una palmada más."
    hide neo2risa
    show neo3risa
    neo "Pfff aun así de rota, tu piel se enrojece."
    hide neo3risa
    show neo1risa
    "Sus ojos permanecen en ti unos segundos antes de mirar a su alrededor..."
    
    play music "audio/club.mp3" fadeout 1.0 fadein 1.0
    hide neo1risa with dissolve
    scene bar with pixellate
    
    "Mientras posas tus ojos en el nuevo paisaje, tu mano se escurre a tu mejilla para sobarla y aliviar el dolor punzante que está comenzando a emerger."
    "Hay música que te inunda los oídos y sombras que parecen tener masa, justo como las que estaban en la feria...¿Estás en un club ahora?"
    show neo2risa with dissolve
    
    "Miras a Neo con algo de incredulidad, ¿Por qué diablos los ha llevado a un club nocturno?"
    menu:
        "¿Qué hacemos aquí?":
            hide neo2risa
            show neo1serio with dissolve
            neo "Qué se yo---"
            neo "Deben ser weas del usurpador --memorias digo--."
            "Él mira a su alrededor, ignorando tu presencia por unos segundos."
            hide neo1serio
            show neo1risa
            neo "Al menos la música es buena, supongo."

        "¿En serio? ¿Me vas a invitar a un club nocturno?":
            hide neo2risa
            show neo1risa with dissolve
            neo "Es nuestra primera cita---"
            neo "Hay alcohol y buena música. ¿Qué más quieres pedir? \n     {size=*0.4}Que no puedes escuchar por temas del copyright, ja jajaaaa---{/size}"
    
    hide neo1risa
    show neo3incomodo
    "Él se hace el desinteresado, colocando sus manos en los bolsillos de su pantalón y encogiéndose de hombros."
    hide neo3incomodo
    show neo1serio
    neo "..."
    hide neo1serio
    show neo3incomodo
    neo "......"
    hide neo3incomodo
    show neo1serio
    neo "Hablando en serio---"
    neo "No te creas que estamos aquí porque me quiero divertir contigo. Supongo que esta debe ser una de las memorias de las previas versiones del {i}sacowea{i} del Nulla."
    hide neo1serio
    show neo3incomodo
    neo "Mmmm."
    "Neo golpea el piso dando un pisotón, el resultado que él percibe hace que forme una mueca, disconforme." 
    hide neo3incomodo with dissolve

    "Sin muchas ganas, intenta el mismo procedimiento de la vez pasada: se agacha, posa la mano en el aire para tomar distancia y golpea el piso con la intención de romperlo y desgarrarlo."
    "...Pero no pasa nada."
    show neo3risa with vpunch
    neo "Mierda----"
    "Se levanta y esboza una sonrisa forzada, que no puede mantener en el tiempo y es borrada al abrir la boca otra vez."
    hide neo3risa
    show neo2enojo
    neo "¿Vamos a tener que hacer este juego de mierda capa por capa?"
    neo "¡MIERDA!"
    menu: 
        "¿A qué te refieres?":
            pass
    
    hide neo2enojo
    show neo1serio

    "Su atención se enfoca en ti. Su mirada te hace sentir como si fueras un insecto que ha volado por cerca de su oído, y te debates entre pensar si su próximo movimiento será aplastarte como a uno o si gritarte."
    neo "Vamos a tener que perder el tiempo jugando a la búsqueda del tesoro."
    hide neo1serio
    show neo3incomodo
    "Neo se frota la cara con frustración genuina mientras suspira pesadamente."
    neo "Necesito un trago. Ven."
    hide neo3incomodo with dissolve

    "Ese 'ven' es una orden que tu cuerpo acata sin chistar. Tus piernas se mueven por ti, siguiendo a Neo a la barra. Y aunque intentes parar o cambiar la dirección, no hay caso."
    "Tus piernas no responden. Casi como si no fueran tuyas."
    "No tienes que ser un genio para comprender que Neo tiene control completo de tu cuerpo."
    
    scene barneo2 with dissolve

    "Él se sienta en una de las tantas butacas vacías que dispone la barra de bar, y tú haces lo mismo. Verte haciendo lo que él quiere parece sacarle una sonrisa pícara que tapa con su mano."
    
    show barneo

    neo "¿Bebes?"
    menu:
        "No...":
            neo "Ja! me lo imaginaba."
            
            hide barneo
            show barneo2

            "Neo hace aparecer un vaso con lo que supones contiene algún tipo de bebida alcohólica. Y se lo lleva a los labios."
            pass
        

        "Sí.":
            neo "Ja."
            "Neo te pasa un vaso con lo que supones es alguna bebida alcohólica. Y espera a que le des un trago."
            "Cuando lo haces, él masculla una risa."
            hide barneo
            show barneo2
            neo "No tiene gracia alguna ver a esta cosa beber."
            neo "Si tienes algo para beber, pues adelante y tómalo."
            "Y con sarcasmo sentencia:"
            neo "Estar tanto tiempo pegado a la computadora debe ser agotador."
            pass
    
    "El tiempo pasa entre sorbo y sorbo, hay un silencio pesado entre ustedes dos, del cual Neo no parece estar preocupado en lo absoluto. Él solo se dedica a beber e inspeccionar su alrededor, buscando algo."
    "No hay caso con tratar de tener una conversación entre él y tú, Neo ya te ha hecho saber que no está interesado ahora. Te ha pedido 'muy amablemente' que lo dejes concentrarse."
    "Así que no te queda otra cosa que mirar el lugar y escuchar la música, ya que pararte e ir a otro lugar no es opción para ti."
    "La música es fuerte y repetitiva... una sola canción es reproducida en bucle, y ya te tiene con ganas de agarrarte el cabello y tirar de el."
    
    hide barneo2
    show barneo3
    
    neo "No te me vayas a ir aún."
    "Dice Neo luego un rato. Te mira de reojo, aun bebiendo de su vaso."
    
    hide barneo3
    show barneo
    
    neo "Sí es que salimos de aquí, te prometo mostrarte algo interesante."
    nj "¿Interesante?"
    neo "Claro. Después de todo, para eso estás aquí."
    "Juguetea con el vaso, moviendo el líquido de un lado para el otro. Sus ojos oscilan entre su vaso y el resto del lugar, aún buscando algo en específico."
    
    hide barneo
    show barneo2
    
    neo "Para consumir y entretener tu aburrida vida con algo. Después de todo, sigues sentado sobre tu trasero jugando es---"
    scene bar with dissolve

    neo "Espera."
    "Neo se levanta de la silla mirando hacia un lugar fijo, lejos de donde ustedes se encuentran. Sin pensarlo mucho, Neo agarra tu mano y te arrastra por el lugar."
    "Corre por la pista de baile hasta el otro lado, llegando a una parte con sillones color burdeos."
    "Pasa por encima de algunas sombras hasta llegar a uno de los sillones, lleno de sombras sentadas... y una mujer regordeta con cabello acaramelado, que lleva una extraña máscara."
    "Al lado de ella hay un ojo..."
    scene act3_neo2 with pixellate
    "Neo sonríe."
    neo "Te encontré."
    stop music fadeout 0.5
    show act3_neo2a with vpunch
    pause 0.5
    hide act3_neo2a
    show act3_neo2b
    "Y agarra el ojo con ambas manos. Lo presiona contra ellas, aplastándolo y provocando que este explote liberando una sustancia negra que recubre gran parte de su ropa."
    "Al explotar, el lugar se borra al instante, perdiendo los colores y las formas que componían el club. Las sombras se esfuman y la mujer no se encuentra en ningún lado."
    
    play music "audio/void3.mp3" fadein 3.0 volume 0.6

    "Todo es reemplazado por un blanco carente de vida. Un lienzo sin tocar. Nuevamente las sombras están ausentes, lo único que te acompaña es Neo."
    menu:
        "¿Qué fue eso?":
            pass
    scene blanco with pixellate
    "Neo se limpia las manos en sus pantalones, eliminando todo rastro del líquido negro que ha dejado esa cosa de sus manos."    
    show neo1serio with dissolve
    neo "¿Te tengo que explicar todo?"
    hide neo1serio
    show neo3incomodo
    "Una de sus manos se eleva llegando a su nuca y masajea el cuello para liberar la tensión. Cierra sus ojos por un instante y suelta un suspira, resignado."
    neo "Eso era una de las versiones de Nulla."
    neo "Tengo que consumirlas para poder pasar a otra memoria."
    "..."
    "No contento con su explicación, añade:"
    hide neo3incomodo
    show neo1serio
    neo "Mmmm, piensa en ellos como el pilar que sostiene cada memoria. Al romperlo, desestabilizamos la memoria completa y me permite hacer esto de nuevo."
    hide neo1serio
    scene act3_neo1a with dissolve

    "Sin perder el tiempo, Neo se agacha para desgarrar la capa con sus manos. De cuclillas y con ambos brazos posado en sus rodillas, mira lo que hay detrás del agujero que ha generado "
    neo "Supongo que ya sabes que hacer."

    menu:
        "Prepararte para zambullirte.":
            neo "Wow~ Que obediente eres."
            pass
        "Retroceder.":
            hide act3_neo1c
            show act3_neo1b
            neo "Tsk."
            pass
    
    show act3_neo1c with dissolve
    "Gira su cabeza para recibirte con una sonrisa llena de gozo, con parpados entrecerrados al mostrar sus dientes. Se ve que está disfrutando esto, el muy maldito..."
    "Algo se enreda en tu tobillo, tomándote por sorpresa y haciendo que tu corazón pegue un brinco. Cuando miras abajo, solo tienes tiempo para confirmar que es la mano de Neo antes de ser lanzado al agujero nuevamente."
    "A la próxima serás tú quien lo empuje a él..."
    scene negro with dissolve
    "Te hundes una vez más. La presión se hace presente, poco a poco haciendo que comiences a desesperar. Cierras los ojos e intentas respirar para calmarte, dándote ánimos de que esto terminará pronto."
    
    play sound "silbido.mp3"

    "Pero un silbido te interrumpe."
    scene act3_neo3 with dissolve

    "{glitch=30.0}{color=ffffff}{b}Ahhh, por esta razón a Nulla le gustaba traerte a un espacio sin luz{b}{/color}"
    #Show Neo mirandote, con risa.
    "{glitch=30.0}{color=ffffff}{b}Los ojos de esta cosa son una ventanita a ti.{b}{/color}"
    
    show act3_neo3b

    "{glitch=30.0}{color=ffffff}{b}Que liiiiindo descubrimiento.{b}{/color}"
    "Añade con un tono despectivo, la burla se expande en todas las vocales i de la palabra lindo."
    "{glitch=30.0}{color=ffffff}{b}Eres justo como te imaginé.{b}{/color}"
    menu: 
        "¡...!":
            scene act3_neo3 with dissolve

            neo "Oh! Esa expresión me gusta."
            neo "Ja ja ja ja, podría acostumbrarme a estar aquí."
            neo "A ver, ahora sonríe mostrando los dientes. Veamos una sonrisa en esa linda carita tuya~"
            menu:
                "Múerete.":
                    show act3_neo3b
                    neo "¡Bah! Que fome eres."
                
                "Hacer lo que pide.":
                    "Neo te mira por unos segundos, esperando a que actues para él." 
                    "..."
                    "Luego solo ríe, complacido con lo que sea que haya visto detrás de la ventana."

        "¿Eso es un insulto?":
            scene act3_neo3b with dissolve

            "Neo levanta las manos y despega la mirada de ti, riendo un poco."
            neo "Yo no he dicho nada insultante."
            neo "Tómatelo como quieras."
            neo "Pero no pongas palabras en mi boca."
    
    "Los siguientes minutos pasan en silencio, Neo ya no te presta atención y decide desaparecer de tu vista."
    scene negro with dissolve
    "Al estar solo, descubres que la presión se acentúa más que cuando estás junto con Neo... te pone nervioso pensar en que pasaría si Neo decide abandonarte aquí a tu suerte."
    "Pero te consuelas con que él necesita de ti para encontrar lo que sea que está buscando."
    "..."
    show negro with vpunch
    "Poco después, sientes el tirón del cuello de tu camisa. Con ello, sabes que Neo ha llegado a tu rescate."
    "Esta vez no necesitas que te golpee la cara para reaccionar y abrir los ojos."
    neo "Por poco te quedas atrapado ahí."
    "No sabes si está jugando o está hablando en serio. Así que te enfocas en su reacción, no se está riendo y su voz suena algo irritada."
    "Quieres preguntarle si eso es verdad, pero tus labios no responden..."
    
    scene calleneo with dissolve

    "Viendo que no hay caso, y que insistir sería una pérdida de tiempo, posas tu vista a tu alrededor. Es una calle abierta, moderna, sin rastros de sombras que decoren el lugar."
    "Neo está plantado en el lugar, observando el cielo con las cejas arqueadas y apretando los puños. Se le ve tenso, cómo si quisiera estar en cualquier otro lado, menos aquí."
    "Sigues la trayectoria de su mirada hacía el cielo y..."
    scene act3_neo4 with vpunch
    pause 0.3
    show act3_neo4a
    pause 0.3
    hide act3_neo4a
    show act3_neo4b
    "¡¿?!"
    "¿Esa es Madre?"
    #Poner la imagen de Madre en el cielo, como si mirara la tierra.
    neo "Esa es Grimal..."
    neo "No las confundas, son dos entidades diferentes debido al tiempo."
    neo "Aquí ella tenía gracia."

    "Neo emprende caminata, dejando de prestar atención a la figura."
    neo "No la pobre versión que ves en el Jardín que llaman Madre."
    
    scene calleneo with dissolve

    "Tu cabeza se ve obligada en desviar la mirada de la gran entidad que observa el terreno. Aún así, sientes que los observa mientras caminan por las calles vacías."
    menu:
        "¿Vamos a buscar otro ojo?":
            show  neo1serio with dissolve
            "La pregunta hace que Neo se detenga y te mire. Es extraño verlo serio. Tan serio que te recuerda un poco a Nulla cuando calla y deja de sonreír por algo que no le ha gustado escuchar."
            neo "Sí."
            "Es lo máximo que te ofrece como respuesta."
            pass
        
        "¿Por qué Madre es tan grande?":
            show  neo1serio with dissolve
            neo "Grimal."
            "Te corrige él, con un poco de irritación en su tono."
            neo "¿Por qué preguntas tanto?"
            neo "Tienes un poco de mí en ti. Deberías ya saberlo."
            "..."
            neo "Uhg."
            neo "Eres peor que entrenar a un novicio."
            pass

        "¿Esta es una memoria de Nulla?":
            show  neo1serio with dissolve
            "La pregunta hace que Neo se detenga y te mire. Es extraño verlo serio. Tan serio que te recuerda un poco a Nulla cuando calla y deja de sonreír por algo que no le ha gustado escuchar."
            neo "No. Esta es mía."
            "Es lo máximo que te ofrece como respuesta."
            pass
    
    "..."
    menu:
        
        "Acerca de lo que prometiste...":
            pass

    hide neo1serio
    show neo3incomodo
    "Él levanta una ceja al escucharte, algo confundido."
    neo "¿Te prometí algo?"
    nj "Sí, mostrarme algo interesante."
    hide neo3incomodo
    show neo3risa
    neo "Ah..."
    hide neo3risa
    show neo1serio
    neo "Uh."
    "Por su reacción, comprendes que no tiene nada preparado para ti, que se lo ha inventado completamente... parte de ti se siente decepcionada."
    "No vas a mentir. Ya te estas cansando un poco."
    hide neo1serio
    show neo3incomodo
    neo "Santa mierda, eres como un niño. ¿Acaso quieres que te ponga luces de colores y sonidos para mantener tu atención? ¿Cómo esas aplicaciones de contenido basura que chupan tu atención con estímulos cortos y llamativos?"
    neo "No tengo nada de eso aquí."
    neo "Así que no puedo recurrir a ello..."
    hide neo3incomodo
    show neo2risa
    neo "Pfff."
    "Neo ríe imaginando quien sabe que cosa."
    hide neo2risa
    show neo1normal
    neo "Pero puedo hacer esto."
    hide neo1normal with dissolve
    "Ante tus ojos, la forma de Neo es cubierta por una sustancia negra. Esta burbujea con insistencia, engullendo todo rastro de su cuerpo, carcomiendo todo lo que lo hace él."
    "Unos apéndices lo envuelven en espiral, apretando con fuerza la masa negra que ahora es Neo. Es una imagen asquerosa, ya que no solo puedes ver, sino sentir y escuchar como estas cosas se mueven."
    "Luego, la masa comienza a inflarse hasta alcanzar un tamaño preocupante. Y de un instante a otro, revienta con violencia."
    scene negro with dissolve
    "Cubres tu cabeza con ambos brazos, temiendo que la sustancia caiga en tus ojos o boca."
    "..."
    "Cuando sientes la ausencia de la voz de Neo y de líquido sobre ti, descubres tu cara para ver que sucede."
    scene calleneo with dissolve
    show act3_neo5 with dissolve
    pause 1.0
    "Uh..."
    "Es un..."
    "Es... la nueva forma de Neo es muy similar a la de un canino de exorbitante altura. Menos de 100 kilos no pesa esta cosa, su largo hocico desfila dientes tan grandes como tus dedos, pero lo que más te sorprende son sus ojos."
    "Tiene 6 de ellos en total, cada par de un tamaño diferente que resaltan gracias al color de su pelaje... Sus pupilas se mueven buscando tu presencia y se clavan en ti."
    hide act3_neo5
    show act3_neo5_enojo
    neo "No es la gran cosa, pero esta forma era la mejor para desplazarse por estas calles."
    neo "Y para ver lo oculto..."
    menu:
        "Acariciarlo.":
            hide act3_neo5_enojo 
            show act3_neo5_harto
            neo "Ni se te ocurra---"
            "Su cola golpea tu cara con fuerza, alejando su cuerpo mientras muestra sus dientes."
            "El golpe te deja estático, con un dolor leve en tu mejilla que te obliga a sobar la zona."
            #Neo no se deja y hace que te va a morder la mano. "ni se te ocurra."
            "..."
        
        "¿Cómo puedes hacer eso?":
            hide act3_neo5_enojo 
            show act3_neo5
            neo "Magia."
            hide act3_neo5
            show act3_neo5_harto
            "Responde con un gesto desdeñoso, poniendo los ojos en blanco, harto de tus preguntas."
            "..."
        
        "Buen chico.":
            hide act3_neo5_enojo 
            show act3_neo5_harto
            neo "Voy a ignorar que dijiste eso."
            #Neo se enoja.
            "..."
    hide act3_neo5_harto with dissolve
    scene calleneo with dissolve
    "Neo se da media vuelta, ignorándote por completo. Sube su cabeza, exponiendo su nariz al frío aire de la cuidad."
    "Ver se hocico y nariz temblar levemente para captar las particulas en el viento  te causa un poco de ternura, la cual intentas sepultarla en lo más bajo de tu ser."
    "Tierno sería el último adjetivo para utilizar con Neo..."
    show act3_neo5 with dissolve
    neo "Está cerca."
    "Dice para si mismo. La voz debería bastarte para identificar que está contento, aunque tus ojos descienden a su cola, con un poco de esperanza de captar su cola moviéndose."
    "Te sorprendes al notar que, en efecto, si hay un meneo de su cola, pero es tan lento que no se asemeja a al movimiento que hacen las colas de los perros cuando están felices."
    "Le falta energía a esa colita... tal vez si le acaricias la cabeza y finges una voz aguda que lo tape en cumplidos te pueda mover la cola como lo hacen los perros normales."
    hide act3_neo5
    show act3_neo5_harto
    neo "¿A tu marioneta le pagan por pensar weas o siempre ha sido así?"
    "Te le quedas mirando, sin decir nada. Je, él podrá controlar todo de ti, menos tus pensamientos." 
    "¡Toma eso pulgoso!"
    hide act3_neo5_harto
    show act3_neo5
    neo "..."
    "Lo que obtienes es una mezcla entre suspiro y gruñido que hace retumbar tus oídos."
    hide act3_neo5
    show act3_neo5_enojo
    neo "No tengo tiempo para esto."
    hide act3_neo5_enojo with dissolve
    scene calleneo with dissolve
    "Neo comienza a caminar al mismo tiempo en que tus piernas avanzan en la misma dirección que él lo hace. No sabes donde van, así que te toca esperar a descubrir cual será la siguiente parada."
    "El tiempo aquí es difícil de medir, sabes que ya llevan una cantidad considerable de el caminando... Tus sentidos están confusos y las calles no hacen más que empeorar la sensación de estar perdido."
    "Todas las cuadras son iguales, tanto así que pareciera que avanzan en una enorme cinta de caminadora. Mismos árboles, mismo farol de luz que titila debido a una ampolleta mal colocada, mismo grafiti en el edificio de la derecha---- te vas a volver loco."
    "Para la vuelta siete, te cuestionas cuantas posibilidades de sobrevivir tendrías si te subes al lomo de Neo. Se ve perfecto en temas de tamaño para montarlo al puro estilo del viejo oeste."
    "Maldices al instante no poder mover tu cuerpo de la manera que quieres. Ni siquiera puedes limpiarte la gota de sudor que te corre por la frente. Y eso es puramente por maldad de Neo. Quien se ríe al notar tus ganas de hacerlo, ya por segunda vez."
    menu:
        "¿Cuanto falta?":
            show act3_neo5_harto with dissolve
            neo "¿Qué, la princesa está cansada ya?"
            "Tus cachetes se inflan pero nada sale de ti. Neo te ha sellado los labios."
            "Pulgoso..."
        
        "¿Por qué todo es igual?":
            show act3_neo5_harto with dissolve
            neo "Porque ya las memorias se están distorsionando."
            neo "Si no nos apuramos, no voy a poder encontrarla."
    hide act3_neo5_harto with dissolve
    show neo1serio with dissolve
    "Caminan por unos metros más, hasta que Neo se detiene. Al hacerlo, su forma vuelve a ser envuelta por la sustancia negra, trayendo de vuelta su figura humana."
    hide neo1serio
    show neo3incomodo
    neo "¿Qué pasa? se supone que eso debería estar por aquí."    
    hide neo3incomodo
    show neo1serio
    neo "... Espera------------------"
    hide neo1serio
    show neo2enojo
    neo "No está físicamente aquí, ¡QUE IMBÉCIL!"
    "Su pequeño debate con si mismo es gracioso de ver. Te hace algo de ruido verlo insultarse con tanta facilidad y el lenguaje grosero que usa en su vocabulario, vocabulario que es recurrente en su hablar."
    "Ya has perdido la cuenta de cuantas veces ha dicho 'mierda' en el tiempo que llevas con él."
    hide neo2enojo
    show neo2risa with vpunch
    "El contacto de su mano con la tuya evita que sigas analizando a Neo. Te asustas por lo súbito de su actuar pero su explicación te frena antes de que saques conclusiones, o siquiera sepas que estás pasando."
    neo "Te voy a usar como carnada."
    "¿¡Huh?!"
    hide neo2risa
    show neo1normal
    "Neo ríe al ver tu reacción, pero no se molesta en consolarte."
    hide neo1normal
    show neo3risa
    neo "Tantas veces siguiendo el protocolo y se me ha olvidado la mierda más básica."
    hide neo3risa
    "Su cara se levanta al viento, buscando a Madre. Ella le devuelve la mirada, esperando."
    neo "Señora Grimal, tengo a un transgresor."
    scene calleneo with vpunch
    "¿¡Qué?! ¿¡Quién se cree ese maldito para ponerte a ti en peligro y decir estupideces que seguro harán que te corten la cabeza?!"
    "No te vas a dejar matar por algo así."
    "Intentas deshacerte de su agarre, y aunque puedes moverte libremente, Neo no te deja ir." 
    "Para peor, él aprieta su agarre en tu brazo, haciendo que te duelan las grietas, que sueltan un poco de líquido negro, simulando sangre."
    neo "Han intentado contactar con las criaturas de la jurisdicción de Ciro y no muestran arrepentimiento en ello."
    neo "Por favor, déjeme acceder al juicio."
    scene negro with dissolve
    "De pronto, todo se vuelve negro."
    scene act3_neo6 with pixellate
    #Insertar la imagen de Neo hablando con grimal y Ciro (ojos solamente).
    #Es una memoria, Neo ha activado una memoria. "eel" es Ciro
    "Hay dos ojos gigantes observando a Neo y a otra figura humana, tiembla y lloriquea pidiendo perdón."
    "Observas a Neo notando que algo está mal con él... Lleva otro tipo de ropa y su peinado es distinto. ¿Se ha cambiado?"
    "Cuando intentas acercarte, te das cuenta de que no avanzas por más pasos que des."
    "..."
    neo "---Se le advirtió 3 veces, y aun así no cesó sus intentos de contacto con los de las capas inferiores."
    scene act3_neo6a with dissolve
    el "¡Mi padre está allí! ¡Él no ha hecho nada para ser tirado a las capas de abajo!"
    show act3_neo6c
    neo "Te he dicho que te calles."
    madre "Joven Neo."
    "Neo retrocede y agacha la cabeza ante la intervención de Madre. Disculpándose, diciendo su nombre."
    hide act3_neo6c
    show act3_neo6b
    ell "Por que tanto escándalo, ya ha roto las reglas, ahora me pertenece."
    el "¡No!"
    ell "Oh ho ho ho, tampoco respeta a la autoridad."
    ell "La quiero aún más."
    "Las comisuras de Neo tiemblan, sientes su desagrado revolotear por tu estómago y garganta, pidiendo a gritos que Girmal mande a callar a esa bestia de las capas de abajo."
    scene act3_neo6 with vpunch
    el "¡Por favor Gran Juez-!"
    madre "Hija mía"
    el "¡Mi padre no hizo nada!"
    madre "Tu progenitor asesinó a dos hombres ---"
    "{glitch=30.0}{color=ffffff}{b}Aquí estás~{b}{/color}"
    menu:
        "¡¿Nulla?!":
            "..."
            "{glitch=30.0}{color=ffffff}{b}A ti como que te cuesta conectar neuronas un poco, ¿no?{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}Él ya no puede acceder a nosotros.{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}Se ha quedado atrapado en la primera capa,\nY seguramente cuando la salga de sus memorias al Jardín buscándote---{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}No te encontrará haya afuera y se quedará imposibilitado de seguir con su plan.{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}Pobrecitooo~{b}{/color}"

        "¿Neo?":
            "{glitch=30.0}{color=ffffff}{b}¡DING,   DING,    DING!{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}Correctooooo, no eres tan cabeza hueca como creí.{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}Me impresionas.{b}{/color}"
    
    "{glitch=30.0}{color=ffffff}{b}Bueno, ya basta.{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}Necesito que toques a esa versión mía.{b}{/color}"
    "Ah... con que la persona que tienes al frente no es Neo. al menos no es 'tu Neo'."
    "Ahora comprendes... un poco..."
    menu:
        "Acercarte y tocar a Neo.":
            pass

        "No hacer caso.":
            "{glitch=30.0}{color=ffffff}{b}¿Te sigues resistiendo?{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}No tienes voz ni voto aquí conmigo, mi vida.{b}{/color}"
            "No importa cuánto te resistas, ni cuánto luches o ignores, tu cuerpo ya no parece ser tuyo."
            "Neo no te va a dejar hacer nada que él no quiera."
    
    scene negro with pixellate
    "Tus pasos son rápidos, sin mucho cuidado. No son cautos al pisar, su eco resuena en todo el espacio pero el resto de las entidades no reaccionan antes ello."
    "Después de todo, es una memoria, no puedes interactuar con una memoria... ¿O sí?"
    "Estás a unos centímetros de Neo y es la primera vez que lo tienes tan cerca sin que él te reconozca. Tiene la misma altura que el Neo que conoces, pero sus facciones son algo diferentes."
    "Son diferencias mínimas, al igual que el peinado, pero no es igual al Neo te ha robado a Nulla."
    "Tocas su hombro, esperando a despertarlo o algo similar. Obtener al Neo que te acompaña a tu viaje. Más lo que obtienes es una salpicadura de líquido en tu cara."
    "Neo acaba de explotar frente a ti."
    "Justo como lo ha hecho el ojo cuando Neo lo presionó entre sus manos..."
    
    scene blanco
    show vacio3
    pause 0.10
    hide vacio3
    show vacio2
    pause 0.10
    hide vacio2
    show vacio
    pause 0.10
    hide vacio
    show blanco
    scene blanco

    "Luego, todo se vuelve blanco."
    
    play music "clap.mp3" fadein 1.5

    "Aplausos con pausas de un segundo te reciben. No son aplausos genuinos, se sienten más como una burla a tus acciones y todo lo que has hecho hasta ahora."
    show neo1risa with dissolve
    neo "Gracias."
    hide neo1risa 
    show neo2risa
    stop music fadeout 2.0
    
    play music "audio/void3.mp3" fadein 1.0 volume 0.5

    neo "Ahora podemos continuar."
    neo "Ya me estaba desesperando."
    menu:
        "¿Ese eras tú?":
            pass
    
    neo "¿Hmm?"
    hide neo2risa with dissolve
    scene act3_neo1b with dissolve

    "Neo ya está en posición para desgarrar esta capa, hace una pausa y te mira. Debido a que está de cuclillas, debe girar su cabeza para mirarte desde abajo."
    neo "Sí, ese era yo."
    neo "Antes de que todo se fuera a la mierda-"
    "Hasta ahí llega su respuesta, pues prefiere rasgar la capa y tirarte al agujero sin darte el derecho a reaccionar primero."
    scene negro with dissolve
    
    "Caes..."
    "El vértigo te revuelve el estómago y te provoca un cosquilleo desagradable en el vientre, que no te deja tranquilo, generando angustia."
    "No crees poder soportar esta sensación una vez más."
    neo "Pffft---"
    neo "No creo que estés sintiendo nada de eso realmente."
    neo "Con tu culo ahí sentado, el vértigo solo es una fantas---"
    stop music fadeout 2.0

    "Neo deja de hablar. Su voz se corta por completo."
    "... Ya no está contigo."
    "Tus pies tocan suelo luego de un tiempo."
    "Todo está a oscuras."
    "El silencio devora el lugar."
    "Hasta que una conversación comienza a filtrarse desde algún punto lejano. Las voces son apenas un murmullo en el aire, demasiado sutiles como para distinguir las palabras que se dicen."
    "Decides seguirlas, curioso por los detalles de esta conversación... Quienesquiera que sean, están lejos, ya que ni siquiera los puedes ver."
    ell "Eres una ternura~"
    "Ahora puedes escuchar con facilidad. Es una voz masculina... tiene el mismo tono de la entidad que acompañaba a Madre en la memoria anterior." 
    "Te acercas más, divisando una luz a unos 10 metros de donde estás."
    ell "Todo arregladito y bonito para recibir tu nuevo rango~"
    ell "Ah~~~ aún recuerdo cuando eras tan solo un cachorrito---"
    el "..."
    ell "Dime, ¿El traje te lo hizo Grimal?"
    scene act3_neo7 with dissolve
    "Wow..."
    "Al frente tienes una entidad en forma de hombre, que se alza sobre ti."
    "Es gigante."
    "Debajo, a la altura de su pecho, se encuentra Neo."
    "Aunque, no es {b}TU{/b} Neo."
    "Es una memoria."
    ell "¿No eres muy conversador, eh?"
    neo "..."
    neo "Dijiste que tenías algo que darme."
    ell "Jaaaa--- ¿sólo vienes por eso?"
    ell "Eres igual a ella."
    neo "Apúrate, no tengo todo el día. Grimal me está esperando."

    scene act3_neo7b
    ell "Te has vuelto arisco conmigo~"
    ell "Si no fueras de ella, ya te habría puesto en tu lugar, mocoso."
    "Neo no responde, solo le mira aburrido. Esperando a que el hombre se digne en darle lo que le ha prometido."
    ell "Bien---"
    ell "Tengo un regalo para ti."
    ell "El conocimiento de un Dios."
    ell "Es un buen regalo de ascenso, ¿no crees?"
    
    play sound "tv-static.mp3" fadein 2.0 volume 0.5

    ell "Bien, escucha con atención----"
    "---------------------"
    scene act3_neo7c
    "{glitch=30.0}{color=ffffff}{b}---------------------------------{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}--------------------------------------------------------{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}--------------------------------------------------------------------------------------{b}{/color}"
    show consumo
    pause 0.5
    scene negro
    show nada1 with dissolve

    play music "audio/ruidoblanco.mp3" fadein 2.0 volume 0.6

    centered "¿Qué haces aquí?...."
    menu:
        "¿Qué fue eso?":
            pass

    centered "Ah- lo viste..."
    centered "Uhg..."
    menu:
        "¿¿Qué fue eso??...":
            pass

    centered "Eh- supongo que así nació todo."
    centered "Bravoooo---"
    "Escupe cada sílaba con asco, fingiendo falsa alegría."
    centered "Encontramos el origen del mal de Nulla~"
    centered "Yujuu----" 
    extend "----------uhg."
    show neo3incomodo with dissolve
    neo "El muy hijo de las re-mil putas ni siquiera me dio nada."
    neo "Solo me hizo dudar de mi todo."
    neo "Terminé yendo con Grimal, él me dijo que ella me lo diría..."
    hide neo3incomodo
    show neo1serio
    neo "Fui un estúpido."
    neo "Le insistí... estaba paranoico."
    hide neo1serio
    show neo3incomodo
    neo "..........."
    extend "Cuando dejé de comer ella cedió."
    neo "...."
    hide neo3incomodo
    show neo1risa 
    "Neo suspira, dejando una pausa pesada que no sabes como rellenar."
    neo "Bueno, nah' que hacerle'."
    hide neo1risa with dissolve

    "....."
    "..........."
    "Y así es como te sometes a otra búsqueda al lado de Neo. Junto con ello se origina la repetición de acciones para pasar a la siguiente capa. Se vuelve un juego tedioso que ni tú ni él disfrutan."
    "Han caído por lo menos cuatro veces  a una nueva capa de memoria y aun no hay avance alguno. Buscan los ojos o segmentos que conforman a Neo y sus vidas pasadas. Con cada capa de memoria nueva, a él se le ve más impaciente."
    "Blanco total. Él rompe la capa. Entran, contigo ya saltando sin ser empujado o arrastrado adentro. Buscan el segmento, hay veces en que demoran más y otras menos. Lo rompe. Explota y se reinicia la secuencia de acciones."
    "A la quinta vez, viendo que no han llegado a lo que él tanto busca, Neo explota en rabia."
    "Han estado en la playa, en medio de un campo vacío, una cabaña vieja; un supermercado de pasillos infinitos; y ahora en un local de comida, de esos típicos que vas con tu familia o amigos a pasar el rato."
    scene restaurante_americano with dissolve
    neo "Esto no está funcionando..."
    neo "Aghh---"
    scene restaurante_americano with vpunch
    "Se desploma en una de las tantas mesas que hay en el lugar, la silla cruje al hacer contacto con el cuerpo de Neo gracias a la fuerza con la que se tira en ella."
    neo "Estamos jugando con aleatoriedades."
    "Se acomoda en el asiento, estirando sus delgadas piernas hasta tocar las patas de la silla que tiene al frente. Una mano masajea su frente, subiendo hasta sus cabellos, dejando por una fracción de segundo su frente despejada del flequillo que tiene."
    neo "..."
    "Neo te atrapa mirando."
    neo "Ven, siéntate."
    "Acostumbrado a no ser el dueño de tus movimientos, te dejas manipular. Neo te sienta al frente suyo, lo que hace que al acomodarte, toques sus piernas por accidente. Sin embargo, él no se mueve ni intenta evitar el contacto."
    "Sus dedos golpeando la mesa acompañan el sonido de las maquinas de refrigeración que se encuentran en el mostrador. Además de ustedes dos, no hay nadie en el local, haciendo el momento más pesado de lo que debería ser."
    scene act3_neo8 with dissolve
    "Sus ojos te escanean por un largo tiempo, deteniéndose en tu cara como si buscara algo en ella."
    "No sabes si el destino te odia o qué, pero tu estómago se hace notar, retorciéndose demandando comida."
    "Neo aprieta los labios, y aunque evita esbozar una sonrisa burlona, su voz no es capaz de ocultarlo."
    show act3_neo8a
    neo "¿Tu marioneta tiene hambre?"
    menu:
        "No.":
            neo "Mmmm, que lástima, porque yo sí."
        
        "Sí...":
            neo "Okay."
            neo "Yo invito."
    scene act3_neo8e with dissolve

    "Le basta con chasquear los dedos para hacer aparecer comida en la mesa. La mayoria es comida chatarra que habitualmente encuentras en las cadenas de comida rápida."
    "La vista es obsena debido a la cantidad innecesaria de alimentos en la mesa. Mas de 3 vasos grandes de liquidos gaseosos, hamburguesas más grandes que tu ambos de tus puños juntos, helados en copa y un montón de otras cosas que te no te da el tiempo de analizar..."
    "Es mucho. Y tienes la oportunidad para escoger lo que quieras gracias a la variedad que hay."
    "Se te hace agua la boca sin que puedas controlarlo... tienes hambre."
    "Dudas que puedan comer siquiera el 20 porciento de lo que tienen al frente."
    scene act3_neo8c
    "Neo no espera a por ti, alarga su mano para sacar un poco de patatas fritas y untarlas en una salsa roja, que intuyes es ketchup."
    "Por algún motivo, esperabas que Neo comiera rápido y de forma decente, sin cuidado... pero no."
    "Come con tranquilidad y eso te deja mudo... al menos tienes modales. Será un papanatas de primera, pero al menos tiene modales en la mesa."
    neo "Qué esperas, come."
    "...si bien tienes hambre, temes que la comida tenga algo que te haga sentir mal... o peor, te mate."
    neo "Ay por favor."
    neo "La comida no te hará nada."
    neo "Come."
    menu:
        "'No quiero nada de lo que está aquí.'":
            show act3_neo8e
            neo "Si que eres dificil de complacer---"
            neo "¿Qué quieres? Te lo puedo dar si me dices."
            "Le describes con lujo de detalle lo que se te antoja comer. Neo te escucha con atención y pregunta por el tamaño de la porción cuando terminas de hablar."
            "No le toma más de 10 segundos hacer aparecer tu plato al frente de ti. El resultado es impresionante, ¡se ve muy rico!"
        
        "Comer algo.":
            show act3_neo8e
            jump opcionescomida    #"Inspeccionas la mesa una vez más antes de decidir lo que comerás."
                                #"Una vez seguro, tomas lo que comeras y lo colocas al frente tuyo."
            
label continuacion_neo:  
    scene act3_neo8c
    "Al inicio no te das cuenta. Comes con normalidad, sin mucha prisa pero con ganas... después de todo, si tenías mucha hambre y sed."
    "Luego, te percatas de Neo, quien posa sus ojos en tu figura mientras comes."
    "..."
    "Te pone los nervios de punta, pero no dejas de comer e ignoras su presencia... o lo intentas."
    "Sus ojos siguen el camino que trazan tus manos para terminar llegando al mismo punto, tus labios."
    "Neo no aparta la vista de ti mientras masticas. Tampoco al tragar, sus ojos siguen el movimiento de tu garganta y eso hace que te sientas expuesto, hasta un poco vulnerable..."
    "Quieres preguntar qué pasa, qué busca. ¿Quiere burlarse una vez más?... no, en su rostro no hay pisca de burla o risa. Le falta ese toque de malicia en los ojos para ello."
    "Él ya no come. Toda su atención está en ti."
    neo "Hace tiempo que no me sentaba a comer con alguien."
    "Dice él, al ver que te has detenido por su culpa."
    neo "Ah vamos, come más~"
    
    scene act3_neo8d

    "Neo toma una porción de lo que estás comiendo y te lo acerca a la boca. Su comportamiento vuelve a ser el mismo, la sonrisa ladeada vuelve a aparecer y en sus ojos se cola esa malicia latente."
    neo "Te ves lindo haciéndolo."
    "Lo dice con un tono condescendiente, ronroneando las silabas para que salgan de su boca." 
    neo "Vamos, come más. Di: ahhh~~"
    "Te está provocando y tus mejillas hierven de vergüenza o rabia... no estás muy seguro."
    neo "Es gracioso cómo cambias cuando sabes que te están mirando, te pareces a---"
    "Neo suelta un jadeo y levanta la vista con urgencia."
    neo "Espera, esto es---"
    
    stop music

    show vacio
    pause 0.10
    hide vacio
    show vacio2
    pause 0.10
    hide vacio2
    show vacio3
    pause 0.10
    hide vacio3
    show negro
    scene negro

    "Todo se vuelve negro."
    "..."
    
    scene act3_neo9
    show vacio3
    pause 0.10
    hide vacio3
    show vacio2
    pause 0.10
    hide vacio2
    show vacio
    pause 0.10
    hide vacio
    scene act3_neo9

    play music "audio/fell.mp3" fadein 2.0 volume 0.4

    "Una memoria se ha accionado. Neo está sentado en la misma mesa, aunque quien lo acompaña no eres tú. Es una chica de cabello castaño miel, largo y lacio... que juega con sus dedos para manejar los nervios."
    "El contenido de la mesa se ve mucho menos lleno que antes, solo tiene lo necesario. Una porción para cada uno, de algún combo que desconoces del lugar, más una gran malteada para compartir."
    "Te centras en Neo, quien si bien tiene esa misma cara de desborda confianza, algo dentro de su pecho y tripa algo no lo deja tranquilo."
    "Sientes lo que él está sintiendo ahora mismo, y para tu sorpresa lo que se desliza por tu cuerpo es una mezcla de nervios y rabia. El viejo dicho de 'mariposas en el estómago' junto con algo de ira."
    "Neo está nervioso porque gusta de esta chica... pero... está enfadado."
    "La chica mira de reojo su alrededor, no queriendo tocar su comida."
    "Él toma su hamburguesa, pero hace una pausa al notar que ella no lo mira."
    neo "¿Sigues pensando en eso?"
    el "..."
    neo "Mira, son unos imbéciles, ni siquiera deberías de escucharlos..."
    neo "Te juro que cuando los vea, les voy---"
    el "Neo, para. Tienen razón."
    "Lo interrumpe soltando un quejido, con una voz que intenta aguantar las lágrimas."
    neo "¡¿Razón en qué?!"
    neo "Eres muy linda. Linda con cualquier ropa que te pongas, linda comiendo, linda---"
    el "Basta---"
    show act3_neo9a
    "La chica se tapa la cara con ambas manos, claramente afectada por los comentarios de Neo, lo que provoca que el pelinegro ría por fin."
    neo "No en serio."
    neo "No te sientas mal por comer."
    "Neo toma sus manos con delicadeza, y descubre su cara para poder mirarla a los ojos."
    neo "Te... te vez muy linda cuando lo haces."

    show nada1 with dissolve

    "{glitch=30.0}{color=ffffff}{b}Huh, que metiche eres. Atrevido~{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}Dime, ¿te diviertes?{b}{/color}"
    "..."
    "{glitch=30.0}{color=ffffff}{b}Mmmm, me pregunto cómo te sentirías tú si un desconocido entrara a tu cabeza para mirar tu vida privada.{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}No es justo, pero no es algo que pueda controlar.{b}{/color}"
    menu:
        "Lo siento...":
            "{glitch=30.0}{color=ffffff}{b}Nahh, te estoy jodiendo.{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}Ya estoy acostumbrado, que sepan todo de mi.{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}Es el precio que tengo que pagar por ser tan guapo e interesante.{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}Pfff--- {b}{/color}"
            extend "{glitch=30.0}{color=ffffff}{b}no te creas.{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}Bueno--- hora de mover esas piernas.{b}{/color}"
        
        "¿Qué es esto?":
            "{glitch=30.0}{color=ffffff}{b}Una memoria muy importante.{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}¿Sabes por qué?{b}{/color}"
    
    "{glitch=30.0}{color=ffffff}{b}Aquí vamos a encontrar a Mary.{b}{/color}"
    menu:
        "¿Qué?":
            pass

    "{glitch=30.0}{color=ffffff}{b}Lo que busco está en esta capa de memoria.{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}La chica que tienes al frente era su amiga. Estamos cerca.{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}Bien, ahora da la vuelta y deja que te lleve.{b}{/color}"

    scene restaurante_americano 
    show nada1
    with dissolve
    
    "Tu cuerpo se acerca a la puerta del local. Abandonando a Neo y a la chica."
    nj "¡Hey, hey! ¿No me harás tocar a este Neo?"
    "{glitch=30.0}{color=ffffff}{b}No seas tarado. Si lo hago, está capa se borrará.{b}{/color}"
    "..."
    "Sales del restaurante a paso lento."

    scene valpo 
    show nada1
    with dissolve

    "Caminas por las calles del lugar. Es un barrio con mucha pendiente, las casas son muy coloridas y te encuentras con varios murales en cada rincón."
    "Cuando miras más allá, vez el mar. Tranquilo y sereno, meciéndose en un vaivén infinito... Al respirar hondo, puedes sentir la brisa de la playa, te calma y no sabes si es por la influencia de Neo o no."
    
    scene casaneo 
    show nada1
    with dissolve

    "Llegas a una casa, la cual es mucho más detallada que las demás. Hasta crees que brilla un poco."
    "En el jardín, hay flores amarillas a por montones repartidas en puntos estratégicos. Se nota que no han crecido ahí por casualidad; han sido plantas por alguien."
    "Abres la reja, y caminas por el jardín, siguiendo el camino de cemento hasta la casa."
    "...."
    "Tienes una sensación extraña, que te recorre por todo el cuerpo."
    stop music fadeout 2.0
    scene puertaneo 
    show nada1
    with pixellate
    
    "De pronto, todo pierde su color. La casa ya no está, en cambio, la reemplaza una puerta negra de aspecto antinatural."
    "A Neo parece no importarle en lo más mínimo."
    scene puertaneo2 
    show nada1
    with dissolve
    
    "Ambos avanzan a la puerta. Una vez al frente, Neo toca la manilla de la puerta y la gira..."
    extend "Nada sucede."
    "Batalla con más fuerza, intentando forzar el mecanismo, perdiendo el quicio rápidamente."
    "Suelta unas maldiciones al aire."
    menu:
        "¿Y si mejor tocas?":
            pass
    "Neo frunce el ceño."
    neo "Claro, como si eso ayudara en algo..."
    neo "No seas estú---"
    play sound "tocarpuerta.mp3"
    "Eres tú quien toca, haciendo callar al pelinegro."
    "La respuesta es inmediata. Se escuchan unos pasos ajetreados, junto con una vocecilla irritada que rebota contra la puerta."
    el "Ya voyyyyy---"
    "Neo se congela por completo. Sus ojos se abren al menos dos veces su tamaño normal y su boca cae con incredulidad."
    
    scene puertaneo3 
    show nada1
    with dissolve
    pause 1.0
    scene puertaneo4
    show nada1
    pause 0.5

    el "¿Neo?"
    pause 1.0
    play sound "tv-static.mp3" volume 0.5

    show vacio
    pause 0.10
    hide vacio
    show vacio2
    pause 0.10
    hide vacio2
    show vacio3
    pause 0.10
    hide vacio3
    show negro
    scene negro
    "-------------------------------"
    "-----------------------------------------"
    scene blanco
    show vacio3
    pause 0.10
    hide vacio3
    show vacio2
    pause 0.10
    hide vacio2
    show vacio
    pause 0.10
    hide vacio
    show blanco
    "-------------------------------------------------"
    "------------------------------------------------------------"



    "{glitch=30.0}{color=ffffff}{b}Mary........{b}{/color}"
    $ MainMenu(confirm=False)()
    return
   

label opcionescomida:
    menu:
        "Quiero el hotdog.":
            neo "Completo."
            nj "¿Qué?"
            neo "Es un completo, no hotdog."
            nj "..."
            neo "No, no, nada de 'hot dog', eso se llama completo."
            "No te vas a poner a discutir con él."  
            jump continuacion_neo        

        "Quiero la hambuerguesa.":
            neo "¿La normal, doble o triple?"
            menu:
                "La normal.":
                    "Neo te inspecciona, serio por un segundo. Para luego, echarse una risa."
                    neo "Esperable."
                "La doble.":
                    "Sonríe encontrando graciosa tu respuesta."
                    neo "Uy, cuidao' con alocarte."

                "La triple":
                    "Neo te muestra los dientes al sonreir, arrungando la nariz."
                    neo "¿Tú quieres dejarme en la ruina, o qué?"
                    "A pesar de sus palabras, él se echa a reír."
            jump continuacion_neo

        "Quiero las papas.":
            neo "La mejor opción."
            neo "Podemos compartir."
            jump continuacion_neo
#1052
label another_story:

    scene negro
    if persistent.juegocompleto == True:
        jump rutasnuevas
    
    else:
        pass
    
    "....."
    creador "Oh no querido."
    creador "Aún no estás listo para pasar a esta parte de la historia."
    creador "Falta una actualización más.          "
    extend "------Luego de eso...."
    creador "Debes completar las tres rutas principales, con eso podrás verme y---"
    creador "Quien sabe... tal vez en un futuro aquí puedas ver el epílogo de todas las historias.."
    #EDITAR  PONER LA CONDENADA VARIABLE AL FINAL DE CADA RUTA
    #$ persistent.juegocompleto = True
    $ MainMenu(confirm=False)()


label rutasnuevas:
    if persistent.rogar == True:
        jump rogar
    #Poner una pantalla para tocar los epilogos que quieres ver.

label rutamusae:

    centered "En el Jardín existen 7 estandartes a los cuales se les debe rendir culto. Cada uno representa un concepto ligado a su creación."
    centered "Los estandartes son entidades engendradas por el Creador para mantener el orden y funcionamiento del jardín."
    creador "Decir que fui yo solamente sería robarme el crédito. Despues de todo, fue Septem quien los creó."
    creador "Yo solamente le he ayudado."
    centered "Todos los seres nacidos bajo el comando del jardín tienen una conexión limitada con un estandarte representativo, dependiendo del día en que se haya nacido"
    centered "... Nadie nace el día 7. El domingo, el domingo es un día sacro."
    creador "Es fue el día en que Septem descansó y observó lo que ha creo bajo mi mandato."
    centered "Se dice que los estandartes eligen a 6 personas luego del festival de las velas, para luego consumirlos-"
    centered "Con la esperanza de que alguno de ellos sea la reencarnación del Creador."
    creador "Y hete aquí, la 'reencarnación del Creador', un reemplazo que viene a salvarlos a todos..."
    creador "O destruirlo todo."
    creador "Dependiendo de lo que quieras con tu narrativa."
    creador "Oh no, no, no. No te juzgo por tu elección, puedes hacer lo que se te de la reverenda gana."
    creador "Esa es la gracia, jugar y entretenerte."
    creador "No puedo hacer más que felicitarte por llegar tan lejos."
    creador "Eres un digno sucesor."
    scene negro with dissolve
    #close up de Musae
    creador "Veo que has eleguido mi 'ruta'."
    creador "No me sorprende mucho, ya sé que soy muy bello. Que está apariencia hace que quieras saber más."
    creador "¿Sabes? la forma que ves de mí fue hecha como un chiste."
    creador "Para comprobar si una el aspecto físico influye en la opinión de un individuo."
    creador "¿Ha funcionado? ¿hmmm?"
    creador "¿Vas a perdonar todos mis pecados por esta cara linda? ¿hmm?"
    menu:
        "Estás loco.":
            "..."
        

        "Sí...":
            ""
        
        "No, te odio.":
            creador "Ah, ya veo."
            creador "Bueno."
            creador "Viendo tu respuesta de tan baja clase. Me veo en la necesidad de vetarte de aquí"
            creador "Si quieres volver aquí, tendrás que rogar."
            $ persistent.rogar = True
            $ renpy.quit()

    #Padre te invita a una cita. La cita es parecida a la que tienes en el ruta de Septem. Padre habla de esa cita y dice que fue muy corta por el hecho de que no quería interrumpir tanto en esa ruta.
    #Que si lo hacía, probablemente ibas a terminar confundido y no recordando mucho donde habías quedado.
    #Padre habla de que siempre ha estado mirandote, y viendo lo que haces. ¡Incluso te ha ayudado en algunas ocaciones!
    #Te dice que la llave del cajón en el cuarto de informaciones, se la ha robado él a Septem y la ha colocado en un lugar de facil acceso para ti.
    #Que sin eso, jamás podrías haber sacado a Rafael. (Este dialogo solo sale si tienes activado el persistent.rafaelhumano)
    #Tambien te dice que la presencia que sentiste en el dominio de Nulla, era él.
    #Que no pudo evitar observarte de cerca.
    #Padre habla de que gusta mucho estar en el Jardín, siempre y cuando tú estés ahí, viendo como la historia se desenvuelve. 
    #Te confieza que hubo un tiempo en que se sintió muy solo, donde nadie, ni siquiera su titiritero le prestaba atención.
    #Que Nulla siempre ganaba la batalla de alguna u otra manera. Consumiendo a su titiritero y a las obras donde Musae trabajaba.
    #Padre lo odiaba.
    #Pero ya no, ahora que tiene un publico, ahora que su titiritero le presta atención. Padre no se preocupa por Nulla.
    #Despues de todo, ya está apunto de deshacerse de él.
    #Padre te pregunta si tienes alguna pregunta.
    #Algunas preguntas son acusatorias, pero Padre te dice que él ve a sus creaciones como un pintor ve a su obra. con amor.
    #Todo lo que hace es por amor al arte, a la comedia. Él es un director, no un padre o una madre.
    # Te confiesa que siente algo de pena por Septem, pero que está orgulloso también.
    #Que no le da pena que Septem se independice de él, despues de todo, esa era la idea desde el inicio.
    #Septem ha crecido para ser otro creador más bajo el mandato de otro titiritero: tú, si lo aceptas.
    #Lo mismo con Nulla, Nulla solo será libre si tú lo aceptas.
    #Padre te muestra sus mundos, te dice que está feliz con lo que tiene.
    #No importa que tan pequeño sean, todos lo hacen felíz.
    #Te muestra su mundo, magnum opus y te dice que Madre ha vuelto ahí.
    #Que su castigo ya ha terminado.
    #Al final, Padre te agradece todo el tiempo que le has concedido.
    #Te felicita por haber consumido su obra y por darle un pequeño espacio en tu memoria para existir.
    #Se despide de ti con otra rosa y te dice que posiblemente se vuelvan a ver.
    return












label rogar:
    scene negro with dissolve
    "...."
    creador "Te he vetado."
    creador "¡Ahora! para poder acceder a los epílogos desde cero. Tienes que pedirme disculpas."

$ click_count = 0  
label disculparse:



    menu:
        "Disculparse.":
            $ click_count += 1

            if click_count == 7:
                jump continuacion_rogar
            else:
                "..."
                creador "Vamos, hazlo otra vez~"
                jump disculparse

label continuacion_rogar:
    creador "Hmmm~"
    creador "Bien, te mereces tu menú del epílogo de vuelta~"
    $ persistent.rogar = False
    return
           
            



