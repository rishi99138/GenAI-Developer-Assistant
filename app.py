import streamlit as st
# We import the functions we made in our "brain" file
from core import get_github_repo_content, get_text_chunks, get_vectorstore, get_conversation_chain

def main():
    # --- Page Setup ---
    # Sets the title that appears in the browser tab
    st.set_page_config(page_title="GitHub Repo Assistant", page_icon="🤖")
    
    # --- Main Title ---
    st.title("🤖 GitHub Repo Assistant")
    st.write("Ask questions about a public GitHub repository. Just provide the URL!")

    # --- User Input Fields ---
    # Creates a text box for the GitHub URL
    repo_url = st.text_input("Enter the GitHub Repository URL:")
    
    # Creates a text box for the user's question
    user_question = st.text_input("Ask your question about the repository:")

    # --- Process Button ---
    # Creates a button. The code inside the 'if' block runs only when it's clicked.
    if st.button("Get Answer"):
        # --- Input Validation ---
        if not repo_url or not user_question:
            st.warning("Please provide both a repository URL and a question.")
        else:
            try:
                # --- The "Thinking" Process ---
                # A spinner shows a "loading" message while the AI works
                with st.spinner("Fetching repo, creating index, and generating answer... Please wait."):
                    
                    # 1. Get the repo content (from core.py)
                    readme_text = get_github_repo_content(repo_url)
                    
                    if readme_text:
                        # 2. Split the content into chunks (from core.py)
                        chunks = get_text_chunks(readme_text)
                        
                        # 3. Create the vector store (from core.py)
                        vectorstore = get_vectorstore(chunks)
                        
                        # 4. Create the conversation chain (from core.py)
                        conversation_chain = get_conversation_chain(vectorstore)
                        
                        # 5. Get the answer from the AI
                        response = conversation_chain.invoke({'question': user_question})
                        
                        # --- Display the Answer ---
                        st.success("Here is the answer:")
                        st.write(response['answer'])
                    else:
                        st.error("Could not fetch the README from the provided URL. Please check the URL and try again.")
            
            except Exception as e:
                st.error(f"An error occurred: {e}")

# This makes sure the main() function runs when the script is executed
if __name__ == '__main__':
    main()