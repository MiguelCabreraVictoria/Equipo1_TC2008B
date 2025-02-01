import asyncio
import websockets


connected_clients = set()

async def ws_server(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in connected_clients:
                # Enviar el mensaje a todos los clientes conectados excepto a quien lo envió
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed")
    finally:
        connected_clients.remove(websocket)

async def send_message():
    # Generar handshake
    server = await websockets.serve(ws_server, "localhost", 8765)
    print("Servidor WebSocket corriendo en ws://localhost:8765")
    # Esperar a que el servidor se cierre
    await server.wait_closed()


asyncio.run(send_message())