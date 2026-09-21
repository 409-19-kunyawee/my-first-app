import tkinter as tk

window = tk.Tk()
window.title("My Gallery")
window.geometry("900x800")

names = [
    "NAME 1", "NAME 2", "NAME 3",
    "NAME 4", "NAME 5", "NAME 6",
    "NAME 7", "NAME 8", "NAME 9"
]

for i in range(9):

    # ช่องแต่ละช่อง
    frame = tk.Frame(
        window,
        borderwidth=1,
        relief="solid",
        padx=30,
        pady=30
    )

    row = i // 3
    column = i % 3

    frame.grid(
        row=row,
        column=column,
        sticky="nsew"
    )

    # ช่องรูป
    photo = tk.Label(
        frame,
        text="PHOTO",
        width=18,
        height=6,
        borderwidth=2,
        relief="solid"
    )

    photo.pack()

    # ชื่อ
    name = tk.Label(
        frame,
        text=names[i],
        font=("Arial", 20)
    )

    name.pack(pady=15)


# ทำให้ 3 คอลัมน์กว้างเท่ากัน
for i in range(3):
    window.grid_columnconfigure(i, weight=1)

# ทำให้ 3 แถวสูงเท่ากัน
for i in range(3):
    window.grid_rowconfigure(i, weight=1)

window.mainloop()
