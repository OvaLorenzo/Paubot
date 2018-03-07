    # validacion de la matricula, acepta 8 digitos y solo numeros
print('Whats your id?')
while True:
    id = input()
    if id.isnumeric() == False or len(id) != 8:
        print('invalid id')
    else:
        login = True
        #  el login = True es para utilizarlo como booleano en el codigo del bot, si es que se necesita.
        print('La matricula %s ha sido registrada' % (id))
        # el with open escribe la matricula introducida 1 sola ves, digase, si corremos el programa de nuevo y
        # introducimos otra matricula, solo aparecera la ultima matricula introducida
        with open('iddata.py', 'w') as file:
            file.write(id)
            break
while True:
    print('''
    eliga un comando
    b)Codewars
    c)Summary
    d)exit''')
    command = input()

    if command == 'codewars' or command == 'b':
            # aqui abajo  el codigo de todo el bot
            path = 'data ova.py'
            param = ('name', 'due_date', 'url')  # Información de cada ejercicio(nombre, fecha de entrega, link).
            batches = {

                'batch_number': [{'name': "", 'due_date': "", 'url': ""}]
                # Aquí van los diccionarios de cada batch, el código de abajo los irá agregando aquí.
            }
            with open(path, 'r') as file:
                lista = file.readlines()  # Files.readlines() devuelve una lista de strings, donde cada string es una línea del archivo.
                for i in range(1, len(lista)):  # Se itera desde 1 para no tomar el header del archivo.
                    lista_split = lista[i].split(
                        ",")  # Se guarda el contenido de una línea en una lista cada vez que se vea una coma.
                    # Ejemplo: 3,2018/02/21,Needle in the Haystack,https://www.codewars.com/kata/a-needle-in-the-haystack
                    # Se guarda como: ['3','2018/02/21','Needle in the Haystack','https://www.codewars.com/kata/a-needle-in-the-haystack']
                    string = "batch" + str(lista_split[0])  # Es un string que indicará a que batch pertenece un ejercicio.
                    if string in batches:  # Devuelve True si el batch está dentro del diccionario batches.
                        batches[string].append({'name': lista_split[2], 'due_date': lista_split[1], 'url': lista_split[3]})
                    # Se le concatena la información de un ejercicio al batch que pertenezca.
                    elif (int(lista_split[0]) > 0):
                        new_batch = [{'name': lista_split[2], 'due_date': lista_split[1], 'url': lista_split[3]}]
                        batches[string] = new_batch
                    # Si el batch no está dentro de 'batches', se crea un diccionario para el batch nuevo con la información de sus ejercicios.
                print('batch deseado?')
                bd=input()
                print(batches['batch' + '%s' %(bd)])  # Aquí se puede imprimir la información del diccionario de cada batch.
    elif command == 'summary' or command == 'c':
        print('aguanta')
    elif command == 'exit' or command == 'd':
        break
    else:
         print('invalid command')

