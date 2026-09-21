import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# ==========================================
# ตั้งค่าหน้าเว็บ
# ==========================================
st.set_page_config(
    page_title="My Gallery",
    layout="wide"
)

st.title("My Gallery")


# ==========================================
# 🟢 โซนเปลี่ยนชื่อ
# ==========================================
names = [
    "ชื่อที่ 1",
    "ชื่อที่ 2",
    "ชื่อที่ 3",
    "ชื่อที่ 4",
    "ชื่อที่ 5",
    "ชื่อที่ 6",
    "ชื่อที่ 7",
    "ชื่อที่ 8",
    "ชื่อที่ 9"
]


# ==========================================
# 🔵 โซนเปลี่ยนลิงก์รูป
# ==========================================
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


# ==========================================
# ฟังก์ชันทำให้รูปทุกภาพขนาดเท่ากัน
# ==========================================
def get_image(url):

    try:
        response = requests.get(url, timeout=10)
        image = Image.open(BytesIO(response.content))

        # ทำให้ทุกภาพเป็นขนาด 600 x 400
        image = image.convert("RGB")
        image.thumbnail((600, 400))

        return image

    except:
        return None


# ==========================================
# แสดง Gallery 3 x 3
# ==========================================

for row in range(3):

    col1, col2, col3 = st.columns(3)

    columns = [col1, col2, col3]

    for col, i in zip(
        columns,
        range(row * 3, row * 3 + 3)
    ):

        with col:

            # กรอบรูป
            image = get_image(images[i])

            if image is not None:
                st.image(
                    image,
                    width="stretch"
                )
            else:
                st.info("ใส่ลิงก์รูปตรงนี้")

            # ชื่อ
            st.markdown(
                f"<h3 style='text-align:center;'>{names[i]}</h3>",
                unsafe_allow_html=True
            )
