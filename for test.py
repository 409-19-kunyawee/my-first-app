import streamlit as st

st.title("ระบบคำนวณส่วนลดสินค้า")

# รับค่ายอดซื้อจากผู้ใช้
total_price = st.number_input("กรอกยอดซื้อรวม (บาท):", min_value=0.0, step=100.0)

# กำหนดเงื่อนไขยอดซื้อขั้นต่ำ เช่น ต้อง 1,000 บาทขึ้นไปจึงจะใช้ส่วนลดได้
min_amount_for_discount = 1000.0

if total_price < min_amount_for_discount:
    st.warning(f"ยอดซื้อยังไม่ถึง {min_amount_for_discount:,.0f} บาท ไม่สามารถใช้ส่วนลดได้")
    net_price = total_price
    st.write(f"*ยอดชำระสุทธิ:* {net_price:,.2f} บาท")
else:
    # เงื่อนไขเมื่อถึงยอดขั้นต่ำ (เช่น ลด 10%)
    discount = total_price * 0.10
    net_price = total_price - discount
    
    st.success("ยินดีด้วย! คุณได้รับส่วนลด 10%")
    st.write(f"ส่วนลด: {discount:,.2f} บาท")
    st.write(f"*ยอดชำระสุทธิหลังหักส่วนลด:* {net_price:,.2f} บาท")
