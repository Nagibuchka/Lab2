import math
def create_mass():
    a = float(input('ВВедіть початок діапазону'))
    b = float(input('ВВедіть кінець діапазону'))
    h = float(input('Введіть крок розрахунку'))
    k = 0
    t = a
    m = []
    xx = []
    while(t<=b):
        if t <=0:
            m.append(math.sin(t) * math.sin(t) - math.cos(t))
        else:
            m.append(math.cos(2 * t) * math.cos(2 * t) * math.cos(2 * t) + math.sin(2 * t ** 2))
        k += 1
        xx.append(t)
        t += h
    return  m,xx,k
def print_mass(xx,m,k):
    for i in range(0,k):
        print(xx[i],'',m[i])

def found_min(m,k):
    imin = 0
    for i in range(0,k):
        if m[i] < m[imin]:
            imin = i
    print('Мінімальній елемент =', m[imin], 'Його номер =',imin + 1)
    return imin

def found_max(m,k):
    imax = 0
    for i in range(0,k):
        if m[i] > m[imax]:
            imax = i
    print('Максимальній елемент =', m[imax], 'Його номер =',imax + 1)
    return imax

def summ(m,a,b):
    if b < a:
        k = a
        a = b
        b = k
    summa = 0
    for i in range(a + 1, b):
        summa += m[i]
    print('Сума елементів, розташована між мінімальним та максимальним елементом =',summa)

y = []
x = []
x,y,n = create_mass()
print_mass(x,y,n)
imn = found_min(y,n)
imx = found_max(y,n)
summ(y,imn,imx)

print(--------HELLO--------)