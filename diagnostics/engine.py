def diagnose_engine(symptom):
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

    return None