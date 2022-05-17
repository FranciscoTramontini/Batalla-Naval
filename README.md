# BATALLA NAVAL
 es un juego tradicional de estrategia y algo de suerte, que involucra a dos jugadores (uno de ellos es la mquina).

## DESCRIPCION DEL JUEGO.

 ### TABLERO:
 La dimension de los tableros son de 10x10. Los jugadores manejan un tablero de océano y un tablero de tiro; cada uno divididos en casillas.
 Cada tablero representa una zona diferente del mar abierto: la propia y la contraria. En el primer tablero, el jugador coloca sus barcos y 
 registra los tiros del oponente; en el otro, se registran los tiros propios contra el otro jugador, diferenciando los impactos y los que 
 dan al agua. Al tiempo, se deduce la posición de los barcos del enemigo. El enemigo lo maneja la computadora, es decir, las coordenadas de 
 ataque son aleatoriamente.

 ### BARCOS:
 Al comenzar, cada jugador posiciona sus barcos en el primer tablero, de forma secreta, invisible al oponente. Cada uno contara con los 
 siguientes barcos a colocar: cinco casillas consecutivas conforman un PORTAAVIONES; cuatro casillas consecutivas conforman un BUQUE;
 tres casillas consecutivas conforman un SUBMARINO; una casilla aislada conforman una LANCHA.
 
 #### Los cuales se reparten en un portaavion, tres buques, dos submarinos y cinco lanchas.
 
 #### No se podrán colocar barcos pegados, es decir, entre barco y barco hay separaciones de una o mas casillas.

 ### DESARROLO DE LA BATALLA NAVAL:
 Una vez que todos los barcos dichos anteriormente fueron posicionados, se inicia una serie de rondas. En cada ronda, cada jugador en su turno 
 dispara (solo misiles,es decir, si le dispara a un barco solo le dañara una casilla) hacia la flota de su oponente indicando una posición 
 (las coordenadas de una casilla), la que registra en el segundo tablero. Si esa posición es ocupada por parte de un barco contrario, el oponente
 decira TOCADO si todavía quedan partes del barco (casillas) sin dañar, o HUNDIDO si con ese disparo el barco ha quedado totalmente destruida 
 (es decir, si la coordenada es la última de las casillas que conforman el barco que quedaba por dañar). Si la posición indicada no corresponde
 a una parte de barco dira AGUA. Si ya se ingreso la coordenada pedida, perdera un turno.
 Cada jugador referenciará en ese segundo tablero los disparos que han caído sobre una nave oponente y los que han caído al agua: se señalaran 
 con un caracter '·' los disparos que cayeron al agua y con un 'X' los que cayeron en alguna parte del barco. Contaran con 73 disparos cada jugador.

 ### FINAL DEL JUEGO:
 El juego puede terminar con un ganador o en empate:

     HAY GANADOR: 
     quien destruya primero todas los barcos de su oponente será el vencedor, en caso de que el jugador que comenzó la partida 
     hunda en su última jugada el último barco de su oponente que quedaba a flote, el otro jugador tiene derecho a una última 
     posibilidad para alcanzar el empate, a un último disparo que también le permita terminar de hundir la flota contraria, 
     lo que generaria un empate.

     EMPATE: 
     esto sucede cuando los dos jugadores llegan a la cantidad maxima de disparos (73) y los dos siguen con barcos sin hundir 
     en su tablero de barcos o si en la ultima jugada los dos destruyen todos los barcos.
 
 ## REQUISITOS
 Tener instalado el lenguaje de programación Python.
 
 ## COMO JUGAR
    * Leer atentamente la descripcion del juego.
    * Crear en el archivo "tab_jugador.txt" el tablero con tus barcos, siempre respetando la descripcion 
      del grupo en la parte de barcos.
    * Pedir ayuda para crear el tablero del oponente en "tab_oponente.txt" respetando lo mismo para el 
      tablero del jugador. Recodar que tanto este tablero como el de jugador deben estar en la misma 
      carpeta que el archivo del juego. Dejo uno de prueba, aclaro que son distintos los tableros.
    * Hecho todo esto, abrir el archivo en algun editor y correrlo. Se le abrira la ventana de la 
      consola con el juego y A JUGAR! y obviamente a GANAR!
