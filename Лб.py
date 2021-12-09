from prettytable import PrettyTable

def read_table(path):
    file = open(path, 'r', encoding = 'utf-8')
    data = file.read()
    file.close()
    
    arr = data.split('\n')
    for i in range(len(arr)):
        arr[i] = arr[i].split(';')
    return arr

def write_file(s, path):
    file = open(path, 'w', encoding = 'utf-8')
    file.write(s)
    file.close()

table1 = read_table('tab1.txt') 
table2 = read_table('tab2.txt')

f1 = PrettyTable(['Код банку','курс на 1,10$','курс на 1,11$','курс на 1,12$','курс на 1,10м','курс на 1,11м','курс на 1,12м','Рік'])
f1.add_rows(table1)

f2 = PrettyTable(['Код банку','Найменування банку'])
f2.add_rows(table2)

print(f1)
print('\n')
print(f2)

table3 = []

for row1 in table1:
    for row2 in table2:
        if row1[0] == row2[0]:
            table3.append([row1[0], row2[1], row1[7]])

f3 = PrettyTable(['Код банку','Найменування банку','Рік','курс на 1,10 США','курс на 1,11 США','курс на 1,12 США','курс на 1,10 ФРН','курс на 1,11 ФРН','курс на 1,12 ФРН'])
f3.add_rows(table3)

write_file(f3.get_string(), 'tab3.txt')
write_file(str(table3).replace('\'', '\"'), 'Аналіз рівня зміни курсу обміну валют.json')