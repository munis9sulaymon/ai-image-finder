# image_finder_app.py

import streamlit as st  # ✅ Import FIRST
from duckduckgo_search import DDGS  # Other imports next

# ✅ Set up the page config AFTER the import
st.set_page_config(page_title="AI Image Finder", page_icon="🖼️", layout="wide")

st.title("🖼️ AI Image Finder")

query = st.text_input("What image are you looking for?")

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
