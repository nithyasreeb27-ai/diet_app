import streamlit as st


def search_conditions(conditions):
    """
    Displays a searchable condition selector.

    Parameters
    ----------
    conditions : list
        List loaded from conditions.json

    Returns
    -------
    list
        Selected condition names.
    """

    st.subheader("🔍 Search Health Condition")

    condition_names = sorted(
        condition["name"]
        for condition in conditions
    )

    selected_conditions = st.multiselect(
        "Search or Select Condition(s)",
        options=condition_names,
        placeholder="Type a condition...",
        help="You can select multiple conditions."
    )

    if not selected_conditions:
        st.info("Search and select at least one health condition.")

    return selected_conditions