import streamlit as st

# MBTI에 어울리는 직업 목록
mbti_jobs = {
    "ISTJ": "💼 회계사, 변호사, 군인",
    "ISFJ": "👩‍🏫 교사, 간호사, 디자이너",
    "INFJ": "🎨 예술가, 작가, 심리학자",
    "INTJ": "🧑‍💻 소프트웨어 개발자, 연구원",
    "ISTP": "🚗 기계공, 프로그래머, 탐험가",
    "ISFP": "🎤 가수, 예술가, 조경사",
    "INFP": "✍️ 작가, 상담가, NGO 활동가",
    "INTP": "🔬 과학자, 수학자, 철학자",
    "ESTP": "🚴‍♂️ 운동선수, 마케팅 전문가",
    "ESFP": "🎭 배우, DJ, 이벤트 플래너",
    "ENFP": "🎨 예술가, 마케팅 전문가, 컨설턴트",
    "ENTP": "🧠 발명가, 법률가, 기업가",
    "ESTJ": "💼 관리자, 기업 리더, 경찰",
    "ESFJ": "👩‍⚕️ 의료 전문가, 판매원, 코디네이터",
    "ENFJ": "💬 상담사, HR 전문가, 교육자",
    "ENTJ": "👔 CEO, 전략가, 변호사",  # 여기에 문자열 종료 추가
}

# 직업 추천 함수
def get_job_recommendation(mbti_type):
    return mbti_jobs.get(mbti_type, "🌟 MBTI를 다시 선택해주세요!")

# 스트림릿 앱 인터페이스 만들기
def main():
    st.title("🔮 MBTI에 맞는 직업 추천 웹앱 🎉
