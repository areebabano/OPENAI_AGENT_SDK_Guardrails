# ------------------------------ INPUT GUARDRAILS ---------------------------------------

from guardrails.guardrail_agent import guardrail_agent

from agents import Agent, GuardrailFunctionOutput, input_guardrail, RunContextWrapper, Runner, TResponseInputItem


@input_guardrail
async def hotel_royal_input_guardrail(ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem])-> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, input=input, context= ctx.context)
    return GuardrailFunctionOutput(
        output_info= result.final_output,
        tripwire_triggered= not result.final_output.is_hotel_royal_query
    )

