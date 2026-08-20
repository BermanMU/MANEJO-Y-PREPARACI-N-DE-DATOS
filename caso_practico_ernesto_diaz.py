import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# =====================================================================
# EJERCICIO 1.1: IDENTIFICACIÓN DE UN VALOR ATÍPICO CON BOXPLOT
# =====================================================================
# Definí los montos de los pedidos en miles de colones. El valor 98 está muy
# separado del resto, por lo que espero verlo como una observación atípica.

# Datos del ejercicio
pedidos = [18, 22, 25, 27, 29, 30, 31, 33, 35, 36, 38, 40, 42, 45, 98]

# Creé una figura horizontal para facilitar la lectura de la escala de montos.
plt.figure(figsize=(8, 4))
# Dibujé el boxplot para resumir la distribución con cuartiles, mediana y bigotes.
# Con flierprops marqué en rojo los valores que quedan fuera de los bigotes.
sns.boxplot(x=pedidos, color="skyblue", flierprops={"markerfacecolor":"red", "marker":"o"})
# Agregué el título, la unidad de medida y una cuadrícula sobre el eje de montos.
plt.title("Distribución de Montos de Pedidos (Ejercicio 1.1)")
plt.xlabel("Monto (en miles de colones)")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()


# =====================================================================
# EJERCICIO 1.2: RECONSTRUCCIÓN DE UN BOXPLOT A PARTIR DE RESÚMENES
# =====================================================================
# Como no tengo los datos individuales, definí el resumen de cinco números y
# el valor atípico para reconstruir el diagrama de caja con Matplotlib.
stats = [{
    'label': 'Tiempo de Entrega',
    'whislo': 1,    # Mínimo
    'q1': 2,        # Primer cuartil
    'med': 3,       # Mediana
    'q3': 4,        # Tercer cuartil
    'whishi': 6,    # Máximo (límite del bigote)
    'fliers': [14]  # Valor atípico
}]

# Creé el lienzo y dibujé el resumen en orientación horizontal.
fig, ax = plt.subplots(figsize=(8, 4))
ax.bxp(stats, vert=False, showfliers=True, flierprops={"markerfacecolor":"red", "marker":"o"})
plt.title("Reconstrucción del Boxplot de Tiempos de Entrega (Ejercicio 1.2)")
plt.xlabel("Días")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()


# =====================================================================
# EJERCICIO 1.3-A: COMPARACIÓN DE COEFICIENTES DE VARIACIÓN
# =====================================================================
# Usé el coeficiente de variación (CV) para comparar la variabilidad relativa
# de los productos. Trabajé con los valores ya calculados y expresados en %.

productos = ['Producto A', 'Producto B']
cv_valores = [15, 30]  # Coeficientes de variación calculados

plt.figure(figsize=(6, 4))
# Dibujé una barra por producto para comparar directamente sus niveles de CV.
plt.bar(productos, cv_valores, color=['blue', 'orange'], alpha=0.7)
plt.title("Comparación del Coeficiente de Variación (CV)")
plt.ylabel("Porcentaje de Variabilidad (%)")
for i, v in enumerate(cv_valores):
    # Escribí el porcentaje encima de cada barra para evitar estimaciones.
    plt.text(i, v + 1, f"{v}%", ha='center', fontweight='bold')
plt.ylim(0, 35)
plt.show()


# =====================================================================
# EJERCICIO 1.3-B: REGIÓN CRÍTICA Y VALOR P EN UNA PRUEBA Z
# =====================================================================
# Representé los valores del caso B: alfa fija la región de rechazo y el valor
# p mide el área extrema asociada al estadístico observado.

# 1. Definí los datos de entrada del caso B.
alfa = 0.05
p_val = 0.184

# Valores Z fijos obtenidos de la tabla de distribución normal estándar
z_crit = 1.6449  # Frontera para alfa = 0.05
z_obs = 0.9004  # Punto equivalente para un área de p = 0.184


# 2. Definí la función de densidad de la distribución normal estándar.
# La función recibe valores Z y devuelve la altura de la campana en cada punto.
def calcular_densidad_normal(valores_z):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-(valores_z**2) / 2)


# Generé 500 puntos para dibujar una curva continua entre -4 y 4.
x = np.linspace(-4, 4, 500)
y = calcular_densidad_normal(x)

# 3. Creé el lienzo y dibujé la distribución de referencia.
plt.figure(figsize=(8, 5))

# Paso A: dibujé la curva normal bajo la hipótesis nula.
plt.plot(x, y, color="black", lw=2, label="Distribución Normal Z")

# Paso B: sombreé la región de rechazo desde Z crítico hasta el extremo derecho.
x_rechazo = np.linspace(z_crit, 4, 100)
y_rechazo = calcular_densidad_normal(x_rechazo)
plt.fill_between(
    x_rechazo,
    y_rechazo,
    color="red",
    alpha=0.4,
    label=f"Región Rechazo (α = {alfa})",
)

# Paso C: marqué el área del valor p desde Z observado hasta el extremo derecho.
x_p = np.linspace(z_obs, 4, 100)
y_p = calcular_densidad_normal(x_p)
plt.fill_between(
    x_p,
    y_p,
    color="none",
    edgecolor="blue",
    hatch="//",
    alpha=0.5,
    label=f"Área Valor p ({p_val})",
)

# Paso D: tracé líneas verticales para ubicar los dos valores de decisión.
# Usé rojo para el límite crítico y azul para el estadístico observado.
plt.axvline(
    x=z_crit,
    color="red",
    linestyle="--",
    lw=1.5,
    label=f"Z Crítico = {z_crit:.2f}",
)
# Línea sólida azul para mostrar la posición de la muestra analizada
plt.axvline(
    x=z_obs, color="blue", linestyle="-", lw=2, label=f"Z Observado = {z_obs:.2f}"
)

# Paso E: agregué el formato visual y expliqué la comparación p > alfa.
plt.title(
    f"Caso B (NO RECHAZA H0)\nAnálisis Visual: p ({p_val}) > α ({alfa})",
    fontsize=13,
    fontweight="bold",
)
plt.xlabel("Valor Z (Desviaciones Estándar)", fontsize=10)
plt.ylabel("Densidad de Probabilidad", fontsize=10)

# Añadí una anotación para resumir la conclusión estadística.
plt.text(
    -3.5,
    0.25,
    "Nota: La línea azul (datos reales)\nno logró entrar a la zona roja.\nNo hay pruebas para cambiar.",
    bbox=dict(facecolor="white", alpha=0.7, boxstyle="round,pad=0.5"),
    fontsize=9.5,
)

plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper left", fontsize=9.5)

# Paso F: ajusté los elementos al lienzo y mostré el gráfico terminado.
plt.tight_layout()
plt.show()





# =====================================================================
# EJERCICIO 2.2: COMPARACIÓN DE TRES PRUEBAS DE HIPÓTESIS
# =====================================================================
# Organicé los datos de los tres casos para generar un gráfico independiente
# y aplicar el mismo procedimiento de comparación en cada uno.

# 1. Definí los datos de entrada de cada caso del ejercicio 2.2.
casos = {
    "Caso A": {
        "alfa": 0.05,
        "p": 0.032,
        "z_critico": 1.6449,
        "z_observado": 1.8518,
        "rechaza": True,
    },
    "Caso B": {
        "alfa": 0.05,
        "p": 0.184,
        "z_critico": 1.6449,
        "z_observado": 0.9004,
        "rechaza": False,
    },
    "Caso C": {
        "alfa": 0.01,
        "p": 0.049,
        "z_critico": 2.3263,
        "z_observado": 1.6546,
        "rechaza": False,
    },
}


# 2. Definí la fórmula de la campana de Gauss para calcular la densidad
# de probabilidad correspondiente a cada valor Z.
def calcular_densidad_normal(valores_z):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-(valores_z**2) / 2)


# Generé 500 puntos entre -4 y 4 para trazar la curva continua de la campana.
x = np.linspace(-4, 4, 500)
y = calcular_densidad_normal(x)

# 3. Procesé y mostré un gráfico independiente para cada caso.
for nombre_caso, datos in casos.items():
    alfa = datos["alfa"]
    p_val = datos["p"]
    z_crit = datos["z_critico"]
    z_obs = datos["z_observado"]

    # Paso A: creé una figura nueva e independiente para este caso.
    plt.figure(figsize=(7, 4.5))

    # Paso B: dibujé la línea de la distribución normal.
    plt.plot(x, y, color="black", lw=2, label="Distribución Normal Z")

    # Paso C: coloreé la región de rechazo desde Z crítico hasta Z = 4.
    x_rechazo = np.linspace(z_crit, 4, 100)
    y_rechazo = calcular_densidad_normal(x_rechazo)
    plt.fill_between(
        x_rechazo,
        y_rechazo,
        color="red",
        alpha=0.4,
        label=f"Región Rechazo (α={alfa})",
    )

    # Paso D: marqué el área del valor p desde el Z observado hasta Z = 4.
    x_p = np.linspace(z_obs, 4, 100)
    y_p = calcular_densidad_normal(x_p)
    plt.fill_between(
        x_p,
        y_p,
        color="none",
        edgecolor="blue",
        hatch="//",
        alpha=0.5,
        label=f"Área Valor p ({p_val})",
    )

    # Paso E: tracé las líneas verticales de Z crítico y Z observado.
    plt.axvline(
        x=z_crit,
        color="red",
        linestyle="--",
        lw=1.5,
        label=f"Z Crítico = {z_crit:.2f}",
    )
    plt.axvline(
        x=z_obs,
        color="blue",
        linestyle="-",
        lw=2,
        label=f"Z Observado = {z_obs:.2f}",
    )

    # Paso F: agregué el resultado, el título, las etiquetas y la cuadrícula.
    resultado_texto = "RECHAZA H0" if datos["rechaza"] else "NO RECHAZA H0"
    plt.title(
        f"{nombre_caso} ({resultado_texto})\np = {p_val} vs α = {alfa}",
        fontsize=12,
        fontweight="bold",
    )
    plt.xlabel("Valor Z (Desviaciones Estándar)", fontsize=10)
    plt.ylabel("Densidad de Probabilidad", fontsize=10)

    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(loc="upper left", fontsize=9)

    # Paso G: ajusté el diseño y mostré el gráfico antes de pasar al siguiente.
    plt.tight_layout()
    plt.show()

# =====================================================================
# EJERCICIO 3.2: MONTOS PROMEDIO CON ERROR ESTÁNDAR
# =====================================================================
# Comparé los montos promedio de compra de la tienda física y la tienda en
# línea, mostrando la incertidumbre de cada media mediante barras de error.

# 1. Definí los datos extraídos de la tabla del ejercicio 3.2.
canales = ["Tienda Física", "Tienda en Línea"]
medias = [32500, 38900]  # Montos promedio de compra (X̄)
desviaciones = [8200, 9100]  # Desviaciones estándar muestrales (S)
muestras = [40, 45]  # Tamaños de muestra para cada canal (n)

# 2. Calculé el error estándar paso a paso.
# Apliqué la fórmula EE = S / sqrt(n), que estima la variabilidad esperada
# de cada media muestral.
error_estandar_fisica = desviaciones[0] / np.sqrt(muestras[0])
error_estandar_linea = desviaciones[1] / np.sqrt(muestras[1])

# Guardé ambos resultados en una lista para utilizarlos como barras de error.
errores_ee = [error_estandar_fisica, error_estandar_linea]

# Imprimí los resultados en consola para verificar mis cálculos.
print(f"Error Estándar - Física: ₡{error_estandar_fisica:.2f}")
print(f"Error Estándar - En Línea: ₡{error_estandar_linea:.2f}")

# 3. Construí el gráfico de comparación.
plt.figure(figsize=(7, 5))

# Definí un color para diferenciar visualmente cada canal.
colores = ["#4A90E2", "#50E3C2"]

# Dibujé las barras principales.
# Usé yerr para añadir los bigotes con los errores estándar calculados y
# capsize para definir el ancho de sus extremos horizontales.
barras = plt.bar(
    canales,
    medias,
    yerr=errores_ee,
    color=colores,
    capsize=8,
    edgecolor="black",
    alpha=0.85,
)

# 4. Agregué etiquetas con los valores monetarios exactos.
# Recorrí las barras para escribir el valor correspondiente en cada una.
for barra in barras:
    altura = barra.get_height()
    plt.text(
        barra.get_x() + barra.get_width() / 2.0,
        altura / 2,
        f"₡{int(altura):,}",
        ha="center",
        va="center",
        color="black",
        fontweight="bold",
        fontsize=11,
    )

# 5. Agregué los detalles visuales y la interpretación de negocio.
plt.title(
    "Comparación de Monto Promedio de Compra\n(Prueba t: p-valor = 0.021)",
    fontsize=13,
    fontweight="bold",
)
plt.ylabel("Monto de Compra Promedio (₡)", fontsize=11)
plt.grid(axis="y", linestyle=":", alpha=0.5)

# Añadí un cuadro de texto con la conclusión de negocio.
plt.text(
    -0.3,
    42000,
    "Nota: Las barras de error no se traslapan.\n"
    "La diferencia a favor de la tienda en línea\n"
    "es estadísticamente significativa (α = 5%).",
    bbox=dict(facecolor="lightyellow", alpha=0.8, boxstyle="round,pad=0.5"),
    fontsize=9.5,
)

# Ajusté los límites del eje Y para dejar espacio al texto explicativo.
plt.ylim(0, 47000)

# Finalmente, ajusté el diseño y mostré el gráfico en una ventana independiente.
plt.tight_layout()
plt.show()

# =====================================================================
# EJERCICIO 4.1: SIGNIFICANCIA ESTADÍSTICA Y SIGNIFICANCIA PRÁCTICA
# =====================================================================
# Analicé el mismo efecto desde dos perspectivas: primero su significancia
# estadística con una muestra grande y después su importancia práctica.

# 1. Definí los parámetros del ejercicio y del procedimiento estadístico.
efecto_real = -0.4  # Reducción observada (segundos)
n = 8000  # Gran tamaño de muestra
sigma = 3.5  # Desviación estándar supuesta del tiempo de pago

# Calculé el error estándar con la fórmula SE = sigma / sqrt(n).
se = sigma / np.sqrt(n)

# =====================================================================
# GRÁFICO 1: SIGNIFICANCIA ESTADÍSTICA (Distribución de Medias)
# =====================================================================
plt.figure(figsize=(8, 5))

# Generé puntos usando el error estándar que calculé.
x1 = np.linspace(-0.2, 0.2, 500)
# Calculé la campana del error muestral, centrada en 0 bajo H0.
y1 = (1 / (se * np.sqrt(2 * np.pi))) * np.exp(-(x1**2) / (2 * se**2))

plt.plot(
    x1, y1, color="#2C3E50", lw=2, label="Distribución de Medias bajo H0"
)

# Calculé los límites de la región de rechazo para alfa = 0.05 a dos colas.
z_critico = 1.96 * se
x_rechazo_izq = np.linspace(-0.2, -z_critico, 100)
y_rechazo_izq = (1 / (se * np.sqrt(2 * np.pi))) * np.exp(
    -(x_rechazo_izq**2) / (2 * se**2)
)
plt.fill_between(
    x_rechazo_izq, y_rechazo_izq, color="red", alpha=0.4, label="Zona Rechazo"
)

# Dibujé la posición del efecto real de -0.4 segundos.
# Como queda muy lejos a la izquierda, no entra en la escala visual elegida.
plt.axvline(
    x=efecto_real,
    color="blue",
    linestyle="-",
    lw=2,
    label=f"Efecto Real = {efecto_real}s",
)

plt.title(
    f"1. Significancia Estadística (Muestra Grande: n = {n})\n"
    f"El Error Estándar es minúsculo (SE = {se:.3f}s)",
    fontsize=12,
    fontweight="bold",
)
plt.xlabel("Diferencia en las Medias de Tiempo (Segundos)", fontsize=10)
plt.ylabel("Densidad de Probabilidad", fontsize=10)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper right", fontsize=9)

# Añadí una nota explicativa con el valor Z y el valor p.
plt.text(
    -0.18,
    4,
    f"¡Z es gigante!\nZ = {efecto_real/se:.1f}\nPor eso el valor-p\nes de 0.001",
    color="red",
    fontweight="bold",
    bbox=dict(facecolor="white", alpha=0.8),
)

plt.tight_layout()
plt.show()

# =====================================================================
# GRÁFICO 2: SIGNIFICANCIA PRÁCTICA (Experiencia Real del Cliente)
# =====================================================================
plt.figure(figsize=(8, 5))

# Generé puntos basados en la dispersión real de las transacciones (sigma).
x2 = np.linspace(-12, 12, 500)
y2 = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(x2**2) / (2 * sigma**2))

plt.plot(x2, y2, color="#2C3E50", lw=2, label="Variabilidad de Transacciones")

# Sombreé la zona del efecto imperceptible entre 0 y -0.4 segundos.
x_efecto = np.linspace(efecto_real, 0, 100)
y_efecto = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(
    -(x_efecto**2) / (2 * sigma**2)
)
plt.fill_between(
    x_efecto,
    y_efecto,
    color="blue",
    alpha=0.3,
    label=f"Ahorro de Tiempo ({abs(efecto_real)}s)",
)

plt.title(
    "2. Significancia Práctica (Experiencia del Cliente)\n"
    "El ahorro es insignificante en el proceso global",
    fontsize=12,
    fontweight="bold",
)
plt.xlabel(
    "Variación en el Tiempo de una Transacción Individual (Segundos)",
    fontsize=10,
)
plt.ylabel("Densidad de Probabilidad", fontsize=10)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper left", fontsize=9)

# Añadí una nota para explicar la conclusión desde el punto de vista del negocio.
plt.text(
    1,
    0.08,
    "Conclusión de Negocio:\n"
    "La franja azul es imperceptible.\n"
    "El cliente no notará el cambio.\n"
    "No se justifica la inversión financiera.",
    bbox=dict(facecolor="lightyellow", alpha=0.9, boxstyle="round,pad=0.5"),
    fontsize=9.5,
)

plt.tight_layout()
plt.show()



# =====================================================================
# EJERCICIO 4.2: REGIÓN DE RECHAZO Y VALOR P DEL NUEVO EMPAQUE
# =====================================================================
# Representé la prueba de hipótesis y comparé visualmente el valor p con alfa.

# 1. Definí los parámetros estadísticos obtenidos de las tablas estándar.
alfa = 0.05
p_valor = 0.09
z_critico = 1.6449  # Frontera para alfa = 0.05 (una cola)
z_observado = 1.3408  # Punto donde el área acumulada restante es 0.09


# 2. Definí la ecuación matemática de la distribución normal.
def calcular_densidad(valores_z):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-(valores_z**2) / 2)


# Generé los puntos de la curva base.
x = np.linspace(-4, 4, 500)
y = calcular_densidad(x)

# 3. Construí el gráfico de la prueba de hipótesis.
plt.figure(figsize=(8, 4.5))
plt.plot(x, y, color="black", lw=2, label="Distribución bajo H0 (Azar)")

# Coloreé la región de rechazo correspondiente a alfa = 0.05.
x_alfa = np.linspace(z_critico, 4, 100)
plt.fill_between(
    x_alfa,
    calcular_densidad(x_alfa),
    color="red",
    alpha=0.4,
    label=f"Región de Rechazo (α = {alfa})",
)

# Marqué el área correspondiente al valor p observado, p = 0.09.
x_p = np.linspace(z_observado, 4, 100)
plt.fill_between(
    x_p,
    calcular_densidad(x_p),
    color="none",
    edgecolor="blue",
    hatch="//",
    alpha=0.4,
    label=f"Área del Valor p ({p_valor})",
)

# Tracé líneas guía verticales para ubicar Z crítico y Z observado.
plt.axvline(
    x=z_critico,
    color="red",
    linestyle="--",
    lw=1.5,
    label=f"Z Crítico = {z_critico:.2f}",
)
plt.axvline(
    x=z_observado,
    color="blue",
    linestyle="-",
    lw=2,
    label=f"Z Observado = {z_observado:.2f}",
)

# Agregué el título, las etiquetas y la anotación de negocio.
plt.title(
    f"Ejercicio 4.2: Análisis del Nuevo Empaque (NO RECHAZA H0)\n"
    f"Matemáticas: p-valor ({p_valor}) > α ({alfa})",
    fontsize=12,
    fontweight="bold",
)
plt.xlabel("Escala de Desviaciones Estándar (Z)", fontsize=10)
plt.ylabel("Densidad de Probabilidad", fontsize=10)

plt.text(
    -3.8,
    0.22,
    "Corrección del Error:\n"
    "El Z observado no logró cruzar\n"
    "la frontera crítica roja.\n"
    "El efecto del empaque está en la\n"
    "ZONA DE INCERTIDUMBRE (Azar).",
    bbox=dict(facecolor="lightgray", alpha=0.8, boxstyle="round,pad=0.5"),
    fontsize=9.5,
)

plt.grid(True, linestyle=":", alpha=0.5)
plt.legend(loc="upper right", fontsize=9)
plt.tight_layout()
plt.show()





# =====================================================================
# EJERCICIO 4.3: INTERVALOS DE ERROR PARA DOS EQUIPOS
# =====================================================================
# Comparé los tiempos promedio de resolución y mostré el error estándar
# de cada equipo para visualizar la diferencia entre sus medias.

# 1. Definí los datos de entrada extraídos del ejercicio.
equipos = ["Equipo A", "Equipo B"]
medias = [4.2, 3.1]  # Tiempos promedio en días (X̄)
n_muestras = [30, 32]  # Tamaños de muestra (n)
sigma_supuesta = 1.2  # Desviación estándar estimada

# 2. Calculé el error estándar con la fórmula EE = sigma / sqrt(n).
ee_a = sigma_supuesta / np.sqrt(n_muestras[0])
ee_b = sigma_supuesta / np.sqrt(n_muestras[1])
errores_ee = [ee_a, ee_b]

# 3. Construí el gráfico de intervalos de error.
plt.figure(figsize=(6.5, 5))

# Usé errorbar para dibujar cada media con sus bigotes verticales.
# Con fmt='o' representé la media mediante un círculo sólido.
plt.errorbar(
    equipos,
    medias,
    yerr=errores_ee,
    fmt="o",
    color="#1E375A",
    markersize=10,
    capsize=8,
    linewidth=2.5,
    label="Media Muestral ± 1 EE",
)

# Añadí líneas horizontales en las medias para enfatizar la brecha visual.
plt.axhline(
    y=medias[0], color="#E74C3C", linestyle=":", alpha=0.6, lw=1.5
)
plt.axhline(
    y=medias[1], color="#2ECC71", linestyle=":", alpha=0.6, lw=1.5
)

# 4. Configuré la presentación visual y agregué el texto de negocio.
plt.title(
    "Tiempo Promedio de Resolución de Quejas\n"
    "Diferencia Práctica Altamente Significativa (p = 0.006)",
    fontsize=12,
    fontweight="bold",
)
plt.ylabel("Días de Espera del Cliente", fontsize=10)
plt.xlabel("Equipos de Soporte en LMB", fontsize=10)
# Ajusté la escala vertical para apreciar mejor la brecha entre los equipos.
plt.ylim(2.5, 4.8)

# Añadí una anotación con la diferencia real detectada.
plt.text(
    0.5,
    3.65,
    f"Brecha Real:\nΔX̄ = 1.1 Días\n"
    f"El Equipo B resuelve\n"
    f"un 26% más rápido.",
    ha="center",
    bbox=dict(facecolor="#E8F8F5", edgecolor="#2ECC71", boxstyle="round,pad=0.5"),
    fontsize=10,
    fontweight="bold",
)

plt.grid(axis="y", linestyle=":", alpha=0.5)
plt.legend(loc="lower left", fontsize=9.5)
plt.tight_layout()
plt.show()
