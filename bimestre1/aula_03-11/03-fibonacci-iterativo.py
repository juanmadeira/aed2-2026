def fibonacci(n):
    fibo = [0, 1]
    a = 0
    b = 1
    while fibo[-1] < n:
        fibo.append(fibo[a] + fibo[b])
        a += 1
        b += 1
    fibo.pop()
    return fibo

print(fibonacci(int(input("Insira um limite (aberto) para a sequência de Fibonacci: "))))