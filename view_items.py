import streamlit as st

def view_items():
    st.header("📋 All Items")
    st.dataframe(st.session_state.data)