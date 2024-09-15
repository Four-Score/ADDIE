import streamlit as st

# Set page configuration
st.set_page_config(page_title="ADDIE - Agents Crew for ADHD Assistance", layout="centered")

# Main title for the homepage
st.title("ADDIE - Agents Crew for ADHD Assistance")

# Description of the app
st.markdown("""
### Welcome to ADDIE!

ADDIE is a multipurpose app designed to help individuals with ADHD manage their tasks and improve productivity through the power of AI agents. Whether you’re struggling to stay organized or overwhelmed with information, ADDIE is here to make things easier and help you stay on top of your tasks.

---

### Key Features:

1. **Google Calendar Integration** 📅  
   ADDIE allows you to type out thoughts or upload files, and AI agents will automatically create Google Calendar events or fetch existing ones. This feature helps users stay organized by efficiently tracking all events and deadlines.

2. **Document and Email Categorization** 📂  
   Users can extract files from Google Drive and emails from Gmail. AI agents will summarize and categorize the content by priority (high, medium, low), helping you focus on the most important tasks.

3. **Meeting Summarization** 🎙️  
   Upload meeting recordings (e.g., from Google Meet), and ADDIE’s AI agents will generate summaries, extracting critical insights. This helps users quickly identify the key points of a meeting without getting lost in details.

4. **Task Guidance via Vector Database** 🗂️  
   Input work-related documents into a vector database, and when starting new tasks, ADDIE provides step-by-step guidance based on the existing information. This is particularly helpful for individuals with ADHD who may struggle with focusing on the next steps in a task.

---

We are excited to submit this project in an upcoming hackathon, and while it is not deployed yet, you can follow the project progress on GitHub.

[GitHub Repository for ADDIE](https://github.com/A-E-R-A/ADDIE-local/tree/master)
""")