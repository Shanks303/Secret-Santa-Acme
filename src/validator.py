from typing import List, Dict

class Validator:
    """Handles input validation."""
    @staticmethod
    def validate_employees(employees: List[Dict[str, str]]) -> bool:
        emails = {e['Employee_EmailID'] for e in employees}
        return len(emails) == len(employees)  

