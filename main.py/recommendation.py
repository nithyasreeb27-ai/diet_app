import json


# -------------------------
# DATA LOADING
# -------------------------

def load_foods():
    with open("data/foods.json", "r") as file:
        return json.load(file)


def load_conditions():
    with open("data/conditions.json", "r") as file:
        return json.load(file)


# -------------------------
# DISPLAY
# -------------------------

def display_conditions(conditions):
    print("\nAVAILABLE CONDITIONS\n")

    condition_names = list(conditions.keys())

    for index, condition in enumerate(condition_names, start=1):
        print(f"{index}. {condition}")

    print()


# -------------------------
# USER INPUT
# -------------------------

def get_user_choice(conditions):
    condition_names = list(conditions.keys())

    choices = input(
        "Enter condition numbers separated by commas: "
    ).split(",")

    selected_conditions = []
    valid = True

    for choice in choices:
        try:
            index = int(choice.strip())

            if 1 <= index <= len(condition_names):
                selected_conditions.append(
                    condition_names[index - 1]
                )
            else:
                print(f"{index} is an invalid choice.")
                valid = False

        except ValueError:
            print(f"'{choice}' is not a number.")
            valid = False

    return valid, selected_conditions


# -------------------------
# RECOMMENDATION
# -------------------------

def recommend_foods(foods, conditions, selected_conditions):

    recommendations = []

    for condition in selected_conditions:

        print(f"\n{condition} : Valid Entry")

        rule = conditions[condition]

        recommended_foods = []

        for rule_name, rule_value in rule.items():

            for food_name, food_data in foods.items():

                if rule_name == "max_glycemic_index":

                    if food_data["glycemic_index"] <= rule_value:
                        recommended_foods.append(food_name)

                elif rule_name == "min_protein":

                    if food_data["protein"] >= rule_value:
                        recommended_foods.append(food_name)

                elif rule_name == "min_calories":

                    if food_data["calories"] >= rule_value:
                        recommended_foods.append(food_name)

        recommendations.append(
            {
                "condition": condition,
                "foods": recommended_foods
            }
        )

    return recommendations


# -------------------------
# DISPLAY RESULTS
# -------------------------

def display_recommendations(recommendations):

    print("\nRECOMMENDED FOODS\n")

    for recommendation in recommendations:

        print(recommendation["condition"])

        for food in recommendation["foods"]:
            print(" -", food)

        print()


# -------------------------
# COMMON FOODS
# -------------------------

def find_common_foods(recommendations):

    if not recommendations:
        return []

    common_foods = set(recommendations[0]["foods"])

    for recommendation in recommendations[1:]:

        common_foods &= set(recommendation["foods"])

    return list(common_foods)