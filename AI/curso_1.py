# https://youtu.be/iX_on3VxZzk?list=PLZ8REt5zt2Pn0vfJjTAPaDVSACDvnuGiG
# https://www.tensorflow.org/install?hl=es-419
# https://numpy.org/install/

import tensorflow as tf
import numpy as np

c = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
f = np.array( [-40, 14, 32, 46.4, 59, 71.6, 100.4], dtype=float)

# units son la cantidad de nuronas por capa
oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1, oculta2, salida])

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
