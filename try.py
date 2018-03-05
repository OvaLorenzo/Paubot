username={}
name= input()
with open('iddata.py','r') as file:
    lines=file.readlines()
    for line in lines:
        n = line.strip().split(',')
        username[n] = u

    print(n)