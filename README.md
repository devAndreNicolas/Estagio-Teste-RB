Teste Estágio
Questão 1: O valor da Variável SOMA será 14, ou seja, SOMA = 0 + 14.

Questão 2:
#Primeiramente a sequência Fibonacci
def fibonacci(num):
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        while len(fib) < num:
            fib.append(fib[-1] + fib[-2])
        return fib
termo = int(input("Digite o termo desejado: "))
fibonacci_sequence = fibonacci(termo)
print(fibonacci_sequence)

#Analisar se o número solicitado está na sequência
def is_fibonacci(num):
    a = 0
    b = 1
    while b < num:
        a, b = b, a + b
    return b == num

numeroDoUsuario = int(input("Digite um número: "))
if is_fibonacci(numeroDoUsuario):
    print("O número pertence à sequência de Fibonacci!")
else:
    print("O número não pertence à sequência de Fibonacci.")

Questão 3:
A) 'N+2' (7+2=9)
B) 'N+N' (64+64=128, 128+128=256)
C) 'N+CrescenteDeNúmeroImpar' (47,60)
D) 'N+(SubtraçãoDoNúmeroPosteriorPeloAnterior+8)' (64+(28+8)=100, 100+(36+8)=144)
E) '+0,+1,+1,+2,+3,+4,+5' (12,17)
F) 'Não poderia acertar isto tentando sozinho, pois não há lógica matemática
na resolução, mas sei que é 200, 201 por ser uma charada famosa, a resposta tem que ser um número natural com D no início.' 

4) Antes da primeira ida eu deixaria ligado o interruptor 1 por um número de tempo suficiente
para esquentar uma lâmpada, e depois de desligá-lo, ligaria o interruptor 2 e agora sim iria para alguma sala.
Se a lâmpada estiver apagada mas quente seria do interruptor 1, Se ligada obviamente o interruptor 2, e se estivesse fria e apagada, o interruptor 3.
Na segunda ida trabalharia com a lógica "do que sobrou". Eu iria apenas ligar o interruptor que sobrou para garantir que ele fosse o responsável ou pela sala com a lâmpada apagada e fria ou pela sala com a lâmpada apagada e quente.

5) 

stringNormal = "Estágio"
stringInvertida = stringNormal[::-1]
print(stringInvertida) 
    
