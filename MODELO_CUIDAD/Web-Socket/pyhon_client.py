import asyncio
import websockets
import json

async def send_data():
    try:
        async with websockets.connect('ws://localhost:8765') as websocket:
            while True:
                message = json.dumps({"message": "Python Client connected"})
                await websocket.send(message)
                # print(f"Sent: {message}")
                await asyncio.sleep(2)
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed: {e}")
    except Exception as e:
        print(f"Error: {e}")

def send_agent_data():
    asyncio.run(send_data())

if __name__ == "__main__":
    send_agent_data()
