def converter_para_hora_minuto_e_segundo(s):
    min = 0
    h = 0
    if s >= 60:
        min = s//60
        s = s % 60
        if min >= 60:
            h = min//60
            min = min % 60
    return h, min, s

s = int(input("Insira o valor total em segundos (s): "))

total = converter_para_hora_minuto_e_segundo(s)

print(f"{s}s = {total[0]}h {total[1]}min {total[2]}s")