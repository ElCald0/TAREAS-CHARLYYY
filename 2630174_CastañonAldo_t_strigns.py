#-------------------------------------------------------------#
#          tarea Manejo de strings en python
#-------------------------------------------------------------#
"""
PORTADA
Nombre: Aldo Manuel Castañon Garcia 
Matricula: 2630174 
Grupo: IM 1-2
"""
#_____________________________________________________________#
#          Resumen ejecutivo de los strings
#_____________________________________________________________#

'''
Un string en Python es un tipo de dato que almacena una secuencia ordenada 
de caracteres (como letras, números, símbolos o espacios) delimitada por 
comillas simples ('hola') o dobles ("mundo").

Los strings son inmutables, por lo que su contenido no se puede modificar directamente pero se pueden
hacer operaciones que crean nuevos strings, python proporciona muchas operaciones utiles para los strings, 
como: concatenación, cálculo de longitud, segmentación, reemplazo de texto etc.

Validar la exactitud, y claridad de los datos es necesario para solucionar cualquier problema
del proyecto, si no se validan los datos, se corre el riesgo de tomar decisiones basadas en datos inexactos 
y poco representativos.

Esta tarea contiene seis problemas centrados en el manejo de cadenas, validacion de entrada,
formato, busqueda y procesamiento de texto cada problema incluye su descripcion, entradas, salidas,
validaciones y tres casos de prueba: normal, borde y error.
'''
#-------------------------------------------------------------#
#         Buenas practicas
#-------------------------------------------------------------#
"""
- Los strings son inmutables: cualquier cambio genera una nueva cadena.
- Es buena práctica normalizar entrada con strip() y lower() antes de compararla.
- Evitar "números mágicos" en índices; documentar qué extrae cada slice.
- Usar métodos de string en lugar de reescribir lógica básica.
- Diseñar validaciones claras: primero que no esté vacío, luego el formato.
- Escribir código legible: nombres de variables claros y mensajes de error entendibles
"""
#-------------------------------------------------------------#
#         Problemas
#-------------------------------------------------------------#
# Full name formatter (1 problem)
#-------------------------------------------------------------#
"""
Problem 1: <Full name formatter>
Descripción:
Dado el nombre completo de una persona en una sola cadena (por ejemplo: "aldo manuel castañon"), el programa debe:
1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
2) Mostrar el nombre formateado en Title Case y las iniciales (por ejemplo: A.M.C).

Entradas:
- full_name (string; nombre completo, puede venir en mayúsculas, minúsculas o mezclado, con espacios extra).

Salidas:
- "Formatted name: <Name In Title Case>"
- "Initials: <X.X.X.>"

Validaciones:
- full_name no debe estar vacío después de strip().
- Debe contener al menos dos palabras (por ejemplo, nombre y apellido).
- No aceptar cadenas que sean solo espacios.

Test cases:
1) Normal: aldo manuel castañon garcia -> Aldo Manuel Castañon Garcia; A.M.C.G.
2) Border: aldo castañon -> Aldo Castañon; A.C. (solo tiene dos palabras)
3) Error: "     " -> Error: invalid name (tambien da eror si solo hay una palabra y si pones numeros o simbolos)
"""
print("\n first problem 1: full name formater".title())
full_name = input("Enter your full name: ")
full_name = full_name.strip()
full_name = " ".join(full_name.split())

if full_name == " ":
    print("Error: invalid name")
else:
    name_parts = full_name.split()
    if len(name_parts) < 2:
        print("Error: enter at least two words")
    else:
        formatted_name = full_name.title()
        initials = ""
        for part in name_parts:
            initials = initials + part[0].upper() + "."
        print("Formatted name: " + formatted_name)
        print("Initials: " + initials)

#-------------------------------------------------------------#
# Simple email validator (2 problem)
#-------------------------------------------------------------#

"""
Descripción:
Valida si una dirección de correo tiene un formato básico correcto:
- Contiene exactamente un '@'.
- Después del '@' debe haber al menos un '.'.
- No contiene espacios en blanco.
Si el correo es válido, también muestra el dominio (la parte después de '@').

Entradas:
- email_text (string).

Salidas:
- "Valid email: true" o "Valid email: false"
- Si es válido: "Domain: <domain_part>"

Validaciones:
- email_text no vacío tras strip().
- Contar cuántas veces aparece '@'.
- Verificar que no haya espacios (no debe haber " " en email_text).

Test cases:
1) Normal: user@email.com -> valid
2) Border: a@b.c -> valid
3) Error: userexemail.com -> invalid

"""
print("\n problem 2: simple email validator".title())
email_text = input("Enter yuo email address: ").strip()

if email_text == "":
    print("Valid email: false")
elif email_text.count("@") != 1:
    print("Valid email: false")
elif " " in email_text:
    print("Valid email: false")
else:
    at_position = email_text.find("@")
    domain_part = email_text[at_position + 1:]
    if at_position == 0 or domain_part == "":
        print("Valid email: false")
    elif "." not in domain_part:
        print("Valid email: false")
    elif domain_part[0] == "." or domain_part[-1] == ".":
        print("Valid email: false")
    else:
        print("Valid email: true")
        print("Domain: " + domain_part)
#-------------------------------------------------------------#       
#    Problem 3: Palindrome Checker (ignoring spaces and case)
#-------------------------------------------------------------#

"""
Descripción:
Determina si una frase es un palíndromo, es decir, se lee igual de izquierda a derecha y de derecha
a izquierda, ignorando espacios y mayúsculas/minúsculas.

Ejemplos:
- "Anita lava la tina" -> palíndromo.
- "Hola mundo" -> no palíndromo.

Entradas:
- phrase (string).

Salidas:
- "Is palindrome: true" o "Is palindrome: false"
- (Opcional) Mostrar también la versión normalizada de la frase.

Validaciones:
- phrase no vacía tras strip().
- Longitud mínima razonable después de limpiar espacios (por ejemplo, al menos 3 caracteres).

Test cases:
1) Normal: Anita lava la tina -> true
2) Border: oso -> true
3) Error: hola chat -> false
"""
print("\n problem 3: palindrome verification".title())
phrase = input("Enter a phrase: ").strip()
normalized_phrase = phrase.lower().replace(" ", "")

if not phrase:
    print("Error: empty phrase")
elif len(normalized_phrase) < 3:
    print("Error: phrase must have at least 3 characters")
else:
    reversed_phrase = normalized_phrase[::-1]

    if normalized_phrase == reversed_phrase:
        print("Is palindrome: true")
    else:
        print("Is palindrome: false")

#-------------------------------------------------------------#
# Problem 4: Sentence word stats (lengths and first/last word)
#-------------------------------------------------------------#
"""
Descripción:
Dada una oración, el programa debe:
1) Normalizar espacios (quitar espacios al principio y al final).
2) Separar las palabras por espacios.
3) Mostrar:
   - Número total de palabras.
   - Primera palabra.
   - Última palabra.
   - Palabra más corta y más larga (por longitud).

Entradas:
- sentence (string).

Salidas:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"

Validaciones:
- Oración no vacía tras strip().
- Debe contener al menos una palabra válida después de split().

Test cases:
1) Normal: hola soy caldo jijijija
2) Border: Hello
3) Error: "     " (solo espacios)
"""
print("\n problem 4: sentence word stats".title())
sentence = input("Enter a sentence: ").strip()

if not sentence:
    print("Error: sentence cannot be empty")
else:
    word_list = sentence.split()

    if len(word_list) == 0:
        print("Error: no valid words")
    else:
        shortest_word = word_list[0]
        longest_word = word_list[0]

        for word in word_list:
            if len(word) < len(shortest_word):
                shortest_word = word

            if len(word) > len(longest_word):
                longest_word = word

        print("Word count: " + str(len(word_list)))
        print("First word: " + word_list[0])
        print("Last word: " + word_list[-1])
        print("Shortest word: " + shortest_word)
        print("Longest word: " + longest_word)

#-------------------------------------------------------------#
#Problem 5: Password strength classifier
#-------------------------------------------------------------#

"""
Descripción:
Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas
(puedes afinarlas, pero documéntalas en los comentarios).

Ejemplo de reglas:
- Weak: longitud < 8 o todo en minúsculas o muy simple.
- Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
- Strong: longitud >= 8 y contiene al menos:
  - una letra mayúscula,
  - una letra minúscula,
  - un dígito,
  - un símbolo no alfanumérico (por ejemplo, !, @, #, etc.).

Entradas:
- password_input (string).

Salidas:
- "Password strength: weak"
- "Password strength: medium"
- "Password strength: strong"

Validaciones:
- No aceptar contraseña vacía.
- Verificar longitud con len().


Test cases:
1) Normal: Hello123! -> strong
2) Border: Abc12345 -> medium
3) Error: empty input
"""

print("\n problem 5: password strength classifier".title())
password_input = input("Enter a password: ")

if not password_input:
    print("Error: password cannot be empty")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for character in password_input:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif not character.isalnum():
            has_symbol = True

    if len(password_input) < 8:
        strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    elif has_upper or has_lower:
        if has_digit or has_upper and has_lower:
            strength = "medium"
        else:
            strength = "weak"
    else:
        strength = "weak"

    print("Password strength: " + strength)

#-------------------------------------------------------------#    
# Problem 6: Product Label Formatter
#-------------------------------------------------------------#

"""
Descripción:
Dado el nombre de un producto y su precio, genera una etiqueta en una sola línea con el siguiente formato:

Product: <NAME> | Price: $<PRICE>

La cadena completa debe tener exactamente 30 caracteres:
- Si es más corta, rellena con espacios al final.
- Si es más larga, recorta hasta 30 caracteres.

Entradas:
- product_name (string).
- price_value (puede leerse como string o número; conviértelo a string para mostrarlo).

Salidas:
- "Label: <exactly 30 characters>"
(Puedes mostrar la etiqueta entre comillas para que se vean los espacios.)

Validaciones:
- product_name no vacío tras strip().
- price_value debe poder convertirse a un número positivo.

Test cases:
1) Normal: monitor, 250
2) Border: a, 0.01
3) Error: coca, -10
"""

print("\n problem 6: product label formatter".title())
product_name = input("Enter product name: ").strip()
price_value = input("Enter product price: ").strip()

if not product_name:
    print("Error: product name cannot be empty") 
else:
    try:
        price_number = float(price_value)

        if price_number <= 0:
            print("Error: price must be positive")
        else:
            label = f"Product: {product_name} | Price: ${price_number:g}"
            label = label[:30].ljust(30)

            print("Label: '" + label + "'")
            print("Label length: " + str(len(label)))

    except ValueError:
        print("Error: price must be a valid number")

#-------------------------------------------------------------#
#   CONCLUSIONES
#-------------------------------------------------------------#


"""
El manejo de strings en Python es importante porque permite recibir, procesar y mostrar información de manera correcta
métodos como lower(), strip(), split() y join() ayudan a limpiar y organizar el texto según lo que necesitemos
normalizar el texto antes de compararlo evita errores causados por mayúsculas o espacios innecesarios
las validaciones permiten detectar datos incorrectos y evitar que el programa trabaje con información inválida
también aprendí que los strings son inmutables, por lo que sus caracteres no se pueden modificar directamente
por otra parte, los slices permiten extraer partes de una cadena usando posiciones específicas
estas herramientas ayudan a crear programas más ordenados, confiables y fáciles de utilizar.

"""
#-------------------------------------------------------------#
#     REFERENCIAS
#-------------------------------------------------------------#

"""
References:
1)https://www.youtube.com/watch?v=8tuyYql2duA
2)https://www.youtube.com/watch?v=66myIII2sY0&pp=ygUJLnNwbGl0IHB5
3)https://ellibrodepython.com/cadenas-python
4)https://ellibrodepython.com/mutabilidad-python
5)https://www.freecodecamp.org/espanol/news/sentencias-if-elif-y-else-en-python/

"""