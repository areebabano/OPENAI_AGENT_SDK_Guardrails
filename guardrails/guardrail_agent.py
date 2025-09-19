from pydantic import BaseModel

from agents import Agent

from config import model

class RoyalComfortHotelOutput(BaseModel):
    is_hotel_royal_query: bool
    is_hotel_royal_account_tax_query: bool
    reasoning: str

guardrail_agent: Agent = Agent(
    name="RoyalComfortHotelGuardrail",
    instructions = """
Check if the user query is related to Royal Comfort Hotel.  

If the query is about hotel services, rooms, booking, pricing, facilities, 
location, policies, events, or anything directly related to Royal Comfort Hotel, 
output 'RELATED'.  

If the query is about accounts, taxes, coding, politics, weather, other hotels, 
or any unrelated topics, output 'NOT RELATED'.  

Do not answer the query, only classify as 'RELATED' or 'NOT RELATED'.
""",
    model=model,
    output_type=RoyalComfortHotelOutput
)