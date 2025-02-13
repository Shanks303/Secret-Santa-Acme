# Secret Santa Acme

A Python-based Secret Santa assignment system for Acme. This project automates the process of assigning Secret Santas by reading employee data from CSV files, ensuring that:

- No employee is assigned to themselves.
- No employee receives the same assignment as in the previous year.
- Each employee is paired exactly once.

## Table of Contents

- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Version Control & .gitignore](#version-control--gitignore)

## Project Overview

This project uses a modular design with object-oriented programming principles. It consists of:

- **FileHandler**: Reads and writes CSV files.
- **SecretSantaAssigner**: Contains the logic for generating valid Secret Santa assignments.
- **Validator**: Ensures employee data integrity (e.g., no duplicate emails).

The system also supports a mechanism to avoid repeating last year's assignments and uses recursive retry logic to handle any assignment conflicts.

## Directory Structure

```
Secret-santa-acme/ ├── data/ │ ├── employees.csv │ └── previous_assignments.csv ├── output/ │ └── .gitkeep ├── src/ │ ├── init.py │ ├── file_handler.py │ ├── secret_santa_assigner.py │ └── validator.py ├── tests/ │ └── test_santa_assigner.py ├── .gitignore ├── README.md ├── requirements.txt └── main.py
```

## Setup & Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/Secret-santa-acme.git
   cd Secret-santa-acme
   ```
2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

The main entry point is main.py, which reads the employee CSV files, processes the assignments, and writes the results to an output CSV.

1. Prepare CSV Files:

   Place your employees.csv and previous_assignments.csv inside the data/ directory.
   (Contents for these files are already included in the project folders.)

2. Run the Application:
   ```bash
   python main.py
   ```
   The new Secret Santa assignments will be saved in output/new_assignments.csv.

## Running Tests

The project uses pytest for testing. Tests cover CSV file handling, validation, and assignment logic.

1. Install pytest:
   ```bash
   pip install pytest
   ```
2. Run Tests from the Project Root:
   ```bash
    pytest
   ```
   Ensure you run the command from the root directory so that the src package is discoverable.
   If you encounter import errors, verify that your directory structure is correct and consider adding the project root to sys.path in your test files.

## Version Control & .gitignore

To include the output folder in your repository but ignore its contents, add the following lines to your .gitignore file:

```bash
# Ignore all files in output except .gitkeep
output/*
!output/.gitkeep
```

Make sure to create an empty .gitkeep file inside the output folder. This ensures the folder is tracked even though its generated files are not.
