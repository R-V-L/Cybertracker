import json
from bs4 import BeautifulSoup
from get_url_info import get_response

def obtener_articulos(Producto, urls: list):
    respuestas = []
    response_urls = get_response(urls)
    for response in response_urls:
        soup = BeautifulSoup(response, 'lxml')
        detalles_producto = soup.find('script', type='application/json', id='cp-details-view-data')
        archivo_json = json.loads(detalles_producto.text)
        id_producto = archivo_json['articleId']
        titulo = archivo_json['article']['title']
        precio = archivo_json['article']['price']
        url = archivo_json['article']['link']
        precio_especial = archivo_json['article']['tPrice']
        existencias = archivo_json['article']['stock']
        envio = archivo_json['article']['shipping']
        es_oferta = archivo_json['article']['isOffer']
        foto = archivo_json['article']['pictures'][0]
        categoria = archivo_json['article']['category']['title']
        respuestas.append(Producto(id_producto, titulo, precio, url,
                                  precio_especial, existencias, envio, es_oferta, foto, categoria))
    return respuestas