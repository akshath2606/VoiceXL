# Feature 003 – Write Cell Value

## Status

🟡 Planned

---

## Goal

Implement a service function that writes a value to a specified cell in a worksheet, saves the workbook, and returns the written value.

This feature enables VoiceXL to modify spreadsheet data and forms the foundation for future NLP commands such as:

> "Set B5 to 1200"

---

## Function

```python
write_cell(sheet_name, cell_reference, value)
```

---

## Inputs

| Parameter | Type | Description |
|-----------|------|-------------|
| sheet_name | str | Name of the target worksheet |
| cell_reference | str | Excel cell reference (e.g. "B5") |
| value | Any | Value to write into the cell |

---

## Output

Returns the value that was successfully written.

Example:

```python
result = write_cell("Sheet1", "A1", "Hello")

print(result)
# Hello
```

---

## Responsibilities

The function must:

- Open the configured workbook.
- Verify the worksheet exists.
- Write the provided value into the specified cell.
- Save the workbook.
- Close the workbook correctly.
- Return the written value.

---

## Error Handling

Handle the following cases:

- Workbook does not exist.
- Worksheet does not exist.
- Invalid cell reference (if encountered).
- Ensure the workbook is closed even if an exception occurs.

---

## Out of Scope

This feature does not:

- Validate the data type of the value.
- Support writing multiple cells.
- Apply formatting.
- Support formulas or merged cells.
- Perform undo/redo.

These capabilities will be implemented in future features.

---

## Manual Test Cases

### Test 1

```python
write_cell("Sheet1", "A1", "Hello")
```

Expected:

- A1 contains "Hello"
- Function returns "Hello"

---

### Test 2

```python
write_cell("Sheet1", "B2", 250)
```

Expected:

- B2 contains 250
- Workbook is saved
- Function returns 250

---

### Test 3

Use a worksheet that does not exist.

Expected:

- Appropriate error is raised or handled.
- Workbook closes correctly.

---

### Test 4

Reopen the workbook in Microsoft Excel.

Expected:

- Previously written values are still present.

---

## Engineering Concept

**CRUD – Update**

This feature introduces the **Update** operation of CRUD.

The Excel Service is responsible for updating spreadsheet data while remaining independent of the NLP and voice layers.

---

## Completion Criteria

- [ ] Function implemented
- [ ] Workbook opens successfully
- [ ] Cell value is updated
- [ ] Workbook is saved
- [ ] Workbook closes correctly
- [ ] Manual testing completed
- [ ] Code reviewed
- [ ] Changes committed