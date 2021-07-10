user = input("Ingresa una palabra.\n")

if " " in user:
    print("Ingresa una sola palabra.")
else: 
    a = len(user)
    b = "*" * a
    b = list(b)
    oportunidades = 0
    print(b)
    print(user)
while "*" in b:
    letra = input("Ingresa una letra \n")
    for i in range (len(user)):
        if (letra == user[i]):
            b[i] = user[i]
    print(b)



        
