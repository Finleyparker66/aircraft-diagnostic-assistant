from diagnostics.engine import diagnose_engine

print("Cessna 172 Diagnostic Assistant")
print("--------------------------------")

symptom = input("Enter aircraft symptom: ").lower()

result = diagnose_engine(symptom)

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