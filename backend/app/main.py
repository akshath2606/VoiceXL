from fastapi import FastAPI
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

try:
    from backend.app.excel_service import read_cell, write_cell
    from backend.app.tool_schema import excel_tool
except ImportError:
    from excel_service import read_cell, write_cell
    from tool_schema import excel_tool

app = FastAPI()

client = genai.Client()

config = types.GenerateContentConfig(
    tools=[excel_tool],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(
        disable=True
    ),
)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

@app.get("/")
def read_root():
    return {"status": "running"}


if __name__ == "__main__":
    user_input = input("Enter command: ").strip()

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=user_input,
        config=config,
    )

    if not response.function_calls:
        print("No valid function call generated.")
        exit()

    function_call = response.function_calls[0]

    print(f"\nSelected Function: {function_call.name}")
    print(f"Arguments: {function_call.args}\n")

    if function_call.name == "write_cell":
        write_cell(**function_call.args)
        print("Write operation completed.")

    elif function_call.name == "read_cell":
        value = read_cell(**function_call.args)
        print(f"Cell Value: {value}")

    else:
        print(f"Unknown function: {function_call.name}")