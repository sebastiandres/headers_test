import streamlit as st

st.title("Header Viewer :eyes:")

headers_dict = st.context.headers
headers_mkd = ""

sorted_bool = st.checkbox("Sort by name")

if sorted_bool:
    headers_dict = dict(sorted(headers_dict.items()))

for header, value in headers_dict.items():
    headers_mkd += f"* **{header}**: {value}  \n"

st.markdown(headers_mkd)

