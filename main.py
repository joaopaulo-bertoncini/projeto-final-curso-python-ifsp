#-------------------------------------------------------
# Aluno: João Paulo Scarebelo Bertoncini
# E-Mail: joao.bertoncini@gmail.com
# Github: plugns
#-------------------------------------------------------
# Como executar:
# Instalando as dependencias
# pip install tabulate
# pip install names
# pip install random
# python3 main.py
#-------------------------------------------------------
import os
from tabulate import tabulate
# usado gerar dados de teste (mock) 
import names
import random

students = []


def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def situation(average):
    if average >= 7:
        return 'Aprovado'
    elif 4 <= average < 7:
        return 'Exame'
    elif average < 4:
        return 'Reprovado'


def menu():
    while True:
        screen_clear()
        print('''Sistema de Notas v1.0''')
        print('''
            MENU:
            [C] - CADASTRAR NOTAS
            [L] - LISTAR NOTAS
            [R] - RELATÓRIOS
            [S] - SAIR
        ''')
        choice = str(input('Escolha uma opção: ')).upper()
        if choice == 'C':
            register()
        elif choice == 'L':
            list()
        elif choice == 'R':
            report()
        elif choice == 'S':
            exit(0)


def register():
    screen_clear()
    while True:
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

        average = round((grade1 + grade2 + grade3) / 3, 2)
        students.append({
            'name': name,
            'sex': sex,
            'grade1': grade1,
            'grade2': grade2,
            'grade3': grade3,
            'average': average
        })
        print('\n')
        print('-----------------------------Resumo do Cadastro------------------------------')
        print(tabulate([[
            name,
            'Masculino' if sex == 'M' else 'Feminino',
            grade1,
            grade2,
            grade3,
            average,
            situation(average)
            ]], headers=['Nome', 'Sexo', 'Nota 1', 'Nota 2', 'Nota 3', 'Média', 'Status']))
        print('----------------------------------------------------------------------------')
        result = ''
        while result != "S" and result != "N":
            result = str(input('Cadastrar outro aluno(a) (S ou N): ')).upper()
        if result == 'N':
            break
    return

def list():
    screen_clear()
    print('-----------------------------Resumo do Cadastro------------------------------')
    list = []
    for student in students:
        s = situation(student['average'])
        list.append([
            student['name'],
            'Masculino' if student['sex'] == 'M' else 'Feminino',
            student['grade1'],
            student['grade2'],
            student['grade3'],
            student['average'],
            s
        ])
    print(tabulate(list, headers=['Nome', 'Sexo', 'Nota 1', 'Nota 2', 'Nota 3', 'Média', 'Status']))
    print('----------------------------------------------------------------------------')
    input('Pressione enter para continuar ')
    return


def report():
    screen_clear()
    total_students = len(students)
    total_students_approved = 0
    total_students_exam = 0
    total_students_failed = 0
    total_female_approved = 0
    total_female_exam = 0
    total_female_failed = 0
    total_male_approved = 0
    total_male_exam = 0
    total_male_failed = 0   
    for student in students:
        if student['average'] >= 7:
            total_students_approved += 1
            if student['sex'] == 'F':
                total_female_approved += 1
            elif student['sex'] == 'M':
                total_male_approved += 1
        elif 4 <= student['average'] < 7:
            total_students_exam += 1
            if student['sex'] == 'F':
                total_female_exam += 1
            elif student['sex'] == 'M':
                total_male_exam += 1           
        elif student['average'] < 4:
            total_students_failed += 1
            if student['sex'] == 'F':
                total_female_failed += 1
            elif student['sex'] == 'M':
                total_male_failed += 1   

    if total_students_approved > 0:
        percentage_approved = round((total_students_approved * 100) / total_students,2)
    else:
        percentage_approved = 0
    if total_students_exam > 0:
        percentage_exam = round((total_students_exam * 100) / total_students,2)
    else:
        percentage_exam = 0
    if total_students_failed > 0:
        percentage_failed = round((total_students_failed * 100) / total_students,2)
    else:
        percentage_failed = 0
    print('-----------------------------------------------------------------------------')
    print('TOTAL DE ALUNOS CADASTRADOS: %d' % total_students)
    print('\n')
    print('QUANTIDADE PORCENTUAL DE ALUNOS APROVADOS: ' + '{:.2f}'.format(percentage_approved) + '%')
    print('QUANTIDADE PORCENTUAL DE ALUNOS DE EXAME: ' + '{:.2f}'.format(percentage_exam) + '%')
    print('QUANTIDADE PORCENTUAL DE ALUNOS REPROVADOS: ' + '{:.2f}'.format(percentage_failed) + '%')
    print('\n')
    print('QUANTIDADE DE PESSOAS DO SEXO FEMININO APROVADAS: ' + '{}'.format(total_female_approved))
    print('QUANTIDADE DE PESSOAS DO SEXO MASCULINO APROVADAS: ' + '{}'.format(total_male_approved))
    print('QUANTIDADE DE PESSOAS DO SEXO FEMININO DE EXAME: ' + '{}'.format(total_female_exam))
    print('QUANTIDADE DE PESSOAS DO SEXO MASCULINO DE EXAME: ' + '{}'.format(total_male_exam))
    print('QUANTIDADE DE PESSOAS DO SEXO FEMININO REPROVADAS: ' + '{}'.format(total_female_failed))
    print('QUANTIDADE DE PESSOAS DO SEXO MASCULINO RESPROVADAS: ' + '{}'.format(total_male_failed))
    print('----------------------------------------------------------------------------')
    input('Pressione enter para continuar ')
    return

def gen_students():
    for i in range(15):
        grade1 = random.randint(0,10)
        grade2 = random.randint(0,10)
        grade3 = random.randint(0,10)   
        average = round((grade1 + grade2 + grade3) / 3, 2)
        students.append({
            'name': names.get_full_name(gender='female'),
            'sex': 'F',
            'grade1': grade1,
            'grade2': grade2,
            'grade3': grade3,
            'average': average
        })

    for i in range(10):
        grade1 = random.randint(0,10)
        grade2 = random.randint(0,10)
        grade3 = random.randint(0,10)   
        average = round((grade1 + grade2 + grade3) / 3, 2)
        students.append({
            'name': names.get_full_name(gender='male'),
            'sex': 'M',
            'grade1': grade1,
            'grade2': grade2,
            'grade3': grade3,
            'average': average
        })


if __name__ == '__main__':
    # mock para gerar dados
    # gen_students()
    menu()
