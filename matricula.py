usernames={}
def read_from_file():
    with open('db.txt.py', 'r') as file:
        lines = file.readlines()
        for line in lines:
            id, u =  line.strip().split(',')
            usernames[n] = u
            print(n)

# validacion de la matricula, acepta 8 digitos y solo numeros
# todavia no esta terminado

print('Whats your id?')
id=input()
if id.isnumeric() ==True:
    if len(id) != 8:
        print('invalid id')
        exit()
    else:
        print('xD')
        # por alguna razon me da KeyError el with open
        with open('iddata.py','r') as file:
            file.readlines()
            print(usernames[id])
else:
    print('invalid id')
    exit()