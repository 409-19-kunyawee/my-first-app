import streamlit as st

# 1. สมมติข้อมูลยอดรวมสินค้าก่อนหน้า (แทนค่าด้วยตัวแปรจากระบบของคุณได้เลย)
st.title("🛒 ระบบคำนวณส่วนลด")
total_amount = st.number_input("ยอดรวมสินค้า (บาท)", min_value=0.0, value=500.0, step=50.0)

st.divider()

# 2. สร้างตัวเลือกโค้ดส่วนลด
st.subheader("🎟️ เลือกส่วนลดของคุณ")
discount_option = st.selectbox(
    "เลือกโปรโมชั่นที่ต้องการใช้:",
    ["ไม่ใช้ส่วนลด", "ลด 50 บาท (ขั้นต่ำ 300 บาท)", "ลด 150 บาท (ขั้นต่ำ 1,000 บาท)", "ลด 10% (ขั้นต่ำ 500 บาท)"]
)

# 3. กำหนดเงื่อนไขของแต่ละส่วนลด
discount_amount = 0.0
is_eligible = True
error_message = ""

if discount_option == "ลด 50 บาท (ขั้นต่ำ 300 บาท)":
    if total_amount >= 300:
        discount_amount = 50.0
    else:
        is_eligible = False
        error_message = f"❌ ยอดซื้อไม่ครบเงื่อนไข (ขาดอีก {300 - total_amount:.2f} บาท)"

elif discount_option == "ลด 150 บาท (ขั้นต่ำ 1,000 บาท)":
    if total_amount >= 1000:
        discount_amount = 150.0
    else:
        is_eligible = False
        error_message = f"❌ ยอดซื้อไม่ครบเงื่อนไข (ขาดอีก {1000 - total_amount:.2f} บาท)"

elif discount_option == "ลด 10% (ขั้นต่ำ 500 บาท)":
    if total_amount >= 500:
        discount_amount = total_amount * 0.10
    else:
        is_eligible = False
        error_message = f"❌ ยอดซื้อไม่ครบเงื่อนไข (ขาดอีก {500 - total_amount:.2f} บาท)"

# 4. แสดงผลลัพธ์ตามเงื่อนไข
if not is_eligible:
    # หากไม่ผ่านเงื่อนไขขั้นต่ำ ให้แจ้งเตือนและเซ็ตส่วนลดเป็น 0
    st.error(error_message)
    discount_amount = 0.0
elif discount_option != "ไม่ใช้ส่วนลด":
    st.success(True and f"🎉 ประยุกต์ใช้ส่วนลดสำเร็จ! ลดไป {discount_amount:.2f} บาท")

# 5. คำนวณยอดสุทธิที่ต้องจ่าย
final_amount = total_amount - discount_amount

st.divider()
st.subheader("📊 สรุปยอดใบเสร็จ")
st.write(f"ยอดรวมสินค้า: *{total_amount:,.2f}* บาท")
st.write(f"ส่วนลด: *-{discount_amount:,.2f}* บาท")
st.markdown(f"### ยอดเงินสุทธิ: :green[{final_amount:,.2f}] บาท")
