def converter_para_segundos(h, min, s):
    s_final = 0
    s_final += h * 3600
    s_final += min * 60
    s_final += s
    return s_final
    

h = int(input("Insira o valor correspondente ao número de horas (h): "))
min = int(input("Insira o valor correspondente ao número de minutos (min): "))
s = int(input("Insira o valor correspondente ao número de segundos (s): "))

print(f"Total em segundos: {converter_para_segundos(h, min, s)}s")