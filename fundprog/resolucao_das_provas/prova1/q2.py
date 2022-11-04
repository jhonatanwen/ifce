for i in range(50, 101):
    primo = True

    for j in range(2, i):
        if(i % j == 0):
            primo = False
    
    if(primo):
        print(f'{i} é primo e impar')
    elif(i % 2 != 0):
        print(f'{i} é impar')
    else:
        print(f'{i} é par')