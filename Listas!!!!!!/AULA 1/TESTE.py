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