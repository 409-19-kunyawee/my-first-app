from tabulate import tabulate

# assign data
a = [
    ["Nikhil", "Delhi"], 
    ["Ravi", "Kanpur"], 
    ["Manish", "Ahmedabad"], 
    ["Prince", "Bangalore"]
]

# create header
headers = ["Name", "City"]

print(tabulate(a, headers=headers, tablefmt="grid"))
