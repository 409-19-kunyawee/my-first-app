import streamlit as st
from PIL import Image, ImageOps
import requests
from io import BytesIO

# =========================
# ตั้งค่าหน้าเว็บ
# =========================
st.set_page_config(
    page_title="My Food Gallery",
    layout="wide"
)

st.title("🍽️ My Food Gallery")


# =========================
# ✏️ แก้ชื่ออาหารตรงนี้
# =========================
names = [
    "ลาบแซลมอน",
    "ซูชิข้าวคลุกกะปิไข่ชะอม",
    "พิซซ่าหน้ากะเพรา",
    "เกี๊ยวซ่ากุ้งผัดไทย",
    "สปาเกตตี้ผัดต้มยำกุ้ง",
    "มักกะโรนี",
    "ชื่ออาหาร 7",
    "ชื่ออาหาร 8",
    "ชื่ออาหาร 9",
    "ชื่ออาหาร 10"
]


# =========================
# 💰 แก้ราคาตรงนี้
# =========================
prices = [
    "99 บาท",
    "69 บาท",
    "129 บาท",
    "89 บาท",
    "109 บาท",
    "99 บาท",
    "79 บาท",
    "89 บาท",
    "69 บาท",
    "99 บาท"
]


# =========================
# 🖼️ ใส่ลิงก์รูปตรงนี้
# ต้องเป็น Direct Image URL
# เช่น .jpg / .png / .webp
# =========================
images = [
    "https://i.pinimg.com/736x/cb/5d/51/cb5d510c28e4a575d45f511beaad0b83.jpg",
    "ใส่ลิงก์รูปที่ 2",
    "ใส่ลิงก์รูปที่ 3",
    "ใส่ลิงก์รูปที่ 4",
    "ใส่ลิงก์รูปที่ 5",
    "ใส่ลิงก์รูปที่ 6",
    "ใส่ลิงก์รูปที่ 7",
    "ใส่ลิงก์รูปที่ 8",
    "ใส่ลิงก์รูปที่ 9",
    "ใส่ลิงก์รูปที่ 10"
]


# =========================
# ฟังก์ชันโหลดรูป
# =========================
def get_image(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        image = Image.open(
            BytesIO(response.content)
        ).convert("RGB")

        # ทำให้รูปทุกใบมีขนาดเท่ากัน
        image = ImageOps.fit(
            image,
            (180, 180)
        )

        return image

    except:
        return None


# =========================
# แสดงอาหาร 5 คอลัมน์
# =========================
for row in range(0, len(images), 5):

    columns = st.columns(5)

    for col, i in zip(
        columns,
        range(row, min(row + 5, len(images)))
    ):

        with col:

            # รูปอาหาร
            image = get_image(images[i])

            if image is not None:
                st.image(
                    image,
                    width=180
                )
            else:
                st.markdown(
                    """
                    <div style="
                        width:180px;
                        height:180px;
                        border:1px solid #ddd;
                        display:flex;
                        align-items:center;
                        justify-content:center;
                        margin:auto;
                        color:#999;
                    ">
                        ใส่รูปตรงนี้
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # ชื่ออาหาร
            st.markdown(
                f"""
                <div style="
                    text-align:center;
                    font-size:16px;
                    font-weight:bold;
                    margin-top:8px;
                ">
                    {names[i]}
                </div>
                """,
                unsafe_allow_html=True
            )

            # ราคา
            st.markdown(
                f"""
                <div style="
                    text-align:center;
                    font-size:15px;
                    margin-top:4px;
                ">
                    {prices[i]}
                </div>
                """,
                unsafe_allow_html=True
            )
