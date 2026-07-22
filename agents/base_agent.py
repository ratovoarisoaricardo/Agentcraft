from typing import List, Dict, Any

class BaseAgent:
    """Base class for autonomous AI agents within the AgentCraft Swarm."""
    
    def __init__(self, name: str, role: str, icon: str, system_prompt: str):
        self.name = name
        self.role = role
        self.icon = icon
        self.system_prompt = system_prompt
        self.memory: List[Dict[str, str]] = []

    def log_thought(self, message: str) -> Dict[str, str]:
        """Logs internal thought or delegation message."""
        log_entry = {"agent": self.name, "role": self.role, "icon": self.icon, "message": message}
        self.memory.append(log_entry)
        return log_entry
