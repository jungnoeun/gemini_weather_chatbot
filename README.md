# Gemini API 와 

Gemini API 기반 날씨 챗봇
Python과 Gemini API를 활용해 자연어로 대화하고, 날씨 질문이 들어오면 Function Calling으로 외부 날씨 API를 호출하는 콘솔 챗봇입니다. 사용자가 특정 도시의 날씨를 물어보면 지역명을 파악하고, 해당 지역의 현재 날씨 데이터를 조회한 뒤 자연스러운 한국어 답변을 생성합니다.

### 주요 기능
- 일반 질의응답: Gemini 모델을 이용한 자유로운 대화
- 현재 날씨 조회: 서울, 대전, 도쿄 등 사용자가 지정한 도시의 날씨 조회
- 자동 함수 호출(Automatic Function Calling): 날씨 질문이라고 판단하면 Gemini가 get_weather() 도구를 선택하고 Python SDK가 실행
- 지역명 → 좌표 변환: Open-Meteo Geocoding API를 이용해 위도·경도 검색
- 대화 맥락 유지: Chat.send_message()로 프로그램 실행 중 이전 대화를 참고
기술 스택
구분	기술	용도
언어	Python	챗봇 및 API 연동 로직
LLM	Gemini API (gemini-3.8-flash)	자연어 이해 및 답변 생성
SDK	google-genai	Gemini 호출 및 Function Calling
외부 API	Open-Meteo Geocoding API	지역명으로 위도·경도 검색
외부 API	Open-Meteo Weather API	현재 기온·습도·강수량 등 조회
라이브러리	requests	외부 HTTP 요청
설정 관리	python-dotenv	.env에서 API 키 로드
개발 환경	VS Code, Python 가상환경 (venv)	개발 및 패키지 관리

### 동작 구조
```
사용자 질문
    │
    ▼
Python 콘솔 챗봇 (chatbot.py)
    │
    ▼
Gemini Chat API (Chat.send_message)
    │
    ├─ 일반 질문 ──────────────────────┐
    │                                 │
    └─ 날씨 질문 → Function Calling    │
                     │                │
                     ▼                │
              get_weather(location)   │
                     │                │
                     ▼                │
             Open-Meteo Geocoding     │
             (지역명 → 위도·경도)      │
                     │                │
                     ▼                │
             Open-Meteo Weather       │
             (현재 날씨 데이터 조회)   │
                     │                │
                     ▼                │
              함수 결과를 Gemini로 전달│
                     │                │
                     └──────┬─────────┘
                            ▼
                  Gemini 최종 답변 생성
                            │
                            ▼
                       콘솔 출력

```


### 실행 결과
<img width="1013" height="497" alt="image" src="https://github.com/user-attachments/assets/e6193f32-859a-47d6-bcc2-9850fd4d158b" />
