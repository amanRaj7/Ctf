import streamlit as st
import os
import tempfile

st.title("File Reader via Query Parameter")

# Get query parameters
query_params = st.query_params if hasattr(st, 'query_params') else st.experimental_get_query_params()

# Extract the filename
file_param = query_params.get("q", [None])

uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w+", encoding="utf-8") as temp_file:
        temp_file.write(uploaded_file.getvalue().decode("utf-8"))
        temp_file_path = temp_file.name

    # Get just the name part for matching with query param
    uploaded_filename = uploaded_file.name

    st.success(f"Uploaded file: `{uploaded_filename}`")

    # Match query parameter with uploaded file name
    if file_param:
        file_param = file_param.strip('"')  # Remove accidental quotes

        if file_param == uploaded_filename:
            st.subheader(f"Reading file: {uploaded_filename}")
            try:
                with open(temp_file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                st.text_area("File Content", content, height=400)
            except Exception as e:
                st.error(f"Error reading file: {e}")
        else:
            st.warning("Uploaded file name does not match the query parameter.")
    else:
        st.info("Add `?q=your_filename.txt` to the URL to display its contents.")
else:
    st.info("Please upload a text file.")