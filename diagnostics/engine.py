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