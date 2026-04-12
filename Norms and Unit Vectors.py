#nomor 1
import numpy as np

# buat vector x dengan ukuran 3x1
x = np.array([[11], [23], [31]])
print(x)
x.shape
# hitung nilai L2 norm dari vector x
(11**2 + 23**2 + 31**2)**0.5
norm_x = np.linalg.norm(x)
print(norm_x)

#nomor 2
# buat vector v dengan elemen (3,4)
v = np.array([[2], [7]])
print(v)
# hitung nilai L2 norm dari vector v
(2**2 + 7**2)**0.5
# tampilkan unit vector dari vector v
norm_v = np.linalg.norm(v)
print(norm_v)
# hitung panjang unit vector dari vector v
unit_v = v / np.linalg.norm(v)
np.linalg.norm(unit_v)
