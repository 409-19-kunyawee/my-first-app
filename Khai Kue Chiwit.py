import streamlit as st
st.markdown("# :orange[🍳 Khai Kue Chiwit 🍴]")

st.divider()
with st.container(border=True):
    st.subheader("📦 เมนูคนชอบข่าย")
    st.write("- เครปไข่เจียว         ราคา 35 บาท")
    st.write("- ซุปไข่ข้นมะเขือเทศ    ราคา 40 บาท")
    st.write("- ไข่ตุ๋นหมูเด้ง         ราคา 40 บาท")
    st.write("- ไข่ลูกเขยระเบิด       ราคา 39 บาท")


with st.container(border=True):
    st.subheader("ส่วนลดของทางร้าน")
    st.write("- ซื้อครบ 300 บาท ลด 15%")
    st.write("- ซื้อทั้ง 4 เมนู ลดเพิ่มอีก 34 บาท")
    
st.divider()
# 1. กำหนดหัวข้อเว็บ
st.title("ระบบคำนวณราคาสินค้าอัจฉริยะ 🛒")

# 2. สร้างฐานข้อมูลรายการสินค้าและราคา (Dictionary)
menu_items = {
    "เครปไข่เจียว": 35,
    "ซุปไข่ข้นมะเขือเทศ": 40,
    "ไข่ตุ๋นหมูเด้ง": 40,
    "ไข่ลูกเขยระเบิด": 39,
    "เครปไข่เจียว": 35,
    "ซุปไข่ข้นมะเขือเทศ": 40,
    "ไข่ตุ๋นหมูเด้ง": 40,
    "ไข่ลูกเขยระเบิด": 39

}

# 3. สร้างช่องเลือกหลายตัวเลือก (Multiselect)
selected_items = st.multiselect(
    label="เลือกรายการสินค้าที่คุณต้องการซื้อ:",
    options=list(menu_items.keys()),
    default=None,
    placeholder="คลิกเพื่อเลือกสินค้า..."
)

# 4. ส่วนการคำนวณเงิน
if selected_items:
    st.write("---")
    st.subheader("📋 รายการที่คุณเลือก:")
    
    total_price = 0
    
    # วนลูปแสดงรายการที่เลือกพร้อมราคา และบวกราคารวม
    for item in selected_items:
        price = menu_items[item]
        total_price += price
        st.write(f"- {item}: *{price} บาท*")
        
    st.write("---")
    # แสดงราคารวมทั้งหมดด้วยตัวหนาและขนาดใหญ่
    st.markdown(f"### 💰 ราคารวมทั้งหมด: {total_price:,} บาท")
else:
    st.info("กรุณาเลือกสินค้าอย่างน้อย 1 รายการเพื่อคำนวณเงิน")
