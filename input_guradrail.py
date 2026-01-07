from agents import Agent, TResponseInputItem, GuradRailFunctionOutput, InputGuradRailTrpiWireTriggered, Runner, RunContextWrapper, input_guradrail


#create tripwire dataclass
class MathGuard(BaseModel):
    reasoning: str
    is_math_home_work: bool
    
#create a guradrail agents
math_guard=Agent(name="math guardrail", instruction="you guard against user asking for help in their math homework", output_type=MathGuard)

#create guradrail func
@input_guradrail
def math_guard_rail(agent: Agent, context: RunContextWrapper, input: str | list[TResponseInputItem]):
    result=Runner.run(math_guard, input)
    result=result.final_output_as(MathGuard)
    
    return GuradRailFunctionOutput(
    output_info=result,
    tripwire_triggered=result.is_math_homework)

async def main():
    input=input("how can i help you today?")
    
    agent=Agent(name="chat_bot", instructions="resolve the user queries")
    
    while True:
        #run the agents
        try:
            result=Runner.run(agent,input_guardrails=[math_guard_rail], input=input)
        #print error if guardrailtripped
            input=result.to_input_list()
        except InputGuradRailTrpiWireTriggered:
            msg="I cant help with math"
            print(msg)
            input.append({"role":"assisstant", "content":msg})
            
            
if __name__ == "__main__":
    asyncio.run(main())
            
            
