import asyncio
import websockets
from datetime import datetime
import logging

logging.basicConfig(format='%(name)s - %(levelname)s : %(message)s', level=logging.INFO)
logger_ws_client = logging.getLogger('ws_client')


async def recv_hand_message():
    async with websockets.connect('ws://localhost:8765') as websocket:
        while True:
            number_seqnuber = await websocket.recv()
            number = float(number_seqnuber.split(',')[0])
            sequence_number = int(number_seqnuber.split(',')[1])
            mu = float(number_seqnuber.split(',')[2])
            sigma = float(number_seqnuber.split(',')[3])
            if number > mu:
                deviation = number - mu
            else:
                deviation = mu - number

            if deviation > sigma * 2:
                logger_ws_client.info("Time - {}, number - {}, sequence_number - {}".format(datetime.today(), number, sequence_number))


asyncio.get_event_loop().run_until_complete(recv_hand_message())
asyncio.get_event_loop().run_forever()