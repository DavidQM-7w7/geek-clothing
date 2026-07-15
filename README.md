# Geek Clothing

## Descripción

Geek Clothing es un proyecto para la gestión de una tienda de ropa geek que utiliza MongoDB Atlas como base de datos y una API REST desarrollada en Python con Flask.

La aplicación permite administrar las siguientes colecciones mediante operaciones CRUD:

- Usuarios
- Marcas
- Prendas
- Ventas

Además, incorpora consultas de agregación para la generación de reportes estadísticos sobre las ventas y el inventario.

## Tecnologías utilizadas

- MongoDB Atlas
- MongoDB Compass
- Python
- Flask
- PyMongo
- Postman
- Visual Studio Code
- Git
- GitHub
- Markdown

## Estructura del proyecto

```text
Geek-Clothing/
│
├── API/
│   └── api/
│       └── v1/
│           ├── app/
│           │   ├── controllers/
│           │   │   ├── marcas.py
│           │   │   ├── prendas.py
│           │   │   ├── reportes.py
│           │   │   ├── usuarios.py
│           │   │   └── ventas.py
│           │   │
│           │   ├── models/
│           │   │   ├── marca.py
│           │   │   ├── prenda.py
│           │   │   ├── venta.py
│           │   │   └── usuario.py
│           │   │
│           │   ├── database.py
│           │   ├── __init__.py
│           │   └── index.py
│           │
│           ├── requirements.txt
│           └── run.py
│
├── database/
│   ├── geek_clothingdb.js
│   ├── usuarios.json
│   ├── marcas.json
│   ├── prendas.json
│   └── ventas.json
│
└── README.md
```

## Instalación

1. Clonar el repositorio.

```bash
git clone https://github.com/DavidQM-7w7/geek-clothing.git
```

2. Ingresar al proyecto.

```bash
cd geek-clothing/API/api/v1
```

3. Activar el entorno virtual.

```powershell
.\venv\Scripts\Activate
```

4. Instalar las dependencias.

```bash
pip install -r requirements.txt
```

5. Ejecutar la API.

```bash
python run.py
```

La API estará disponible en:

```
http://127.0.0.1:5000
```

![Texto alternativo](Evidencias/Entorno-virtual.png)

---

## API REST

### Usuarios

### Obtener todos los usuarios

**Método**

GET

**URL**

```
http://127.0.0.1:5000/api/v1/usuarios
```

![Texto alternativo](Evidencias/Obtener-usuarios.png)

---

### Obtener usuario por ID

**Método**

GET

**URL**

```
http://127.0.0.1:5000/api/v1/usuarios/1
```

![Texto alternativo](Evidencias/Usuario1.png)

---

### Insertar usuario

**Método**

POST

**URL**

```
http://127.0.0.1:5000/api/v1/usuarios
```

**Ejemplo Body**

```json
{
    "_id":11,
    "nombre":"Hugo Ramírez",
    "correo":"hugo.ramirez@geek-clothing.com",
    "telefono":"81112222",
    "fechaRegistro":"2026-08-12"
}
```

![Texto alternativo](Evidencias/Agregar-usuario.png)

---

### Actualizar usuario

**Método**

PUT

**URL**

```
http://127.0.0.1:5000/api/v1/usuarios/11
```

![Texto alternativo](Evidencias/Actualizar-usuario.png)

---

### Eliminar usuario

**Método**

DELETE

**URL**

```
http://127.0.0.1:5000/api/v1/usuarios/11
```

![Texto alternativo](Evidencias/Eliminar-usuario.png)

![Texto alternativo](Evidencias/Usuario-inexistente.png)

---

### Marcas

### Obtener todas las marcas

**Método**

GET

**URL**

```
http://127.0.0.1:5000/api/v1/marcas
```

![Texto alternativo](Evidencias/Obtener-marcas.png)

---

### Obtener marca por ID

**Método**

GET

**URL**

```
http://127.0.0.1:5000/api/v1/marcas/1
```

![Texto alternativo](Evidencias/Marca1.png)

---

### Insertar marca

**Método**

POST

**URL**

```
http://127.0.0.1:5000/api/v1/marcas
```

**Ejemplo Body**

```json
{
    "_id": 11,
    "nombre": "CyberStyle",
    "pais": "Corea del Sur",
    "colaboracion": "Solo Leveling"
}
```

![Texto alternativo](Evidencias/Agregar-marca.png)

---

### Actualizar marca

**Método**

PUT

**URL**

```
http://127.0.0.1:5000/api/v1/marcas/11
```

![Texto alternativo](Evidencias/Actualizar-marca.png)

---

### Eliminar marca

**Método**

DELETE

**URL**

```
http://127.0.0.1:5000/api/v1/marcas/11
```

![Texto alternativo](Evidencias/Eliminar-marca.png)

![Texto alternativo](Evidencias/Marca-inexistente.png)

---

### Prendas

### Obtener todas las prendas

**Método**

GET

**URL**

```
http://127.0.0.1:5000/api/v1/prendas
```

![Texto alternativo](Evidencias/Obtener-prendas.png)

---

### Obtener prenda por ID

**Método**

GET

**URL**

```
http://127.0.0.1:5000/api/v1/prendas/1
```

![Texto alternativo](Evidencias/Prenda1.png)

---

### Insertar prenda

**Método**

POST

**URL**

```
http://127.0.0.1:5000/api/v1/prendas
```

**Ejemplo Body**

```json
{
    "_id": 11,
    "nombre": "Sudadera Kaiju",
    "marcaId": 6,
    "categoria": "Sudaderas",
    "precio": 38000,
    "stock": 18
}
```

![Texto alternativo](Evidencias/Agregar-prenda.png)

---

### Actualizar prenda

**Método**

PUT

**URL**

```
http://127.0.0.1:5000/api/v1/prendas/11
```

![Texto alternativo](Evidencias/Actualizar-prenda.png)

---

### Eliminar prenda

**Método**

DELETE

**URL**

```
http://127.0.0.1:5000/api/v1/prendas/11
```

![Texto alternativo](Evidencias/Eliminar-prenda.png)

![Texto alternativo](Evidencias/Prenda-inexistente.png)

---

### Ventas

### Obtener todas las ventas

**Método**

GET

**URL**

```
http://127.0.0.1:5000/api/v1/ventas
```

![Texto alternativo](Evidencias/Obtener-ventas.png)

---

### Obtener venta por ID

**Método**

GET

**URL**

```
http://127.0.0.1:5000/api/v1/ventas/1
```

![Texto alternativo](Evidencias/Venta1.png)

---

### Insertar venta

**Método**

POST

**URL**

```
http://127.0.0.1:5000/api/v1/ventas
```

**Ejemplo Body**

```json
{
    "_id": 11,
    "usuarioId": 3,
    "fecha": "2026-08-25",
    "detalle": [
        {
            "prendaId": 4,
            "cantidad": 2
        }
    ],
    "total": 72000
}
```

![Texto alternativo](Evidencias/Agregar-venta.png)

---

### Actualizar venta

**Método**

PUT

**URL**

```
http://127.0.0.1:5000/api/v1/ventas/11
```

![Texto alternativo](Evidencias/Actualizar-venta.png)

---

### Eliminar venta

**Método**

DELETE

**URL**

```
http://127.0.0.1:5000/api/v1/ventas/11
```

![Texto alternativo](Evidencias/Eliminar-venta.png)

![Texto alternativo](Evidencias/Venta-inexistente.png)

---

## Reportes

## Marcas con al menos una venta

**Método**

GET

**URL**

```
http://127.0.0.1:5000/api/v1/reportes/marcas-con-ventas
```

![Texto alternativo](Evidencias/Marcas-con-ventas.png)

---

## Prendas vendidas con stock restante

**Método**

GET

**URL**

```
http://127.0.0.1:5000/api/v1/reportes/prendas-stock
```

![Texto alternativo](Evidencias/Prendas-stock.png)

---

## Top 5 marcas más vendidas

**Método**

GET

**URL**

```
http://127.0.0.1:5000/api/v1/reportes/top5-marcas
```

![Texto alternativo](Evidencias/Top5-marcas.png)

---

## Pruebas realizadas

La API fue validada mediante Postman verificando el correcto funcionamiento de:

- CRUD de Usuarios.
- CRUD de Marcas.
- CRUD de Prendas.
- CRUD de Ventas.
- Reporte de marcas con al menos una venta.
- Reporte de prendas vendidas con stock restante.
- Reporte del Top 5 de marcas más vendidas.

Todas las pruebas fueron ejecutadas satisfactoriamente mediante Postman utilizando MongoDB Atlas como base de datos.

---

## Autor

David Quesada Mata

## Profesor

Daniel Bogarín Granados