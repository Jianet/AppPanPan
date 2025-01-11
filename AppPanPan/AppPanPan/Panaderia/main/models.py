from django.db import models
class Producto(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del producto
    descripcion = models.TextField()           # Descripción del producto
    precio = models.DecimalField(max_digits=8, decimal_places=2)  # Precio del producto
    stock = models.PositiveIntegerField()      # Cantidad disponible en inventario
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)  # Imagen del producto (opcional)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)       # Nombre completo del cliente
    correo = models.EmailField(unique=True)         # Correo electrónico
    telefono = models.CharField(max_length=15)      # Número de teléfono
    direccion = models.TextField()                  # Dirección del cliente

    def __str__(self):
        return f"{self.nombre} ({self.correo})"

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relación con Cliente
    productos = models.ManyToManyField(Producto, through='DetallePedido')  # Relación con Producto
    fecha = models.DateTimeField(auto_now_add=True)                 # Fecha del pedido
    total = models.DecimalField(max_digits=10, decimal_places=2)    # Total del pedido

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nombre}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)    # Relación con Pedido
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Relación con Producto
    cantidad = models.PositiveIntegerField()                        # Cantidad de productos
    subtotal = models.DecimalField(max_digits=10, decimal_places=2) # Subtotal (cantidad x precio)

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre} en Pedido {self.pedido.id}"




