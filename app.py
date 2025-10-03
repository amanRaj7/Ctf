import streamlit as st
import os

st.title("File Reader via Query Parameter")

# Get query parameters
query_params = st.query_params if hasattr(st, 'query_params') else st.experimental_get_query_params()

# Extract the filename
file_param = query_params.get("q", [None])[0]

if file_param:
    st.subheader(f"Reading file: `{file_param}`")
    # Only read from current directory (or a safe subdirectory)
    safe_path = os.path.join(os.getcwd(), file_param)

    if os.path.exists(safe_path) and os.path.isfile(safe_path):
        try:
            with open(safe_path, "r", encoding="utf-8") as f:
                content = f.read()
            st.text_area("File Content", content, height=400)
        except Exception as e:
            st.error(f"Error reading file: {e}")
    else:
        st.error("File not found.")
else:
    st.info("Please add a file name in the query string, e.g. `/?q=helloWorld.txt`")
