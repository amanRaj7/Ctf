import streamlit as st
from urllib.parse import urlparse, parse_qs
import os

# Title
st.title("File Reader via Query Parameter")

# Get the query parameters from the URL
query_params = st.experimental_get_query_params()

# Extract the filename from `q`
file_param = query_params.get("q", [None])[0]

if file_param:
    st.subheader(f"Reading file: `{file_param}`")

    # Ensure file exists
    if os.path.exists(file_param) and os.path.isfile(file_param):
        try:
            with open(file_param, "r", encoding="utf-8") as f:
                content = f.read()
            st.text_area("File Content", content, height=400)
        except Exception as e:
            st.error(f"Error reading file: {e}")
    else:
        st.error("File not found.")
else:
    st.info("Please add a file name in the query string, e.g. `/?q=example.txt`")
