from agents.generate_agent import GenerateAgent
from agents.analyst import AnalystAgent

print(AnalystAgent().run(GenerateAgent().run("Discuss the impact of AI on modern education.")))
