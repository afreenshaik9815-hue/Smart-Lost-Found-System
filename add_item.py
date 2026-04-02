import streamlit as st
import pandas as pd

def add_item():
    st.header("➕ Add Lost / Found Item")

    item_type = st.selectbox("Type", ["Lost", "Found"])
    name = st.text_input("Item Name")
    description = st.text_input("Description")
    location = st.text_input("Location")

    if st.button("Submit"):
        if name and description and location:
            new_row = pd.DataFrame(
                [[item_type, name, description, location]],
                columns=["Type", "Item Name", "Description", "Location"]
            )
            st.session_state.data = pd.concat(
                [st.session_state.data, new_row], ignore_index=True
            )
            st.success("Item added successfully!")
        else:
            st.warning("Please fill all fields")