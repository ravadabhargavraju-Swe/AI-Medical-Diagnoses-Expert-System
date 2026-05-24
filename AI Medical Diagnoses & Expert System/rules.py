def diagnose(symptoms):
    # Create a copy of symptoms to track derived facts 
    facts = symptoms.copy() 
    # Rule 1: Intermediate fact derivation (Flu)
    if "fever" in facts and "cough" in facts:
        facts.append("flu")

    # Rule 2: Viral Infection
    if "flu" in facts and "headache" in facts:
        return "Viral Infection", [
            "Drink plenty of water",
            "Take rest",
            "Consult doctor if symptoms continue"
        ]

    # Rule 3: Heart Disease
    elif "chest_pain" in facts and "breathlessness" in facts:
        return "Heart Disease", [
            "Avoid heavy work",
            "Seek immediate medical attention"
        ]

    # Rule 4: Dengue
    elif "fever" in facts and "body_pain" in facts:
        return "Dengue", [
            "Drink fluids",
            "Monitor platelet count",
            "Visit hospital immediately"
        ]

    # Rule 5: Throat Infection
    elif "fever" in facts and "sore_throat" in facts:
        return "Throat Infection", [
            "Warm salt water gargle",
            "Rest your voice",
            "Stay hydrated"
        ]

    # Default fallback if no conditions match standard rules
    return "Unknown Condition", ["Please consult a medical professional for an accurate diagnosis."]