import streamlit as st

st.set_page_config(page_title="My Gallery")

st.title("My Gallery")

names = [
    "NAME 1", "NAME 2", "NAME 3",
    "NAME 4", "NAME 5", "NAME 6",
    "NAME 7", "NAME 8", "NAME 9"
]

for row in range(3):
    col1, col2, col3 = st.columns(3)

    for col, i in zip(
        [col1, col2, col3],
        range(row * 3, row * 3 + 3)
    ):
        with col:

            st.image(
                f"images/photo{i + 1}.jpg",
                use_container_width=True
            )

            st.markdown(
                f"""
                <div style="
                    border: 1px solid black;
                    padding: 10px;
                    margin: 5px;
                    text-align: center;
                ">
                    <h3>{names[i]}</h3>
                </div>
                """,
                unsafe_allow_html=True
            )
