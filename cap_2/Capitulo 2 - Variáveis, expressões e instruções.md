# Capitulo 2 

## Exercício 2.1

1 - Vimos que n = 42 é legal. E 42 = n?
```
>>> 42 = n
  File "<stdin>", line 1
    42 = n
    ^^
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
```

2 - Ou x = y = 1?
```
>>> x = y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    x = y
        ^
NameError: name 'y' is not defined
>>> x = y = 1
>>> x 
1
>>> y
1
```

3 - Em algumas linguagens, cada instrução termina em um ponto e vírgula ;. O que acontece se você puser um ponto e vírgula no fim de uma instrução no Python?

R: Executa normalmente, o python aceita o ; no final da linha 
```
>>> x + 1;
2
```

4 - E se puser um ponto no fim de uma instrução?

R: Ele da erro de sintaxe, ele não entende 
```
>>> print(x).
  File "<stdin>", line 1
    print(x).
             ^
SyntaxError: invalid syntax
```

5 - Em notação matemática é possível multiplicar x e y desta forma: xy. O que acontece se você tentar fazer o mesmo no Python?
```
>>> x * y 
10
>>> xy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    xy
NameError: name 'xy' is not defined
```

## Exercício 2.2
Pratique o uso do interpretador do Python como uma calculadora:

1 - O volume de uma esfera com raio r é 
```math
\frac{4}{3} \pi r^3
```  
Volume de uma esfera.. Qual é o volume de uma esfera com raio 5?
```
a fórmula é (4/3) * pi * r ^3  e vou usar pi = 3,14

>>> r = 5
>>> pi = 3.14
>>> r^3
6
>>> r**3
125
>>> 4/3
1.3333333333333333
>>> j = 4/3
>>> j * pi
4.1866666666666665
>>> j = j*pi
>>> i = r**3
>>> print(j*i
... )
523.3333333333334
```

2 - Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?
```
>>> capa_de_livro = 24.95 # valor de capa
>>> desconto_livraria = 0.40 
>>> transporte = 3 #transporte do primeiro livro
>>> transporte_exemplar = 0.75 # transporte dos outros exemplares fora o primeiro
>>> qtd_livros = 60 
>>> 
>>> primeiro_livros = (capa_de_livro-(capa_de_livro * desconto_livraria))+transporte 
>>> primeiro_livros
17.97
>>> livros = ((capa_de_livro-(capa_de_livro * desconto_livraria))+transporte_exemplar)* (qtd_livros - 1) + primeiro_livros
>>> livros
945.4499999999999
```

3 - Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?
[!script] (./script/cap2 - exercicios.py)