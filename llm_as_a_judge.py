"""
This example shows the LLM as a judge pattern. The first agent generates an outline for a story.
The second agent judges the outline and provides feedback. We loop until the judge is satisfied
with the outline.
"""
from open_ai_env import setup_openai_env
setup_openai_env()

import asyncio
from agents import Agent, ItemHelpers, TResponseInputItem, Runner, trace
from pydantic import BaseModel


#create outline_generator
outline_instructions="""you generate short stories' outline. your output will be judged and
 if you get a feedback then improve the outline accordingly"""
outline_generator=Agent(name="outline_generator", instructions=outline_instructions)

class OutlineEvaluation(BaseModel):
    is_good_qual: False
    feedback: str

judge_instructions="""you judge the outline of short stories. you will be provided an outline and if you feel that the 
outline lacks quality then you need to give feedback using which a new outline will be created and passed back to you."""
judge=Agent(name="outline_judge", instructions=judge_instructions, output_type=OutlineEvaluation)

async def main():
    msg=input("enter the type of the story outline you want")
    input_items: list[TResponseInputItem]=[{"role":"user", "content":msg}]

    while True:
        with trace("story_outline"):
            outline=await Runner.run(outline_generator, input_items)
            latest_outline=ItemHelpers.text_message_outputs.(outline.new_items)
            
            result=await Runner.run(judge, outline.to_input_list())
            
            evaluation: OutlineEvaluation = result.final_output.is_good_qual
            if evaluation:
                print("this outline was passed by the judge")
                print(latest_outline)
                break
            
            
if __name__=="__main__":
    asyncio.run(main())