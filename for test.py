import streamlit as st
from collections import Counter
from datetime import datetime

# ส่วนที่ 1: ส่วนหัวและเมนูร้าน (โค้ดเดิมของคุณ)
st.markdown("# :orange[🍳 Khai Kue Chiwit 🍴]")

st.divider()
with st.container(border=True):
    st.subheader("📦 เมนูคนชอบข่าย")
    st.write("- ลาบแซลมอน  99 บาท")
    st.write("- ซูชิข้าวคลุกกะปิไข่ชะอม  69 บาท")
    st.write("- พิซซ่าหน้ากะเพรา  129 บาท")
    st.write("- เกี๊ยวซ่ากุ้งผัดไทย  89 บาท")
    st.write("- สปาเกตตี้ผัดต้มยำกุ้ง 99 บาท")
    st.write("- ซูชิข้าวเหนียวไก่ย่างจิ้มแจ่ว 69บาท")
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
    st.write("- ซื้อครบ 500 บาท ลด 20% ")
    
st.divider()
st.title("ระบบเลือกรายการและคำนวณเงิน")

# กำหนดราคาสินค้า/บริการตั้งต้น
menu_prices = {
    "ลาบแซลมอน": 99,
    "ซูชิข้าวคลุกกะปิไข่ชะอม": 69,
    "พิซซ่าหน้ากะเพรา": 129,
    "เกี๊ยวซ่ากุ้งผัดไทย": 89,
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

# ใช้ st.session_state เพื่อเก็บบันทึกรายการที่เลือกเพิ่มได้หลายครั้ง
if "selected_items" not in st.session_state:
    st.session_state.selected_items = []

# ฟังก์ชันเพิ่มรายการ
def add_item():
    item = st.session_state.new_item
    price = menu_prices[item]
    st.session_state.selected_items.append({"item": item, "price": price})

# ฟังก์ชันล้างข้อมูล
def clear_all():
    st.session_state.selected_items = []

# ส่วนเลือกรายการ (เลือกซ้ำได้โดยการกดเพิ่มทีละครั้ง)
st.selectbox("เลือกรายการที่ต้องการ (เลือกซ้ำได้)", list(menu_prices.keys()), key="new_item")
st.button("➕ เพิ่มรายการนี้", on_click=add_item)

# ส่วนที่ 2: แสดงผลในรูปแบบใบเสร็จรับเงิน (Receipt Layout)
# 

st.divider()

if st.session_state.selected_items:
    # 1. รวบรวมนับจำนวนรายการสินค้าที่สั่งซ้ำ
    item_counts = Counter(item["item"] for item in st.session_state.selected_items)
    
    # 2. คำนวณราคารวม ส่วนลด และยอดสุทธิ
    subtotal = sum(item["price"] for item in st.session_state.selected_items)
    
    discount_percent = 0
    if subtotal >= 500:
        discount_percent = 20
    elif subtotal >= 300:
        discount_percent = 10
        
    discount_amount = subtotal * (discount_percent / 100)
    total_price = subtotal - discount_amount

    # 3. แสดงผลตัวใบเสร็จ (สไตล์ Receipt Box)
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

           if st.button(
        "🧾 ออกใบเสร็จและคำนวณเงิน", type="primary", use_container_width=True
    ):
        st.session_state.calc = True
        # สรุปยอดเงิน
        st.write(f"*รวมเป็นเงิน (Subtotal):* {subtotal:,.2f} บาท")
        if discount_percent > 0:
            st.write(f"*ส่วนลด ({discount_percent}%):* -{discount_amount:,.2f} บาท")
        else:
            st.write("*ส่วนลด:* 0.00 บาท")
            
        st.markdown(f"### *ยอดชำระสุทธิ (NET TOTAL):* :green[{total_price:,.2f} บาท]")
        st.text("=" * 45)
        st.markdown("<p style='text-align: center;'>🙏 ขอบคุณที่อุดหนุนครับ/ค่ะ 🙏</p>", unsafe_allow_html=True)

    # แสดงคำแนะนำการรับส่วนลดเพิ่มเติม
    if subtotal < 300:
        st.info(f"💡 ซื้อเพิ่มอีก {300 - subtotal:,.2f} บาท เพื่อรับส่วนลด 10%")
    elif subtotal < 500:
        st.info(f"🎉 ได้รับส่วนลด 10% แล้ว! (ซื้อเพิ่มอีก {500 - subtotal:,.2f} บาท เพื่อรับส่วนลด 20%)")
    else:
        st.success("🔥 คุณได้รับส่วนลดสูงสุด 20% เรียบร้อยแล้ว!")

    # ปุ่มล้างรายการ
    st.button("🗑️ ล้างรายการสั่งซื้อทั้งหมด", on_click=clear_all, type="primary")
