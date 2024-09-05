import streamlit as st

# 페이지 구성 설정
st.set_page_config(
    page_title="CCTV Viewer",
    layout="wide"
)

# 스타일링을 위한 HTML/CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Sunflower:wght@300&display=swap');

    .title-container {
        background-color: black; /* 타이틀 영역의 배경색을 검정으로 설정 */
        padding: 20px;
        text-align: center;
        margin-bottom: 20px;
    }

    .title {
        color: yellow;
        font-size: 2em; /* 폰트 크기 조정 */
        font-weight: bold;
        font-family: 'Sunflower', sans-serif; /* 폰트 적용 */
        line-height: 1.5; /* 줄 간격 조정 */
    }

    .rainbow-divider {
        border: 0;
        height: 3px;
        background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
        margin: 20px 0; /* 위아래 여백 추가 */
    }

    /* 모바일 환경에서 텍스트와 이모티콘을 한 줄씩 보이게 하는 설정 */
    @media (max-width: 768px) {
        .title {
            font-size: 1.8em; /* 모바일에서 더 작은 폰트 크기 */
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 타이틀
st.markdown('''
<div class="title-container">
    <div class="title">
        신능 교통지옥 물럿거라!
        <br>
        🤬😤😡🧐😏🤨😎😍
    </div>
</div>
''', unsafe_allow_html=True)

# 서브타이틀을 일반 텍스트로 변경
st.write("출퇴근길 도와주는 상습 정체구역 cctv")

# 무지개 구분선 추가
st.markdown('<hr class="rainbow-divider">', unsafe_allow_html=True)

# CCTV URL과 지역명을 미리 정의
cctv_data = [
    {'url': 'https://gitsview.gg.go.kr/60237/e3jOoGDN4MBX4fDVzQskRtG+Pk5x+y0URgosXjREzYXfXQLd2Z5P1Bv1nMOaaytU', 'location': '⛪️ 분당요한성당'},
    {'url': 'https://gitsview.gg.go.kr/6718/syRv7yYNFpDvkp+gBmPK6G6lc6BX/JV9KWVj+M1XYP6WJ0/bgl5oYGJvXNmOkuRq', 'location': '⛰ 태재고개'},
    {'url': 'https://gitsview.gg.go.kr/60233/6K7yWTSrx%2BSKA/XdrNFI4ag/lc1eRQmhq6it2YeiSYxWOG31zZPBz/m/fLz74fsP', 'location': '🛣 하이마트 사거리'},
    {'url': 'https://gitsview.gg.go.kr/60231/hAghk8I/A4mBVrjG6jPafbzXkNgawgpLH4eJgkpjaqQOawhQaz70Uf+lJ4WYzae5', 'location': '🚥 이매 사거리'}
]

# CCTV 섬네일 디스플레이
if cctv_data:
    cols = st.columns(3)  # 3개의 CCTV를 한 줄에 표시

    for idx, data in enumerate(cctv_data):
        with cols[idx % 3]:
            st.write(data['location'])
            if "youtube.com" in data['url']:
                # YouTube URL을 임베드 URL로 변환
                youtube_embed_url = data['url'].replace("watch?v=", "embed/")
                # iframe을 통해 비디오 재생
                st.components.v1.iframe(youtube_embed_url, width=300, height=300)
            else:
                # HTML을 사용하여 비디오 직접 임베드
                video_html = f"""
                <video style="width: calc(100% - 46px);" controls autoplay>
                    <source src="{data['url']}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
                """
                st.markdown(video_html, unsafe_allow_html=True)
            
            # 줄바꿈 추가
            st.markdown("<br>", unsafe_allow_html=True)

# CSS 스타일 추가
st.markdown(
    """
    <style>
    [data-testid="stImage"] > div {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
