# Import pandas
import pandas as pd

# Create a dictionary with usernames and passwords
data = {
    "Usernames": ["admin", "Charles", "Deku"],
    "Passwords": ["password", "Charli3", "AllMight"]
}

dataframe = pd.DataFrame(data)

# Print the DataFrame
print("Original DataFrame:")
print(dataframe)

# Write the DataFrame to a CSV file
dataframe.to_csv("sample.csv", index=False)
print("\nCSV file 'sample.csv' created successfully!\n")