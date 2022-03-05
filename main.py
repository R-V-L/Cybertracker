import cyberpuerta
from urllib.parse import urlparse

class Producto:
    def __init__(self, id_producto, titulo, precio, url, precio_especial, existencias, envio, es_oferta, foto, categoria):
        self.id_producto = id_producto
        self.titulo = titulo
        self.precio = precio
        self.url = url
        self.precio_especial = precio_especial
        self.existencias = existencias
        self.envio = envio
        self.es_oferta = es_oferta
        self.foto = foto
        self.categoria = categoria

urls = ["https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Tarjetas-de-Video/MSI-GeForce-210-1GB-GDDR3-DVI-VGA-HDCP-PCI-Express-2-0.html",
        "https://www.cyberpuerta.mx/Punto-de-Venta-POS/Lectores-y-Terminales/Lectores-de-Codigo-de-Barras/Zebra-LI4278-Lector-de-Codigo-de-Barras-1D-no-incluye-Cable-USB-ni-Base.html",
        "https://www.cyberpuerta.mx/Energia/Proteccion-Contra-Descargas/Reguladores-de-Voltaje/Regulador-Koblenz-RS-1410-700W-1410VA-Salida-108-132V-8-Contactos.html"]

test = cyberpuerta.obtener_articulos(Producto, urls)

for elemento in test:
    print(f'{elemento.categoria}')
