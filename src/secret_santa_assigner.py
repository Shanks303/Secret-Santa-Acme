import random
from typing import List, Dict

class SecretSantaAssigner:
    """Handles the Secret Santa assignment logic."""
    def __init__(self, employees: List[Dict[str, str]], previous_assignments: List[Dict[str, str]]):
        self.employees = employees
        self.previous_assignments = {entry['Employee_EmailID']: entry['Secret_Child_EmailID'] for entry in previous_assignments}

    def assign_santa(self) -> List[Dict[str, str]]:
        employees_pool = self.employees[:]
        random.shuffle(employees_pool)
        assignments = []

        for giver in self.employees:
            possible_recipients = [e for e in employees_pool if e['Employee_EmailID'] != giver['Employee_EmailID'] and e['Employee_EmailID'] != self.previous_assignments.get(giver['Employee_EmailID'])]
            
            if not possible_recipients:
                return self.retry_assignment()
            
            recipient = random.choice(possible_recipients)
            employees_pool.remove(recipient)
            assignments.append({
                "Employee_Name": giver['Employee_Name'],
                "Employee_EmailID": giver['Employee_EmailID'],
                "Secret_Child_Name": recipient['Employee_Name'],
                "Secret_Child_EmailID": recipient['Employee_EmailID']
            })
        
        return assignments

    def retry_assignment(self) -> List[Dict[str, str]]:
        print("Reattempting assignment due to conflicts...")
        return self.assign_santa()