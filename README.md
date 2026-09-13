# Operation Automation

Terminal application written in Python for managing operational incidents. It lets a user register, review, find, update, delete, and review the general situation of incident records.

The application stores its data locally in `tickets.json`, so changes remain available the next time it is run.

## Features

- Register a new incident with an automatically assigned ID.
- View all stored incidents.
- Find an incident by its ID.
- Update a field in an existing incident.
- Delete an incident by its ID.
- View incidents ordered by the number of affected users.
- Validate required entries and handle invalid numeric menu and ID input.

## Project structure

```text
operation_automation/
├── operation_automation.py  # Main terminal application
├── tickets.json             # Local incident data
└── README.md                # Project documentation
```

## Requirements

- Python 3

No external packages are required; the project uses Python's built-in `json` module.

## How to run

1. Open a terminal in the `operation_automation` folder.
2. Run:

   ```powershell
   python operation_automation.py
   ```

3. Choose an option from the menu by entering a number from `1` to `7`.

> Run the program from this folder. It reads and writes `tickets.json` using a relative path.

## Incident data

Each incident is saved as a JSON object with these fields:

```json
{
    "id": 1,
    "name": "juan",
    "lastname": "perez",
    "information": "system access problem",
    "scope": 3,
    "priority": "high"
}
```

`scope` represents the number of affected users. The **General Situation** option displays incidents sorted from the lowest to the highest scope.

## Current limitations

- This is a terminal application; it does not have a graphical interface.
- The JSON file must already exist and contain valid JSON when the program starts.
- Updates accept the name of an existing field and save the entered value as text, so numeric values are not revalidated during an update.
- There are no automated tests yet.

## Learning goals

This project practices Python fundamentals including functions, loops, conditionals, input validation, lists and dictionaries, JSON file handling, sorting, and basic CRUD operations.
