r = int(input())
g = int(input())
b = int(input())

if r > g and r > b:
    print('На космических мышей нападают коты.')
elif g > b:
    print('На инопланетных котов нападают космические мыши.')
else:
    print('Ошибочный сигнал.')
