from datetime import datetime
from collections import Counter
import streamlit as st

# ==========================================
# ส่วนที่ 1: ส่วนหัวและเมนูอาหาร
# ==========================================
st.markdown("# :orange[🍳 Khai Kue Chiwit 🍴]")

st.divider()
with st.container(border=True):
    st.subheader("📦 เมนูคนชอบไข่")
    st.write("- เครปไข่เจียว         ราคา 35 บาท")
    st.write("- ซุปไข่ข้นมะเขือเทศ    ราคา 40 บาท")
    st.write("- ไข่ตุ๋นหมูเด้ง         ราคา 40 บาท")
    st.write("- ไข่ลูกเขยระเบิด       ราคา 39 บาท")

with st.container(border=True):
    st.subheader("ส่วนลดของทางร้าน")
    st.write("- ซื้อครบ 300 บาท ลด 10%")
    st.write("- ซื้อครบ 500 บาท ลด 20%")

st.divider()
st.title("ระบบเลือกรายการอาหาร")

# กำหนดราคาสินค้า/บริการตั้งต้น
menu_prices = {
    "เครปไข่เจียว": 35,
    "ซุปไข่ข้นมะเขือเทศ": 40,
    "ไข่ตุ๋นหมูเด้ง": 40,
    "ไข่ลูกเขยระเบิด": 39,
}

# Session State สำหรับเก็บตะกร้าสินค้า และสถานะการพิมพ์ใบเสร็จ
if "cart" not in st.session_state:
    st.session_state.cart = []
if "show_receipt" not in st.session_state:
    st.session_state.show_receipt = False


# ฟังก์ชันเพิ่มรายการ
def add_item():
    item = st.session_state.new_item
    st.session_state.cart.append(item)
    st.session_state.show_receipt = False  # ซ่อนใบเสร็จชั่วคราวเมื่อมีการเพิ่มสินค้าใหม่


# ฟังก์ชันล้างข้อมูล
def clear_all():
    st.session_state.cart = []
    st.session_state.show_receipt = False


# ==========================================
# ส่วนที่ 2: ฟอร์มเลือกรายการใส่ตะกร้า
# ==========================================
col_select, col_btn = st.columns([3, 1])

with col_select:
    st.selectbox(
        "เลือกรายการที่ต้องการ (เลือกซ้ำได้)",
        list(menu_prices.keys()),
        key="new_item",
    )

with col_btn:
    st.write("")  # จัดระยะเว้นบรรทัดให้ตรงกับ selectbox
    st.write("")
    st.button("➕ เพิ่มใส่ตะกร้า", on_click=add_item, use_container_width=True)

# แสดงรายการที่อยู่ในตะกร้าขณะนี้
if st.session_state.cart:
    st.markdown("### 🛒 รายการในตะกร้าของคุณ")
    counts = Counter(st.session_state.cart)
    for item_name, qty in counts.items():
        price = menu_prices[item_name]
        st.write(
            f"• *{item_name}* x {qty} จาน — (รวม {price * qty:,.2f} บาท)"
        )

    st.write("")
    col_calc, col_clear = st.columns([2, 1])

    with col_calc:
        # ปุ่มสำหรับกดคิดเงินและแสดงใบเสร็จ
        if st.button(
            "🧾 ออกใบเสร็จและคำนวณเงิน",
            type="primary",
            use_container_width=True,
        ):
            st.session_state.show_receipt = True

    with col_clear:
        st.button(
            "🗑️ ล้างตะกร้า",
            on_click=clear_all,
            use_container_width=True,
        )
else:
    st.info("กรุณาเลือกเมนูอาหารแล้วกด 'เพิ่มใส่ตะกร้า'")

# ==========================================
# ส่วนที่ 3: ใบเสร็จรับเงิน (แสดงเมื่อกดปุ่มคิดเงิน)
# ==========================================
if st.session_state.show_receipt and st.session_state.cart:
    st.divider()

    # คำนวณราคารวม
    subtotal = sum(menu_prices[item] for item in st.session_state.cart)

    # คำนวณส่วนลดตามเงื่อนไข
    discount_percent = 0
    if subtotal >= 500:
        discount_percent = 20
    elif subtotal >= 300:
        discount_percent = 10

    discount_amount = subtotal * (discount_percent / 100)
    net_total = subtotal - discount_amount

    # แสดงผลใบเสร็จในลักษณะ Receipt Box
    with st.container(border=True):
        st.markdown(
            "<h2 style='text-align: center;'>🧾 ใบเสร็จรับเงิน / RECEIPT</h2>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='text-align: center; color: gray;'>ร้าน Khai Kue Chiwit (ไข่คือชีวิต)</p>",
            unsafe_allow_html=True,
        )
        st.caption(
            f"วันที่-เวลา: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        st.text("-" * 55)

        # หัวตารางรายการ
        st.markdown(
            "*{:^5} {:<25} {:^8} {:>10}*".format(
                "ลำดับ", "รายการ", "จำนวน", "ราคารวม"
            )
        )
        st.text("-" * 55)

        # รายการสินค้า
        counts = Counter(st.session_state.cart)
        for idx, (item_name, qty) in enumerate(counts.items(), 1):
            item_price = menu_prices[item_name] * qty
            st.text(
                f"{idx:^5} {item_name:<25} x{qty:^6} {item_price:>8,.2f} บ."
            )

        st.text("=" * 55)

        # สรุปยอดเงิน
        st.text(f"ราคารวมทั้งหมด (Subtotal):           {subtotal:>10,.2f} บาท")

        if discount_percent > 0:
            st.text(
                f"ส่วนลด {discount_percent}% (Discount):               -{discount_amount:>10,.2f} บาท"
            )
        else:
            st.text(
                f"ส่วนลด (Discount):                        {0.0:>10,.2f} บาท"
            )

        st.text("-" * 55)
        st.markdown(
            f"### *ยอดชำระสุทธิ (Net Total): {net_total:,.2f} บาท*"
        )
        st.text("=" * 55)

        # แสดงข้อความสิทธิประโยชน์ส่วนลดเพิ่มเติม
        if subtotal < 300:
            st.info(
                f"💡 ซื้อเพิ่มอีก {300 - subtotal:,.2f} บาท เพื่อรับส่วนลด 10%"
            )
        elif subtotal < 500:
            st.success(
                f"🎉 คุณได้รับส่วนลด 10% (ซื้อเพิ่มอีก {500 - subtotal:,.2f} บาท เพื่อรับส่วนลด 20%)"
            )
        else:
            st.success("🔥 คุณได้รับส่วนลดสูงสุด 20%!")

        st.markdown(
            "<p style='text-align: center; margin-top: 15px;'>🙏 ขอบคุณที่อุดหนุนครับ 🙏</p>",
            unsafe_allow_html=True,
        )
