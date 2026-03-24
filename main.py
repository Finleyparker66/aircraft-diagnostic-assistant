print("Cessna 172 Diagnostic Assistant")
print("--------------------------------")

def diagnose(symptom):
    if "stall" in symptom:
        return {
            "system": "Engine / Fuel System",
            "causes": [
                "Fuel starvation",
                "Carburettor icing",
                "Air intake blockage"
            ],
            "checks": [
                "Check fuel supply",
                "Apply carb heat",
                "Inspect air intake"
            ]
        }

    elif "rough" in symptom:
        return {
            "system": "Engine",
            "causes": [
                "Spark plug fouling",
                "Incorrect mixture",
                "Carburettor icing"
            ],
            "checks": [
                "Inspect spark plugs",
                "Adjust mixture control",
                "Apply carb heat"
            ]
        }

    else:
        return None


# Main program
symptom = input("Enter aircraft symptom: ").lower()

result = diagnose(symptom)

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