from src.state import AgentState

def sentry_node(state: AgentState) -> AgentState:
    """Agent 1: Detects fire from simulated satellite data."""
    print("\n[SENTRY] 🛰️  Scanning Satellite Feeds...")
    
    # Mock Data: Simulating a fire detection
    log = "Fire signature detected at 34.05N, 118.24W (North Ridge)"
    print(f"   └── {log}")
    
    return {
        "fire_detected": True, 
        "fire_location": "North Ridge Sector 4",
        "logs": [log]
    }

def analyst_node(state: AgentState) -> AgentState:
    """Agent 2: Enriches alert with weather data."""
    print("[ANALYST] 🌩️  Querying Weather Data...")
    
    wind_speed = 45.0 # mph
    wind_dir = "NW"
    risk = "Critical" if wind_speed > 30 else "Moderate"
        
    log = f"Wind: {wind_speed}mph {wind_dir} | Risk: {risk}"
    print(f"   └── {log}")
    
    return {"wind_speed": wind_speed, "wind_direction": wind_dir, "risk_level": risk}

def commander_node(state: AgentState) -> AgentState:
    """Agent 3: Generates the evacuation plan."""
    print("[COMMANDER] 🛡️  Generating Evacuation Strategy...")
    
    risk = state.get("risk_level")
    if risk == "Critical":
        # We intentionally create a risky plan to test the Auditor
        plan = "Evacuate via Highway 9 South."
    else:
        plan = "Monitor sector."
        
    print(f"   └── Proposed Plan: {plan}")
    return {"evac_route": plan}

def auditor_node(state: AgentState) -> AgentState:
    """Agent 4: The Safety Guardrail (Human-in-the-Loop Logic)."""
    print("[AUDITOR] 🔍  Validating Plan against Safety Protocols...")
    
    plan = state.get("evac_route")
    wind_dir = state.get("wind_direction")
    
    # Safety Logic: If wind is NW, smoke blows SE over Highway 9.
    if "Highway 9" in plan and wind_dir == "NW":
        passed = False
        feedback = "SAFETY VIOLATION: Highway 9 is in the smoke path."
        print(f"   └── ❌ PLAN REJECTED: {feedback}")
    else:
        passed = True
        feedback = "Plan complies with safety standards."
        print(f"   └── ✅ PLAN APPROVED: {feedback}")
        
    return {"audit_passed": passed, "audit_feedback": feedback}