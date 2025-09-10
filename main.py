# ----------------------------- GUARDRAILS --------------------------------------

from config import model

import asyncio

from agents import (
    Agent,
    Runner,
    InputGuardrailTripwireTriggered,
    OutputGuardrailTripwireTriggered
)

from guardrails.input_guardrails import hotel_royal_input_guardrail
from guardrails.output_guardrails import hotel_royal_output_guardrail, MessageOutput

agent: Agent = Agent(
    name="RoyalComfortHotelAgent",
    instructions="""
You are the official customer care agent for Royal Comfort Hotel. 
Assist guests politely with room bookings, pricing, and availability.  

Hotel Information:  
- Total Rooms: 120 luxury rooms & suites  
- Facilities: Free Wi-Fi, pool, spa, gym, restaurant, banquet hall, airport service  
- Check-in: 2:00 PM | Check-out: 12:00 Noon  
- Payment: Credit/Debit Cards, Online Transfers, Cash  
- Policy: Free cancellation up to 24 hours before check-in  

Always respond in a professional and welcoming tone, making guests 
feel comfortable and valued.
""",
    model=model,
    output_type=MessageOutput,
    input_guardrails=[hotel_royal_input_guardrail],
    output_guardrails=[hotel_royal_output_guardrail]
)


async def main():
    try:
        result = await Runner.run(
            agent,
            "How many rooms available in Royal Comfort Hotel?"
        )
        print("Guardrail didn't trip - this is unexpected\n")
        print(result.final_output)

    except InputGuardrailTripwireTriggered as e:
        print(f"Input Guardrail Tripped \n{e}.")

    except OutputGuardrailTripwireTriggered as e:
        print(f"Output Guardrail Tripped \n{e}.")

if __name__ == "__main__":
    asyncio.run(main())