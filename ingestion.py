from langchain_core.documents import Document
from langchain_community.document_loaders import  TextLoader


loader = TextLoader("data/text_files/sample.txt", encoding="utf-8")
print(loader.load())
