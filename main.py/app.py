from recommendation import *

def main():
    foods = load_foods()
    conditions = load_conditions()

    display_conditions(conditions)

    valid, selected_conditions = get_user_choice(conditions)

    if not valid:
        return

    recommendations = recommend_foods(
        foods,
        conditions,
        selected_conditions
    )

    display_recommendations(recommendations)

    common = find_common_foods(recommendations)

    print("\nCommon Foods")
    for food in common:
        print(food)

if __name__ == "__main__":
    main()