""" nome = input("escreva seu noome aki:")

time = input("time:")

print ("o", nome, "torce para o time", time)
 """
 


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

