def analyze_soil(soil_type, pH, moisture):
    if soil_type == 'loamy' and 6 <= pH <= 7:
        return "Ideal for most crops."
    elif soil_type == 'clayey' and moisture > 40:
        return "Suitable for rice, but improve drainage."
    else:
        return "Add organic matter to improve soil quality."
def recommend_crops(climate, season):
    if climate == 'tropical' and season == 'rainy':
        return "Recommended Crops: Rice, Maize."
    elif climate == 'temperate' and season == 'winter':
        return "Recommended Crops: Wheat, Barley."
    else:
        return "Please consult local guidelines."
def diagnose_disease(symptoms):
    disease_dict = {
        '1': "Leaf Spot: Possible disease - Leaf Spot. Treatment: Use fungicide.",
        '2': "Wilting: Possible disease - Fusarium Wilt. Treatment: Improve soil drainage.",
        '3': "Yellowing Leaves: Possible disease - Nitrogen Deficiency. Treatment: Apply nitrogen-rich fertilizer.",
        '4': "Stunted Growth: Possible disease - Root Knot Nematodes. Treatment: Use nematicides.",
        '5': "Mildew on Leaves: Possible disease - Powdery Mildew. Treatment: Apply sulfur-based fungicide.",
        '6': "Curling Leaves: Possible disease - Aphid Infestation. Treatment: Use insecticidal soap or neem oil.",
        '7': "Black Rot on Fruits: Possible disease - Anthracnose. Treatment: Remove infected fruits and apply fungicide."
    }
    results = []
    for symptom in symptoms:
        result = disease_dict.get(symptom, "Symptom not recognized. Please consult an expert.")
        results.append(result)
    return results
def main():
    print("Welcome to AgriAssist: Your Crop and Soil Management System")
    soil_type = input("Enter soil type (sandy/clayey/loamy): ")
    pH = float(input("Enter soil pH level: "))
    moisture = float(input("Enter soil moisture content (%): "))
    print(analyze_soil(soil_type, pH, moisture))
    climate = input("Enter climate (tropical/temperate): ")
    season = input("Enter current season: ")
    print(recommend_crops(climate, season))
    print("Select the symptoms you observe (you can select multiple by separating numbers with commas):")
    print("1. Leaf Spots")
    print("2. Wilting")
    print("3. Yellowing Leaves")
    print("4. Stunted Growth")
    print("5. Mildew on Leaves")
    print("6. Curling Leaves")
    print("7. Black Rot on Fruits")
    symptom_input = input("Enter the symptom numbers (e.g., 1,3,5): ")
    symptom_list = symptom_input.split(',')
    symptom_list = [symptom.strip() for symptom in symptom_list]
    results = diagnose_disease(symptom_list)
    for result in results:
        print(result)
    print("Sustainability Tip: Practice crop rotation to maintain soil fertility.")
    print("\nThank you for using AgriAssist. We hope this system helps you in achieving better crop management and soil health. Happy farming!")
if __name__ == "__main__":
    main()
