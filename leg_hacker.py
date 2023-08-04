

print("""
  +===============================================================================+
  | Escribe un programa que reciba un texto y transforme lenguaje natural a       |
  | "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje    |
  | se caracteriza por sustituir caracteres alfanuméricos.                        |
  | - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) |
  |   con el alfabeto y los números en "leet".                                    |
  |   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a") |
  +===============================================================================+
      """)

def usuarioTexto(): #Esta función solicita al usuario que ingrese un texto y devuelve la entrada como una cadena/str.
    usuario: str = input("Ingrese un texto --> ")
    return usuario

leet : dict = { # Diccionario el cual contiene los caracteres del legnuaje leet segundo el alfabeto.
      ' ': ' ',
    'a': '4',
    'b': 'I3',
    'c': '[',
    'd': ')',
    'e': '3',
    'f': '|=',
    'g': '&',
    'h': '#',
    'i': '1',
    'j': ',_|',
    'k': '>|',
    'l': '1',
    'm': '/\\/\\',
    'n': '^/',
    'o': '0',
    'p': '|*',
    'q': '(_,)',
    'r': 'I2',
    's': '5',
    't': '7',
    'u': '(_)',
    'v': '\\/',
    'w': '\\/\\/',
    'x': '><',
    'y': 'j',
    'z': '2',
    '1': 'L',
    '2': 'R',
    '3': 'E',
    '4': 'A',
    '5': 'S',
    '6': 'b',
    '7': 'T',
    '8': 'B',
    '9': 'g',
    '0': 'o'}

text_usuaio = usuarioTexto()

Lenguaje_hacker : list = [] #Esta lista alamecena los caracters dados por el usuario y luego dentro de ella se convierten en legnauje leet.

ind_dl : int= 0 # Esta variable representa el índice de la lista 'Lenguaje_hacker'.
for i in text_usuaio: # Iteramos sobre cada carácter del texto ingresado por el usuario.
  Lenguaje_hacker.append(i) # Agregamos cada carácter a la lista 'Lenguaje_hacker'.
  for rec_dict in leet: # Buscamos la transformación leet para cada carácter y lo agregamos a la lista.
    if i == rec_dict: # Validamos si el carácter debe ser transformado a leet.
      for x in Lenguaje_hacker: # Iteramos sobre los caracteres de la lista 'Lenguaje_hacker' para reemplazar el carácter.
        Lenguaje_hacker.pop(ind_dl) # Eliminamos el carácter sobrante de la lista.
        ind_dl+=1
        x = leet[rec_dict] # Obtenemos la transformación leet del diccionario.
        Lenguaje_hacker.append(x) # Agregamos la transformación leet a la lista.
        break
      break

cadena_resultante = "".join(Lenguaje_hacker) 
print(f'{text_usuaio} se a convetido a leet/"lenguaje hacker" --> {cadena_resultante}')