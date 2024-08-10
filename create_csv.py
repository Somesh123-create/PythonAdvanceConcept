import csv

# Sample data to be written to CSV
employee_data = [
    ["name", "age", "title", "department", "paygrade"],
    ["Alice", 30, "Software Engineer", "Engineering", 5],
    ["Bob", 45, "Project Manager", "Management", 7],
    ["Charlie", 25, "Data Analyst", "Data Science", 4],
    ["Diana", 35, "Product Manager", "Product", 6],
    ["Eve", 28, "UX Designer", "Design", 5],
    ["Frank", 50, "CTO", "Executive", 9],
    ["Grace", 40, "HR Manager", "Human Resources", 6],
    ["Henry", 32, "DevOps Engineer", "Engineering", 5],
    ["Isabel", 29, "Marketing Specialist", "Marketing", 4],
    ["John", 27, "Sales Representative", "Sales", 4]
]

# Define the CSV file name
csv_file = "employees.csv"

# Write the sample data to CSV
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(employee_data)

print(f"CSV file '{csv_file}' created successfully.")
