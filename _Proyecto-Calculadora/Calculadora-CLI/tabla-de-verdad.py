# -*- coding: utf-8 -*-
"""
Programa básico de tablas de verdad.

Permite visualizar las tablas de verdad de los conectivos lógicos:
- Negación (~)
- Conjunción (AND)
- Disyunción (OR)
- Bicondicional (IFF)
"""

from itertools import product
import os


# Constantes para representar los valores de verdad
VERDADERO = True
FALSO = False


def limpiar_pantalla():
    """Limpia la consola/terminal según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')


def tablero_negacion():
    """
    Muestra la tabla de verdad de la negación.
    La negación invierte el valor de verdad: ~V = F, ~F = V.
    """
    print("=" * 35)
    print("TABLA DE VERDAD - NEGACIÓN (~p)")
    print("=" * 35)
    print(f"{'p':^5} | {'~p':^5}")
    print("-" * 13)

    for p in (VERDADERO, FALSO):
        resultado = not p
        p_texto = "V" if p else "F"
        resultado_texto = "V" if resultado else "F"
        print(f"{p_texto:^5} | {resultado_texto:^5}")

    print()


def tablero_conjuncion():
    """
    Muestra la tabla de verdad de la conjunción.
    La conjunción es verdadera solo si ambos operandos son verdaderos: p AND q.
    """
    print("=" * 35)
    print("TABLA DE VERDAD - CONJUNCIÓN (p AND q)")
    print("=" * 35)
    print(f"{'p':^5} | {'q':^5} | {'p AND q':^9}")
    print("-" * 19)

    for p, q in product((VERDADERO, FALSO), repeat=2):
        resultado = p and q
        p_texto = "V" if p else "F"
        q_texto = "V" if q else "F"
        resultado_texto = "V" if resultado else "F"
        print(f"{p_texto:^5} | {q_texto:^5} | {resultado_texto:^7}")

    print()


def tablero_disyuncion():
    """
    Muestra la tabla de verdad de la disyunción.
    La disyunción es falsa solo si ambos operandos son falsos: p OR q.
    """
    print("=" * 35)
    print("TABLA DE VERDAD - DISYUNCIÓN (p OR q)")
    print("=" * 35)
    print(f"{'p':^5} | {'q':^5} | {'p OR q':^8}")
    print("-" * 19)

    for p, q in product((VERDADERO, FALSO), repeat=2):
        resultado = p or q
        p_texto = "V" if p else "F"
        q_texto = "V" if q else "F"
        resultado_texto = "V" if resultado else "F"
        print(f"{p_texto:^5} | {q_texto:^5} | {resultado_texto:^7}")

    print()


def tablero_bicondicional():
    """
    Muestra la tabla de verdad del bicondicional.
    El bicondicional es verdadero cuando ambos operandos tienen el mismo
    valor de verdad: p IFF q.
    """
    print("=" * 35)
    print("TABLA DE VERDAD - BICONDICIONAL (p IFF q)")
    print("=" * 35)
    print(f"{'p':^5} | {'q':^5} | {'p IFF q':^9}")
    print("-" * 19)

    for p, q in product((VERDADERO, FALSO), repeat=2):
        resultado = (p == q)
        p_texto = "V" if p else "F"
        q_texto = "V" if q else "F"
        resultado_texto = "V" if resultado else "F"
        print(f"{p_texto:^5} | {q_texto:^5} | {resultado_texto:^7}")

    print()


def mostrar_menu():
    """
    Muestra el menú principal del programa y devuelve la opción elegida.
    """
    print("=" * 40)
    print("   PROGRAMA DE TABLAS DE VERDAD")
    print("=" * 40)
    print("1. Negación (~p)")
    print("2. Conjunción (p AND q)")
    print("3. Disyunción (p OR q)")
    print("4. Bicondicional (p IFF q)")
    print("5. Mostrar todas las tablas")
    print("0. Salir")
    print("=" * 40)
    return input("Seleccione una opción: ")


def main():
    """
    Función principal que controla la ejecución del programa.
    """
    while True:
        opcion = mostrar_menu()
        limpiar_pantalla()

        if opcion == "1":
            tablero_negacion()
        elif opcion == "2":
            tablero_conjuncion()
        elif opcion == "3":
            tablero_disyuncion()
        elif opcion == "4":
            tablero_bicondicional()
        elif opcion == "5":
            tablero_negacion()
            tablero_conjuncion()
            tablero_disyuncion()
            tablero_bicondicional()
        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
