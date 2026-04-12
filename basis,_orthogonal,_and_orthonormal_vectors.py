import numpy as np

# buat vector i dengan elemen (1,0) dan vector j dengan elemen (0,1)
i = np.array([1, 0])
i

j = np.array([0, 1])
j

# buktikan bahwa vector i dan vector j itu orthogonal
bukti1 = np.dot(i, j)
if bukti1 == 0:
  print(f'Jadi i dan j adalah orthogonal karena secara matematisnya juga (1, 0) . (0, 1) = (1 x 0) + (0 x 1) = {bukti1}')
else:
  print(f'i dan j bukan orthogonal karena hasil akhirnya {bukti1}')

#NOMOR 2

# Bagaimana dengan v=(1,2) dan w=(2,-1), apakah juga orthogonal?
v = np.array([1, 2])
w = np.array([2, -1])
bukti2 = np.dot(v, w)
if bukti2 == 0:
  print(f'v dan w juga orthogonal, karena hasil akhirnya: {bukti2}')
else:
  print(f'v dan w bukan orthogonal karena hasil akhirnya: {bukti2}')
