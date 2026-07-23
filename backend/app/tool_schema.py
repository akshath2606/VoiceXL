from google.genai import types

write_tool = types.FunctionDeclaration(
    name="write_cell",
    description="Writes a value to a specific cell in an Excel worksheet.",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "sheet_name": {
                "type": "string",
                "description": "The name of the worksheet to write to."
            },
            "cell_reference": {
                "type": "string",
                "description": "The cell reference (e.g., A1, B2) where the value should be written."
            },
            "value": {
                "type": "string",
                "description": "The value to write into the specified cell."
            }
        },
        "required": [
            "sheet_name",
            "cell_reference",
            "value"
        ]
    }
)

read_tool = types.FunctionDeclaration(
    name="read_cell",
    description="Reads the value from a specific cell in an Excel worksheet.",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "sheet_name": {
                "type": "string",
                "description": "The name of the worksheet to read from."
            },
            "cell_reference": {
                "type": "string",
                "description": "The cell reference (e.g., A1, B2) to read."
            }
        },
        "required": [
            "sheet_name",
            "cell_reference"
        ]
    }
)

excel_tool = types.Tool(
    function_declarations=[
        write_tool,
        read_tool
    ]
)