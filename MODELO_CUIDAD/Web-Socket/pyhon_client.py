import asyncio
import websockets
import json

from Model.model import model_data
from Model.parameters import param_01


# TODO: Import the model and run the simulation
# TODO: Extract the data from the model
# TODO: Send the data to the server

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

def send_agent_data(data):
    asyncio.run(send_data(data))

if __name__ == "__main__":
    print(model_data)
    for i in range(len(model_data)):
        print(model_data[i])
        send_agent_data(model_data[i])

    # model.run(steps=100, display=False)
    # print(len(model.model_data))

    
    # send_agent_data()
