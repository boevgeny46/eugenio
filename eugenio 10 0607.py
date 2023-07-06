# CSV comma separated value
import csv

# goods, price
goods = [('carpet', 5000 ),('iron', 3500),('penal', 1200)]


with open('sq.csv','w', newline='', encoding='utf-8') as f:
     # reader = csv.reader(f,delimiter=';', quotechar='"')


     writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

     for i in goods:
        writer.writerow(i)
        print(i)



# # здесь в команде open мы создали в нашем проекте файл sq.csv
# # и  пположили в него наши три элемента