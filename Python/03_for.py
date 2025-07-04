# La estructura básica de un for es la siguiente:
# for variable in secuencia:
#   Bloque de código a repetir
#   instrucciones

for i in range(10):

    if i % 2 == 0:
        continue    # Solo es útil en loops
    print(i)
""" 
Condición continue
Si es verdadera (es decir, i es par), se ejecuta continue.
Esto provoca que el bucle salte inmediatamente al siguiente valor
de i, sin ejecutar las líneas que vienen después dengtro del cuerpo 
del for.

Por otra parte, si es falsa (es decir, i es impar), no entra en el if
y continúa ejecutando la siguiente instrucción.
 """

