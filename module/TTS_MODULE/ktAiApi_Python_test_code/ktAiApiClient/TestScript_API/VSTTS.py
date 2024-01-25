import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from TestCommon.conf import config
from TestCommon.conf import bcolors
import json
import base64
from ktAiApiSDK.VSTTS import VSTTS

#-------------------------------------------
# 호출용 데이터 설정
#-------------------------------------------
vstts_client = VSTTS()
vstts_client.__init__()
vstts_client.setAuth(config['api']['apiKey'], config['api']['clientID'], config['api']['secret'])
text = "안녕하세요. 신비한 화가들입니다."
speaker = 100
voiceName = ""
pitch = 100
speed = 100
volume = 100
emotion = "neutral"
language = "ko"
encoding = "wav"
channel = 1
sampleRate = 16000
sampleFmt = "S16LE"

#-------------------------------------------
# 호출
#-------------------------------------------
print("[" + os.path.basename(sys.argv[0]).replace(".py", "") + "]")
print(bcolors.ENDC, "========= 호출정보 =========")
print(bcolors.WARNING, "text:", text, "speaker:", speaker, "voiceName:", voiceName, "pitch:", pitch, "speed:", speed, "volume:", volume, "emotion:", emotion, "language:", language, "encoding:", encoding, "channel:", channel, "sampleRate:", sampleRate, "sampleFmt:", sampleFmt)
response = vstts_client.requestVSTTS(text, speaker, voiceName, pitch, speed, volume, emotion, language, encoding, channel, sampleRate, sampleFmt)

#-------------------------------------------
# 결과 출력
#-------------------------------------------
print(bcolors.ENDC, "========= 응답결과 =========")
print(bcolors.HEADER, response)

if response != "" :
    responseObj = json.loads(response)
    if responseObj["statusCode"] == 200 :
        if responseObj["audioData"] != "" :
            file = open('./TestFile_download/VSTTS.mp3', 'wb')
            base64data = base64.b64decode(responseObj["audioData"])
            file.write(base64data)
            file.close()
            print(bcolors.HEADER, "파일 저장 완료")

print(bcolors.ENDC)