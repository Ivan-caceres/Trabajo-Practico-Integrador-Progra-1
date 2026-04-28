print("Sistema de facturación de Agua Potable - Gotita S.A")

cargo_fijo = 7000
costo_por_metro = 200
iva = .21

metros_consumidos = float(input("Ingrese los metros cúbicos consumidos: ")) #20
tipo_cliente = input("Ingrese tipo de cliente (Residencial - Comercial - Industrial): ")


subtotal_consumo = metros_consumidos * costo_por_metro #400

bonificacion = 0
recargo = 0

total_sin_descuento_sin_recargo = subtotal_consumo + cargo_fijo


if tipo_cliente == "Residencial":
    if metros_consumidos < 30:
        bonificacion = subtotal_consumo * 0.1 
    elif metros_consumidos > 80:
        recargo = subtotal_consumo * 0.15

    if total_sin_descuento_sin_recargo < 35000:
        bonificacion *= 0.95


elif tipo_cliente == "Comercial":
    if metros_consumidos > 300:
        bonificacion = subtotal_consumo * 0.12
    elif metros_consumidos > 150:
        bonificacion = subtotal_consumo * 0.08
    elif metros_consumidos < 50:
        recargo = subtotal_consumo * 0.05


elif tipo_cliente == "Industrial":
    if metros_consumidos > 1000:
        bonificacion = subtotal_consumo * 0.3
    elif metros_consumidos > 500:
        bonificacion = subtotal_consumo * 0.2
    elif metros_consumidos < 200:
        recargo = subtotal_consumo * 0.1


else:
    print("Tipo de cliente no contemplado.")


subtotal_final = total_sin_descuento_sin_recargo - bonificacion + recargo
total_con_iva = subtotal_final * iva

total_final = subtotal_final + total_con_iva

print(f"Tipo cliente: {tipo_cliente}")
print(f"Metros consumidos: {metros_consumidos}")
print(f"Bonificación: {bonificacion}")
print(f"Recargo: {recargo}")
print(f"Subtotal consumo: {subtotal_consumo}")
print(f"Subtotal con recargos y bonificaciones: {subtotal_final}")
print(f"IVA aplicado (si corresponde): {total_con_iva}")
print(f"Total a pagar: {total_final}")