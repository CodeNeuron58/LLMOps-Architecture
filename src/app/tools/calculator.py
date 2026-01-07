from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers together."""
    return a * b

# Note: The "Docstring" (the text in triple quotes) is actually sent to the LLM so it knows when and how to use this tool.