import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from TestCommon.conf import config
from TestCommon.conf import bcolors
from ktAiApiSDK.GENIEMEMO import GENIEMEMO

#-------------------------------------------
# 호출용 데이터 설정
#-------------------------------------------
geniememoasync_client = GENIEMEMO()
geniememoasync_client.__init__()
geniememoasync_client.setAuth(config['api']['apiKey'], config['api']['clientID'], config['api']['secret'])
callKey = "callKey 입력"
callIndex = 0

#-------------------------------------------
# 호출
#-------------------------------------------
print("[" + os.path.basename(sys.argv[0]).replace(".py", "") + "]")
print(bcolors.ENDC, "========= 호출정보 =========")
print(bcolors.WARNING, "callKey:", callKey, "callIndex:", callIndex)
response = geniememoasync_client.queryGENIEMEMOASYNC(callKey, callIndex)

#-------------------------------------------
# 결과 출력
#-------------------------------------------
print(bcolors.ENDC, "========= 응답결과 =========")
print(bcolors.HEADER, response)

print(bcolors.ENDC)