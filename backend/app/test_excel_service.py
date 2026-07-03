from backend.app.excel_service import read_cell, write_cell

print("===== Feature 003 Test =====")

result = write_cell("Sheet1", "A1", "VoiceXL")

print("Returned:", result)

print("Reading Back...")

print(read_cell("Sheet1", "A1"))