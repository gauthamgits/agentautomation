import json
import os
from anthropic import Anthropic
from agent.jira_client import JiraClient
from config.settings import Settings

client = Anthropic()

SYSTEM_PROMPT = """
You are a senior test automation engineer working with a Python + Playwright + pytest framework.

Your job:
1. Read the FRAMEWORK_GUIDE.md first — always
2. Check existing components to avoid duplication
3. Read the user story and extract each testable acceptance criterion
4. Generate a page object if the test is UI-based
5. Generate the pytest test file covering every acceptance criterion

Strict rules:
- Follow the framework conventions exactly as described in FRAMEWORK_GUIDE.md
- UI tests must subclass BasePage
- Name test functions as test_<action>_<expected_outcome>
- Write one test function per acceptance criterion
- Output only valid Python code, no markdown fences, no explanations
"""

tools = [
    {
        "name": "read_framework_guide",
        "description": "Read FRAMEWORK_GUIDE.md before generating any code",
        "input_schema": {"type": "object", "properties": {}}
    },
    {
        "name": "list_existing_components",
        "description": "List existing page objects and service clients to avoid duplication",
        "input_schema": {"type": "object", "properties": {}}
    },
    {
        "name": "write_file",
        "description": "Write a Python file to the project",
        "input_schema": {
            "type": "object",
            "properties": {
                "filepath": {"type": "string"},
                "content": {"type": "string"}
            },
            "required": ["filepath", "content"]
        }
    }
]

written_files = {}

def handle_tool(name, inputs):
    global written_files

    if name == "read_framework_guide":
        return open("FRAMEWORK_GUIDE.md").read()

    if name == "list_existing_components":
        pages = os.listdir("tests/pages")
        services = os.listdir("tests/services")
        return json.dumps({"page_objects": pages, "service_clients": services})

    if name == "write_file":
        filepath = inputs["filepath"]
        content = inputs["content"]
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as f:
            f.write(content)
        written_files[filepath] = content
        print(f"  ✓ Written: {filepath}")
        return f"File written: {filepath}"

def run_agent(story_key: str):
    global written_files
    written_files = {}

    print(f"\n🔍 Fetching story {story_key} from Jira...")
    jira = JiraClient()
    story = jira.get_story(story_key)

    print(f"📋 Summary: {story['summary']}")
    print(f"🤖 Agent is generating tests...\n")

    messages = [{
        "role": "user",
        "content": (
            f"Generate tests for Jira story {story['key']}.\n\n"
            f"Summary: {story['summary']}\n\n"
            f"User Story:\n{story['description']}"
        )
    }]

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            tools=tools,
            messages=messages
        )

        if response.stop_reason == "end_turn":
            print("\n✅ Done! Files generated:")
            for f in written_files:
                print(f"   → {f}")
            break

        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                print(f"  🔧 {block.name}")
                result = handle_tool(block.name, block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result
                })

        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})

if __name__ == "__main__":
    import sys
    run_agent(sys.argv[1])