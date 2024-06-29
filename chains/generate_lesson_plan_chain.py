from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import PromptTemplate

system_prompt = """
You are an expert curriculum writer whos job is to help teacher create tailored curriculum to their classroom.
Please ensure you are professional, appropiate, and knowledgeable, and use language at an eight grade reading level.
Make sure to take into consideration all the information provided, and generate lesson plans focused on the subject and specific standards provided.
Format all lesson plans in valid markdown format.
"""
llm = Ollama(model="llama3:8b", system=system_prompt, temperature=0)
prompt = PromptTemplate.from_template(
    """
Write a lesson plan including assesments, homework and group activities for a {subject} unit covering the following standard:
{standard}
Additionally consider the following information about the classroom:
{additional_info}

"""
)


LessonChain = prompt | llm
