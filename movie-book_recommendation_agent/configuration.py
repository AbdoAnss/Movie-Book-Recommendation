from dotenv import load_dotenv
import os
from llama_index.core.settings import Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

class Configuration:
    def __init__(self):
        print("Loading environment variables...")
        load_dotenv()  # Loads the environment variables from the .env file.
        self.openai_api_key = os.getenv('OPENAI_API_KEY')  # Retrieves the OpenAI API key from the environment.

        if not self.openai_api_key:
            print("ERROR: OpenAI API key not found.")  # Error handling if API key is not found.

        self.embed_model = OpenAIEmbedding(model="text-embedding-3-small", dimensions=256)  # Setting up the embedding model.
        self.llm = OpenAI(api_key=self.openai_api_key)  # Initializing the OpenAI model with the API key.
        self.configure()  # Apply the configurations to the settings.

    def configure(self):
        print("Configuring settings...")
        Settings.llm = self.llm  # Sets the global LlamaIndex settings for the language model.
        Settings.embed_model = self.embed_model  # Sets the global embedding model.