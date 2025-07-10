import csv

# Sample credentials
data = [
    ["email", "password"],
    ["alice123@gmail.com", "ilcnnmdrvohcvzqz"],
    ["bob456@gmail.com", "ilcnnmdrvohcvzqz"],
    ["charlie789@gmail.com", "ilcnnmdrvohcvzqz"],
    ["diana321@gmail.com", "ilcnnmdrvohcvzqz"],
    ["eve654@gmail.com", "ilcnnmdrvohcvzqz"],
    ["frank987@gmail.com", "ilcnnmdrvohcvzqz"],
    ["grace000@gmail.com", "ilcnnmdrvohcvzqz"],
    ["heidi111@gmail.com", "ilcnnmdrvohcvzqz"],
    ["ivan222@gmail.com", "ilcnnmdrvohcvzqz"],
    ["judy333@gmail.com", "ilcnnmdrvohcvzqz"],
]

# Write to file
with open('email_credentials.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("✅ email_credentials.csv created successfully.")
