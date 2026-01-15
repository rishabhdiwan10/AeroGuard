from src.graph import app

def run_simulation():
    print("--- 🚒 INITIALIZING AEROGUARD SYSTEM 🚒 ---")
    inputs = {"location": "Sector 4", "logs": []}
    result = app.invoke(inputs)
    
    print("\n--- 🏁 FINAL REPORT 🏁 ---")
    print(f"📍 Status: {'🔥 FIRE DETECTED' if result.get('fire_detected') else '✅ CLEAR'}")
    print(f"📋 Plan: {result.get('evac_route')}")
    print(f"👮 Audit: {'✅ PASSED' if result.get('audit_passed') else '❌ FAILED'}")
    print(f"📝 Reason: {result.get('audit_feedback')}")

if __name__ == "__main__":
    run_simulation()