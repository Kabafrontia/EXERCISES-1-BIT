import array

# 🧮 Integers: Quantities of ID cards printed per day
daily_prints = [120, 135, 150, 110, 145, 160, 130]
total_prints = sum(daily_prints)
average_prints = total_prints / len(daily_prints)
min_prints = min(daily_prints)
max_prints = max(daily_prints)

# 📝 Strings: Formatted report using f-strings
report = (
    f"📊 University ID Card Print Queue Report\n"
    f"Total cards printed this week: {total_prints}\n"
    f"Average daily prints: {average_prints:.2f}\n"
    f"Minimum daily prints: {min_prints}\n"
    f"Maximum daily prints: {max_prints}\n"
)
print(report)

# ✅ Booleans: Threshold check
threshold = 140
if average_prints > threshold and max_prints > 150:
    print("Status: Above Standard ✅")
else:
    print("Status: Below Standard ⚠️")

# 📋 Lists: Maintain and modify print queue
print_queue = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
print("Original Queue:", print_queue)

# Add new element
print_queue.append("Fiona")

# Remove one based on condition (e.g., name starts with 'C')
print_queue = [name for name in print_queue if not name.startswith("C")]

# Sort and display
print_queue.sort()
print("Modified & Sorted Queue:", print_queue)

# 📦 Arrays: Fixed-size numeric subset
subset_array = array.array('i', daily_prints[:5])  # First 5 days
array_sum = sum(subset_array)
list_sum = sum(daily_prints[:5])
print(f"Array Sum: {array_sum}, List Sum: {list_sum}")

# 🗂️ Dictionaries: List of records
records = [
    {"id": 101, "name": "Alice", "value": 120},
    {"id": 102, "name": "Bob", "value": 135},
    {"id": 103, "name": "Charlie", "value": 150},
    {"id": 104, "name": "Diana", "value": 110},
]

# Update one record (e.g., Bob's value)
for record in records:
    if record["name"] == "Bob":
        record["value"] = 140

# Delete another (e.g., Charlie)
records = [r for r in records if r["name"] != "Charlie"]

# Compute total value
total_value = sum(r["value"] for r in records)
print(f"Total Value of Remaining Records: {total_value}")