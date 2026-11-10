import json


# -------------------------
# DATA LOADING
# -------------------------

def load_foods():

    with open("data/foods.json", "r") as file:
        foods = json.load(file)
    return foods


def load_conditions():

    with open("data/conditions.json", "r") as file:
        conditions = json.load(file)

    return conditions


# -------------------------
# DISPLAY
# -------------------------

def display_conditions(conditions):

    print("\nAvailable Health Conditions:\n")

    for index, condition in enumerate(conditions, start=1):

        print(f"{index}. {condition['name']}")

    print()


# -------------------------
# USER INPUT
# -------------------------

def get_user_choice(conditions):

    condition_names = [
        condition["name"]
        for condition in conditions
        ] #List comprehension

    while True:

        choices = input(
            "\nEnter condition numbers separated by commas: "
        ).split(",")

        selected_conditions = []

        valid = True

        for choice in choices:

            try:

                index = int(choice.strip())

                if 1 <= index <= len(condition_names):

                    condition = condition_names[index - 1]

                    if condition not in selected_conditions:
                        selected_conditions.append(condition)

                else:

                    print(
                        f"{index} is an invalid choice."
                    )

                    valid = False

            except ValueError:

                print(
                    f"'{choice.strip()}' is not a valid number."
                )

                valid = False

        if valid:
            return selected_conditions

        print("\nPlease try again.") # it works only if the entry is invalid

def evaluate_food(food, rules):
    """Check a food against rules and return the verdict with the reasons."""

    failed = []

    for rule in rules:

        field = rule["field"]
        operator = rule["operator"]
        value = rule["value"]

        # None means "we don't have this nutrient for this food"
        actual = food.get(field)

        if actual is None:
            passed = False

        elif operator == ">=":
            passed = actual >= value

        elif operator == "<=":
            passed = actual <= value

        elif operator == "==":
            passed = actual == value

        else:
            raise ValueError(f"Unknown operator: {operator}")

        if not passed:
            failed.append(
                {
                    "field": field,
                    "operator": operator,
                    "value": value,
                    "actual": actual,
                }
            )

    return {"allowed": len(failed) == 0, "failed": failed}

# -------------------------
# FOOD_MATCHES_RULE
# -------------------------

def food_matches_rules(food, rules):
    return evaluate_food(food, rules)["allowed"]

# -------------------------
# RECOMMENDATION
# -------------------------

def recommend_foods(foods, conditions, selected_conditions):

    conditions_by_name = {c["name"]: c for c in conditions}

    recommendations = []

    for condition_name in selected_conditions:

        condition_data = conditions_by_name.get(condition_name)

        if condition_data is None:
            raise ValueError(f"Unknown condition: {condition_name}")

        recommended_foods = []

        # Check every food
        for food in foods:

            if food_matches_rules(food, condition_data["rules"]):

                recommended_foods.append(food)

        recommendations.append(
            {
                "condition": condition_name,
                "rules": condition_data["rules"],
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

        print(f"\n{recommendation['condition']}")
        print("-" * len(recommendation["condition"]))

        if not recommendation["foods"]:
            print("No foods found for this condition.")
            continue

        for food in recommendation["foods"]:

            print(f"\n{food['name']}")

            print("Recommended because:")

            for rule in recommendation["rules"]:

                field = rule["field"]
                operator = rule["operator"]
                value = rule["value"]

                print(
                    f" • {field.replace('_',' ').title()} "
                    f"= {food[field]} "
                    f"({operator} {value})"
                )

        print()


# -------------------------
# COMMON FOODS
# -------------------------

def find_common_foods(recommendations):

    if not recommendations:
        return []

    common_foods = {
        food["name"]
        for food in recommendations[0]["foods"]
    }

    for recommendation in recommendations[1:]:

        current_foods = {
            food["name"]
            for food in recommendation["foods"]
        }

        common_foods &= current_foods

    return sorted(common_foods)