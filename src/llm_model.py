from langchain_groq import ChatGroq


llm_model = ChatGroq(
    groq_api_key="GROQ_API_KEY",
    model_name="mixtral-8x7b-32768"
)