import streamlit as st
from chains import *
import os

st.set_page_config(page_title="Smart School", page_icon="📖", layout="wide")
tabs = st.tabs(["Generate Material", "View Resources"])
st.session_state["lesson"] = ""


with tabs[0]:
    col1, col2 = st.columns([3, 1])
    col1.title("Generate Material")
    col2.title("Classroom Informtion")
    subject = col2.text_input("Subject")
    addtional_info = col2.text_area("Additional Classroom Info")
    standards_list = col1.text_area("Standards to genrate")
    col1.write("Please seperate standards with a newline")

    def generate_lesson_plans():
        standard_list = [x for x in standards_list.split("\n") if x]
        for x in standard_list:
            with open(f"./resources/{subject} - {x}.md", "w") as f:
                f.write(
                    LessonChain.invoke(
                        {
                            "subject": subject,
                            "standard": x,
                            "additional_info": addtional_info,
                        }
                    )
                )

    col1.button("Generate Lesson Plans", on_click=generate_lesson_plans)

with tabs[1]:
    st.title("View Resources")
    col3, col4 = st.columns([3, 1])
    col3.write(st.session_state["lesson"])
    for item in os.listdir("./resources/"):
        if col4.button(item):
            col3.write(open(f"./resources/{item}", "r").read())
