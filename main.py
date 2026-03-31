from diagnostics.engine import diagnose_engine
from diagnostics.fuel import diagnose_fuel

print("Cessna 172 Diagnostic Assistant")
print("--------------------------------")

symptom = input("Enter aircraft symptom: ").lower()

results = []

# Collect results from systems
engine_results = diagnose_engine(symptom)
fuel_results = diagnose_fuel(symptom)

if engine_results:
    results.extend(engine_results)

if fuel_results:
    results.extend(fuel_results)

# Output
if results:
    print("\n=== DIAGNOSTIC REPORT ===")
    print(f"\nSymptom: {symptom}")

    for r in results:
        print("\n------------------------")
        print("System:", r["system"])
        print(f"[{r['likelihood'].upper()}] {r['cause']}")
        print("→ Check:", r["check"])
else:
    print("\nNo data available for this symptom yet.")