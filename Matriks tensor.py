#Nomor 1
import numpy as np

# buat matrix X berukuran 2x3 menggunakan numpy
X = np.array([[13, 21, 34], [46, 59, 67]])
print(X)
# tampilkan ukuran dari matrix X
print(f"Ukuran matrix X: {X.shape}")
# tampilkan seluruh elemen dari kolom pertama dari matrix X
print(X[:, 0])
# tampilkan seluruh elemen dari baris kedua dari matrix X
print(X[:, 1])

#pytrch
import torch as pt

# ulangi soal nomor 1 menggunakan pytorch

# buat matrix X berukuran 2x3
X = pt.tensor([[13, 21, 34], [46, 59, 67]])
print(X)

# tampilkan ukuran dari matrix X
print(f"Ukuran matrix X: {X.shape}")

# tampilkan seluruh elemen dari kolom pertama dari matrix X
print(X[:, 0].tolist())

# tampilkan seluruh elemen dari kolom pertama dari matrix X
print(X[:, 1].tolist())

#Tensorflow
import tensorflow as tf

# buat matrix X berukuran 2x3
X = tf.Variable([[13, 21, 34], [46, 59, 67]])
print(X)

# tampilkan ukuran dari matrix X
print(f"Ukuran matrix X: {X.shape}")

# tampilkan seluruh elemen dari kolom pertama dari matrix X
print(X[:, 0].numpy())

# tampilkan seluruh elemen dari kolom kedua dari matrix X
print(X[:, 1].numpy())
