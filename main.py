
from database.db import connect_db, create_table
from api.weather_api import get_weather
from utils.logger import logger

def add_employee():
    name = input("Enter employee name: ").strip()
    department = input("Enter department: ").strip()

    try:
        salary = float(input("Enter salary: "))
        if not name or not department or salary < 0:
            print("Invalid employee details.")
            return
    except ValueError:
        print("Please enter a valid salary.")
        return

    conn = connect_db()
    conn.execute(
        "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
        (name, department, salary)
    )
    conn.commit()
    conn.close()
    print("Employee added successfully!")
    logger.info("Employee added successfully")


def view_employees():
    conn = connect_db()
    employees = conn.execute(
        "SELECT * FROM employees ORDER BY id"
    ).fetchall()
    conn.close()

    if not employees:
        print("No employee records found.")
        return

    print("\nID | Name | Department | Salary")
    print("-" * 40)
    for employee in employees:
        print(
            f"{employee[0]} | {employee[1]} | "
            f"{employee[2]} | {employee[3]:.2f}"
        )


def update_employee():
    try:
        employee_id = int(input("Enter employee ID to update: "))
        salary = float(input("Enter new salary: "))
        if salary < 0:
            print("Salary cannot be negative.")
            return
    except ValueError:
        print("Please enter valid numbers.")
        return

    conn = connect_db()
    cursor = conn.execute(
        "UPDATE employees SET salary = ? WHERE id = ?",
        (salary, employee_id)
    )
    conn.commit()
    conn.close()

    
    if cursor.rowcount:
        print("Employee salary updated successfully!")
        logger.info("Employee salary updated for ID %s", employee_id)
    else:
        print("Employee ID not found.")
        logger.warning("Update failed: employee ID %s not found", employee_id)



def delete_employee():
    try:
        employee_id = int(input("Enter employee ID to delete: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    conn = connect_db()
    cursor = conn.execute(
        "DELETE FROM employees WHERE id = ?",
        (employee_id,)
    )
    conn.commit()
    conn.close()

    
    if cursor.rowcount:
        print("Employee deleted successfully!")
        logger.info("Employee deleted: ID %s", employee_id)
    else:
        print("Employee ID not found.")
        logger.warning("Delete failed: employee ID %s not found", employee_id)


def main():
    create_table()
    logger.info("Employee Management System started")
    while True:
        print("\n=== Employee Management System ===")
        choice = input("Enter your choice: ").strip()

        
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            get_weather()
        elif choice == "6":
            print("Thank you for using Employee Management System!")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
