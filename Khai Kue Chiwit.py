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
    st.write("- ซื้อครบ 300 บาท ลด 10%")
    st.write("- ซื้อครบ 500 บาท ลด 20% ")
    
st.divider()
st.title("ระบบเลือกรายการและคำนวณเงิน")

# กำหนดราคาสินค้า/บริการตั้งต้น
menu_prices = {
    "เครปไข่เจียว": 35,
    "ซุปไข่ข้นมะเขือเทศ": 40,
    "ไข่ตุ๋นเนื้อหมูเด้ง": 40,
    "ไข่ลูกเขยระเบิด": 39,
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

st.divider()

# แสดงรายการที่เลือกทั้งหมด
st.subheader("📋 รายการที่คุณเลือก:")
if st.session_state.selected_items:
    total_price = 0
    for i, entry in enumerate(st.session_state.selected_items):
        col1, col2 = st.columns([3, 1])
        col1.write(f"{i+1}. {entry['item']}")
        col2.write(f"{entry['price']:,.2f} บาท")
        total_price += entry['price']
    
    st.divider()
    st.markdown(h2 := f"### *ยอดรวมทั้งหมด: {total_price:,.2f} บาท*")
    st.button("🗑️ ล้างรายการทั้งหมด", on_click=clear_all)
else:
    st.info("ยังไม่มีรายการถูกเลือก กรุณากดเพิ่มรายการด้านบน")
