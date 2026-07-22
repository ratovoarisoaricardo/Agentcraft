from agents.researcher import ResearcherAgent
from agents.analyst import AnalystAgent
from agents.writer import WriterAgent
from typing import List, Dict, Any

class SwarmOrchestrator:
    """Orchestrates sequential multi-agent task execution and logs inter-agent communication."""
    
    def __init__(self):
        self.researcher = ResearcherAgent()
        self.analyst = AnalystAgent()
        self.writer = WriterAgent()

    def run_swarm(self, goal: str):
        """Runs the multi-agent pipeline and yields step-by-step logs and final report."""
        logs: List[Dict[str, str]] = []
        
        res_output = self.researcher.execute_task(goal)
        logs.extend(self.researcher.memory)
        
        analysis_output = self.analyst.execute_task(res_output)
        logs.extend(self.analyst.memory)
        
        final_report = self.writer.execute_task(analysis_output)
        logs.extend(self.writer.memory)
        
        return {
            "logs": logs,
            "report": final_report
        }
