st.divider()
st.subheader("🛒 สรุปรายการสั่งซื้อ")

# ตรวจสอบว่ามีการเลือกสินค้าหรือยัง
if st.session_state.selected_items:
    # 1. คำนวณราคารวมก่อนหักส่วนลด (Subtotal)
    subtotal = sum(item["price"] for item in st.session_state.selected_items)
    
    # 2. คำนวณส่วนลดตามเงื่อนไข
    discount_percent = 0
    if subtotal >= 500:
        discount_percent = 20
    elif subtotal >= 300:
        discount_percent = 10
        
    discount_amount = subtotal * (discount_percent / 100)
    total_price = subtotal - discount_amount

    # 3. แสดงรายการสินค้าที่เลือกไว้
    for idx, item in enumerate(st.session_state.selected_items, 1):
        st.write(f"{idx}. {item['item']}")
    
    st.divider()

    # 4. แสดงผลสรุปยอดเงิน
    col1, col2, col3 = st.columns(3)
    col1.metric("ราคารวม", f"{subtotal:,.2f} บาท")
    col2.metric("ส่วนลด", f"{discount_percent}% (-{discount_amount:,.2f} บาท)")
    col3.metric("ยอดรวมสุทธิ", f"{total_price:,.2f} บาท")

    # แจ้งเตือนสิทธิประโยชน์ส่วนลด
    if subtotal < 300:
        st.info(f"💡 ซื้อเพิ่มอีก {300 - subtotal:,.2f} บาท เพื่อรับส่วนลด 10%")
    elif subtotal < 500:
        st.info(f"🎉 คุณได้รับส่วนลด 10%! (ซื้อเพิ่มอีก {500 - subtotal:,.2f} บาท เพื่อรับส่วนลด 20%)")
    else:
        st.success("🔥 คุณได้รับส่วนลดสูงสุด 20%!")

    # ปุ่มสำหรับล้างรายการทั้งหมด
    st.button("🗑️ ล้างรายการทั้งหมด", on_click=clear_all, type="primary")

else:
    st.info("ยังไม่มีรายการที่เลือก กรุณาเลือกสินค้าแล้วกด 'เพิ่มรายการนี้'")
