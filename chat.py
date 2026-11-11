"""Interactive multi-turn CLI chat for SupplyChainX using Gemini."""
from pathlib import Path
import os
from google import genai

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().with_name(".env"), override=True)
except ImportError:
    pass


def main() -> None:
    """Run an interactive chat loop against agent_instructions.md."""
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        raise SystemExit("GEMINI_API_KEY is not set. Copy .env.example to .env and add your key.")

    instructions_path = Path(__file__).resolve().with_name("agent_instructions.md")
    instructions = instructions_path.read_text(encoding="utf-8")

    client = genai.Client(api_key=key.strip())
    chat = client.chats.create(
        model="gemini-3.8-flash",
        config={"system_instruction": instructions},
    )

    print("SupplyChainX interactive chat ready. Type 'exit' or 'quit' to stop.\n")
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting chat.")
            break

        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            print("Exiting chat.")
            break

        response = chat.send_message(user_input)
        print(f"\nAgent:\n{response.text}\n")


if __name__ == "__main__":
    main()

