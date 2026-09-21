import streamlit as st

# ==============================
# ตั้งค่าหน้าเว็บ
# ==============================
st.set_page_config(
    page_title="My Gallery",
    layout="wide"
)

st.title("My Gallery")


# ==================================================
# 🟢 โซนเปลี่ยนชื่อ
# ==================================================
names = [
    "ลาบแซลมอน 99 บาท",
    "ชื่อที่ 2",
    "ชื่อที่ 3",
    "ชื่อที่ 4",
    "ชื่อที่ 5",
    "ชื่อที่ 6",
    "ชื่อที่ 7",
    "ชื่อที่ 8",
    "ชื่อที่ 9"
]


# ==================================================
# 🔵 โซนเปลี่ยนลิงก์รูป
# ==================================================
images = [
    "https://apimain.kleensstation.com/images/1695562648.jpg",
    "ใส่ลิงก์รูปที่ 2",
    "ใส่ลิงก์รูปที่ 3",
    "ใส่ลิงก์รูปที่ 4",
    "ใส่ลิงก์รูปที่ 5",
    "ใส่ลิงก์รูปที่ 6",
    "ใส่ลิงก์รูปที่ 7",
    "ใส่ลิงก์รูปที่ 8",
    "ใส่ลิงก์รูปที่ 9"
]


# ==================================================
# แสดง Gallery 3 × 3
# ==================================================

for row in range(3):

    col1, col2, col3 = st.columns(3)

    for col, i in zip(
        [col1, col2, col3],
        range(row * 3, row * 3 + 3)
    ):

        with col:

            st.markdown(
                f"""
                <div style="
                    border: 1px solid #cccccc;
                    padding: 10px;
                    margin: 5px;
                    text-align: center;
                    background-color: white;
                ">

                    <div style="
                        width: 100%;
                        height: 200px;
                        overflow: hidden;
                    ">

                        <img
                            src="{images[i]}"
                            style="
                                width: 100%;
                                height: 200px;
                                object-fit: cover;
                                display: block;
                            "
                        >

                    </div>

                    <h3 style="
                        margin-top: 12px;
                        margin-bottom: 5px;
                    ">
                        {names[i]}
                    </h3>

                </div>
                """,
                unsafe_allow_html=True
            )
