from Data_management import DataManager, DocumentProcessor, IndexManager
from configuration import Configuration

def setup():
    config = Configuration()
    mongo_uri = "mongodb+srv://majidiahmed799:6EuT2KYiSTXb5Lau@cluster0.cixrvkn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    db_name = 'majidi'
    collection_name = 'movies'
    json_path = 'first_50_films.json'

    data_manager = DataManager(mongo_uri, db_name, collection_name, json_path=json_path)
    document_processor = DocumentProcessor(data_manager, config.embed_model)
    nodes = document_processor.process_documents()

    index_manager = IndexManager(mongo_uri, db_name, collection_name, index_name='vector_index')
    index_manager.add_to_index(nodes)
    vector_index = index_manager.create_index()

    return vector_index