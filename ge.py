n=['list','lost','lust']
for i in range(0, len(n)):
    with open('gg.py','a') as file:
        file.writelines(n[i]+'\n')