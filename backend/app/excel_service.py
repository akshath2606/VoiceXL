from pathlib import Path

from openpyxl import load_workbook

# Hardcoded path to the Excel workbook for Prototype 001.
WORKBOOK_PATH = Path(__file__).resolve().parent.parent / "data" / "Budget.xlsx"

def open_workbook():
    """Open the hardcoded workbook and return its name and worksheet names."""
    try:
        workbook = load_workbook(WORKBOOK_PATH, read_only=True)
        worksheet_names = workbook.sheetnames
        workbook_name = WORKBOOK_PATH.name
        workbook.close()
        return workbook_name, worksheet_names
    except FileNotFoundError:
        print(f"Error: The workbook '{WORKBOOK_PATH}' was not found.")
        return None, None



def sheet_count():
    """Return the number of worksheets in the workbook."""
    _, worksheet_names = open_workbook()
    return len(worksheet_names)


def print_workbook_info():
    """Print the name of the workbook and all worksheet names."""
    workbook_name, worksheet_names = open_workbook()
    print(f"Workbook: {workbook_name}")
    print("\nWorksheets:")
    for i, sheet_name in enumerate(worksheet_names, start=1):
        print(f"{i}. {sheet_name}")

try:
    print_workbook_info()
except FileNotFoundError:
    print(f"Error: The workbook '{WORKBOOK_PATH}' was not found.")

if __name__ == "__main__":
    print_workbook_info()

def validate_workbook():
    """Validate that the workbook exists and can be opened."""
    try:
        load_workbook(WORKBOOK_PATH, read_only=True)
        return True
    except FileNotFoundError:
        print(f"Error: The workbook '{WORKBOOK_PATH}' was not found.")
        return False

