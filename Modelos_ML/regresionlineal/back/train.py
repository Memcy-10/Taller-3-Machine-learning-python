import matplotlib.pyplot as plt
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression

# Predecir precios de las casas basadas en su superficie

# Datos de entrenamiento (x) y etiquetas (y)
x = np.array([[40], [50], [70], [100], [200]])
y = np.array([410000000,500000000,700000000,1000000000,2000000000])

# Entrenamiento modelo regrecion lineal
Model =  LinearRegression()
Model.fit(x, y)

# Predicciones de prueba
# y_pred = Model.predict(x)
# # Imprimir la informacion del modelo entrenado
# print("Coeficiente (pendiente):", Model.coef_[0])
# print("Intersección (ordenada al origen):", Model.intercept_)

# # Graficar datos reales
# plt.scatter(x, y, color='red', label='Datos reales')

# # Graficar los datos de entrenamiento y la línea de regresión
# plt.plot(x,y_pred, color='blue', label='Línea de regresión')
# plt.xlabel("superficie m2")
# plt.ylabel("Precio(COP)")
# plt.title("Regresión lineal: Precio de casas vs Superficie (m2)")
# plt.legend()
# plt.grid(True)

# # Imprimir la grafica
# plt.show()

# Guardar el artefacto del modelo entrenado en un archivo
joblib.dump(Model,"./Modelos_ML/regrecion lineal/Models/linea_model.pkl")
