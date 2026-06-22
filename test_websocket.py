# test_ws.py

import asyncio
import websockets

async def main():

    async with websockets.connect(
        "ws://localhost:8000/ws/albie123"
    ) as ws:

        await ws.send("hello")

        response = await ws.recv()

        print(response)

asyncio.run(main())