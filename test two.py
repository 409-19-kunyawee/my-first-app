from tabulate import tabulate

# เตรียมข้อมูลหัวตารางและเนื้อหา
data = [
    ["John", 25, "Thailand"],
    ["Alice", 30, "USA"],
    ["Bob", 22, "Japan"]
]

headers = ["Name", "Age", "Country"]

# สั่งพิมพ์ตารางรูปแบบ grid
print(tabulate(data, headers=headers, tablefmt="grid"))
