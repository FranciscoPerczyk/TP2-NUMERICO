import numpy as np
from decimal import Decimal
XT = -4.670E6
YT = 0
X2 = 379.7E6
Y2 = 0
G = 6.674E-11
M1 = 5972E21
M2 = 0#73.48E21
W = 0 #(4.236E-7)**2

def main():

	x0 = input("Ingrese x0:")
	if (not x0): x0 = -110401000
	y0 = input("Ingrese y0:")
	if (not y0): y0 = 	0
	vx0 = input("Ingrese vx0:")
	if (not vx0): vx0 = 0
	vy0 = input("Ingrese vy0:")
	if (not vy0): vy0 = 10000
	h = input('ingrese h:')
	if (not h): h = 0.1
	euler(float(x0), float(y0), float(vx0), float(vy0), float(h))


def escribir_posicion(archivo, v):
	archivo.write("{:.4E},{:.4E} \n".format(Decimal(v[0]), Decimal(v[1])))


def euler(x0, y0, vx0, vy0, h):
	archivo = open('posiciones.txt', 'w')
	Rn = np.array([vx0, vy0, x0, y0])
	F = euler_F(Rn)
	for i in range(100000):
		escribir_posicion(archivo, Rn[2:])
		Rn = np.add(Rn, np.multiply(h, euler_F(Rn)))
	archivo.close()


def euler_Fvx(x, y):
	return G*M1*np.cos(a1(x, y))/d1(x, y) + G*M2*np.cos(a2(x,y))/d2(x,y) + W*dg(x,y)*np.cos(a3(x,y))

def euler_Fvy(x, y):
	return G*M1*np.sin(a1(x, y))/d1(x, y) + G*M2*np.sin(a2(x,y))/d2(x,y) + W*dg(x,y)*np.sin(a3(x,y))

def euler_F(Rn):
	vx = Rn[0]
	vy = Rn[1]
	x = Rn[2]
	y = Rn[3]
	return np.array([euler_Fvx(x, y), euler_Fvy(x,y), vx, vy])

def a1(x, y):
	return np.arctan((YT - y)/(XT - x))


def a2(x, y):
	return np.arctan((Y2 - y)/(X2 - x))


def a3(x, y):
	return np.arctan(y/x)


def d1(x, y):
	return (XT - x)**2 + (YT - y)**2


def d2(x, y):
	return (X2 - x)**2 + (Y2 - y)**2

def dg(x, y):
	return np.sqrt(x**2 + y**2)

main()