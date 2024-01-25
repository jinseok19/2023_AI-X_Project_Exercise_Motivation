import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from TestCommon.conf import config
from TestCommon.conf import bcolors
from ktAiApiSDK.STT import STT
from pathlib import Path

#-------------------------------------------
# 호출용 데이터 설정
#-------------------------------------------
stt_client = STT()
stt_client.__init__()
stt_client.setAuth(config['api']['apiKey'], config['api']['clientID'], config['api']['secret'])
file_name = './TestFile/STT.mp3'
audioData = Path(file_name).read_bytes() 
encoding = "mp3"
sttModelCode = 5

#-------------------------------------------
# 호출
#-------------------------------------------
print("[" + os.path.basename(sys.argv[0]).replace(".py", "") + "]")
print(bcolors.ENDC, "========= 호출정보 =========")
print(bcolors.WARNING, "audioData:", file_name, "encoding:", encoding, "sttModelCode:", sttModelCode)
response = stt_client.requestSTT2(audioData, encoding, sttModelCode)
print(bcolors.ENDC, "========= 응답결과 =========")
print(bcolors.HEADER, response)

print(bcolors.ENDC)