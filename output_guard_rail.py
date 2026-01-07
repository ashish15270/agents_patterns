import asyncio

from agents import Agent, OutputGuardrailTripwireTriggered, Runner, TResponseInputItem

from pydantic import BaseModel

# create data class with fields "response", reasoning, tripwiretriggered

class BotAnswer(BaseModel):
    reasoning: str = Field("caputres reasoning used by the agent")
    response: str = Field("final answer given by the bot")
    usr_name: str | None = Field("optional: user name if known")
    
@output_guardrail
def pii_data_guard(context: RunContextWrapper, output: MessageOutput, agent: Agent) -> GuardRailFunctionOutput:
     pii_detected = "650" in response or "650" in resoning
     
     return GuradRailFunctionOutput(
     output_info={"ppii was found":True},
     tripWireTriggered=pii_detected
     )
     
agent=Agent("chat_bot", instructions="you answer user queries", output_type=BotAnswer, output_guardrail=[pii_data_guard])

async def main():
    input=input("how can i help you today?")
    try:
        result=Runner.run(agent, input=input)
    excpet OutputGuardrailTripwireTriggered as e:
        print("cant answer pii related questions")
        
    