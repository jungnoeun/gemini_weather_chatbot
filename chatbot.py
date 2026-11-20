
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from weather_api import get_weather

# 1. API 키 불러오기
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API 키가 설정되지 않았습니다.")

# 2. Gemini 클라이언트 생성
client = genai.Client(api_key=api_key)

# 3. Gemini에게 사용할 도구 등록
config = types.GenerateContentConfig(
    system_instruction=(
        "당신은 친절한 한국어 AI 챗봇입니다. "
        "사용자가 날씨를 질문하면 get_weather 함수를 사용하세요. "
        "조회한 날씨 데이터를 바탕으로 답변하세요. "
        "조회된 지역명을 명확하게 알려주세요. "
        "제공되지 않은 날씨 정보는 추측하지 마세요. "
        "그 외 질문에는 일반 챗봇처럼 답변하세요."
    ),
    tools=[get_weather]
)

# 4. 대화 세션 생성
chat = client.chats.create(
    model="gemini-3.8-flash",
    config=config
)

print("Gemini 챗봇을 시작합니다!")
print("종료하려면 '종료'를 입력하세요.")

# 5. 사용자 입력 반복
while True:
    question = input("\n사용자: ").strip()

    if question == "종료":
        print("챗봇을 종료합니다.")
        break

    if not question:
        continue

    try:
        # 6. 대화 메시지 전송
        response = chat.send_message(question)

        # 7. 답변 출력
        print("\nGemini:", response.text)

    except Exception as e:
        print("오류 발생:", e)
