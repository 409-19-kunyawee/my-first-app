from collections import Counter
import streamlit as st

st.title("🍳 Khai Kue Chiwit 🍴")
prices = {
    "เครปไข่เจียว": 35,
    "ซุปไข่ข้นมะเขือเทศ": 40,
    "ไข่ตุ๋นหมูเด้ง": 40,
    "ไข่ลูกเขยระเบิด": 39,
}

if "cart" not in st.session_state:
    st.session_state.cart = []
if "show" not in st.session_state:
    st.session_state.show = False

item = st.selectbox("เลือกรายการ", list(prices.keys()))
if st.button("➕ เพิ่มใส่ตะกร้า"):
    st.session_state.cart.append(item)
    st.session_state.show = False

if st.session_state.cart:
    st.write(
        "🛒 ตะกร้า:",
        dict(Counter(st.session_state.cart)),
    )
    col1, col2 = st.columns(2)
    if col1.button("🧾 ออกใบเสร็จ"):
        st.session_state.show = True
    if col2.button("🗑️ ล้างตะกร้า"):
        st.session_state.cart = []
        st.session_state.show = False

if st.session_state.show and st.session_state.cart:
    st.divider()
    st.subheader("🧾 ใบเสร็จรับเงิน")
    subtotal = sum(prices[i] for i in st.session_state.cart)

    discount = 0.2 if subtotal >= 500 else (0.1 if subtotal >= 300 else 0)
    disc_amt = subtotal * discount
    net = subtotal - disc_amt

    for k, v in Counter(st.session_state.cart).items():
        st.write(f"- {k} x{v} = {prices[k]*v} บาท")

    st.write(f"*ราคารวม:* {subtotal} บาท")
    st.write(f"*ส่วนลด ({int(discount*100)}%):* -{disc_amt:.2f} บาท")
    st.success(f"*ยอดชำระสุทธิ: {net:.2f} บาท*")
