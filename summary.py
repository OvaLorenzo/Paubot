from datetime import datetime

path='path.py'
path2='path2.py'
path3='path3.py'

excersices = []
returnable = []

with open(path, 'r') as file:
    lista = file.readlines()
    for i in range(1, len(lista)):
        lista_split = lista[i].split(",")
        paste = {'slug': lista_split[3].replace("https://www.codewars.com/kata/", ""), 'due_date': lista_split[1],
                 'batch': lista_split[0]}
        excersices.append(paste)

with open(path2, 'r') as file2:
    lista2 = file2.readlines()
    control = False
    for j in range(len(excersices)):

        control = False
        returnable = []
        for i in range(1, len(lista2)):
            lista2_split = lista2[i].split(",")
            # print(excersices[j]['due_date'])
            # time2 = datetime.strptime(excersices[j]['due_date'], '%Y/%d/%m')

            if lista2_split[2] == excersices[j]['slug']:
                control = True
                returnable.append(excersices[j]['batch'])
                returnable.append(excersices[j]['slug'])
                returnable.append(True)
                returnable.append(lista2_split[4].replace("Z\n", "").replace("T", " "))

                time1 = datetime.strptime(lista2_split[4].replace("Z\n", "").replace("T", " "), '%Y-%m-%d %H:%M:%S')
                time2 = datetime.strptime(excersices[j]['due_date'] + " 00:00:00", '%Y/%m/%d %H:%M:%S')
                if (time1 <= time2):
                    returnable.append(False)
                else:
                    returnable.append(True)
                    total_late += 1
            with open(path3, 'a') as file3:
                file3.write(str(returnable) + "\n")

            print(returnable)

        # print(lista2_split[4].replace("Z\n", "").replace("T", " "))
        # print(time2)
    if control == False:
        returnable.append(excersices[j]['batch'])
        returnable.append(excersices[j]['slug'])
        returnable.append(False)
        returnable.append(None)
        returnable.append(False)
        with open(path3, 'a') as file3:
            file3.write(str(returnable) + "\n")
        print(returnable)
        print("\n")
    "# tareagrupal"


    import csv

    reader1 = csv.reader(open("path.py"), delimiter=',')  # ejercicios resueltos
    reader = csv.reader(open("path2.py"), delimiter=',')  # ejercicios totales
    data = []
    data1 = []
    sum = 0
    sum1 = 0
    total_late = 0
    # split_exercise =
    for row in reader:
        data.append(row)
        sum += 1

    for row in reader1:
        data1.append(row)
        sum1 += 1

    # for i in
    # total_late += 1
    print("Total exercises:", sum - 1)
    print("Total completed:", sum1 - 1)
    print("Total late:", total_late)
    print("Total missing:", (sum - 1) - (sum1 - 1))