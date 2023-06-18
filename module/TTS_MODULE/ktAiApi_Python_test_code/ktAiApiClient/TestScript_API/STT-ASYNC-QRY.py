import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from TestCommon.conf import config
from TestCommon.conf import bcolors
from ktAiApiSDK.STT import STT

#-------------------------------------------
# 호출용 데이터 설정
#-------------------------------------------
stt_client = STT()
stt_client.__init__()
stt_client.setAuth(config['api']['apiKey'], config['api']['clientID'], config['api']['secret'])
transactionId = "transactionId 입력"

#-------------------------------------------
# 호출
#-------------------------------------------
print("[" + os.path.basename(sys.argv[0]).replace(".py", "") + "]")
print(bcolors.ENDC, "========= 호출정보 =========")
print(bcolors.WARNING, "transactionId:", transactionId)
response = stt_client.querySTT(transactionId)
print(bcolors.ENDC, "========= 응답결과 =========")
print(bcolors.HEADER, response)

print(bcolors.ENDC)