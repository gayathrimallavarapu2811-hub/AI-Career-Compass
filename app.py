
import streamlit as st

st.set_page_config(
    page_title="AI Career Compass",
    page_icon="🧭",
    layout="wide"
)

st.title("🧭 AI Career Compass")
st.subheader("Your Personal AI Career Guidance System")

st.write(
    "Discover suitable career paths based on your skills "
    "and build your learning roadmap."
)

st.success("Welcome! Let's explore your career opportunities.")

student_name = st.text_input("Enter your name")

skills = st.multiselect(
    "Select the skills you know",
    [
        "Python",
        "SQL",
        "Excel",
        "Statistics",
        "Machine Learning",
        "Data Visualization",
        "Power BI",
        "Communication"
    ]
)

if st.button("Analyze My Career"):
    if student_name.strip() and skills:
        st.subheader(f"Career Profile: {student_name}")
        st.write("Your selected skills:", ", ".join(skills))

        if "Python" in skills and (
            "Statistics" in skills or "Machine Learning" in skills
        ):
            st.success("Suggested Career: Data Scientist")
        elif "Python" in skills or "SQL" in skills:
            st.success("Suggested Career: Junior Data Analyst")
        elif "Power BI" in skills or "Excel" in skills:
            st.success("Suggested Career: BI Analyst")
        else:
            st.info(
                "Suggested starting point: Explore entry-level "
                "technology roles and develop your technical skills."
            )

        st.info(
            "Next step: Compare your skills with job requirements "
            "and create a personalized learning plan."
        )
    else:
        st.warning("Please enter your name and select at least one skill.")
