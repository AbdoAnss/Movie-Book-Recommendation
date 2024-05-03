import streamlit as st

def main():
    st.title("Contact Us")
    with st.sidebar:
        st.header('🧭 Navigation')
        st.page_link("app.py", label="Home", icon="🏠")
        st.page_link('pages/data.py', label='Data', icon='📊')
        st.page_link('pages/about.py', label='About our team', icon='🌟')
        st.page_link('pages/contact.py', label='Contact us', icon='📧')
        st.page_link('pages/help.py', label='Help', icon='❓')
        st.markdown('---')

    # Display contact form
    st.write("Please fill out the form below to get in touch with us.")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message", height=150)
    
    # Submit button
    if st.button("Submit"):
        if name and email and message:
            # Process the form (e.g., send email, save to database, etc.)
            st.success("Thank you for your message! We will get back to you soon.")
        else:
            st.error("Please fill out all the fields.")

if __name__ == "__main__":
    main()
