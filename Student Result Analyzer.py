# Student Result Analyzer

students = []

# Add student
def add_student():
    name = input("Enter student name: ")

    marks = []
    for i in range(3):
        m = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully")

# Calculate result
def calculate_result(student):
    total = sum(student["marks"])
    avg = total / len(student["marks"])

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "Fail"

    return total, avg, grade

# View all results
def view_results():
    if not students:
        print("No data available")
        return

    for s in students:
        total, avg, grade = calculate_result(s)

        print("\nName:", s["name"])
        print("Marks:", s["marks"])
        print("Total:", total)
        print("Average:", round(avg, 2))
        print("Grade:", grade)

# Find topper
def find_topper():
    if not students:
        print("No data available")
        return

    topper = max(students, key=lambda s: sum(s["marks"]))
    total, avg, grade = calculate_result(topper)

    print("\nTopper:", topper["name"])
    print("Total Marks:", total)
    print("Average:", round(avg, 2))

# Sample data
def add_sample_data():
    students.append({"name": "Sanjay", "marks": [85, 90, 88]})
    students.append({"name": "Arun", "marks": [70, 75, 72]})
    students.append({"name": "Priya", "marks": [95, 92, 96]})

# Main menu
def main():
    add_sample_data()

    while True:
        print("\n--- Student Result Analyzer ---")
        print("1. Add Student")
        print("2. View Results")
        print("3. Find Topper")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_results()
        elif choice == "3":
            find_topper()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()
