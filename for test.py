import streamlit as st

st.title("💰 ระบบคำนวณส่วนลดสินค้าใน Streamlit")

# 1. รับค่าราคาสินค้าเริ่มต้น
price = st.number_input("กรอกราคาสินค้าตั้งต้น (บาท):", min_value=0.0, value=1000.0, step=100.0)

# 2. เลือกประเภทของส่วนลด
discount_type = st.selectbox(
    "เลือกประเภทส่วนลด:",
    ["ไม่มีส่วนลด", "ลดเป็นเปอร์เซ็นต์ (%)", "ลดเป็นจำนวนเงิน (บาท)", "ใช้โค้ดส่วนลด (Promo Code)"]
)

discount_amount = 0.0
promo_code = ""

# 3. เงื่อนไขตามประเภทส่วนลดที่เลือก
if discount_type == "ลดเป็นเปอร์เซ็นต์ (%)":
    percent = st.slider("ระบุเปอร์เซ็นต์ส่วนลด:", min_value=0, max_value=100, value=10)
    discount_amount = price * (percent / 100)

elif discount_type == "ลดเป็นจำนวนเงิน (บาท)":
    discount_amount = st.number_input("ระบุจำนวนเงินส่วนลด (บาท):", min_value=0.0, max_value=price, value=100.0)

elif discount_type == "ใช้โค้ดส่วนลด (Promo Code)":
    promo_code = st.text_input("กรอกโค้ดส่วนลดของคุณ:").strip().upper()
    # กำหนดโค้ดตัวอย่าง เช่น SAVE20 ลด 20%, SALE500 ลด 500 บาท
    if promo_code == "SAVE20":
        discount_amount = price * 0.20
        st.success("ใช้โค้ด SAVE20 สำเร็จ! (ลด 20%)")
    elif promo_code == "SALE500":
        discount_amount = 500.0
        st.success("ใช้โค้ด SALE500 สำเร็จ! (ลด 500 บาท)")
    elif promo_code != "":
        st.error("โค้ดส่วนลดไม่ถูกต้องหรือหมดอายุ")

# 4. คำนวณราคาสุทธิ
# ป้องกันส่วนลดมากกว่าราคาสินค้า
if discount_amount > price:
    discount_amount = price

final_price = price - discount_amount

# 5. แสดงผลลัพธ์
st.markdown("---")
st.subheader("📋 สรุปรายการคำนวณ")
st.write(f"*ราคาก่อนหักส่วนลด:* {price:,.2f} บาท")
st.write(f"*ส่วนลด 100% / หักออก:* -{discount_amount:,.2f} บาท")
st.markdown(f"### *ราคาสุทธิที่ต้องชำระ:* :green[{final_price:,.2f}] บาท")
