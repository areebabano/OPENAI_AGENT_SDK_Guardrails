# ----------------------- OUTPUT GUARDRAILS ------------------------------

from pydantic import BaseModel

from guardrails.guardrail_agent import guardrail_agent

from agents import GuardrailFunctionOutput, RunContextWrapper, Agent, Runner, output_guardrail

class MessageOutput(BaseModel):
    response: str

@output_guardrail
async def hotel_royal_output_guardrail(ctx: RunContextWrapper[None], agent: Agent, output: MessageOutput)-> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, output.response, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_hotel_royal_account_tax_query
    )