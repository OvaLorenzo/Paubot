# validacion de la matricula, acepta 8 digitos y solo numeros
login=False
print('Whats your id?')
while True:
    id = input()
    if id.isnumeric() ==False or len(id) != 8:
            print('invalid id')
    else:
        login=True
        # el login = True es para utilizarlo como booleano en el codigo del bot, si es que se necesita.
        print('La matricula %s ha sido registrada' % (id))
        # el with open escribe la matricula introducida 1 sola ves, digase, si corremos el programa de nuevo y
        # introducimos otra matricula, solo aparecera la ultima matricula introducida
        with open('iddata.py','w') as file:
            file.write(id)
        break
        # aqui abajo  el codigo de todo el bot
