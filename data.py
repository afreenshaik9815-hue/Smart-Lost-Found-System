import streamlit as st
import pandas as pd

def init_data():
    if "data" not in st.session_state:
        st.session_state.data = pd.DataFrame(
            columns=["Type", "Item Name", "Description", "Location"]
        )