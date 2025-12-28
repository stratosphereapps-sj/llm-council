from agents.analyst import AnalystAgent
from agents.critic import CriticAgent
from agents.summarizer import SummarizerAgent
from agents.generate_agent import GenerateAgent
from db.council import save_response

def run_council(initial_prompt: str):
    agents = [
        GenerateAgent(),
        AnalystAgent(),
        CriticAgent(),
        SummarizerAgent()
    ]

    current_input = initial_prompt
    results = []
    for agent in agents:
        # print(f"\n--- {agent.name} speaking ---\n with input:\n{current_input}\n")
        output = agent.run(current_input)

        # print(output)

        save_response(
            agent_name=agent.name,
            input_text=current_input,
            output_text=output
        )
        
        results.append({
            "agent": agent.name,
            "output": output
        })

        current_input = output
        print(f"\n--- {agent.name} finished speaking ---\n with output:\n{output}\n")
    return results

if __name__ == "__main__":
    user_prompt = input("Enter discussion topic:\n")
    # print("\nStarting council discussion...\n with topic:", user_prompt)
    run_council(user_prompt)
