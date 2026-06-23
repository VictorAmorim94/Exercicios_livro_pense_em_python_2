#function exercicio 1 
def right_justify(s: str):
    tam_string = len(s)
    qtd_espacos = 70 - int(tam_string)
    print(' '*qtd_espacos + s)

####right_justify('testando')


#Funcion exercicio 2 
def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_twice(f,x):
    f(x)


def print_spam(y):
    print(y)


def do_four(f,valor):
    f(valor)
    f(valor)


####do_four(print_twice,'spam')

# Function exercicio 3
def linha_horizontal():
    print('+ - - - - + - - - - +')


def linha_vertical():
    print('|         |         |')

def desenhar_vertical():
    linha_vertical()
    linha_vertical()
    linha_vertical()
    linha_vertical()

def desenhar_grade():
    linha_horizontal()
    desenhar_vertical()
    linha_horizontal()
    desenhar_vertical()
    linha_horizontal()

desenhar_grade()