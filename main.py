# Aluno: João Paulo Scarebelo Bertoncini
# E-Mail: joao.bertoncini@gmail.com
# Github: plugns
import os

students = []


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
            register()
        elif choice == 'S':
            exit(0)


def register():
    # screen_clear()
    name = ''
    while name == "":
        name = str(input('Entre com o nome do aluno(a): ')).upper()
        if name == "":
            print("Error: Favor digitar o nome do aluno(a)!")
    sex = ""
    while sex != "F" and sex != "M":
        sex = str(input('Entre com o sexo do aluno(a) (F ou M): ')).upper()
        if sex != "F" and sex != "M":
            print("Error: Favor digitar o sexo do aluno(a)!")
    grade1 = -1
    while 0 > grade1 or 10 < grade1:
        try:
            grade1 = float(input('Entre com a nota 1 do aluno(a) (0 - 10): '))
        except ValueError:
            print("Error: Nota invalida!")
    grade2 = -1
    while 0 > grade2 or 10 < grade2:
        try:
            grade2 = float(input('Entre com a nota 2 do aluno(a) (0 - 10): '))
        except ValueError:
            print("Error: Nota invalida!")
    grade3 = -1
    while 0 > grade3 or 10 < grade3:
        try:
            grade3 = float(input('Entre com a nota 3 do aluno(a) (0 - 10): '))
        except ValueError:
            print("Error: Nota invalida!")

    average = (grade1 + grade2 + grade3) / 3
    students.append({
        'name': name,
        'sex': sex,
        'grade1': grade1,
        'grade2': grade2,
        'grade3': grade3,
        'average': average
    })
    print('-----Resumo do cadastro-----')
    print('Aluno: %s' % name)
    print('Masculino' if sex == 'M' else 'Feminino')
    print('Nota 1: %.2f' % grade3)
    print('Nota 2: %.2f' % grade2)
    print('Nota 2: %.2f' % grade2)
    print('---------------------------- \n')
    return

if __name__ == '__main__':
    print('Sistema de Notas v1.0')
    menu()
