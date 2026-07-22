import streamlit as st


def create_sidebar():
    """
    Creates the application sidebar.

    Returns
    -------
    recommend : bool
        True when the Recommend Foods button is clicked.
    """

    st.sidebar.title("🥗 Diet Recommendation System")

    st.sidebar.markdown(
        "Find foods based on your health condition."
    )

    st.sidebar.markdown("---")

    recommend = st.sidebar.button(
        "🍽️ Recommend Foods",
        use_container_width=True,
        type="primary"
    )

    st.sidebar.markdown("---")

    st.sidebar.info(
        "Select one or more health conditions "
        "and click Recommend Foods."
    )

    return recommend