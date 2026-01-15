# AeroGuard: Agentic Wildfire Response System 🌲🔥

**Status:** 🚧 Prototype (v0.1) | **Architecture:** Multi-Agent LangGraph

AeroGuard is an **Agentic AI system** designed to coordinate autonomous disaster response. Unlike standard LLM chatbots, AeroGuard uses a state-machine architecture to reason, plan, and validate logistical decisions in real-time.

It moves beyond simple detection to solve the "last mile" problem of response: **How do we coordinate safe evacuation routes without human bottlenecks?**

---

## 🏗 System Architecture
The system is orchestrated using **LangGraph**, creating a directed cyclic graph (DAG) where four specialized agents collaborate:

### 1. 🛰️ Sentry Agent (Ingestion Layer)
* **Role:** The "Eyes" of the system.
* **Function:** Ingests satellite thermal data (NASA FIRMS API) and edge computer vision feeds to detect fire anomalies.
* **Current State:** Simulates thermal signature detection at specific coordinates.

### 2. 🌩️ Analyst Agent (Enrichment Layer)
* **Role:** The "Brain" of context.
* **Function:** Enriches raw fire data with geospatial context (wind vectors, humidity, topography).
* **Logic:** Calculates a "Risk Spread Vector" to predict where the fire will be in 1 hour.

### 3. 🛡️ Commander Agent (Strategic Layer)
* **Role:** The Decision Maker.
* **Function:** Formulates evacuation routes and resource dispatch plans based on the Analyst's risk vector.
* **Goal:** Minimize civilian exposure to the predicted spread zone.

### 4. 👮 Auditor Agent (Governance Layer)
* **Role:** The Guardrail (Human-in-the-Loop).
* **Function:** A deterministic safety node that validates the Commander's plan against safety protocols (ISO-31000).
* **Key Feature:** If the Commander suggests a route through a smoke path, the Auditor **rejects the plan** and forces a retry. This prevents "Hallucinated Danger."

---

## 🛠️ Tech Stack
* **Orchestration:** LangGraph (State management & looping)
* **LLM Integration:** LangChain
* **Language:** Python 3.10+
* **Safety/Eval:** Ragas (Semantic evaluation concepts)
* **Data Sources:** NASA FIRMS (Planned), NOAA Weather Data

## 🚀 Getting Started
```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/AeroGuard.git](https://github.com/YOUR_USERNAME/AeroGuard.git)

# Install dependencies
pip install -r requirements.txt

# Run the simulation
python main.py
