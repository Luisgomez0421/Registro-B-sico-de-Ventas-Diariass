# 🛒 Sistema Básico de Registro de Ventas - RiwiTechStore

Este es un programa sencillo desarrollado en **Python** que permite registrar una venta en la tienda ficticia **RiwiTechStore**, calculando automáticamente el subtotal, aplicando descuento por membresía VIP y mostrando el total final a pagar.

---

## 📌 Descripción

El sistema solicita al usuario:

- Nombre del cliente  
- Precio unitario del producto  
- Cantidad de productos comprados  
- Si el cliente posee membresía VIP  

Si el cliente tiene membresía VIP, se aplica un **10% de descuento** sobre el subtotal de la compra.

Finalmente, el programa muestra un resumen detallado de la venta.

---

## ⚙️ Funcionalidades

✔ Captura de datos por consola  
✔ Cálculo automático del subtotal  
✔ Aplicación de descuento del 10% para clientes VIP  
✔ Visualización clara del resumen de venta  
✔ Formato monetario con dos decimales  

---

## 🧮 Fórmulas utilizadas

- **Subtotal** = precio_unitario × cantidad  
- **Descuento VIP** = subtotal × 0.10  
- **Total final** = subtotal − descuento  

---

## 🖥️ Requisitos

- Python 3.x instalado

Puedes verificar tu versión con:

```bash
python --version
```

---

## ▶️ Cómo ejecutar el programa

1. Guarda el archivo como:

```bash
registro_ventas.py
```

2. Ejecuta el programa desde la terminal:

```bash
python registro_ventas.py
```

3. Ingresa los datos solicitados en la consola.

---

## 💡 Ejemplo de ejecución

```
Sistema básico de registro de ventas - RiwiTechStore
Ingresar el nombre del cliente: Luis
Ingrese el precio unitario del producto: 100
Ingrese la cantidad de productos comprados: 2
¿El cliente cuenta con alguna membresía VIP? (si/no): si

----- RESUMEN DE LA VENTA -----
Cliente: Luis
Subtotal: $200.00
Descuento aplicado: $20.00
Total final a pagar: $180.00
--------------------------------
```

---

## 📚 Objetivo del Proyecto

Este proyecto fue desarrollado con fines académicos para practicar:

- Entrada y salida de datos en Python  
- Uso de variables  
- Condicionales (`if`)  
- Operaciones matemáticas  
- Formateo de texto con `f-strings`  

---

## 🚀 Posibles mejoras futuras

- Validación de datos ingresados  
- Manejo de errores con `try-except`  
- Soporte para múltiples productos  
- Interfaz gráfica  
- Registro de ventas en archivo `.csv`  

---

## 👨‍💻 Autor

Luis David Gómez Díaz  