import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_items():
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