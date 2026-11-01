# Declare characters used by this game.

default marioneta_encuento = False
default mensaje_guardado = None
label menupreguntas_septem2:
    menu:
        "Las manos de mi marioneta...":
            show s_biblioteca8_0
            septem "Eso no sería un problema si pudiera encontrar la solución rápido."
            septem "Mientras más días pasen, más se pudrirá tu marioneta."
            menu:
                "¿Pudrir?":
                    scene s_biblioteca9
                    septem "Mientras la usas, más agotas tu fuente de vida."
                    septem "Tú nunca sueltas a la marioneta para que se reponga."
                    show s_biblioteca8_0
                    septem "Hasta cuando tu marioneta duerme, estás conectada a ella."
                    septem "Haciendo que quites su tiempo de utilidad más rápido."

                "¿Hay algo que yo pueda hacer?":
                    scene s_biblioteca8_1
                    septem "No."
                    show s_biblioteca8_0
                    septem "Por eso tengo que buscar otra solución para la transfusión."
                    septem "Si no lo hago... estaremos condenados."
                    septem "Y tú te verás obligado a abandonar el 'juego'."
                    septem "Ya que la marioneta morirá."
            
            scene s_biblioteca8_1 
            septem "..."
            "Septem se quita la prenda que le cubre parte de su muñeca y brazo... por alguna extraña razón se siente ilegal ver aquello."
            "Su brazo tambien está siendo comido por el color negro que antes decoraban solo sus dedos."
            septem "Estamos en las mismas condiciones..."
            septem "Dame tu mano."
            show s_biblioteca8_2
            "No fue pregunta. Septem espera con su mano alzada a que le entregues tu mano..."
            "Con algo de miedo posas tu palma sobre la suya."
            hide s_biblioteca8_1
            show s_biblioteca6
            "El rubio atrapa tu mano y la aprieta mientras la examina."
            "Con su pulgar traza lineas imaginarias que se detienen de vez en cuando para luego trazar una nueva en otro lugar."
            "Desvías la mirada para poder centrarte en la cara del séptimo."
            "Sus ojos color cielo están mirando con mucha atención el movimiento de su dedo. y A pesar de la presión que su mano impone sobre la tuya, no sientes ni cosquillas."
            septem "¿Sientes eso?"
            menu:
                "No.":
                    pass
            septem "Hmm..."
            hide s_biblioteca6
            show s_biblioteca7
            "Una sutil sonrisa se posa en los labios de Septem, que te hace sentir un escalofrío recorrer tu cuerpo."
            "Poco a poco la presión va creciendo, pero no puedes quitar tu mano."
            "No le darás la satisfacción de ver tu terror, ni en tu cara ni en tus acciones."
            "Ya que no duele."
            "Septem aprieta cada vez más, lentamente pero de manera progresiva."
            "El sentimiento de presión de apoco se transforma en dolor."
            "Estás seguro de que tus huesos cederán en cualquier momento si es que no logras zafarte de su agarre."
            "Llega un punto en que no puedes aguantar más y tiras tu mano para hacerle notar que: ya basta."
            "Pero Septem no te deja."
            hide s_biblioteca7
            show s_biblioteca7_1
            septem "¿Pasa algo, [nombrejugador]?"
            menu:
                "Decirle a Septem que pare.":
                    septem "¿Hmmm?"
                    hide s_biblioteca7_1
                    show s_biblioteca8
                    "Septem sube la mirada para observar tu cara, sonriendo dulcemente, dejando de aumentar la presión, pero manteniéndola."
                    septem "Oh."
                    septem "Disculpa, me he pasado un poco."
                    "{sc=3}[nombrejugador]... gracias.{/sc}"
                
                "Dejar que Septem la rompa":
                    "Dejas que Septem te rompa la muñeca, porque quieres saber que pasará en el caso de que lo haga."
                    "{sc=3}...{/sc}"
                    "{sc=3}[nombrejugador]...{/sc}"
                    hide s_biblioteca7_1
                    show s_biblioteca8
                    "Septem sube la mirada para observar tu cara, sonriendo dulcemente, dejando de aumentar la presión, pero manteniéndola."
                    septem "Me gustaría que pudieras ver la cara que está poniendo tu marioneta ahora mismo."
                    septem "Realmente le duele y no quiere este destino que se le está imponiendo."
                    septem "Es casi como si fuera uno de los nuestros..."
                    septem "Pero aun así, no hará nada para cambiarlo, con tal de complacerte."
                    septem "..."
                    hide s_biblioteca8
                    show s_biblioteca6
                    septem "Me impresiona la convicción de tu marioneta, [nombrejugador]."
                    septem "Intenta cumplir cada uno de tus comandos, sin importar su integridad..."
                    septem "Tengo que darle ese reconocimiento."

            "Hay un breve silencio antes de que el rubio decida como seguir con esta interacción."
            scene s_bibliotecabeso2
            "Septem guia tu mano a su cara, sus labios rosando delicadamente tus nudillos."
            "Y te observa."
            septem "Me pregunto que expresión tendrás..."
            septem "¿Asco? ¿Verguenza? ¿Neutal? hmmm."
            show s_bibliotecabeso1
            "Septem sonrie y te planta un beso, un contacto tierno y delicado."
            scene s_biblioteca8_1
            "Sin más, Septem te suelta y se coloca nuevamente la prenda que le cubre el brazo."

            call menupreguntas_septem2 from _call_menupreguntas_septem2

    
        "Te ves fatal.":
            scene s_biblioteca9
            "Septem te mira con los ojos entrecerrados."
            scene s_biblioteca8_0
            septem "¿Yo?"
            septem "No."
            septem "Es culpa de este cuerpo mortal..."
            septem "Créeme, mi intención no es romperlo, pero estamos contra el tiempo."
            septem "...Cuando encuentre la solución. Lo dejaré descansar el tiempo que desee."
            call menupreguntas_septem2 from _call_menupreguntas_septem2_1

        "Acerca de Madre":
            "Le cuentas lo que pasó cuando dormías."
            scene s_biblioteca9
            "Septem te escucha sin interrumpir ni opinar. Mientras más explicas, la cara de Septem va tomando un aire de tristeza."
            "Aunque en cierto punto de tu explicación, Septem levanta la mano."
            "Pidiendo silenciosamente que te detengas."
            scene s_biblioteca8_0
            septem "Hablaremos de eso luego."
            septem "Tengo otras cosas que solucionar antes."
            septem "Cuando encuentre una manera de unirnos sin poner en peligro tu experiencia o la mía, solucionaremos el problema que tiene Madre."
            septem "Pero lo tendré en cuenta."
            call menupreguntas_septem2 from _call_menupreguntas_septem2_2
        

        "Despedirse.":
            scene s_biblioteca8_0
            septem "¿Eso fue todo?"
            "... momento."
            "una cosa más."
            menu:
                "Sobre unirnos en una transfusión":
                    "Se le ve afligido al escucharte."
                    show s_biblioteca9
                    "Se toma un tiempo antes de responder."
                    scene s_biblioteca8_1
                    septem "{size=*0.6}... no sé como resultará.{/size}"
                    "Septem habla tan despacio que te ha costado un poco entenderle. Antes de que puedas preguntarle, él se aclara la garganta para explicarse."
                    show s_biblioteca8_0
                    septem "Cuando te di uno de mis ojos, no resultó como yo esperaba."
                    septem "{b}Algo{b} dentro de esta cosa me prohíbe enlazarme contigo."
                    septem "Además,te ha quitado la poca libertad que tienes para controlar a la marioneta."
                    septem "Si hacemos la transfusión... no cumpliré con lo que te prometí y ambos seremos absorbidos por la marioneta si continuamos como estaba planeado..."
                    septem "Será un desastre."
                    septem "..."
                    "Septem guarda silencio por un largo rato. Y tú no sabes como rellenar ese silencio incómodo."
                    septem "Retírate."
                    scene habitacionrafael with dissolve
                    "Ni siquiera te da la oportunidad de tomar una decisión, pues te teletransporta a la pieza donde duermes."
                    return

        
                "Has hecho un buen trabajo hasta ahora.":
                    "..."
                    show s_biblioteca10
                    "Septem te mira frunciendo el ceño."
                    "Pero en su expresión hay algo más que no puedes identificar."
                    "Es como si estuviera teniendo un debate interno donde no puede ganar ni pensar en una reacción apta para esta situación."
                    "Definitivamente no se esperaba esto."
                    "{sc=3}Heh, toma eso anciano.{/sc}"
                    hide s_biblioteca10
                    show s_biblioteca11
                    "Septem abre la boca para gritar y seguramente hacer explotar todos tus órganos como si de globos rellenos de agua se tratasen."
                    "Te preparas para morir, tomando un último aliento."
                    septem "Vete."
                    septem "Vete de aquí."
                    septem "Antes de que te corte la cabeza."
                    scene habitacionseptem with dissolve
                    "Ni siquiera te da la oportunidad de tomar una decisión, pues te teletransporta a la pieza donde duermes."
                    "{sc=3}Heh, para la próxima podríamos llamarlo buen chico y ver como reacciona.{/sc}"
                    "{sc=3}Para molestarlo un poquito.{/sc}"
                    return
            
    
    return


label badend_septem9:
    "..."
    "No vas a entrar... Quizás que cosas sucedan si lo haces."
    "Así que, sin decir nada, caminas hacia atrás."
    scene pasilloseptem with dissolve
    "Llegas al pasillo."
    play music "audio/the_chillout_factory.WAV" fadein 2.0 volume 0.4
    septem "Te he dicho que pases."
    scene badendseptem with dissolve
    septem "Hoy no estoy para juegos. No voy a aceptar este comportamiento."
    septem "Tu desobediencia ya no es divertida."
    septem "Si realmente te tomas esto en serio, volverás."
    "Septem te agarra por la garganta y comienza a apretar sin cuidado."
    "Quitándote el aire de a poco, el sonríe."
    "BAD END: ..."
    $ MainMenu(confirm=False)()
    
return

label badendexplosion:
    "No colocas las manos, no te piensas quemar."
    scene negro with pixellate
    play music "audio/the_chillout_factory.WAV" fadein 2.0 volume 0.3
    "'Que lo haga Unum'.... es tu último pensamiento antes de escuchar un estruendo... como una explosión."
    "BAD END: Explosión."
    $ MainMenu(confirm=False)()

label badendseptemjardin:
    "Es ahora o nunca."
    "Ahora nadie te está vigilando, estás practicamente a unos cuantos metros de tu libertar."
    "Que importa los posibles problemas que tengas allá afuera por ser un humano. ¡Lo que importa es que eres libre!"
    play music "audio/the_chillout_factory.WAV" fadein 2.0 volume 0.4
    scene badendseptem with pixellate
    septem "Realmente eres imbécil..."
    "Septem te corta la cabeza."
    "BAD END: A metros de tu libertad."
    $ MainMenu(confirm=False)()

label septem_badend_insistir:
    septem "Tú no entiendes..."
    septem "¿O es que te lo estás buscando?"
    septem "Veo que entiendes a la fuerza."
    play music "audio/the_chillout_factory.WAV" fadein 2.0 volume 0.4
    scene badendpureseptem with pixellate
    "Septem toma una de tus manos, usando una fuerza que rompe y destroza tus huesos. Un dolor intenso explota en tu ser."
    "Es un dolor que no sabes bien como se origina, un dolor fantasma que se cuela en todo lo que puedes llamar tuyo."
    "Y es un dolor compartido... uno dolor que Septem también siente."
    "Pero él está decidido a seguir."
    "Luego es tu ojo."
    scene negro with dissolve
    "El cual es cerrado de golpe."
    septem "Vuelve cuando sepas respetar mi palabra."
    "No sabes bien lo que sucede luego."
    "Pero tu conexión con Septem se corta."
    $ MainMenu(confirm=False)()
return

label castigo:
    $ powerhungry += 5
    "Mirando con frialdad a la entidad, él chasquea los dedos."
    scene consejo3 with vpunch
    "Un líquido negro comienza a salir de la boca de la entidad."
    "Y el corazón de Septem comienza a latir con una rapidez preocupante. Dándose cuenta de que: realmente ha lastimado a uno de los suyos por primera vez."
    "Pero el arrepentimiento no llega al instante."
    "Todos dentro del lugar reaccionan con horror, incluso los Estandartes. Menos uno."
    "Sextam en cambio aprieta los labios y se encoje bajando la mirada."
    "Decepcionada."
    septem "Ya han sido dos ofensas. A la próxima, no solo tu lengua será la que arrancaré."
    duae "¡Andrómeda!"
    "El tono de Duae está entre una mezcla de miedo y reproche. Pero no se atreve a mover ni un músculo."
    "Mientras Andrómeda coloca ambas manos sobre su boca y mandíbula, Unum se levanta de su lugar para recargar sus manos en la mesa y observar con una curiosidad morbida como la entidad, llamada Andrómeda, escupe lo que parece ser sangre."
    scene reunion with dissolve
    show unum2blush at left with dissolve
    unum "¡Mierda, Septem! ¿¡Desde cuando puedes hacer eso?! HAHAHAHAHA INCREÍBLE."
    "Sus ojos se abren, como si una idea que anteriormente haya sido imposible, de la noche a la mañana se haya hecho realidad."
    hide unum2blush
    show unum2feliz at left
    unum "¿Podemos combatir? Por favor, por favor. POR FAVOR."
    show pureseptem3enojo
    septem "Unum siéntate. Ahora no quiero escuchar estupideces."
    hide unum2feliz and pureseptem3enojo with dissolve
    "El cuerpo de Unum cae reprentinamente sobre su asiento al mismo tiempo que Duae se levanta del suyo y agacha la cabeza."
    duae "Su santidad Septem--"
    scene consejo2a with dissolve
    "Septem levanta su mano, parando en seco el discurso de Duae."
    septem "Basta Duae, no es tu culpa que tu consejero no sepa como expresar respeto..."
    septem "Ahora, siéntense."
return




label menuexplorar3_nulla:
    menu:
        "Mirar los documentos del escritorio.":
            scene habitacionnulla with dissolve
            if mensaje_guardado is None:
                "Caminas al escritorio de la habitación. Al llegar allí, puedes observar como todos están ordenados, de manera casi complusiva."
                "Todas las hojas están perfectamente apiladas."
                "Ojeas algunas, pero ninguna te llama la atención."
                "Hasta que encuentras una pila con hojas en blanco y un bolígrafo."
                "...."
                "Dejar un mensaje para Nulla no estaría mal..."
                "¿No crees?"
                menu:
                    "Escribir algo.":
                        "Tomas el bolígrafo y mientras meditas lo que vas a escribir, dibujas garabatos en la esquina de la hoja."
                        $ mensaje_guardado = renpy.input(_("¿Qué quieres escribir?"), length=230)
                        "Miras tu mensaje por un momento y un pensamiento furtivo pasa por tu cabeza."
                        "Realmente esperas que Nulla lo pueda leer algún día..."
                    
                    "No escribir nada.":
                        "No..."
                        "No vale la pena."
                


            else:
                "Vas nuevamente al escritorio. Esperando a que tu mensaje no haya sido borrado y olvidado por las mecanicas básicas del juego."
                "Encuentras tu hoja encima de todos los papeles, esperando a ser leída."
                "Así que, lees lo que escribiste la última vez:"
                "[mensaje_guardado]"
                "Je..."

            jump menuexplorar3_nulla
        
        "Recorrer las habitaciones.":
            scene segundopiso with dissolve
            "Te paseas por toda la casa, recorriendo cada habitación en busca de algo que despierte tu curiosidad, algo que revele un poco más de él."
            "Pero pronto caes en la cuenta de que la casa de Nulla carece por completo de personalidad."
            "No hay decoraciones, fotografías, ni objetos que cuenten cómo era su vida antes de tu llegada."
            "Tampoco hay libros, ni señales de pasatiempos que alguna vez haya disfrutado en tiempos mejores..."
            "Todo se siente vacío, sin alma. Artificial."
            "Nulla tiene solo lo justo y necesario para existir."
            "Y, por alguna razón, eso te entristece un poco."
            "..."
            scene cocinanulla with dissolve
            "Caminas por la cocina..."
            scene cocinanulla with dissolve
            "Por la entrada de la casa."
            scene escaleranulla with dissolve
            "Y cerca de las escaleras."
            "No hay nada que capte tu atención."
            "...."
            "...."
            jump menuexplorar3_nulla
        
        "Ir afuera.":
            scene jardinnulla with dissolve
            "Afuera es frío y muy silencioso."
            "Como si hubiera helada ahora mismo y el lugar fuera solo una fotografía."
            "Nada se mueve y nada perturba el lugar."
            "Exepto tú."
            scene entradanulla with dissolve
            "Decides volver dentro de la casa cuando ya no aguantas más el frío."
            jump menuexplorar3_nulla
        
        "Terminar y buscar a Nulla":
            scene escaleranulla with dissolve
            "Caminas por toda la casa en busca de Nulla, te cuesta admitirlo pero te sorprende lo difícil que es de encontrar."
            show nulla1risa with dissolve
            "Y ahí está él."
            "Juras que ya pasaste por este lugar y él no estava ahí."
            "Tal vez está jugándote una broma."
            hide nulla1risa
            show nulla1coqueto
            nulla "¿Me extrañaste?"
            "Pregunta él, muy campante."
            menu:
                "No.":
                    hide nulla1coqueto
                    show nulla1disgusto
                    nulla "Ouch."
                
                "Sí.":
                    hide nulla1coqueto
                    show nulla2normal
                    "Sonríe complacido."
            hide nulla2normal
            hide nulla1disgusto
            scene cocinanulla with dissolve
            "Nulla te encamina a la cocina, enciende la tetera y busca un cuchillo junto con algunas frutas." 
            "Comienza a preparar fruta mientras tú lo observas. La habilidad que tiene con el cuchillo es admirable..."
            
            jump continuacion_nulla2
#EDITAR       
label menuexplorar_unum:
        menu:

            "Ir con los niños":
                scene palaciounum with dissolve
                "Buscas a los niños dentro de la residencia, pero solo encuentras remanentes de que estuvieron ahí. Una vasija rota más para la colección, uno de los cuadros rellados con lo que esperas sea pintura y así puedes seguir hasta mañana..."
                "En cambio, a ellos no los hallas por ninguna parte."
                scene jardinunum with dissolve
                "Sales con la esperanza de encontrarlos en el patio."
                "Tampoco están ahí."
                "Supones que deben estar en la residencia de las esposas de Unum."
                "... no sabes si será muy prudente ir allá."
                call menuexplorar_unum from _call_menuexplorar_unum
            "Ir a la residencia de las esposas de Unum":
                scene jardinunum with dissolve
                "Tus pasos son lentos. Temes que, si te apresuras, algo saldrá mal." 
                "No estás haciendo nada prohibido, al menos no de forma explícita; Unum nunca te ha dicho que no puedas venir aquí."
                scene jardin_chicas with dissolve
                "Sin embargo, a medida que te acercas, cada paso te saca una gota de sudor que recorre tu nuca."
                scene puerta_residencia with dissolve 
                "Finalmente, te detienes frente a una gran puerta cerrada, imponente, con grabados en la madera que hacen alegoría al sol."
                "Al levantar la mano para tocarla, algo en tu estómago se revuelve. Un nudo que asciende hasta la garganta, que no te permite pensar correctamente." 
                "El miedo entra en tu cuerpo, apretando tu suave piel. Un cuerpo jugoso, que no es nada más que un trozo de carne esperando a ser comido"
                scene puerta_residencia2 with dissolve 
                "Estás a punto de darte la vuelta cuando, de pronto, la puerta se abre de par en par."
                show solaris_normal with dissolve
                "Es Solaris. Está sonriendo. Por un segundo, esa sonrisa te recuerda a la de Unum... por los dientes. Brillantes. Perfectos. Demasiado visibles."
                solaris "¿Uh?"
                solaris "¿[nombrejugador]?"
                hide solaris_normal
                show solaris_enojo
                "Solaris parece sinceramente sorprendida. Deja de sonreír apenas reconoce quien eres tú."
                "El aire a su alrededor cambia. Puedes verlo sin problema: su cuerpo se tensa, y la sonrisa que intenta rearmar no le sale del todo bien." 
                "Lo que resulta en una mueca incómoda. Demasiado diente, muy poca expresión en los ojos."
                solaris "No puedes entrar aquí sin permiso."
                solaris "Es peligroso. Unum aún no ha regresado con—"
                solaris "Uhhh—"
                "Se interrumpe a sí misma. Aprieta los labios hasta formar una delgada línea y desvía la mirada hacia un costado, como si esperara que algo o alguien la salve de tener que continuar hablando."
                solaris "¡Noor! ¡Shams! ¡Han venido a buscarlos!"
                solaris "¡Ya les dije que deben avisar antes de aparecer aquí, par de sabandijas!"
                "Los niños no tardan en salir, con ambas colas conectadas resitando disculpas vacías a la mujer mientras ríen sin un rastro de vengüenza alguna en sus cuerpos."
                solaris "¡Si lo hacen denuevo, le diré a Ignis que les prohiba la entrada!"
                "Dice forzando una voz dura, aunque no convence a nadie. Luego de eso te mira, y te pide disculpas antes de cerrar la puerta en tu cara."
                "Tú estás atónito."
                "No sabes que pensar realmente."
                "Sientes pena y rechazo."
                scene jardin_chicas with dissolve
                "Pero los niños no te dan tiempo a poner en orden tus pensamientos, ya que te jalan de las mangas en dirección a la residencia de Unum."
                "Todo mientras te cuentan lo que hicieron en casa de las estrellas del cinturón de Orión."
                "De lo poco que puedes captar y procesar, es que Noor aprendió a bajar su intensidad, sea lo que eso signifique."
                pass
            "Mirar las pinturas":
                scene pasillounum with dissolve
                "Paseas por los pasillos observando las pinturas que Unum tiene en su residencia."
                "Y te das cuenta de que todas siguen un patrón muy especifico: Todas muestran cuerpos humanos en diferentes posiciones y expresiones."
                "Hay mucho cuidado en el uso de sombras, un contraste entre la luz y la sombra que es imposible de pasar por alto."
                "Hay algunas que te causan un poco de grima, siendo grotescas al punto de causar algo de incomodidad."
                "No te quieres imaginar como se verán en la noche."
                "No gracias."
                call menuexplorar_unum from _call_menuexplorar_unum_1
        return      
        

#label ataque_noor:

#    menu:
#        "¡Noor, para!":
#            jump badend_noor

#        "{glitch=30.0}{color=ffffff}¡SIRIUS!{glitch}" if click_count >= 7:
#            $ sirius_nombre = True
#            nj "¡SIRUS, para!"
#            return

#        "Tratar de decir su nombre de origen.":
#            if click_count in click_texts:
#                "[click_texts[click_count]]"  

#            elif click_count >= 10:
#                jump badend_noor

#            $ click_count += 1
#            call ataque_noor from _call_ataque_noor

#    return

#EDITAR
label badend_noor:
    "Noor hace caso omiso a tus palabras."
    "Poco a poco, mueres a manos de tu propio hijo."
    scene negro with dissolve
    ".........."
    "BAD END: Los nombres aquí son importantes."
    $ MainMenu(confirm=False)()
#Que mirá bobo
#Salí de aquí bobo

label finalacto25:
    "..."
return



label cuadro:
    nulla "..."
    show para_nulla with dissolve
    nulla "Realmente lo has hecho..."
    nulla "Eres increible, [nombrejugador]."
    jump continuacion_nulla
    
    

return




label ataque_noor:

    menu:
        "¡Noor, para!":
            jump badend_noor

        "{glitch=30.0}{color=ffffff}¡SIRIUS!{glitch}" if click_count >= 5:
            $ sirius_nombre = True
            nj "¡SIRIUS, para!"
            jump continuacion_unum

        "Tratar de decir su nombre de origen.":
            if click_count == 0:
                "Intentas gritar su nombre. Pero no puedes.\n\n{glitch=30.0}{size=*0.7}Intenta de nuevo.{glitch}{/size}"

            elif click_count == 1:
                "Forcejeas para poder liberarte, usando tus manos en su cara, tratando de empujarlo hacía atrás pero es imposible. En tu desesperación intentas poner distancia entre él y tú con tus piernas.\nEso funciona.\n{glitch=30.0}{size=*0.7}¡Otra vez!{glitch}{/size}"

            elif click_count == 2:
                "Noor no desea ganar, y vuelve a tomar posición, esta vez con sus manos sobre tu estómago.\n\n{glitch=30.0}{color=ffffff}OTRAAAAA.{glitch}"

            elif click_count == 3:
                "Su desesperación y su hambre lo ciega de tal manera que tus gritos no llegan a sus oídos, sumido en un trance que no puedes romper. Sus uñas rompen la ropa, llegando a la carne.\n{glitch=30.0}{color=ffffff}Dale, con más fuerzaaaa.{glitch}{/color}"

            elif click_count == 4:
                "Agarra la piel en su puño, con el objetivo claro: destriparte y comer tus órganos.\n\n{glitch=30.0}Una mássss.{glitch}"

            elif click_count == 5:
                "{glitch=30.0}{color=ffffff}PFFFF en serio sigues haciendo click?{glitch}"

            elif click_count == 6:
                "{glitch=30.0}{color=ffffff}Ah, ya veo, quieres leerme por un poquito más, lindooo..........{glitch}\n\n{glitch=30.0}{color=ffffff}Te estás quedando sin tiempoooo....{glitch}{/color}"

            elif click_count >= 10:
                jump badend_noor

            $ click_count += 1
            call ataque_noor from _call_ataque_noor



label s_preguntas_act3:
    scene ps_mesa_normal
    menu:
        "Preguntar por Rafael.":
            show ps_mesa_sad
            septem "Puedo hacerle un corazón que funcione... pero necesito arreglar el Jardín antes de hacerlo despertar."
            septem "No quiero traerlo de vuelta a un mundo que no está listo aún."
            menu:
                "Ya quiero verlo despierto.":
                    hide ps_mesa_sad
                    show ps_mesa_normal
                    septem "Sí..."
                    septem "Yo también."
                    pass

                "¿Vivirá aquí después de que despierte?":
                    septem "..."
                    hide ps_mesa_sad
                    show ps_mesa_serio
                    septem "No lo creo."
                    hide ps_mesa_serio
                    show ps_mesa_sad
                    "Baja la mirada, incapaz de darte la cara."
                    septem "Los humanos deben ir con los humanos..."
                    septem "Él perderá todos sus rangos una vez que se desligue completamente de mí."
                    septem "Vivirá como ellos, y morirá como ellos..."
                    pass
            "....."
            jump s_preguntas_act3
        

        "Preguntar por Septem.":
            show ps_mesa_sad
            "Le preguntas por cómo se encuentra. Y cuando él te mira con cara de no entender tu pregunta del todo te explicas diciendo que quieres saber como se siente emocionalmente."
            "Que quieres saber si hay algo que le preocupa o algo que quiera compartir contigo para sentirse más liberado. Evitas decir que lo has sentido en tus sueños, para no ponerlo de malas o hacerlo sentir pequeño y expuesto."
            "Septem frunce el ceño como primera respuesta, sin saber cómo tomarse tu curiosidad, y bebe un poco de su copa antes de responder."
            "Al terminar de dar su trago, se aclara la garganta."
            hide ps_mesa_sad
            show ps_mesa_hablando
            septem "Estoy bien."
            hide ps_mesa_hablando
            show ps_mesa_normal
            "Es lo único que te ofrece. Tú sabes que hay más que solo esa respuesta vaga y ensayada, pero no sabes cómo hacerlo escupir todo lo que le persigue en su cabeza."
            "Así que aplicas el silencio, esperando que aquello haga que Septem quiera rellenarlo con más palabras."
            "..."
            "....?"
            "No funciona. Septem no tiene el más mínimo sentido de la incomodidad o presión social en rellenar el silencio incómodo con palabras."
            "Hasta tiene el descaro de sonreír levemente, a sabiendas de que no obtendrás lo que buscas."
            menu:
                "Guardar silencio.":
                    "Septem sigue bebiendo de su copa sin darle importancia al silencio que lo acompaña."
                    "Es mejor así, te consuelas mentalmente."
                
                "Cuestionar su respuesta.":
                    "Sabes que es riesgoso, pero él jamás te ha dicho que no sigas preguntando. ¡Además se está burlando de ti con esa sonrisa que tiene pegada a los labios!"
                    "Se está haciendo él de rogar, no tienes suficientes pruebas, más que esa maldita sonrisa, pero tampoco dudas."
                    "Así qué lo cuestionas, formulando preguntas para hacerlo hablar más."
                    hide ps_mesa_normal
                    show ps_mesa_serio
                    septem "¿Realmente te intesesa saber?"
                    hide ps_mesa_serio
                    show ps_mesa_sad
                    "Tú respondes que sí, que si no te interesará ni siquiera le preguntarías nuevamente. Eso gana una expresión de sorpresa por parte de Septem."
                    hide ps_mesa_sad
                    show ps_mesa_serio
                    septem "Tengo algunas dudas de lo que está por venir..."
                    septem "Los cambios no me gustan... romper las reglas tampoco..."
                    septem "Hoy haremos todo lo que me disgusta."
                    septem "Pero hay que hacerlo."
            "..."
            jump s_preguntas_act3
#EDITAR        
        "Preguntar por tu cuerpo.":
            show ps_mesa_serio
            septem "¿Qué quieres saber?"
            menu:
                "Mis manos...":
                    hide ps_mesa_serio
                    show ps_mesa_hablando
                    septem "Es la única parte que no se puede cambiar."
                    septem "Toda la energía que compartes conmigo se acumula ahí."
                    hide ps_mesa_hablando
                    show ps_mesa_sad
                    septem "..."
                    "Septem siente la duda invadir tus pensamientos."
                    hide ps_mesa_sad
                    show ps_mesa_normal
                    septem "Puedo ver evitar que la energía no se manifieste así... cambiarlo."
                    septem "No hay problema en eso, pero---"
                    hide ps_mesa_normal
                    show ps_mesa_hablando
                    septem "Con estas manos que tienes es más fácil identificarte como mío."
                    hide ps_mesa_hablando
                    show ps_mesa_blush
                    septem "No habrá humano o Dios que dude de nuestra unión."
                
                "Acerca de mi mortalidad":
                    hide ps_mesa_serio
                    show ps_mesa_hablando
                    septem "Eres inmortal hasta que yo deje de permitirlo."
                    hide ps_mesa_hablando
                    show ps_mesa_normal
                    "Septem sonríe con ternura, ignorando lo brutal de sus propias palabras."
                    "Pasan los segundos, y nada. Septem no se retracta o termina su comentario con algún chiste liviano..."
                    hide ps_mesa_normal
                    show ps_mesa_hablando
                    septem "No te preocupes, [nombrejugador], no pienso hacer eso."
                    hide ps_mesa_hablando
                    show ps_mesa_blush
                    septem "Eres vital para mí. Jamás dejaría que tu cuerpo vasija muera."
                    septem "Aunque---"
                    septem "Si llega el momento en que te hartes de este cuerpo, podría fabricar otro con el que te sientas más cómodo."
            
                "Acerca de dormir o comer...":
                    hide ps_mesa_serio
                    show ps_mesa_normal
                    septem "Mhhm---"
                    "Septem suelta una risa que no logra escapar de sus labios, los cuales mantiene sellados."
                    hide ps_mesa_normal
                    show ps_mesa_hablando
                    septem "Te recomiendo seguir la dieta y las rutinas de un cuerpo mortal..."
                    septem "Eres inmortal, pero sigues atado a lo mundano de la vida humana."
                    hide ps_mesa_hablando
                    show ps_mesa_blush
                    septem "Sentirás hambre y sueño. Sufrirás si no sacias tu sed."
                    septem "Pero no podrás morir de ello."
                    "Su sonrisa es inquietante. Algo en sus ojos brilla con una chispa que solo puedes llamarla placer."
                    "Septem disfruta de esto."
            "...."

            jump s_preguntas_act3
        
        "Dejar de preguntar.":
            jump acto3_septem_continuacion



label act3_explorar_septem:
    play music "audio/calamity.WAV" fadeout 1.0 fadein 2.0 volume 0.4

    menu:
    
        "Ir al jardín.":
            scene jardinseptem with dissolve
            "Sales directo al jardín por un poco de aire fresco."
            "Temes que las telas de tu túnica se ensucien por lo que te quedas cerca de la entrada del templo, donde no hay tierra o pasto."
            "El solo pensar que te puedes tropezar en la tierra o manchar las telas que cuelgan de tu cuerpo te genera estrés. No te gustaría presentarte ante todo el Jardín con tu ropa manchada o rota."
            "Las primeras impresiones importan, más cuando eres una figura importante."
            "Aunque, si bien Septem podría darte otro conjunto, quieres demostrarle que tú puedes ser elegante y cuidadoso también."
            "Manchar estas ropas sería como fallar en ello."
            "..."
            scene negro with dissolve
            "Respiras hondo, cerrando los ojos y canalizando tranquilidad. La obtienes con el sonido de la brisa del lugar, junto con el correr del agua."
            scene septem_jardin_place with dissolve
            "Al abrir los ojos, tu mirada cae en las columnas de piedra que están más allá de la cerca de árboles."
            "Quieres ir allí y descubrir que es lo que esconde... recuerdas que Septem no quiso ir a ese lugar cuando lo señalaste."
            "Hum, luego de la ceremonia le preguntarás si te acompaña allá."
            "...."
            jump act3_explorar_septem
        
# EDITAR IMPORTANTE 
        "Caminar por los pasillos." if marioneta_encuento == False:

            scene pasilloseptem with dissolve

            "Caminas por los pasillos del templo. Al ser una distancia larga entre cada pasillo, tiendes a tropezar con las telas de tu túnica que se enredan en tus pies."
            "Es algo que no puedes evitar. No estás acostumbrado a caminar largas distancias con ropaje que toca y se desliza por el suelo con cada paso que das."
            "Tu caminata es poco productiva, los pasillos no tienen nada nuevo que agregar. Nada nuevo que mirar o conocer."
            if necesitasanulla == True:
                
                play music "audio/meeting.mp3" fadein 2.0 volume 0.2
                "Estás por desistir tu exploración en los pasillos cuando sientes que algo te llama. No es una voz como tal..."
                "Es una sensación que llama a todo tu cuerpo a ponerse alerta y a prestar atención a lo que te rodea. Como si te tiraran de la manga de tu túnica, pidiendo que pares y escuches."
                "..."
                scene negro with dissolve

                centered "{glitch=30.0}{color=ffffff}{b}[nombrejugador]...{b}{/color}"
                "¿¡!?"
                scene pasilloseptem with dissolve
                
                "Tu nombre ha sido llamado por una voz que reconoces muy bien..."
                "..."
                scene negro with dissolve
                
                centered "{glitch=30.0}{color=ffffff}{b}[nombrejugador]...{b}{/color}"
                scene pasilloseptem with dissolve

                "Esperas por un largo tiempo para que te diga otra cosa, pero eso no sucede, e incluso, su voz se siente más lejana."
                "No quieres perder esa voz, no quieres dejar que él se vaya. Después de todo, tú mismo has dicho que lo necesitabas."
                "Nulla..."
                menu:
                    "Necesitas a Nulla.":
                        "Sí..."
                    "Necesitas a tu marioneta.":
                        "Necesitas a tu marioneta... y probablemente él sepa que le ha pasado. Te rehusar a creer que ha muerto. Debe estar por ahí, junto con el dueño del vacío."
                
                "Serás algo lento, pero tonto no eres. Nulla te está llamando y necesitas encontrarlo."
                "Caminas siguiendo su llamado."
                "En ciertas ocasiones lo sientes cerca, para luego darte cuenta de que mientras más caminas, más te alejas."
                "Es como jugar al juego del 'Frío o Caliente', solo que más difícil porque las pistas no están tan claras y dependes solo de una voz que se esfuma cuando cometes un error."
                
                scene puerta with dissolve

                "Te toma un tiempo para llegar a tu destino... es una puerta entreabierta a la que entras sin chistar."
                scene cuartonegro 
                show restos
                with dissolve
                "Hay algo dentro del cuarto... algo que se mueve como si respirase y que no debería estar ahí."
                "El pánico te agarra de los pies y te obliga a salir de la habitación sin siquiera procesar que es lo que acabas de ver."
                "Pero, tus pies se anclan en el suelo, atrapándote en el lugar. No importa cuanto te muevas o luches por liberarte, no hay caso. No tienes como salir de aquí."
                el "[nombrejugador]..."
                "La masa extraña te llama y lloriquea."
                "Su voz es una horripilante combinación entre la voz de Nulla y tuya, pero sin llegar a ser una copia exacta de ellas."
                "Al mirarla con detención te das cuenta de que reconoces lo que representa. Lo has vivido, lo has tocado, has pasado tiempo con ello."
                "Es tu marioneta... o lo que queda de ella."
                "Sus quejidos son como los de un bebé. Tiene miedo y necesita de ti."
                "Necesita que la tomes."
                $ marioneta_encuento = True
                #EDITAR !!!!!
                menu:
                    "Tomarla.":
                        "La tomas."
                        "La masa se pega a ti. Te atrapa, envolviendo sus tentáculos."
                        jump act3_s_badendnulla
                        
                    
                    "Salir de ahí.":
                        "Te retuerces para escapar, con todas tus fuerzas."
                        "La masa parece avanzar, buscándote, buscando tocarte."
                        "Comienzas a lloriquear, aterrado de lo que te pueda hacer esta cosa."
                        "Solo unos centímetros más y aquello te comerá... o peor, tomará control de ti."
                        scene blanco with pixellate
                        septem "Con que aquí estaba..."
                        "La voz de Septem se instala en el lugar, imponente y tranquila. Suelta un largo suspiro antes de continuar."
                        septem "Reconozco que me demoré porque quería ver que hacías."
                        septem "Me disculpo si te aterraste."

                        play sound "audio/huesoroto.mp3"
                        $ persistent.nulla_symbol = False
                        $ persistent.septem_symbol = True
                        $ persistent.septem_symbol2 = True

                        septem "..."
                        septem "Bien. Es momento que salga de aquí."
                        septem "Ya he eliminado a esa abominación."
                        menu:
                            "Pero---":
                                septem "Ah no, no, no. Es peligroso."
                                septem "Y no me voy a arriesgar más."
                            "...":
                                pass
                        septem "No entrarás más ahí..."
                        septem "Ve a pasar el tiempo en otro lugar."
                        septem "Si te aburres, ven conmigo."
                        $ necesitasanulla = False
                        #Septem al rescate.
                        jump act3_explorar_septem

            
            else:
                "Recorres los pasillos una vez más... ya no encuentras la puerta que da a la habitación con el cuarto oscuro..."
                "Extraño... ¿Será que Septem la ha bloqueado de alguna manera?"
                jump act3_explorar_septem
#En la exploración, sientes que algo te llama a la habitación del vacío. Al entrar, tu cuerpo emite luz propia, iluminando la habitación lo sificiente como para captar una pequeña cosa en la esquina.
#Es lo que queda de la marioneta, un ojito que mira con miedo y te llama.
#Te ruega para que lo tomes y te unas con él. Si lo tomas, sale Nulla del ojo y te lleva a su ruta o activa un final malo (nulla aprovecha tu nuevo poder que te conecta con Septem y consume todo.)
#Si ignoras el ojo o si te demoras al entablar conversación con él, llega Septem. Y lo elimina. Dejándote sin la posibilidad de encontrar a Nulla nuevamente, ya que septem clausura la habitación.
            "...."
            jump act3_explorar_septem
        

        "Ir a ver a Rafael.":
            scene temploseptem with dissolve
            
            "..."
            
            scene puerta with dissolve
            
            "Caminas hasta llegar a la puerta que aísla a Rafael del resto del templo."
            
            scene habitacionrafael with dissolve   
            
            "Entras sin restricción aparente: la puerta está desbloqueada, no hay fuerza invisible que te impida entrar en la habitación, y el lugar te recibe con una cálida energía."
            "En la cama está Rafael. Te acercas a paso lento, con miedo a despertarlo." 
            "Sabes que es imposible, pero no puedes evitar en pensar que estás infringiendo en alguna regla que Septem ha dictaminado sin informarte."
            
            scene rafael_dormido with dissolve

            "Te quedas a un costado de la cama. Sabes lo suficiente de espacio personal y comportamiento social básico como para no subirte a la cama e invadir su espacio personal."
            "Lo observas un buen rato."
            "Te da pena verlo sin reaccionar, a sabiendas de que no está dormido ni muerto. Su estado es incierto, a lo único que podrías asimilarlo es a un estado de pausa donde lo único que hace su cuerpo es respirar."
            "No hay existencia de micro-movimientos que pasan en el sueño o expresiones de dolor."
            "Te quedas para acompañar a esta alma atrapada en un cuerpo que no responde. Desconoces si puede oír lo que pasa a su alrededor, por lo que no te atreves a hablarle."
            "Los minutos pasan...."
            "Cuando crees que ha sido suficiente, abandonas el lugar." 
            scene temploseptem with dissolve
            "Te preguntas cuando podrás ver a Rafael activo y con un cuerpo que solo le pertenezca a él."
            jump act3_explorar_septem
        

        "Ir a ver a Septem."if latin == False:
            "Quieres verlo y si Septem necesita más tiempo solo, ya que te lo diría. Jamás te prohibió ir a visitarlo a la biblioteca."
            "Además, quieres mostrarle cómo te queda el conjunto de ropa que él te ha elegido." 
            "Entonces, es {b}muy{b} necesario que lo veas antes de que sea el mediodía, ya que necesitas su opinión."
            
            scene pasilloseptem2 with dissolve
            
            "Subes las escaleras cuidando tus pasos. Mirando donde caen tus pies en cada escalón. Se te dificulta un poco por lo largo de la túnica, que te impide ver dónde aterriza cada pie."
            "Cuando llegas al último escalón, celebras en silencio tu logro. Estas ropas no fueron hechas para moverse como uno lo hace cotidianamente. Posiblemente fueron hechas para sentarse y verse bonito."
            "Como una muñeca de mostrador... bien cuidada y destinada solamente a ser observada desde el cristal. Una belleza perpetua que no alcanza a tener un propósito más grande que aquello."
            "Huh..."
            "Decides dejar ese pensamiento fuera de tu cabeza. No vale la pena ocasionar una jaqueca con pensar en todas posibilidades que no puedes controlar por ahora..."
            
            scene puerta with dissolve

            "Te detienes en frente de la entrada de la biblioteca."
            "Te cuestionas si debes entrar... tal vez Septem quiera tener un momento sin tu presencia."
            "La puerta es la única barrera que hay entre tú y él. Solo tienes que levantar la mano y llamar a la puerta."
            "Te preparas para tocar la puerta, pero la voz de Septem te hace pausar."
            septem "Pasa."
            "Tu estómago da un vuelco al escuchar su voz. Si bien es un comando, tú no tienes la obligación de cumplirlo bajo obligaciones de reglas que aún no entiendes."
            "No ha dicho tu nombre, por lo que eres libre de tomar la decisión de si pasar o no."
            "Te preguntas que pasaría si no lo haces."
            menu:
                "No entrar.":
                    septem "¿Has cambiado de opinión?"
                    septem "Parecías muy decidido a venir antes de llegar aquí."
                    "Septem solo ríe, divertido con tu cambio tan repentino en tu actitud... su risa casi se siente como una burla por su parte."
                    septem "Recuerda de que tenemos que salir al mediodía."
                    septem "No te vayas tan lejos. Este lugar es más grande de lo que crees."
                    call act3_explorar_septem from _call_act3_explorar_septem
                
                "Entrar.":
                    pass

            scene biblioteca3 with dissolve

            "La puerta se abre antes de que puedas tocar el pomo y empujar."
            "Dentro de la biblioteca, Septem se encuentra al frente del ventanal, devolviéndote la mirada. Sus manos yacen entrelazadas detrás de su espalda, con una postura anormalmente recta."
            "Te esperabas encontrarlo sentado en su escritorio, leyendo algo con el semblante serio, tal vez con las cejas fruncidas y una pequeña mueca en tu boca."
            "Verlo ahí te confirma que debe haber estado mirando por la ventana antes de que entraras."
            septem "Ven, siéntate."
            scene bibliotecaseptem with dissolve
            
            
            "Rompe el silencio luego de ver que te has quedado pasmado en la puerta, sin saber que hacer. Septem corre la silla del escritorio, donde él se sienta, ofreciendo el lugar para ti."
            "Avanzas y te sientas con cuidado en la silla."
            show pureseptem2risa with dissolve

            septem "Te queda bien."

            hide pureseptem2risa
            show pureseptem1sonrisa

            "Cuando le miras para entender a que se refiere, Septem agrega señalando con la mano en tu dirección."
            
            hide pureseptem1sonrisa
            show pureseptem2feliz

            septem "Tus vestimentas."
            hide pureseptem2feliz

            "Oh... sientes tu cara enrojecer..." 
            "Te encojes en la silla, no sabiendo que hacer con el cumplido que te ha hecho Septem. Te obligas a decir un 'gracias' que suena ahogado, delatando tu nerviosismo."
            "Septem se acerca un poco más a ti, invadiendo tu espacio personal por un segundo, antes de retomar la distancia previa con una de tus mangas en la mano."
            scene libros2 with dissolve
            show act3_s3d with dissolve
            
            septem "Las mangas se han ensuciado un poco."
            "Dice él examinando la tela. Pasa sus dedos por cada hebra que compone la manga, acariciando con suavidad."
            
            hide act3_s3d
            show act3_s3c
            
            septem "Al parecer las hice muy largas para ti."
            "Sientes su enojo subir por tu tráquea."
            septem "Las arrastras al caminar."
            
            hide act3_s3c
            show act3_s3e
            
            "Las mangas se han ensuciado porque son en extremo largas, claro. No es tu culpa, pero parte de ti espera que Septem te dé un sermón por ensuciar las ropas que te ha cedido, como mínimo."
            "No lo puedes evitar. Más cuando sientes como su enojo bombea por tu sangre."
            "Él es muy severo con su juicio y expectativas con el resto de las entidades que interactúa... y tú no puedes ser la excepción..."
            
            scene negro with vpunch
            
            "El tirón en tu manga hace que cierres los ojos con fuerza."
            septem "..."
            septem "Listo."
            "Al no sentir nada en tu cuerpo parecido al dolor, abres tus ojos."
            
            scene libros2 with dissolve
            
            "Lo primero vez es la mano de Septem con la mitad de tu manga, perfectamente cortada."
            
            show act3_s3c with dissolve
            
            septem "Ese error no volverá a cometerse."

            hide act3_s3c
            show act3_s3d

            septem "Tus próximas vestimentas no tendrán esa falla, mi salvador."
            
            hide act3_s3d
            show act3_s3e

            "Ah..."
            "El enojo que estabas sintiendo era por su error... no el tuyo."
            "No sabes si eso es malo y bueno..."
            
            scene biblioteca2 with dissolve

            "Pasas el tiempo junto con Septem en la biblioteca. Él te trae un libro que deja en el escritorio. Es grande, de esos que hacen un ruido seco y fuerte cuando los dejas caer en la mesa."
            "Mientras miras el libro, Septem opta por quedarse erguido detrás de tu silla."
            septem "Un líder competente debe saber el idioma de su gente."
            "Escuchas su voz detrás se tu oreja, tan cerca que los vellos de tus brazos se erizan al percibir su aliento cerca de tu cuello." 
            "No puedes evitar girar tu cabeza para comprobar la distancia que existe entre tú y él."
            
            show act3_s4a with dissolve

            "Un pedazo de alma sale por tu boca cuando te encuentras con su cara a centímetros de ti, asomándose por tu hombro derecho."
            "Septem te sostiene la mirada, sin reacción aparente, y continúa."
            hide act3_s4a
            show act3_s4
            septem "Quien dirige la palabra, debe saber leerla y hablarla."
            septem "La lengua madre del Jardín es el latín."
            septem "Tú la usarás para invocar y comandar."
            
            hide act3_s4
            show act3_s4a

            "Una de sus manos se desliza por tu brazo hasta llegar a tu cuello. Sin apretar su agarre, su dedo índice marca y traza la arteria que se encuentra al lado izquierdo."
            "Lo hace lento, buscando el bombeo de la sangre que llevan tus venas. Al tragar saliva, Septem siente el movimiento de tu garganta, y aprieta el agarre un poco más, escapándosele un suspiro..."
            "Ahora te es imposible ignorar como sus dedos se clavan en tu piel."
            septem "El tono al nombrar las palabras tiene que ser exacto. Un solo flaqueo en el, rompe la invocación."
            "..."
            septem "Abre el libro en la página veinticuatro."
            scene silabario with dissolve

            "Lo haces como puedes. Tu cabeza está en todos lados menos en la finalidad de la tarea y estás más que seguro que nada de lo que hagas o aprendas se quedará realmente contigo después de esto."
            "Hay un montón de sensaciones y sentimientos que se ebullen en tu cuerpo, pero el miedo no es una de ellas."
            "Y Septem lo sabe."
            septem "No te distraigas."
            "Su llamado de atención no hace más que quieras maldecirlo por ponerte en esta situación."
            
            scene biblioteca2 
            show act3_s4b
            with dissolve

            septem "Lo primero que debemos saber antes de hacer una invocación es a quien te refieres."
            septem "Sea un tú, un yo o un nosotros."
            "Con la mano disponible, Septem te muestra donde salen esas palabras y te hace repetirlas en latín. Cuando detecta que tu voz se rompe o flaquea, sus dedos ayudan apretando o soltando tu garganta para dejar salir la voz justo como él quiere."
            "Así que para eso ha puesto su mano ahí..."
            septem "Cuando pedimos algo que solo te involucre a ti, debes decir---"
            "Su cuerpo se acerca más al tuyo, rozando tu hombro con su pecho, tomando la oportunidad de colocar su boca directamente en tu oído. Resguardando sus palabras solo para ti, como si alguien más pudiese escuchar y robarte esas palabras de ti."
            septem "{i}Sub potestate quae mihi conceditur ego faciam...{i} \n {size=*0.6}Bajo el poder que me confiere,       yo hare.{/size}"
            "Las palabras que salen de su boca son desconocidas, pero las entiendes de alguna manera. El problema reside en poder imitar su vocalización..."
            "Dudas que lo puedas hacer a la primera, sin tropezar con la lengua al soltar todas las palabras en una frase."
            septem "Repite."
            septem "{i}Sub potestate quae mihi conceditur ego faciam...{i} \n {size=*0.6}Bajo el poder que me confiere,       yo hare.{/size}"
            
            scene biblioteca2 with dissolve

            "Lo intentas una vez, sin lograrlo del todo. Dos veces, te ahogas con tu propia saliva... que Humillante. A la tercera, ya tienes a Septem apretando tu garganta para sacar correctamente las vibraciones de cada comando."
            "Él es estricto y serio, pero cuando ve que te frustras y refunfuñas como un gato enojado, no puede evitar soltar una pequeña risa que oculta con la mano."
            "Intentas nuevamente. Ahora la lengua la tienes suelta de tanto pronunciar cada palabra, lo te permite sacarlas de tu boca con más fluidez"
            "Tu avance no pasa desapercibido. Septem se encarga de reconocerlo cada vez que lo haces bien o cuando vas por buen camino."            
            "Se ríe cuando fallas, pero no es una risa burlona. No. Es una risa que late con ternura al verte intentarlo, y desborda orgullo al ver progreso en tu pronunciación."
            septem "Ahora. Veamos que si has prestado atención realmente."
            "Septem suelta una risa jugetona justo detrás de tu oreja."
            menu:
                "Okay.":
                    jump claseslatin
            




            


















        "Esperar al mediodía."if latin == True: 
            "No queda otra que esperar..." 
            "Sabes que de mediodía cuando la voz de Septem te llama por tu nombre, haciendo que todo tu cuerpo se enderece." 
            "No esperas mucho para apreciar como su cuerpo se materializa frente de ti. Con esa apariencia tan refinada y gloriosa que no permite la aparición alguna imperfección." 
            "Septem te pide que camines con él hasta la entrada del templo. Te espera cuando nota que vas atrás, siempre intentando ir a la par tus pasos."   
            jump acto3_septem_continuacion2



label explorar_unum_act3:
    scene salchichas with dissolve
    menu:
        "Buscar a Noor.":
            "Sabes que Noor se ha ido al patio, lo conoces tan bien que no te cabe duda de ello."
            "Así que vas en su búsqueda."
            #cambio de escena
            scene jardin_chicas with dissolve
            "Apenas sales de la residencia, y ya lo divisas a lo lejos."
            "Se encuentra acostado en el suelo, dormitando con ambos brazos encima de su estómago, en posición de descanso. Su cola barre el suelo en un serpenteo constante, buscando cada roce."
            scene noor_sol with dissolve
            "Se le ve tan agusto que decides no molestarlo con acercarte. Por lo que lo miras de lejos."
            show noor_sol2 
            "Él nota tu presencia, su mirada te lo confirma."
            noor "Ven."
            "Te pide, palpando el suelo."
            "Vas sin apuro, aunque desearías ir corriendo para saltar en sus brazos y acurrucarte con tu bebé."
            "Pero te aguantas... Noor ya está grande, no quiere ser tratado como un bebé."
            "..."
            "Te recuestas como puedes a su lado. Copias la misma pose que tiene, mirando al cielo con las manos descansando encima del vientre."
            hide noor_sol2
            show noor_sol
            "Escuchar su respiración te llena de calma, es tan natural que olvidas que a tu lado tienes a un semidios. No es artificial y vacía como la de Unum, tiene pausas que denotan vida, exalaciones que transmiten una canción llena de vida."
            "La entidad que tienes aquí a tu lado, es más humano que dios. Un niño con sueños y deseos, que pide a gritos ser contenido por un adulto competente."
            "Tú quieres ser aquel quien lo contenga y cuide del resto de este mundo, al menos por el tiempo que le queda para desarrollarse."
            "..."
            "Pasas el tiempo mirando el cielo, en compañía silenciosa de tu hijo. Disfrutando el momento junto con él."
            "Cuando te percatas de que Noor se ha dormido, te levantas. Le miras por un tiempo antes de decidir si despertarlo o no."
            scene jardin_chicas with dissolve

            "Es mejor dejarle este tiempo para que descanse, se lo merece."
            jump explorar_unum_act3
        

        "Acompañar a Shams e Ignis.":
            "Ir a ver lo que Shams está haciendo junto a Ignis no es mala idea, tienes un poco de curiosidad acerca de las habilidades culinaria de la mayor de los gemelos."
            scene cocinaunum with dissolve
            "No te sorprende ver a tu hija rezongar cuando erra en las notas más altas o difíciles del cantido, pero aun así es divertido de ver."
            "Finge un llanto que pone a Ignis de pelos de punta, haciendo que la mujer que siempre parece tan compuesta, alce la voz y demande orden en la cocina."
            "Le advierte a Shams que si no deja de llorar, no continuará la lección."
            "Eso le basta a la chiquilla para cesar todo llanto y enderece la compostura, sin antes pedir perdón."
            "Ignis, por lo bajo, se lamenta el parecido que tiene la niña con Unum."
            jump explorar_unum_act3
        

        "Explorar la residencia.":
            "La residencia de las esposas de Unum es totalmente diferente a la de Unum; no hay pinturas que rozan lo grotesco, o habitaciones amuebladas que intenten simular un hogar típico del mundo real."
            "Todo aquí tiene un propósito. No existen decoraciones para embellecer la casa, ni menos muebles que puedan servir como comodidades para sentarse a descansar o dormir."
            scene cocinaunum with dissolve
            "Es chocante como la residencia no presenta nada de lo que debería existir en un hogar. Lo único remotamente humano es la cocina -la cual es una copia de la que tiene Unum- y una mesa para comer."
            scene salchichas with dissolve
            "El resto, es solo espacio muerto, habitaciones vacías o lugares a los cuales físicamente no puedes acceder por falta de suelo."
            "..."
            "Da miedo."
            jump explorar_unum_act3
        
        "Dejar de explorar.":
            jump acto3_unum_continuacion
        

    return 








label explorar_nulla_act3:
    

    menu:
        "Mostrarle tu mensaje." if mensaje_guardado is not None:
            scene segundopiso with dissolve

            "Llevas a Nulla de la mano por la casa, dirigiéndolo a su habitación."
            
            scene habitacionnulla with dissolve

            "Nulla es quien te abre la puerta, dejando que pases primero con un gesto de su mano."
            "El escritorio está esperándote junto con la hoja en donde has escrito tu pequeño mensaje."
            "Sin vacilación en tus movimientos, le entregas la hoja a Nulla para que sea él quien lo lea."
            "Nulla se hace el sorprendido. Sospechas que, al menos, se ha aguantado las ganas de no leer el contenido..."
            
            scene act3_n_mensaje with dissolve

            "Nulla lee tu mensaje en voz alta luego de sentarse en su cama."
            nulla "[mensaje_guardado]"
            $ amor_nulla += 1
            "..."
            
            scene act3_n_mensaje4 with dissolve

            nulla "..."
            nulla "[nombrejugador], corazón."

            show act3_n_mensaje3
            
            nulla "Pfff--"
            "Nulla suelta aire, que se traduce en una risa mal formada. Una que intenta contener, asustado de que se malinterprete su intención. Se le ve nervioso, no sabiendo cómo reaccionar."
            nulla "No puede ser..."
            
            hide act3_n_mensaje3

            "Observas como su mandíbula tiembla por unos segundos, al igual que sus manos que sostienen el papel con tu mensaje."

            menu:
                "¿No te ha gustado?":
                    
                    nulla "..."
                    nulla "No, no es eso."
                    nulla "Claro que me ha gustado..."
                    
                
                "Perdón...":
                    nulla "¡No!--- no pidas perdón."
                    "..."
                
                "¿Pasa algo?":
                    "..."
            
            nulla "Ay---"
            "Nulla intenta ocultar su cara con la mano, desviando la mirada al suelo."
            
            show act3_n_mensaje2

            nulla "No puedo creer que tenga algo escrito por ti, aquí... conmigo."
            nulla "Algo que pueda mirar directamente y tocar..."
            nulla "Algo que puedo guardar."
            nulla "¿Es mío? ¿Me lo puedo quedar?"
            menu:
                "No.":
                    menu:
                        "{glitch=30.0}{color=ffffff}{b}Sí.{b}{/color}":
                            pass

                        "Sí.":
                            pass
                
                "Sí.":
                    pass
            
            hide act3_n_mensaje2
            show act3_n_mensaje5

            "Su rostro se transforma completamente, totalmente ido."
            "Solo falta que lo bese... o se lo coma... huh."
            nulla "Lo llevaré conmigo."
            nulla "A donde sea que vaya."
            
            hide act3_n_mensaje5
            scene habitacionnulla 
            with dissolve

            jump explorar_nulla_act3
        
        "Decirle que has modificado la imagen." if cuadro_modificado():
            #Ver la posibilidad de modificar el tamaño y hacer que Nulla sostenga la imagen para ponerla en el cuadro....
            "Nulla sonríe."
            nulla "A ver si mi increible [nombrejugador] ha podido crear algo para mí~~~"
            show para_nulla with dissolve
            pause 3.0
            "..."
            scene act3_n_dibujo with pixellate
            nulla "Wow."
            scene act3_n_dibujo2 
            nulla "Woow---"
            pause 1
            $ nulla_spam()
            nulla "Este es el mejor regalo que alguien me ha hecho."
            nulla "{size=*0.6}Ay--- se me va a salir el corazón-{/size}"
            scene act3_n_dibujo3
            nulla "Agradece que estás detrás de esa pantalla---"
            nulla "Porque si no fuera por eso---" 
            scene act3_n_dibujo3 with dissolve
            pause 0.05
            scene act3_n_dibujo4
            pause 0.05
            #TE COMO, A BESOS ;)
            scene act3_n_dibujo5
            show tecomoabesos
            pause 3.0
            "Comienzas a sentir una presión ajena en la parte de tu cuerpo inferior. Miras con urgencia hacia abajo, pensando en la posibilidad de que tu cuerpo ya esté cediendo al uso prolongado y esté comenzando a fallar."
            "Mas solo te encuentras con 4 apéndices formados por las sombras de Nulla. Se enroscan y contorsionan en tus piernas y cintura, imposibilitando una posible huida."
            menu:
                "Decirle que te suelte.":
                    "Se lo dices antes de que esas cosas te atrapen la boca."
                    nulla "¿Hmm?"
                    hide act3_n_dibujo5
                    show act3_n_dibujo4
                    "Te devuelve la mirada confundido. Y tú no tienes más opción que agitar tu cuerpo para que él lo note."
                    pass

                "No decir nada y ver que pasa.":
                    if amor_nulla >= 5:
                        "Los apéndices se deslizan por tu cuerpo, subiendo hasta tu cuello. Envolviéndose entre si, bifurcando su camino con cada toque con otro apéndice."
                        "Con cada segundo pasado, las ramificaciones contraen la piel debajo de tus ropas, llegando a un punto en que sientes como la sangre bombea por tus venas."
                        nulla "Quiero tenerte."
                        nulla "Te quiero todo para mí."
                        nulla "Quiero ser tuyo."
                        "Los apéndices se contraen más en tu cuerpo, como si intentaran perforar la piel y escurrirse dentro de tu carne. Contaminar todo tu sistema con ese negro antinatural que rodea a Nulla."
                        scene negro with pixellate
                        nulla "Podría engullir a la marioneta y mandar todo a la mierda."
                        "Eso es todo lo que falta para que Nulla decida por fin moverse y tirarse hacia ti. Ambas manos toman tus mejillas para facilitar un feroz beso."
                        "No te deja respirar, es demandante e intenso, desesperado por un contacto que dificilmente puede llamarse tierno."
                        nulla "..."
                        "Cuando finalmente Nulla decide separar su boca de la tuya, encuentra refugio en tu cuello. Respira hondo, intentando calmarse."
                        nulla "Gracias---" 
                        nulla "No sabes lo feliz que me hace ver que has editado parte del juego por mí."
                        pass

                    else:
                        "..."
                        "La presión llega a doler, pero te aguantas."
                        "........"
                        "Duele."
                        pass
            
            scene blanco with dissolve

            "Nulla mira abajo, notando cómo sus sombras aún siguen estrujando tus extremidades, peligrando con cortar la circulación de estas mismas."
            nulla "¡Oh!"
            nulla "Lo siento."
            nulla "Me emocioné de más. Ja ja ja."

            jump explorar_nulla_act3
        
        "Ir afuera.":
            scene jardinnulla with dissolve
            #Nulla habla de sus vidas pasadas como si fueran memorias lejanas. Él habla como si realmente las hubiera vivido, pero solo son recuerdos.
            "Van afuera. Todo lo que recubre el supuesto jardín de su casa es una negrura que se extiende por todo tu campo de visión. No tienes idea de cuanto sea la magnitud de extensión del vacío, y eso te causa mucha curiosidad."
            "Nulla se sienta en los escalones y espera en silencio."
            menu:
                "Sentarse a su lado.":
                    pass
                "No sentarse.":
                    "Optas por quedarte de pie. Al final, sigues estando a su lado, y verlo desde arriba no está tan mal."
                    "Se ve tierno. Pequeño."
                    pass
            
            show nulla1triste with dissolve

            nulla "Si no te tuviera a mi lado ahora."
            nulla "Si no te hubiera conocido---"
            nulla "Seguiría sentado aquí, mirando el vacío."
            "Sus ojos yacen pegados al horizonte, enfocado en algo que no comprendes del todo aún."
            
            hide nulla1triste
            show nulla1serio
            
            nulla "¿Conoces la ciudad de Valparaíso?"
            menu:
                "Sí.":
                    pass

                "No.":
                    nulla "Ja, supongo que no es muy conocido."

            hide nulla1serio
            show nulla1normal

            nulla "Viví ahí."
            nulla "Hay veces en que me gustaría estar ahí por mí mismo."
            nulla "Oler y escuchar el mar. Caminar por esas calles empinadas. No sé, experimentar realmente la ciudad."
            nulla "A mi yo del pasado no le gustaba tanto."
            
            hide nulla1normal
            show nulla1silencio

            nulla "..."
            "Medita por un momento antes de suspirar decepcionado."
            
            hide nulla1silencio
            show nulla1triste

            nulla "Supongo que es cuestión de gustos y uno sueña con lo que no puede tener."
            "Nulla te comenta de memorias maltrechas por el tiempo, hay lagunas en sus historias, las cuales no puede rememorar."
            "Termina por evitar contar más memorias, frustrado con la dificultad de traer recuerdos no vividos."
            hide nulla1triste with dissolve
            
            jump explorar_nulla_act3
        
        "Preguntarle que quiere hacer.":
            
            scene entradanulla with dissolve

            nulla "Cualquier cosa que me deje estar mirando tus ojos."
            "Le ofreces platicar y él acepta."
            "Pasan un buen rato hablando de pequeñeces y temas que sirven para matar el tiempo. Aun así, no es tiempo perdido, pues Nulla se asegura de no perder tu atención."
            jump explorar_nulla_act3
        
        "Esperar al almuerzo.":
            "...."
            jump continuacion_nulla_act3
        


label septemgana_n_act3:
    scene comedorseptem2 with dissolve
    "Vas directo a donde se encuentra la vela, no lo dudas mucho. Sabes qué significa esa vela, ya has visto lo que puede hacer cuando estuviste con Septem en su momento..."
    "Esto es traición, lo sabes."
    "Y sabes que Nulla sabe."
    centered "{glitch=30.0}{color=ffffff}{size=*4.0}¡[nombrejugador]!{/size}{/color}"
    "Ignoras sus gritos."
    "Ignoras sus comandos. Tanto piernas como brazos buscan tomar el control de sus deseos; evitar que no llegues, que no la toques. Pero eso no lo vas a permitir."
    $ persistent.septem_symbol = True
    $ bloquear_iconos = True
    "Septem no lo permite."
    scene blanco
    show ojo
    with dissolve
    septem "Te lo dije."
    septem "Haré que te quedes conmigo el final."
    hide ojo with dissolve
    scene comedorseptem2 with dissolve
    "Teniendo más libertad en tus movimientos gracias a la intervención de Septem, corres hacia la vela. Rompes el cristal que la protege, no importa cuanto tus manos sangren, tu objetivo es tomar la vela."
    "Cuando por fin la tienes entre tus dedos, la cera se filtra por tus heridas, creando carne divina desde el ardiente dolor."
    scene blanco with dissolve
    "Espirales blanquecinos toman posesión de tu cuerpo, volviendo todo estímulo confuso. Ya no ves, no sientes y a penas escuchas. Escuchas sus gritos pero no puedes hacer nada."
    "Pronto, los gritos de Nulla se mezclan con el ruido blanco del lugar en que te encuentras. Él maldice, llora y grita por ti."
    $ persistent.nulla_symbol = False
    "Te pide que vuelvas, pero tú ya no te encuentras en ese lugar."
    "Hasta que no lo escuchas más."
    "..."
    "Tienes la sensación de que tu mano es apretada por otra de mayor tamaño. Al mirar, te das cuenta de que no tienes un cuerpo como tal."
    "Eres algo más. Eres un todo, intangible y hermoso."
    septem "Por fin te tengo."
    septem "No fue fácil llegar a ti."
    "Sientes la presencia de Septem a tu lado... dentro y sobre de ti. Su alma rodea la tuya, la abraza y mece mientras te lleva por un flujo de energía que aún no puedes comprender."
    "El calor que transmite te calma. El alma de Septem tiene un efecto embriagador, evitando que pienses en demasiadas cosas a la vez, eliminando todo dato o persona que te ha hecho algún mal."
    "Y junto a ello, borrando al dueño del vacío de tu alma proyectada en este plano."
    "Septem ríe."
    septem "Podríamos quedarnos así."
    septem "Hasta que decidas volver conmigo por tu cuenta."
    septem "Mientras... nos quedaremos aquí."
    scene negro with dissolve
    $ bloquear_iconos = False
    centered "{sc=3}{b}BAD END: Reminiscencias.{/b}{/sc}"
    $ MainMenu(confirm=False)()
    return

#EDITAR
label septemgana2_n_act3:
    scene negro with dissolve
    "Septem aprovecha de esos segundos de desconcierto. Una de sus manos consigue liberarse del agarre de Nulla y alcanza el cuchillo que está entre tus manos."
    scene blanco with dissolve
    "Antes de que puedas reaccionar, o siquiera pestañear, sus dedos se cierran alrededor del mango. Forcejea contigo, tirando del arma con una fuerza descomunal."
    "De la nada, un destello de luz te deja ciego y confundido. Justo el tiempo suficiente para que Septem te arrebate el cuchillo de las manos."
    
    menu:
        "Luchar contra Septem.":
            scene septembadendd with vpunch
            pause 0.05
            scene septemcuchillo2
            show sangre
            "Septem te clava el cuchillo sin piedad en el pecho."
            "Hundiendo la hoja en tu carne, haciéndose paso entre tus costillas."
            "Una vez."
            "Otra."
            "Y otra más."
            "No se detiene. Cada puñalada viene con rabia. Odio."
            "Perece disbrutar de ver como el rojo tiñe su mano y tu pecho."
            scene negro with pixellate
            centered "{sc=3}{b}BAD END: Muy lento~{/b}{/sc}"
            $ MainMenu(confirm=False)()

        "Dejarlo ganar." if persistent.septem_symbol2 == True:
            "Algo parece poseer a Septem. Agarra a Nulla de la cara, buscando con sus dedos sus ojos... intenta clavarlos ahí."
            "Las sombras de Nulla se precipitan a retener al rubio, sin embargo, es inútil... Algo impide que puedan tocarlo. Una fuerza invisible protege a Septem."
            $ persistent.septem_symbol = True
            $ bloquear_iconos = True
            "Un crujido recorre el piso."
            "Bajo de los pies de ambos, el suelo se resquebraja, formando grietas profundas y muy brillantes." 
            "De ellas nacen apéndices pálidos que reptan rápidamente por el suelo en dirección a Nulla."
            "Él a penas tiene tiempo de reaccionar, tomándolo por sorpresa cuando esas masas de luz toman captura de sus extremidades. Suspendiéndolo  en el aire."
            "Septem se incorpora lentamente, tranquillo, ya sabiendo que Nulla está a su merced." 
            "Escupe un poco de sangre al suelo, mira con atención como el liquido se esparce por el piso, intrigado."
            "Luego, con fastidio busca a Nulla con la mirada."
            "Los apéndices se convierten en garras que tiran de las manos y piernas de Nulla. Rompiendo su cuerpo de manera lenta y tortuosa. Septem no le presta atención, en cambio, decide acercarse a ti, bloqueando tu vista con su cuerpo."
            scene act3_s3f with dissolve
            septem "Con que aquí te vas cuando no estás conmigo."
            septem "Eres morboso."
            "Escuchas los quejidos de Nulla, quien te llama... su voz, que habitualmente va cargada con seguridad, se ve reducida a solo un grito roto."
            "Entre sus quejidos, detectas otro sonido, uno humedo y espantoso." 
            "Luego de eso, los quejidos cesan."
            septem "Eso lo mantendrá callado por un tiempo."
            "Septem no se molesta confirmar que es lo que ha pasado con Nulla."
            septem "Ahora---"
            septem "Has sido tan bueno--- dejándome ver esta línea temporal."
            septem "Eligiéndome a mí al final. Después de todo el trabajo que has hecho."
            scene act3_s3c
            septem "Pero no te voy a perdonar el desastre que has causado al Jardín."
            septem "Estarás a mi merced hasta que decida que puedes tener más libertades."
            scene act3_s3f
            "Septem te observa durante un largo tiempo. Al estar satisfecho con tu reacción, una pequeña sonrisa aparece en sus labios."
            septem "Voy a tomarme mi tiempo para domesticarte."
            septem "No me molesta."
            septem "Ni en lo más mínimo."
            scene negro with dissolve
            centered "{sc=3}{b}BAD END: Si tuvieras que elegir{/b}{/sc}"

            $ MainMenu(confirm=False)()
    
            
    return




label act3_s_badendnulla:
    if persistent.nulla_symbol2 == True:
        $ persistent.nulla_symbol = True
        $ persistent.septem_symbol = False
        "....."
        $ persistent.nulla_icono_act3 = True
        "........"
        centered "Vamos mi vida, tóca el botón~"
        centered "Te esto esperando~"
        jump act3_s_badendnulla
    
    else:
        scene negro 
        show nada1
        with dissolve
        "Respirar se te hace cada vez más difícil."
        "Los tentáculos se fusionan contigo, tapando tus vias respiratorias. Buscan cercanía, buscan contacto, y lo toman con fuerza, sin cuidado."
        "Pronto, pierdes la consciencia."
        centered "{sc=3}{b}BAD END: Aún no estás listo.{/b}{/sc}"
        $ MainMenu(confirm=False)()
    

label claseslatin:
    septem "Tú puedes hacerlo..."
    septem "Pide algo que te involucre a ti."

    menu:
        "{i}Sub potestate que mehi conceditud ego...{i}":
            "Septem se ríe de tu pronunciación, bajito e intenta aguantarse un poco... no es una risa mal intencionada."
            septem "No, no, [nombrejugador]."
            septem "Recuerda...... {sc=3}{b}ego faciam{/sc}{b}"
            jump claseslatin
        
        "{i}Sub potestate quae mihi conceditur ego faciam...{i}":
            jump claseslatin2
        
        "{i}Sus potestate qae conceditur ego faciam...{i}":
            septem "Tienes que soltar un poco más tu lengua."
            septem "Y prestar más atención a lo que digo."
            septem "Sub potestate---"
            extend "quae mihi conceditur---"
            extend "ego faciam."

            jump claseslatin
        
        "{i}Sub potest quae mihi concediur ego faciam...{i}":
            septem "Tierno..."
            septem "Pero no es exactamente lo que buscamos."
            "Sus dedos te acarician el cuello, apretando un poquito más tu tráquea, siempre teniendo cuidado de no apretar de más y dañarte la zona."
            jump claseslatin






label claseslatin2:
    "Cuando por fin lo logras, Septem te felicita, enfatizando lo perfecto que ha salido."
    "Septem es un buen maestro."

    show act3_s4b with dissolve

    septem "Para pedir algo que involucre a un otro, un {i}tú{i}, debes decir---"
    septem "{i}Sub potestate quae mihi conceditur, tu facies...{i} \n {size=*0.6}Bajo el poder que me confiere,       tú harás.{/size}"
    "Habiendo pronunciado el anterior comando, te es más fácil sacar este. Lo único que cambia son las palabras del final."
    septem "Y para un nosotros, sería---"
    septem "{i}Sub potestate quae mihi conceditur, nos faciemu... {i} \n {size=*0.6}Bajo el poder que me confiere,       nosotros haremos...{/size}"
            
    hide act3_s4b

    "Ya lo tienes dominado. No necesitas la guía de Septem con sus dedos o pausas para pedir que él te lo repita porque tú lo has olvidado."
    "Ya lo manejas, por lo que Septem te deja descansar."
    "Llega un momento en que te preguntas si deberías seguir aquí o salir a ver qué otras cosas hay por ver."
    $ latin = True
    menu:
        "Seguir explorando.":
            "Te despides de Septem, excusándote, diciendo que quieres seguir explorando el templo."
            "Él te desea suerte."
            jump act3_explorar_septem
                
        "Quedarte con Septem.":
            "Quedarte con Septem no suena mal. Te gusta pasar el tiempo con él."
            "El tiempo pasa y cuenta no te das cuando Septem te comenta que ya es hora. Te espera para que tú te levantes de su silla y camina junto contigo a la entrada del templo."
            jump acto3_septem_continuacion2