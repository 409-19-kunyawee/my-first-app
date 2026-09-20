import streamlit as st

st.title("ระบบคำนวณส่วนลดอัตโนมัติ")

# 1. รับค่าราคาสินค้าตั้งต้น
price = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0, value=1000.0, step=100.0)

# 2. ตัวเลือกประเภทสมาชิก
member_type = st.selectbox(
    "เลือกประเภทสมาชิก:",
    ["General (ทั่วไป)", "Silver (สมาชิกซิลเวอร์)", "Gold (สมาชิกโกลด์)", "VIP (วีไอพี)"]
)

# 3. เงื่อนไขส่วนลดอัตโนมัติ (If-Else Condition)
discount_rate = 0.0

if member_type == "Silver (สมาชิกซิลเวอร์)":
    discount_rate = 0.05  # ส่วนลด 5%
elif member_type == "Gold (สมาชิกโกลด์)":
    discount_rate = 0.10  # ส่วนลด 10%
elif member_type == "VIP (วีไอพี)":
    discount_rate = 0.20  # ส่วนลด 20%
else:
    discount_rate = 0.00  # ไม่มีส่วนลด

# 4. คำนวณราคาหลังหักส่วนลด
discount_amount = price * discount_rate
final_price = price - discount_amount

# 5. แสดงผลลัพธ์แบบอัตโนมัติ
st.divider()
st.subheader("สรุปยอดชำระเงิน")
st.write(f"ราคาตั้งต้น: *{price:,.2f} บาท*")
st.write(f"ได้รับส่วนลด ({int(discount_rate * 100)}%): *-{discount_amount:,.2f} บาท*")
st.success(f"ยอดเงินที่ต้องชำระสุทธิ: *{final_price:,.2f} บาท*")
