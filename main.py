import streamlit as st

# MBTI에 맞는 영화, 책, 음악 추천 목록과 추천 이유 및 영화 줄거리
mbti_recommendations = {
    "ISTJ": {
        "movie": "🎥 액션, 범죄 영화 - 예: '다크 나이트', '인셉션'",
        "movie_reason": "👨‍💼 ISTJ는 현실적이고 신뢰할 수 있는 성격으로, 액션과 범죄 영화처럼 논리적이고 계획적인 전개를 좋아해요.",
        "movie_plot": "📝 '다크 나이트'는 고담시를 위협하는 악당 조커와, 그를 막으려는 배트맨의 치열한 대립을 그린 영화입니다. 복잡한 윤리적 질문을 던지는 이야기.",
        "book": "📚 '명품을 만드는 사람들' - 명확한 계획과 분석을 좋아하는 ISTJ에게 맞는 책입니다.",
        "book_reason": "📖 ISTJ는 사실적이고 실용적인 지식을 추구하는 성향이 강해서, 실용적이고 구체적인 내용을 담은 책에 관심이 많아요.",
        "music": "🎶 클래식, 재즈 - 예: 'Beethoven - Symphony No.5', 'Miles Davis - So What'",
        "music_reason": "🎵 ISTJ는 안정적이고 고전적인 것을 선호하며, 클래식이나 재즈와 같은 음악을 즐깁니다."
    },
    "ISFJ": {
        "movie": "🎥 드라마, 감동적인 영화 - 예: '포레스트 검프', '타이타닉'",
        "movie_reason": "💖 ISFJ는 배려심 깊고 따뜻한 마음을 가진 사람으로, 감동적이고 감성적인 드라마 영화를 좋아할 거예요.",
        "movie_plot": "📝 '포레스트 검프'는 지적 장애를 가진 포레스트가 역사적인 사건 속에서 뛰어난 성과를 이루어내는 감동적인 이야기입니다.",
        "book": "📚 '마더 테레사' - 타인을 배려하는 ISFJ에게 적합한 책입니다.",
        "book_reason": "📖 ISFJ는 다른 사람들을 돕고자 하는 마음이 크기 때문에, 감동적이고 영감을 주는 이야기를 선호합니다.",
        "music": "🎶 팝, 발라드 - 예: 'Adele - Someone Like You', 'Ed Sheeran - Perfect'",
        "music_reason": "🎵 ISFJ는 감성적이고 부드러운 음악을 좋아하는 경향이 있습니다."
    },
    "INFJ": {
        "movie": "🎥 심리 드라마, 미스터리 - 예: '셔터 아일랜드', '파이트 클럽'",
        "movie_reason": "🧠 INFJ는 깊이 있는 사고를 즐기며, 심리적으로 복잡한 미스터리와 드라마 영화를 선호합니다.",
        "movie_plot": "📝 '셔터 아일랜드'는 심리적인 불안정성을 겪는 두 명의 연방수사관이 정신병원에서 벌어지는 사건을 조사하는 이야기입니다.",
        "book": "📚 '해리 포터' - 마법과 인물들의 심리적 깊이가 있는 이야기를 좋아하는 INFJ에게 적합한 책입니다.",
        "book_reason": "📖 INFJ는 창의적이고 깊이 있는 내용을 선호하며, 자신과 타인의 내면을 탐구하는 이야기를 좋아합니다.",
        "music": "🎶 클래식, 앰비언트 - 예: 'Ludovico Einaudi - Nuvole Bianche', 'Brian Eno - Music for Airports'",
        "music_reason": "🎵 INFJ는 감성적이고 평화로운 음악을 선호하며, 클래식과 앰비언트 음악을 좋아합니다."
    },
    "INTJ": {
        "movie": "🎥 과학, SF 영화 - 예: '인터스텔라', '2001: 스페이스 오디세이'",
        "movie_reason": "🚀 INTJ는 전략적이고 미래지향적인 사고를 좋아하며, 과학과 SF 영화에서 지적 자극을 받습니다.",
        "movie_plot": "📝 '인터스텔라'는 지구가 멸망할 위기에 처한 상황에서, 인류를 구하기 위한 우주 여행과 사랑에 대한 이야기를 그린 영화입니다.",
        "book": "📚 '사피엔스: 유인원에서 사이보그까지' - INTJ에게는 미래적이고 심도 있는 분석이 담긴 책이 어울립니다.",
        "book_reason": "📖 INTJ는 깊이 있는 사고를 중시하며, 인류의 진화와 미래를 탐구하는 책을 선호합니다.",
        "music": "🎶 전자음악, 앰비언트 - 예: 'Daft Punk - Voyager', 'Moby - Porcelain'",
        "music_reason": "🎵 INTJ는 창의적이고 논리적인 음악을 선호하며, 전자음악과 앰비언트 음악을 좋아합니다."
    },
    # 나머지 MBTI 유형에 대한 추천도 추가 가능
}

# 추천 정보 함수
def get_recommendations(mbti_type):
    recommendation = mbti_recommendations.get(mbti_type)
    if recommendation:
        return recommendation
    return None

# 스트림릿 앱 인터페이스 만들기
def main():
    st.title("🎬 MBTI에 맞는 영화, 책, 음악 추천 웹앱 🎉")
    st.markdown("👋 안녕하세요! 당신의 MBTI를 입력하면 어울리는 영화, 책, 음악을 추천해 드려요! 🚀")
    
    # MBTI 입력 선택
    mbti_type = st.selectbox(
        "당신의 MBTI 유형을 선택하세요:",
        ["ISTJ", "ISFJ", "INFJ", "INTJ"]
        # 나머지 MBTI도 여기에 추가 가능합니다.
    )

    # 추천 정보 불러오기
    recommendations = get_recommendations(mbti_type)
    
    if recommendations:
        # 영화 추천
        st.subheader("🎬 추천 영화:")
        st.markdown(f"**{recommendations['movie']}**")
        st.markdown(f"📖 **추천 이유:** {recommendations['movie_reason']}")
        st.markdown(f"📝 **영화 줄거리:** {recommendations['movie_plot']}")
        
        # 책 추천
        st.subheader("📚 추천 책:")
        st.markdown(f"**{recommendations['book']}**")
        st.markdown(f"📖 **추천 이유:** {recommendations['book_reason']}")
        
        # 음악 추천
        st.subheader("🎶 추천 음악:")
        st.markdown(f"**{recommendations['music']}**")
        st.markdown(f"📖 **추천 이유:** {recommendations['music_reason']}")
        
        # 풍선 효과 (스트림릿 내장 함수 사용)
        st.balloons()  # 스트림릿 내장 풍선 효과

    else:
        st.write("🌟 MBTI를 다시 선택해주세요!")

    # 추가적인 장식
    st.markdown("🎉✨ 다양한 추천을 통해 즐거운 시간을 보내세요! ✨🎉")

if __name__ == "__main__":
    main()
