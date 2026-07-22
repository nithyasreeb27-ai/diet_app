import streamlit as st


def display_recommendations(recommendations):
    """
    Displays recommended foods as compact cards.
    """

    st.header("🍽 Recommended Foods")

    if not recommendations:
        st.warning("No recommendations found.")
        return

    for recommendation in recommendations:

        st.subheader(f"📌 {recommendation['condition']}")

        foods = recommendation["foods"]

        if not foods:
            st.error("No foods found.")
            continue

        # ------------------------
        # 2 Cards Per Row
        # ------------------------

        cols = st.columns(2)

        for index, food in enumerate(foods):

            with cols[index % 2]:

                with st.container(border=True):

                    # ---------------------
                    # Food Name
                    # ---------------------

                    st.markdown(f"### 🍽 {food['name']}")

                    # ---------------------
                    # Veg / Non Veg
                    # ---------------------

                    if food["vegan"]:
                        st.success("🌱 Vegan")

                    elif food["vegetarian"]:
                        st.info("🥗 Vegetarian")

                    else:
                        st.warning("🍗 Non Vegetarian")

                    # ---------------------
                    # Meal
                    # ---------------------

                    st.write(
                        "**Meal:** " +
                        ", ".join(food["meal"])
                    )

                    # ---------------------
                    # Why Recommended
                    # ---------------------

                    st.write("**Why Recommended?**")

                    for rule in recommendation["rules"]:

                        st.write(
                            f"✅ {rule['field'].replace('_',' ').title()} "
                            f"{rule['operator']} "
                            f"{rule['value']}"
                        )

                    # ---------------------
                    # More Details
                    # ---------------------

                    with st.expander("📊 More Details"):

                        st.write(f"**Category:** {food['category']}")
                        st.write(f"**Calories:** {food['calories']}")
                        st.write(f"**Protein:** {food['protein']} g")
                        st.write(f"**Carbohydrates:** {food['carbs']} g")
                        st.write(f"**Fat:** {food['fat']} g")
                        st.write(f"**Fiber:** {food['fiber']} g")
                        st.write(f"**Iron:** {food['iron']} mg")
                        st.write(f"**Calcium:** {food['calcium']} mg")
                        st.write(
                            f"**Glycemic Index:** {food['glycemic_index']}"
                        )

        st.divider()