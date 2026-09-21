import streamlit as st
from PIL import Image, ImageOps
import requests
from io import BytesIO
from collections import Counter
from datetime import datetime

st.markdown("# :blue[ร้านนี้อร่อยทุกอย่าง]")

# =========================
# ตั้งค่าหน้าเว็บ
# =========================
st.set_page_config(
    page_title="อาหาร",
    layout="wide"
)

st.title("🍽️ MENU")


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
    "https://static.amarintv.com/images/upload/editor/source/IceZ/food/ep68/B3/3x7a8158.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQLaWIj-LU2P70X1TQmzebIudzBS0kFBAelAHYnpwzar6o7Fl85aoo-UfY&s=10",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScZ6qSVMBe67temGrfV0TwKwnvXxoPjf9Uw7ZbrhdJbg&s=10",
    "https://www.pholfoodmafia.com/wp-content/uploads/2022/07/SpaTumYum1000.jpg",
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

            # =========================
            # รูป
            # =========================
            image = get_image(images[i])

            if image is not None:
                st.markdown(
                    f"""
                    <div style="
                        display:flex;
                        justify-content:center;
                        align-items:center;
                    ">
                        <img src="{images[i]}"
                            style="
                                width:180px;
                                height:180px;
                                object-fit:cover;
                                display:block;
                            ">
                    </div>
                    """,
                    unsafe_allow_html=True
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

            # =========================
            # ชื่ออาหาร
            # =========================
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

            # =========================
            # ราคา
            # =========================
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
            
# ส่วนที่ 1: ส่วนหัวและเมนูร้าน
st.markdown("# :orange[🍳 Khai Kue Chiwit 🍴]")

st.divider()
with st.container(border=True):
    st.subheader("📦 เมนูคนชอบข่าย")
    st.write("- ลาบแซลมอน 99 บาท")
    st.write("- ซูชิข้าวคลุกกะปิไข่ชะอม 69 บาท")
    st.write("- พิซซ่าหน้ากะเพรา 129 บาท")
    st.write("- เกี๊ยวซ่ากุ้งผัดไทย 89 บาท")
    st.write("- สปาเกตตี้ผัดต้มยำกุ้ง 99 บาท")
    st.write("- ซูชิข้าวเหนียวไก่ย่างจิ้มแจ่ว 69 บาท")
    st.write("- เปาะเปี๊ยะส้มตำ 69 บาท ")
    st.write("- ขนมควยลิง 39 บาท")
    st.write("- ขนมพระพาย 45 บาท")
    st.write("- ขนมบุหลันดั้นเมฆ 45 บาท")
    st.write("- ขนมผการอง 45 บาท")
    st.write("- ขนมเสน่ห์จันทร์ 45 บาท")
    st.write("- ซากุระมะนาวโซดา 49 บาท")
    st.write("- บลูเบอร์รีครัมเบิลโยเกิร์ตดริ๊ง 59 บาท")
    st.write("- ชาเขียวนม 45 บาท")
    st.write("- ชาเย็น 45 บาท")
    st.write("- สตรอว์เบอร์รี่มะม่วงอกร่อง 55 บาท")
    st.write("- น้ำเปล่า 15 บาท")
    st.write("- น้ำแข็ง 1 ถัง 10 บาท")

with st.container(border=True):
    st.subheader("ส่วนลดของทางร้าน")
    st.write("- ซื้อครบ 300 บาท ลด 10%")
    st.write("- ซื้อครบ 500 บาท ลด 20%")
    
st.divider()
st.title("ระบบเลือกรายการและคำนวณเงิน")

# กำหนดราคาสินค้า/บริการตั้งต้น
menu_prices = {
    "ลาบแซลมอน": 99,
    "ซูชิข้าวคลุกกะปิไข่ชะอม": 69,
    "พิซซ่าหน้ากะเพรา": 129,
    "เกี๊ยวซ่ากุ้งผัดไทย": 89,
    "สปาเกตตี้ผัดต้มยำกุ้ง": 99,
    "ซูชิข้าวเหนียวไก่ย่างจิ้มแจ่ว": 69,
    "เปาะเปี๊ยะส้มตำ": 69,
    "ขนมควยลิง": 39,
    "ขนมบ้า": 39,
    "ขนมพระพาย": 45,
    "ขนมบุหลันดั้นเมฆ": 45,
    "ขนมผกากรอง": 45,
    "ขนมเสน่ห์จันทร์": 45,
    "ซากุระมะนาวโซดา": 49,
    "บลูเบอร์รีครัมเบิล โยเกิร์ตดริ๊งค์": 59,
    "ชาเขียวนม": 45,
    "ชาเย็น": 45,
    "สตรอว์เบอร์รี่มะม่วงอกร่อง": 55,
    "น้ำเปล่า": 15,
    "น้ำแข็ง 1 ถัง": 10,
}

# กำหนด Session State
if "selected_items" not in st.session_state:
    st.session_state.selected_items = []

if "show_receipt" not in st.session_state:
    st.session_state.show_receipt = False

# ฟังก์ชันเพิ่มรายการ
def add_item():
    item = st.session_state.new_item
    price = menu_prices[item]
    st.session_state.selected_items.append({"item": item, "price": price})
    st.session_state.show_receipt = False

# ฟังก์ชันเพิ่มจำนวนสินค้าเฉพาะรายการ
def increment_item(item_name):
    price = menu_prices[item_name]
    st.session_state.selected_items.append({"item": item_name, "price": price})
    st.session_state.show_receipt = False

# ฟังก์ชันลดจำนวนสินค้าเฉพาะรายการ
def decrement_item(item_name):
    for i in range(len(st.session_state.selected_items) - 1, -1, -1):
        if st.session_state.selected_items[i]["item"] == item_name:
            st.session_state.selected_items.pop(i)
            break
    st.session_state.show_receipt = False

# ฟังก์ชันลบรายการสินค้านั้นๆ ทั้งหมด
def remove_all_of_item(item_name):
    st.session_state.selected_items = [
        item for item in st.session_state.selected_items if item["item"] != item_name
    ]
    st.session_state.show_receipt = False

# ฟังก์ชันออกใบเสร็จ
def generate_receipt():
    if st.session_state.selected_items:
        st.session_state.show_receipt = True
    else:
        st.warning("กรุณาเลือกรายการสินค้าอย่างน้อย 1 รายการก่อนออกใบเสร็จ")

# ฟังก์ชันล้างข้อมูลทั้งหมด
def clear_all():
    st.session_state.selected_items = []
    st.session_state.show_receipt = False

# ส่วนเลือกรายการ
st.selectbox("เลือกรายการที่ต้องการ (เลือกซ้ำได้)", list(menu_prices.keys()), key="new_item")

col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
with col_btn1:
    st.button("➕ เพิ่มรายการนี้", on_click=add_item, use_container_width=True)
with col_btn2:
    st.button("📄 ออกใบเสร็จรับเงิน", on_click=generate_receipt, type="primary", use_container_width=True)
with col_btn3:
    st.button("🗑️ ล้างรายการทั้งหมด", on_click=clear_all, use_container_width=True)

# ----------------------------------------------------
# ส่วนที่เพิ่มเข้ามา: แสดงรายการสินค้าที่เลือกไว้พร้อมจำนวน
# ----------------------------------------------------
if st.session_state.selected_items:
    st.markdown("### 🛒 รายการที่สั่งไว้ขณะนี้")
    item_counts = Counter(item["item"] for item in st.session_state.selected_items)
    
    with st.container(border=True):
        # หัวตารางรายการสั่งซื้อ
        head_c1, head_c2, head_c3, head_c4 = st.columns([3, 1.5, 2, 1])
        head_c1.write("**รายการ**")
        head_c2.write("**ราคา/ชิ้น**")
        head_c3.write("**จำนวน**")
        head_c4.write("**จัดการ**")
        st.divider()

        # รายละเอียดแต่ละรายการ
        for item_name, count in item_counts.items():
            unit_price = menu_prices[item_name]
            c1, c2, c3, c4 = st.columns([3, 1.5, 2, 1])
            c1.write(f"• {item_name}")
            c2.write(f"{unit_price} บาท")
            
            # ปุ่มเพิ่ม-ลดจำนวนในแถวเดียวกัน
            with c3:
                btn_c1, btn_c2, btn_c3 = st.columns([1, 1.5, 1])
                btn_c1.button("➖", key=f"dec_{item_name}", on_click=decrement_item, args=(item_name,))
                btn_c2.write(f"**{count}**")
                btn_c3.button("➕", key=f"inc_{item_name}", on_click=increment_item, args=(item_name,))
            
            # ปุ่มลบรายการทั้งหมด
            c4.button("❌", key=f"del_{item_name}", on_click=remove_all_of_item, args=(item_name,))

st.divider()

# ส่วนที่ 2: แสดงผลในรูปแบบใบเสร็จรับเงิน (Receipt Layout)
if st.session_state.show_receipt and st.session_state.selected_items:
    item_counts = Counter(item["item"] for item in st.session_state.selected_items)
    subtotal = sum(item["price"] for item in st.session_state.selected_items)
    
    discount_percent = 0
    if subtotal >= 500:
        discount_percent = 20
    elif subtotal >= 300:
        discount_percent = 10
        
    discount_amount = subtotal * (discount_percent / 100)
    total_price = subtotal - discount_amount

    # แสดงผลตัวใบเสร็จ (สไตล์ Receipt Box)
    with st.container(border=True):
        st.markdown("<h3 style='text-align: center;'>🧾 ใบเสร็จรับเงิน / RECEIPT</h3>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: #FF8C00;'>ร้าน Khai Kue Chiwit</h4>", unsafe_allow_html=True)
        st.caption(f"วันที่-เวลา: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        st.text("-" * 45)

        # หัวตารางใบเสร็จ
        col1, col2, col3 = st.columns([3, 1, 1.5])
        col1.write("*รายการ*")
        col2.write("*จำนวน*")
        col3.write("*จำนวนเงิน*")
        st.text("-" * 45)

        # รายการสินค้า
        for item_name, count in item_counts.items():
            unit_price = menu_prices[item_name]
            item_total = unit_price * count
            
            c1, c2, c3 = st.columns([3, 1, 1.5])
            c1.write(f"{item_name} (@{unit_price})")
            c2.write(f"x{count}")
            c3.write(f"{item_total:,.2f} ฿")

        st.text("=" * 45)
        
        # สรุปยอดเงิน
        st.write(f"*รวมเป็นเงิน (Subtotal):* {subtotal:,.2f} บาท")
        if discount_percent > 0:
            st.write(f"*ส่วนลด ({discount_percent}%):* -{discount_amount:,.2f} บาท")
        else:
            st.write("*ส่วนลด:* 0.00 บาท")
            
        st.markdown(f"### ยอดชำระสุทธิ (NET TOTAL): :green[{total_price:,.2f} บาท]")
        st.text("=" * 45)
        st.markdown("<p style='text-align: center;'>🙏 ขอบคุณที่อุดหนุนครับ/ค่ะ 🙏</p>", unsafe_allow_html=True)

    # แสดงคำแนะนำการรับส่วนลดเพิ่มเติม
    if subtotal < 300:
        st.info(f"💡 ซื้อเพิ่มอีก {300 - subtotal:,.2f} บาท เพื่อรับส่วนลด 10%")
    elif subtotal < 500:
        st.info(f"🎉 ได้รับส่วนลด 10% แล้ว! (ซื้อเพิ่มอีก {500 - subtotal:,.2f} บาท เพื่อรับส่วนลด 20%)")
    else:
        st.success("🎉 คุณได้รับส่วนลดสูงสุด 20% แล้ว!")
