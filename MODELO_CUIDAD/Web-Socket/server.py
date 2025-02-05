import asyncio
import websockets

connected_clients = set()

async def ws_server(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in connected_clients:
                print(f"Received: {message}")
                if client != websocket:  # No enviar el mensaje al remitente
                    await client.send(message)
                    print(f'{message} enviado a {client}')
    except websockets.exceptions.ConnectionClosed:
        print("Connection closed")
    finally:
        connected_clients.remove(websocket)

async def main():
    # Generar handshake
    server = await websockets.serve(ws_server, "localhost", 8765)
    print("Servidor WebSocket corriendo en ws://localhost:8765")
    # Esperar a que el servidor se cierre
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
