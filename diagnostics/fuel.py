def diagnose_fuel(symptom):
    if "fuel leak" in symptom:
        return {
            "system": "Fuel System",
            "causes": [
                "Damaged fuel line",
                "Loose connection",
                "Worn seal"
            ],
            "checks": [
                "Inspect fuel lines",
                "Check connections",
                "Examine seals"
            ]
        }

    elif "low fuel pressure" in symptom:
        return {
            "system": "Fuel System",
            "causes": [
                "Fuel pump failure",
                "Blocked fuel filter",
                "Air in fuel line"
            ],
            "checks": [
                "Test fuel pump",
                "Inspect filter",
                "Check for air leaks"
            ]
        }

    return None