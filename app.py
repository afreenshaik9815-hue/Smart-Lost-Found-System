import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
st.set_page_config(page_title="Campus Lost & Found System", layout="centered")
st.title("🎒 Campus Lost & Found System")
st.write("Smart system to match lost and found items using Machine Learning")
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
        columns=["Type", "Item Name", "Description", "Location"]
    )
menu = st.sidebar.selectbox("Menu", ["Add Item", "View Items", "Find Matches"])
if menu == "Add Item":
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
elif menu == "View Items":
    st.header("📋 All Items")
    st.dataframe(st.session_state.data)
elif menu == "Find Matches":
    st.header("🔍 Matching Lost & Found Items")
    lost_items = st.session_state.data[st.session_state.data["Type"] == "Lost"]
    found_items = st.session_state.data[st.session_state.data["Type"] == "Found"]
    if lost_items.empty or found_items.empty:
        st.warning("Please add both lost and found items first")
    else:
        vectorizer = TfidfVectorizer()
        lost_desc = lost_items["Description"].tolist()
        found_desc = found_items["Description"].tolist()
        vectors = vectorizer.fit_transform(lost_desc + found_desc)
        similarity = cosine_similarity(
            vectors[:len(lost_desc)], vectors[len(lost_desc):]
        )
        match_found = False
        for i, lost in enumerate(lost_desc):
            for j, found in enumerate(found_desc):
                if similarity[i][j] > 0.3:
                    st.success("✅ Match Found!")
                    st.write(f"Lost Item: {lost}")
                    st.write(f"Found Item: {found}")
                    st.write("---")
                    match_found = True
        if not match_found:
            st.info("No matching items found")