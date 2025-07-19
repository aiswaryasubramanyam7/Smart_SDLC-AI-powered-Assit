import streamlit as st
import requests

st.title("🧠 SmartSDLC - AI-Powered SDLC Assistant")

task = st.selectbox("Choose a task", [
    "Requirement Analysis", "Code Generation",
    "Test Case Creation", "Bug Fixing", "Documentation"
])

user_input = st.text_area("Enter your prompt or code snippet")

task_map = {
    "Requirement Analysis": "requirement",
    "Code Generation": "code",
    "Test Case Creation": "test",
    "Bug Fixing": "bugfix",
    "Documentation": "docs"
}

if st.button("Generate"):
    if not user_input.strip():
        st.warning("Please enter a prompt first.")
    else:
        payload = {
            "prompt": user_input,
            "task": task_map[task]
        }
        try:
            response = requests.post("http://localhost:8000/ask/", json=payload)
            if response.status_code == 200:
                st.subheader("🔍 Result")
                st.code(response.json()["response"])
            else:
                st.error("Error from backend. Check console.")
        except Exception as e:
            st.error(f"Failed to connect to backend: {e}")
