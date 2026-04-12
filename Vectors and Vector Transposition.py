#Nomor 1
import numpy as np

# buat vector x_np dengan ukuran 3x1
x_np = np.array([[13], [17], [30]])
print(x_np)

# buat vektor y_np dengan ukuran 3x1
y_np = np.array([[18], [22], [40]])
print(y_np)

# hitung panjang vector x_np
len(x_np)

# tampilkan ukuran vector x_np
x_np.shape

# tampilkan tipe data dari vector x_np
x_np.dtype

# akses elemen pertama dari vector x_np
x_np[0]

# tampilkan tipe data elemen pertama dari vector x_np
x_np[0].dtype

#Nomor 2

# lakukan transpose pada vector x_np dan simpan pada variabel x_t
x_t = x_np.T
print(x_t)

# tampilkan ukuran dari vector x_t
x_t.shape

# lakukan transpose pada vector y_np dan simpan pada variabel y_t
y_t = y_np.T
print(y_t)

#nomor 3
import torch as pt

# buat vector x_pt dengan ukuran 3x1 menggunakan pytorch dan ukuran dari vector x_pt
x_pt = pt.tensor([13, 17, 30])
print(x_pt)
x_pt.shape

# buat vector y_pt dengan ukuran 3x1 menggunakan pytorch dan ukuran dari vector y_pt
y_pt = pt.tensor([18, 22, 40])
print(y_pt)
y_pt.shape

# lakukan transpose pada vector x_pt dan simpan pada variabel x_pT
x_pT = x_pt.T
print(x_pT)
x_pT.shape

#tensorfloww
import tensorflow as tf

# buat vector x_pt dengan ukuran 3x1 menggunakan tensorflow dan ukuran dari vector x_pt
x_tf = tf.Variable([13, 17, 30], dtype = tf.int32)
print(x_tf)
x_tf.shape

# buat vector y_pt dengan ukuran 3x1 menggunakan tensorflow dan ukuran dari vector y_pt
y_tf = tf.Variable([18, 22, 40], dtype = tf.int32)
print(y_tf)
y_tf.shape

# lakukan transpose pada vector x_tf dan simpan pada variabel x_tF
x_tF = tf.transpose(x_tf)
print(x_tF)
x_tF.shape
