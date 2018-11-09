#!/usr/bin/env python
import ctypes as C

biblio = C.CDLL('./calc_lib.so')

# prueba add_float

biblio.add_float.restype = C.c_float
biblio.add_float.argtypes = [C.c_float, C.c_float]
print biblio.add_float(5,6)

# prueba add_int 

print (biblio.add_int(3,4))

# prueba add_float_ref

dos = C.c_float(2)
tres = C.c_float(3)
res = C.c_float()
biblio.add_float_ref(C.byref(dos),C.byref(tres),C.byref(res))
print(res.value)

# prueba add_int_ref

dos = C.c_int(2)
cuatro = C.c_int(4)
res = C.c_int()
biblio.add_int_ref(C.byref(dos),C.byref(cuatro),C.byref(res))
print(res.value)

# prueba add_int_array

dos = (C.c_int*3)(1,2,-2)
tres = (C.c_int*3)(1,7,648)
res = (C.c_int*3)()
biblio.add_int_array(C.byref(dos),C.byref(tres),C.byref(res),3)
print(res[0], res[1], res[2])

# prueba dot_product

dos = (C.c_float*4)(1.0,2.0,-2.0,4.0)
tres = (C.c_float*4)(1.0,7.0,2.0,4.0)
#print (biblio.dot_product(C.byref(dos),C.byref(tres),4))

biblio.dot_product.restype = C.c_float
biblio.dot_product.argtypes = [(C.c_float*4), (C.c_float*4)]
print (biblio.dot_product(dos,tres,4))


