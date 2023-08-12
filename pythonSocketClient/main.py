import asyncio
import websockets
from FakerPython.faake import *
import time
import json

# Bring your packages onto the path
import sys, os


sys.path.append(os.path.abspath(os.path.join('..', 'Emisor')))
sys.path.append(os.path.abspath(os.path.join('..', 'Receptor')))

import Emisor
import Receptor


async def receive_messages(websocket):
    try:
        while True:
            print("Waiting for message...")
            data = await websocket.recv()
            data = json.loads(data)
            
            
            
            binaryMessage = data["hammingCode"]
            r = data["r"]
            correction = Receptor.detectError(binaryMessage,r)
            res = ""
            if(correction==0):
                print("There is no error in the received message.")
                res= "There is no error in the received message."
            else:
                print("The position of error is ",len(binaryMessage)-correction,"from the left")
                res= "The position of error is "+str(len(binaryMessage)-correction)+" from the left"
    
            # append data to a csv file
            with open('dataFalse.csv', 'a') as f:
                # set header
                if os.stat("dataFalse.csv").st_size == 0:
                    f.write("originalMessage,asciiBinary,hammingCode,Error index,result of error,noiseApplied\n")
                f.write(data["originalMessage"]+","+data["asciiBinary"]+","+data["hammingCode"]+","+str(correction)+","+res+","+str(data["noiseApplied"])+"\n")
    except websockets.exceptions.ConnectionClosed:
        print("WebSocket connection closed.")


async def send_messages(websocket):
    cont = 0
    while cont<10000:
        # solicitar mensaje
        message = await asyncio.get_event_loop().run_in_executor(None, getRandomSentence)
        
        # encriptar mensaje
        encryptedMessage = await asyncio.get_event_loop().run_in_executor(None, Emisor.codificarStringToBinaryAscii, message)
        
        
        # calcular integridad
        hammingCode,r = await asyncio.get_event_loop().run_in_executor(None, Emisor.compute_hamming_code, encryptedMessage)
        print("sending message: ", hammingCode)
        data = {
            "originalMessage": message,
            "asciiBinary": encryptedMessage,
            "hammingCode": hammingCode,
            "r": r,
        }

        await websocket.send(json.dumps(data))
        cont+=1
        # time.sleep(2)
        # print(f"Sent message: {message}")

async def main(isEmisor):
    uri = "ws://localhost:8080"
    async with websockets.connect(uri) as websocket:
        if isEmisor:
            await send_messages(websocket)
        else:
            await receive_messages(websocket)

if __name__ == "__main__":
    emisor = input("Do you want to be a sender or a receiver? [s|r]: ")
    flag = False
    while not flag:
        if emisor == "s":
            flag = True
            asyncio.run(main(True))
        elif emisor == "r":
            flag = True
            asyncio.run(main(False))
        else:
            print("Please enter a valid option.")
            emisor = input("Do you want to be a sender or a receiver? [s|r]: ")
