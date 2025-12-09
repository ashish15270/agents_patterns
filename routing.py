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

from openai.types.responses import ResponseContentPartDoneEvent, ResponseTextDeltaEvent

from agents import Agent, RawResponsesStreamEvent, Runner, TResponseInputItem, trace

french_agent=Agent(name="french_agent", instructions="you only speak french")
spanish_agent=Agent(name="french_agent", instructions="you only speak spanish")
english_agent=Agent(name="french_agent", instructions="you only speak english")

triage_agent=Agent(name="triage_agent",
instructions="Handoff to the appropriate agent based on the language of the request."
handoffs=[french_Agent,spanish_agent,english_agent])

async def main():
    # get a uuuid for conversation
    conv_id=str(uuid.uuid4().hex[:16])
    
    #construct inputs
    inputs: list[TresponseInputItem]=[{"role":"user","content":msg}]
    msg = input("Hi! We speak French, Spanish and English. How can I help? ")
    agent = triage_agent
    
    #start while loop
    while True:
        # creare trace
        #run the agent
        with trace("trace_name",group_id=conv_id):
            result=Runner.run(agent,input=inputs)   
    #under a for loop
            async for event in result.stream_events():
                if not isinstance(event, RawResponseSrteamEvent):
                    continue
                data=event.data

                if isinstance(data, ResponseTextDeltaEvent):
                    print(data.delta,end="",flush=True)
                elif isinstance(data, ResponseContentPartDoneEvent):
                    print()
            #update_inputs
            inputs=result.to_input_list()
            #get user message
            msg=input("\nYour turn: ")      
            inputs.append({"role":"user","content":msg})
            #switch agent
            agent=result.current_agent      


if __name__=="__main__":
    asyncio.run(main())
    
    
    

