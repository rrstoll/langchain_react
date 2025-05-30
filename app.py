import os
from dotenv import load_dotenv
import streamlit as st

from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate

from tools.search_tool import search_tool
from tools.calculator_tool import calculator_tool
from tools.weather_tool import weather_tool
from tools.news_tool import news_tool

# Load API keys
load_dotenv()

# Initialize LLM
llm = ChatOpenAI(model="gpt-4", temperature=0)

# Define custom ReAct prompt with correct variables
react_prompt = PromptTemplate(
    input_variables=["input", "agent_scratchpad", "tools", "tool_names"],
    template="""
You are a helpful AI agent. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought: {agent_scratchpad}
"""
)

# Tools list
tools = [search_tool, calculator_tool, weather_tool, news_tool]

# Create ReAct agent
agent = create_react_agent(llm, tools, react_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

st.set_page_config(page_title="City Info", page_icon="")
st.image("assets/cityscape.png", use_container_width=False)

# Custom CSS for Streamlit app
st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .stAppViewContainer {
        top: 4rem;
    }
    .block-container + div {
        flex-grow: 0;
    }
    .stApp h1 {
        text-align: center;
        font-size: 2.5rem;
        color: #0a3d62;
    }
    .stMarkdown p {
        font-size: 1.2rem;
        text-align: center;
    }
    .stChatMessage {
        border-radius: 12px;
        padding: 10px;
        margin: 10px 0;
    }
    .stChatMessage.user {
        background-color: #dff9fb;
        color: #130f40;
    }
    .stChatMessage.assistant {
        background-color: #f6e58d;
        color: #30336b;
    }
    .stTextInput>div>div>input {
        font-size: 1.1rem;
        padding: 8px;
        border-radius: 8px;
    }
    .stButton>button {
        font-size: 1.1rem;
        padding: 8px 20px;
        background-color: #0a3d62;
        color: white;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #2980b9;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("City Info")
st.markdown("Ask me a question about a foreign city!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        try:
            response = agent_executor.invoke({"input": user_input})["output"]
        except Exception as e:
            response = f"Error: {e}"
    st.session_state.messages.append({"role": "assistant", "content": response})

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(msg["content"])
