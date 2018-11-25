def calcular(sueldo):
    xsueldo = int(sueldo)
    if xsueldo > 0 or xsueldo <=12450:
        irpf = xsueldo * 0.19

        print("Cobrando ", sueldo, "€ al año, usted tendria que pagar ", irpf)
    elif xsueldo > 12450 or xsueldo <=20200:
        irpf = xsueldo * 0.24

        print("Cobrando ", sueldo, "€ al año, usted tendria que pagar ", irpf)
    elif xsueldo > 20200 or xsueldo <=35200:
        irpf = xsueldo * 0.30

        print("Cobrando ", sueldo, "€ al año, usted tendria que pagar ", irpf)
    elif xsueldo > 35200 or xsueldo <=60000:
        irpf = xsueldo * 0.37

        print("Cobrando ", sueldo, "€ al año, usted tendria que pagar ", irpf)
    elif xsueldo > 60000 :
        irpf = xsueldo * 0.45

        print("Cobrando ", sueldo, "€ al año, usted tendria que pagar ", irpf)


sueldo = input("Ingrese su salario anual: ")
calcular(sueldo)