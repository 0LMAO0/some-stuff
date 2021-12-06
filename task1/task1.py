def analyse(programm: list[tuple[str, int]]) -> int:
    cnt = 0
    srtd_prog = sorted(programm, key= lambda package: package[1])
    for i in range(0, len(srtd_prog)-1):
        for j in range(len(srtd_prog)-1):
            if (srtd_prog[j][0] == srtd_prog[j+1][0])\
            or (srtd_prog[j-1][1] == srtd_prog[j+1][1]):
                c = srtd_prog[j]
                srtd_prog[j] = srtd_prog[j+1]
                srtd_prog[j+1] = c
            
    for i in range(0,len(srtd_prog)-1):
        for j in range(len(srtd_prog)-1):
            if srtd_prog[j][0] == srtd_prog[j+1][0] and \
                srtd_prog[j][1] > srtd_prog[j+1][1]:
                c = srtd_prog[j+1]
                srtd_prog[j+1] = srtd_prog[j]
                srtd_prog[j] = c

    for i in range(len(srtd_prog)):
        if srtd_prog[i][0] == "принять":
            cnt += 1
        elif srtd_prog[i][0] == "выгрузить":
            if srtd_prog[i][1] == srtd_prog[i-1][1]:
                cnt +=1           
    return cnt
            


        


args = []
energy = 0
while True:
    print("Чтобы прекратить ввод значений, введите -1\n")
    some_str = str(input("Введите команду поступления/выдачи:   "))
    val = int(input("Введите номер ящика:   "))
    if val == -1 or some_str == '-1':
        break
    args.append((some_str, val))
energy = analyse(args)


print(energy)