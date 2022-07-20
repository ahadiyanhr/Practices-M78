file = input("Enter the name of text file: ")
ph1 = input("Enter the 1st word/phrases: ")
ph2 = input("Enter the 2nd word/phrases: ")


with open(file, 'r') as f:
    list1 = f.readlines()

list2 = []

for item in list1:
    if ph1 in item:
        item = item.replace(ph1,ph2)
    list2.append(item)

with open(file, 'w') as f:
    f.writelines(list2)
    list1 = list2

print(list1)
