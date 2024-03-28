#Questão 2:
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
    input()
else:
    print("O número não pertence à sequência de Fibonacci.")
    input()
