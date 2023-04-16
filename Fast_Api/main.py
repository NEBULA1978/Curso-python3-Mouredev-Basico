from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# Este código crea una instancia de FastAPI y define dos rutas:

#     La ruta raíz (/) devuelve un saludo simple en formato JSON.
#     La ruta / items/{item_id} recibe dos parámetros: item_id(un número entero) y q(un string opcional). Devuelve un objeto JSON con estos valores.

#     Ejecutar la aplicación:

# En la terminal, navega al directorio donde se encuentra tu archivo main.py y ejecuta el siguiente comando para iniciar el servidor Uvicorn:

# css

# uvicorn main: app - -reload

# Esto iniciará el servidor en http: // 127.0.0.1: 8000/. Puedes visitar esta dirección en tu navegador para ver la respuesta de la ruta raíz.

# Probar la API:

# FastAPI genera automáticamente un esquema de OpenAPI y una interfaz de usuario interactiva con Swagger UI. Puedes visitar http: // 127.0.0.1: 8000/docs en tu navegador para explorar y probar tu API.

# Ahora que tienes una aplicación FastAPI básica en funcionamiento, puedes continuar desarrollando y agregando más rutas y funcionalidades según las necesidades de tu proyecto. Consulta la documentación oficial de FastAPI para obtener más información y ejemplos.
