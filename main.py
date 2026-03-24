from diagnostics.engine import diagnose_engine
from diagnostics.fuel import diagnose_fuel

print("Cessna 172 Diagnostic Assistant")
print("--------------------------------")

symptom = input("Enter aircraft symptom: ").lower()

results = []

# Collect results from systems
results.extend(diagnose_engine(symptom))
results.extend(diagnose_fuel(symptom) or [])

# Output
if results:
    print("\nPossible Issues:")

    for i, r in enumerate(results, 1):
        print(f"\n{i}. {r['cause']} ({r['likelihood']} likelihood)")
        print("   System:", r["system"])
        print("   Check:", r["check"])
else:
    print("\nNo data available for this symptom yet.")