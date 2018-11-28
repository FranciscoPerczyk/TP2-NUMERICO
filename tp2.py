import numpy as np
from decimal import Decimal

XT = -4.670E6
YT = 0
X2 = 379.7E6
Y2 = 0
G = 6.674E-11
M1 = 5972E21
M2 = 73.48E21
W = 4.236E-7 ** 2
R_TIERRA = 6.731E6 + 0.602E6
V_TIERRA = np.sqrt(G*M1/R_TIERRA)


def main():
	x0 = -12003000
	y0 = 0
	vx0 = 0
	vy0 = input("Ingrese vy0:")
	if (not vy0): vy0 = V_TIERRA
	h = input('ingrese h:')
	if (not h): h = 0.1
	cant_iter = input('Ingrese cantidad de iteraciones:')
	if (not cant_iter): cant_iter = 100000

	#runge_kutta(float(x0), float(y0), float(vx0), float(vy0), float(h), int(cant_iter))
	euler(float(x0), float(y0), float(vx0), float(vy0), float(h), int(cant_iter))


def escribir_par(archivo, v):
	archivo.write("{:.4E},{:.4E} \n".format(Decimal(v[0]), Decimal(v[1])))

def escribir_d(archivo, d):
	archivo.write("{:.4E},\n".format(float(d)))


def output_e(t,R, f):	
	e_cin = e_cinetica(R)
	e_pot = e_potencial(R)
	f.write("{},{},{},{}\n".format(float(e_cin),float(e_pot),float(e_cin+e_pot),float (t)))

def runge_kutta(x0, y0, vx0, vy0, h, cant_iter):
	archivo = open('posiciones_rk.txt', 'w')
	archivoe = open('emecanica_rk.txt', 'w')
	archivod = open('distancia_rk.txt', 'w')
	Rn = np.array([vx0, vy0, x0, y0])
	for i in range(cant_iter):
		escribir_d(archivod, d1(Rn[2], Rn[3]))
		output_e(h*i,Rn, archivoe)
		escribir_par(archivo, Rn[2:])
		Rn = np.add(Rn, np.multiply(0.5, cal_Rq(Rn, h)))
	output_e(h*i,Rn, archivoe)
	archivo.close()
	archivoe.close()


def cal_Rq(Rn, h):
	Rq1 = cal_Rq1(Rn, h)
	Rn = Rn + Rq1
	Rq2 = cal_Rq2(Rn, Rq1, h)
	Rn = Rn - Rq1
	return np.add(Rq1, Rq2)


def cal_Rq1(Rn, h):
	return np.array([h * Fvx(Rn[2], Rn[3]), h * Fvy(Rn[2], Rn[3]), h * Rn[0], h * Rn[1]])


def cal_Rq2(Rn, Rq1, h):
	return np.array(
		[h * Fvx(Rn[2] + Rq1[2], Rn[3] + Rq1[3]), h * Fvy(Rn[2] + Rq1[2], Rn[3] + Rn[3]), h * Rn[0],
		 h * Rn[1]])


def euler(x0, y0, vx0, vy0, h, cant_iter):
	archivo = open('posiciones_euler.txt', 'w')
	archivoe = open('emecanica_euler.txt', 'w')
	archivod = open('distancia_euler.txt', 'w')
	Rn = np.array([vx0, vy0, x0, y0])
	R0 = Rn.copy()
	for i in range(cant_iter):
		escribir_d(archivod, d1(Rn[2], Rn[3]))
		output_e(h*i,Rn, archivoe)
		escribir_par(archivo, Rn[2:])
		Rn = np.add(Rn, np.multiply(h, euler_F(Rn)))
	output_e(h*i,Rn, archivoe)
	archivo.close()
	archivoe.close()


def Fvx(x, y):
	return ((G * M1 * np.cos(a1(x, y))) / d1(x, y)) + ((G * M2 * np.cos(a2(x, y))) / d2(x, y)) + (
			W * dg(x, y) * np.cos(a3(x, y)))


def Fvy(x, y):
	return ((G * M1 * np.sin(a1(x, y))) / d1(x, y)) + ((G * M2 * np.sin(a2(x, y))) / d2(x, y)) + (
			W * dg(x, y) * np.sin(a3(x, y)))


def euler_F(Rn):
	vx = Rn[0]
	vy = Rn[1]
	x = Rn[2]
	y = Rn[3]
	return np.array([Fvx(x, y), Fvy(x, y), vx, vy])


def a1(x, y):
	return np.arctan2((YT - y), (XT - x))


def a2(x, y):
	return np.arctan2((Y2 - y), (X2 - x))


def a3(x, y):
	return np.arctan2(y, x)


def d1(x, y):
	return (XT - x) ** 2 + (YT - y) ** 2


def d2(x, y):
	return (X2 - x) ** 2 + (Y2 - y) ** 2


def dg(x, y):
	return np.sqrt(x ** 2 + y ** 2)


# Energia -------------------------
def e_cinetica(R):
	vx, vy = R[0], R[1]
	return np.linalg.norm(np.array([vx, vy])) ** 2 / 2

def e_potencial(R):
	x, y = R[2], R[3]
	return -G * (M1 / np.sqrt(d1(x, y)) - M2 / np.sqrt(d2(x, y)))

main()