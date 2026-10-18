"""Student Grade Analyzer - Starter Code

Complete every section marked TODO. Keep this file and grades.txt in the
same folder. Rename the completed file to student_grade_analyzer_.py.
"""


def classify_grade(grade):
    """Return the classification and status of a grade."""
    if grade >= 90:
        return ("Excellent", "Passed")
    elif grade >= 85:
        return ("Very Good", "Passed")
    elif grade >= 80:
        return ("Good", "Passed")
    elif grade >= 75:
        return ("Satisfactory", "Passed")
    else:
        return ("Needs Improvement", "Failed")


def load_students(filename):
    """Read valid student records from a text file and return them as a list."""
    students = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split(",")

                if len(parts) != 3:
                    continue

                student_id = parts[0].strip()
                name = parts[1].strip()

                try:
                    grade = float(parts[2].strip())
                except ValueError:
                    continue

                if grade < 0 or grade > 100:
                    continue

                students.append({
                    "student_id": student_id,
                    "name": name,
                    "grade": grade
                })

    except FileNotFoundError:
        print("Error: File not found.")

    return students


def calculate_statistics(students):
    """Calculate and return the class statistics."""
    if not students:
        return None

    total_grade = 0
    passed_count = 0
    failed_count = 0
    highest_student = students[0]
    lowest_student = students[0]

    for student in students:
        total_grade += student["grade"]

        classification, status = classify_grade(student["grade"])

        if status == "Passed":
            passed_count += 1
        else:
            failed_count += 1

        if student["grade"] > highest_student["grade"]:
            highest_student = student

        if student["grade"] < lowest_student["grade"]:
            lowest_student = student

    average = total_grade / len(students)

    return {
        "count": len(students),
        "average": average,
        "passed": passed_count,
        "failed": failed_count,
        "highest": highest_student,
        "lowest": lowest_student
    }


def display_students(students):
    """Display all student records in a formatted table."""

    print("\nStudent Records")
    print("-" * 75)
    print(f"{'ID':<12}{'Name':<20}{'Grade':<8}{'Classification':<20}{'Status'}")
    print("-" * 75)

    for student in students:
        classification, status = classify_grade(student["grade"])
        print(
            f"{student['student_id']:<12}"
            f"{student['name']:<20}"
            f"{student['grade']:<8.2f}"
            f"{classification:<20}"
            f"{status}"
        )

    print("-" * 75)


def display_statistics(statistics):
    """Display the calculated class statistics."""

    print("\nClass Statistics")
    print("-" * 30)
    print(f"Total Students: {statistics['count']}")
    print(f"Average Grade: {statistics['average']:.2f}")
    print(f"Passed: {statistics['passed']}")
    print(f"Failed: {statistics['failed']}")
    print(
        f"Highest: {statistics['highest']['name']} - "
        f"{statistics['highest']['grade']:.2f}"
    )
    print(
        f"Lowest: {statistics['lowest']['name']} - "
        f"{statistics['lowest']['grade']:.2f}"
    )
    print("-" * 30)


def search_student(students, keyword):
    """Return records whose student number or name matches the keyword."""
    matches = []

    keyword = keyword.strip().lower()

    for student in students:
        if (
            keyword in student["student_id"].lower()
            or keyword in student["name"].lower()
        ):
            matches.append(student)

    return matches


def save_report(students, statistics, filename):
    """Write the student results and class statistics to a report file."""

    try:
        with open(filename, "w") as file:
            file.write("STUDENT GRADE REPORT\n")
            file.write("=" * 50 + "\n\n")

            for student in students:
                classification, status = classify_grade(student["grade"])

                file.write(
                    f"{student['student_id']} - "
                    f"{student['name']} - "
                    f"{student['grade']:.2f} - "
                    f"{classification} - "
                    f"{status}\n"
                )

            file.write("\nCLASS STATISTICS\n")
            file.write("=" * 50 + "\n")
            file.write(f"Total Students: {statistics['count']}\n")
            file.write(f"Average Grade: {statistics['average']:.2f}\n")
            file.write(f"Passed: {statistics['passed']}\n")
            file.write(f"Failed: {statistics['failed']}\n")
            file.write(
                f"Highest: {statistics['highest']['name']} - "
                f"{statistics['highest']['grade']:.2f}\n"
            )
            file.write(
                f"Lowest: {statistics['lowest']['name']} - "
                f"{statistics['lowest']['grade']:.2f}\n"
            )

        print(f"Report saved to {filename}")

    except OSError:
        print("Error: Could not write the report file.")


def main():
    """Run the menu-driven Student Grade Analyzer."""

    students = load_students("grades.txt")

    if not students:
        print("No valid student records were loaded.")
        return

    statistics = calculate_statistics(students)

    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_students(students)

        elif choice == "2":
            display_statistics(statistics)

        elif choice == "3":
            keyword = input("Enter student ID or name: ").strip()
            matches = search_student(students, keyword)

            if matches:
                display_students(matches)
            else:
                print("No matching student found.")

        elif choice == "4":
            save_report(students, statistics, "grade_report.txt")

        elif choice == "5":
            print("Thank you for using Student Grade Analyzer.")
            break

        else:
            print("Invalid choice. Please try again.")
            continue


if __name__ == "__main__":
    main()