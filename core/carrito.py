class carrito:
    def __init__(self, reauest):
        self.request = request
        self.session = request.session
        carrito = self.session["carrito"]
        if not carrito:
            self.session["carrito"]={}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado" : producto.costo,
                "cantidad": 1,
            }
        else: 
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += 1


