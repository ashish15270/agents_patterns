import os
from dotenv import load_dotenv, find_dotenv

import asyncio

from pydantic import BaseModel

from agents import Agent, Runner, trace

load_dotenv(dotenv_path=find_dotenv(), override=True)

"""
This example demonstrates a deterministic flow, where each step is performed by an agent.
1. The first agent generates a story outline
2. We feed the outline into the second agent
3. The second agent checks if the outline is good quality and if it is a scifi story
4. If the outline is not good quality or not a scifi story, we stop here
5. If the outline is good quality and a scifi story, we feed the outline into the third agent
6. The third agent writes the story
"""

story_line_agent=Agent(name="storyline_agent", instructions="Generate a very short story outline based on the user's input.")

# create class to check output from the above agent

class OutlineCheckerType(BaseModel):
    good_qual: bool
    is_scifi: bool
    
# create a checker agent to check the output from storyline agent



outline_checker_agent=Agent(name="checker", 
instrctions="Read the given story outline, and judge the quality. Also, determine if it is a scifi story.",
output_type=OutlineCheckerType)

story_agent=Agent(name="story_Agent", instructions="Write a short story based on the given outline.",
    output_type=str,
)

async def main():
    input_prompt = input("What kind of story do you want? ")

    # Ensure the entire workflow is a single trace
    with trace("Deterministic story flow"):
        story_outline=Runner.run(story_line_agent, input_prompt)
        
        outline_checker_result=Runner.run(outline_checker_agent,story_outline.final_output)
        
        # check datatype of the output from above agent
        
        assert isinstance(outline_checker_result.final_output,OutlineCheckerType)
        
        outline=outline_checker_result.final_output
        
        if not outline.good_qual:
            print("outline quality was bad")
            exit(0)
            
        if not outline.is_scifi:
            print("story is not scifi")
            exit(0)
            
        print("Outline has good quality")
        
        story=Agent(story_agent,story_outline.final_output)
        
        print("story: /n {story.final_output}")
        
        
if __name__=="__main__":
    asyncio.run(main())