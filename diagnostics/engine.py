def diagnose_engine(symptom):
    results = []

    if "stall" in symptom:
        results.append({
            "system": "Engine / Fuel System",
            "cause": "Fuel starvation",
            "likelihood": "High",
            "check": "Check fuel supply"
        })
        results.append({
            "system": "Engine / Fuel System",
            "cause": "Carburettor icing",
            "likelihood": "Medium",
            "check": "Apply carb heat"
        })
        results.append({
            "system": "Engine / Fuel System",
            "cause": "Air intake blockage",
            "likelihood": "Low",
            "check": "Inspect air intake"
        })

    if "rough" in symptom:
        results.append({
            "system": "Engine",
            "cause": "Spark plug fouling",
            "likelihood": "High",
            "check": "Inspect spark plugs"
        })
        results.append({
            "system": "Engine",
            "cause": "Incorrect mixture",
            "likelihood": "Medium",
            "check": "Adjust mixture"
        })
        results.append({
            "system": "Engine",
            "cause": "Carburettor icing",
            "likelihood": "Medium",
            "check": "Apply carb heat"
        })

    return results


def follow_up_engine(symptom):
    if "rough" in symptom or "stall" in symptom:

        carb_heat = input("\nIs carb heat applied? (yes/no): ").lower()

        if carb_heat == "no":
            return {
                "system": "Engine",
                "cause": "Carburettor icing highly likely",
                "likelihood": "HIGH",
                "check": "Apply carb heat immediately"
            }

        elif carb_heat == "yes":
            rpm_change = input("Does engine RPM improve with carb heat? (yes/no): ").lower()

            if rpm_change == "yes":
                return {
                    "system": "Engine",
                    "cause": "Carburettor icing confirmed",
                    "likelihood": "HIGH",
                    "check": "Continue carb heat and monitor"
                }
            else:
                return {
                    "system": "Engine",
                    "cause": "Fuel or ignition issue likely",
                    "likelihood": "MEDIUM",
                    "check": "Inspect fuel system and spark plugs"
                }

    return None