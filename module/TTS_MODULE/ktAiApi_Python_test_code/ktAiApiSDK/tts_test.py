import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import grpc_channel
import json
import base64
import TTS

#-------------------------------------------
# 호출용 데이터 설정
#-------------------------------------------
tts_client = TTS()
tts_client.__init__()
tts_client.setAuth(config['api']['apiKey'], config['api']['clientID'], config['api']['secret'])
text = "연출아 운동가야지"
pitch = -1
speed = -1
speaker = 1
volume = -1
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
print(bcolors.WARNING, "text:", text, "pitch:", pitch, "speed:", speed, "speaker:", speaker, "volume:", volume, "language:", language, "encoding:", encoding, "channel:", channel, "sampleRate:", sampleRate, "sampleFmt:", sampleFmt)
response = tts_client.requestTTS(text, pitch, speed, speaker, volume, language, encoding, channel, sampleRate, sampleFmt)

#-------------------------------------------
# 결과 출력
#-------------------------------------------
print(bcolors.ENDC, "========= 응답결과 =========")
print(bcolors.HEADER, response)

if response != "" :
    responseObj = json.loads(response)
    if responseObj["statusCode"] == 200 :
        if responseObj["audioData"] != "" :
            file = open('./TTS.mp3', 'wb')
            base64data = base64.b64decode(responseObj["audioData"])
            file.write(base64data)
            file.close()
            print(bcolors.HEADER, "파일 저장 완료")

print(bcolors.ENDC)