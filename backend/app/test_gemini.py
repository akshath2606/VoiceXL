from google import genai
from dotenv import load_dotenv
import os
from google.genai import types
from tool_schema import excel_tool

print(type(excel_tool))

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

config = types.GenerateContentConfig(
    tools=[excel_tool],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(
        disable=True
    ),
)



response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Insert 500 into cell C3 of Budget.",
    config=config
)

if response.function_calls:
    function_call = response.function_calls[0]
    print("Selected function:", function_call.name)
    print("Generated arguments:", function_call.args)
else:
    print("No function call found in the response.")


# from google import genai
# import os
# from dotenv import load_dotenv

# load_dotenv()

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# response = client.models.generate_content(
#     model="gemini-3.6-flash",
#     contents="Say hello"
# )

print(response.text)