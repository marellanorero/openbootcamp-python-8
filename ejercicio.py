import datetime

t = datetime.datetime.now()
time = t.strftime('%H')
print("Son las: " + time)

if int(time) < 19:
    faltante = 19 - int(time)
    print("Te faltan " + faltante + "por trabajar")
else:
    print("Ya puedes ir a casa! Nos vemos mañana")