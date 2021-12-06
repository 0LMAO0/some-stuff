def calculate(m:int, n:int, p:list[int]):
    a=[int(elem) for elem in p.split()]
    x=0
    b=[-1 for i in range(1002)]
    s=[-1 for i in range(1002)]
    s[0]=0
    for i in range(0,n):
        for j in range(0,m):
            if s[j]==-1: continue
            d=a[j%m]
            if b[0]<s[j]:
                b[0]=s[j]
            if b[(j+1)%m]<=s[j]+d:
                b[(j+1)%m]=s[j]+d
        s=b[:]
    for j in range(m):
        x=max(s[j],x)
    return x

def main():
    print('Введите m и n через SPACE и нажмите Enter.\n')
    m,n=[int(elem) for elem in input().split()]
    print('Введите элементы p через SPACE и нажмите Enter.\n')
    p=str(input())+' '
    x = calculate(m,n,p)
    print('Вывод:\n')
    print(x)
    return 0
main()    