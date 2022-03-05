import sqlite3
from datetime import datetime

localizacion_base_datos = r"./db/data.db"

def crear_tablas():
    with sqlite3.connect(localizacion_base_datos) as conexion:
        cursor = conexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS PRODUCTOS (
                    PRO_PRODUCTO_ID INTEGER PRIMARY_KEY UNIQUE,
                    PRO_PAGINA_ID INTEGER NOT NULL,
                    PRO_ID_ARTICULO TEXT,
                    PRO_TITULO TEXT NOT NULL,
                    PRO_URL TEXT NOT NULL,
                    PRO_FOTO TEXT,
                    PRO_CAGEGORIA INTEGER,
                    PRO_FECHA TEXT NOT NULL,
                    FOREIGN KEY(PRO_PAGINA_ID) REFERENCES PAGINAS(PAG_PAGINA_ID)
                )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS CATEGORIAS (
                   CAT_CATEGORIA_ID INTEGER PRIMARY_KEY UNIQUE,
                   CAT_PAGINA_ID INTEGER,
                   CAT_NOMBRE TEXT,             
                   CAT_FECHA TEXT,
                   FOREIGN KEY(CAT_PAGINA_ID) REFERENCES PAGINAS(PAG_PAGINA_ID))''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS PAGINAS (
                   PAG_PAGINA_ID INTEGER PRIMARY_KEY UNIQUE,
                   PAG_NOMBRE TEXT NOT NULL,
                   PAG_FOTO TEXT,
                   PAG_FECHA TEXT NOT NULL)''')

def insertar_pagina(nombre, foto_url):
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with sqlite3.connect(localizacion_base_datos) as conexion:
            cursor = conexion.cursor()
            try:
                id = cursor.execute("SELECT MAX(PAG_PAGINA_ID) FROM PAGINAS").fetchone()[0] + 1
            except:
                id = 1
            cursor.execute(
                f"INSERT INTO PAGINAS VALUES ({id}, '{nombre}', '{foto_url}', '{fecha_actual}')")
        return True
    except Exception as e:
        return False

def insertar_categoria(nombre, pagina_id):
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with sqlite3.connect(localizacion_base_datos) as conexion:
            cursor = conexion.cursor()
            try:
                id = cursor.execute(
                    "SELECT MAX(CAT_CATEGORIA_ID) FROM CATEGORIAS").fetchone()[0] + 1
            except:
                id = 1
            cursor.execute(
                f"INSERT INTO CATEGORIAS VALUES ({id}, {pagina_id}, '{nombre}', '{fecha_actual}')")
        return True
    except Exception as e:
        return False

def ver_info_tablas():
    with sqlite3.connect(localizacion_base_datos) as conexion:
        cursor = conexion.cursor()
        for row in cursor.execute('SELECT * FROM PRODUCTOS').fetchall():
            print(row)
        for row in cursor.execute('SELECT * FROM CATEGORIAS').fetchall():
            print(row)
        for row in cursor.execute('SELECT * FROM PAGINAS').fetchall():
            print(row)

if __name__ == '__main__':
    crear_tablas()
    test = insertar_pagina('CYBERPUERTA',
          'https://www.cyberpuerta.mx/out/cyberpuertaV5/img/logo2.png')
