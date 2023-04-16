from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat en tiempo real con FastAPI</title>
    </head>
    <body>
        <h1>Chat en tiempo real con FastAPI</h1>
        <form id="messageForm" action="javascript:void(0);">
            <input type="text" id="messageInput" autocomplete="off" placeholder="Escribe un mensaje..."/>
            <button>Enviar</button>
        </form>
        <ul id="messages"></ul>
        <script>
            const ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = (event) => {
                const messageElement = document.createElement("li");
                messageElement.innerText = event.data;
                document.getElementById("messages").appendChild(messageElement);
            };
            document.getElementById("messageForm").addEventListener("submit", (event) => {
                event.preventDefault();
                const message = document.getElementById("messageInput").value;
                ws.send(message);
                document.getElementById("messageInput").value = "";
            });
        </script>
    </body>
</html>
"""

connected_websockets: List[WebSocket] = []


async def broadcast_message(message: str):
    """
    Send a message to all connected WebSockets.

    Args:
        message (str): The message to be broadcasted.
    """
    for websocket in connected_websockets:
        await websocket.send_text(message)


@app.get("/")
def get():
    """
    Serve the chat HTML page.
    
    Returns:
        HTMLResponse: The chat HTML page.
    """
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint to handle chat connections and messages.

    Args:
        websocket (WebSocket): The WebSocket instance for the connected client.
    """
    await websocket.accept()
    connected_websockets.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await broadcast_message(f"Mensaje: {data}")
    except WebSocketDisconnect:
        connected_websockets.remove(websocket)


# Con estos cambios, el código ahora mantiene una lista de connected_websockets, que contiene todos los WebSockets conectados. Cuando un cliente envía un mensaje, este se transmite a todos los WebSockets conectados utilizando la función broadcast_message. Además, si un cliente se desconecta, su WebSocket se elimina de la lista connected_websockets.

# Guarda los cambios en main.py y reinicia el servidor FastAPI ejecutando uvicorn main: app - -reload. Ahora, cuando abras dos chats en diferentes pestañas o navegadores y envíes un mensaje desde uno de ellos, deberías ver el mensaje en ambos chats.
# ///////////////////////////
# ///////////////////////////

# EJEJMPLO

# from fastapi import FastAPI, WebSocket
# from fastapi.responses import HTMLResponse

# app = FastAPI()

# html = """
# <!DOCTYPE html>
# <html>
#     <head>
#         <title>Chat en tiempo real con FastAPI</title>
#     </head>
#     <body>
#         <h1>Chat en tiempo real con FastAPI</h1>
#         <form id="messageForm" action="javascript:void(0);">
#             <input type="text" id="messageInput" autocomplete="off" placeholder="Escribe un mensaje..."/>
#             <button>Enviar</button>
#         </form>
#         <ul id="messages"></ul>
#         <script>
#             const ws = new WebSocket("ws://localhost:8000/ws");
#             ws.onmessage = (event) => {
#                 const messageElement = document.createElement("li");
#                 messageElement.innerText = event.data;
#                 document.getElementById("messages").appendChild(messageElement);
#             };
#             document.getElementById("messageForm").addEventListener("submit", (event) => {
#                 event.preventDefault();
#                 const message = document.getElementById("messageInput").value;
#                 ws.send(message);
#                 document.getElementById("messageInput").value = "";
#             });
#         </script>
#     </body>
# </html>
# """


# @app.get("/")
# def get():
#     return HTMLResponse(html)


# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(f"Mensaje: {data}")

# Ejecutar el servidor Uvicorn:       
# uvicorn main: app - -reload

# //////////////////////////////////////////
# //////////////////////////////////////////

# EJEMPLO2
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}


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
