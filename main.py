import streamlit as st

# MBTI에 맞는 영화, 책, 음악 추천 목록과 추천 이유 및 영화 줄거리
# 각 MBTI 유형에 대한 공식 설명과 취미활동을 같이 즐기면 좋은 MBTI
mbti_recommendations = {
    "ISTJ": {
        "movie": "🎥 액션, 범죄 영화 - 예: '다크 나이트', '인셉션'",
        "movie_reason": "👨‍💼 ISTJ는 현실적이고 신뢰할 수 있는 성격으로, 액션과 범죄 영화처럼 논리적이고 계획적인 전개를 좋아해요.",
        "movie_plot": "📝 '다크 나이트'는 고담시를 위협하는 악당 조커와, 그를 막으려는 배트맨의 치열한 대립을 그린 영화입니다. 복잡한 윤리적 질문을 던지는 이야기.",
        "movie_poster": "https://m.media-amazon.com/images/I/71bRHTXcU2L._AC_SY679_.jpg",  # '다크 나이트' 포스터 URL
        "book": "📚 '명품을 만드는 사람들' - 명확한 계획과 분석을 좋아하는 ISTJ에게 맞는 책입니다.",
        "book_reason": "📖 ISTJ는 사실적이고 실용적인 지식을 추구하는 성향이 강해서, 실용적이고 구체적인 내용을 담은 책에 관심이 많아요.",
        "book_cover": "https://images-na.ssl-images-amazon.com/images/I/51b5QW49KJL._SX354_BO1,204,203,200_.jpg",  # '명품을 만드는 사람들' 표지
        "music": "🎶 클래식, 재즈 - 예: 'Beethoven - Symphony No.5', 'Miles Davis - So What'",
        "music_reason": "🎵 ISTJ는 안정적이고 고전적인 것을 선호하며, 클래식이나 재즈와 같은 음악을 즐깁니다.",
        "official_description": "📝 **ISTJ**는 현실적이고 철저하며, 신뢰할 수 있는 사람입니다. 계획적이고 규칙을 따르며, 전통과 안정성을 중시합니다.",
        "hobby_match": "🧩 **추천 취미 활동:** 보드게임, 퍼즐 맞추기, 독서\n**같이 즐기면 좋은 MBTI:** INTJ, ESTJ"
    },
    "ISFJ": {
        "movie": "🎥 드라마, 감동적인 영화 - 예: '포레스트 검프', '타이타닉'",
        "movie_reason": "💖 ISFJ는 배려심 깊고 따뜻한 마음을 가진 사람으로, 감동적이고 감성적인 드라마 영화를 좋아할 거예요.",
        "movie_plot": "📝 '포레스트 검프'는 지적 장애를 가진 포레스트가 역사적인 사건 속에서 뛰어난 성과를 이루어내는 감동적인 이야기입니다.",
        "movie_poster": "https://m.media-amazon.com/images/I/61M0D4twf8L._AC_SY679_.jpg",  # '포레스트 검프' 포스터 URL
        "book": "📚 '마더 테레사' - 타인을 배려하는 ISFJ에게 적합한 책입니다.",
        "book_reason": "📖 ISFJ는 다른 사람들을 돕고자 하는 마음이 크기 때문에, 감동적이고 영감을 주는 이야기를 선호합니다.",
        "book_cover": "https://images-na.ssl-images-amazon.com/images/I/71kg%2BGh5hLL._AC_SY679_.jpg",  # '마더 테레사' 표지
        "music": "🎶 팝, 발라드 - 예: 'Adele - Someone Like You', 'Ed Sheeran - Perfect'",
        "music_reason": "🎵 ISFJ는 감성적이고 부드러운 음악을 좋아하는 경향이 있습니다.",
        "official_description": "📝 **ISFJ**는 따뜻하고 섬세한 성격을 가지고 있으며, 사람들을 돕고 지원하는 것을 즐깁니다. 세심한 관심과 책임감을 바탕으로 자신의 가족과 친구들을 돌봅니다.",
        "hobby_match": "🧩 **추천 취미 활동:** 자원봉사, 요리, 가드닝\n**같이 즐기면 좋은 MBTI:** ESFJ, ENFJ"
    },
    "INFJ": {
        "movie": "🎥 심리 드라마, 미스터리 - 예: '셔터 아일랜드', '파이트 클럽'",
        "movie_reason": "🧠 INFJ는 깊이 있는 사고를 즐기며, 심리적으로 복잡한 미스터리와 드라마 영화를 선호합니다.",
        "movie_plot": "📝 '셔터 아일랜드'는 심리적인 불안정성을 겪는 두 명의 연방수사관이 정신병원에서 벌어지는 사건을 조사하는 이야기입니다.",
        "movie_poster": "https://m.media-amazon.com/images/I/91R2E2a4NkL._AC_SY679_.jpg",  # '셔터 아일랜드' 포스터 URL
        "book": "📚 '해리 포터' - 마법과 인물들의 심리적 깊이가 있는 이야기를 좋아하는 INFJ에게 적합한 책입니다.",
        "book_reason": "📖 INFJ는 창의적이고 깊이 있는 내용을 선호하며, 자신과 타인의 내면을 탐구하는 이야기를 좋아합니다.",
        "book_cover": "https://images-na.ssl-images-amazon.com/images/I/91P2b5RO7PL.jpg",  # '해리 포터' 표지
        "music": "🎶 클래식, 앰비언트 - 예: 'Ludovico Einaudi - Nuvole Bianche', 'Brian Eno - Music for Airports'",
        "music_reason": "🎵 INFJ는 감성적이고 평화로운 음악을 선호하며, 클래식과 앰비언트 음악을 좋아합니다.",
        "official_description": "📝 **INFJ**는 깊은 통찰력과 이상주의적 사고를 지닌 사람으로, 사람들의 내면을 이해하고 돕는 것을 중요하게 생각합니다.",
        "hobby_match": "🧩 **추천 취미 활동:** 명상, 글쓰기, 예술 활동\n**같이 즐기면 좋은 MBTI:** ENFJ, INFP"
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
    st.title("🎬 현진서의 MBTI별 영화, 책, 음악 추천 🎉")  # 제목 변경
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
        st.image(recommendations['movie_poster'], caption="🎬 영화 포스터", use_column_width=True)
        
        # 책 추천
        st.subheader("📚 추천 책:")
        st.markdown(f"**{recommendations['book']}**")
        st.markdown(f"📖 **추천 이유:** {recommendations['book_reason']}")
        st.image(recommendations['book_cover'], caption="📚 책 표지", use_column_width=True)
        
        # 음악 추천
        st.subheader("🎶 추천 음악:")
        st.markdown(f"**{recommendations['music']}**")
        st.markdown(f"📖 **추천 이유:** {recommendations['music_reason']}")
        
        # 공식 설명
        st.subheader("📖 MBTI 공식 설명:")
        st.markdown(f"{recommendations['official_description']}")
        
        # 취미 추천
        st.subheader("🎯 추천 취미 활동:")
        st.markdown(f"{recommendations['hobby_match']}")
        
        # 풍선 효과 (스트림릿 내장 함수 사용)
        st.balloons()  # 스트림릿 내장 풍선 효과

    else:
        st.write("🌟 MBTI를 다시 선택해주세요!")

    # 추가적인 장식
    st.markdown("🎉✨ 다양한 추천을 통해 즐거운 시간을 보내세요! ✨🎉")

if __name__ == "__main__":
    main()
