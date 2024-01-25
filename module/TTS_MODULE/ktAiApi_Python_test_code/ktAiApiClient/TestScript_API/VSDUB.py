import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from TestCommon.conf import config
from TestCommon.conf import bcolors
import json
import base64
from ktAiApiSDK.VSDUB import VSDUB
from pathlib import Path

#-------------------------------------------
# 호출용 데이터 설정
#-------------------------------------------
vsdub_client = VSDUB()
vsdub_client.__init__()
vsdub_client.setAuth(config['api']['apiKey'], config['api']['clientID'], config['api']['secret'])
text = "안녕하세요. 보이스 스튜디오입니다."
speaker = 101
voiceName = ""
pitch = 100
speed = 100
volume = 100
emotion = "happy"
language = "ko"
encoding = "wav"
sampleRate = 16000
file_name = './TestFile/VSDUB.mp3'
audioData = Path(file_name).read_bytes() 

#-------------------------------------------
# 호출
#-------------------------------------------
print("[" + os.path.basename(sys.argv[0]).replace(".py", "") + "]")
print(bcolors.ENDC, "========= 호출정보 =========")
print(bcolors.WARNING, "audioData:", file_name, "text:", text, "speaker:", speaker, "voiceName:", voiceName, "pitch:", pitch, "speed:", speed, "volume:", volume, "emotion:", emotion, "language:", language, "encoding:", encoding, "sampleRate:", sampleRate)
response = vsdub_client.requestVSDUB(audioData, text, speaker, voiceName, pitch, speed, volume, emotion, language, encoding, sampleRate)

#-------------------------------------------
# 결과 출력
#-------------------------------------------
print(bcolors.ENDC, "========= 응답결과 =========")
print(bcolors.HEADER, response)

if response != "" :
    responseObj = json.loads(response)
    if responseObj["statusCode"] == 200 :
        if responseObj["audioData"] != "" :
            file = open('./TestFile_download/VSDUB.mp3', 'wb')
            base64data = base64.b64decode(responseObj["audioData"])
            file.write(base64data)
            file.close()
            print(bcolors.HEADER, "파일 저장 완료")

print(bcolors.ENDC)