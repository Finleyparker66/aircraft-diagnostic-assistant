from diagnostics.engine import follow_up_engine
from diagnostics.electrical import diagnose_electrical
from diagnostics.engine import diagnose_engine
from diagnostics.fuel import diagnose_fuel

print("Cessna 172 Diagnostic Assistant")
print("--------------------------------")

user_input = input("Enter aircraft symptom(s): ").lower()
symptoms = user_input.split(" and ")

from collections import defaultdict

results = []

for symptom in symptoms:
    engine_results = diagnose_engine(symptom)
    fuel_results = diagnose_fuel(symptom)
    electrical_results = diagnose_electrical(symptom)

    if engine_results:
        results.extend(engine_results)
    if fuel_results:
        results.extend(fuel_results)
    if electrical_results:
        results.extend(electrical_results)

# Combine and rank
combined = defaultdict(lambda: {"count": 0, "data": None})

for r in results:
    key = r["cause"]
    combined[key]["count"] += 1
    combined[key]["data"] = r

# Sort by frequency (more matches = higher priority)
sorted_results = sorted(combined.values(), key=lambda x: x["count"], reverse=True)

# Output
if sorted_results:
    print("\n=== DIAGNOSTIC REPORT ===")
    print(f"\nSymptoms: {user_input}")

    for item in sorted_results:
        r = item["data"]
        confidence = "HIGH" if item["count"] > 1 else r["likelihood"].upper()

        print("\n------------------------")
        print("System:", r["system"])
        print(f"[{confidence}] {r['cause']}")
        print("→ Check:", r["check"])
else:
    print("\nNo data available for this symptom yet.")

# Follow-up diagnostic (only trigger for engine-related issues)
if any("Engine" in r["data"]["system"] for r in sorted_results):
    for symptom in symptoms:
        follow_up = follow_up_engine(symptom)
        if follow_up:
            print("\n=== FOLLOW-UP DIAGNOSIS ===")
            print("System:", follow_up["system"])
            print(f"[{follow_up['likelihood']}] {follow_up['cause']}")
            print("→ Action:", follow_up["check"])
            break