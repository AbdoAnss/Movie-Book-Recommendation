# Movie & Book Recommendation System

Welcome to the Movie & Book Recommendation System! This application was developed for the 2024 Hackathon: Assistants-api-llamaindex-mongodb-battle. The primary function of this app is to provide movie and/or book recommendations based solely on the user's description of the movie.

## Table of Contents
1. [Roadmap](#roadmap)
2. [Progress](#progress)

## Roadmap

The development of the Movie & Book Recommendation System is divided into the following stages:

1. **Data Filtering and Preprocessing:**
   - Collection of raw data from reliable sources.
   - Filtering of data to remove any irrelevant information.
   - Cleaning and preprocessing of data to ensure consistency and accuracy.
   - Transformation of data into a format suitable for our machine learning models.

2. **RAG Pipeline with LLamaindex, GPT-4, and MongoDB Vector Database:**
    - Development of a MongoDB vector database for storing and querying vector representations of data.
    - Implementation of the Retrieval-Augmented Generation (RAG) pipeline.
    - Integration of LLamaindex for efficient data indexing and retrieval.
    - Use of GPT-4 for generating high-quality text based on user input.


3. **LLM Testing with TruLens:**
   - Evaluation of the Language Learning Model (LLM) using TruLens to ensure its performance and reliability.
   - Identification and rectification of any issues or discrepancies in the LLM.
   - Continuous testing and improvement of the LLM based on user feedback and performance metrics.

## Progress
- Data Filtering: #################--: 90%

- DataSet construction: #################: 100%

```
Movie-Book-Recommendation
├─ .git
│  ├─ config
│  ├─ description
│  ├─ HEAD
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  ├─ sendemail-validate.sample
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ logs
│  │  ├─ HEAD
│  │  └─ refs
│  │     ├─ heads
│  │     │  └─ main
│  │     └─ remotes
│  │        └─ origin
│  │           └─ HEAD
│  ├─ objects
│  │  ├─ info
│  │  └─ pack
│  │     ├─ pack-84738efec78a09533b80ca85df4e43dfed9d0e4a.idx
│  │     ├─ pack-84738efec78a09533b80ca85df4e43dfed9d0e4a.pack
│  │     └─ pack-84738efec78a09533b80ca85df4e43dfed9d0e4a.rev
│  ├─ packed-refs
│  └─ refs
│     ├─ heads
│     │  └─ main
│     ├─ remotes
│     │  └─ origin
│     │     └─ HEAD
│     └─ tags
├─ .gitignore
├─ app.py
├─ configuration.py
├─ Data_management.py
├─ default.sqlite
├─ Feedback.py
├─ first_30_books.json
├─ first_50_films.json
├─ pages
│  ├─ about.py
│  ├─ contact.py
│  ├─ data.py
│  └─ help.py
├─ README.md
├─ requirements.txt
├─ Setup.py
├─ User_query_management.py
└─ __pycache__
   ├─ configuration.cpython-312.pyc
   ├─ Data_management.cpython-312.pyc
   ├─ Feedback.cpython-312.pyc
   ├─ Setup.cpython-312.pyc
   └─ User_query_management.cpython-312.pyc

```