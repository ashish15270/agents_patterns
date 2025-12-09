'''

while True:	Multi‑turn conversation loop
with trace(...)	Log this turn for debugging
Runner.run_streamed()	Call the agent with streaming
async for event...	Process streaming events
ResponseTextDeltaEvent	Print partial text
ResponseContentPartDoneEvent	End of a chunk
inputs = result.to_input_list()	Update conversation history
user_msg = input()	Get next user message
inputs.append(...)	Add user message to history
agent = result.current_agent	Switch to the routed agent
'''

import asyncio
import uuid
from open_ai_env import env_func
env_func()

from openai.types.responses import ResponseContentPartDoneEvent, ResponseTextDeltaEvent

from agents import Agent, RawResponsesStreamEvent, Runner, TResponseInputItem, trace, ItemHelpers, MessageOutputItem

french_agent=Agent(name="french_agent", instructions="you only speak french")
spanish_agent=Agent(name="french_agent", instructions="you only speak spanish")
english_agent=Agent(name="french_agent", instructions="you only speak english")

triage_agent=Agent(name="triage_agent",
instructions="Handoff to the appropriate agent based on the language of the request.",
handoffs=[french_agent,spanish_agent,english_agent])

async def main():
    # get a uuuid for conversation
    conv_id=str(uuid.uuid4().hex[:16])
    
    #construct inputs
    msg = input("Hi! We speak French, Spanish and English. How can I help? ")
    inputs: list[TResponseInputItem] = [{"content": msg, "role": "user"}]
    agent = triage_agent


    #start while loop
    while True:
        # creare trace
        #run the agent
        with trace("trace_name",group_id=conv_id):
            result=await Runner.run(agent,msg)   
    #under a for loop
            for item in result.new_items:
                if isinstance(item, MessageOutputItem):
                    text=ItemHelpers.text_message_output(item)
                    if text:
                        print(f"  - Translation step: {text}")     


if __name__=="__main__":
    asyncio.run(main())
    
    
    

