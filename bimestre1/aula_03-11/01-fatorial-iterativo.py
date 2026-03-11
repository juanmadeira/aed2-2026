def fatorial(n):
    a = n - 1
    result = 0
    while a >= 1:
        if a == (n - 1):
            result += n * a
        else:
            result = result * a
        print(result, n, a)
        a -= 1
    return result

print(fatorial(int(input("Insira um número para calcular seu fatorial: "))))