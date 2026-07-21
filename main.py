from diet_app import recommendation

def main():

    foods = recommendation.load_foods()
    conditions = recommendation.load_conditions()

    recommendation.display_conditions(conditions)

    selected_conditions = recommendation.get_user_choice(conditions)

    recommendations = recommendation.recommend_foods(
        foods,
        conditions,
        selected_conditions
    )

    recommendation.display_recommendations(recommendations)

    common_foods = recommendation.find_common_foods(recommendations)

    print("Common Foods:\n")

    for food in common_foods:
        print("-", food)


main()