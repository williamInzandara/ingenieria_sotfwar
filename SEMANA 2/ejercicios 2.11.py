class CalcularPagoAlberca:
    def calcularPagoAlberca(self, ancho, largo, profundidad, precioPorMetroCubico):
        volumen = ancho * largo * profundidad
        
        totalPago = volumen * precioPorMetroCubico
        
        return totalPago

    def ejecutar(self):
        ancho = int(input("Ingresa el ancho de la alberca (en metros): "))
        largo = int(input("Ingresa el largo de la alberca (en metros): "))
        profundidad = int(input("Ingresa la profundidad de la alberca (en metros): "))
        precioPorMetroCubico = int(input("Ingresa el precio por metro cúbico de agua: "))

        total = self.calcularPagoAlberca(ancho, largo, profundidad, precioPorMetroCubico)
        print(f"El total a pagar por llenar la alberca es: ${total:.2f}")

pago = CalcularPagoAlberca()
pago.ejecutar()
