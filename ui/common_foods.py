import streamlit as st


def display_common_foods(common_foods):
    """
    Display common foods in attractive cards.
    """

    st.header("🥗 Common Foods")

    if not common_foods:
        st.info("No common foods found.")
        return

    st.caption(
        "Foods suitable for all selected health conditions."
    )

    cols = st.columns(3)

    for index, food in enumerate(common_foods):

        with cols[index % 3]:

            st.success(f"🥗 {food}")