# Exercício 1.1

##### 1 - Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?	
```

>>>print 'hello' 
  File "<python-input-15>", line 1
    print 'hello'
    ^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```
##### 2 - Se estiver tentando imprimir uma string, o que acontece se omitir uma das aspas ou ambas?
```
>>> print('hello)
  File "<python-input-16>", line 1
    print('hello)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```
##### 3 - Você pode usar um sinal de menos para fazer um número negativo como -2. O que acontece se puser um sinal de mais antes de um número? E se escrever assim: 2++2?
```
>>> 2++2
4

Temos a soma dos numeros como se fosse apenas 1 sinal de +
```
##### 4 - Na notação matemática, zeros à esquerda são aceitáveis, como em 02. O que acontece se você tentar usar isso no Python?
```
>>> 02
  File "<python-input-19>", line 1
    02
    ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
```
##### 5 - O que acontece se você tiver dois valores sem nenhum operador entre eles?
```
>>> 02
  File "<python-input-19>", line 1
    02
    ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> 2 2
  File "<python-input-20>", line 1
    2 2
      ^
SyntaxError: invalid syntax
>>> 22
22
>>> print(2 2)
  File "<python-input-22>", line 1
    print(2 2)
          ^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

# Exercício 1.2
Inicialize o interpretador do Python e use-o como uma calculadora.

##### 1 - Quantos segundos há em 42 minutos e 42 segundos?
```
>>> (42*60)+42
2562
```
##### 2 - Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.
```
>>> 10/1.61
6.211180124223602
```
##### 3  -Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? 
```
 1 - Descobrir quantos segundos por 1 milha 
>>> 2562/6.21
412.56038647342996
 2 - 1 milha são quantos minutos?
>>> 412.56/60
6.876 
Pegando a casa decimal, conseguimos saber quantos segundos são 0.876
>>> 0.876*60
52.56

Então são 6 minutos e 52 segundos por milha

```
##### 4 - Qual é a sua velocidade média em milhas por hora?
```
Aqui pegamos o valor de milhas por segundo depois converter em horas 
>>> 6.21/2562 # milhas por segundo
0.002423887587822014
>>> 0.002423*3600 # Milhas por hora
8.7228
```