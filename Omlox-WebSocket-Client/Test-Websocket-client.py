import asyncio
import websockets
import json


async def test():
    async with websockets.connect('ws://192.168.8.1:8090/json/device/all/position') as websocket:
        response = await websocket.recv()
        obj = json.loads(response.txt)
        x = len(obj)
        print(x)
        print(obj[0])
        #pras = json.dumps(obj, indent=4, sort_keys=True)
        #print(pras)
        #Y = parsed["payload"]
        with open('omlox.json', 'w') as json_file:
            json.dump(obj, json_file)
while True:
    asyncio.get_event_loop().run_until_complete(test())
