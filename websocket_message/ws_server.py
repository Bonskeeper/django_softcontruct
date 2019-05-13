from numpy import random as npr
import asyncio
import websockets

mu, sigma = 0.5, 0.1


async def send_number(websocket, path):
    sequence_number = 1
    while True:
        sended_number = npr.normal(mu, sigma)
        await websocket.send("{},{},{},{}".format(sended_number, sequence_number, mu, sigma))
        sequence_number += 1
        await asyncio.sleep(1)

start_server = websockets.serve(send_number, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()