import streamlit as st
from duckduckgo_search import DDGS
import requests

# Page settings
st.set_page_config(page_title="AI Image Finder", page_icon="🖼️", layout="wide")

# Theme toggle (just for UX — true theming is in settings.toml)
theme = st.radio("🌓 Choose Theme:", ["Light", "Dark"], horizontal=True)

# Title
st.title("🧠 AI Image Finder")

query = st.text_input("🔎 What image are you looking for?")

if query:
    st.info(f"Searching DuckDuckGo for '{query}'...")

    with DDGS() as ddgs:
        results = ddgs.images(query, max_results=5)
        image_results = list(results)

    if image_results:
        for i, result in enumerate(image_results):
            image_url = result["image"]
            st.image(image_url, caption=f"Result {i+1}", use_column_width=True)

            # Download button
            try:
                img_data = requests.get(image_url).content
                st.download_button(
                    label="⬇️ Download Image",
                    data=img_data,
                    file_name=f"{query.replace(' ', '_')}_{i+1}.jpg",
                    mime="image/jpeg"
                )
            except:
                st.warning("⚠️ Couldn’t load image for download.")
    else:
        st.error("😢 No images found. Try a different prompt.")
