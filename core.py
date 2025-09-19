 # Step A: Setup - Importing necessary libraries and loading our secret key
import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from github import Github

# Load environment variables from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# --- We will now define the functions that make our app work ---

# Step B: A function to fetch the README content from a GitHub repo
def get_github_repo_content(repo_url):
    """
    Takes a GitHub repo URL and returns the content of its README.md file.
    """
    try:
        # Extract the user/repo part from the URL
        repo_path = repo_url.split("github.com/")[1]
        g = Github() # You can add a GitHub token here for more requests
        repo = g.get_repo(repo_path)
        readme_content = repo.get_readme().decoded_content.decode('utf-8')
        return readme_content
    except Exception as e:
        print(f"Error fetching README: {e}")
        return None

# Step C: A function to split the text into smaller chunks
def get_text_chunks(text):
    """
    Takes a long text and splits it into smaller chunks for processing.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    return chunks

# Step D: A function to create our "magic index" (Vector Store)
def get_vectorstore(text_chunks):
    """
    Takes text chunks, creates embeddings using a local model, and stores them in a Chroma vector store.
    """
    # Use a free, open-source embedding model from Hugging Face
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # We are storing the vectors in-memory for simplicity
    vectorstore = Chroma.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

# Step E: A function to create the "brain" that connects everything
def get_conversation_chain(vectorstore):
    """
    Creates a conversational chain that uses the vector store and a chat model.
    """
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)
    # Memory allows the chatbot to remember previous parts of the conversation
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

# --- This is the main part of the script that runs when we execute it ---

if __name__ == '__main__':
    # 1. Define the target GitHub repository
    repo_url = "https://github.com/langchain-ai/langchain"
    print(f"Fetching README from {repo_url}...")

    # 2. Get the content
    readme_text = get_github_repo_content(repo_url)

    if readme_text:
        # 3. Split the content into chunks
        print("Splitting text into chunks...")
        chunks = get_text_chunks(readme_text)

        # 4. Create the vector store (our "magic index")
        print("Creating vector store... this may take a moment.")
        vectorstore = get_vectorstore(chunks)

        # 5. Create the conversation chain (our "brain")
        print("Creating conversation chain...")
        conversation_chain = get_conversation_chain(vectorstore)

        print("\nReady to chat! Type 'exit' to quit.")
        
        # 6. Start the conversation loop
        while True:
            user_question = input("Your question: ")
            if user_question.lower() == 'exit':
                break
            
            # Get the answer from our "brain"
            response = conversation_chain.invoke({'question': user_question})
            chat_history = response['chat_history']
            
            # Print the AI's answer
            print("AI Answer:", chat_history[-1].content) # The last message is the AI's answer
