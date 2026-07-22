import streamlit as st


def display_statistics(recommendations):
    """
    Displays summary statistics for the recommended foods.

    Parameters
    ----------
    recommendations : list
        Output from recommend_foods() after filters are applied.
    """

    foods = []

    # Collect all displayed foods
    for recommendation in recommendations:
        foods.extend(recommendation["foods"])

    # Remove duplicates
    unique_foods = {}

    for food in foods:
        unique_foods[food["id"]] = food

    foods = list(unique_foods.values())

    if not foods:
        return

    total_foods = len(foods)

    vegetarian = sum(
        food["vegetarian"]
        for food in foods
    )

    vegan = sum(
        food["vegan"]
        for food in foods
    )

    non_vegetarian = total_foods - vegetarian

    avg_calories = round(
        sum(food["calories"] for food in foods) / total_foods,
        1
    )

    avg_protein = round(
        sum(food["protein"] for food in foods) / total_foods,
        1
    )

    st.header("📊 Recommendation Summary")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Foods",
        total_foods
    )

    col2.metric(
        "Vegetarian",
        vegetarian
    )

    col3.metric(
        "Vegan",
        vegan
    )

    col4.metric(
        "Non-Veg",
        non_vegetarian
    )

    col5.metric(
        "Avg Calories",
        avg_calories
    )

    st.metric(
        "Average Protein",
        f"{avg_protein} g"
    )

    st.divider()