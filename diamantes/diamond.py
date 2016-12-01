def diamond(n):
    # Make some diamonds!
    asteriscos = ""
    if n >= 0 and n % 2 != 0:
        lista = list(range(1,n+1)) + list(range(n-1,0,-1))  
        print(lista)
        for item in lista:
            if item % 2 != 0:
                qtde = " "*((n-item)//2) + "*"*item
                asteriscos += qtde + '\n'
    else:
        asteriscos = None
    return asteriscos
    
print(diamond(9))