jugadores=["Messi", "Cr7", "Mbappe"]
for jugador in jugadores:
    print(jugador)

tupla=("Lionel", "Cristiano","Kilyan")

print(tupla)

tupla= ("Lionel Andres","Cristiano","Kylian")

print(tupla)

#SACAR UN ELEMENTO DE LA TUPLA/ cuando desempquetamos, es una lista, etnonces podemos  modificar sobre lalista


a,b,c=tupla

print(a)

a="MessiDios"

print(a)
print(tupla[0])
tupla= ("Lionel Andres","Cristiano","Kylian",1,2,3,4,5,6,7,8,9)

a,b,*c=tupla

print(a,b,c)

c[0]=987

print(c)

#CONJUNTO
lenguajes = {"python","c","rust","python"}
print(lenguajes)


numeros=range(11)

print(numeros)

for i in range(11):
    print(i)

for i in range(0,10,2):
    print(i)