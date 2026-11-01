default noor_hambre = 0
default no_confianza = False
default comida_noor = False
define shams =Character ("Shams", color= "#00d9ff")
define noor =Character ("Noor", color= "#20a0b4")
default click_count = 0
default sirius_nombre = False
label rutaunum2:
    stop music fadeout 3.0
    "..."
    play music "audio/calamity.WAV" fadein 1.0 volume 0.4
    "El aumento de la temperatura es lo que te despierta."
    "Sientes como una gota gorda de sudor te recorre la frente."
    "... pero quieres volver nuevamente a dormir, estás muy cansado."
    el "Deberías agradecer que la biología de esta cosa y los míos son muy parecidas..."
    unum "¿Ya lo has hecho más veces?"
    el "Claro. No puedo estar en todos lados a la vez, siempre existe la posibilidad de que alguno de mis niños coma una fruta que faltó por santificar."
    scene unum_quinque1 with dissolve
    "Abres los ojos para ver que está pasando, pero la luz es muy brillante."
    unum "¡OH! ¡Quinque, está funcionando!"
    "Unum dice como si no se lo creyera. Quinque chasquea la lengua, exasperado."
    scene unum_quinque3
    quinque "¡No grites! aún falta sacar la rosa principal."
    "Una sensación extraña se forma en la piel que recubre tu vientre. Hay algo que se abre paso desde tu estómago hacía arriba con urgencia, no duele pero se siente molesto."
    quinque "Escúpelo aquí."
    scene act2_u1
    "Tu vista se ve invadida por una mano que espera con la palma abierta algo."
    "Y ese algo no tarda en llegar, pues de tu boca expulsas una rosa en perfecto estado."
    "Es asqueroso, pero a juzgar por la cara de Quinque, el no piensa lo mismo... es más, se le ve completamente indiferente, le da igual tener en su mano una rosa llena de saliva y jugos gástricos."
    "Cómo si ya lo hubiera hecho un montón de veces."
    quinque "Es exactamente lo mismo..."
    quinque "Realmente no entiendo la diferente entre los míos y los de Sextam."
    quinque "Su biología es muy parecida..."
    unum "Los tuyos no piensan."
    "Contesta Unum con gracia."
    quinque "¡El que no piensa eres tú!"
    scene act2_u2 with vpunch
    "Quinque se levanta con rapidez para agarrar a Unum de sus ropas. El pelirrojo solo rie, restando importancia al enojo de Quinque."
    quinque "Te vuelvo a escuchar decir eso una vez más y juro que rompo ese hibrido que tienes guardado."
    show act2_u3
    "Su sonrisa se desvanece por completo, optando por mirar hacia abajo a Quinque, completamente serio."
    unum "¿Ah? ¿Y tú cómo sabes eso?"
    quinque "Escucho otro corazón además de el que tiene este humano."
    unum "Hmmm."
    "Unum no se mueve mientras mira fijamente a Quinque."
    scene pasillounum with dissolve
    "Ya sea por la dificultad de sostener la mirada al sol o por simple incomodidad, Quinque chasquea la lengua, soltando y empujándolo."
    show unum3serio at left with dissolve
    unum "Supongo que ya Septem les ha dicho que seré yo quien hará el cambio."
    show quinque1serio at right with dissolve
    quinque "Sí."
    unum "Entonces..."
    hide unum3serio
    show unum1normal at left
    "Unum vuelve a sonreir."
    hide unum1normal
    show unum2feliz at left
    unum "¿Lo quieres ver?"
    quinque "No gracias. Volveré a mi dominio."
    quinque "Si necesitas ayuda en cualquier situación que desconozcas, puedes llamarme a mi o a Sextam."
    quinque "Todos estamos al tanto."
    hide unum2feliz with dissolve
    scene pasillounum with dissolve
    "Sin más, Quinque se retira de la habitación."
    "Unum se queda por un momento pensativo, para luego dedicarte una mirada complice."
    show unum2blush with dissolve
    unum "Ahora viene lo difícil. Cultivar a un dios."
    menu:
        "¿Qué?":
            unum "Tenemos que cultivar a este dios hasta que esté completamente listo."

        "¿A qué te refieres?":
            hide unum2blush
            show unum2duda
            unum "¿No es así cómo se dice?"
            nj "¿Que cosa?"
            unum "Cuando tienes que cuidar algo hasta que esté listo."
            nj "Eso es criar..."
            hide unum2duda
            show unum2feliz
            unum "¡Perfecto! vamos a criar a un dios."
    hide unum2feliz
    hide unum2blush
    show unum3blush
    unum "Pero voy a necesitar tu ayuda..."
    hide unum3blush
    show unum2duda
    unum "Sigo sin entender cómo la vida orgánica pasa por cambios que le permiten crecer y mejorar."
    unum "Nunca lo he visto por mí mismo..."
    hide unum2duda
    show unum2feliz
    unum "Así que supongo que tú sabes un poco más de esto..."
    "Harás lo que sea necesario para salvarte el pellejo, y si eso requiere jugar a la familia feliz con el dios del sol, lo harás sin dudarlo."
    menu:
        "Sí, cuenta conmigo.":
            hide unum2feliz
            show unum1normal
            "Unum sonríe sin mostrar los dientes."
            "Su expresión es tierna, nada parecida a las miradas que te ha dedicado en el pasado."
        
        "...Yo tampoco sé mucho...":
            hide unum2feliz
            show unum3risa
            unum "Oh."
            unum "No te preocupes."
            unum "Ambos nos apoyaremos con esto."
            unum "Después de todo, este dios no es ni humano ni un Estandarte completamente."
            hide unum3risa
            show unum2feliz
            unum "¡Será lo mejor de dos mundos!"
    stop music fadeout 3.0
    scene cocinaunum with dissolve
    "El día pasa."
    play music "audio/hope.WAV" fadein 2.0 volume 0.4
    "E increíblemente te encuentras acompañado por Unum y sus esposas."
    "A pesar de que el calor se hace cada vez más difícil de soportar, no es nada que te pueda hacer un daño verdadero."
    "Un poco de calor no mata a nadie... ¿cierto?"
    "Miras tu entorno y te encuentras con 3 pares de ojos puestos en ti."
    "Aeliana, Ignis y Solaris. Quienes a pesar de mirarte como si te quisieran comer, son bastante respetuosas y calmadas, a diferencia de Unum."
    scene act2_u4 with dissolve
    "Unum le pide a sus esposas que le enseñen a hacer la purificación de los alimentos, ya que según él tanto tú como el 'bebé' deben alimentarse sin preocuparse por un envenenamiento por parte de Tria."
    ignis "Tienes que juntar tus manos alrededor de la fruta y..."
    solaris "Debes cantar a la esencia de Tria."
    show act2_u5
    "Sin más explicación, Ignis comienza a cantar en un idioma que desconoces. Tanto tú, junto con Unum miran con la boca abierta como la fruta comienza a brillar."
    "Para luego ser espectadores de como un sello se rompe en el aire."
    aeliana "Cuando el sello de Tria se rompa, la fruta puede ser consumida."
    solaris "Hum... puede que el mini dios pueda no tener un riesgo mortal como [nombrejugador] al comer frutas no santificadas, pero el riesgo siempre está."
    ignis "Tal vez sea como nosotros..."
    aeliana "No asuman sin saber, queridas."
    aeliana "Hoy nosotras haremos la comida, pero a partir de mañana tú lo harás."
    aeliana "Cocinaras para todos."
    "Por un momento crees que te está hablando a ti, pero te das cuenta de que Aeliana tiene los ojos puestos en Unum."
    aeliana "Así que presta atención."
    scene palaciounum with dissolve
    "Después de una intensa clase de cocina, en la que deben redirigir constantemente la atención de Unum a la explicación, todos se reúnen alrededor de la mesa para comer."
    "Y comienzan a comer."
    "El ambiente es hogareño, más hogareño de lo que tu mente podría imaginar. Y eso te asusta un poco."
    "Las esposas de Unum hablan mucho, demasiado... tanto que te cuesta seguirles el hilo, pero a Unum no."
    "Él está atento a todo lo que dicen, preguntando de vez en cuando, pero sin llegar a interrumpirlas."
    "Estás anonadado."
    show aeliana_serio at left with dissolve
    aeliana "Mañana iremos con Duae a ver cómo está el cinturón de Orión."
    show unum3serio at right with dissolve
    unum "Hace mucho tiempo que no van."
    unum "... no me gusta que Duae se refiera a ustedes con sus nombre asignados, ustedes ya no son su propiedad..."
    show solaris_enojo with dissolve
    solaris "{size=*0.6}Si lo somos...{/size}"
    hide aeliana_serio with dissolve
    show ignis_normal at left with dissolve
    ignis "Unum, ya hemos hablado de esto..."
    "Unum suelta un quejido, claramente angustiado y sobrepasado por la situación."
    unum "Es que sigo sin entender como no les molesta."
    unum "Ustedes son libres, ya no están bajo el mandato de nadie."
    solaris "Eso solo aplica cuando no está Duae, y aún tenemos responsabilidades."
    unum "Pero..."
    hide ignis_normal with dissolve
    show aeliana_feliz at left with dissolve
    aeliana "No nos molesta, Unum."
    scene palaciounum with dissolve
    "Aeliana toma la mano de Unum con ternura, y con su pulgar acaricia el dorso de su mano."
    "...Unum en cambio se come sus palabras, optando por no discutirles más."
    scene cocinaunum with pixellate
    "Para cuando terminan, Unum y tú retiran los platos para lavarlos. Mientras que las esposas se despiden y te dan las buenas noches."
    menu:
        "¿Ellas tenían otros nombres?":
            show unum2duda
            unum "Ah... sí."
            hide unum2duda
            show unum3serio
            unum "Duae se los pone al crearlas, por lo general solo les pone un número... pero si son brillantes y tienen un buen desempeño, Duae las nombra con honores."
            nj "¿Cómo se llamaban?"
            unum "Alnitak, Alnilam y Mintaka."
            hide unum3serio
            show unum3risa
            unum "Son nombres bellos, pero son nombres de propiedad."
            unum "Cuando vinieron conmigo, les pedí que eligieran sus propios nombres."
            nj "Ya veo."
            hide unum3risa
            show unum2duda
            unum "Tu nombre..."
            hide unum2duda
            show unum3serio
            unum "¿Te lo han impuesto?"
            "{sc=3}El nombre que me has dado cuando estabas con Nulla.... ¿Cuenta como impuesto?{/sc}"
            "... desvias el tema para no tener que responder su pregunta. No sabes si Unum comprende la indirecta o no, pero te sigue el juego."
    scene act2_u6 with dissolve
    "Pasan el tiempo conversando de como santificar la comida, Unum te muestra lo que aprendió con una manzana."
    "E increíblemente, ha podido romper el sello."
    show act2_u7
    "Con una sonrisa que muestra todos sus dientes, te la ofrece."
    menu:
        "Aceptar.":
            "Tomas la manzana y le das un gran mordisco."
            "Luego de mascar, le sonríes mostrando los dientes, al igual que lo hace él."
            "Unum se sonroja y suelta una carcajada."

        "Rechazar":
            nj "No gracias."
            scene cocinaunum with dissolve
            "Claramente tu rechazo le afecta, pues su sonrisa se esfuma para soltar un simple {i}oh{i}."
            unum "La dejaré aquí por si te llega a dar hambre."
    scene habitacion with dissolve
    "Llega el momento en que te sientes cansado, por lo que Unum te lleva a tu habitación."
    scene piezaunum with dissolve
    "Unum te mira por un segundo cuando ya te encuentras cubierto por las sábanas y se acerca repentinamente a ti."
    unum "Cuándo duermes, ¿Que se siente?"
    "... te cuesta un poco responder con su cara tan cerca de la tuya."
    "¿Cómo responderle eso a alguien que no puede o necesita dormir?"
    menu:
        "Explicarle detalladamente.":
            "Tomas un poco de aire y comienzas a explicar desde como se siente dormir, porqué debes dormir y que pasa durante el sueño."
            "Le explicas la existencia de los sueños, recalcando que no siempre eres capaz de recordar tus sueños."
            

        "Explicarle de manera fácil.":
            "No quieres confundirlo y sacar a tema conceptos rebuscados o difíciles de explicar, como las fases del sueño y el porqué existen los sueños."
            "Tal vez eso se lo puedas explicar otro día."
            "Así que le respondes solo que es lo que se siente dormir."
    scene piezaunum1     
    "Mientras hablas, notas cómo Unum se recuesta en la cama, observándote con los ojos bien abiertos."
    "Su atención está en todo momento sobre ti, está pendiente de cada palabra que pronuncias, tal como lo hizo mientras sus esposas conversaban en la mesa."
    "Se ve lindo."
    unum "..."
    "En un momento, la expresión de Unum se torna a una expresión angustiada."
    unum "¿Crees que él bebé pueda soñar?"
    unum "Me gustaría que pudiera experimentar aquello."
    unum "Suena... liberador."
    menu:
        "¿Ustedes no sueñan?":
            unum "...no."
            unum "No estamos configurados como los humanos."
            unum "No necesitamos descansar y menos soñar."
            unum "Nuestro único propósito es mantener el orden del jardín."
            unum "Por lo que dormir y soñar es una pérdida de tiempo."
            "Oh."

        "Yo creo que podrá soñar.":
            scene piezaunum0
            unum "Waaah."
            unum "¡¿De verdad lo crees?!"
            "Asientes con la cabeza y Unum se abalanza sobre ti para darte un abrazo junto con un beso."
            unum "Estoy tan feliz."
            "Te asusta un poco que te crea como si lo que dices es la verdad absoluta..."

        "...":
            pass

    "..."
    scene piezasinunum with dissolve
    "Unum se aclara la garganta, algo avergonzado con su comentario."
    unum "Deberías descansar ahora."
    unum "Nos vemos en unas horas."
    unum "¡Buenas noches!"
    "Te besa en la frente y se va de la habitación."
    "Meditas por un largo tiempo lo conversado con Unum..."
    "Los nombres aquí son importantes, más importantes de lo que tu creías."
    "Si las esposas de Unum fueron pertenencia de Duae, entonces... los Estandartes también deben pertenecer a alguien."
    "¿Ese alguien será Septem?"
    "Tal vez mañana deberías preguntar por qué los nombres son tan importantes y porqué Unum no se siente cómodo con nombrar a sus esposas por sus nombres originales."
    "Poco a poco vas cerrando los ojos."
    "Y te dejas caer en un sueño profundo."
    scene piezasinunumnoche
    pause 0.1
    scene negro with dissolve
    stop music fadeout 3.0
    "..."
    scene piezasinunum with dissolve
    unum "¡[nombrejugador]!"
    scene habitacion with vpunch
    play music "audio/mechanique.mp3" fadein 2.0 volume 0.2 
    unum "{size=*2.5}¡[nombrejugador]!{/size}"
    "Dos manos te agarran por los hombros para sacudirte con urgencia."
    show unum2enojo with dissolve
    unum "Fui a ver al bebé y hay algo raro en él."
    "Tienes que parpadear unas cuantas veces para despertar completamente y entender que demonios está diciendo el pelirrojo."
    nj "¿Q- Que?"
    unum "Hay algo raro con el bebé."
    scene pasillounum with dissolve
    "Sin más aviso que aquello, Unum toma tu mano y te arrastra fuera de la cama."
    "Unum te explica cómo puede, entre el pánico y los nervios, lo que está pasando con el bebé."
    "Pero tú no comprendes nada."
    "Necesitas solo 5 minutos de paz... por favor."
    "Solo 5 minutos, para pensar las decisiones que has tomado para haber llegado hasta aquí..."
    scene act2_u8 with pixellate
    unum "¿Es normal que se mueva tanto?"
    "... ¿¿¿¿Por qué te pregunta esto, sabiendo que ninguno de ustedes dos TIENE IDEA ALGUNA DE COMO FUNCIONA EL DESARROLLO DE UN BEBÉ CREADO CON COMBINACIÓN DE ALMAS?????"
    nj "¿¿¿No lo sé???"
    nj "Acaso Sextam no te ha explicado el proceso de desarrollo de esta cosa?"
    unum "¡¿Cosa?!"
    unum "¡Es un bebé!"
    "...no sabes que es lo hace que el comentario sea más divertido, la cara de Unum o el hecho de que la cosa que está apuntado claramente, no es un bebé."
    "Es una masa transparente que se mueve como si sintiera incomodidad..."
    "Y ni siquiera sabes si eso es capaz de sentir o no algo aún."
    unum "Creo que necesita estabilizarse..."
    unum "Ambos tenemos que tomarlo."
    "Esperas que esto se lo haya dicho Sextam y no se lo esté inventando..."
    "A medida que se acercan puedes sentir un golpe de calor inmenso, no es agradeble como el calor que transmite el cuerpo de Unum."
    "No, este calor es insoportable."
    menu:
        "Poner tu mano en la masa.":
            pass
        "No poner tus manos ahí.":
            jump badendexplosion
            #BADEND: Al no tener tus manos en la estrella, su explosión te mata.
    show act2_u9
    "Junto con Unum, ambos colocan sus manos en la masa."
    "Sientes un hormigueo en tus dedos y brazo, pero no te duele ni quema."
    unum "Esto es como el nacimiento de una estrella..."
    scene negro with dissolve
    "No eres capaz de responder a Unum cuando un destello te nubla los ojos. Es tan brillante que los tienes que cerrar con fuerza para no quedar ciego."
    "Un calor intenso te rodea y abraza, es como si los rayos del sol se clavaran en tu piel, besándote suavemente por un prolongado tiempo."
    "Luego, el brillo cesa."
    scene act2_u8b with vpunch
    "Cuando abres los ojos, Unum grita."
    unum "¿Se partió?"
    "Efectivamente, la masa ya no es una, sino dos."
    scene salaunum with vpunch
    "Escuchas como la puerta se abre de golpe."
    show aeliana_serio at right with dissolve
    aeliana "Mi señora Duae, no puede entrar a esta sala sin avisar."
    show duae1serio at left with dissolve
    duae "No quiero que hables, Alnitak."
    "Aeliana hace una mueca de dolor, y sus labios se sellan con fuerza."
    "Unum se gira para ver a Duae entrar por la puerta, seguida de Aeliana."
    hide aeliana_serio
    show unum3serio at right with dissolve
    unum "No tienes permiso de darles órdenes en mi dominio."
    unum "Devuélvele el habla ahora mismo."
    duae "Hmmm. Luego de esto."
    "Duae ignora la orden, para acercarse a ustedes."
    duae "Debo asistir en el nacimiento de estas estrellas binarias."
    unum "No son tuyas."
    duae "Septem me ha dado órdenes de asistir en todo lo que sea necesario."
    duae "Y mi asistencia es necesaria ahora, tú no estás calificado para esto..."
    "Unum no tiene la oportunidad de rebatir su comentario cuando Duae agrega con algo de veneno en su voz."
    hide unum3serio
    show unum3callado at right
    duae "Eres muy egocéntrico, siendo que las que te rodean son incluso mejores que tú."
    duae "Más fuertes y grandes."
    hide unum3callado
    show unum2feliz at right
    unum "Pero no aptos para dar espacio a la vida orgánica."
    duae "Ja."
    "Duae quita tu mano de la masa y le pide a Unum espacio para que ella pueda hacer su trabajo."
    scene act2_u10 with dissolve
    "Unum a regañadientes da unos pasos atrás junto contigo, cuando considera que están a una distancia prudente, se coloca delante tuyo, cubriendo tu cuerpo con el suyo."
    "Supones que debe ser por protección."
    show act2_u11 with dissolve
    "Duae coloca ambas manos en cada una de las masas, y de un solo jalón se forma un brillo mucho más brillante que el anterior."
    scene negro with dissolve
    "Unum te cubre los ojos con su brazo."
    "Hay un silencio sepulcral luego de aquello, y la temperatura que hay ahora en la sala es insoportable."
    "..."
    "Y el llanto de un bebe lo rompe, seguido por otro mucho más débil."
    duae "¿Qué es esto?"
    scene salaunum with dissolve
    "Como si de un pescador se tratase, Duae sujeta a dos criaturas por los pies, ambas lloran por la posición en la que están."
    "Sientes como sudas, y tu visión comienza a nublarse. El aire que respiras es caliente y no hace más que desesperarte con el pasar de los segundos."
    unum "¡Así no se toman, bruta!"
    duae "..."
    scene act2_u12 with dissolve
    "Anonadada Duae entrega a las dos entidades en los brazos de Unum. Quien las toma como es debido tomar a un bebé humano."
    duae "¿Esto es un humano?"
    unum "No, híbridos."
    duae "Pensé que de aquí saldría un dios ya listo para tomar su rango."
    duae "No esto."
    unum "... eso da igual."
    duae "Supongo que Septem está al tanto de que jugarás a ser humano..."
    "Duae observa a las pequeñas entidades en los brazos de Unum. El ambiente está tenso."
    duae "Son tuyos, debes ponerles un nombre."
    duae "Ahora."
    show act2_u13
    "Ya no aguantas más y Unum parece darse cuenta de lo mal que te encuentras. Con nervios asomándose en su voz, te pide salir de la sala por un momento."
    "Indicando que salgas al jardín para que tomes aire."
    scene pasillounum with dissolve
    "Y tú lo haces sin chistar."
    scene jardinunum with dissolve
    "Caminas con dificultad hacia la puerta que conduce al jardín y te sientas en una de las bancas cercanas."
    show negro with dissolve
    stop music fadeout 3.0
    "Respiras hondo y cierras los ojos..."
    "Aquí el aire es fresco y no te da la sensación de quemarte los pulmones al inspirar."
    scene jardinunum with dissolve
    play music "audio/fell.mp3" fadein 2.0 volume 0.3
    "Miras tus manos y hay algo que te está comenzando a preocupar..."
    "No es el color de ellas, pues Septem también tiene esas marcas, no... lo que te preocupa es que has comenzado a sentir menos en ellas."
    "No tienes sensación en las yemas de tus dedos, la sensibilidad en esa zona es casi inexistente."
    "Si bien puedes mover tus dedos, algo dentro de ti te dice que tarde o temprano dejarás de tener ese beneficio."
    "Si le comunicas esto a Unum, ¿podrá ayudarte?"
    "Sinceramente, ahora Unum no parece ser tan aterrador, pero crees que es porque ya llevas algo de tiempo con él, entonces puede que ya te hayas acostumbrado a su extraña presencia y personalidad."
    "No es malo... solo extraño y algo violento cuando tiene hambre."
    "¿Será viable quedarte aquí?"
    "Si intentas escapar... ¿tendrás alguna otra opción de sobrevivir?"
    menu:
        "Escapar.":
            jump badendseptemjardin
        
        "Quedarte con Unum":
            pass
    "Sí, es lo mejor dentro de tus posibilidades."
    "No conoces que hay más allá de este jardín, ni menos como es el mundo o sociedad allá afuera."
    "Para colmo: {i}apestas a humano{i}, según lo que has visto y escuchado, y eso no es bueno para ti."
    "Eres una presa fácil."
    el "{sc=2}¿Ya tienes permiso de estar afuera?{/sc}"
    "Conoces esa voz..."
    show septem1normal with dissolve
    "Subes la mirada y vez como Septem se encuentra parado a tú lado, mirando por sobre tu hombro."
    menu:
        "¿Qué haces acá?":
            hide septem1normal
            show septem2normal
            septem "{sc=2}¿Quien te dio el derecho de hacer preguntas?{/sc}"
            "Septem sonríe dulcemente, pero su voz no refleja su expresión."
            "Suena molesto."
            hide septem2normal
            show septem2risa
            septem "{sc=2}Responde mi pregunta.{/sc}"
            nj "..."
            

        "Saludarlo":
            nj "Buenos días..."
            "Septem sonríe complacido."
            hide septem1normal
            show septem2risa
            septem "{sc=2}Responde mi pregunta.{/sc}"
            "¡Oh! cierto."
            

        "Responder su pregunta.":
            hide septem1normal
            pass
    hide septem2risa
    show septem2feliz
    nj "Unum me ha pedido que salga a tomar aire."
    nj "La habitación en que estábamos no era muy agradable."
    hide septem2feliz
    show septem2incomodo
    septem "{sc=2}Me imagino... {/sc}"
    septem "{sc=2}Los humanos no pueden resistir el poder de tantas estrellas por mucho tiempo.{/sc}"
    septem "{sc=2}Menos de estrellas recién creadas.{/sc}"
    septem "{sc=2}Si no hubieras salido, seguramente estarías ya muerto.{/sc}"
    "Quieres preguntar si ha venido a ver a los híbridos, pero tienes miedo de como él pueda reaccionar."
    hide septem2incomodo
    show septem2normal
    septem "{sc=2}Vamos a verlos.{/sc}"
    nj "¿A los híbridos de Unum?"
    hide septem2normal
    show septem2incomodo
    septem "{sc=2}Son tuyos también.{/sc}"

    menu:
        "Si. Los quiero ver.":
            pass
        
        "No. No los quiero ver ahora.":
            hide septem2incomodo
            show septem1risa
            septem "{sc=2}Hmmm, no fue una pregunta.{/sc}"
            septem "{sc=2}Vamos.{/sc}"

    scene pasillounum with dissolve
    "El camino de vuelta es incómodo, Septem no hace esfuerzo alguno por entablar una conversación y tú estás seguro de que si hablas primero, y sin permiso, él se enojará."
    "Dentro de la residencia de Unum se encuentran con sus esposas, quienes están fuera de la habitación."
    "Al notar la presencia de Septem, las tres agachan la cabeza a modo de saludo."
    show septem2incomodo at left with dissolve
    septem "{sc=2}Alnitak ¿Se ha estabilizado la situación?{/sc}"
    "Aeliana no responde y Septem parece darse cuenta del porqué, ya que con sus manos hace unas señas."
    "Sus labios dejan de estar tensos y ella responde."
    show aeliana_serio at right with dissolve
    aeliana "La señora Duae ha estabilizado a las nuevas estrellas."
    aeliana "Ya es seguro para [nombrejugador]."
    hide septem2incomodo
    show septem2normal at left
    septem "{sc=2}Bien.{/sc}"
    hide septem2normal and aeliana_serio with dissolve
    scene salaunum with dissolve
    "La puerta de la habitación se abre por si sola y Septem se abre paso por la habitación."
    show septem2normal at left with dissolve
    septem "{sc=2}Duae. Unum.{/sc}"
    hide septem2normal
    show septem2enojo at left
    septem "{sc=2}Les recuerdo que es primordial que [nombrejugador] esté en los momentos más cruciales.{/sc}"
    septem "{sc=2}No volveré a tolerar que le separen de ellos.{/sc}"
    "Duae se endereza completamente, como si de un soldado de bajo rango viera entrar a su general."
    show duae1serio with dissolve
    duae "Septem, mil disculpas."
    show unum3callado at right
    unum "Le pedí que saliera porque la energía de todos está muy condensada en esta habitación."
    hide septem2enojo
    show septem2incomodo at left
    septem "{sc=2}Lo sé. Pero yo necesito que [nombrejugador] esté observando el desarrollo de ambos dioses.{/sc}"
    septem "¿Ya están estables?"
    duae "Sí."
    septem "{sc=2}Okay. Duae, nos retiramos ahora.{/sc}"
    septem "{sc=2}Unum.{/sc}"
    unum "¿Sí?"
    hide septem2incomodo
    show septem2normal at left
    septem "{sc=2}Quiero una audiencia contigo en la noche.{/sc}"
    hide septem2normal with dissolve
    hide duae1serio with dissolve
    "Sin nada más que agregar, Septem se retira de la habitación con Duae."
    "Unum no se mueve hasta sentir que ambos Estandartes se encuentran lejos."
    hide unum3callado
    show unum1risa at right 
    stop music fadeout 3.0
    "Luego esboza una sonrisa."
    unum "¡Mira!"
    scene act2_u14 with dissolve
    play music "audio/frozen_winter.WAV " fadein 2.0 volume 0.2
    "Se acerca a ti con ambas criaturas en los brazos."
    unum "Tienen un pulso al igual que tú."
    unum "Aunque tienen una frecuencia cardiaca muy diferente a la tuya."
    unum "¡Son tan lindos!"
    unum "Aún no los puedes tomar, su cuerpo aún está muy caliente."
    unum "Te puedes quemar tus manos."
    "Oh."
    "Bueno, te conformarás con mirarlos de cerca."
    "Cuando acercas tu cara, te das cuenta nuevamente del calor que el cuerpo de ambos bebés transmite."
    nj "¿Cómo se llaman?"
    unum "..."
    unum "Me gustaría esperar a que sea lo suficientemente grandes para que elijan sus propios nombres."
    nj "¿Por qué?"
    unum "Quiero que sean libres."
    unum "Que hagan lo que quieran hasta..."
    "Unum cierra su boca antes de terminar la frase."
    "Y luego ríe nervioso."
    unum "Septem dijo que crecerán rápido."
    unum "Posiblemente mañana ya no sean así de pequeñitos."
    "..."
    scene habitacion with dissolve
    "Pasan gran parte del tiempo cuidando de los bebés."
    "Bueno.. tú le das instrucciones a Unum para los cuidados, ya que aún no puedes tocarlos."
    "...y lo has comprobado por ti mismo, cuando intentaste tocar la mejilla de uno de ellos. Te quemaste la mano."
    "Unum casi llama a Quinque para que viniera a curarte, pero tú le has dicho que no es necesario."
    "Cuando llega la noche, Unum se excusa con que debe hacer algo importante y se lleva a ambos bebés consigo."
    "Te pide que descanses y duermas para que mañana tengas todas tus energías."
    "Así que descansas."
    scene negro with dissolve
    "..."
    stop music fadeout 3.0
    "Hoy sueñas." 
    "Por primera vez en tu corta existencia este mundo."
    "Estás en un lugar oscuro."
    "Y se escucha una voz."
    "Pero no logras identificar que es lo que dice."
    "..."
    scene camaunum with dissolve
    "No sabes cómo ni cuándo, pero ya es el otro día."
    show camaunum1
    play music "audio/fell.mp3" fadein 2.0 volume 0.3
    "Y lo primero que miras al abrir los ojos son tus manos."
    "El negro se ha comido más piel..."
    scene act2_u16b with dissolve
    "Lo segundo que tus ojos ven es a Unum recostado a tu lado, mirándote con mucha atención."
    show act2_u15
    unum "Eres una criatura asombrosa."
    unum "Jamás creí que podría ser esposo de un humano."
    "¿Esposo?"
    "¿Cuántos pasos se ha saltado este hombre?"    
    "¿Desde cuándo él piensa que ustedes están en una relación? ¿Será así con todos los estandartes o es solo Unum quien no tiene idea de cómo funcionan las relaciones?"
    "Sueltas una risa por lo extraño que te parece estar en esta relación."
    show act2_u16b
    "Unum te mira confundido."
    menu:
        "¿Quieres ser mi esposo?":
            show act2_u16
            unum "¿No somos ya?"
            "No puedes evitar dejar salir la carcajada que se forma en tu garganta."
            unum "Pero si hasta ya hemos tenido descendencia... y vives conmigo."
            unum "Según lo que he leído, eso es más que suficiente para llamarnos esposos."
            "Vuelves a soltar otra risa."
            unum "¡No te rias!"
            nj "¡Está bien! ¡está bien!"
            nj "No sé cómo serán las relaciones de la gente del jardín... pero los humanos necesitamos tiempo y acuerdos para llegar a tener ese título."
            unum "Oh."
            unum "¿Me podrías explicar?"
            unum "Aquí no hay ningún libro que te explique eso."
            "No tienes problemas con explicarle lo que se necesita para convertirse en 'esposos' a Unum, aunque recalcas que para todos es distinto."
            show act2_u16b 
            unum "Mmm."
            unum "Si me esfuerzo... ¿Podría ser yo tu esposo?"
            menu:
                "Sí":
                    scene act2_u15
                    "Unum sonríe mostrando todos sus dientes, victorioso."
                "Tal vez":
                    scene act2_u15
                    "Unum sonrie."
                "No.":
                    scene act2_u16
                    unum "Oh."

        "No comentar nada.":
            "No te da el corazón para corregirlo."
            "Que crea lo que quiera creer."
        
    unum "..."
    hide act2_u16
    show act2_u15
    unum "Quería mostrarte el resto de mi dominio hoy, pero Septem dijo que es peligroso que salgas."
    unum "Así que nos tendremos que quedar en el templo hasta que las estrellas hayan crecido."
    unum "No quiero perderme nada, ningún momento de su desarrollo."
    nj "¿Estás emocionado?"
    unum "¡Claro! Además, te tengo a mi lado, lo que lo hace aún mejor."
    unum "Somos como las familias que Sextam adoraba ver crecer."
    unum "¡Oh! Podríamos invitarla cuando deje sus rezos."
    scene habitacion with dissolve
    "Unum se levanta de la cama y te mira con emoción." 
    show unum2blush with dissolve
    unum "Las chicas están cuidando de ellos, mientras, nosotros haremos el desayuno."
    "Vaya... parece que Unum se está tomando las palabras de Aeliana en serio..."
    "Increíble."
    scene pasillounum with dissolve
    pause 0.2
    scene cocinaunum with dissolve
    "Caminan a la cocina y Unum se encarga de hacer el ritual de santificación antes de comenzar a preparar el desayuno."
    "Tú le ayudas en algunas cosas, pero él es quien hace la mayoría de las cosas, copia con exactitud lo preparado por las chicas el día anterior."
    "Y luego de un tiempo cocinando, el desayuno ya está listo."
    "Inflando el pecho, Unum mira con orgullo el resultado."
    "Pero al instante se desinfla como un globo."
    show unum2enojo with dissolve
    unum "Ahhhhhh- extraño ver a mis esposas cocinar...."
    hide unum2enojo
    show unum2feliz
    solaris "Veo que lo hiciste bastante bien."
    show solaris_normal at right with dissolve
    "Solaris entra por la puerta, sonriendo de medio lado."
    solaris "Parece que ahora serás tú el encargado de cocinar, querido."
    hide unum2feliz
    show unum1normal
    unum "Solo si me acompañan."
    solaris "Lo pensaremos."
    solaris "¿Necesitan ayuda para colocar la mesa?"
    hide unum1normal
    show unum1risa
    unum "Si, por favor."
    scene cocinaunum with dissolve
    "Es extraño..."
    "Esto es totalmente extraño. Jamás te imaginaste que convivir con ellos sería tan.... ¿normal?"
    "¿Dónde se fue ese Unum sobreexaltado por cualquier cosa? ¿Ese que intentaba atacarte a la mínima reacción de tu cuerpo?"
    "¿Dónde está el truco?"
    "..."
    "¿Será que luego te comerán? después de todo son entidades que comen carne de humanos..."
    "¿Realmente estás jugando a la familia feliz?"
    unum "¿[nombrejugador]?"
    nj "¡Ah! ¿s-sí?"
    show unum3risa with dissolve
    unum "¿Los bebés humanos pueden comer en la mesa?"
    nj "¿Qué?"
    hide unum3risa
    show unum2duda
    unum "Sinceramente no me los imagino sentados en la mesa con un tenedor y un cuchillo en las manos..."
    unum "Sus manos son muy pequeñas y no tienen tanta coordinación con ellas."
    unum "Bueno... no tiene coordinación en nada."
    "Respiras hondo antes de contestar, y recuerdas que Unum es una entidad totalmente opuesta a ti."
    "Que solo sabe de los humanos gracias a lo que ha leído."
    "Y solo dios sabe que cosas que estado leyendo..."
    scene palaciounum with dissolve
    "Los días pasan rápido, más rápido de lo que te gustaría confesar. Con la presencia de Unum y sus esposas en casa, no hay momento en que te quedes solo."
    "Siempre hay algo que hacer, y siempre resulta ser algo agradable."
    "Bueno... no siempre."
    scene cocinaunum with dissolve
    unum "¿Puedes pelar esto?"
    unum "Tengo que ir a preguntar a Ignis una cosa."
    nj "Claro."
    scene act2_u17 with dissolve
    "Cuando tomas el cuchillo y la fruta en tu mano te das cuenta de que tal vez no solo el color de tu piel está cambiando, sino que también tu movilidad en tus dedos."
    "Te cuesta coordinar y ejercer presión, pero aún lo puedes hacer."
    scene act2_u17 with vpunch
    "Estás a punto de terminar de pelar cuando Unum aparece por detrás tuya, tocándote los hombros."
    unum "¡HAHA! Lo haces mejor que yo."
    scene act2_u18
    show sangre with dissolve
    "Y solo eso basta para desconcentrarte y cortarte con el cuchillo la palma de tu mano."
    "El corte es profundo."
    "Y la sangre sale de ahí a cantidades preocupantes."
    scene cocinaunum with dissolve
    "Luego todo es un caos."
    "Estás agradecido de que Unum no te haya desgarrado la mano de un solo bocado."
    "Por qué a quien vamos a mentir, sabes que lo único que quería hacer en ese momento era comerte entero."
    "De pies a cabeza."
    scene negro with dissolve
    pause 0.5
    scene palaciounum with dissolve
    "Para el cuarto día, y poco a poco, te vas abriendo a cada una de las esposas de Unum."
    "Y al igual que el pelirrojo, están deseosas de saber más de los humanos."
    "Gracias a ellas descubres que ambos bebés necesitan estás juntos."
    "'Son estrellas binarias, lo que significa que están ligadas permanentemente por una cola en una danza infinita' dijo Ignis una vez."
    "Aunque hay una gran preocupación en las caras de las chicas cuando hablan de ello, pero cada vez que les preguntas por la razón, ellas cambian el tema."
    scene act2_u19 with dissolve
    "Al quinto día descubres el nombre de origen de ambos y si te concentras bien, enfocando tu mirada en los niños, puedes ver una cola." 
    "Sirius, ese es el nombre que ambos comparten, Aeliana te explicó que eso es debido a que ambos nacieron al mismo tiempo."
    "Pero no debes preocuparte pues solo será un nombre que nadie utilizará luego de que ambos dioses escojan sus propios nombres."
    "No puedes pasar mucho tiempo con ellos dentro de una habitación ya que su presencia te quema la piel, y te impide respirar con normalidad."
    "Al menos ahora los puedes cargar por un pequeño tiempo... y, no puedes evitar pensar que son lindos. Ambos se parecen a Unum, no tienen ningún parecido a ti físicamente. Y cuando le comentas esto a Unum, él solamente suelta una carcajada."
    scene act2_u20 with dissolve
    "Recuerdas vívidamente las palabras que salieron del dios del Sol en ese momento."
    show act2_u21
    unum "Ambos comparten un corazón y esencia parecida a la tuya."
    unum "Y eso... es mil veces mejor que si tuvieran una apariencia parecida a la mía." 
    nj "¿Por qué?"
    show act2_u22
    unum "Porque ahora puedo sentir tu corazón, acompañado de dos melodías más." 
    unum "Son diferentes, pero... la de ellos nace de la tuya, y juntas hacen la sinfonía más bella que he podido de escuchar."
    "... aún no puedes creer que Unum te haya dicho aquello."
    "Cada vez que lo recuerdas, sientes tus mejillas calentarse."
    "..."
    scene negro with dissolve
    pause 0.5
    scene habitacion with dissolve
    "Al séptimo día, un domingo, Septem viene a ver a tus bebés."
    "Los mira por un solo segundo y luego te observa a ti."
    show septem2incomodo with dissolve
    septem "{sc=2}Tus manos...{/sc}"
    nj "Ah... no es nada."
    hide septem2incomodo
    show septem1triste
    septem "{sc=2}Buscaré una solución para eso.{/sc}"
    hide septem1triste with dissolve
    "Sin explicarse, se retira."
    show unum2duda with dissolve
    unum "Ahora que Septem lo menciona."
    "Dice Unum mientras se acerca a inspeccionar tus manos."
    unum "Tus manos y brazos han cambiado con el tiempo."
    unum "¿Qué pasa con ellas?"   
    menu:
        "No sé":
            unum "...no te preocupes."
            hide unum2duda
            show unum3risa
            unum "Septem siempre cumple su palabra."
            hide unum3risa
            show unum2enojo
            unum "Siempre."
            "...."
        
        "No te preocupes por ello.":
            unum "Hmmm..."
            "...."
        
        "No decir nada y abrazarlo.":
            hide unum2duda
            show unum2blush
            unum "¡Oh!"
            "...."
    hide unum2enojo
    hide unum2duda
    show unum2blush
    unum "Hmmm."
    unum "¡Hey!"
    nj "¿Si?"
    hide unum2blush
    show unum1risa
    unum "He estado viendo a Sirius dormir... y creo que sueñan."
    unum "Se mueven y hacen gestos mientras duermen."
    unum "¡Por lo que sueñan!"
    hide unum1risa
    show unum2blush
    unum "Ah---- muchas gracias por darme este cambio."
    unum "Realmente eres lo mejor que me ha pasado en un largo tiempo."
    scene habitacion with dissolve
    "Unum comienza a acercarse para rodearte con sus brazos. Él es tan alto y su complexión es tan grande que no puedes evitar sentirte enano a comparación."
    "Su abrazo es cálido, el sentimiento de que en cualquier momento te puede arrancar un trozo de piel con sus dientes no deja tu cabeza por nada del mundo."
    unum "Realmente me gusta tenerte aquí."
    unum "Me gusta tu calor, tu olor y tus latidos."
    unum "Lo mortal y cambiante que eres."
    scene act2_u24 with dissolve
    "Unum suelta un poco su agarre para tomar una de tus manos."
    "Y la inspecciona mientras traza con su pulgar la costra que se te ha formado."
    unum "...y lo adaptable que eres."
    menu:
        "Suéltame por favor.":
            unum "Mmm, hahaha."
            "Unum te ignora."

        "...":
            scene act2_u23
            "Sin aviso lleva tu mano a su boca para lamerla."
            "Tu corazón late a mil, aunque no sabes si es por miedo o otra cosa..."
            unum "Ahhh~--"
            "Su cara se acerca peligrosamente a la tuya."

    scene act2_u24b
    unum "Pero también me dan ganas de comerte..."
    unum "Esa vez que te cortaste con el cuchillo pelando la fruta."
    unum "Fue de lo peor."
    unum "Si no me gustaras tanto, probablemente te abría destripado ahí mismo."
    "¿¿¿Qué clase de comentario es ese y por qué lo dice como si fuera un cumplido???"
    show act2_u24
    unum "Pero no te preocupes."
    unum "Te voy a cuidar."
    scene habitacion with dissolve
    "Sin explicar su razonamiento más allá de una sonrisa, Unum te planta un beso en los labios."
    scene negro with dissolve
    pause 0.5
    scene palaciounum with dissolve    
    "Más días pasan y te cuesta un poco creer lo rápido que crecen los niños... Te has acostumbrado a decirles 'los niños' y no por su nombre de origen"
    "Ahora que pueden caminar sueles pasar gran parte del día en el jardín junto con ellos, ya que aún es peligroso estar mucho tiempo con ellos dentro de un lugar cerrado."
    "La energía que ellos liberan es muy inestable y peligrosa para un cuerpo como el tuyo."
    "..."
    scene act2_u25 with dissolve
    "Son adorables."
    "Es adorable verlos jugar e interactuar entre ellos o con las chicas."
    "Aunque hay algo que te preocupa desde hace un tiempo ya, algo que ni Unum y las chicas han mostrado interés en explicar o comentar."
    "Por lo que supones que es algo normal... pero de igual forma te preocupa."
    "Y es que mientras más crecen más tendencias muestran a estar juntos, entrelazados por sus colas."
    "Pueden pasar días enteros sujetos a sus colas."
    menu:
        "Consultar a Unum.":
            "Le avisas a los niños que entrarás por un segundo y que volverás luego."
            scene pasillounum with dissolve
            "Buscas a Unum por los pasillos del templo y lo encuentras en la cocina junto con Solaris, quien le está dando consejos de cómo mejorar su última comida que ha hecho."
            scene cocinaunum with dissolve
            "Por curiosidad te detienes para escuchar un poco de su conversación."
            show solaris_normal at left with dissolve
            solaris "Tienes que mejorar tu canto, mi sol."
            solaris "Si lo haces desafinado, puede que llegue a afectar el sabor."
            "Su voz oscila entre la risa y la ternura, pero no puede evitar en soltar una pequeña carcajada al final."
            show unum2enojo at right with dissolve
            unum "¿Me estás diciendo que canto mal?"
            solaris "Tal vez."
            "Y solo eso falta para que Solaris deje salir la gran carcajada que estaba aguantando."
            hide unum2enojo
            show unum2duda at right
            unum "[nombrejugador], ¿tú piensas que hago los cánticos mal?"
            "Te sobresaltar un poco...No sabes cómo Unum pudo detectarte."
            solaris "¡No es que los haces mal! es solo que eres desafinado."
            menu:
                "Evitar la respuesta y preguntar por los niños.":
                    nj "uh..."
                    pass
                
                "Responder a favor de Unum y preguntar por los niños.":
                    hide unum2duda
                    show unum1risa at right
                    nj "No.... Unum canta bien."
                    "Solaris vuelve a reír, aún más fuerte. Y entre risas dice:"
                    solaris "¡Tampoco hace falta mentir para convivir!"
                    pass
                
                "Responder en contra de Unum y preguntar por los niños.":
                    nj "...sí."
                    hide unum2duda
                    show unum2enojo at right
                    "Unum hace un quejido, derrotado mientras Solaris ríe con más fuerza."
                    pass
            nj "¿Puedo preguntar algo? es sobre los niños."
            "Solo eso hace falta para que tengas la atención de ambos nuevamente en ti. Y no hace falta tener una respuesta verbal porque ellos y te miran esperando tu pregunta."
            nj "¿Es normal que tengan sus colar entrelazadas todo el tiempo?"
            unum "Es algo que hacen las estrellas binarias, uh... Solaris sabe más de eso."
            hide solaris_normal
            show solaris_enojo at left 
            solaris "Hmmm, nosotros no tenemos cola... pero según lo que nos ha dicho Duae, cuando la acompañábamos a nacimientos de estrellas binarias, la unión de ambas colar es su forma de mantener el equilibrio gravitacional de ambas."
            solaris "Así que funciona también como ah... ehh- un método de comunicación entre ambas estrellas."
            hide unum2enojo
            hide unum2duda
            hide unum1risa
            show unum3risa at right
            unum "Si, eso mismo."
            unum "No te preocupes, es normal."
            pass

            

        "Consultar a las chicas.":
            scene jardinunum with dissolve
            "Le avisas a los niños que entrarás por un segundo y que volverás luego."
            "No te hace falta buscar pues las divisas saliendo de su residencia, así que corres hacía ellas."
            "Son Ignis y Aeliana, solamente. Solaris no está con ellas."
            show ignis_normal at left with dissolve
            ignis "Pequeño humano, ¿ha pasado algo?"
            "Ignis pregunta con algo de miedo en su voz, ya que verte correr y jadear debe ser algo extraño de ver."
            nj "No, no es nada... es solo que me preocupa algo de los niños."
            show aeliana_feliz at right with dissolve
            aeliana "¿Qué es lo que te preocupa cariño?"
            "No importa cuantas veces Aeliana se refiera a ti como 'cariño', cada vez que lo hace sientes un hormigueo en tu estómago."
            nj "¿Es normal que tengan sus colas entrelazadas todo el tiempo?"
            hide aeliana_feliz
            show aeliana_serio at right
            "Ambas mujeres te observan en silencio antes de contestar, y la sonrisa de Aeliana flaquea por un segundo."
            aeliana "Las estrellas binarias usan su cola para estabilizarse y mantener su campo gravitacional en un buen estado."
            aeliana "Si no lo hacen, es posible que uno de ellos sea absorbido por el otro."
            aeliana "Al conectar sus colas, su poder se equilibra y reparte en partes iguales."
            ignis "También les ayuda a mejorar su vínculo emocional."
            hide aeliana_serio
            show aeliana_feliz at right
            aeliana "Cierto."
            aeliana "No es nada de qué preocuparse, ellos lo hacen instintivamente."
            pass
        
        "No consultar nada.":
            "No crees que sea nada TAN preocupante como para consultarles a los demás."
            "Si fuera algún problema, Unum ya lo habría discutido contigo para mantenerte al tanto."
            pass
    scene palaciounum with dissolve
    "El resto del día lo pasas descansando con las chicas mientras Unum se encarga de los niños."
    stop music fadeout 3.0
    "Ya no te da miedo dejarlos con él, pues Unum ha demostrado ser un muy buen cuidador. Increíblemente, contra todo pronóstico."
    scene pasillounum with dissolve
    play music "audio/woo_scary.WAV" fadein 2.0 volume 0.6
    "Llega nuevamente el domingo. Y Septem vuelve a aparecer..."
    "No te gusta que tú no puedas estar en la revisión del crecimiento de los niños. Pero Unum si, así que no te preocupas más de lo necesario. decidiendo esperar fuera de la sala."
    "..."
    "Pasan alrededor de 30 minutos, y ellos aún no salen."
    "...no es nada de preocuparse."
    "Cuando se cumple una hora, llegan las chicas a acompañarte. Sin decir nada, lo que hace que comiences a sudar frío."
    "¿Por qué está acá? ¿Y por qué se ven tan tensas?"
    show solaris_enojo at right with dissolve
    solaris "¿si no pasan la revisión...?"
    show aeliana_serio at left with dissolve
    aeliana "Calla. Ni se te ocurra."
    solaris "Lo siento."
    scene pasillounum with dissolve
    "¿Qué pasará si no pasan la revisión?"
    stop music fadeout 3.0
    "Estás a punto de entrar en pánico y preguntar a gritos a que se refieren cuando la puerta de la sala se abre."
    play music "audio/frozen_winter.WAV " fadein 2.0 volume 0.3
    "Los dos niños salen y corren a ustedes riendo, como si festejaran algo que desconoces."
    show septem2normal at left with dissolve
    "Septem sale con ambos brazos detrás de su espalda, detrás de él viene Unum."
    show unum1risa at right with dissolve
    unum "¡Ya tienen sus nombres!"
    hide septem2normal
    hide unum1risa
    show septem2incomodo at left
    show unum2enojo at right
    septem "Todos los presentes: Unum; Alnitak; Mintaka y Alnilam, deberán referirse con esos nombres a partir de ahora. Tienen estrictamente prohibido nombrarlos por sus nombres de origen."
    "...Una presión inexplicable atraviesa tu cuerpo. Por la tensión en el rostro de Unum, sabes que no has sido el único en sentirla."
    hide septem2incomodo
    show septem2normal at left
    septem "Sirius, pueden presentarse."
    scene act2_ufinal with dissolve
    noor "¡Mi nombre es Noor!"
    shams "Y yo me llamo Shams."
    "Complacido y sin agregar nada más, Septem se despide con una voz monótona y distante. Aunque sus movimientos y su rostro mantienen la elegancia propia de su ser..."
    "...¿Por qué él es el único que puede referirse a ellos por su nombre impuesto?"
    "¿Y Unum no lo tiene permitido?"
    "Temes por la razón de tal comando... pero por ahora no puede hacer nada."
    noor "¿Podemos ir al jardín a jugar?"
    "Tu atención se centra en tus niños, quienes te miran suplicantes y con sus colas entrelazadas."
    menu:
        "Primero deben comer.":
            "La respuesta que obtienes es un coro de berrinches infantiles."
            "Pero aceptan viendo que no sacarán nada haciendo eso."
        
        "Está bien.":
            "Shams y Noor se van corriendo por el pasillo hacía el jardín."
            "En todo momento, sus colas yacen entrelazadas."

    "La vida aquí no es tan mala..."
    #Tres semanas de cuidados. PRIMERA SEMANA: NIÑOS.
    #Mostrar la residencia de las esposas.
    #La marioneta te dice que no es bueno escuchar a Septem.
    #Tienes la opotunidad de sabotear los chequeos de Septem. Y hablar con los niños, decirles que no confien en Septem.
    scene negro with dissolve
    stop music fadeout 3.0
    "............"
    "........................"
    scene jardinunum with dissolve
    play music "audio/fell.mp3" fadein 2.0 volume 0.3
    "Las palabras de Septem no te dejan en paz. Con cada silencio o tiempo muerto, su voz retumba y persiste en tu cabeza, recordándote que existe algo más profundo y preocupante que simplemente jugar a la casita con Unum y sus esposas."
    "...No podía ser todo tan color de rosas."
    "Septem tiene que estar moviendo los hilos por debajo de toda acción del Estandarte del sol."
    "Supones que podrías preguntar de que va todo esto. Sentarte con Unum un día a hablar con seriedad acerca de la razón de tener descendientes."
    "Pero..."
    "Te da miedo. Decepcionarte al escuchar su respuesta. Miedo a que Unum esté actuando todo. Que esa imagen tan paternal que tienes de él se destruya. Pero más te duele que los niños sean solo un objeto a usar para planes que desconoces."
    "Te duele un poco, más de lo que estás dispuesto a admitir."
    ignis "Estoy impresionada..."
    scene ignis with dissolve
    "La voz de Ignis te interrumpe de tus sombríos pensamientos y teorías fatalistas." 
    "Ella está sentada a tu lado con un vaso en mano, mirando en dirección hacia el jardín. Atenta a cada movimiento de los niños, esperando el momento de interrumpir si es necesario."
    "Shams y Noor juegan a las luchas. Al inicio, te preocupabas por su integridad, pronto te diste cuenta de que ellos no salen afectados en lo más mínimo durante y luego de sus peleas."
    ignis "Estrellas que cambian y crecen con el tiempo... jamás me habría imaginado."
    "Ella gira su cabeza para mirarte, es una lástima que no puedas apreciar su expresión. La máscara que trae te impide ver sus gestos y rostro."
    ignis "Hoy han crecido tres centímetros más."
    ignis "Y Shams a ganado más masa corporal."
    "Su voz es cálida, casi tierno. Posee ese tono maternal de quien está orgullosa de sus hijos."
    menu:
        "Tengo miedo de que crezcan muy rápido.":
            ignis "..."
            ignis "Entonces deberías apreciar cada momento."
            "Desvía su rostro, optando en poner su foco en otro lugar. Cualquiera menos tú."
            "Aún así, su voz sigue siendo cálida y calmada."
            ignis "Y guardarlos con cariño en tu memoria."
            ignis "Ellos crecerán rápido, y no hay nada que podamos hacer para detenerlo."
        
        "Noor es muy pequeño...":
            ignis "¿Te preocupa aquello?"
            menu:
                "Sí.":
                    "Ignis suspira, apretando con fuerza su vaso contra su regazo y manos."

                "No.": 
                    "Ignis no responde, pero su silencio es más que suficiente para hacerte entender que no está dispuesta a seguir con el tema."

        "¿No existen niños en el Jardín?":
            ignis "¿Crías como las tuyas? ¿Crías de los súbditos? no..."
            ignis "Son contraproducentes para la mantención de cada dominio. Una distracción para la labor de nosotros..."
            ignis "Los únicos súbditos que podían tener crías eran los de la señora Sextam."
    
    "Ignis aprieta el vaso con más fuerza. Por un instante, crees que va a romperse."
    ignis "Debo retirarme. Es tiempo de que vuelvas a la residencia de Unum."
    ignis "No--- ya no soporto tu olor."
    "Sabes que no lo dice con desprecio. Pero aun así duele."
    "Unum te lo explicó antes, y tú ya medio lo intuías desde antes."
    "Tu carne... tu cuerpo... es como un plato refinado y delicioso para ellos. Ya sea humanos de otros mundos o placebos creados aquí."
    "Algo que pueden comer, pero que tienen prohibido probar, ya que esos recursos son exclusivamente para los Estandartes."
    "Fuente principal de energía para los altos mandos."
    "Y un manjar inalcanzable para los sirvientes de cada dominio."
    "..."
    scene jardinunum with dissolve
    "No tiene caso seguir pensando en ello. Podrás ser un platillo codiciado para los habitantes del Jardín, incluidos para los que comparten techo contigo." 
    "Tanto Unum como sus esposas te ven como una potencial comida, pero... ves que realmente lo intentan."
    "Hacen el esfuerzo de no devorarte cuando te ven o pasan el tiempo junto a ti."
    "Ignis muchas veces evita pasar demasiado tiempo contigo por este motivo."
    "Y Unum jamás se salta los placebos de los domingos. Mañana tiene su reunión en el hotel para recibir su dosis semanal."
    "Mañana es domingo. Lo que significa que antes de ir al hotel, Septem vendrá a chequear el estado de los gemelos."
    "La ansiedad te atrapa el pecho con tan solo pensar en lo que podrá pasar mañana. Qué es lo que dirá Septem y qué pasará con Noor y Shams luego."
    "Dos pequeñas manos te rodean el cuello, trayéndote nuevamente a tierra. Ignis ya no está y en su lugar tienes a los niños sobre tu espalda y tu regazo."
    show shamsynoor_normal with dissolve

    shams "Ignis dijo que nos llamaste."
    shams "¿Pasó algo?"
    "Pregunta Shams dejando caer todo su peso sobre ti, quitando el aire de tus pulmones. Ignis tiene razón... Tendrás que enseñarle a medir su fuerza."
    "Al menos cuando se trate de ti."
    menu:
        "Eso hora de irnos.":
            hide shamsynoor_normal
            show shamsynoor_enojado
            noor "Pero---"
            noor "Solaris prometió jugar conmigo."
            shams "No, ¡dijo que jugaría conmigo!"
            shams "Tú querías cocinar con Aeliana."
            noor "¡Eso fue ayer!..."
            "Shams empuja a Noor, llamándolo mentiroso."

        "Tienen que prepararse para mañana.":
            hide shamsynoor_normal
            show shamsynoor_enojado
            shams "No quieroooo."
            shams "Es muy aburrido hablar con su santidad Septem."
            noor "A mí me gusta..."
            "Shams hace le saca la lengua a Noor y murmura por lo bajo que él es un aburrido, al igual que Septem."
    scene jardinunum with vpunch
    "Ella sale corriendo bajo la mirada apenada de Noor. Quien no espera a que tú reacciones y va tras de Shams con el ceño fruncido. Buscando venganza."
    "Ambos se dirigen a la residencia de Unum."
    "Contemplas por última vez la residencia de las chicas antes de seguirlos. Sientes curiosidad por ese lugar, y ya mirarla desde fuera no te basta." 
    "Hay días en que tienes que morderte la lengua para evitar preguntar si te dejan entrar. Pero te aguantas..."
    "Mucha curiosidad tendrás pero no eres tan tonto como para saber que eso sería peligroso."
    stop music fadeout 1.5
    "..."
    scene palaciounum with dissolve
    play music "audio/hope.WAV" fadein 2.0 volume 0.4    
    "Ya en casa, te enteras de que Unum ha vuelto de su reunión con Septem. Y como siempre, trae un montón de libros de vuelta."
    "Últimamente, las reuniones de Unum y Septem han aumentado, son más frecuentes y tienen una duración que cada vez aumenta más... eso te molesta un poco." 
    "Porque gran parte del día donde ocurren estas reuniones, quedas a cargo de los niños. Y ellos demandan más de lo que puedes dar."
    scene unum_libro with dissolve
    unum "[nombrejugador], ¿Sabías que es bueno leerle historias a los niños cuando están en pleno crecimiento?"
    "Pero basta con que Unum aparezca con esa sonrisa satisfecha para que todo tu enojo se esfume."
    "Unum se planta a tu lado, libro en mano, dispuesto a presentarte su contenido."
    "Por la portada te das cuenta de que se trata de un libro para niños de entre 5 a 10 años, humanos claro. Si bien, no eres capaz de leer el título, es más que obvio que es un libro de aventuras o fantasía."
    scene unum_libro2 with dissolve
    "Mientras él cuenta todo lo que vio en la biblioteca de Septem, tú ojeas el contenido del libro."
    "Más imágenes que texto. Ideal para niños con poca capacidad de concentración... como Shams. Confías en que los dibujos la mantendrán interesada."
    scene palaciounum with vpunch
    "Cierras el libro de golpe, provocando que Unum calle de inmediato. Tú sueltas un suspiro largo, exhausto."
    menu:
        "¿Hay algo importante que yo deba saber?":
            show unum3callado with dissolve
            "..."
            hide unum3callado
            show unum1normal
            unum "No por ahora."
            unum "Todo está bajo control."
            unum "Y Septem está satisfecho con los resultados."

        "Parece que te lo pasas muy bien con Septem.":
            show unum3callado with dissolve
            "Él te mira con desconcierto, tan por sorpresa lo has tomado que no sabe como responder."
            "Hasta parece que se le ha olvidado como hablar."
            hide unum3callado
            show unum1incomodo
            unum "No voy por opción..."
            unum "Pero..."
            hide unum1incomodo
            show unum3callado
            "¿¡PERO?! ¿Te está jodiendo, no? ¿¿¿¿¿¿??????"
            hide unum3callado
            show unum1risa
            unum "No es tan malo como creí."
            unum "Además, me deja llevar lo que quiera de su biblioteca."
            "Increíble... tu 'esposo' se vende por unos libros. Que poco respeto por su honor." 
            "Estás seguro de que gran parte de la reunión se resume en Septem insultando a Unum de una forma tan sutil, que Unum no se da cuenta de aquello..."
            "O también puede ser que gran parte de la reunión es Unum quien le hace pasar un mal rato a Septem."
            "No sabes cual de las dos es peor."
        
        "Te extrañé.":
            show unum3callado with dissolve
            "Él te mira perplejo, tan por sorpresa lo has tomado que no sabe como responder."
            "Hasta parece que se le ha olvidado como hablar."
            "Su boca se abre y cierra, buscando la respuesta correcta para dártela."
            "No se lo esperaba."
            hide unum3callado
            show unum2blush
            unum "¡Yo también!"
            hide unum2blush
            show unum2enojo
            unum "Le he dicho a Septem que tener tantas reuniones me está haciendo perder tiempo contigo y con lo niños, pero---"
            unum "Necesitamos hablar y planear todo al pie de la letra."
            hide unum2enojo
            show unum1normal
            unum "Cuando esta acabe podremos tener todo el tiempo del día."
            unum "Lo prometo."

    hide unum1normal
    hide unum1risa
    show unum3serio
    "Unum se aclara la garganta."
    "Luego toma una bocanada de aire y sus palabras saltan tal como si de un globo desinflándose se tratase."
    unum "A partir de mañana los niños deberán pasar por separado para tener los chequeos con Septem."
    "{sc=2}No creo que sea buena idea.{/sc}"
    "{sc=2}Cualquier cosa que sea lo que Septem busca, no le permitiré usar a los niños.{/sc}"
    "{sc=2}Son míos, no suyos.{/sc}"
    menu:
        "Quiero entrar con ellos.":
            hide unum3serio
            show unum2duda
            unum "...uh."
            unum "No sé si puedas..."
        
        "No irán a menos que yo sepa lo que hacen ahí.":
            hide unum3serio
            show unum3callado
            unum "..."
            hide unum3callado
            show unum1incomodo
            unum "Así no funcionan las cosas..."
        
        "No confío en Septem.":
            unum "Él está haciendo todo lo que puede para restaurar el Jardín..."
            nj "No me importa eso, me importan los niños."
            hide unum3serio
            show unum3callado
            unum "..."
            hide unum3callado
            show unum3serio
            unum "A mí igual me importan..."
            nj "Entonces demuéstralo."
            hide unum3serio
            show unum2enojo
            unum "¡Lo hago! eso hago."
            "Quieres decirle que no lo parece, pero te detienes al ver su cara."
            "Está dolido. Pero no te disculpas."

        "¿No les pasará nada, cierto?":
            unum "¿En los chequeos?"
            unum "No claro que no."

    scene palaciounum with dissolve
    "No importa cuántas veces le preguntes o interrogues a Unum acerca del plan que Septem tiene con los niños, él siempre te da respuestas vagas. Que rallan lo absurdo."
    "'Los hará subir de rango'; 'Serán una divinidad, dejarán de ser mortales'; 'Solo hay que esperar al momento adecuado, aún son muy pequeños'."
    "Y tú no tienes como seguir insistiendo pues Unum siempre encuentra una excusa para salir de la situación."
    show unum2enojo with dissolve
    "Pero hoy Unum parece no aguantar más y se compromete a preguntarle a Septem si tú puedes estar presente en el próximo chequeo."
    hide unum2enojo
    show unum3serio
    unum "No prometo nada..."
    unum "Septem es quien decide."
    scene habitacion with pixellate
    "El resto del día te encierras en tu habitación. Sientes que vas a explotar en cualquier momento frente a cualquier incidente mínimo, y no quieres hacerlo frente a los niños." 
    "Lo mejor es que te quedes aquí, por lo menos hasta mañana. Así sacas provecho de descansar, tu cuerpo y manos agradecen la decisión."
    "..."
    "Te enoja que Unum no haga nada frente a esta situación."
    "Y por otro lado te llama la atención el que Estandarte del sol sea tan precavido en todo lo que hace."
    "Ya no se ve tan imponente como tu creías. Demonios, incluso ahora ha dejado de ser impulsivo en todo sentido."
    "Y eso se debe a la constante presencia de Septem."
    "Siempre es: Septem dice esto; Septem tiene que saber de aquello; si Septem nos concede el permiso entonces..."
    "Ya estás harto."
    "Lo peor es que Unum le resta importancia o hace ver que tu enojo es algo gracioso o interesante."
    "Como si de un perro haciendo una gracia fueras..."
    "Tal vez seas eso."
    "Solo una mascota que no tiene una voz o voto en nada de lo que sucede en esta casa."
    "Adoptada por un solo propósito y a la espera de que el dueño se aburra."
    "..."
    "No sabes que es peor, si ir con Unum o seguir comiéndote el coco en un constante sobrecuestionamiento de todo y nada."
    "Antes de poder decidir, tu puerta es golpeada tres veces."
    show unum1risa at center with moveinleft
    "La ilusión de tener privacidad no dura más de cinco segundos, y verlo entrar como si fuera el dueño de todo es echar más sal a la herida."
    hide unum1risa
    show unum1normal 
    unum "Los niños ya están durmiendo."
    "Proclama él, con energía. Ajeno a todo lo que está pasando dentro de ti."
    "Camina con todo el derecho del mundo sobre tu espacio, sin prestar atencion a su alrededor ni a ti realmente."
    "O tal vez se está haciendo el desentendido. Debe serle más fácil así."
    hide unum1normal
    show unum3risa
    unum "Hablé con Septem---"
    "Si escuchas una vez más el nombre de Septem, juras que---"
    unum "Y dijo que no hay problemas con que mañana entres con los niños al chequeo."
    unum "Pero a mí no me dejó hacerlo."
    "Confiesa haciendo un puchero."
    "La noticia debería de alegrarte, pero no lo hacer completamente."
    menu:
        "¿Por qué haces todo lo que Septem dice?":
            hide unum3risa
            show unum1incomodo
            unum "Ah--"
            hide unum1incomodo
            show unum1risa
            unum "HAHAHAHAHAHA."
            "Unum se sujeta el abdomen, sacudido por una carcajada tan profunda que temes que algo en su interior o exterior se desgarre."
            hide unum1risa
            show unum1incomodo
            unum "¿Crees que soy un lamebotas?"
            "Pregunta con incredulidad."
            "...Lo ha dicho él. Tú no."
            "Pero lo es. Y del tipo más peligroso: el que no acepta que lo es."
            "Si Septem dictaminase que hoy el sol no debe salir, Unum movería cielo y tierra para que se cumpla la orden. Maldito LAMEBOTAS."
            hide unum1incomodo
            show unum2enojo
            unum "Aquí, una palabra es un mandato."
            unum "Septem gobierna todo ahora que tiene un cuerpo. Basta con que pronuncie tu nombre y una orden."
            unum "Estoy obligado a obedecer.   {size=*1.5}¡Por ley!{/size}"
            "Se ha puesto a la defensiva, lo que significa que por lo menos, le has dado en el orgullo de alguna u otra manera."
            unum "{size=*0.7}Si tan solo Septem volviera a ser un ser intangible...{/size}"
            menu:
                "¿Qué has dicho?":
                    hide unum2enojo
                    show unum1incomodo
                    unum "Ah---"
                    hide unum1incomodo
                    show unum3callado
                    "Por un instante, Unum guarda silencio. Sin palabras para ofrecer una respuesta, lo has tomado desprevenido."
                    hide unum3callado
                    show unum3serio
                    unum "Hubo un tiempo en que Septem no tenía cuerpo..."
                    unum "Al principio de todo."
                    unum "Sin boca, no podía mandar."
                    unum "Y era Nulla quien hablaba por él. Era como su vocero."
                    unum "Y teniamos más libertad, hasta que apareció con un cuerpo."
                    unum "Sextam dijo que se lo ha prestado... pero no le creo."
                    "Unum hace una pausa larga, como si estuviera recordando que fue que lo llevó a hablar de aquello."
                    "Hasta que exhala mientras hace una mueca chistosa."
                    unum "Así que no---"
                    unum "No soy un lamebotas."
                    "No lo dice para convencerte a ti. Lo dice como si intentara convencerse a sí mismo."


                "...":
                    hide unum2enojo
                    show unum3callado
                    unum "..."

            ".............."
            hide unum3serio
            show unum3callado
            "El silencio es pesado, y sinceramente, no sabes como rescatar la conversación."
            "Por lo que decides ponerte debajo de las sábanas, dispuesto a terminar el día."
            "Él viendo tu acción se siente a los pies de la cama y te mira, debatiéndose entre abrir la boca o no."
            hide unum3callado
            show unum3blush
            unum "¿Puedo acompañarte mientras duermes?"
            menu:
                "No...":
                    scene habitacion with dissolve
                    "Respetando tu decisión, abandona el lugar. Cerrando con suavidad la puerta."
                    pass

                "Sí...":
                    hide unum3blush
                    show unum2blush
                    "Unum sonríe y se acuesta a tu lado."
                    pass

        "Quiero estar solo... vete.":
            hide unum3risa
            show unum2enojo
            unum "¡¿Qué?!"
            unum "¿Ya te has aburrido de mí?"
            unum "He hecho todo lo que aparece en los libros de romance que están en la biblioteca."
            hide unum2enojo
            show unum3callado
            nj "Tienes que dejar de leer y tomar todo como si fuera la verdad absoluta..."
            hide unum3callado
            show unum1incomodo
            unum "Tienes razón..."
            unum "Voy---"
            hide unum1incomodo
            show unum3callado
            "Unum retrocede, totalmente desconcetado. No esperando esa respuesta por parte tuya."
            hide unum3callado
            show unum3blush
            unum "Buenas noches."
            unum "Espero que descanses."
            "Tienes que morderte el interior de las mejillas para soportar la visión que tienes frente a ti."
            "Debería ser ilegal que Unum pueda hacer tantas expresiones con su rostro y que cada una de ellas sea tan expresiva."
            "Prácticamente parece un cachorro que ha sido gritoneado y expulsado por su dueño a otra habitación."
            "Como lo odias..."
            "..."
            "Sin decir nada más, él abandona el lugar. Cerrando con suavidad la puerta."
            pass
    hide unum3blush with dissolve
    hide unum2blush with dissolve
    scene negro with dissolve
    stop music fadeout 1.5
    "El sueño no se hace esperar y te duermes al instante."
    "                                  .   .   .   .                                           "
    scene camaunum with dissolve and vpunch
    play music "audio/calamity.WAV" fadein 1.0 volume 0.4
    "Es domingo. Tu cuerpo no ha tenido tiempo de acostumbrarse al nuevo día cuando Shams entra en la habitación, lanzándose de lleno sobre tu cama. Al caer, te aplasta una costilla con la rodilla mientras grita con impaciencia."
    shams "¡Nos están esperando!"
    "Entre la confusión y el tironeo insistente de tu camisa, apenas logras mantener tus ojos abiertos mientras Shams vomita explicaciones a medias."
    "Sin darte tiempo para preguntas, te arrastra fuera de la cama, repitiendo sin descanso que se hace tarde, que hay que apurarse, que Septem los quiere a ambos presentes ¡Ahora mismo!"
    "La imitación de la voz de Septem echa por Shams es la que te basta para comprender completamente: es día de chequeo semanal."
    "Antes de poder darte cuenta, ya estás cruzando los pasillos que dan al 'ala médica'. Shams abre la puerta sin detenerse a tocar ni a anunciar su presencia."
    scene unum_reunion with dissolve
    septem "Debes tocar antes de entrar."
    shams "Le dijiste a papá que estabas apurado."
    "Su respuesta es inmediata, importándole casi o nada lo que el rubio piense o haga con ello." 
    "Él, en cambio, decide ignorar. Sentado con la espalda recta frente a Unum, apenas desvía la mirada a ti, ni siquiera hace un gesto para saludarte."
    "Es Unum quien te recibe, levantándose con una sonrisa amplia y tierna, que muestra sus dientes blancos y filosos. Al acercarse a ti, te planta un cálido beso en la mejilla, murmurando un 'buenos días'" 
    "Apenas tiene tiempo de decirte aquello antes de que la mirada de Septem lo obligue a marcharse de la habitación."
    scene salaunum with dissolve
    "Shams corre al rincón donde descansan los instrumentos: la balanza, la cinta métrica, una camilla, entre otros." 
    scene unum_chequeo1 with dissolve
    "Parece que ya conoce la rutina, pues se sienta en la camilla a esperar. Mientras tanto, Septem se pone de pie con libreta y lápiz en mano. Se instala junto a la niña y empieza a registrar datos."
    "Le indica que levante los brazos, que estire las piernas, que respire profundo. Todo lo hace con una precisión casi mecánica y clínica." 
    "Anota lo necesario, sin hacer comentarios más allá de lo funcional."
    scene salaunum with dissolve
    show septem2incomodo with dissolve
    septem "Unum me ha dicho que querías formar parte de los chequeos."
    "Es la primera vez que te dirige la palabra desde que entraste." 
    "Ya habías asumido que te ignoraría hasta que el chequeo de Shams acabara."
    "Aunque, en cierto modo lo hace a medias, ya que habla sin mirarte de forma directa."
    hide septem2incomodo
    show septem1triste
    septem "¿No confías en mí?"
    menu:
        "¿Por qué debería hacerlo?":
            hide septem1triste
            show septem1normal
            septem "Hmmm..."
            hide septem1normal
            show septem2risa
            septem "Porque no tienes opción."

        "No.":
            hide septem1triste
            show septem1normal
            septem "Oh."
            septem "Al menos eres honesto."

        "Solo quiero saber cómo son los chequeos.":
            hide septem1triste
            show septem2incomodo
            septem "..."
            septem "Me alegra que te preocupes por tus hijos..."
            septem "Siendo sincero, no me lo esperaba."

    scene salaunum with dissolve
    "Shams, distraída por completo de la conversación, juega con uno de los estetoscopios." 
    "Se lo pone en el cuello, lo gira, lo estira y muerde. Septem tiene que quitárselo de las manos para evitar que lo rompa."
    "luego, escribe algunas líneas más, para terminar con su mirada sobre ti."
    show septem2incomodo with dissolve
    septem "Independiente de lo que pienses, no tienes más opción que seguir lo que se te pide."
    septem "Si deseas sobrevivir a este mundo, necesitas confiar en mí."
    hide septem2incomodo
    show septem1risa
    septem "De lo contrario, tu marioneta no tardará en quedar obsoleta."
    septem "Hoy son tus manos. Mañana será el brazo completo. Después, vendrán los pies. Y luego las piernas."
    hide septem1risa
    show septem2normal
    septem "Te quedarás reducido a un cuerpo inútil, que solo servirá como carne para nosotros..."
    septem "Un placebo a punto de expirar."
    septem "Y cuando eso suceda, perderás la única forma que tienes de permanecer en este plano."
    scene unum_chequeo1 with dissolve
    "Septem guarda silencio por unos segundos, mirando a Shams. Luego dice una sola palabra."
    septem "Cola."
    scene unum_chequeo2 with dissolve
    "Extiende la mano, esperando a que Shams haga lo pedido. Ella obedece de inmediato, levantando su cola con para dejarla reposar sobre la palma de Septem."
    "Estás a punto de intervenir. Sabes que las colas de estrellas como Shams son peligrosas: inestables y dañinas, energía pura capaz de quemar la piel de cualquier entidad sin importar el rango. Incluso Unum, ha salido herido antes."
    "Pero la ver que Septem no reacciona con dolor, te detienes y observas."
    "No ocurre nada. No hay piel quemada ni dolor reflejado en los ojos de Septem. Él sostiene la cola de Shams como si fuese otra extremidad más." 
    "La examina con calma y anota en su libreta."
    "¿Cómo es que pudo tocarla así sin más?"
    "¿Serán sus manos?"
    "No..."
    "Las tuyas también presentan una condición similar... y tú claramente no puedes tocar sus colas sin presentar quemaduras de grado 3 mínimo."
    septem "¿Pasa algo?"
    scene salaunum with dissolve
    show septem1risa
    septem "Si sigues con la boca abierta se te meterá una mosca..."
    septem "Ciérrala."
    menu:
        "¿No te ha hecho daño?":
            hide septem1risa
            show septem1normal
            septem "Hmmm."
            hide septem1normal
            show septem2normal
            septem "No."
            septem "Nadie ni nada puede hacerme daño."
            "Dice él restándole importancia."
            "Esperas una explicación, pero nunca llega. Quedando más confundido que antes."
        
        "Perdón...":
            hide septem1risa
            show septem2normal
            septem "Mmmm."
            "Septem sonríe, complacido."

    scene salaunum with dissolve
    show noorchiquito_normal at left with moveinleft
    "El chequeo termina y Shams sale para que Noor pueda entrar."
    "Noor a diferencia de Shams parece estar más a gusto con lo meticuloso que es Septem. Mientras ella fue inquieta, Noor observa y espera a que el rubio comande."
    show septem1normal at right
    septem "Vas a tener que comer menos."
    "Le dice luego de terminar el chequeo."
    nj "¿Qué?"
    nj "No. Noor necesita comer más."
    hide septem1normal
    show septem2enojo at right
    "Septem te mira como si fueras un loco, y estuvieras hablando disparates."
    hide septem2enojo
    show septem2incomodo at right
    septem "Sirius, debes comer menos."
    hide noorchiquito_normal
    show noorchiquito_hablando at left
    noor "Está bien."
    hide noorchiquito_hablando and septem2incomodo with dissolve
    "Si tuvieras la fuerza y el poder de gritarle o darle una cachetada, lo harías. Pero te traería más problemas que otra cosa."
    scene salaunum with pixellate
    "No tienes derecho a rebatir o pedir explicaciones pues Septem los expulsa de la habitación con un solo aplauso. Ambos transportados fuera."
    "La puerta está cerrada y cuando te giras para volver a entrar, decidido a encarar al rubio. Él ya no se encuentra dentro."
    "Se ha ido."
    "Por un lado, eso es bueno... ya estás harto de él."
    "No lo quieres ver más en tu casa. Al menos por los próximos 7 días."
    stop music fadeout 1.5
    "¡Uhg!"
    scene palaciounum with dissolve
    "El resto del día lo pasas acompañando y jugando con los niños. Esperando a que cuando Unum vuelva del hotel, tenga la panza llena y sin deseos de comerte."
    play music "audio/fell.mp3" fadein 2.0 volume 0.3
    "..."
    menu:
        "Esperar a Unum en tu habitación.":
            "Matas tiempo en tu habitación."
            "No haces nada más que esperar."
            "Hasta que los niños irrumpen tu tranquilidad y te piden que los acompañes a dibujar un rato."
            "Solo un ratito."
            "..."
            "No te queda de otra que aceptar..."
            pass

        "Explorar.":
            call menuexplorar_unum from _call_menuexplorar_unum_2
    "..."
    scene unum_dibujo with dissolve
    "Ver como compiten por tus elogios es algo gracioso al inicio. Pero cuando te das cuenta de que ambos están compitiendo de forma seria, y con el objetivo de pisotear al otro. Los detienes en seco."
    "Les llamas la atención, y les adviertes que si siguen así, tú darás por terminada la actividad."
    "Ambos se disculpan y vuelven a dibujan, ahora más tanquilos."
    "Las horas pasan, y ya no estás tan enojado con Unum..."
    "O eso crees."
    "Los niños ya van por su sexto dibujo cuando Unum hace acto de presencia."
    "Y la escena que tienes frente a tus ojos es tan absurda como cómica, ya que parece como si Unum llegase del trabajo a casa."
    scene unum_dibujo2 with dissolve
    "Shams y Noor lo reciben felices y compitiendo por quien habla más fuerte para que Unum les haga caso."
    "Él hace lo que puede para escuchar a ambos, pero pronto se vuelve imposible con Shams queriendo toda la atención. Tira de la túnica de Unum hasta desajustarlas, mientras Noor mira con rechazo la acción de su hermana."
    "A Unum poco le importa, y no entiendes como puede ser tan permisivo..." 
    scene unum_dibujo3
    "Es Noor quien deja de hablar, prefiriendo volver contigo para seguir con su dibujo. No puedes evitar ver su carita apenada mientras dibuja."
    "Por lo que intentas alegrarlo hablando cosas sin sentido y tirando chistes que dan más pena que gracia. Pero eso a Noor le termina sacando un par de risas."
    "..."
    "Ambos terminan sus dibujos y comparan, Noor es mucho mejor que tú. Le echas la culpa a tus manos... si las tuvieras en mejor estado, tal vez tus dibujos serían mejores."
    "Noor deja la mesa para ir a su habitación, y Shams sigue ahí, dándole un monólogo a Unum."
    "El pobre te mira, pidiendo auxilio con sus ojos y..."
    "Decides intervenir."
    scene palaciounum with dissolve
    "Eres tú el que tiene que ponerle un freno a Shams para que deje a Unum tranquilo. Ella te obedece al instante, sin reproche alguno."
    "Quedas a solas con Unum."
    scene unum_ojo with dissolve
    "Se acerca con la intención de que le des un beso de bienvenida."
    menu:
        "Besar su mejilla":
            scene unum_ojo1
            "El contacto con sus mejillas es cálido, ofreciéndote una sensación que viaja desde sus labios hasta tu estómago."
            "Realizar esta clase de saludo con Unum, reservados para gente a la que quieres o tienes confianza, se siente bien."
            "Casi algo íntimo, un secreto que solo ustedes dos guardan."
            "Cultura humana que no existe en otros dominios. Los besos en la mejilla no son un concepto conocido aquí, y eso te hace sentir de cierta manera orgulloso."
            "Orgullo de que le enseñes cosas tan mínimas y que él lo tome con tanta seriedad, al mismo tiempo que las aprecie y atesore en su día a día."
        
        "Besar sus labios.":
            scene unum_ojo1
            "Es un beso casto, nada subido de tono o pasional. Un saludo íntimo que has llegado a compartir con él un par de veces."
            "Y él parece ya haberse acostumbrado tanto a ello, que lo demanda cada vez que llega del hotel."
            scene unum_ojo
            "Hasta crees que se ha vuelto adicto a ellos. Pues siempre lo atrapas mirándote a los labios luego de hacerlo... te preguntas si es porque quiere otro o porque quiere comerte de a poco."
            "Probando y tanteando, pedacito a pedacito. Haciendo durar su ración hasta decidir cuando comerla por completo."
            "El pensamiento hace que te retuerzas de manera involuntaria."
            "Debe haber algo mal contigo. O este mundo te ha corrompido por completo, ¿Dónde quedó tu descencia?."

        "Desviar la cara.":
            scene unum_ojo3
            "Unum se detiene cuando ve tu reacción. Se disculpa algo avergonzado e intenta hacer conversación para olvidar tu rechazo."
    
    scene unum_ojo1
    unum "Mira lo que les traje a los niños."
    "Dice él, tan contento que por un segundo se te olvida con quién estás tratando."
    scene unum_ojo2 with dissolve
    "Así que cuando Unum saca de su bolsillo un pañuelo manchado con sangre, un balde de agua fría cae sobre ti, figurativamente, claro."
    "No podía ser un juguete o un jodido perro de mascota, si es que siquiera existen aquí los perros."
    "NO. Tenía que ser dos ojos de color café que te miran. Crudos, sanguinolentos y viscosos ojos que yacen inertes en el pañuelo."
    "Es tan asqueroso que no puedes evitar empujar a Unum lejos de ti."
    "Y él tiene el descaro de soltar un quejido, confundido por tu acción."
    unum "¿No te gustan?"
    show unum_ojo with dissolve
    "Toma uno con sus dedos, y lo acerca a su rostro en búsqueda de detalles que tú no quieres conocer. Lo aprieta un poquito, es más firmes de lo que te imaginabas..."
    unum "Mmmm, debe ser porque ahora no tienen ese brillo que traían cuando estaban conectados al cuerpo del placebo."
    scene palaciounum with dissolve
    "La imagen mental de Unum arrancando los ojos de una persona--- o placebo, lo que sea, es más grotesca que los ojos en sus manos. Porque te lo puedes imaginar con todo lujo de detalles, todo mientras Unum sonríe en el proceso."
    show unum2blush with dissolve
    unum "Se parecían a los tuyos, pero sin ese puntito blanco que tienes, que cambia el tamaño cuando te sorprendes..."
    unum "Me gustan mucho los tuyos..."
    unum "¿Sabrán igual que los demás?"
    menu:
        "¡No son para que los comas!":
            nj "¡Los necesito para ver!"
            hide unum2blush
            show unum2feliz
            unum "Ahh-- pero solo con uno es suficiente para que puedas hacer eso."
            unum "Al igual que tus riñones."
            unum "Lo leí una vez."
            hide unum2feliz
            show unum1risa
            "No te gusta cómo lo dice. Las palabras que salen de su boca son fuertes, rozan lo criminal." 
            "Pero las pronuncia con una banalidad tal que el contraste entre el contenido y la forma en que lo expresa te genera un malesta físico y emocional."
            "Unum no ve el problema. Lo que propone--- su idea, tiene lógica para él. Después de todo, es verdad: con un solo ojo basta para ver. Y, en cierto sentido, no está equivocado."
            "Claro, eso si ignoramos todo lo que implicaría el proceso: que te arranquen un ojo sin anestesia, contener la hemorragia, cauterizar la herida si es necesario, y luego aprender a adaptarte a percibir el mundo con una sola fuente de visión." 
            "Nada de eso parece entrar en su razonamiento."
            "Supones que no puedes culparlo. Es evidente que su fisiología no se parece a la tuya, así que no alcanza a imaginar lo que significaría realmente quitarte un ojo."
            nj "No te lo voy a dar."
            hide unum1risa
            show unum2duda
            "Su rostro se apaga por una fracción de segundo, apenado a que le hayas dicho que no."
            "Pero lo entiende."
            "Y eso para ti, es fascinante."
            scene palaciounum with dissolve
        
        "¿Cómo sabrán los tuyos?":
            "Tu pregunta sale naturalmente, con el mismo tono e intención que Unum ha preguntado antes."
            hide unum2blush
            show unum2feliz
            "Él, te mira con los ojos bien abiertos. No se lo esperaba."
            "Excelente, magnífico. Pero que buen contrataque, igual de trastornado que el suyo. Eres el puto amo."
            "No puedes saborear la grandiosidad de tus palabras con tranquilidad, ni menos disfrutar la expresión del pelirrojo por mucho tiempo. Ya que él comienza a reír."
            unum "No saben a nada."
            unum "Mira"
            scene palaciounum with dissolve
            "Guarda los ojos en su túnica, con cuidado de no hacerles daño."
            "Su próximo movimiento no te lo esperas, su propia mano viaja a toda velocidad, en dirección a su ojo derecho. Lo que hace que pegues un salto hacia atrás y grites que no es necesario."
            "La mano se detiene, solo a centímetros de su ojo."
            "Hoy no quieres ver una automutilación. Ya has tenido suficiente con el regalo para Shams y Noor."
            "Unum te intenta explicar que no es nada; que no le duele; que luego puede regenerar otro. Pero tu haces oídos sordos y le comentas que otro día, cuando tengas el estómago menos revuelto, estarías dispuesto a ver eso."
    
    "Conversan un rato sobre cómo le fue a cada uno en el día." 
    "Unum te escucha con una atención que te asusta un poco, como si cada palabra tuya mereciera ser recordada y tatuada en su memoria." 
    "Le narras todo lo que has hecho hoy; que si bien, para ti no es nada relevante, a él parece encantarle. No sabes si es tu voz lo que lo atrapa o si genuinamente le interesa conocer cada pequeño detalle de tu día."
    scene cocinaunum with dissolve
    "Sin darte cuenta o recordar como sucedió, ya están en la cocina." 
    show unum1risa
    "Sigues hablando, relatando incluso lo más mínimo, aunque evitando nombrar lo que pasó en el chequeo." 
    "Le muestras los dibujos que hiciste con Noor, pasando las hojas una vez has sentido que Unum ya ha visto todos los detalles dentro de cada dibujo. Él los observa fascinado, y con una sonrisa suave, los compara con las obras que adornan sus pasillos." 
    "Incluso se pregunta en voz alta si podrá encontrar marcos del tamaño de las hojas para colgarlos en su habitación."
    "Ahora, entre algunos silencios y risas, se encuentran preparando la cena para ti y los niños." 
    "Lo malo es que tuviste que escuchar a Unum hacer los cánticos para santificar los ingredientes."
    "Todo con una expresión neutral en la cara... ganas no te faltaron para reírte, pero aguantaste como un campeón." 
    "Sin duda alguna, él no tiene una voz muy melodiosa cuando canta." 
    "Al momento de cocinar, el aroma empieza a llenar el espacio, y por un instante todo parece cómodo, doméstico y familiar."
    "Y poco a poco, tu mente evita dejar esa preocupación de lado. No puedes olvidar lo que Septem le dijo a Noor."
    "Así que, te debates un par de veces si mencionarlo. Sin embargo, en el fondo, sospechas que aunque él lo supiera, no se opondría a lo que la cabeza del Jardín ha ordenado."
    menu:
        "Mencionarle lo que Septem dijo.":
            "Aprovechas el próximo segundo de silencio para soltar lo que llevas guardando desde que entraron a la cocina."
            "No preparas tu discurso, ni te extiendes con tus palabras para decir lo que realmente importa."
            "Un solo 'Septem ha dicho que Noor tiene que comer menos' basta y sobra para que Unum sepa de que estás hablando de lo que pasó en el chequeo."
            hide unum1risa
            show unum3callado
            "Su sonrisa cae al instante."
            "El cuchillo que tiene en mano corta una última rebanada de fruta, pasando de largo hasta el plato. Un ruido desagradable nace cuando este hace contacto directo con el material del plato."
            "Un poco más de fuerza, y estás seguro de que alguno de los dos se rompería."
            unum "..."
            nj "Sabes que Noor necesita comer más."
            nj "Ha perdido peso, porque ya come poco."
            nj "¿No crees que--"
            hide unum3callado
            show unum3serio
            unum "¿Te lo dijo a ti o se lo dijo a él?"
            "Unum te interrumpe con la voz seca y sin emoción alguna en la cara. Totalmente neutral, como un robot."
            "Lo miras confundido, no entiendes a qué viene la pregunta y si es que importa a quien se lo haya dicho."
            unum "Si ha dicho su nombre no hay nada que yo o tú podamos hacer."
            "Para probar su punto, Unum sirve porciones iguales en los platos de los niños. Sus movimientos son bruscos y rápidos, como si estuviera enojado con la situación. Tal vez sintiéndose impotente."

        "No decir nada.":
            "Optas por callar."
            "De cualquier modo Unum se enterará tarde o temprano."
            "Hoy no quieres tener más discusiones."
            "Estás cansado."
            "Unum termina de cortar la fruta, coloca los platos y sirve porciones iguales para ambos niños."
    
    "Como último toque, deja un ojo en cada plato... tienes que desviar tu mirada de los platos para no sentir nauseas."
    scene palaciounum with dissolve
    "Juntos ponen la mesa, colocando los platos en su lugar."
    "Cuando tú estás sentado en la mesa, Unum llama a los niños para que te acompañen a comer."
    "Shams y Noor llegan corriendo desde la misma dirección, y con la ropa manchada de tierra. Supones que pasaron el tiempo afuera, jugando a las luchas."
    "Te apena ver a Noor tan delgado y pequeño. Se supone que ambos tienen las mismas condiciones de vida, el mismo horario y el mismo trato por parte de ustedes."
    "Pero Noor se va quedando cada vez más atrás. Y Shams avanza sin mirar atrás."
    shams "¿¡Qué es eso?!"
    show shamsynoor_mesa with dissolve
    "Pregunta al sentarse, mirando su plato. Tú no necesitas ser un genio para saber a que se refiere. Noor en cambio mira con comida sin mucho interés, moviendo su tenedor de un lado a otros, tocando la comida con el."
    unum "Hoy es el último día del mes."
    unum "Hoy tocaba humano en vez del placebo."
    unum "Estuve a punto de comerlos en el camino a casa."
    noor "Tienen el mismo olor que tú..."
    "Comenta Noor mientras te mira, se le ve algo apenado. Y tu corazón pega un vuelco."
    shams "Tienes razón, Noor."
    shams "¿Por qué?"
    hide shamsynoor_mesa with dissolve
    show unumcercaserio with dissolve
    "Tu mirada busca a Unum al instante, no tienes idea de como explicarle aquello a los niños."
    "Aunque cuando tus ojos encuentran a los de Unum, te das cuenta de que él tampoco tiene idea de que decir."
    "Y es que... ¿Cómo les explicas a una entidad que tiene la mentalidad de un niño que están apunto de comer a un ser muy parecido a la persona que hace el rol de padre y madre?"
    scene palaciounum with dissolve
    "Al final, le dices que le explicarás luego. Que coma antes de que la comida se pudra. Y Shams deja el tema de lado, optando por comer su comida. Dejando el ojo para el último bocado."
    "En ocasiones le dedicas pequeñas miradas nerviosas a Noor. Su plato sigue intacto, salvo por la ausencia del ojo."
    "..."
    "Cuando todos terminan, Noor sigue con su plato, casi lleno."
    "Cuando tú le preguntas si hay algo mal, Noor simplemente responde que no tiene hambre."
    "Y se levanta de la mesa para ir a dormir, junto con Shams..."
    "Sientes que tienes ganas de llorar. Pero te tragas el llanto como puedes."
    stop music fadeout 1.5
    "                         .    .    .    .    .    .    .     .    .          "
    scene habitacion with dissolve
    play music "audio/hope.WAV" fadein 2.0 volume 0.4        
    "Han pasado tres días desde el último chequeo."
    "Y ya no puedes seguir fingiendo que no ves lo evidente."
    "Los niños crecen... y lo hacen demasiado rápido."
    "¿Fue ayer cuando {b}realmente{/b} caíste en cuenta? ¿O tal vez anteayer? No puedes recordarlo con precisión, pero sí recuerdas la sensación de horror y preocupación que te cayó encima."
    "Esta vez, el terror es distinto, ¿Qué tal si no paran de crecer? ¿Qué tal si en unos días más llegan a ser viejos, para luego terminar siendo ceniza y huesos?" 
    "Cada hora cuenta..."
    "Si tuvieras que adivinar en qué etapa están ahora, dirías que han entrado en la adolescencia."
    "Cuerpos larguiruchos que no parecen calcular bien el espacio entre lo suyo y lo ajeno."
    "Y esa actitud desafiante."
    "Un juego constante al tire y afloje entre lo que pueden hacer y lo que no. Tanteando hasta dónde pueden llegar sin recibir un llamado de atención por tu parte."
    "Intentan medir qué obtendrán si empujan un poco más, si cederás y los dejarás pasar o no."
    "Es un juego para ellos, pero para ti es extremadamente cansador."
    "Si tan solo tuvieras la potestad que posee Septem con ellos."
    "Decir su nombre y que hagan caso al instante."
    "...Y cuando Shams te mira, te da pena confesar que te da algo de miedo."
    "Porque si bien, ella te sigue mirando con amor y ese toque de inocencia en sus ojos. Si prestas más atención--- o mejor dicho, si comienzas a sobrepensar de más: te das cuenta de que te mira como un gato observa atento, desde fuera, al pájaro que está encerrado en su jaula."
    "En cuanto a Noor... Cada vez come menos. Y no es porque guste hacerlo, ya que en más de una ocación lo atrapas mirando a su comida con hambre."
    "Haz recurrido a extremos. Algunos que no te sientes orgulloso de admitir, pero estabas desesperado..."
    "Obligarlo no funciona, ya que su cuerpo expulsa la comida que le obligas a comer, y ni siquiera es mucha. Es como si su cuerpo no admitiese más comida que solo un par de bocados al día."
    "Y no hay nada que puedas hacer."
    scene camaunum with dissolve
    "Es el movimiento en las sábanas lo que te hace volver al presente."
    "Unum te acompaña en la cama mientras tú ojeabas los libros que ha traído, aunque no los puedes leer, son lo suficientemente interesantes para pasar el tiempo."
    scene unum_mordida with dissolve
    "Ahora, sus manos toman una de las tuyas para acercarlas a su rostro. Cerca de la boca, rozando tus nudillos sobre sus labios y mejillas."
    "De pronto, entran sus dientes a la ecuación. Los desenfunda con una sonrisa traviesa, todo bajo tu atenta mirada, atrapa entre ellos la piel del dorso de tu mano. Sosteniendo tu mirada aún, comienza a apretarla con lentitud"

    menu:
        "Dejar que Unum siga.":
            "No apartas la mano. Ves como sus dientes aprientan más y más, junto con ello, un cosquilleo extraño que viaja hasta tu brazo y luego tu pecho."
            "La mirada de Unum no se aparta ni un segundo, disfrutando de tu reacción."
            "Cuando por fin afloja la mordida, pasa la lengua con lentitud por donde sus dientes estuvieron."
            "Lo que queda ahí son las marcas y una mancha rojiza que tintan tu piel. Es un marca temporal hecha por él, quien la observa con una mezcla de orgullo y deseo."
            unum "¿Te ha dolido?"
            "Pregunta luego con un largo beso en uno de tus nudillos."
            "La respuesta que le ofreces es corta. Un simple 'no'." 
            "Tus manos ya no tienen sensación alguna, ni siquiera puedes sentir la presión en ellas. En el hipotetico caso de que Unum te arranque la mano entera o un dedo de un solo mordisco, no serías capaz de sentir dolor."
            "Pero eso no le da el derecho a obtener las partes de tu cuerpo que están a punto de quedar inutilizables en un futuro..."
            unum "Uhggg, no es justo que no puedas darme ni siquiera un pedacito tuyo."
            unum "Inlcuso las partes que se están muriendo saben bien."
            unum "¿Un solo dedito? por favor~~~~"
            nj "No."
            unum "Uhhhhhh............"
            unum "Eres cruel......................"
            unum "Vas a dejar que muera de hambre."
            nj "Así es."
            "Te muerdes los labios luego de hablar, intentando ocultar una risita. Fallas en el intento al ver como la cara del pelirrojo se arruga, simulando una expresión de dolor."
        
        "Deternerlo.":
            scene camaunum with dissolve
            "Retiras la mano con firmeza."
            "Unum no hace nada para detenerte, solo observa tu expresión en silencio."
            

    scene act2_u16b with dissolve
    "Vuelves tu atención al libro. Unum se recuesta a tu lado, abrazando la almohada. Respira con fuerza, inhalando y exhalando, como si intentara llamar tu atención."
    "Lo está haciendo adrede... él no necesita respirar. Casi parece una pobre imitación tuya de cuando duermes, hasta puede estar burlándose de aquello si lo piensas demasiado."
    unum "UHhhhh---"
    "Gime con dolor fingido, restregando su cara en la almohada que tiene debajo, atrapada entre sus grandes brazos."
    unum "Hoy tengo una reunión con mi consejo."
    "Rompe el silencio, tú tienes que levantar la vista del libro para procesar sus palabras."
    "¿Consejo? ¿Qué?"
    "Él debe haberse percatado de tu confusión pues se dispone a explicar, tomando una bocanada de aire antes de soltar la información."
    show act2_u16
    unum "Debo hablar con ellos cada mes para informarme de cambios o problemas que hay en mi dominio."
    unum "Nada entretenido..."
    unum "No me gusta, todas son tan anticuadas y aburridas."
    unum "Quiero quedarme contigo."
    menu:
        "Llévame a la reunión.":
            "Unum te mira con los ojos muy abiertos, y luego ríe fuerte, casi descontrolado."
            hide act2_u16
            show act2_u15
            unum "¿TÚ QUIERES MORIR?"
            unum "Viéndote y oliendo así no vas a llegar ni siquiera a la puerta del salón."
            unum "Bueno... no creo que ellas puedan contra mí."
            unum "Pero creo que tampoco estarías a salvo si comienzo a pelear cerca tuyo..."
            unum "Jajaja---"
            unum "Es mejor que te quedas aquí."
            unum "Puedo decirle a las chicas que te hagan compañía por el día."
        
        "No vayas, quédate aquí conmigo.":
            unum "¿Por qué me lo haces más difícil? uhggggg."
            unum "Tengo prohibido faltar."
            unum "Prometo volver antes del final del día."

    scene palaciounum with dissolve
    "Frente al llamado del deber, no puedes interrumpir. Por lo que después de que Unum preparara el desayuno para ti y los niños, tuvo que irse."
    "Shams hoy no quiere estar en la residencia, prefiere ir a visitar a Ignis, Solaris y Aeliana. Te lo menciona antes de salir, y te pide que no la obligues a llevar a Noor."
    "Le preguntas el porqué, algo enojado con ella por su actitud."
    show shams_enojo with dissolve
    shams "Noor no quiere."
    shams "Me cerró la puerta en la cara cuando le pregunté si quería ir conmigo."
    nj "¿Han peleado?"
    hide shams_enojo
    show shams_serio
    "Shams mira por un segundo a la izquierda, apretando con fuerza los labios, mientras piensa como responder a tu pregunta."
    shams "No."
    "Es algo obvio de que han peleado, pero aún así Shams intenta negarlo."
    "Antes de salir de casa, Shams te mira de reojo, con una mezcla de culpa y preocupación."
    "Te llama por tu rol de figura parental, su voz es delicada y hasta tierna. Te hace recordar a todas las veces que esa palabra a salido de su boca, en todos los contextos y situaciones posibles. Pero esta vez se siente extraño."
    "Tan extraño que te sacude el estómago."
    hide shams_serio
    show shams_enojo
    shams "...Sería mejor que él lo resuelva."
    hide shams_enojo with dissolve
    "Y se va sin más. No alcanzas a preguntar a quién se refiere con 'él'. Con la influencia que Septem tiene en tus niños, no estás seguro si Shams se refiere a él o a Unum."
    "..."
    "Intentas pasar el tiempo en búsqueda de cualquier actividad que te mantenga ocupado. Pero es difícil encontrar algo que hacer." 
    "¿Limpiar? no es necesario, Unum siempre tiene todo ordenado y estás seguro que hace la limpieza de su residencia cuando tú duermes." 
    "¿Cocinar? Imposible: no tus cánticos no sirve ya que no sabes el lenguaje que ellos evocan cada vez que santifican la comida." 
    "¿Leer? Ja!... cuando Unum tenga tiempo, le pedirá que te enseñe a leer y a cantar."
    "Por lo que tienes dos opciones, conversar con las pinturas de los pasillos o ir a hablar con tu hijo."
    menu:
        "Ir a conversar con las pinturas.":
            scene palaciounum with dissolve
            "Suena lo suficientemente estúpido para intentarlo, y--- si te ayuda a que las horas pasen más rápido, no pierdes nada."
            "Caminas decidido, en dirección a la primera pintura que se te viene a la mente."
            "Tus primeras victimas son las dos mujeres degollando al hombre que yace en una cama."
            "Les explicas tu teoría del porqué crees que están haciendo eso, puras chorradas, pero nunca pierdes el respeto. Esperas alguna clase de respuesta si hablas mientras miras la obra pero ni la mujer ni su acompañante te la dan."
            "No te molestas en preguntarle al hombre, pues... no puede hablar con la garganta abierta. Pobre...."
            "Te detienes por un momento, a procesar lo que estás haciendo."
            "Uy."
            "Te has vuelto el loquito del centro en el instante que has decido hablar con las pinturas... Menos mal nadie puede ver lo delirante de tu actuar."
            "Sí, crees que es momento de parar."
            "En silencio, y con algo de vergüenza en tu alma, te retiras de la escena. A paso lento y mirando al suelo."
            "..."
            "A pesar del pasar de las horas, no puedes quitarte de la cabeza lo que ha dicho Shams."
        
        "Ir a hablar con Noor.":
            pass
    
    "¿Es mejor que {b}él{/b} lo resuelva? No lo crees..."
    "¿Septem? ¿Unum? No sabes a quién se refiere y eso te molesta más. La incertidumbre de que no se refiera a Unum, y que efectivamente, sea Septem, te hierve la sangre."
    "Tú eres quien está ahí con ellos, día a día, viendo con miedo como crecen a una velocidad preocupante. Tú, quién añora  y se lamenta no haberlos abrazado cuando eran bebés." 
    "Y nadie te va a arrebatar la responsabilidad que tienes con tus hijos."
    "Es momento que hables con Noor, buscas tener una conversación profunda acerca de como se está sintiendo últimamente."
    stop music fadeout 1.0
    "..."
    "Caminas con una sensación extraña en tu garganta, cada paso llena y contamina la estática calma del lugar. No deberían sonar tan fuertes o con tanto eco, pero hoy lo hacen."
    scene pasillounum with dissolve
    "Vas directo a la habitación que Noor comparte con su hermana. Unos cuantos pasos más y luego girar a la izquierda, ya posees el plano mental de esta residencia como la palma de tu mano."
    "Esperas que cuando entres a la habitación Noor te reciba con su tierna y tímida sonrisa una vez más."
    "Llegas antes la puerta de su habitación, está abierta. Tocas antes de entrar para anunciar tu presencia, pero nadie responde."
    scene salaunum with dissolve
    "Cuando entras, la habitación está vacía..."
    nj "¿Noor?"
    "Nadie responde al llamado. Eso es extraño."
    "Giras sobre tus talones para salir en búsqueda de Noor. Sabes que no debe estar fuera, ya que siempre que alguno de los gemelos sale, te avisan."
    scene pasillounum with vpunch
    play music "audio/meeting.mp3" fadein 2.0 volume 0.2
    "Al colocar un pie fuera de la pieza, lo único que sientes es un golpe duro en tu pecho. Es una fuerza tan descomunal que hace que pierdas el equilibrio y caigas de espaldas."
    scene badendnoor with vpunch
    "Con todo su peso encima tuyo, Noor te agarra de los hombros, impidiendo que te reincorpores. Sus dedos y uñas se clavan en tu piel, rompiéndola y haciendo que emane sangre de las heridas."
    "Miras sus ojos con horror, en ellos ya no existe esa tierna mirada que tanto conoces."
    "Ahora comprendes por qué Shams no quería que te involucraras... Noor te mira como mira a la comida restante que no puede comer. Con hambre."
    jump ataque_noor 
label continuacion_unum:
    "Noor se detiene en seco, su cuerpo se tensa al instante en que pronuncias su nombre de origen. En sus ojos se refleja tu expresión de terror"
    "Ambos brazos extendidos frente a ti como un inútil escudo de carne y hueso que pueden ser desgarrados en cualquier instante por él."
    scene noor_llorando with dissolve
    "Noor pestañea una vez, pequeñas lágrimas decoran sus ojos. En su próximo parpadeo estas se rompen, cayendo por sus mejillas sin parar. Abre la boca, pero sus palabras no logran salir."
    "Lo único que sale de su garganta son balbuceos que son detenidos por su llanto, ahora descontrolado."
    "Cuando por fin saca fuerzas para hablar, te llama asustado, con pena y remordimiento. Pero no alza sus manos buscando tu abrazo o que lo toques."
    "Se queda quieto e intenta volverse lo más pequeño que puede, mientras sigue llorando."
    "Pide perdón, repetidas veces sin parar a tomar aire."
    "Hasta que su voz se vuelve ronca."
    menu:
        "Acercarse y sostenerlo en tus brazos.":
            "Noor te intenta apartar, pone pies y manos en ello, patalea como un bebé... pero es un intento débil."
            "Si él pudiera, ya te tendría lejos y con más heridas en tu cuerpo."
            "Si bien su cercanía te quema, no te importa."
            "Necesitas consolar a tu bebé."
            "..."
            "No te toma mucho tiempo en tenerlo alrededor de tus brazos, llorando descontroladamente mientras te implora perdón."
            "Le cuesta verbalizar bien lo que quiere decir, ya que sus palabras son comidas por el llanto."
            "Pero tú le entiendes."
            "Le acaricias la cara y le recitas palabras de amor."
            "Le dices que jamás podrías enojarte u odiarlo."
            "Qué él seguira siendo tu pequeño, sin importar lo que suceda."
            "Luego de un rato, él se calma."
            "Pero no deja de llorar."
        "Levantarse e irse.":       
            scene pasillounum with dissolve
            "Ahora no puedes lidear con esto."
            "Así que escapas..."
            "Te alejas lo más rápido que puedes, corriendo a ocultarte en tu habitación..."
            "Cuando Unum llegue verás que hacer."
            
        

        "Sermonearlo.":
            "Te levantas como puedes. No sabes de dónde sacas el valor o la energía para hacerlo, pero lo haces."
            "Y con la voz más dura que tienes, comienzas a sermonearlo."
            "Apenas te detienes a pensar en lo que dices, todo sale como un vómito emocional de tu boca."
            "Apenas puedes escucharte, pues todo lo que inunda tus oidos son los llantos de Noor que pierden la intensidad poco a poco."
            "Hasta que se vuelven solo quejidos pequeños."
            
    "..."
    "Es ahora que entres en razón realmente. Estás jugando con entidades y un mundo peligroso."
    "Estás criando entidades que te pueden arrancar los ojos de un solo tirón."
    "...Es ahora que caes en cuenta que deberías sentir miedo."
    "Pero te cuesta sentirlo en su totalidad..."
    "Detrás de esos dientes y garras, están tus niños."
    "No son unos monstruos..."



    scene negro with pixellate
#    "FIN DEL ACTO 2."
#    "En proceso de elaboración..."
#    "{sc=2} Tendrás que esperar un poco para descubrir como acaba esto... :3{/sc}"
    "..."
    
    play music "audio/calamity.WAV" fadein 1.0 volume 0.4

    scene habitacion with dissolve
    "Te encuentras mirando el techo de tu habitación... Unum está con los niños, dándoles las buenas noches de tu parte..."
    "No se te ha permitido acercarte a ellos por hoy, ya que Noor está muy alterado aún y... no quiere verte."
    "Te duele el pecho de solo recordar sus llantos."
    "Hay partes del día que están difusas, no recuerdas que hiciste exactamente después con Noor, pero Unum llegó e intervino."
    "..."
    scene act3_u1 with dissolve
    "Aquella escena se reproduce una y otra vez en tu mente, impidiéndote dormir."
    noor "¡É-él me lo dijo! ¡no-- yo no quise hacer eso!"
    noor "No es mi culpa."
    noor "Yo no quise---"
    noor "¡Jamás atacaría a mi progenitor! ¡Tú lo sabes, papá!"
    noor "¡No le quiero hacer eso!"
    unum "Tenemos que decirle a Septem."
    noor "¡No-- no le digan a Su Santidad Septem!"
    noor "¡Por favor, papá!"
    noor "Si su santidad interviene será peor... él se llevará a [nombrejugador] lejos de aquí."
    noor "¡Y a mí me comerá!"
    "Noor agarra la túnica de Unum, plantado en el suelo bramando perdón entre sollozos que no le dejan expresarse correctamente. Oculta su carita entre las telas, impidiendo que veas su expresión facial."
    noor "Yo solo debo aguantar, esto no es nada."
    noor "No puedo explotar ahora---"
    scene habitacion with dissolve
    "---"
    "Giras en la cama, buscando bloquear la memoria para evitar caer nuevamente en el espiral de 'los que pasaría' y la impotencia que te azota con fuerza."
    "Pero las sábanas y el colchón poco pueden hacer."
    "Es inútil."
    scene act3_u2 with dissolve

    play music "audio/fell.mp3" fadeout 1.5 fadein 2.0 volume 0.3

    unum "[nombrejugador]..."
    unum "¿Te duele algo?"
    "Unum está en la cama antes de que te des cuenta. Se sienta sin tomar mucho espacio, apenas en el costado, temiendo acercarse a ti."
    "Te incorporas en la cama y meditas su pregunta. Le das al menos dos vueltas para comprender si Unum se refiere a un dolor físico o emocional."
    "Supones que la pregunta encasilla a ambas..."
    menu:
        "Encarar a Unum y su estúpido plan.":
            "Ya estás cansado. El plan no parece más que una sesión de tortura psicológica y física a un niño que no superaría los 13 años humanos..."
            "Y la incompetencia de tu autoproclamado esposo, no hace más que echar sal en la herida."
            nj "¡Todo esto es estúpido! Eres su padre ¿cómo es posible que no puedas hacer nada?"
            unum "..."
            "Unum no es capaz de sostenerte la mirada, busca que responder pero nada sale de su boca."
            nj "¡Lo único que haces es bajar la cabeza y hacer todo lo que ese imbécil te pide!"
            unum "No tengo permitido hablar de esto contigo..."
            unum "Por por favor créeme---"
            nj "¿¡Lo ves!? ¡Haces todo lo que te piden sin cuestionar! ¡Como si tu hijo no se estuviera muriendo de hambre!"
           

        "Decir que Noor no merece esto.":
            "Hay veces en que te da rabia no pertenecer al mismo rango de los Estandartes. Ser un simple trozo de carne, sin poder y desechable, es frustrante. Es una posición que te incapacita a tomar decisiones reales en tu propia vida y la de los que te rodean."
            "Crees que jamás podrás pasar del rango de mascota en este lugar..."
            "Eres solo una mascota con lujos, en un lugar hostil. Mascota que no puede ayudar o defender a su hijo por sus propios medios..."
            "Un tercero debe ayudar... Unum puede ayudar a Noor."
            nj "Tenemos que hacer algo..."
            nj "Noor se está muriendo de hambre, Unum."
            nj "Lo que está comiendo no es suficiente."
            "Unum no es capaz de sostenerte la mirada, busca que responder pero nada sale de su boca."
            "Aprieta los puños, conteniendo el enojo que siente ante la situación en que ambos están atrapados. Sabes que Unum adora a Noor y a Shams, que su amor es incondicional..."
            "Pero ese amor no se traduce en buscar lo mejor para ellos. Si no fuera así, Unum no dejaría a Septem interferir en sus vidas como lo hace actualmente."
            unum "Noor no puede comer más, ya lo viste."
            unum "No podemos ir en contra del mandato de Septem."
            nj "Eres su padre, tienes que hacer algo, antes de---"


    scene camaunum
    show act3_u3 with vpunch
    "De repente, Unum te toma de los hombros con tanta fuerza que cierras la boca al instante, asustado a que te rompa un hueso si sigues con esto."
    unum "Que tengo que hacer para que entiendas que {b}no puedo hacer nada{b}."
    "Entre voz quebrada y cejas que tiemblan batallando para encontrar una expresión que pueda representar correctamente como se siente, sus dedos se clavan en tu piel. Te duele aquello, pero más te duele que Unum te trate de esta manera."
    
    menu:
        "Decirle que te está haciendo daño.":
            nj "Unum..."
            nj "Me duele."
            unum "¡Ah!"
            unum "Lo siento, no era mi intención."
            "Sus manos te sueltan, como si tu piel quemara con el contacto. En su cara puedes ver el arrepentimiento grabado en su expresión."
                
        "Forcejear":
            "Mueves tu cuerpo intentando zafarte de su agarre. No tardas en concluir que no hay escape si es que Unum no te lo permite. Sus manos no parecen moverse con ninguna fuerza que tú puedas ejercer."
            "A él le toma unos segundos entender que es lo que estás haciendo, y con algo de vergüenza te suelta, disculpándose por la fuerza aplicada."
            "Que no era su intención hacerte daño."
    
    
    unum "Lo siento, [nombrejugador]..."
    unum "Tienes que créeme, no quiero esto para Noor..."
    hide act3_u3
    show act3_u3a
    "No sabiendo que hacer con sus manos, toma la tela de sus túnica apretando con fuerza. En sus ojos hay pánico puro, que busca alguna salida para soltar todo el estrés y miedo."
    "Poco tardan en brotar las primeras lágrimas en la esquina de sus ojos, que tímidamente auguran un llanto."
    "Es raro verlo así."
    unum "Pero no puedo hacer nada---"
    "Esa proclamación es lo que falta para que con un solo pestañeo las lágrimas comiencen a caer sin que Unum reaccione ante ellas."
    "Caen sin prohibición, libres por sus mejillas hasta llegar a su mandíbula, donde rompen en su pecho desnudo."
    hide act3_u3a
    show act3_u3b
    "Una de ellas cae en su mano, llamando su atención. Él mira con extrañeza el líquido cristalino. Y por instinto, lleva una de sus manos a sus mejillas."
    "Toca el camino de las lágrimas hasta llegar a su ojos."
    "Traga saliva, evitando el contacto visual en todo momento. Un quejido que simula ser una risa corta e incrédula se le escapa al intentar dar una explicación."
    hide act3_u3b
    show act3_u4 
    unum "¿Qué---"
    "Pasa su mano por la boca, ocultando su voz en ella. El silencio invade la habitación, lo único que los acompaña es el acelerado latir de tu corazón, del cual estás seguro que Unum puede oir."
    "El próximo movimiento de su parte, es escapar de la cama y tomar distancia."
    unum "Yo---"
    unum "Debo irme."
    hide act3_u4 with dissolve
    scene habitacion with dissolve
    "...Quedas solo y confundido con lo que acaba de pasar. Con la imptencia hirviendo en tu garganta, deseando haber dicho más. Unum tiene que entender de alguna manera." 
    "Y si él no hace nada... tu encontrarás la manera de salvar a Noor. Después de todo, ya has le has dado una orden usando su nombre."
    menu:
        "Podemos probarlo...":
            "Mañana probarás hacerlo de nuevo... quizás así puedas ordenarle comer hasta que se harte."
            "No pierdes nada con intentarlo."
            play music "audio/fronbondi2.mp3" fadein 2.0 volume 0.4
            show nada1 with dissolve
            "{glitch=30.0}{color=ffffff}{b}¡Efectivamente!{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}Nada pierdes, y si lo haces--- puedes volver atrás <3{b}{/color}"
        
        "No... es peligroso.":
            "No sabes a lo que te estás enfrentando. Usar el nombre original de Noor podría ser peligroso, tanto para él como para ti."
            "Y si Septem se entera... puede que termines con una muerte rápida si está de buenas... o siendo torturado por tus malas decisiones, a juicio de Septem."
            show nada1 with dissolve
            play music "audio/fronbondi2.mp3" fadein 2.0 volume 0.4
            "{glitch=30.0}{color=ffffff}{b}Ay no digas esas cosas---{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}Es asqueroso... ew{b}{/color}"

    "¡¿!?"
    "¿Quién?---"
    "{glitch=30.0}{color=ffffff}{b}Oh vamos, no me digas que no te acuerdas de mí.{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}Tu humilde~ servidor ~~~\n{size=*0.7}(y apuesto){/size}{b}{/color}"
    "..."
    menu:
        "¿Nulla?":
            "{glitch=30.0}{color=ffffff}{b}¡Bingo!{b}{/color}"
        

        "¿Septem...?":
            "{glitch=30.0}{color=ffffff}{b}Creo que te equivocaste al pinchar la opción.{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}¿O es que pensar no se te da muy bien, cariño?...{b}{/color}"
            "{sc=1}{size=*2}¡H e y !{/size}{/sc}"
            "{glitch=30.0}{color=ffffff}{b}Ja ja, no te creas. Estoy jugando, ¡Al igual que tú!{b}{/color}"
    
    menu:
        "¿Qué haces aquí?":
            pass

    "{glitch=30.0}{color=ffffff}{b}Vengo a escuchar tus agradecimientos por darte esa pequeña ayuda antes.{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}Créeme, si no fuera por eso. Ya estarías muerto.{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}Eso era un deadend, básicamente.{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}Además... ya me estaba aburriendo de solo observar, ya es momento de meter la cuchara.{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}...{b}{/color}"
    "........."
    "{glitch=30.0}{color=ffffff}{b}Bueno si no me vas a agradecer, te diré lo que quiero que hagas y me iré.{b}{/color}"

    menu:
        "No te voy a hacer caso.":
            "{glitch=30.0}{color=ffffff}{b}¿Ah, no?{b}{/color}"
            "{glitch=30.0}{color=ffffff}Esto es para que ayudes a {b}tu hijo.{b}{/color}"
            "Bien... te escucho..."
        
        "¡Noooo, perdón :(!":
            "{glitch=30.0}{color=ffffff}{b}Sigo esperando~~{b}{/color}"
            menu:
                "Gracias, Nulla, por salvarme :)":
                    pass
            "{glitch=30.0}{color=ffffff}{b}De nada, el placer es mío, cariño.{b}{/color}"

    "{glitch=30.0}{color=ffffff}{b}¡Bueno! Puedes pedirle a Noor comer siempre y cuando no esté Unum cerca.{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}Septem puede ver lo que pasa en los dominios a través de los ojos que se encuentran en los halos de sus Estandartes.{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}Aunque eso es solamente cuando se enfoca... pero viendo lo obsesionado que está con los niños, no debe ni dormir con tal de vigilar lo que pasa en el dominio del Sol.{b}{/color}"
    "...Ya veo."
    "{glitch=30.0}{color=ffffff}{b}¡Oh! Me debo ir.{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}Nos vemos luego. Buenas noches, cariñito.{b}{/color}"
    
    "...."
    hide nada1 with dissolve
    stop music fadeout 2.0

    "Y como si fuera una sola alucinación, su voz desaparece. Eres nuevamente el dueño de tus pensamientos, siendo tu voz la única perturbación que hace eco en tu mente."
    "Quieres seguir sobrepensando; buscar soluciones, maldecir a los culpables que permiten que Noor muera de hambre, analizar como ha cambiado Noor, cómo hablar con Noor mañana... pero estás cansado."
    "Tus parpados ya se cierran solos y te cuesta batallar contra ellos para mantenerlos abiertos. La necesidad del sueño se hace presente y no se hace esperar."
    "Tus pensamientos pueden esperar hasta mañana, tu cansancio no."
    "Resignado, abrazas la almohada y dejas que el sueño te atrape."
    scene negro with dissolve
    "........"
    scene camaunum with dissolve
    #Poner una transición.
    play music "audio/fell.mp3" fadeout 1.5 fadein 2.0 volume 0.4

    ell "[nombrejugador]..."
    "Alguien te llama, interrumpiendo tu descanso."
    "Abres los ojos lentamente y maldices lo iluminada que es la habitación de Unum. Todas esas ventanas dejan entrar la luz de fuera, haciendo que tus retinas lloren al quedar descubiertas."
    scene act3_u5a with dissolve
    "Cuando tus ojos se adecuan a la intensa luz, se enfocan en Unum, quien está sentado a los pies de la cama con cara de no querer estar ahí."
    "Es increíble como su actitud ha cambiado, si es que la comparas con su comportamiento habitual. Se le ve apagado, con labios tensos que intentan formar una sonrisa, fallando en el intento."
    "Se le nota preocupado. Presente aquí, pero ensimismado en sus propios pesares..."
    unum "Te preparé el desayuno."
    scene act3_u5
    "Te muestra la bandeja que tiene entre las manos, ofreciéndotela para que la tomes, aunque no la suelta. Te mira, esperando algo."
    "Cuando intentas tomarla, tus brazos no responden. Se mueven pero el movimiento de flexión en tus dedos y muñecas es inexistente. Cada intento es en vano, pero no te rindes."
    "No vas a dejar que eso consuma tu independencia. Primero son las manos... luego serán los pies, y acabarás siendo solo una masa de carne que terminará en la boca de algún Estandarte o, dependiendo de uno por completo..."
    "Y siendo sincero, cada una de las opciones te aterra."
    scene act3_u5a
    "Unum, viendo que tienes complicaciones con tus extremidades, se acerca al punto de sentarse a tu lado. Coloca la bandeja entre ustedes dos y toma el vaso."
    unum "Déjame ayudar."
    scene act3_u5b
    "Dice él, esperando con el tenedor lleno, frente a tu boca."
    "...No importa que tan enojado puedas estar con el mundo y sus leyes estúpidas. O la rabia que sientas hacia Unum por no hacer nada a la hora de proteger a Noor."
    "Dependes de él ahora. Al menos para estas tareas que requieran el uso exclusivo de manos."
    "Aceptas a regañadientes."
    "..."
    "Tu desayuno es amargo, no en cuanto a sabor, sino más bien a la sensación total del momento. Unum no hace esfuerzo en hablar, pues nota tu enojo, y sumiso se dedica a darte de comer."
    "Planeas hablar de Noor una vez que termines con tu comida. Sabes que no sacarás nada con replantearle tus plegarias a Unum, pero quieres saber como ha quedado Noor después de la última vez que lo viste."
    scene act3_u5c
    unum "Sé que estás enojado conmigo..."
    unum "No he sido un buen padre... o un buen esposo."
    unum "Pero por favor, confía en mí."
    unum "Sé lo que hago, sé lo que Septem quiere hacer."
    unum "Y no es algo malo."
    show nada1 with dissolve
    "{glitch=30.0}{color=ffffff}{b}Ja ja.{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}Hay un dicho que dice: {i}Los ingenuos son los que le dan el poder a un mentiroso.{i}{b}{/color}"
    hide nada1 with dissolve
    menu:
        "No te creo...":
            scene act3_u5a
            unum "..."
            
        
        "...Demuéstralo.":
            scene act3_u5d
            unum "No puedo..."
            unum "Tenemos que esperar..."
            #Unum no puede demostrar nada, por órdenes de Septem. 
    
    "Su reacción lastimera te es difícil de ver, ya que no acostumbras a tener este tipo de conversaciones con él. Tampoco se te ha cruzado por la cabeza que en algún momento verías a Unum tan triste o serio."
    show act3_u5c
    unum "Voy---"
    "Se aclara la garganta para evitar que su voz que quiebre."
    unum "Voy a hablar con Septem."
    unum "Intentaré convencerlo para que te pueda contar todo."
    unum "Él... tiene miedo..."
    "Su voz se va apagando a medida que se da cuenta de como está exponiendo al cabecilla del Jardín. Hasta desvanecerse por completo."
    menu:
        "¿Miedo de qué?":
            pass

    scene act3_u5d
    unum "Del poder de Noor."
    show nada1 with dissolve

    "{glitch=30.0}{color=ffffff}{b}¿Lo ves? Septem va a terminar matando a tu bebé si no haces nadaaa~{b}{/color}"
    "{sc=2}...Ahora lo entiendo.{/sc}"
    "{sc=2}No podemos confiar en nadie...{/sc}"
    menu:
        "NO, tenemos que confiar.":
            "{glitch=30.0}{color=ffffff}{b}¿En serio?{b}{/color}"
            hide nada1 with dissolve

            "...Ellos saben lo que hacen. Por algo han vivido tanto."
            "Unum es una estrella, al igual que Noor. Septem debe tener un conocimiento mucho más extenso que el tuyo en cuanto a la fisiología de tus hijos."
            "Debes esperar, morderte la lengua y rezar a que Septem acepte explicarte todo."
            pass

        "No confiar en nadie.":
            $ no_confianza = True
            "No puedes confiar en nada de lo que salga de la boca de alguien que activamente está dañando a Noor con su indiferencia y decisiones."
            "Todo el amor que le pueda tener Unum a Noor se queda corto, siendo claro que él jamás se rehusará a los comandos de Septem, aunque terminen siendo la causa de la muerte de Noor."
            "Así, su amor no vale de nada."
            hide nada1 with dissolve
            pass
    
    pause 1.0
    "..."
    scene act3_u5b
    
    "El tiempo pasa con cada bocado que le das a tu comida, entre el silencio y el cuidado de cada movimiento en sus manos, masticas y tragas la comida."
    "Al terminar, preguntas por Shams y Noor."
    show act3_u5a
    "Unum hace un gesto que te llama la atención, él aprieta los labios sin saber que respuesta darte. Ya con eso, sabes que cualquier palabra que salga de la boca de Unum no te dejará tranquilo."
    "Comienzas a imaginarte lo peor cuando Unum te responde encongiéndose de hombros, con la voz tan baja que apenas puedes oirle."
    hide act3_u5a
    show act3_u5c
    unum "Están con las chicas. Hoy pasarán el día con ellas."
    "Notando que estás apunto de reclamarle, Unum se escuda al instante con un explicación que expulsa nervioso."
    hide act3_u5c
    show act3_u5e
    unum "Noor no quería estár aquí hoy."
    unum "Se siente mal y no quiere verte."
    unum "Al inicio no quería dejarlo ir... ¡él no puede escapar de sus acciones así sin más!"
    hide act3_u5e
    show act3_u5a
    "Ya te lo imaginas... Noor pataleando y resongando contra Unum para que lo deje escapar."
    "...Reconoces que Noor puede llegar a ser muy terco, y no hay como hacerlo cambiar de opinión. El es capaz de mover cielo, mar y tierra para lograr su cometido... Y sabes que Unum no ocuparía su nombre original para imponerle algo más."
    "Por lo que ves plausible el hecho de que Noor haya insistido en irse... pero---"
    show nada1 with dissolve
    "{glitch=30.0}{color=ffffff}{b}Puede que te esté mintiendo, ¿no crees?{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}Puede que Septem lo haya mandado lejos de tu protección.{b}{/color}"
    "{glitch=30.0}{color=ffffff}{b}Y Unum solo esté dando excusas---{b}{/color}"
    hide nada1 with dissolve

    if no_confianza == True:
        "{sc=2}. . . {/sc}"
        "{sc=2}Puede ser que Unum mienta. . .{/sc}"
    else:
        "..."
        "No, no puede ser eso."
        "Septem ha dicho que te necesita cerca de ellos para verlos crecer--- o algo así era."
    
    hide act3_u5a
    show act3_u5d
    unum "Noor tiene que hablar contigo..."
    unum "Pero creo que también necesita tiempo a solas."
    unum "Le di hasta el término del día."
    unum "Antes de que se vaya a dormir tiene que hablar contigo."
    unum "Y pedirte disculpas por lo que hizo."
    "No entiendes muy bien porqué Unum pone toda la culpa en Noor, pero ya no quieres pelear más, al menos no antes de ver la cara de Noor."
    "Estás desesperado por verlo, pero Unum tiene razón: Noor necesita tiempo a solas."
    "Mientras Unum retira la bandeja, exclama al recordar algo que se le ha olvida."
    hide act3_u5d
    show act3_u5e
    unum "¡Ah! Shams fue la que te preparó el desayuno."

    unum "Bueno... la ayudé un poco----- mucho."
    menu:
        "Gracias...":
            hide act3_u5e
            show act3_u5f
            "Unum sonríe... lo único que le faltan son las orejas y la cola para parecer un perro contento ante el más mínimo contacto positivo con su dueño."
            "A pesar de ello, su sonrisa no aguanta por mucho tiempo, y las comisuras de sus labios caen cansadas."
            pass


        "Gracias por proteger mis oidos de tus cánticos...":
            hide act3_u5e
            show act3_u5f
            unum "¡Hey!"
            unum "¡¡¡¡A Shams le salen peor!!!!"
            pass


        "...":
            "Unum aprieta los labios, deteniendo su parloteo al sentir que no estás de humor como para cambiar el tema o seguir el ritmo de su patético intento de calmar las aguas."
            pass
    
    scene act3_u5a
    unum "..."
    "Su mirada es culposa, la de quien sabe que ha hecho algún mal y se arrepiente de aquello. Quiere decirte algo, se le nota en la cara."
    "Unum deja de lado la bandeja, para recostarse cerca tuyo. Sus manos buscan rodearte la cintura, mientras su cabeza desciende para resguardarse en tu regazo. Aunque, todo lo hace con cuidado, esperando a que tú lo aceptes."
    menu:
        "Alejarte.":
            scene habitacion with dissolve
            "Viendo tu acción, Unum se levanta al instante, disculpándose."
        
        "Aceptarlo.":

            scene act3_u6 with dissolve

            "Abres tus brazos, despejando tu regazo e invitándolo a ocupar ese espacio como si fueras una almohada. Unum se acomoda al instante, dejando caer su cabeza contra tus muslos."
            "Murmura algo, pero no logras captar sus palabras que son calladas por la ropa de las sábanas y su propia cara. Tienes que pedirle que lo repita nuevamente y así poder escuchar bien."
            "Acomoda el cuello, dejando solo su mejilla en contacto con las sábanas, permitiendo así que su boca quede liberada para hablar sin problemas."
            scene act3_u6a
            unum "Ayer hice lo mismo que Noor..."
            "Tienes problemas con comprender a lo que se refiere, sus palabras son tan generales que no te permiten saber a que es lo que alude."
            unum "También lo hacen ustedes, cuando algo duele."
            unum "Se siente horrible."
            unum "Es algo que duele dentro. No me gusta."
            "¿Se refiere a las lágrimas?... ayer Unum casi rompe en llanto cuando estaba discutiendo contigo. Debe ser eso a lo que se refiere."
            "Acaricias sus cabellos y le preguntas."
            nj "¿Llorar?"
            unum "Sí. es la primera vez que lo hago, pero---"
            unum "No es eso... el líquido no duele."
            unum "No sé como explicarlo. Jamás me había sentido así."
            unum "No me gusta."
            "Sus dedos se ajustan en tu ropa, tensándola al punto de que crees que la rasgará."
            unum "Porque no para."
            unum "...Se parece a cuando conocí a Quattor y su brillo, me sentía tan enojado porque lo quería y no lo tenía... y solo se pasó cuando le quité los ojos."
            unum "Ella también lloró ahí."
            "Su voz te confirma que Unum ha tenido una revelación." 
            "Por primera vez, tienes la sensación de que Unum está entendiendo el dolor ajeno...El egocéntrico sol por fin a tomado en consideración lo que le rodea y ha pasado de solo verlo a entenderlo verdaderamente."
            "No puedes culparlo... dudas que Unum o las demás entidades de este lugar tuvieran algún tipo de educación emocinal, hayan pasado por los estadios del desarrollo cognitivo por el que pasan niños humanos..."
            unum "Ah--- mierda."
            "Sabes que a esté punto Unum está despotricando y desahogándose, soltando todo lo que pasa por su mente para no tener que lidear con tantos pensamientos que ahora no puede guardar."
            "Así que tú solo escuchas, prestando tu oído."
            unum "¿Así se está sintiendo Noor?"
            scene act3_u6
            unum "...¿Sientes tanto que tienes que soltarlo en un llanto?"
            "Unum suelta un sollozo, que evita que pueda seguir hablando. Levanta la cabeza para buscarte con la mirada, sus mejillas están mojadas, indicativo de que ha estado llorando mientras tenía su cara escondida en tu regazo."
            "A pesar de ello, se le ve decidido."
            unum "Tengo que hablar con Septem..."
            scene habitacion with dissolve
        
    

    "Luego de eso, Unum abandona tu lado para ordenar la habitación. Deja la bandeja en un escritorio cercano y te pide que te levantes para ordenar la cama."
    "Tú te ofreces a ayudar, pero Unum te recuerda rápidamente tu estado actual."
    "Tus manos no sirven ya. No puedes ayudar. Así que solo te dedicas a observar cómo él hace las cosas."
    "Son tareas simples, que cualquiera puede hacer por sí solo... tareas que tú podrías hacer si no fuera por tu condición..."
    scene palaciounum with dissolve
    #Cambiar la escena.
    "..."   
    "Las primeras horas del día se te hacen lentas. Si bien, pasar el día solo con Unum no es tan malo, no puedes evitar pensar en Noor." 
    "Cuentas los minutos que faltan para que sea el final de la jornada para poder hablar con él. Ver cómo está, cómo se siente... decirle que no es su culpa... abrazarlo o darle un beso."
    "En cuanto a Unum... él intenta de todo para que no te sumas en tus pensamientos. No sabes si es porque él no quiere que te pongas mal o porque él también necesita distraerse de algún modo. Supones que es un poco de ambas."
    "Y lo agradeces. Mantenerte ocupado evita que te hundas en ese mar de posibilidades que es el futuro, ese del que podrías pasarte horas intentando desenredar cada hilo en búsqueda de alguna respuesta que no llegará."
    "Así que el resto de tu día es ocupado, aun si no haces mucho por tus manos."
    scene pasillounum with dissolve

    "Te enseña algunas de sus pinturas, acompañándolo con alguna que otra explicación que él mismo se ha inventado. Puede que lo que te esté contando sea interesante, pero hoy no estás interesado en escuchar aquello, por lo que todo su parloteo se traduce en un balbuceo constante en tus oídos."
    "Después, ordenan el cuarto de los niños."
    "Te contentas con verlo mover y guardar las pertenencias de Shams, que están tiradas por toda la habitación."
    "Mientras él hace el trabajo, te cuenta un poco de sus reuniones con 'el consejo' y lo harto que está de 'Júpiter'. Te divierte ver lo exasperado que se pone al hablar de ella."
    show unum2enojo with dissolve  
    unum "Siempre me lleva la contraria."
    unum "¡Y me cuestiona cada decisión!"
    hide unum2enojo
    show unum3callado
    "Toma uno de los últimos libros que están en el suelo, sin revisar su contenido lo guarda con fuerza en la estantería, aunque no lo suelta."
    hide unum3callado
    show unum2enojo
    unum "¡Y lo peor es que siempre tiene razón!"
    unum "¡¡¡Ugh-!!!"
    hide unum2enojo
    show unum3serio
    unum "Ya le dejo manejar las reuniones sola, ni me meto."
    unum "No voy a estar peleando con palabras."
    hide unum3serio
    show unum3callado
    "Que haya acotado el 'con palabras' te deja la idea de que si gustaría de pelear de otra forma... ya te puedes imaginar como le gustaría pelear."
    hide unum3callado
    show unum1risa
    "Notando tu cara, Unum ríe."
    hide unum1risa
    show unum1normal
    unum "Nah... no puedo pelear con ellas. Son muy delicadas... Huh---{size=*0.6}todas, menos Júpiter---{/size}"
    hide unum1normal
    show unum1incomodo
    unum "Si les llego a tocar un solo pelo, todo el Jardín colapsaría ya que yo no podría manejar más de dos conceptos juntos."
    hide unum1incomodo
    show unum3risa
    unum "Es mucho trabajo."
    hide unum3risa
    show unum3callado
    menu:
        "¿Puedes hacerles daño?":
            nj "¿Puedes dañarlas? Pensé que eso estaría prohibido por Septem."
            "Lo sueltas con veneno. Con lo demandante que se ve Septem, se te hace descabellado que Unum tenga permitido dañar a quienes son vitales para el Jardín."
            hide unum3callado
            show unum2duda
            unum "Hmmm, sí."
            "Unum no le presta atención al tono con que hablas, y desconoces si lo hace a consciencia, ignorándolo, o por mera incapacidad de detectar tu comentario ácido."
            unum "Creo que Septem es el único que no puede pelear o hacer daño--- algo de las reglas, o no sé, algo así."
            hide unum2duda
            show unum3callado
            "Otro libro es tomado, esta vez si lo inspecciona. Mientras ojea el libro, Unum piensa en como seguir, no contento con la explicación que ha ofrecido."
            hide unum3callado
            show unum1incomodo 
            unum "Es más que nada para proteger el Jardín."
            unum "Si uno no hace bien su trabajo, llegará otro que te reemplace."
            unum "No es común... pero pasa."
            hide unum1incomodo
            show unum3callado 
            "Hay una pausa larga, donde él se toma el tiempo de guardar el libro en la estantería, deteniendo sus manos para tocar la cubierta por unos segundos antes de soltarlo por completo."
            hide unum3callado
            show unum2feliz
            unum "A Plutón le pasó."
            unum "Y Júpiter solo está esperando el momento perfecto para quitarme el rango."
            hide unum2feliz
            show unum1incomodo 
            "La risa que suelta es estruendosa, resultado de su propio comentario. Algo en él le hace gracia y supones que es por lo imposible que suena para él que Júpiter le 'quite el rango'."
            unum "Eso no va a pasar, pero---"
            hide unum1incomodo
            show unum2enojo 
            unum "UHGGG--- gracias a eso tengo que estar atento y a la defensiva en las reuniones."
            hide unum2enojo
            show unum3serio 
            unum "Al menos Saturno me cuida la espalda."

        
        "¿Mucho trabajo?":
            nj "¿Mucho trabajo---?"
            hide unum3callado
            show unum3serio
            unum "Mantener dos conceptos. Es mucho trabajo. Gastas mucha energía; tienes que estar pendiente de todos los cambios; de las entidades que trabajan ahí; de los recursos que entrar o salen..."
            hide unum3serio
            show unum2enojo 
            unum "Es horrible."
            "Lleva ambas de sus manos a la cara y aplasta sus mejillas, sacando todo el aire que tiene en el cuerpo. Sin duda, un gesto muy exagerado de suspiro."
            unum "Yo tengo que estar pendiente de las órbitas y tirar de ellas; de la temperatura; de hablar constantemente con Tierra para ponernos de acuerdo con las estaciones del año, cuidando de no afectar las predicciones de Tria."
            "Resopla sin ganas y tú, apenas has entendido ni la mitad."
            unum "UN HORRORRRR."
            unum "Ahora imagina DOS CONCEPTOS JUNTOS."
            hide unum2enojo
            show unum3serio
            "..." 
    
    "Oh. \n                                     {i}Oh.{i}"
    hide unum3serio with dissolve
    "La vida aquí es difícil para todos, concluyes. No importa si es una simple estrella o un Estandarte como Unum: todos tienen problemas de los que deben priorizar."
    "A la vez de tener la carga de ser todo menos indispensable."
    "Te recuerda a la vida de un trabajador de tiempo completo, claro, que sin vacaciones o regalías o incluso protección del trabajador... que triste."
    "Que horror."
    scene cocinaunum with dissolve
    "..."
    "Sabes que el día está llegando a su fin al momento en que Unum te llama para que lo ayudes a cocinar la cena. Te causa gracia que la ayuda que necesita es solo tu compañía." 
    "Cocina hablando de pequeñeces, y gracias a ello te enteras de que los niños llegarán más tarde, después de que tú comas. Aquello no te hace gracia alguna, y antes de que puedas discutir con Unum, él te asegura que fue porque Noor lo ha pedido."
    "Noor te está evitando, o eso es lo que Unum quiere hacerte creer."
    "Odias estar en esta posición. Si fuera por ti, ya habrías hablado con Noor desde la mañana... pero, supones que debes respetar sus tiempos."
    "Esto es un proceso por el que él debe pasar. Y si tomarse un tiempo a solas, lejos de ti, le ayudará... lo mejor es esperar a que él vuelva a ti."
    "Sabes que al final del día, Noor te buscará."
    #Cambio de escena
    scene palaciounum with dissolve
    
    "Una vez lista la cena, vas a la mesa en compañía de Unum. La conversación es mínima, pues Unum considera que es mil veces mejor mirarte como un loco, sin perderse detalle alguno, a hacerte perder tiempo en hablar."
    #Describir comida
    show act3_u8 with dissolve
    "Él es quien te da de comer. Cada tanto comenta algo que te hace preguntarte mentalmente, que es lo que está mal con este tipo."
    "La respuesta llega sola: 'Es de esperarse este comportamiento de alguien no humano'... pero eso no te reconforta ni en lo más mínimo."
    "Así que, para distraerte, tus pensamientos vuelven a Noor."
    "Miras tu comida y los pensamientos intrusivos te secuestran..."
    "{sc=2}Tal vez puedas llevarle algo a Noor... y ver si puedes hacer que coma algo de más...{/sc}"
    "Tal vez---"
    if no_confianza == True:
        "Sería lo mejor que puede hacer. Unum no te va a ayudar... debes tomar cartas en el asunto."
        "No seas cobarde. . ."
    else:
        "..."
    menu:
        "Guardar un poco de comida para Noor.":
            "Piensas una manera de hacer que Unum no se de cuenta... pero todos sus ojos están puestos en ti."
            "La mesa tiene todo lo que necesitas lamentablemente, por lo que no puedes pedir que vaya a buscar algo que falte... salvo---"
            scene act3_u8a with vpunch
            "Mueves tu brazo e intentas tomar el vaso con agua que tienes cerca, y que está peligrosamente cerca del límite de la mesa. Aquello provoca que el vaso se de vuelta, cayendo fuera de la mesa."
            scene palaciounum with dissolve
            play sound "vidrio.mp3"

            show act3_vasoroto with dissolve
            "El ruido de los vidrios rompiéndose es molesto, pero la reacción del pelirrojo es inmediata."
            unum "Ouuh, recuerda que no puedes tomar las cosas."
            "No hay enojo en su voz, ni tampoco restos de querer darte un sermón. No... su única reacción es agacharse y recoger los pedazos de vidrio."
            hide act3_vasoroto with dissolve
            "Al tener todos en su mano, los funde y genera un nuevo vaso. Cierras la boca para fungir que no te ha sorprendido, pero es imposible que Unum no lo note, pues suelta una risa triunfal."
            "¡Genial, eso no ha servido de nada! Qué más---"
            
            unum "Iré a buscar más agua."
            "Oh."
            "Okay, eso si ha servido después de todo."
            "Bien. Ahora lo difícil... guardar la comida..."
            "Sinceramente no habías pensado en eso. Tus manos son inútiles y no tienes como agarrar las cosas con tus manos..."
            "Además... ¿Será que Unum puede percibir el olor de la comida? Uhhhh--- definitivamente no lo has pensado bien..."
            show nada1 with dissolve

            play music "audio/fronbondi2.mp3" fadeout 1.5 fadein 2.0 volume 0.3

            "{glitch=30.0}{color=ffffff}{b}Yo puedo ayudar~{b}{/color}"
            "{sc=2} Pues apuráte, no tenemos mucho tiempo{/sc}"
            "{glitch=30.0}{color=ffffff}{b}Ja, la marioneta ya hasta habla por si sola, wow, cariño.{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}Te dejas controlar muy fácil~~{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}¡Bien!, disfruta este regalo.{b}{/color}"
            "Una sensación de escalofrío recorre todo tu ser, desde las puntas de tus pies hasta tu lengua. Algo crece dentro de ti, aunque no puedes identificar donde."
            "Lo sientes en la espalda, manos y pecho. Se siente como una tercera o cuarta extremidad---un nuevo brazo."
            "Miras tu cuerpo, buscando el responsable de esa sensación. No son tus manos, ni brazos. Giras la cabeza, buscando por sobre tu hombro--- y ahí lo ves."
            "Una mano negra, parecida a la brea en consistencia, oscila a tu lado."
            "Viaja hasta el plato y toma una porción generosa, para luego tragarla. Haciéndola desaparecer."
            "{glitch=30.0}{color=ffffff}{b}Llama a mi nombre cuando lo necesites.{b}{/color}"
            stop music fadeout 2.0

            $ comida_noor = True
            hide nada1 with dissolve
            "----"
        
        "No tomar nada.":
            "Es mejor que no intervengas... no quieres imaginar como reaccionarán ellos si se enteran de que planeas darle más comida a Noor."
    
    
    
    play music "audio/fell.mp3" fadeout 1.5 fadein 2.0 volume 0.4

    "Unum regresa con el vaso lleno. Su sonrisa es amplia, más esta se desvanece al llegar a la mesa, es un cambio instantáneo."
    if comida_noor == True:
        show unum2enojo with dissolve
        "En su rostro se forma una mueca que denota desagrado, mostrando los dientes."
        "Te mira de pies a cabeza, buscando algo. Aguantas la respiración, rezando para que no se de cuenta."
        "Al no encontrar nada, sus ojos se posan en el plato."
        hide unum2enojo
        show unum3serio
        unum "Algo malo en ese plato. No comas más"
        "Sus ojos se entrecierran con sospecha. Y para sí mismo, se pregunta por lo bajo."
        unum "¿Será la contaminación cruzada?..."
        hide unum3serio with dissolve

    else:
        scene palaciounum with dissolve
        
        show unum2duda with dissolve
        unum "Oh ¿Qué pasa?"
        unum "¡Estás pálido!"
        "El vaso de agua queda olvidado en la mesa. Ahora tienes a Unum encima, revisando tu cara, respetando poco y nada el espacio personal."
        unum "No puede ser, ¡si he hecho todo bien!"
        "Le dices que no pasa nada. Que solo ya no tienes hambre."
        hide unum2duda with dissolve


    "Terminas tu comida tomando el agua, él te la ofrece con cuidado, aterrado de ser muy brusco y derramar en líquido sobre ti."
    "Ya terminada la tarea de comer, Unum te mira con algo se pena en sus ojos."
    show unum3serio with dissolve
    unum "Mañana le preguntaré a Septem por tus manos..."
    unum "No quiero que---"
    "No sabe como terminar la idea y decide cortar de lleno con su parloteo, aclarando su garganta con incomodidad..."
    hide unum3serio 
    show unum3risa
    unum "Voy a ir a buscar a los niños."
    unum "¿Vas a hablar con Noor?"
    hide unum3risa
    show unum3callado
    "Asientes, sin muchas ganas de hablar."
    "Hay un nudo entre tu gargánta y estómago que no te permite hablar, el solo pensamiento de tener a Noor contigo te pone ansioso. Temes de ver su reacción..."
    "Tu corazón no podría aguantar un rechazo por su parte. Y aunque estás seguro de que eso no pasará, la posibilidad siempre está ahí, asechando en tu mente."
    hide unum3callado
    show unum3serio 
    unum "Me llevaré a Shams para que puedan hablar tranquilos."
    hide unum3serio with dissolve
    "La gran mano de Unum te toca la cabeza, es un gesto tierno y suave, que intenta calmar tu corazón."
    "Es extraño, pues en cierto sentido, lo hace."
    "Es cálido, delicado como un pequeño rayo de sol que pasa por tu ventana al amanecer. Su toque te envuelve en una sensación que no puedes describir por completo."
    "Pero que es similar a tocar un objeto cálido cuando te estás congelando."
    "Se siente bien."
    "..."
    "Le agradeces antes de que se vaya."
    ". . ."
    "    .     .     .     .     .     ."

    #Cambio de escena.
    
    play music "audio/calamity.WAV" fadeout 2.0 fadein 1.0 volume 0.4

    "Los minutos se extienden a un nivel en que sientes que ha pasado al menos una hora entera. Que, aunque sabes que es solo una percepción alterada por culpa de los nervios, te es imposible determinar en su totalidad el tiempo real."
    "Por lo que al escuchar como la puerta de la entrada se abre, te toma por sorpresa."
    "Con el corazón a mil por minuto, buscas a Noor con la mirada, olvidándote de Unum y Shams."
    "Ahora tu principal inquietud es Noor y saber como está."
    scene pasillounum with dissolve
    "Así que corres a la puerta, esperanzado de ver esa carita sin lágrimas esta vez, dispuesto a hablar contigo."
    show unum3serio at left with dissolve
    show shams_serio at right with dissolve
    "Pero Unum te bloquea el paso. Detrás de él está Shams, observándote con los ojos bien abiertos."
    "Te tomas un momento antes de devolverle la mirada con el ceño fruncido."
    unum "Noor está afuera."
    unum "Iré a acostar a Shams..."
    unum "Shams---"
    hide shams_serio
    show shams_feliz at right
    "El llamado de su padre le basta para ponerse recta y mostrar los dientes, algo incómoda te saluda y te da las buenas noches."
    "Luego de eso, ambos se retiran."
    hide unum3serio 
    hide shams_feliz 
    with dissolve
    "Ahora estás a solas con Noor..."
    "La barrera que tienes al frente es la puerta semiabierta, que espera a que cruces por el umbral, en búsqueda de tu hijo. Das los últimos pasos y la abres por completo para poder pasar sin problemas."
    scene act3_u7 with dissolve
    "Afuera sigue siendo de día, aunque sea el final del día. No existe la noche en este lugar, el principal indicativo de que ha llegado el final del día es que la luz fuera del templo es más tenue."
    "Como la de un atardecer corriente."
    "Noor está sentado en los escalones que conducen a la entrada." 
    scene act3_u7a with dissolve
    "Llamas su nombre, su verdadero nombre: Noor. La respuesta es inmediata, vuelve la cabeza hacia ti, te sostiene la mirada por un momento, y te saluda en voz baja."
    "Sabes que quiere que te acerques, pues se acomoda para dejarte un espacio en el escalón. Invitándote silenciosamente a sentarte a su lado."
    "Sentarse es un acto solemne, que ampara una conversación necesaria."
    "Es ahora o nunca."
    menu:
        "Hablar y decirle que debe comer." if comida_noor:
            "Sabes que lo que estás a punto de hacer es romper un montón de reglas que no deberían ser rotas bajo ninguna circunstancia--- baajo el juicio de quienes comandan el Jardín."
            "Pero tú ya no estás para juegos de complacencia hacia quienes no te respetan lo suficiente como para tomarse el tiempo y explicar las cosas."
            "Eso ya se acabó..."
            "Tu discurso es simple; le afirmas a Noor que no estás enojado y que entiendes como se siente. Que quieres ayudarlo y deseas que se tenga las mismas condiciones que Shams para crecer."
            "Dices que los amas a ambos por igual, y por ello estás dispuesta a hacer lo que sea para asegurar que ese amor se transmita en cada acción que tomas."
            "Noor te mira, más no te ofrece palabra alguna."
            nj "Tienes que comer."
            "Dictaminas cuando sientes que la conversación está corriendo en círculos, gracias a la falta de participación de Noor."
            scene act3_u7a with vpunch
            noor "¿Qué--? No puedo..."
            noor "Su Santidad Septem---"
            nj "No quiero escuchar nada de eso."
            nj "Vas a comer. No puede ser que te estés muriendo de hambre, Noor."
            nj "Estás creciendo."
            noor "Ma- [nombrejugador], no puedo."
            "No queda de otra..."
            
            play music "audio/fronbondi2.mp3" fadeout 1.5 fadein 2.0 volume 0.3
            
            menu:

                "{glitch=30.0}{color=ffffff}{b}Decir su nombre original: Sirius{b}{/color}":
                    pass
                
            scene negro with dissolve
            show nada1 with dissolve
            
            centered " {glitch=30.0}{color=ffffff}{b}Sirius{b}{/color}, te comando a que debes comer cada vez que sientas hambre."
            $ noor_hambre += 5
            centered " {glitch=30.0}{color=ffffff}{b}Asimismo, no puedes hablar de Septem acerca de esto.{b}{/color}"
            hide nada1 with dissolve
            scene act3_u7a
            "Con ojos que peligran salir de sus cuencas, él te mira aterrado, sin poder creer lo que acabas de hacer."
            "Te mira como si lo que acabas de hacer fuera una sentencia de muerte. Una traición que jamás podría haber venido de ti."
            "Es dolor, lo que se asoma en su cara."
            noor "¡No--- no puedes...!"
            noor "Si lo hago yo voy a---"
            "Un escalofrío recorre tu cuerpo, y crees escuchar el un murmullo dentro de tu mente, pero no captas su significado."
            "Noor también parece sentirlo. Aunque la reacción es más violenta, sus labios se sellan con fuerza, impidiendo que pueda seguir hablando. Enojado y frustrado, el trata de comunicarse, pero es en vano."
            "Su boca no responde."
            show nada1 with dissolve
            "{glitch=30.0}{color=ffffff}{b}Oh! veo que necesitas ayuda.{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}Ten, prueba si tu comando sirve~{b}{/color}"
            "Tu compañero de dudosa omnisciencia llega al rescate. Junto con el mismo escalofrío, se manifiesta el brazo de brea con el pastelito que has guardado para Noor."
            "Lo tomas, temiendo contaminar la comida con esa sustancia asquerosa. Y como si nada hubiera pasado, la brea desaparece."
            hide nada1 with dissolve
            "Examinas el pedazo con detenimiento. Al no encontrar nada extraño, se lo ofreces a Noor."
            scene act3_u9 with vpunch
            "El lo toma sin chistar. Y lo devora sin cuidado, olvidando las etiquetas de los modales que Unum y tú le han enseñando desde pequeño."
            "Lo come al punto de atragantarse en cada bocado, con tantas ganas que aquello te neutraliza cualquier gota de duda en tu cuerpo. Esto tiene que significar que estás haciendo lo correcto.."
            "Su reacción de terror se debió al terror que le tiene a Septem..."
            "Hay algo malo en el plan que tienen para tus hijos... algo siniestro."
            "Noor tiene hambre. La comida que le están dando no es suficiente... quieren dejarlo débil--- no, no quieres ni pensar la razón de todo esto."
            "Pero ahora estás tú."
            "No permitirás ver a Noor empeorar."
            "Cuando quedan solo las migajas del pastel, Noor pausa un momento para procesar lo que ha pasado."
            scene negro with dissolve
            "Y sin dirigirte la palabra, se aleja de ti para salir corriendo hacia la dentro de la casa."
            "..."
            "Sabes que está enojado... y posiblemente asustado."
            "Pero es algo que debes hacer."
            pass
            


            
        

        "Hablar con Noor.":
            "La conversación no se te hace fácil, hablas cuidando cada palabra que sale de tu boca, temiendo que alguna pueda alejar a Noor de ti."
            "Necesitas lograr que Noor se abra a una conversación recíproca, la cual ambos participen..."
            "Hasta ahora no has tenido suerte... él solo te escucha, atento pero no interesado en devolver una respuesta verbal."
            "Le dices que no lo culpas; que sabes que jamás fue su intención asustarte o hacerte daño; que lo entiendes."
            "Llega un punto en que te rompes, y comienzas a llorar de la desesperación al confesarle que no quieres perderlo."
            "Noor por fin reacciona, te mira a los ojos preocupado por tu actuar. Pequeñas manos temblorosas se posan en tus brazos, en un agarre que te conecta a tierra, un pequeño soporte que te indica que Noor sigue aquí contigo."
            "Que no se ha ido a ningún lado."
            show act3_u7a
            noor "¿Por qué dices eso?"
            "Sientes su confusión en su voz."
            nj "Cada día estás más débil... Shams ya te saca una cabeza entera de altura y pesa el doble que tú---"
            "Le confiesas sin restricciones o filtros en tus palabras. Necesitas sacar todas tus preocupaciones, hacerlas notar para que, de alguna forma u otra, te puedan ofrecer respuestas a todas tus dudas que han surgido por la falta de información."
            "Ya no te basta con asumir. Necesitas respuestas."
            "Necesitas saber si Noor es consciente de su estado actual o no."
            noor "No..."
            noor "Es para que Shams me absorba sin problemas."
            "El aire deja de entrar a tus pulmones, sientes como el corazón se detiene por un instante para luego comenzar a palpitar tan fuerte que cada bombeo de sangre, duele al pasar por tus arterias."
            "¿A qué mierda se refiere con 'absorber sin problemas'? ¿y por qué lo dice como si no fuera nada del otro mundo?"
            nj "¿Qu--"
            "Noor baja la cabeza, comprendiendo que esto no ha hecho más que alterarte más."
            noor "...pensé que sabías---"
            noor "No es nada de que preocuparse---"
            show nada1 with dissolve
            
            play music "audio/fronbondi2.mp3" fadeout 1.5 fadein 2.0 volume 0.3
            
            "{glitch=30.0}{color=ffffff}{b}Claro que es algo de lo que debes preocuparte.{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}Puedo ser todo lo que Septem dice de mi a mis espaldas, pero---{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}Te puedo decir con total seguridad de que ese niño está hablando desde el miedo.{b}{/color}"
            "{glitch=30.0}{color=ffffff}{b}Quizás que cosas le habrán dicho este pobre bebé~{b}{/color}"
            menu:
                "Comandarle que coma sin restricciones.":
                    "Sin duda te quieren quitar a tu hijo. Quieren condenarlo a ser comido por su hermana, y le han lavado tanto el cerebro que ni siquiera es capaz de cuestionarlo."
                    "Ya has tenido suficiente."
                    "No vas a escuchar nada más de esto."
                    centered "{glitch=30.0}{color=ffffff}{b}Sirius{b}{/color}, te comando a que debes comer cada vez que sientas hambre."
                    $ noor_hambre += 2
                    centered "{glitch=30.0}{color=ffffff}{b}Asimismo, no puedes hablar de Septem acerca de esto.{b}{/color}"
                    scene act3_u7a with vpunch
                    noor "¿¡Q-que?!---"
                    noor "¡No--- no puedes...!"
                    "Un escalofrío recorre tu cuerpo, y crees escuchar el un murmullo dentro de tu mente, pero no captas su significado."
                    "Noor también parece sentirlo. Aunque la reacción es más violenta, sus labios se sellan con fuerza, impidiendo que pueda seguir hablando. Enojado y frustrado, el trata de comunicarse, pero es en vano."
                    "Su boca no responde."
                    show nada1 with dissolve
                    "{glitch=30.0}{color=ffffff}{b}Tsk.{b}{/color}"
                    "{glitch=30.0}{color=ffffff}{b}Pobre niño... Septem lo tiene tan manipulado que rechaza tu ayuda...{b}{/color}"
                    scene negro with dissolve
                    "Sin dirigirte la palabra, Noor se aleja de ti para salir corriendo hacia la dentro de la casa."
                    "Sabes que está enojado... y posiblemente asustado."
                    "Pero es algo que debes hacer."
                    pass
                
                "Intentar calmarte y escucharlo.":
                    show nada1 with dissolve
                    "{glitch=30.0}{color=ffffff}{b}Tsk.{b}{/color}"
                    "{glitch=30.0}{color=ffffff}{b}Luego no vengas llorando a mí cuando obtengas un final malo...{b}{/color}"
                    hide nada1 with dissolve
                    "Te esfuerzas, realmente intentas respirar y actuar con cautela."
                    "No puedes perder la cabeza tan fácil, menos tomar decisiones a la rápida."
                    "Respiras contando los segundos, lo que sirve para no hiperventilarte."
                    noor "No te preocupes..."
                    noor "Es algo que tenemos que hacer."
                    noor "Para eso nos crearon."
                    "Te duele."
                    "Escucharlo tan seguro y convencido de que las cosas son así, te rompe el corazón."
                    "Antes de que puedas tomar su cara, Noor se levanta."
                    "Te mira desde arriba con una sonrisa, y te desea las buenas noches antes de dejarte solo."
                    pass
            

    #cambio de escena
    scene piezasinunumnoche with dissolve
    play music "audio/calamity.WAV" fadeout 2.0 fadein 1.0 volume 0.3

    "Te vas a la cama pensando en Noor..."
    if noor_hambre >= 1:
        "Esperas que mañana él no esté enojado contigo..."
        "Todo esto lo haces por él."
        "¡Eres el único que está intentando hacer algo aquí!"
    else:
        "Tienes que saber que es lo que están haciendo con tu hijo. No te vas a quedar de brazos cruzados esperando a que ocurra algo de lo que luego te puedes arrepentir."
        "Unum tendrá que hablar con Septem para que te den las respuestas que buscas."
        "Pero independientemente de la respuesta... no vas a dejar que Noor muera por nada del mundo."
    scene negro with dissolve
    "Dios."
    "..."
    pause 2.0

    ".     .      .      ."

    #cambio de escena
    scene pasillounum with dissolve
    pause 2.0

    "Los días pasan hasta llegar al siguiente chequeo."
    "Esta vez no entras con los niños, pues presientes que se formará un altercado entre Septem y tú."
    if noor_hambre >= 1:
        "Y no te crees capaz de mantener en secreto el comando que le has dado a Noor, por el mero hecho de que deseas sacárselo en cara a ese imbécil."
        "Piensas en los días anteriores mientras esperas a que Noor salga del chequeo."
        "Noor ha comido sin restricciones, se le ve contento cuando lo hace. Mas al terminar de hacerlo puedes observar como la culpa lo consume."
        "Es en esos momentos en donde te acercas a hablar con él, e intentas convencerlo de que no hay nada de malo con comer lo mismo que come Shams."
        "Después de todo, ambos tienen la misma edad y necesitan las mismas condiciones para poder crecer sanos y fuertes."
        "Crees que la palabra 'fuertes' hace que Noor cambie de parecer... se le ve decidido, cada vez que le mencionas aquello."
        "Al punto de que te da la sensación de que quiere obtener más fuerza que Shams."
        "Cada vez que termina su comida, Noor no se ve satisfecho... y en más de alguna ocasión lo has visto sacar comida a escondidas."
        "Es de esperarse... está comiendo todo lo que no comió cuando tenía la restricción de Septem."
        "Es una buena señal."
        show noor_serio at left
        show septem1disgusto at right
        with dissolve
        "Cuando por fin Noor sale de la sala, lo hace con Septem a su lado."
        "En su cara lleva una expresión de desconcierto, peligrosamente cerca del enojo. Al mirarte, este chasquea la lengua y se retira, sin ofrecerte explicaciones o recomendaciones."
        hide septem1disgusto with dissolve
        $ noor_hambre += 10

    
    else: 
        "Prefieres esperar a la intervención de Unum... esperar a ver que es lo que decide Septem antes de actuar."
        "Piensas en los días anteriores mientras esperas a que ambos niños salgan del chequeo..."
        "Noor sigue comiendo lo mismo, y si bien se le ve hambriento, él se asegura de mostrarte una sonrisa cada vez que termina de comer."
        "A la vez de que se te acerca para decirte que todo está bien. Que no tiene hambre."
        "Y tú no lo puedes soportar..."
        show noor_serio at left
        show septem1disgusto at right
        with dissolve
        "Noor no tarda en salir de la sala, detrás de él aparece Septem."
        "El rubio te analiza con la mirada, no hay signos de molestia o desagrado, pero aún así hace que te sientas nervioso."
        hide septem1disgusto
        show septem2incomodo at right
        septem "Noor me ha dicho que quieres saber la razón de su dieta."
        hide septem2incomodo
        show septem1triste at right
        "Subes la mirada al instante, espectante a recibir respuestas."
        hide septem1triste
        show septem2incomodo at right
        septem "Unum también me lo comentó hace ya un tiempo."
        hide septem2incomodo
        show septem1triste at right
        "Se toca el cabello y lo acomoda hacia atrás, soltando un suspiro."
        septem "..."
        septem "Confían mucho en ti..."
        septem "Me temo que no puedo compartirte esta información aún..."
        hide septem1triste
        hide noor_serio
        with dissolve
        "Septem se acerca a ti, toma tus manos en las suyas, y como si de una plegaria se tratase, se encorva un poco para quedar al nivel de tus ojos."
        septem "Pero te aseguro,[nombrejugador], que esto es necesario para mantener a tus hijos y al Jardín con vida."
        "Luego de aquello toma distancia de ti."

    hide septem1disgusto with dissolve
    "Septem desaparece del lugar en un solo parpadeo. Quedando solos en el pasillo."
    "..."
    "Se crea un silencio, del cual no sabes como romper." 
    show shams_feliz with moveinleft
    "Afortunadamente, Shams aparece para llamar tu atención. Corriendo con una energía desbordante, que te trae reminicencias de cuando ella solo era un infante."
    "Se aferra a tus prendas, tirando de ellas para lograr que la mires a los ojos."
    "Iris de una tonalidad gris te saludan con ternura, intentando ocultar su naturaleza traviesa e indomable que la caracteriza."
    "Se parece tanto a Unum te dan ganas de tomarla y hacer una comparación exhaustiva, con el fin de encontrar alguna diferencia. A sabiendas de que poco o nada encontrarás."
    "Llega a ser chistoso y algo frustrante las similitudes entre padre e hija."
    "Es una copia exacta."
    shams "¡Ignis nos ha invitado a la residencia!"
    shams "Quieren vernos a los tres."
    "...Eso es nuevo."
    hide shams_feliz with dissolve
    "Aceptas acompañarlos por mera curiosidad. Después de todo, hoy es domingo y Unum no llegará hasta el final del día."
    "Tener algo más aparte de quedarte en casa descansando suena bien."
    "Quedarse en la cama pudriéndote no es algo que te apetezca hacer hoy."
    scene jardinunum with pixellate
    #cambio de escena
    "Los niños van delante tuya, marcando el paso. Caminan lento, procurando no sacarte mucha distancia."
    "Les has dicho que no se preocupen por ti... que aún puedes caminar sin molestias."
    "Pero ninguno de los dos parecen muy convencidos de aquello, pues cada cierto tiempo miran atrás, atentos a cada cambio que esté experimentando tu cuerpo."
    "De juego, aguantas la respiración, queriendo ver su reacción."
    "No pasan más de diez segundos para que ambos giren todo su cuerpo, alarmados y listo para correr hacia ti."
    "Al ver aquello, dejas que una carcajada retumbe en todo el jardín."
    "Ambos reaccionan igual, refunfuñando como gatos y gritando tu nombre."
    "'No es chistoso' dicen al unísono."
    "..."
    scene jardin_chicas with dissolve
    "La residencia de las esposas de Unum es un lugar misterioso, uno del cual siempre has estado interesado en conocer. Por el simple hecho de que se te ha negado la entrada anteriormente."
    "Resultando en que la curiosidad tome posesión de tu cuerpo y pensamientos."
    scene puerta_residencia with dissolve
    pause 1.0
    scene puerta_residencia2 with dissolve
    "Por ello, pasar por el umbral de la puerta es como un gran logro que has conquistado."

    scene salchichas 
    show ignis_normal at left
    with dissolve

    play music "audio/hope.WAV" fadein 1.0 volume 0.4
    
    ignis "Bienvenidos, ¿Cómo les fue en el chequeo?"
    "Shams entra rápidamente para abrazar a Ignis, restregando su cara en ella."
    show shams_feliz with dissolve
    shams "¡Bien! Septem dice que mi masa está en perfecto estado."
    show noor_serio at right with dissolve 
    if noor_hambre >= 1:
        noor "..."
        "Noor se toma más tiempo de lo normal en responder, como si estuviera buscando que decir sin causar algún tipo de conflicto."
        "Queriendo evitarlo a toda costa."
        hide noor_serio
        show noor_hablando at right
        noor "Mi masa está bien."
    else:
        "Noor te mira antes de contestar."
        hide noor_serio
        show noor_hablando at right
        noor "Mi masa está estable."

    ignis "Ya veo..."
    ignis "Incluso ya les han permitido estár más tiempo separados, uh."
    hide shams_feliz
    show shams_serio
    shams "Sí, se siente extraño."
    
    hide shams_serio
    hide ignis_normal
    hide noor_hablando
    with dissolve
    "Ahora que lo piensas, Ignis tiene razón: Ellos ya no están entrelazados todo el tiempo... a diferencia de cuando eran más pequeños."
    "Intentas recordad lo que Aeliana te habló de las colas y su función pero te es difícil traer el recuerdo a ti."
    "Estar sujetos a la cola del otro les servía de estabilizador o algo así... era importante, estás seguro de ello."

    show ignis_normal with dissolve
    menu:
        "¿Eso es bueno?":
            "Ignis te observa detrás de su máscara, y suspira con cansancio."
            pass
        "¿Eso es malo?":
            "Ignis pausa lo que está haciendo y te observa. No despega la mirada de tu figura, haciendo que los segundos pasen más lento de lo habitual."
            pass

    ignis "Es bueno..."
    ignis "Deben acostumbrarse a ello para no tener problemas al momento de la fusión."
    "¿Fusión?..."
    hide ignis_normal with dissolve

    "Deseas saber más pero Shams arrastra a Ignis a la cocina, insistiendo en que le enseñe más cánticos."
    "...."
    "Te han dejado sin supervición, en la sala ya no hay nadie. Noor probablemente se ha escabullido a fuera."
    "Y Shams ha preferido ir con Ignis a una lección de cocina..."
    "Hmmm..."
    menu:
        "Explorar la residencia.":
            jump explorar_unum_act3


    label acto3_unum_continuacion:
        "..."
        scene jardin_chicas with dissolve
        "Viendo que no hay nada más que hacer, escojes el patio para esperar a que Shams y Noor se aburran."
        "Podrías volver a la residencia de Unum, pero allá tampoco hay mucho que hacer."
        "..."
        "Mientras descansas en el patio, detectas a lo lejos a Aeliana y Solaris, caminando por el camino que conecta el templo de Unum con su residencia."
        "Solaris sonríe, mostrando sus puntiagudos dientes."
        show solaris_normal at left
        show aeliana_serio at right
        with dissolve

        solaris "Que raro verte aquí."
        solaris "Pensé que no aceptarias nuestra invitación."
        menu:
            "Explicar que querías verlas.":
                pass

            "Saludarlas.":
                pass
        hide aeliana_serio
        show aeliana_feliz at right

        aeliana "Hmmm~"
        aeliana "Es un gusto verte a ti también."
        "Ambas se detienen ante ti, dejando un espacio razonable entre tú y ellas."
        "Ya pasado tiempo con ellas anteriormente, ya sea con o sin Unum presente. Ellas siempre han sido muy correctas y amables contigo... pero te sigues poniendo algo nervioso cuando se trata de ellas."
        "Llámalo paranoia, o lo que quieras... ese sentimiento de que estás acercándote demasiado cerca al sol siempre está contigo, que ya llegará el día en que te quemarás por las llamaradas de la estrella."
        "Puede que ese día llegue, y te encontrarás con las estrellas hambrientas, dispuestas a saciar esa hambre con tu carne."
        "Y todo lo que quede de ti será tus recuerdos."
        solaris "¿Estás bien?"
        "Su mano se coloca en tu hombro, obligando a escapar de esos pensamientos fatalistas."
        solaris "Ja! ¡Tu motor parece un pulsar, va muy rápido!"
        hide aeliana_feliz
        show aeliana_serio at right
        aeliana "Corazón."
        "Corrige Aeliana, quitando de encima la mano de Solaris sobre tu hombro."
        hide aeliana_serio
        show aeliana_feliz at right
        aeliana "Tu corazón late muy rápido-- ¿Tienes miedo?"
        "Tú solo te excusas con que te han tomado por sorpresa. No tienes el coraje de confesarles que tienes miedo de lo que podría pasar si es que algún día llegan a verte con hambre."
        "Sabes que cambiar el tema es la mejor opción que tienes actualmente. Por lo que preguntas, con genuina curiosidad."
        nj "¿Dónde estaban?" 
        hide solaris_normal
        show solaris_enojo at left
        solaris "Supervisando los colapsos estelares."
        hide aeliana_feliz
        show aeliana_serio at right
        aeliana "La señora Duae quiere que aprendamos de ellos."
        "Aeliana agrega, ante la nula explicación de Solaris."
        menu:
            "¿Qué es eso?":
                "El término no te causa buena espina, sabes que las estrellas pueden llegar a colapsar, por ende es muy probable que tus niños también puedan sufrir aquello."
                "La idea es saber para poder actuar bajo una base de conocimiento si es que lo llegases a necesitar."
                solaris "Mmh... es un proceso que pasamos todas las estrellas."
                solaris "Cuando no hay más combustible, explotamos."
                "¡¿Huh?!"
                nj "¡¿Se mueren?!"

            "¿Vieron la muerte de estrellas?":
                "Ambas rien, solo Aeliana tiene el reparo de tapar su risa con la mano. Solaris en cambio, suelta una carcajada libre, que retumba en todo el patio."
                "La reacción de ambas mujeres te aterra, es una actitud muy extraña. Es como si tomasen la muerte como un concepto insignificante"
        
        aeliana "La muerte es para lo organico."
        aeliana "Solo lo sufren los del número 4 al 6."
        aeliana "Nosotras somos mejor que eso."
        "Tu rostro no logra ocultar la mueca de horror que se te escapa de los labios. Muchas veces se te olvida que estás tratando con entidades que simulan un cuerpo similar al tuyo en apariencia, nada más..."
        solaris "¡No te pongas así!"
        solaris "Si pudieras ver una supernova, entenderias todo."
        solaris "Espero que mi colapso sea presenciado por la señora Duae---"
        solaris "Sería un honor, ahhh~"
        "Okay... ya comprendes de donde viene esta mentalidad de propósito por sobre el 'yo'. Probablemente a Shams y a Noor también se le ha inculcado esta manera de pensar..."
        "Te preocupa..."
        nj "Noor---"
        aeliana "Escúchame, [nombrejugador]."
        scene act3_u11 with dissolve
        play music "audio/mechanique.mp3" fadein 2.0 volume 0.1

        "Se coloca al frente, invadiendo tu espacio personal, ignorando tu deseo de retroceder para poner distancia, Aeliana te detiene agarrando tu hombro."
        aeliana "Entiendo te preocupes por tu hijos."
        if noor_hambre >= 1:
            aeliana "Pero no te metas en cosas que no sabes."
            aeliana "Desde aquí siento como la masa de Noor a aumentado."
            aeliana "Él no puede comer más de lo establecido por la señora Duae y su Santidad Septem."
            nj "¡Lo quieren matar!"
            nj "Va a terminar muerto si su masa--combustible, la mierda que sea-- se agota!"
            solaris "¡Hey! no le subas la voz a---"
            "Aeliana levanta la mano, en signo de que guarde silencio. Solaris cierra la boca al instante."
            aeliana "No existe la muerte para las estrellas."
            nj "¡Noor no es una estrella como ustedes!"
            nj "¡Es un niño!"
            scene jardin_chicas with dissolve
            "Has tenido suficiente."
            "Un solo grito, llamando el nombre de tus niños, basta para que los tengas a tu lado. Mirando confundidos la escena."
            "Tú no ofreces explicación, solo los tomas y comienzas a alejarte de la residencia. Ellas no hacen nada por detenerte."
            aeliana "Deberías prestar más atención a lo que pasa con tus niños."
            aeliana "Shams ya no gusta de dormir en las noches."
            aeliana "Dice que le da miedo soñar."
            aeliana "Espero que te hagas cargo de eso."
            "Shams intenta callarla, gritando que no diga eso, muy enojada con que su secreto haya sido liberado."
            scene jardinunum with dissolve
            "Tú no respondes y sigues caminando."
            "Lo último que escuchas por parte de ellas, es a Ignis preguntar que ha pasado."
        
        else:
            aeliana "Pero te aseguro que no les pasará nada malo."
            aeliana "No dejaría que nada malo le pase a tus criaturas, confía en los que saben."
            aeliana "Recuerda que no son humanos."
            aeliana "Por favor."
            aeliana "..."
            aeliana "No le digas a Shams, pero---"
            "Sus manos toman las tuyas, buscando un contacto más intimo. Baja su voz, como si de un secreto se tratara."
            aeliana "Dice que ya no le gusta ir a dormir."
            aeliana "Le tiene miedo a la oscuridad y a las sombras porque se parecen al monstruo que aparece cuando duerme..."
            aeliana "A Noor también le pasa."
            scene jardin_chicas with dissolve
            "Le prometes que averiguarás que es lo que está pasando con los niños. Pero no más de eso."
            "Aún tienes miedo."
            "Miedo a que tus hijos sufran las consecuencias de ser estrellas..."
            "Los chequeos no son por casualidad, Septem busca algo. La información que te ocultan tampoco es por falta de tacto..."
            "Hay algo estraño en todo esto."
            "Y vas a conseguir las respuestas que buscas."
            "..."
            scene jardinunum with dissolve
            "Te excusas diciendo que debes volver a casa, que necesitas hablar con Unum. Aeliana y Solaris entienden. Deseándote suerte, se despiden de ti."

    scene negro with pixellate
    "Fin del acto 3."
    "Tocará esperar a la última actualización para saber como acaba esta historia :3"
    $ MainMenu(confirm=False)()
    return

        


    




        





    
    #SEGUNDA SEMANA: ADOLECENTES
    #Tus brazos están completamente negros y no puedes mover mucho tus manos.
    #Los niños por fin te dicen de que van los chequeos, y te comentan que en Septem espera que en el futuro colisionen y se absorban.
    #Ellos te lo dicen como si no fuera nada del otro mundo... tú en cambio...
    #Se te da la opción de como sentirte  y luego que decirles.
    #Te sientes cada vez más cansado. pero Septem y Unum hacen todo lo que pueden para manterner tu cuerpo funcionando.
    #Unum te cuida mucho.
    #Los niños te vienen a ver siempre que pueden a tu pieza. Ya pueden controlar su calor.
        #Noor se pelea con Shams... alguien le está hablando.
        #Noor te confiesa que alguien le está hablando.
    #Tercera semana: Ya crecidos, Shams es mucho más fuerte y grande que Noor. Ella es la candidata para absorber a su hermano. 
    #Si has hecho caso a Septem, comienza la colisión de ambas estrellas para formar un hoyo negro.
    #Esto es con el fin de reemplazar el vacío con el hoyo negro... ambos tienen la misma función. devorar y mantener el jardín a raya.
    #El hoyo negro devora al vacío y lo reemplaza.
    #En el caso de que no pase eso. Nulla mantiene a ambos hermanos separados. Y toma posesión del más débil, Septem no se da cuenta de esto.
    #Ya que aquí no puso su ojo en tu cuerpo, y no sabía que tu marioneta tiene un pedazo de Nulla.

     












        


