import streamlit as st
import requests

st.set_page_config(page_title="AI Database Assistant", layout="wide")

st.title("🤖 AI Database Assistant")
st.write("Ask questions about your employee database using natural language.")

question = st.text_input("Ask a question")

if st.button("Ask AI"):
    if question:
        response = requests.get(
            "http://127.0.0.1:8000/query",
            params={"q": question}
        )

        if response.status_code == 200:
            data = response.json()

            st.success("Answer")

            st.write(data["response"])
        else:
            st.error("Backend Error")