import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from TestCommon.conf import config
from TestCommon.conf import bcolors
from ktAiApiSDK.GENIEMEMO import GENIEMEMO
from pathlib import Path

#-------------------------------------------
# 호출용 데이터 설정
#-------------------------------------------
geniememoasync_client = GENIEMEMO()
geniememoasync_client.__init__()
geniememoasync_client.setAuth(config['api']['apiKey'], config['api']['clientID'], config['api']['secret'])
callKey = "callKey 입력"
file_name = './TestFile/GENIEMEMO.wav'
audioData = Path(file_name).read_bytes()

#-------------------------------------------
# 호출
#-------------------------------------------
print("[" + os.path.basename(sys.argv[0]).replace(".py", "") + "]")
print(bcolors.ENDC, "========= 호출정보 =========")
print(bcolors.WARNING, "audioData:", file_name, "callKey:", callKey)
response = geniememoasync_client.requestGENIEMEMOASYNC(audioData, callKey)
print(bcolors.ENDC, "========= 응답결과 =========")
print(bcolors.HEADER, response)

print(bcolors.ENDC)