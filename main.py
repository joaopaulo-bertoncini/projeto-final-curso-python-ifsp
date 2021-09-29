# Aluno: João Paulo Scarebelo Bertoncini
# E-Mail: joao.bertoncini@gmail.com
# Github: plugns
import os


def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')


def menu():
    while True:
        print('''
            MENU:

            [C] - Cadastrar Notas
            [R] - Relatórios
            [S] - Sair
        ''')
        choice = str(input('Escolha uma opção: ')).upper()
        if choice == 'C':
            cadastrar()
        elif choice == 'S':
            exit(0)


def cadastrar():
    #screen_clear()
    name = ''
    while name == "":
        name = str(input('Entre com o nome do aluno: ')).upper()
        if name == "":
            print("Error: Favor digitar o nome do aluno")
    sex = ""
    while sex != "F" and sex != "M":
        sex = str(input('Entre com o sexo do aluno: F ou M ')).upper()
        if sex != "F" and sex != "M":
            print("Error: Favor digitar o sexo do aluno")

    return

if __name__ == '__main__':
    print('Sistema de Notas v1.0')
    menu()


