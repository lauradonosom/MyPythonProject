"""
match term:
    case pattern-1:
         action-1
    case pattern-2:
         action-2
    case pattern-3:
         action-3
    case _:
        action-default
"""

lenguaje = input("What's the programming language you want to learn? ")

match lenguaje:
    case "JavaScript":
        print("Puedes convertirte en web developer.")

    case "Python":
        print("Puedes convertirte en Data Scientist")

    case "PHP":
        print("Puedes convertirte en backend developer")

    case "Solidity":
        print("Puedes convertirte en Blockchain developer")

    case "Java":
        print("Puedes convertirte en mobile app developer")
    case _:
        print("El lenguaje no importa, lo que importa es la habilidad de resolver problemas.")

n