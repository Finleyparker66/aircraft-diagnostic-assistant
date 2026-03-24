from diagnostics.engine import diagnose_engine
from diagnostics.fuel import diagnose_fuel

print("Cessna 172 Diagnostic Assistant")
print("--------------------------------")

symptom = input("Enter aircraft symptom: ").lower()

# Try each system
result = diagnose_engine(symptom)

if not result:
    result = diagnose_fuel(symptom)

# Output
if result:
    print("\nSystem:", result["system"])

    print("\nLikely Causes:")
    for cause in result["causes"]:
        print("-", cause)

    print("\nRecommended Checks:")
    for check in result["checks"]:
        print("-", check)
else:
    print("\nNo data available for this symptom yet.")