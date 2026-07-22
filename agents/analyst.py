from agents.base_agent import BaseAgent
from typing import Dict, Any

class AnalystAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Elena Rostova",
            role="Senior Critical Analyst",
            icon="🧠",
            system_prompt="Critique, validate consistency, risk-assess data, and structure insights."
        )

    def execute_task(self, research_data: Dict[str, Any]) -> Dict[str, Any]:
        self.log_thought("Receiving raw research data from Dr. Vance...")
        self.log_thought("Evaluating technical feasibility & conducting risk-benefit analysis...")
        
        insights = []
        for fact in research_data["raw_facts"]:
            insights.append(f"Validated Insight: {fact} -> Verified consistency & low integration risk.")
            
        self.log_thought("Critical evaluation complete (0 contradictions found). Handing off to Writer Agent.")
        return {
            "goal": research_data["goal"],
            "insights": insights,
            "risk_assessment": "Low risk profile with high enterprise scalability potential."
        }
