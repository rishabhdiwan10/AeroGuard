from langgraph.graph import StateGraph, END
from src.state import AgentState
from src.nodes import sentry_node, analyst_node, commander_node, auditor_node

# Initialize Graph
workflow = StateGraph(AgentState)

# Add Agents
workflow.add_node("sentry", sentry_node)
workflow.add_node("analyst", analyst_node)
workflow.add_node("commander", commander_node)
workflow.add_node("auditor", auditor_node)

# Connect Agents
workflow.set_entry_point("sentry")
workflow.add_edge("sentry", "analyst")
workflow.add_edge("analyst", "commander")
workflow.add_edge("commander", "auditor")
workflow.add_edge("auditor", END)

# Compile
app = workflow.compile()