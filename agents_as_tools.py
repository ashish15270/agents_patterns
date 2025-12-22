from open_ai_env import env_func
env_func()

from agents import Agent, Runner, trace, MessageOutputItem, ItemHelpers
import asyncio

french_agent=Agent(name="french_agent",instructions="You translate the user's message to french", handoff_description="An english to french translator")
italian_agent=Agent(name="italian_agent", instructions="You translate the user's message to italian",handoff_description="An english to italian translator")
spanish_agent=Agent(name="spanish_agent", instructions="You translate the user's message to Spanish",handoff_description="An english to spanish translator")

tools=[french_agent.as_tool(tool_name="translate to french",
description="Translate user's message to french"),
spanish_agent.as_tool(tool_name="translate to spanish",
description="Translate user's message to spanish"),
italian_agent.as_tool(tool_name="translate to italian",
description="Translate user's message to italian")]

syntesiser_agent=Agent(name="synthesiser agent", instructions="You inspect translations, correct them if needed, and produce a final concatenated response.",)

orchestrator_agent=Agent(name="orchestrator_agent", description="You are a translation agent. You use the tools given to you to translate."
        "If asked for multiple translations, you call the relevant tools in order."
        "You never translate on your own, you always use the provided tools."
        tools=tools)
        
async def main():
    msg=input("Hi! What would you like translated, and to which languages? ")
    
    with trace("translations"):
        orchestration_output=await Runner.run(orchestrator_agent,msg)
        
    for item in orchestration_output.new_items:
        if isinstance(item,MessageOutputItem):
            text=ItemHelpers.text_message_output(item)
            
            if text:
                print(f"  - Translation step: {text}")
                
        synthesise=await Runner.run(syntesiser_agent,orchestration_output.to_input_list())
        
    print(f"\n\nFinal response:\n{synthesise.final_output}")


if __name__ == "__main__":
    asyncio.run(main())
    
    
