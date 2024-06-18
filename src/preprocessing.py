from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.docstore.document import Document

def file_preprocessing(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    content = ''

    for page in docs:
        content += page.page_content

    
    text_splitter = TokenTextSplitter(
        model_name='gpt-3.5-turbo',
        chunk_size = 10000,
        chunk_overlap=200
    )

    chunks_doc = text_splitter.split_text(content)

    document_chunk = [Document(page_content=con) for con in chunks_doc]

    return document_chunk