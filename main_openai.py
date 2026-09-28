# Importér de nødvendige komponenter
# Agent --> Bruges til at definere agenten: navn, model og værktøjer.
# AgentRuntime --> Bruges til at afvikle agentens opgave.
# tool --> Bruges til at definere et værktøj, som agenten kan bruge.
from agentspan.agents import Agent, AgentRuntime, tool

"""
Gør funktionen til et værktøj
Dette kaldes en decorator. En decorator tilføjer funktionalitet til den funktion, 
der står lige nedenunder.
Her gør @tool funktionen egnet til brug som et Agentspan-værktøj.
"""


@tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    return f"72 degrees and sunny in {city}"


agent = Agent(
    name="weatherbot",  # der er agent navn , du kan godt vælge et andet navn, hvis du vil.
    model="openai/gpt-5.4-mini",  # der er agent model
    tools=[get_weather],  # der er agent værktøjer
)

with AgentRuntime() as runtime:
    result = runtime.run(agent, "What's the weather in CPH?")
    result.print_result()

"""
Den forventede proces er:
1. Modellen modtager spørgsmålet og oplysninger om værktøjet.
2. Modellen kan anmode om get_weather med et bynavn.
3. Agentspans afvikling udfører værktøjet.
4. Værktøjets tekst bliver tilgængelig for modellen.
5. Modellen kan formulere et svar.

"""
