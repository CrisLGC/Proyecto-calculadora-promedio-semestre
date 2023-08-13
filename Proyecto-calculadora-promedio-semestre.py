def prom2(a,b):
    promedio=(a+b)/2
    return promedio

def prom5(a,b,c,d,e):
    promedio=(a+b+c+d+e)/5
    return promedio

def prom4(a, b, c, d):
    promedio = (a+b+c+d)/4
    return promedio

print("A continuacion ingrese las notas que saco en cada parcial de matematica")
primerpmate=float(input("ingrese primer parcial"))
if primerpmate >20 or primerpmate <=0:
    print("error ingrese una nota valida del 1 al 20")
else:
    segundopmate=float(input("ingrese segundo parcial"))
    if segundopmate >20 or segundopmate <=0:
        print("error ingrese una nota valida del 1 al 20")
    else:
        tercerpmate=float(input("ingrese tercer parcial"))
        if tercerpmate >20 or tercerpmate <=0:
            print("error ingrese una nota valida del 1 al 20")
        else:
            cuartopmate=float(input("ingrese cuarto parcial"))
            if cuartopmate >20 or cuartopmate <=0:
                print("error ingrese una nota valida del 1 al 20")
            else:
                promediomat=prom4(primerpmate , segundopmate , tercerpmate, cuartopmate)
                
                print("A continuacion ingrese las notas que saco en cada parcial de fisica")
                primerpfis=float(input("ingrese primer parcial"))
                if primerpfis >20 or primerpfis <=0:
                    print("error ingrese una nota valida del 1 al 20")
                else:
                    segundopfis=float(input("ingrese segundo parcial"))
                    if segundopfis >20 or segundopfis<=0:
                        print("error ingrese una nota valida del 1 al 20")
                    else:
                        tercerpfis=float(input("ingrese tercer parcial"))
                        if tercerpfis>20 or tercerpfis <=0:
                            print("error ingrese una nota valida del 1 al 20")
                        else:
                            cuartopfis=float(input("ingrese cuarto parcial"))
                            if cuartopfis>20 or cuartopfis<=0:
                                print("error ingrese una nota valida del 1 al 20")
                            else:   
                                promediofis=prom4(primerpfis , segundopfis , tercerpfis, cuartopfis)
                                
                                print("A continuacion ingrese las notas que saco en cada parcial de algebra lineal")
                                primerpalg=float(input("ingrese primer parcial"))
                                if primerpalg>20 or primerpalg<=0:
                                    print("error ingrese una nota valida del 1 al 20")
                                else:
                                    segundopalg=float(input("ingrese segundo parcial"))
                                    if segundopalg>20 or segundopalg<=0:
                                        print("error ingrese una nota valida del 1 al 20")
                                    else:
                                        tercerpalg=float(input("ingrese tercer parcial"))
                                        if tercerpalg>20 or tercerpalg<=0:
                                            print("error ingrese una nota valida del 1 al 20")
                                        else:   
                                            cuartopalg=float(input("ingrese cuarto parcial"))
                                            if cuartopalg>20 or cuartopalg<=0:
                                                print("error ingrese una nota valida del 1 al 20")
                                            else:
                                                promedioalg=prom4(primerpalg , segundopalg , tercerpalg, cuartopalg)

                                                print("A continuacion ingrese las notas que saco en cada parcial de programacion")
                                                primerpprg=float(input("ingrese primer parcial"))
                                                if primerpprg>20 or primerpprg<=0:
                                                    print("error ingrese una nota valida del 1 al 20")
                                                else:
                                                    segundopprg=float(input("ingrese segundo parcial"))
                                                    if segundopprg>20 or segundopprg<=0:
                                                        print("error ingrese una nota valida del 1 al 20")
                                                    else:
                                                        tercerpprg=float(input("ingrese tercer parcial"))
                                                        if tercerpprg>20 or tercerpprg<=0:
                                                            print("error ingrese una nota valida del 1 al 20")
                                                        else:
                                                            cuartopprg=float(input("ingrese cuarto parcial"))
                                                            if cuartopprg>20 or cuartopprg<=0:
                                                                print("error ingrese una nota valida del 1 al 20")
                                                            else:
                                                                promedioprg=prom4(primerpprg , segundopprg , tercerpprg, cuartopprg)

                                                                print("A continuacion ingrese las notas que saco en cada parcial de creatividad")
                                                                primerpcre=float(input("ingrese primer parcial"))
                                                                if primerpcre>20 or primerpcre<=0:
                                                                    print("error ingrese una nota valida del 1 al 20")
                                                                else:
                                                                    segundopcre=float(input("ingrese segundo parcial"))
                                                                    if segundopcre>20 or segundopcre<=0:
                                                                        print("error ingrese una nota valida del 1 al 20")
                                                                    else:
                                                                        tercerpcre=float(input("ingrese tercer parcial"))
                                                                        if tercerpcre>20 or tercerpcre<=0:
                                                                            print("error ingrese una nota valida del 1 al 20")
                                                                        else:
                                                                            cuartopcre=float(input("ingrese cuarto parcial"))
                                                                            if cuartopcre>20 or cuartopcre<=0:
                                                                                print("error ingrese una nota valida del 1 al 20")
                                                                            else:
                                                                                prom4(primerpcre , segundopcre , tercerpcre, cuartopcre)
                                                                                
                                                                                print("el promedio de su 2do semestre es:", prom5(prom4(primerpcre , segundopcre , tercerpcre, cuartopcre), 
                                                                                prom4(primerpprg , segundopprg , tercerpprg, cuartopprg), 
                                                                                prom4(primerpalg , segundopalg , tercerpalg, cuartopalg), 
                                                                                prom4(primerpfis , segundopfis , tercerpfis, cuartopfis), 
                                                                                prom4(primerpmate , segundopmate , tercerpmate, cuartopmate)))