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

def merge(left, right):
    merged_list = [0 for x in range(len(left) + len(right))]
    # SU SOLUCION EMPIEZA AQUI
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            merged_list[k] = left[i]
            i += 1
        else:
            merged_list[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        merged_list[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        merged_list[k] = right[j]
        j += 1
        k += 1

    # SU SOLUCION TERMINA AQUI
    return merged_list

def merge_sort(lista):
    if len(lista) == 1:
        return lista
    elif len(lista) > 1:
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:]
        
        der = merge_sort(right)
        izq = merge_sort(left)
        
    return merge(izq, der)

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
                nombre_1 = input("""
                ◤--                 --◥
                | Ingrese su nombre:   |
                ◣--                 --◢
                |👉 """).upper()
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
        nombre_1 = input("""
        ◤--                 --◥
        | Ingrese su nombre:   |
        ◣--                 --◢
        |👉 """).upper()
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
        puntaje = list()
        for nombre in lista_nombres:
            with open(nombre + ".txt", "r", encoding = "utf-8") as nuevo_archivo:
                punto = int(nuevo_archivo.read())
                jugadore_puntos = (punto, nombre)
                puntaje.append(jugadore_puntos)
        
        jugadores = merge_sort(puntaje)
        n = 1
        print("◤--                  --◥")
        for i in jugadores[-1::-1]:
            print(" [{} °] {} -- {} pts ".format(n, i[1], i[0]))
            print("                      ")
            n += 1
        print("◣--                  --◢")
            
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
    animales =  input("""
    ◤--                                          
    | Ingrese un animal: 
    |👉 """)
    profesion = input("""
    | Ingrese el nombre de una profesion:                 
    | 👉 """).capitalize()  
    prenda = input("""
    | Ingrese un tipo de prenda:
    | 👉 """)
    objeto = input("""
    | Ingrese el nombre de un objeto: 
    | 👉 """)
    nombre = input("""
    | Ingrese un nombre:
    | 👉 """).capitalize()
    lugar  = input("""
    | Ingrese el nombre de un lugar:
    | 👉 """).capitalize()
    comida = input("""
    | Ingrese el nombre de una comida: 
    | 👉""")
    color = input("""
    | Ingrese un color: 
    | 👉 """)
    adjetivo = input("""
    | Ingrese un adjetivo: 
    | 👉 """)
    
    h_1 = f"""
    LAS MANZANAS 

    Hoy fui a visitar a mi abuelo _{nombre}_ a su granja. Mientras paseaba para ver cómo iban sus cosechas me quedé muy 
    sorprendido, no tenía idea de que había tantas variedades diferentes de manzanas. Pero sobre todo me quede muy sorprendido 
    al encontrar una de color _{color}_, directamente de un árbol que tenia el mismo color.
    Mientras comía una de esas manzanas se acercó a mi un _{profesion}_, se me quedó observando mientras yo seguía comiendo, 
    me sentía muy incómodo. Creí que tenía hambre y le ofrecí un plato de _{comida}_ le dije que el granjero era mi abuelo y 
    le podíamos invitar. El hombre no respondió y me miraba cada vez más con esos ojos de _{objeto}_, me enfade tanto que le 
    dije que era un _{adjetivo}_ y le tire mi manzana en la cara y me fui corriendo, en el camino encontré un _{animales}_ el cual 
    decidí montar para llegar más rápido donde mi abuelo, pero como todo en la vida me sale mal siempre, este tropezó y me caí, manche 
    mi _{prenda}_ por completo, seguía muy molesto, pensaba en los días felices cuando estaba en _{lugar}_. Pero bueno seguí caminando 
    y sin darme cuenta ya había llegado a la casa de mi abuelo, su granja era gigantesca, pero al fin llegue, y de pronto veo a ese hombre 
    con mi abuelo y se notaba muy molesto. Al llegar  a ellos mi abuelo me dijo que ese árbol era de aquel hombre y que me demandaría 
    por comer parte de su cosecha y golpearlo. Y bueno eso es todo, si alguien pregunta por mí, o por manzanas, diganle que me morí.                                                                                                                                                        
    """

    h_2 = f"""
    EL OTRO PLANETA
    
    Un día iba camino a mi casa cuando encontré un _{animales}_ gigante me dijo que venía de un planeta nunca descubierto, en 
    donde era _{profesion}_, yo me quedé muy sorprendido, y de pronto me dijo que necesitaba mi _{prenda}_, que con eso salvaría 
    a su mundo de los extraterrestres, se la di y de pronto abrió sus alas gigantes y me pidió que me subiera encima para volar con 
    él a su planeta, yo muy decidido a ayudarlo agarre un_{objeto}_ que estaba tirado en la calle y decidí ir a batallar, en el camino 
    le pregunte cual era su nombre, a lo que respondió me llamo _{nombre}_, me quedé muy sorprendido con ese nombre. Pasados unos 
    minutos nos dio mucha hambre y decidimos bajar a comer algo, nos encontrábamos en _{lugar}_ y por ahi habia una vendedora 
    de _{comida}_, estabamos comiendo de lo mejor cuando alguien se acerca y me dice que me estoy poniendome de color _{color}_, yo 
    no entendia que pasaba y de pronto senti como me desmayaba, desperte en el hospital y la doctora me dijo que me habian encontrado 
    en la calle borracho junto a un _{animales}_ e intentando comer mi zapato, ahi me di cuenta que todo habia sido mi imaginación y me 
    dije: eres tan _{adjetivo}_ y por eso me amo. Sean como yo muchachos, este es el fin de mi historia.                                                                                                                                                
    """
    
    h_3 = f"""
    TÍA SUSY
    
    Una mañana saliendo del trabajo me encontré con Susy Díaz y me pidió que por favor la acompañara a su concierto 
    porque le faltaba alguien que bailara junto a su elenco. Yo me dije: ¡Esta es tu oportunidad! y entre en mi 
    modo _{animales}_ decidido, inmediatamente le dije que acepto, que yo ya tenía experiencia porque soy _{profesion}_ y 
    me subí a su bus el cual se dirigía al lugar del concierto, entonces me dijo que me cambiara y le pedí si me podria dar 
    ropa y me dio su _{prenda}_ de la suerte, agarre un _{objeto}_ y le dije: ¡Quédatelo! para que nunca me olvide Tía Susy. A 
    ella le caí tan bien que me bautizó con el nombre de _{nombre}_, yo me emocione mucho, cuando de pronto veo por la 
    ventana y ya habíamos llegado a _{lugar}_ donde sería el concierto, cuando llegué me ofrecieron _{comida}_ para comer 
    antes del concierto, estuvo delicioso. Cuando termine nos dirigimos al escenario, todo era de color _{color}_, empezó 
    el show y comencé a sacar mis pasitos prohibidos, lo hize de lo mejor, al finalizar Susy me felicito y me dijo: Eres 
    muy _{adjetivo}_, luego me despedí  y fue así como viví el mejor día de mi vida.
    """
    
    historias = [h_1.replace("_", '"'), h_2.replace("_", '"'), h_3.replace("_", '"')]

    return random.choice(historias)
    
def mad_story(historia):
    limpiarPantalla()
    print("**** Mad Story ***")
    print(historia)
    print()
    print()
    input("""
          ⚜️ PRECIONE ENTER PARA IR AL MENÚ PRINCIPAL ⚜️
              /\___/\ ((
              \`@_@'/  ))
              {_:Y:.}_//
    ----------{_}^-'{_}----------
          """)
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