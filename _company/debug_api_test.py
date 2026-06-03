import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import json

# --- 1. 설정 영역 ---
# 실제 API 서비스와 자격 증명에 맞게 수정 필요
API_SERVICE_NAME = 'youtube' # 예시: 유튜브 API
API_VERSION = 'v3'
# 인증 방식에 따라 아래 중 하나를 사용하도록 코드를 수정해야 합니다.
# 1. API Key를 직접 설정하는 방식
API_KEY = os.getenv("YOUTUBE_API_KEY", "YOUR_HARDCODED_KEY_HERE") # <-- 여기에 실제 Key를 넣거나 환경 변수를 설정해야 함
# 2. 서비스 계정 사용 시: SCOPES와 CREDENTIALS 로드 로직 추가 필요

print("--- [코다리] API 디버깅 테스트 시작 ---")

try:
    if not API_KEY or API_KEY == "YOUR_HARDCODED_KEY_HERE":
        print("❌ FATAL: API_KEY가 설정되지 않았거나 기본값입니다. 인증 정보 확인 필수.")
        exit(1)

    # API Key를 사용한 클라이언트 빌드 (가장 간단한 테스트)
    youtube_service = build(
        "youtube", 
        "v3", 
        developerKey=API_KEY
    )
    print("✅ 클라이언트 빌드 성공.")

    # 2. 가장 간단한 메서드 호출 시도 (API 연결 테스트)
    request = youtube_service.channels().list(
        part="snippet,contentDetails",
        id="UC_YOUR_CHANNEL_ID" # <-- 실제 채널 ID로 교체하여 테스트
    )
    response = request.execute()
    
    print("\n--- API 호출 성공 ---")
    print(f"응답 상태 코드: {response.get('kind')}")
    print(f"채널 정보 일부 출력: {response.get('items')[0]['snippet']['title'] if response.get('items') else '데이터 없음'}")

except Exception as e:
    print("\n--- 💥 API 호출 중 치명적 오류 발생 ---")
    print(f"에러 타입: {type(e).__name__}")
    print(f"에러 메시지: {e}")
    print("\n💡 코다리 진단: 이 에러는 보통 400/401/403 (인증/권한) 또는 네트워크 문제에서 발생합니다.")

print("--- [코다리] API 디버깅 테스트 종료 ---")