# La estructura básica de un for es la siguiente:
# for variable in secuencia:
#   Bloque de código a repetir
#   instrucciones

# frutas = ["manzana", "banana", "naranja"]

# for fruta in frutas:
#     print(fruta)

# for i in range(5):
#     pass

for i in range(10):

    if i % 2 == 0:
        continue    # Solo es útil en loops
    print(i)

