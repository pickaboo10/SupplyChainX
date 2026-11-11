"""Check that your Gemini API key and model work, outside Nonilion."""
import os
from google import genai

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

key = os.environ.get("GEMINI_API_KEY")
if not key:
    raise SystemExit("GEMINI_API_KEY is not set. Copy .env.example to .env and add your key.")

client = genai.Client(api_key=key.strip())

print("Models available to this key:")
for m in client.models.list():
    print(" ", m.name)

# Run the real agent instructions against the P101 prompt
instructions = open("agent_instructions.md", encoding="utf-8").read()
prompt = ("Our Delhi warehouse has only 20 units of Product P101. "
          "Check other warehouses and find the best way to avoid a stockout.")
r = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt,
    config={"system_instruction": instructions},
)
print("\n--- Agent reply ---\n")
print(r.text)
