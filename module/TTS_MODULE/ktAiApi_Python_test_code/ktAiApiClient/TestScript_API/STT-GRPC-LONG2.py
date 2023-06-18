import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import time
from ktAiApiSDK.gRPC import gRPC
from TestCommon.conf import config

class bcolors:
    HEADER = '\033[94m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'

def onError(message):
    print(bcolors.ERROR, "[gRPC] onError message: ", message, bcolors.ENDC)
    if message == 'CODE0301':
        gRPC.serviceflag.clear()
        gRPC.releaseConnection()
        print('ReConnection gRpc Server ')

def onResult(message):
    print("[gRPC] onResult message: ", message)


def command(request_text=''):
    gRPC.serviceflag.set()
    sttModelCode = 2
    sampleRate = 8000
    channel = 1

    if request_text == '1':
        print(bcolors.WARNING, "[gRPC] gRPC.startSTT2 sttModelCode: ", sttModelCode, bcolors.ENDC)    
        gRPC.startSTT2(sttModelCode, onError)

    elif request_text == '2':
        fileContent = None
        filePath = "./TestFile/GRPC2.pcm"
        print(bcolors.WARNING, "[gRPC] gRPC.sendAudioData filepath: ", filePath, bcolors.ENDC)
        with open(filePath, mode='rb') as file:
            while 1: 
                fileContent = file.read(sampleRate*channel)
                if len(fileContent) == 0:
                    break
                gRPC.sendAudioData(fileContent, onResult)
                time.sleep(0.1)

    elif request_text == '3':
        print(bcolors.WARNING, "[gRPC] gRPC.stopSTT", bcolors.ENDC)
        gRPC.stopSTT()

    elif request_text == '4':
        print(bcolors.WARNING, "[gRPC] gRPC.releaseConnection", bcolors.ENDC)
        gRPC.releaseConnection()


def main():
    print("[" + os.path.basename(sys.argv[0]).replace(".py", "") + "]")

    client_id = config['api']['clientID']
    client_key = config['api']['apiKey']
    client_secret = config['api']['secret']

    gRPC.setMetaData(client_key, client_id, client_secret)
    print(bcolors.WARNING, '[gRPC server] addr: ', gRPC.grpc_channel.HOST, gRPC.grpc_channel.PORT)
    print(bcolors.WARNING, '[gRPC client] id: ', client_id, bcolors.ENDC)
    print(bcolors.WARNING, '[gRPC client] key: ', client_key, bcolors.ENDC)
    print(bcolors.WARNING, '[gRPC client] secret: ', client_secret, bcolors.ENDC)

    if not gRPC.grpcThread.is_alive():
        gRPC.start_grpc_thread()
    
    command("1")
    time.sleep(1)
    command("2")
    command("3")
    command("4")
    
    print(bcolors.HEADER, "[AI API gRPC Verify TEST] <<< END >>>", bcolors.ENDC)
    exit()
    
if __name__ == "__main__":
	main()
