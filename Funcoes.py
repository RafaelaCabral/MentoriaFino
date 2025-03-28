## Função para saber se o quadrilatero é um quadrado
def quadrilatero_quadrado(base, altura):
    if base == altura:
        print("É um quadrado")
    else:
        print("Não é um quadrado")

quadrilatero_quadrado(3, 4)  # Saída: Não é um quadrado
quadrilatero_quadrado(5, 5)  # Saída: É um quadrado


## Função para saber se a área do quadrilatero
def quadrilatero_area(base,altura):
    area= base*altura
    print(f"A área do quadrilatero é:{area}")

quadrilatero_area(2,3)

## Função para saber se o perímetro do quadrilatero
def quadrilatero_perimetro(base,altura):
    perimetro= (base*2) + (altura*2)
    print(f"O perímetro do quadrilatero é:{perimetro}")

quadrilatero_perimetro(2,3)

## Função para saber se o área do triangulo
def triangulo_area(base,altura):
    area= (base*altura)/2
    print(f"A área do triangulo é:{area}")

triangulo_area(8,3)

## Função para saber se o perímetro do triangulo
def triangulo_perimetro(lado1,lado2, lado3):
    perimetro = lado1 + lado2 + lado3
    print(f"O perímetro do quadrilatero é:{perimetro}")

triangulo_perimetro(8,3,9)