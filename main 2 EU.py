import random as r


# r_string = 'dddbhhgffeefef45'
# lst = list(r_string) # строку превращаем в список
# r.shuffle(lst) # замешиваем наш список
# temp = lst[:8]  # забираем из списка 8 значений
# print(lst)
# if '@' in temp: # смотрим, есть ли такие знаки в списке
#      print(*temp, sep='')   # программа выбор случайного пароля работает
# else:
#      temp.append('@')
#      print(*temp, sep='')

# a={1,2,3,4}
# b={2,3,5,7,11}
#
# string = 'телевидение'
# st= set(string)
# print(*st,sep='-') # sep - команда,которая задает вид пробела в списке
# print(a.union(b)) # обьединение множеств
# print(a.intersection(b)) # пересечение - ищет одинаковые
# print(a.difference(b)) # разность - ищет разные значения в списках
# print(a.symmetric_difference(b)) # симметричная разность элементы входящие и в а и в б

# a = 1.1 # это оформление кортежа


# lst={2,3,5,7,11}
#
# # for i,v in enumerate(lst):
# #      print('индекс', i, 'значение',v ) # работает программа присвоения индекса элементам
#
# d = {'Дмитриев': 'плотник',               # словарь, обращение по ключу
#      'Иванов': 'программист',
#      'Hetrov': 'удожник' }
# print(d['Иванов'])                         # аботает
#
# d['Никитин'] = 'Сисадмин'
# print(d['Никитин'])
# for k, v in  d.items():     # для каждого элемента в списке-словаре d

  #   print(k, '->', v)



# source = 'город рим'  # задача - превратить в миргород, а потом в дорог город миргород
# lst =source.split()
# print(lst)
# print(lst[0][::-1] +lst[0]) # программа напечала миргород
# print(lst[1][::-1] +lst[0])
# x1=(lst[0][::-1] +lst[0])
# x2=(lst[1][::-1] +lst[0])
# name = x1+x2
# print(name)  # работает






# phone ='+7-812-345-67-89'
#
# print ('исходная строка :' , phone)   # исходная строка : +7-812-345-67-89
# spacedphone = phone.replace('-','')
# print (spacedphone)  # с пом replace заменили пробелы в номере на без пробелов +78123456789
# temp = phone.replace('-','(', 1)
# print(temp)
#
# ku = 'тиливизор'
# b = ku.replace('и','е', 2)
#  print(b)







# name = 'victor'
# age = 99
#
#
#
# height = 180
#
#
#  # вариант с форматированной строкой
# f_string = f'Имя:{name},возраст: {age} лет, рост: {height},cm'
# print(f_string)  #  Имя:victor,возраст: 99 лет, рост: 180
#
#
#
#
# # списочные выражения записываются прямо а квадратные скобки
# a= [i for i in range(101) if i % 10 == 5]
# print(a)   # [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]










from PIL import Image
from PIL import ImageDraw
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# блок констант
YELLOW = (255,255, 0)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)

W,H = (10,10) # скобки здесь не обязательны
RW = 50
RN = 50
required_height = 100
ratio = W/H
original = Image.open('python.png')
resized = original.resize((int(required_height*ratio),required_height))
resized.save('resized.png')
cropped_image = original.crop((300, 0, 600, 200))
cropped_image.save('cropped.png')
pixels = original.load()
for x in range(W):
    for y in range(H):
        r, g, b = pixels[x,y]
        pixels[x,y] = g, b, r
        original.save(' inverted.png')
        


TEXT= 'PYTHON'
canvas = Image.new("RGB", (W, H), BLACK) # СТРОКА, СОЗДАЮШАЯ ФОН
draw = ImageDraw.Draw(canvas)

draw.text((10,10,), TEXT)
draw.polygon((W//2, 0,0, H,W,H), fill = WHITE, outline=YELLOW)
draw.arc(xy=(50,25,175,200 ), start=0, end=360, fill=BLUE, width=10)
draw.rectangle((0,0,50,50), fill=RED)
draw.rectangle((75,75,125,125), fill=GREEN)  # зеленый квадрат  (x,y,W,H) - вводим координаты
draw.rectangle((0,0,50,50), fill=BLUE)


draw.line((0, 50, W, H ), fill = YELLOW, width=5)
canvas.save('image.png',  'PNG')


 # ВСТРОИЛИ 3 ШАРА
draw.ellipse((0,0,50,50), fill=RED)
draw.ellipse((75,75,125,125), fill=BLUE)
draw.ellipse((150,150,200,200), fill=YELLOW)
draw.line((0, 0, W, H ), fill = YELLOW, width=5)
canvas.save('image.png',  'PNG')


fffff















