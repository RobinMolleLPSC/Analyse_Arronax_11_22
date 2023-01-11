import numpy as np
import os
import scipy
import Fichier_trc as fichier
import readTrc as rT
import matplotlib.pyplot as plt
from scipy import integrate
from scipy.optimize import curve_fit

adresse = "C:\\Users\\molle\\Documents\\LPSC_Stage\\ARRONAX\\ARRONAX_11_22\\Data\\SamEndommagement\\"
pointA = "PointA"
pointB = "PointB"
pointC = "PointC"
pointD = "PointD"
pointE = "PointE"
num_acqu = [str(i).zfill(2) for i in range(11)]

liste_point = [pointA,pointB,pointC,pointD,pointE]
file = "C2--"

flux = [3.25472E+13,1.65521E+13,5.72958E+12,1.59155E+12,5.57042E+11]
#surface_irradiee =[0.022,0.024,0.025,0.012,0.010]
surface_irradiee = [1,1,1,1,1]

FluenceA0 = [ 1.99872E11*i+2.98742E13 for i in range(59)]
FluenceA1 = [ 1.15991E11*i+1.42296E14 for i in range(61)]
FluenceA2 = [ 1.24131E11*i+2.83019E14 for i in range(76)]
FluenceA3 = [ 1.46573E11*i+4.24529E14 for i in range(59)]
FluenceA4 = [ 1.10339E11*i+5.66038E14 for i in range(57)]
FluenceA5 = [ 1.15991E11*i+7.07548E14 for i in range(61)]
FluenceA6 = [ 1.22838E11*i+8.49057E14 for i in range(64)]
FluenceA7 = [ 1.45138E11*i+9.90567E14 for i in range(65)]
FluenceA8 = [ 1.14121E11*i+1.13208E15 for i in range(62)]
FluenceA9 = [ 0.929871E11*i+1.27752E15 for i in range(93)]
FluenceA10 = [ 1.10869E11*i+1.4151E15 for i in range(78)]

FluenceB0 = [ 1.03480E11*i+1.19943E13 for i in range(85)]
FluenceB1 = [ 1.12446E11*i+1.44731E14 for i in range(64)]
FluenceB2 = [ 1.21154E11*i+2.87863E14 for i in range(66)]
FluenceB3 = [ 1.24940E11*i+4.31794E14 for i in range(64)]
FluenceB4 = [ 1.24940E11*i+5.76525E14 for i in range(64)]
FluenceB5 = [ 1.12446E11*i+7.20457E14 for i in range(64)]
FluenceB6 = [ 1.17591E11*i+8.64388E14 for i in range(68)]
FluenceB7 = [ 1.12446E11*i+1.00912E15 for i in range(64)]
FluenceB8 = [ 1.14231E11*i+1.15145E15 for i in range(63)]
FluenceB9 = [ 1.12446E11*i+1.29938E15 for i in range(64)]
FluenceB10 = [ 1.11058E11*i+1.44011E15 for i in range(108)]

FluenceC0 = [ 1.24131E11*i+7.86164E11 for i in range(76)]
FluenceC1 = [ 1.20948E11*i+1.4151E14 for i in range(65)]
FluenceC2 = [ 1.20948E11*i+2.83805E14 for i in range(65)]
FluenceC3 = [ 0.967586E11*i+4.26101E14 for i in range(65)]
FluenceC4 = [ 1.07204E11*i+5.66824E14 for i in range(66)]
FluenceC5 = [ 0.914144E11*i+7.01258E14 for i in range(86)]
FluenceC6 = [ 1.05604E11*i+8.49843E14 for i in range(67)]
FluenceC7 = [ 1.15612E11*i+9.90567E14 for i in range(68)]
FluenceC8 = [ 1.10554E11*i+1.13286E15 for i in range(64)]
FluenceC9 = [ 1.12309E11*i+1.27437E15 for i in range(63)]
FluenceC10 = [ 1.64380E11*i+1.41588E15 for i in range(110)]

# j'en suis là

FluenceD0 = [ 1.99872E11*i+2.98742E13 for i in range(59)]
FluenceD1 = [ 1.15991E11*i+1.42296E14 for i in range(61)]
FluenceD2 = [ 1.24131E11*i+2.83019E14 for i in range(76)]
FluenceD3 = [ 1.46573E11*i+4.24529E14 for i in range(59)]
FluenceD4 = [ 1.10339E11*i+5.66038E14 for i in range(57)]
FluenceD5 = [ 1.15991E11*i+7.07548E14 for i in range(61)]
FluenceD6 = [ 1.22838E11*i+8.49057E14 for i in range(64)]
FluenceD7 = [ 1.45138E11*i+9.90567E14 for i in range(65)]
FluenceD8 = [ 1.14121E11*i+1.13208E15 for i in range(62)]
FluenceD9 = [ 0.929871E11*i+1.27752E15 for i in range(93)]
FluenceD10 = [ 1.10869E11*i+1.4151E15 for i in range(78)]

FluenceE0 = [ 1.99872E11*i+2.98742E13 for i in range(59)]
FluenceE1 = [ 1.15991E11*i+1.42296E14 for i in range(61)]
FluenceE2 = [ 1.24131E11*i+2.83019E14 for i in range(76)]
FluenceE3 = [ 1.46573E11*i+4.24529E14 for i in range(59)]
FluenceE4 = [ 1.10339E11*i+5.66038E14 for i in range(57)]
FluenceE5 = [ 1.15991E11*i+7.07548E14 for i in range(61)]
FluenceE6 = [ 1.22838E11*i+8.49057E14 for i in range(64)]
FluenceE7 = [ 1.45138E11*i+9.90567E14 for i in range(65)]
FluenceE8 = [ 1.14121E11*i+1.13208E15 for i in range(62)]
FluenceE9 = [ 0.929871E11*i+1.27752E15 for i in range(93)]
FluenceE10 = [ 1.10869E11*i+1.4151E15 for i in range(78)]