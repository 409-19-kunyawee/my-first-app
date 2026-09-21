import streamlit as st

st.set_page_config(
    page_title="My Gallery",
    layout="wide"
)

st.title("My Gallery")

names = [
    "NAME 1", "NAME 2", "NAME 3",
    "NAME 4", "NAME 5", "NAME 6",
    "NAME 7", "NAME 8", "NAME 9"
]

for row in range(3):
    cols = st.columns(3)

    for col in range(3):
        index = row * 3 + col

        with cols[col]:
            st.image(
                f"images/photo{index + 1}.jpg",
                width=180
            )
            st.write(names[index])
