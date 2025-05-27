import streamlit as st
from llama_index.llms.llama_cpp import LlamaCPP
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.memory import ChatMemoryBuffer

def init_page() -> None:
    st.set_page_config(page_title="LLAMA Chatbot", layout="wide")
    st.title("🧠 LLAMA Chatbot")
    st.sidebar.title("Options")

def select_llm() -> LlamaCPP:
    return LlamaCPP(
        model_path="llama-2-7b-chat.Q2_K.gguf",  # Update to full path if needed
        temperature=0.1,
        max_new_tokens=500,
        context_window=3900,
        model_kwargs={"n_gpu_layers": 1},
        verbose=True,
    )

def init_messages() -> None:
    if st.sidebar.button("🗑️ Clear Conversation", key="clear"):
        st.session_state.messages = []
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful AI assistant. Reply in markdown.")
        ]

# def get_answer(llm, messages) -> str:
#     response = llm.complete(messages)
#     return response.text
def get_answer(llm, messages) -> str:
    prompt = messages_to_prompt(messages)
    response = llm.complete(prompt)
    return response.text


def render_chat():
    for message in st.session_state.messages:
        if isinstance(message, AIMessage):
            with st.chat_message("assistant"):
                st.markdown(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.markdown(message.content)

def messages_to_prompt(messages) -> str:
    prompt = ""
    for message in messages:
        if isinstance(message, SystemMessage):
            prompt += f"<<SYS>>\n{message.content}\n<</SYS>>\n\n"
        elif isinstance(message, HumanMessage):
            prompt += f"[INST] {message.content} [/INST]\n"
        elif isinstance(message, AIMessage):
            prompt += f"{message.content}\n"
    return prompt

def load_data_index(llm: LlamaCPP) -> RetrieverQueryEngine:
    # Load documents from 'data' folder
    documents = SimpleDirectoryReader("data").load_data()
    
    # Create vector index
    index = VectorStoreIndex.from_documents(documents)
    
    # Create retriever and query engine
    retriever = index.as_retriever(similarity_top_k=3)
    memory = ChatMemoryBuffer.from_defaults(token_limit=2000)

    query_engine = RetrieverQueryEngine.from_args(
        retriever=retriever,
        llm=llm,
        memory=memory,
    )
    return query_engine
# def main() -> None:
#     init_page()
#     llm = select_llm()
#     init_messages()

#     user_input = st.chat_input("Ask me anything...")
#     if user_input:
#         st.session_state.messages.append(HumanMessage(content=user_input))
#         with st.spinner("🤖 Thinking..."):
#             answer = get_answer(llm, st.session_state.messages)
#         st.session_state.messages.append(AIMessage(content=answer))

#     render_chat()

def main() -> None:
    init_page()
    llm = select_llm()
    init_messages()
    #query_engine = load_data_index(llm)
    user_input = st.chat_input("Ask me anything...")

    if user_input:
        # Append user message immediately
        st.session_state.messages.append(HumanMessage(content=user_input))

    # Render all messages before generating the assistant reply
    for message in st.session_state.messages:
        if isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.markdown(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant"):
                st.markdown(message.content)

    # If user just sent a message and last message is from user,
    # generate assistant reply and display it immediately under spinner
    if user_input:
    # Placeholder for assistant message
      placeholder = st.chat_message("assistant")
      with placeholder.container():
        with st.spinner("🤖 Thinking..."):
            # Use query engine to get context-augmented response
            #response = query_engine.query(user_input)
            #st.markdown(response.response)
            answer = get_answer(llm, st.session_state.messages)
        # Clear spinner and show answer inside the same container
        # This ensures icon + message stay aligned
        st.markdown(answer)

      st.session_state.messages.append(AIMessage(content=answer))


if __name__ == "__main__":
    main()
