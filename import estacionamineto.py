
horas=int(input("Ingrese la cantidad de horas: "))
monto_final_pagar= 0
if horas >= 2 and horas <=5:
    monto_final_pagar = horas * 10;
elif horas >=5:
    monto_final_pagar = horas * 15;

print ("su monto a pagar es de: ", monto_final_pagar)
