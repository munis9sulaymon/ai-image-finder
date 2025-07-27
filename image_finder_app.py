# image_finder_app.py
st.set_page_config(page_title="AI Image Finder", page_icon="🖼️", layout="wide")

import streamlit as st
from duckduckgo_search import DDGS

# Streamlit app title
st.title("🖼️ AI Image Finder")

# User input for search query
query = st.text_input("What image are you looking for?")

# If user typed something
if query:
    st.info("🔍 Searching DuckDuckGo for images...")

    with DDGS() as ddgs:
        results = ddgs.images(query, max_results=5)
        image_results = list(results)

    if image_results:
        for i, result in enumerate(image_results):
            st.image(result['image'], caption=f"Result {i+1}", use_column_width=True)
    else:
        st.error("😢 No images found. Try a different prompt.")
