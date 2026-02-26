print("Sistema básico de registro de ventas - RiwiTechStore")

nombre_cliente = input("Ingresar el nombre del cliente:")

precio_unitario = float(input("Ingrese el precio unitario del producto:"))
cantidad = int(input("Ingrese la cantidad de productos comprados:"))

vip_input = input("¿El cliente cuenta con alguna membresía VIP? (si/no): ").strip().lower()

es_vip = vip_input == "si"

subtotal = precio_unitario * cantidad

descuento = 0.0
if es_vip:
    descuento = subtotal * 0.10  
total_final = subtotal - descuento

print("\n----- RESUMEN DE LA VENTA -----")
print(f"Cliente: {nombre_cliente}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total final a pagar: ${total_final:.2f}")
print("--------------------------------")