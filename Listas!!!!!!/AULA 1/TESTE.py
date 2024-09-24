""" nome = input("escreva seu noome aki:")

time = input("time:")

print ("o", nome, "torce para o time", time)




A, B, C = input("escreva o valor de A, B e C:").split()

A = float(A)

B = float(B)

C = float(C)


delta = (B**2) - 4 * A * C

if delta == 0: {
    print("impossivel calcular")
  }

x1 = (-B + (delta ** 0.5))/(2 * A)

x2 = (-B - (delta ** 0.5))/(2 * A)


print("x1 é =", x1)
print("x2 é =", x2)
"""




""" x_alvo, y_alvo, raio_alvo = input("digite os valores do alvo X, Y e seu raio: ").split()
x_alvo = float(x_alvo)
y_alvo = float(y_alvo)
raio_alvo = float(raio_alvo)

x_tiro, y_tiro, raio_tiro = input("digite onde foi o tiro x e y, e onde foi o raio do tiro: ").split()
x_tiro = float(x_tiro)
y_tiro = float(y_tiro)
raio_tiro = float(raio_tiro)

distancia = ((x_alvo - x_tiro) ** 2 + (y_alvo - y_tiro) ** 2) ** 0.5

if x_alvo != x_tiro: 
  print("o tiro nao teve a colisao pois o alvo: ", x_alvo, "e o tiro: ", x_tiro, "não estao no mesmo ponto")
  print("a distancia do alvo ao tiro foi: ", distancia)

elif y_alvo != y_tiro:
  print("o tiro nao teve a colisao pois o alvo: ", y_alvo, "e o tiro: ", y_tiro, "não estao no mesmo ponto")
  print("a distancia do alvo ao tiro foi: ", distancia)

elif raio_alvo != raio_tiro:
  print("o tiro nao teve a colisao pois o raio do alvo:", raio_alvo,"e do tiro: ", raio_tiro,"não batem")
  print("a distancia do alvo ao tiro foi: ", distancia)
  
else:
  print("o tiro teve uma colisao")
  print("a distancia do alvo ao tiro foi: ", distancia)
"""

  

""" 
if distancia <= (raio_alvo + raio_tiro):
  print("o tiro teve a colisao")
else:
  print("o tiro nao teve a colisao pois o") """



























import math


AOC = float(input("escreva o valor do angulo: "))
AOC = math.radians(AOC)
t = float(input("digite o tamanho do canhão: "))


h, w = input("digite o valor da altura e da largura do tanque: ") .split()
h = float(h)
w = float(w)


ty, tx = input("digite o valor do canhão na posição ty e tx: ") .split()
ty = float(ty)
tx = float(tx)


by = ty

bx = (w/2) + tx

cy = by - (t * math.cos(AOC))
cx = bx + (t * math.sin(AOC))



print("o valor do angulo é: ", AOC,)

print("o valor da altura do tanque é", h, "e o valor de largura do tanque é", w)

print("o valor de ty é", ty, "e o valor de tx é", tx)

print("o valor de bx é: ", bx)

print("o valor de  by é: ", by)

print("o valor de cy é", cy, "e o valor de cx é", cx)






















""" cy = by - (t*Math.cos(AOC))
print("o valor da posição da ponta do canhão é: ", cy)


cx = bx - (t * math.sin(AOC))
print("o valor da posição da ponta do canhão é: ", cx) """


