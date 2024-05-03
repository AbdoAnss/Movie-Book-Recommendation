import streamlit as st

def main():
    st.title("Help")

    # Display help content
    st.write("Welcome to the Help page. Here are some common questions and answers:")

    # FAQ section
    st.header("FAQs")
    st.write("**Q: How do I use this app?**")
    st.write("A: This app allows you to discover book and movie recommendations. Simply describe what you're looking for to get personalized suggestions.")
    st.write("**Q: Can I save my favorite recommendations?**")
    st.write("A: Currently, this feature is not available. We're working on adding it in a future update.")
    st.write("**Q: How can I contact support?**")
    st.write("A: Visit our Contact Us page to get in touch with our support team.")

if __name__ == "__main__":
    main()
