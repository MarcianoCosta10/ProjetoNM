import math
# CABO 1
print('\033[34m',"="*10,"C1","="*13,'\033[m')
# CALCULO DO F1
v1 = float(input("Informe o Kg/m do Cabo: "))
v2 = float(input("Informe o tamanho em metros do cabo 1: "))
f1 = (v1 * v2)
r1 = f1

# CALCULO DO COSSENO E SENO V3
v3 = float(input("Informe o angulo do cabo 1: "))
coss = math.cos(math.radians(v3))
sen = math.sin(math.radians(v3))

# CALCULO DO F2
f2 = r1 * coss
r2 = f2

# CALCULO DO F3
f3 = r1 * sen
r3 = f3

# CABO 2
print('\033[34m',"="*10,"C2","="*13,'\033[m')
v6a = float(input("Informe o angulo do cabo 2: "))
v6 = v6a + 0.000000001
v4 = float(input("Informe o comprimento do cabo 2:"))

# SENO E COSSENO V6
coss2 = math.cos(math.radians(v6))
sen2 = math.sin(math.radians(v6))

# CALCULO DO F4
f4 = v4 * v1
r4 = f4

# CALCULO DO F5
f5 = r4 * coss2
r5 = f5

# CALCULO DO F6
f6 = r4 * sen2
r6 = f6

# CALCULO DO F7
f7 = r3 + r6
r7 = f7

# CALCULO DO F8)
f8 = (r2 - r5)
if f8 <= 0:
    f8 = f8*(-1)
r8 = f8

print('\033[34m',"="*8,"CALCULO DA FORÇA RESULTANTE","="*17,'\033[m')
f9 = ((r7**2) + (r8**2))**(1/2)
r9 = f9
print("O valor da Força Resultante é {:.2f}".format(r9),"\n")

print('\033[34m',"="*8,"CALCULO DO ÂNGULO DA FORÇA RESULTANTE","="*8,'\033[m',)
teta = math.degrees(math.atan(r7/r8))
r10 = teta
print("O Ângulo da Força Resultante é {:.2f}°".format(r10))

