# Intermediate_Level_Project_for_AI-X
🤖AI+X 선도 인재 양성 중급 프로젝트 with KT & 상명대학교🤖

# Chat Gpt API를 활용한 운동 동기부여 TTS bot 및 Chat bot 서비스 개발

## Function
운동 전/중/후/로 나누고, 운동 기록이 없으면 운동 전으로 간주하여, 그에 맞는 동기부여를 제공 운동 전, 중은 chat gpt API를 이용해 상황에 맞는 적절한 prompt가 나오게 하여 그 응답을 TTS API를 사용해 음성 알림을 제공 운동 후는 Chat gpt API를 이용해 사용자가 운동 후 다짐이와 대화를 나누며 운동을 기록하고, 동기부여를 제공받아 다음 목표를 설정할 수 있도록 도와줌.
___
### Files
```bash
├── module
│   ├── TTS_MODULE
│   │    ├── After_tts(운동 후 동기부여 대사)
│   │    ├── Before_tts(운동 전 동기부여 대사)
│   │    ├── Progress_tts(운동 중 동기부여 대사)
│   │    └── TTS_Create.py(TTS 생성 파일)
│   ├── DZM.ipynb
│   ├── DZM_chatbot.ipynb
│   ├── DZM_chatbot_v02.ipynb
│   └── module_all.ipynb
└── website
   ├── audios (differential dropout modules)
   │   ├── Before
   │   └── Progress   
   ├── images
   ├── js
   │   ├── home.js
   │   ├── login.js
   │   ├── main.js
   │   ├── mypage.js
   │   └── signup.js
   └── templates
       ├── chatbot.html
       ├── home.html
       ├── login.html
       ├── main.html
       ├── mypage.html
       └── signup.html

```

## 서비스 실행 화면


<img width="588" alt="image" src="https://github.com/jinseok19/Intermediate_Level_Project_for_AI-X/assets/121952875/ef8c95b4-893b-4623-9dc7-33cf1d98958f">

<img width="574" alt="image" src="https://github.com/jinseok19/Intermediate_Level_Project_for_AI-X/assets/121952875/579476c8-65b3-4e51-a00e-a929cf6f8312">

<img width="592" alt="image" src="https://github.com/jinseok19/Intermediate_Level_Project_for_AI-X/assets/121952875/e8835b03-202d-4585-a54e-7c3713ab2590">

<img width="590" alt="image" src="https://github.com/jinseok19/Intermediate_Level_Project_for_AI-X/assets/121952875/244ed8c8-8dbc-4c1c-8def-9618d04b9cf9">

<img width="587" alt="image" src="https://github.com/jinseok19/Intermediate_Level_Project_for_AI-X/assets/121952875/422c0f16-bc2a-4f12-9c75-a154b8274c16">

<img width="588" alt="image" src="https://github.com/jinseok19/Intermediate_Level_Project_for_AI-X/assets/121952875/98ef5c7f-7b71-4e96-ab59-4e745105df63">

<img width="587" alt="image" src="https://github.com/jinseok19/Intermediate_Level_Project_for_AI-X/assets/121952875/e4ea1a2d-5165-41cd-81ca-de1f0b8de4e3">

<img width="589" alt="image" src="https://github.com/jinseok19/Intermediate_Level_Project_for_AI-X/assets/121952875/608bcf81-7f97-4a37-b6ca-5a61c9567bfc">

<img width="587" alt="image" src="https://github.com/jinseok19/Intermediate_Level_Project_for_AI-X/assets/121952875/3261f067-703c-4d0d-a181-ea2f710acd0d">

<img width="582" alt="image" src="https://github.com/jinseok19/Intermediate_Level_Project_for_AI-X/assets/121952875/31db987a-858a-4000-8565-6472d000ae26">


