from agents.base_agent import BaseAgent
from typing import Dict, Any

class WriterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Marcus Chen",
            role="Executive Technical Writer",
            icon="✍️",
            system_prompt="Synthesize research and analysis into a polished, professional Markdown report."
        )

    def execute_task(self, analysis_data: Dict[str, Any]) -> str:
        self.log_thought("Receiving validated insights from Elena Rostova...")
        self.log_thought("Structuring executive summary and formatting Markdown report...")
        
        goal = analysis_data["goal"]
        insights_str = "\n".join([f"- {item}" for item in analysis_data["insights"]])
        
        report = f"""# 📄 AgentCraft Executive Report: {goal}

## 🎯 Executive Summary
This report was autonomously researched, critically analyzed, and synthesized by the **AgentCraft Multi-Agent Swarm** (*Dr. Vance, Elena Rostova, Marcus Chen*).

---

## 🔍 Key Domain Insights
{insights_str}

---

## 🧠 Risk & Feasibility Assessment
- **Status**: {analysis_data['risk_assessment']}
- **Recommendation**: Highly suitable for production deployment.

---
*Report generated autonomously by AgentCraft AI Swarm Engine.*
"""
        self.log_thought("Final Markdown report compilation completed successfully! 🎉")
        return report
