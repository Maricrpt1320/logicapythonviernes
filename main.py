nivelAgua= int(input('Digita la cantidad de agua de la represa:'))

if (nivelAgua<200):
    print('No tengo agua')
elif (nivelAgua>=200 and nivelAgua<450):
    print('Esta en su punto')
else: 
    print('Nos vamos a morir')    

