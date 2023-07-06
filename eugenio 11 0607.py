# CSV comma separated value
import csv

data = [{
    'Lastname': 'Smith',
    ' firstname': 'Peter',
    'class_number': 9,
    'class_letter': 'A'
}, {
    'Lastname': 'Piccolo',
    ' firstname': 'Alex',
    'class_number': 9,
    'class_letter': 'B'

}]

# with open('form.csv', 'w', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=list(data[0].keys()), delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
#     writer.writeheader()
#     for item in data:
#         writer.writerow(item)


with open('form.csv', 'r', newline='') as f:
    reader = csv.DictReader(f, fieldnames=list(data[0].keys()), delimiter=';', quoting=csv.QUOTE_NONNUMERIC)


    for item in reader:
        for k, v, in item.items():
          print(k, v)