# Modulos Globales
import os
import random

# Modeulos Locales
from pantalla import imprimirAhorcado

#================================================================
if not os.path.exists("nombres.txt"):
    with open("nombres.txt", "w", encoding="utf-8") as archivo_nombres:
        pass
#================================================================
# VARIABLES GENERALES

palabraAdivinada = []
letrasEscritas = []
letrasErradas = []
frase = ""
categoria = ""
nombre = ""


def limpiarPantalla():
    if os.name == "posix":
        os.system ("cls")
        
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
# La funcion corre en visual studio

#================================================================
#PALABRAS ALEATORIAS

def obtenerFrase(grupo):
    grupos = { 
        "series" : ["Mad Men", "Breaking Bad", "Fleabag", 
    "Game of Thrones", "Puedo destruirte", "The Americans", "The Office", "Succession", "BoJack Horseman" 
    "Six Feet Under", "Atlanta", "Chernobyl",
    "The Crown", "Deadwood", "Frena tu entusiasmo", "Black Mirror", "Better Call Saul", 
    "Sherlock", "Watchmen", "Line of Duty", "Friday Night Lights", "Girls", "True Detective",
    "Arrested Development", "La buena esposa", "El puente", "Fargo", "Downton Abbey", "Band of Brothers",
    "El cuento de la criada", "Borgen", "Peep Show", "Money Heist", "Comunidad", "The Good Fight", "Homeland",
    "Inside No 9", "The Bureau", "Small Axe", "Happy Valley", "The Shield", "The Big Bang Theory", "The Young Pope",
    "Dark", "The Underground Railroad", "House of Cards", "The Good Place", "Pose",
    "Detectorists", "Orange is the New Black", "Mare of Easttown", "Battlestar Galactica", "Iluminadas","Gilmore Girls",
    "Planeta Tierra", "Rick y Morty", "American Crime Story", "The Killing", "Mindhunter", "House", "Big Little Lies",
    "Inseguro", "Gente normal", "Narcos", "The Comeback", "The OA", "Dexter", "Westworld", "Treme", "Louie", "Zuther",
    "Hannibal", "Steven Universe", "Loki"],
        
    "colores" : ['Negro', 'azul', 'marron', 'gris', 'verde', 'naranja', 'rosa', 'purpura', 'rojo', 'blanco' ,' amarillo', "celeste"],
    
    "animales" : ['Aguila', 'Ardilla', 'allena', 'Caballo', 'Cocodrilo', 'Conejo' ,'Delfin',
    'Elefante' ,'Foca', 'Gato' ,'Gorila' ,'Hamster' ,'Hipopotamo', 'Hormiga', 'Iguana','Jirafa','Lagartos', 'Leon','Leopardo',
    'Lince','Lobo',' Mariposa','Medusa','Mono','Murcielago','Oso','Pájaros','Peces','Perro','Pinguino','Rinoceronte',
    'Serpiente','Tiburon','Tigre','Tortuga'],
    
    "paises" : ['Argentina','Aruba','Bahamas','Barbados','Belice','Bolivia','Brasil','Canada','Chile','Colombia ','Costa Rica',
    'Cuba', 'Curazao', 'Dominica', 'Ecuador',' El Salvador',' Estados Unidos ','Granada ','Guatemala','  Guyana', 'Haiti',
    'Honduras ','Jamaica','Mexico ','Nicaragua','Panama ','Paraguay',' Peru','Uruguay',' Venezuela',' Trinidad y Tobago']}
    grupoelegido = grupos[grupo]
    return random.choice(grupoelegido)

#================================================================

def prepararPalabra(original):
    global palabraAdivinada
    
    original = original.upper()
    
    palabraAdivinada = []
    
    
    for letra in original:
        if letra == " ":
            adivinada = True
        else:
            adivinada = False

        palabraAdivinada.append({
            
            "letra": letra,
            "adivinada": adivinada,
        })
        
def letraEstaEnPalabra(letra):
    global palabraAdivinada
    
    for letraCompuesta in palabraAdivinada:
        if letraCompuesta["letra"] == letra:
            return True
    return False

def descubrirLetra(letraEnviada):
    abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] 
    
    while True:
        if letraEnviada.upper() not in abc:
            letraEnviada = input("No se acepta números o caracteres extraños. Ingresa la letra: ")
        else:
            break
              
    global palabraAdivinada
    global letrasEscritas
    global letrasErradas
    global intentos
    global puntos
    global nombre
    
    letraEnviada = letraEnviada.upper()
    if letraEnviada in letrasEscritas:
        return
    else:
        letrasEscritas.append(letraEnviada)
        
    if not letraEstaEnPalabra(letraEnviada):        
        letrasErradas.append(letraEnviada)
        intentos -= 1
        puntos -= 10
    else:
        for letraCompuesta in palabraAdivinada:
            if letraCompuesta["letra"] == letraEnviada:
                letraCompuesta["adivinada"] = True
    
    

def jugar():
    global frase
    global nombre
    global intentos
    global puntos
    
    puntos = 60
    intentos = 6
    frase = obtenerFrase(categoria)
       
    prepararPalabra(frase)

    while True:
        imprimirtituloAhorcado()
        imprimirAhorcado(intentos)
        imprimirPalabra()
        imprimirErradas()
        descubrirLetra(input("""
        ◤--          --◥
        | Ingrese letra |
        ◣--          --◢
        |👉 """))
        limpiarPantalla()
        
        if intentos <= 0:
            leaderboard_1(nombre, intentos)
            print("""
            ◤--        --◥
            |  GAME OVER  |
            ◣--        --◢
              ⛓️       ⛓️
            ◤--           --◥
            | La palabra era |
            ◣--           --◢
            """)
            imprimirPalabraOriginal()
            reiniciarTodo()
            input("""
            ◤--                                  --◥
            | Presione enter para continuar jugando |
            ◣--                                  --◢
            |👉 """)
            return
        if haGanado():
            leaderboard_1(nombre, intentos)
            print("""
                   🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊
                   
                     🎉  🎈 Felicitaciones ganaste 🎉  🎈  
                   
                   🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊
                   """)
            print("Obtuviste: ", puntos, " pts")
            reiniciarTodo()
            input("""
            ◤--                                  --◥
            | Presione enter para continuar jugando |
            ◣--                                  --◢
            |👉 """)
            return
    
#================================================================
# PARTE: ESTADO DEL HOMBRE
# ESTADO DE LA PARTIDA: GANAR / PERDER

def imprimirtituloAhorcado():
    print(f"""\n **** El Ahorcado *** 
Categoria seleccionada: {categoria.title()}""")

def imprimirErradas():
    global letrasErradas
    print("Errores: ", end="")
    for letra in letrasErradas:
        print("[", letra, "] ", end="")
    print("")

def imprimirPalabra():
    for letraCompuesta in palabraAdivinada:
        if letraCompuesta["adivinada"]:
            print(letraCompuesta["letra"], end="")
        else:
            print("-", end="")
    print("")

def imprimirPalabraOriginal():
    print("           ", "   ⛓️       ⛓️")
    print("           ", "◤--                         --◥") 
    print("              ", frase.upper())
    print("           ", "◣--                         --◢")
    print("           ", "   ⛓️       ⛓️")
    print("           ", "◤--                         --◥")
    print("          ","  |  Obtuviste: ", puntos, " pts |")
    print("           ", "◣--                         --◢")

def haGanado():
    global palabraAdivinada
    
    for letra in palabraAdivinada:
        if not letra["adivinada"]:
            return False      
    return True 

#================================================================
#PARTE: MENUS 

def menu_ahorcado():
    global categoria

    limpiarPantalla()
    menu = """
        ◤--      El Ahorcado    --◥
        | Seleccione una categoria |
        | [1] Series               |
        | [2] Paises               |
        | [3] Colores              |
        | [4] Animales             |
        | [5] Regresar             |
        ◣--                     --◢
            ⛓️                ⛓️
        ◤--               --◥
        | Ingrese una opción |
        ◣--               --◢
        |👉 """
    eleccion = input(menu)
    
    while True:
        eleccion_3 = ["1", "2", "3", "4", "5"]
        menu_3 = """
        ◤--      El Ahorcado    --◥
        | Seleccione una categoria |
        | [1] Series               |
        | [2] Paises               |
        | [3] Colores              |
        | [4] Animales             |
        | [5] Regresar             |
        ◣--                     --◢
            ⛓️                ⛓️
        ◤--                                                --◥
        | No se permite botones que no esten en las opciones: |
        ◣--                                                --◢
        |👉 """
        if eleccion not in eleccion_3:
            limpiarPantalla()
            eleccion = input(menu_3)
            limpiarPantalla()
            if eleccion == "1":
                categoria = "series"
                limpiarPantalla()
                jugar()
            if eleccion == "2":
                categoria = "paises"
                limpiarPantalla()
                jugar()
            if eleccion == "3":
                categoria = "colores"
                limpiarPantalla()
                jugar()
            if eleccion == "4":
                categoria = "animales"
                limpiarPantalla()
                jugar()
        else:
            break
            
    if eleccion == "1":
        categoria = "series"
        limpiarPantalla()
        jugar()
    if eleccion == "2":
        categoria = "paises"
        limpiarPantalla()
        jugar()
    if eleccion == "3":
        categoria = "colores"
        limpiarPantalla()
        jugar()
    if eleccion == "4":
        categoria = "animales"
        limpiarPantalla()
        jugar()

def menu_principal():
    global nombre
    limpiarPantalla()
    menu = """
    ◤--     UTEC GAMES      --◥
    | [1] Juego del ahorcado   |
    | [2] Mad Story            |
    | [3] Otros juego          |
    | [4] Leaderboard          |
    | [5] Salir                |
    ◣--                     --◢
      ⛓️                ⛓️
     ◤--               --◥
     | Ingrese una opción |
     ◣--               --◢
    |👉 """
    eleccion_1 = ["1", "2", "3", "4", "5"]
    eleccion = input(menu)
    
    while True:
        menu_1 = """
        ◤--     UTEC GAMES      --◥
        | [1] Juego del ahorcado   |
        | [2] Mad Story            |
        | [3] Otros juego          |
        | [4] Leaderboard          |
        | [5] Salir                |
        ◣--                     --◢
            ⛓️                ⛓️
        ◤--                                                --◥
        | No se permite botones que no esten en las opciones: |
        ◣--                                                --◢
        |👉 """ 
        
        if eleccion not in eleccion_1:
            limpiarPantalla()
            eleccion = input(menu_1)
            limpiarPantalla()
            if eleccion == "1":
                limpiarPantalla()
                nombre_1 = input("Nombre: ").upper()
                nombre = nombre_1.strip()
                menu_ahorcado()
            if eleccion == "2":
                limpiarPantalla()
                mad_story(obternerHistoria())
            if eleccion == "3":
                limpiarPantalla()
                otro_juego()
            if eleccion == "4":
                limpiarPantalla()
                leaderboard()
            if eleccion == "5":
                limpiarPantalla()
                exit()
        else:
            break
           
    if eleccion == "1":
        limpiarPantalla()
        nombre_1 = input("Nombre: ").upper()
        nombre = nombre_1.strip()
        menu_ahorcado()
    if eleccion == "2":
        limpiarPantalla()
        mad_story(obternerHistoria())
    if eleccion == "3":
        limpiarPantalla()
        otro_juego()
    if eleccion == "4":
        limpiarPantalla()
        leaderboard()
    if eleccion == "5":
        limpiarPantalla()
        exit()

def otro_juego():
    m = """
    ◤-- Elige otro juego --◥
    | [1] SUDOKU            |
    | [2] RUN RUN           |
    | [3] Menú principal    |
    ◣--                  --◢
       ⛓️                ⛓️
     ◤--                --◥
     | Ingrese una opción: |
     ◣--                --◢
    |👉 """
    
    opcion = input(m) 
    
    while True:
        opcion_1 = ["1", "2", "3"]
        m_1 = """
            ◤-- Elige otro juego --◥
            | [1] SUDOKU            |
            | [2] RUN RUN           |
            | [3] Menú principal    |
            ◣--                  --◢
              ⛓️                 ⛓️
        ◤--                                                --◥
        | No se permite botones que no esten en las opciones: |
        ◣--                                                --◢
        |👉 """
    
        if opcion not in opcion_1:
            limpiarPantalla()
            opcion = input(m_1)
            limpiarPantalla()
            if opcion == "1":
                limpiarPantalla()
                sudoku()
            if opcion == "2":
                limpiarPantalla()
                run_run()
            if opcion == "3":
                limpiarPantalla()
                menu_principal()
        else:
            break
                    
    if opcion == "1":
        limpiarPantalla()
        sudoku()
    if opcion == "2":
        limpiarPantalla()
        run_run()
    if opcion == "3":
        limpiarPantalla()
        menu_principal()

def leaderboard_1(a, puntos):
    
    if os.path.exists(a + ".txt"):
        with open(a + ".txt", "r", encoding = "utf-8") as  nuevo_archivo:
            lista_nombres = nuevo_archivo.readlines() 
        pun = int(lista_nombres[0].strip())
    
        with open(a + ".txt", "w", encoding = "utf-8") as nuevo_archivo:
            nuevo_archivo.write(str(pun + puntos * 10))    
    else:
        with open("nombres.txt", "a", encoding = "utf-8") as archivo_nombres:
            archivo_nombres.write(a + "\n")  
        with open(a + ".txt", "w", encoding = "utf-8") as nuevo_archivo:
            nuevo_archivo.write(str(puntos * 10))

def leaderboard():
    print("**** Leaderboard *** ")
    print()
    print("Jugadores")
    
    with open("nombres.txt", "r", encoding = "utf-8") as archivo_nombres:
        lista_nombres = archivo_nombres.readlines()
    
    for i in range(len(lista_nombres)):
        lista_nombres[i] = lista_nombres[i].strip()
        
    if len(lista_nombres) == 0:
        print("No hay jugadores")
    
    else:
        n = 0
        jugadores = dict()
        puntaje = list()
        for nombre in lista_nombres:
            n += 1
            with open(nombre + ".txt", "r", encoding = "utf-8") as nuevo_archivo:
                punto = nuevo_archivo.read()
                print("[{}] {} -- {} pts".format(n, nombre, punto))
                """
                
                puntaje.append(int(punto))
                jugadores.setdefault(punto, nombre)
                
                """
        
            #print(puntaje.sort())
            
            
    m = """ 
        ◤--                          --◥
        | Presione enter para continuar |
        ◣--                          --◢
        |👉 """
    opcion = input(m)

def sudoku(): 
    m = """ 
        🎅♥☻♠☻♣☻♦☻ - - - SUDOKU - - - ☻♦☻♣☻♠☻♥🎅 
    
        🎅 ♥☻♠☻♣☻♦☻ - PROXIMAMENTE - ♥☻♠☻♣☻♦☻ 🎅
        [1] Regresar
        
            ◤--                --◥
            | Ingrese una opción: |
            ◣--                --◢
            |👉 """
    opcion = input(m)

    while True:
        m_2 = """ 
        🎅♥☻♠☻♣☻♦☻ - - - SUDOKU - - - ☻♦☻♣☻♠☻♥🎅 
    
        🎅 ♥☻♠☻♣☻♦☻ - PROXIMAMENTE - ♥☻♠☻♣☻♦☻ 🎅
        [1] Regresar
        
        ◤--                                                --◥
        | No se permite botones que no esten en las opciones: |
        ◣--                                                --◢
        |👉 """
        
        if opcion != "1":
            opcion = input(m_2)
        if opcion == "1":
            limpiarPantalla()
            otro_juego()
        else:
            break
            
    if opcion == 1:
        limpiarPantalla()
        otro_juego()
      
def run_run():
    m = """"
        🦊                           🦊 
        🦊     🐕 .RUN RUN. 🐕 
        🦊                           🦊

        🕹️
        🕹️                  🕹️
        🕹️   PROXIMAMENTE   
        🕹️                  🕹️
        🕹️

        [1] Regresar
        ◤--                --◥
        | Ingrese una opción: |
        ◣--                --◢
        |👉 """
    opcion = input(m)

    while True:
        m_3 = """"
        🦊                           🦊 
        🦊     🐕 .RUN RUN. 🐕 
        🦊                           🦊

        🕹️
        🕹️                  🕹️
        🕹️   PROXIMAMENTE   
        🕹️                  🕹️
        🕹️

        [1] Regresar
        ◤--                                                --◥
        | No se permite botones que no esten en las opciones: |
        ◣--                                                --◢
        |👉 """
        if opcion != "1":
            opcion = input(m_3)
        if opcion == "1":
            limpiarPantalla()
            otro_juego()
        else:
            break
    
    if opcion == "1":
        limpiarPantalla()
        otro_juego()
    
#=================================================================
        
def obternerHistoria():
    historias = []
    print("**** Mad Story ***")
    print("""Bienvenidos a Mad Story. Por favor conteste las
    siguientes preguntas.""")
    animales =  input("👉 Ingrese el nombre de un animal: ")
    profesion = input("👉 Ingrese el nombre de una profesion: ").capitalize()
    prenda = input("👉 Ingrese un tipo de prenda: ")
    objeto = input("👉 Ingrese el nombre de un objeto: ")
    nombre = input("👉 Ingrese un nombre: ").capitalize()
    lugar  = input("👉 Ingrese el nombre de un lugar: ").capitalize()
    comida = input("👉 Ingrese el nombre de una comida: ")
    color = input("👉 Ingrese un color: ")
    adjetivo = input("👉 Ingrese un adjetivo: ")
    
    h_1 = f""" 
    LAS MANZANAS
    
    Hoy recogimos manzanas de la granja de _{nombre}_. No tenía idea de que había tantas variedades diferentes de manzanas. Comí manzanas de _{color}_, directamente del árbol que el _{profesion}_ probó como {comida}. Luego había una manzana _{adjetivo}_ que parecía un _{objeto}_. Cuando nuestra bolsa estaba llena, fuimos en un paseo en _{animales}_ gratis a _{lugar}_ y de regreso. Terminó en una pila de heno donde llegamos caminando. Apenas puedo esperar para llegar a casa y cocinar con las manzanas. ¡Vamos a hacer pasteles de manzanas con _{comida}_ y _{prenda}_."""

    h_2 = f"""  
    EL FOTOGRAFO
    
    _{comida}_, dijo el fotógrafo mientras la cámara parpadeaba! _{nombre}_ y yo habíamos ido a _{lugar}_ para tomar nuestras fotos en mi cumpleaños. La primera foto que realmente queríamos era una foto de nosotros vestidos como _{animales}_ fingiendo ser un _{profesion}_. Cuando vimos la segunda foto, era exactamente lo que queríamos. Ambos parecíamos un _{objeto}_ usando _{prenda}_ y _{verbo}_, exactamente lo que tenía en mente."""
    
    h_3 = f"""
    LA MARIPOSA
    
    Anoche soñé que era una mariposa  _{adjetivo}_  con _{color}_ splocthes que parecían _{objeto}_. Volé a _{lugar}_ con mi mejor amigo y _{nombre}_ que era un _{animales}_. Comimos un poco de  _{comida}_ cuando llegamos allí y luego decidimos _{verbo}_ y el sueño terminó cuando dije: _{profesion}_"""
    
    h_4 = f"""
    LA TÍA SUSY
    
    Una mañana saliendo del trabajo me encontré con Susy diaz y me pidio que porfavor la acompañara a su concierto porque le faltaba alguien que bailara junto a su elenco. Yo me dije: esta es tu oportunidad, y entre en mi modo _{animales} decidido, inmediatamente le dije que acepto que yo ya tenía experiencia porque soy _{profesion}_ y me subi a su bus el cual se dirigia al lugar del concierto, entonces me dijo que me cambiara y le pedi si me podria dar ropa y me dio su _{prenda}_ de la suerte, agarrre un _{objeto}_ y le dije quedatelo, para que nunca me olvide Tia Susy. A ella le caí tan bien que me bautizo con el nombre de _{nombre}_, yo me emocione mucho, cuando de pronto veo por la ventana y ya habíamos llegado a _{lugar}_ donde seria el concierto, cuando llegué me ofrecieron un _{comida}_ para comer antes del concierto, estuvo delicioso. Cuando termine nos dirigimos al escenario todo era de color _{color}_, empezo el show y comence a sacar mis pasitos prohibidos, lo hize de lo mejor, al finalizar Susy me felicito y me dijo eres muy _{adjetivo}_, luego me despedi y fue asi como vivi el mejor dia de mi vida.
    """
    h_5 = f"""
    Hoy fui a visitar a mi abuelo_{nombre}_a su granja. Mientras me paseaba para ver como iban sus cosechas me quede muy sorprendido, no tenía idea de que había tantas variedades diferentes de manzanas. Pero sobre todo me quede muy sorprendido al encontrar una de color _{color}_, directamente de un árbol que tenia el mismo color.
    Mientras comía una de esas manzanas se acercó a mi un _{profesion}_, se me quedó observando mientras yo seguía comiendo, me sentía muy incómodo. Creí que tenía hambre y le ofrecí un plato de {comida} le dije que el granjero era mi abuelo y le podíamos invitar. El hombre no respondió y me miraba cada vez más con esos ojos de _{objeto}_, me enfade tanto que le dije que era un _{adjetivo}_ y le tire mi manzana en la cara y me fui corriendo, en el camino encontré un _{animales}_ el cual decidí montar para llegar mas rapido donde mi abuelo, pero como todo en la vida me sale mal siempre, este tropezó y me caí, manche mi _{prenda}_ por completo, seguía muy molesto, pensaba en los días felices cuando estaba en _{lugar}_. Pero bueno seguí caminando y sin darme cuenta ya había llegado a la casa de mi abuelo, su granja era gigantesca, pero al fin llegue, y de pronto veo a ese hombre con mi abuelo y se notaba muy molesto. Al llegar  a ellos mi abuelo me dijo que ese árbol era de aquel hombre y que me demandaria por comer parte de su cosecha y golpearlo. Y bueno eso es todo, si alguien pregunta por mí, o por manzanas, diganle que me morí. Adiós
    """
    
    h_6 = """
    Este es el camino del_{animal}{nombre} el siempre lleva en su cabeza un {ropa}y en sus ojos unas {objeto} {color} y en sus patas unos {objetos } {color},su profesión era {profesión} los dientes de los niños y a cambio les daba monedas y luego de acabar con su labor se iba a comer un delicioso {comida} para luego irse a descansar.
    """
    historias = [h_1.replace("_", '"'), h_2.replace("_", '"'), h_3.replace("_", '"'), h_4.replace("_", '"'), h_5.replace("_", '"')]

    return random.choice(historias)
    
def mad_story(historia):
    limpiarPantalla()
    print("**** Mad Story ***")
    print(historia)
    print()
    print()
    input("⚜️ PRECIONE ENTER PARA IR AL MENÚ PRINCIPAL ⚜️")
    menu_principal()
                     
#=================================================================

def main():
    while True:
        menu_principal()

def reiniciarTodo():
    global letrasEscritas
    global palabraAdivinada
    global letrasErradas
    palabraAdivinada = []
    letrasEscritas = []
    letrasErradas = []
main()