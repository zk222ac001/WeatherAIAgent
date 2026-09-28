# første download ollama model   https://ollama.com/download/windows
# ollama pull llama3.2:3b
# tilføje Powershell command : $env:OLLAMA_BASE_URL = "http://localhost:11434" 
from agentspan.agents import Agent, AgentRuntime, tool


# Decoratoren gør funktionen til et værktøj for agenten.
@tool
def get_weather(city: str) -> str:
    """Return simulated weather for a city for a classroom demo."""
    # Denne besked viser de studerende, at værktøjet bliver kaldt.
    print(f"\n[VÆRKTØJ KALDT] get_weather(city={city!r})")
    # Faste demodata – ikke en rigtig vejrudsigt.
    return f"Demodata: Det er 22 °C og solskin i {city}."


agent = Agent(
    name="weatherbot",
    # Modellen kører lokalt gennem Ollama.
    model="ollama/llama3.2:3b",
    # Agenten får adgang til vores Python-funktion.
    tools=[get_weather],
)

with AgentRuntime() as runtime:
    result = runtime.run(
        agent,
        "Brug get_weather til at hente vejret i København. "
        "Svar på dansk, og nævn, at det er demodata.",
    )

result.print_result()
