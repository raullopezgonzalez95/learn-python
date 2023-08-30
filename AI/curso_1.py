# https://youtu.be/iX_on3VxZzk?list=PLZ8REt5zt2Pn0vfJjTAPaDVSACDvnuGiG
# https://www.tensorflow.org/install?hl=es-419
# https://numpy.org/install/

import tensorflow as tf
import numpy as np

c = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
f = np.array( [-40, 14, 32, 46.4, 59, 71.6, 100.4], dtype=float)

capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Comenzando entrenamiento...")
historial = modelo.fit(c, f, epochs=1000, verbose=False)
print("Modelo entrenado")

# import matplotlib.pyplot as plt

# plt.xlabel("# Epoca")
# plt.ylabel("Magnitud de perdida")
# plt.plot(historial.history["loss"])

res = modelo.predict([100.0])
print(res)

# log
# cas/learn-python/AI/curso_1.py
# 2023-08-29 18:01:59.914065: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
# To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
# Comenzando entrenamiento...
# Modelo entrenado
# 1/1 [==============================] - 0s 101ms/step
# [[211.99522]]