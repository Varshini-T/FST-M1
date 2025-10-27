import pandas as pd

data = {
    "Usernames": ["admin", "Varshini", "Tulluri"],
    "Passwords": ["password", "Password", "Test123"]
}

df = pd.read_csv("sample.csv")

print("Data read from CSV file:")
print(df)

# Print only the values in the Usernames column
print("\nUsernames column:")
print(df["Usernames"])

# Print the username and password of the second row
print("\nSecond row details:")
print("Username:", df.loc[1, "Usernames"])
print("Password:", df.loc[1, "Passwords"])

# Sort Usernames column in ascending order and print
print("\nUsernames sorted in ascending order:")
print(df.sort_values("Usernames"))

# Sort Passwords column in descending order and print
print("\nPasswords sorted in descending order:")
print(df.sort_values("Passwords", ascending=False))
