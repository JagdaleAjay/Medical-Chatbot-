from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from typing import List
from langchain.schema import Document


# 1. Extract Data from PDF File
def load_pdf_file(data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader  # ✅ Fixed: was myPDFLoader
    )
    documents = loader.load()
    return documents


# 2. Filter to Minimal Metadata
def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    minimal_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
            )
        )
    return minimal_docs


# 3. Split the Data into Chunks
def text_split(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
    )
    texts_chunk = text_splitter.split_documents(minimal_docs)
    return texts_chunk


# 4. Download Embeddings from HuggingFace
def download_hugging_face_embeddings():  # ✅ Fixed: renamed to match import
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embeddings