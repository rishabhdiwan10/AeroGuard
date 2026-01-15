from typing import TypedDict, List, Optional

class AgentState(TypedDict):
    location: str           # The target zone
    fire_detected: bool     # True/False
    fire_location: Optional[str]
    wind_speed: float       # In mph
    wind_direction: str     # "NW", "SE", etc.
    risk_level: str         # "Critical", "Moderate"
    evac_route: Optional[str] # The plan
    audit_passed: bool      # Safety check
    audit_feedback: str     # Reason for pass/fail
    logs: List[str]         # Debugging logs