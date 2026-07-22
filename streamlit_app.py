import streamlit as st

from diet_app import recommendation

from ui.sidebar import create_sidebar
from ui.search import search_conditions
from ui.filters import (
    create_filters,
    apply_filters,
    sort_foods
)
from ui.cards import display_recommendations
from ui.common_foods import display_common_foods
from ui.statistics import display_statistics


# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Diet Recommendation System",
    page_icon="🥗",
    layout="wide"
)

st.title("🥗 Diet Recommendation System")

st.write(
    "Get personalized food recommendations based on your health conditions."
)

st.divider()


# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------

foods = recommendation.load_foods()
conditions = recommendation.load_conditions()


# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

recommend = create_sidebar()

meal_filter, food_type, sort_by = create_filters(foods)


# -------------------------------------------------
# SEARCH
# -------------------------------------------------

selected_conditions = search_conditions(conditions)


# -------------------------------------------------
# RECOMMEND
# -------------------------------------------------

if recommend:

    if not selected_conditions:

        st.warning("Please select at least one health condition.")

    else:

        recommendations = recommendation.recommend_foods(
            foods,
            conditions,
            selected_conditions
        )

        # -----------------------------------------
        # Apply Filters & Sorting
        # -----------------------------------------

        for rec in recommendations:

            filtered_foods = apply_filters(
                rec["foods"],
                meal_filter,
                food_type
            )

            filtered_foods = sort_foods(
                filtered_foods,
                sort_by
            )

            rec["foods"] = filtered_foods

        # -----------------------------------------
        # Statistics
        # -----------------------------------------

        display_statistics(recommendations)


        # -----------------------------------------
        # Common Foods
        # -----------------------------------------

        common_foods = recommendation.find_common_foods(
            recommendations
        )

        display_common_foods(common_foods)

        # -----------------------------------------
        # Recommendation Cards
        # -----------------------------------------

        display_recommendations(recommendations)