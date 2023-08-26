print("JUEGO DE PIEDRA, PAPEL o TIJERA")
participante = input("Hola, ¿como te llamas? ")
name = participante.title()
print("Hola",name,", juguemos. \nEl que gane 3 veces sera el CAMPEÓN\nEstas son las alternativas:")
print("-piedra \n-papel \n-tijera")

computadora = 0
usuario = 0

while True:

    seleccione = input(name + " Escribe la alternativa que seleccionaste: ")
    alternativa = seleccione.lower()

    tipo = ("piedra", "papel", "tijera")
    import random
    num_computer = random.choice(tipo)
    print("La computadora selecciono la alternativa:", num_computer)

    if alternativa == "piedra" and num_computer == "papel":
        print("papel gana a piedra, Tu pierdes")
        computadora += 1
        print("Resultado => computadora:" ,computadora, "usuario:", usuario)
    elif alternativa == "piedra" and num_computer == "tijera":
        print("piedra gana a tijera, ¡¡Ganaste!!")
        usuario += 1
        print("Resultado => computadora:" ,computadora, "usuario:", usuario)
    elif alternativa == "papel" and num_computer == "piedra":
        print("papel gana a piedra, ¡¡Ganaste!!")
        usuario += 1
        print("Resultado => computadora:" ,computadora, "usuario:", usuario)
    elif alternativa == "papel" and num_computer == "tijera":
        print("tijera gana a papel, Tu pierdes")
        computadora += 1
        print("Resultado => computadora:" ,computadora, "usuario:", usuario)
    elif alternativa == "tijera" and num_computer == "piedra":
        print("piedra gana a tijera, Tu pierdes")
        computadora += 1
        print("Resultado => computadora:" ,computadora, "usuario:", usuario)
    elif alternativa == "tijera" and num_computer == "papel":
        print("tijera gana a papel, ¡¡Ganaste!!")
        usuario += 1
        print("Resultado => computadora:" ,computadora, "usuario:", usuario)
    elif alternativa == num_computer:
        print("La computadora y tu seleccionaron la misma alternativa, EMPATE!!")
    else:
        print("Usted no selecciono una alternativa adecuada, intentelo otra vez")

    if computadora == 3:
        print("oww lo siento, el ganador final es la computaora \nGAME OVER! ")
        print("──────▄▀▄─────▄▀▄")
        print("─────▄█░░▀▀▀▀▀░░█▄")
        print("─▄▄──█░░░░░░░░░░░█──▄▄")
        print("█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█")
        break

    if usuario == 3:
        print("El ganador final eres tu. \n¡¡GANASTE!! ")
        print("░░░░░░░░░░░░░░░░░░░░░░█████████░░░░░░░░░")
        print("░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███░░░░░░░")
        print("░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███░░░░")
        print("░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░")
        print("░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███░")
        print("░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██")
        print("░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
        print("░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██")
        print("░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██")
        print("██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██")
        print("█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██")
        print("██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░")
        print("░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░")
        print("░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░")
        print("░░████████████░░░█████████████████░░░░░░")
        print("Eres el Mejor!!")
        break