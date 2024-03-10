#from my_sel import *

print('Выберите режим использования:')
print('Одиночный - S')
print('Многопоточный - M')
ver = input("Выбранный режим: ")

proxys = [
    '6NeZMV: i5xcP9mEj0@185.181.244.91 :5501',
]

if (ver == "S" or ver == "s"):
    proxy = input('Введите прокси: ')
    i = input('Введите номер хоста: ')
 #   single(proxy, i)


elif (ver == "M" or ver == "m"):
    a = input("Введите кол-во сессий: ")
    k = a
  #  multi(a, k, proxys)






