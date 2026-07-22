import streamlit as st


# ----------------------------------------
# FILTER WIDGETS
# ----------------------------------------

def create_filters(foods):
    """
    Creates filter widgets.

    Returns
    -------
    meal_filter
    food_type
    sort_by
    """

    st.sidebar.subheader("Filters")

    # -------------------------
    # Meal Filter
    # -------------------------

    meals = sorted(
        {
            meal
            for food in foods
            for meal in food["meal"]
        }
    )

    meal_filter = st.sidebar.selectbox(
        "Meal",
        ["All"] + meals
    )

    # -------------------------
    # Food Type
    # -------------------------

    food_type = st.sidebar.radio(
        "Food Preference",
        (
            "All",
            "Vegetarian",
            "Non Vegetarian",
            "Vegan"
        )
    )

    # -------------------------
    # Sorting
    # -------------------------

    sort_by = st.sidebar.radio(
        "Sort By",
        (
            "Default",
            "Highest Protein",
            "Lowest Calories",
            "Highest Fiber",
            "Lowest Fat",
            "Alphabetical"
        )
    )

    return meal_filter, food_type, sort_by


# ----------------------------------------
# APPLY FILTERS
# ----------------------------------------

def apply_filters(
    foods,
    meal_filter,
    food_type
):
    """
    Filters recommended foods.
    """

    filtered = foods

    # -------------------------
    # Meal Filter
    # -------------------------

    if meal_filter != "All":

        filtered = [
            food
            for food in filtered
            if meal_filter in food["meal"]
        ]

    # -------------------------
    # Food Type
    # -------------------------

    if food_type == "Vegetarian":

        filtered = [
            food
            for food in filtered
            if food["vegetarian"]
        ]

    elif food_type == "Non Vegetarian":

        filtered = [
            food
            for food in filtered
            if not food["vegetarian"]
        ]

    elif food_type == "Vegan":

        filtered = [
            food
            for food in filtered
            if food["vegan"]
        ]

    return filtered


# ----------------------------------------
# SORT FOODS
# ----------------------------------------

def sort_foods(
    foods,
    sort_by
):
    """
    Sorts filtered foods.
    """

    if sort_by == "Highest Protein":

        return sorted(
            foods,
            key=lambda x: x["protein"],
            reverse=True
        )

    elif sort_by == "Lowest Calories":

        return sorted(
            foods,
            key=lambda x: x["calories"]
        )

    elif sort_by == "Highest Fiber":

        return sorted(
            foods,
            key=lambda x: x["fiber"],
            reverse=True
        )

    elif sort_by == "Lowest Fat":

        return sorted(
            foods,
            key=lambda x: x["fat"]
        )

    elif sort_by == "Alphabetical":

        return sorted(
            foods,
            key=lambda x: x["name"]
        )

    return foods