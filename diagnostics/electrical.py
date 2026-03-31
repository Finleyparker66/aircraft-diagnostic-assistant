def diagnose_electrical(symptom):
    results = []

    keywords = {
        "battery": ["battery", "dead battery", "low battery"],
        "power": ["no power", "loss of power", "electrical failure"]
    }

    if any(word in symptom for word in keywords["battery"]):
        results.append({
            "system": "Electrical System",
            "cause": "Battery failure",
            "likelihood": "High",
            "check": "Check battery voltage"
        })
        results.append({
            "system": "Electrical System",
            "cause": "Loose battery connection",
            "likelihood": "Medium",
            "check": "Inspect battery terminals"
        })

    if any(word in symptom for word in keywords["power"]):
        results.append({
            "system": "Electrical System",
            "cause": "Master switch off",
            "likelihood": "High",
            "check": "Check master switch"
        })
        results.append({
            "system": "Electrical System",
            "cause": "Blown fuse",
            "likelihood": "Medium",
            "check": "Inspect fuse panel"
        })

    return results