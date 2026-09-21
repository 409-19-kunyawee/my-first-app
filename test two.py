import pandas as pd

# Load your data
df = pd.read_csv('sales_data.csv')

# Create a basic pivot table
pivot = pd.pivot_table(
    df,
    values='Sales',
    index='Region',
    columns='Product',
    aggfunc='sum',
    fill_value=0
)

# Display the pivot table
print(pivot)

# Export to Excel
pivot.to_excel('sales_pivot.xlsx', sheet_name='Sales Summary')
