import asyncio
import websockets
import json

from Model.model import model_data

async def send_data(data):
    try:
        async with websockets.connect('ws://localhost:8765') as websocket:
            while True:
                message = json.dumps(data)
                await websocket.send(message)
                print(f"Sent: {message}")
                await asyncio.sleep(2)
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed: {e}")
    except Exception as e:
        print(f"Error: {e}")

async def send_data(data):
    try:
        async with websockets.connect('ws://localhost:8765') as websocket:
            for d in data:
                message = json.dumps(d)
                await websocket.send(message)
                print(f"Sent: {message}")
                await asyncio.sleep(2)
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed: {e}")
    except Exception as e:
        print(f"Error: {e}")

def send_agent_data(data):
    asyncio.run(send_data(data))

if __name__ == "__main__":
        send_agent_data(model_data)

    

   

    
    # send_agent_data()
