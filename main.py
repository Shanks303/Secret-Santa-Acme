from src.file_handler import FileHandler
from src.secret_santa_assigner import SecretSantaAssigner
from src.validator import Validator

def main():
    # Read the CSV files for employees and previous assignments.
    employees = FileHandler.read_csv("data/employees.csv")
    previous_assignments = FileHandler.read_csv("data/previous_assignments.csv")
    
    # Check if employees were loaded successfully.
    if not employees:
        print("No employees found. Exiting...")
        return
    
    # Validate that employee emails are unique.
    if not Validator.validate_employees(employees):
        print("Duplicate employee emails found. Exiting...")
        return
    
    # Create the Secret Santa assignment using the given data.
    assigner = SecretSantaAssigner(employees, previous_assignments)
    assignments = assigner.assign_santa()
    
    # Write the new assignments to an output CSV file.
    output_file = "output/new_assignments.csv"
    FileHandler.write_csv(
        output_file, 
        assignments, 
        ["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"]
    )
    
    print(f"Assignments saved to {output_file}")

if __name__ == "__main__":
    main()
