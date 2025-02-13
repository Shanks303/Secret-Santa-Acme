# tests/test_santa_assigner.py
import os
import sys
import tempfile
import pytest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.file_handler import FileHandler
from src.secret_santa_assigner import SecretSantaAssigner
from src.validator import Validator

# Sample employee data for tests
@pytest.fixture
def sample_employees():
    return [
        {"Employee_Name": "John Doe", "Employee_EmailID": "john.doe@example.com"},
        {"Employee_Name": "Jane Smith", "Employee_EmailID": "jane.smith@example.com"},
        {"Employee_Name": "Alice Johnson", "Employee_EmailID": "alice.johnson@example.com"},
        {"Employee_Name": "Bob Brown", "Employee_EmailID": "bob.brown@example.com"}
    ]

# Sample previous assignments data for tests
@pytest.fixture
def sample_previous_assignments():
    return [
        {
            "Employee_Name": "John Doe",
            "Employee_EmailID": "john.doe@example.com",
            "Secret_Child_Name": "Jane Smith",
            "Secret_Child_EmailID": "jane.smith@example.com"
        },
        {
            "Employee_Name": "Jane Smith",
            "Employee_EmailID": "jane.smith@example.com",
            "Secret_Child_Name": "Bob Brown",
            "Secret_Child_EmailID": "bob.brown@example.com"
        },
        {
            "Employee_Name": "Alice Johnson",
            "Employee_EmailID": "alice.johnson@example.com",
            "Secret_Child_Name": "John Doe",
            "Secret_Child_EmailID": "john.doe@example.com"
        },
        {
            "Employee_Name": "Bob Brown",
            "Employee_EmailID": "bob.brown@example.com",
            "Secret_Child_Name": "Alice Johnson",
            "Secret_Child_EmailID": "alice.johnson@example.com"
        }
    ]

def test_validator_valid(sample_employees):
    # Validator should return True when there are no duplicate emails.
    assert Validator.validate_employees(sample_employees)

def test_validator_duplicate():
    # Create a list with duplicate emails.
    employees = [
        {"Employee_Name": "John Doe", "Employee_EmailID": "john.doe@example.com"},
        {"Employee_Name": "John Duplicate", "Employee_EmailID": "john.doe@example.com"}
    ]
    assert not Validator.validate_employees(employees)

def test_assignment_no_self(sample_employees, sample_previous_assignments):
    assigner = SecretSantaAssigner(sample_employees, sample_previous_assignments)
    assignments = assigner.assign_santa()
    
    for giver in sample_employees:
        # Find the assignment for the current giver.
        assignment = next(
            (a for a in assignments if a["Employee_EmailID"] == giver["Employee_EmailID"]), 
            None
        )
        assert assignment is not None, "Assignment for a giver not found."
        # Ensure that the giver is not assigned to themselves.
        assert giver["Employee_EmailID"] != assignment["Secret_Child_EmailID"]

def test_assignment_not_previous(sample_employees, sample_previous_assignments):
    assigner = SecretSantaAssigner(sample_employees, sample_previous_assignments)
    assignments = assigner.assign_santa()
    
    for assignment in assignments:
        giver_email = assignment["Employee_EmailID"]
        # Retrieve the previous recipient for this giver if available.
        previous = next((a for a in sample_previous_assignments if a["Employee_EmailID"] == giver_email), None)
        if previous:
            # The new assignment should not match last year's assignment.
            assert assignment["Secret_Child_EmailID"] != previous["Secret_Child_EmailID"]

def test_file_handler_read_write():
    # Create some test data.
    data = [{"Employee_Name": "Test User", "Employee_EmailID": "test@example.com"}]
    fieldnames = ["Employee_Name", "Employee_EmailID"]
    
    # Use a temporary file to test writing and then reading.
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, newline="") as tmpfile:
        tmp_filename = tmpfile.name
        FileHandler.write_csv(tmp_filename, data, fieldnames)
        # Read the file back.
        read_data = FileHandler.read_csv(tmp_filename)
    
    # Clean up the temporary file.
    os.remove(tmp_filename)
    
    # The read data should match the data we wrote.
    assert read_data == data
