from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, ToolMessage
from src.app.tools.calculator import multiply
from src.app.core.config import get_settings
import logging

# Setup structured logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

settings = get_settings()

from typing import List, Any

def run_agent(user_input: str):
    logger.info(f"Received user input: {user_input}")
    llm = ChatGoogleGenerativeAI(model=settings.MODEL_NAME, api_key=settings.GEMINI_API_KEY)

    # Define our tools list
    tools = [multiply]
    llm_with_tools = llm.bind_tools(tools)
    
    # 1. First Pass: LLM decides to use a tool
    messages = [HumanMessage(content=user_input)]
    ai_msg = llm_with_tools.invoke(messages)
    messages.append(ai_msg)
    
    # 2. Check if the LLM requested a tool
    if ai_msg.tool_calls:
        for tool_call in ai_msg.tool_calls:
            try:
                # Execute the actual Python function
                result = multiply.invoke(tool_call["args"])
                status = "success"
            except Exception as e:
                # Capture the error to send back to the LLM
                result = f"Error executing tool: {str(e)}. Please check your inputs."
                status = "failed"
                logger.error(f"Tool execution failed: {tool_call['name']} with error {e}")

            tool_msg = ToolMessage(
                tool_call_id=tool_call["id"],
                content=str(result)
            )
            messages.append(tool_msg)

        # 4. Second Pass: LLM generates the final answer based on tool output
        final_response = llm_with_tools.invoke(messages)
        return final_response.content

    return ai_msg.content