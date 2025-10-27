import pandas as pd

data = {
    'FirstName': ['Satvik', 'Avinash', 'Lahri'],
    'LastName': ['Shah', 'Kati', 'Rath'],
    'Email': ['satshah@example.com', 'avinashk@example.com', 'lahri.rath@example.com'],
    'PhoneNumber': [4537829158, 5892184058, 4528727830]
}

# Create DataFrame
df = pd.DataFrame(data)

# Write to Excel file
excel_file = 'Activity19_20.xlsx'
df.to_excel(excel_file, index=False)

print("Excel file created successfully!\n")