from datetime import datetime
import streamlit as st

# 1. แสดงเมนูและส่วนลด
st.markdown("# :orange[🍳 Khai Kue Chiwit 🍴]")
st.divider()
st.subheader("📦 เมนูและส่วนลด")
st.write(
    "- เครปไข่เจียว 35 บ. | ซุปไข่ข้นมะเขือเทศ 40 บ. | ไข่ตุ๋นหมูเด้ง 40 บ. | ไข่ลูกเขยระเบิด 39 บ."
)
st.caption("💡 ส่วนลด: ซื้อครบ 300 บาท ลด 10% | ครบ 500 บาท ลด 20%")

menu = {
    "เครปไข่เจียว": 35,
    "ซุปไข่ข้นมะเขือเทศ": 40,
    "ไข่ตุ๋นหมูเด้ง": 40,
    "ไข่ลูกเขยระเบิด": 39,
}
if "cart" not in st.session_state:
    st.session_state.cart = []
if "calc" not in st.session_state:
    st.session_state.calc = False

# 2. เลือกสินค้าใส่ตะกร้า
st.divider()
item = st.selectbox("เลือกรายการอาหาร", list(menu.keys()))
col1, col2 = st.columns(2)
if col1.button("➕ เพิ่มใส่ตะกร้า", use_container_width=True):
    st.session_state.cart.append(item)
    st.session_state.calc = False
if col2.button("🗑️ ล้างตะกร้า", use_container_width=True):
    st.session_state.cart, st.session_state.calc = [], False

# 3. แสดงตะกร้าและปุ่มคิดเงิน
if st.session_state.cart:
    st.write(f"🛒 *รายการในตะกร้า ({len(st.session_state.cart)} รายการ):*")
    for idx, name in enumerate(st.session_state.cart, 1):
        st.write(f"{idx}. {name} ({menu[name]} บาท)")

    if st.button(
        "🧾 ออกใบเสร็จและคำนวณเงิน", type="primary", use_container_width=True
    ):
        st.session_state.calc = True

# 4. ออกใบเสร็จคำนวณเงิน
if st.session_state.calc and st.session_state.cart:
    subtotal = sum(menu[i] for i in st.session_state.cart)
    disc_pct = 20 if subtotal >= 500 else (10 if subtotal >= 300 else 0)
    disc_amt = subtotal * (disc_pct / 100)
    net = subtotal - disc_amt

    with st.container(border=True):
        st.markdown(
            "### 🧾 ใบเสร็จรับเงิน (Khai Kue Chiwit)\n"
            f"<small>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</small>",
            unsafe_allow_html=True,
        )
        st.text("-" * 45)
        for i in set(st.session_state.cart):
            qty = st.session_state.cart.count(i)
            st.text(f"{i:<22} x{qty:<3} {menu[i]*qty:>8,.2f} บ.")
        st.text("=" * 45)
        st.text(
            f"ราคารวม (Subtotal):               {subtotal:>8,.2f} บ.\n"
            f"ส่วนลด {disc_pct}% (Discount):          -{disc_amt:>8,.2f} บ.\n"
            f"ยอดชำระสุทธิ (Net Total):         {net:>8,.2f} บ."
        )
        st.text("=" * 45)
        st.success(
            "🔥 สิทธิพิเศษ: ลดสูงสุด 20% แล้ว!"
            if subtotal >= 500
            else (
                f"🎉 ได้ส่วนลด 10% (ซื้ออีก {500-subtotal:,.2f} บ. ลด 20%)"
                if subtotal >= 300
                else f"💡 ซื้ออีก {300-subtotal:,.2f} บ. เพื่อรับส่วนลด 10%"
            )
        )
