print ("........Solicitar al usuario un año,dar como resultado si es bisiesto o no.....")
print ("....................Por favor digite el año a evaluar...........................")

year=int (input("ingrese un año:"))

if(year % 4 == 0 and year % 100!=0 ) or (year % 400 == 0) :
    print ("El año",year,"es un año bisiesto")
else :
    print ("El año",year, "no es un año bisiesto:")
