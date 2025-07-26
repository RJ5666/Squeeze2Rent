import streamlit as st

st.title("Squeeze2Rent 🏠")
st.subheader("Can you afford to live in this state?")

state = st.selectbox(
    "Choose a state",
    [
        "Texas", "California", "New York", "Florida", "Illinois",
        "Pennsylvania", "Ohio", "Georgia", "North Carolina", "Michigan",
        "New Jersey", "Virginia", "Washington", "Arizona",
        "Massachusetts", "Tennessee", "Indiana"
    ]
)
