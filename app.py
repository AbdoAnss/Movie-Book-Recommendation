import time
import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PIL import Image

# Define the pages
PAGES = {
    "Home": "home",
    "About Team": "about_team",
    "Contact": "contact"
}

def send_email(sender, recipient, subject, message):
    # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'your_email@gmail.com'  # Your email
    smtp_password = 'your_password'  # Your email password

    # Email content
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()



def main():
    st.sidebar.image('images/logo.png', use_column_width=True)
    
    # Initialize page with a default value
    page = "home"  # Default page
    
    # Navigation buttons
    if st.sidebar.button("Initialize System"):
        page = "init-sys"
    if st.sidebar.button("Home"):
        page = "home"
    if st.sidebar.button("About Team"):
        page = "about_team"
    if st.sidebar.button("Contact"):
        page = "contact"
    
    # Page content
    if page == "home":
       
        st.title("🔍Movies and Books Recommendation System")
        st.markdown("**😉Ready for your next binge?** We'll find the perfect movie or book to fuel your obsession. **🤔💭Can't decide what to watch or read?** Let us be your story sherpa and guide you to your next adventure. **🚀Tell us your taste, we'll find your treasure!** Dive into a personalized world of movies and books you'll love. ")

        st.title("📄 Submit Your Description")
        query = st.text_input("Enter your query here:")
        st.markdown("""
        <style>
            div[data-testid="stTextInput"] input {
                border: 2px solid red !important;
                border-radius: 5px;
                padding: 5px;
            }
        </style>
        """, unsafe_allow_html=True)



        if st.button("Submit"):
            st.write(f"Submitted query: {query}")
        
    elif page == "about_team":
        st.title("About Our Team")

        # Text before the image
        st.write("🌟 Meet our dedicated team of professionals who are passionate about their work and committed to providing the best service to our clients. 💼👩‍💼👨‍💼🔧📈🌟")
        st.write("Check out our team members on lablab.ai:")
        st.write("https://lablab.ai/event/assistants-api-llamaindex-mongodb-battle/datacraft-leaders")
       

    elif page == "contact":
        st.title("Contact Us")
        st.write("Send us your queries and we'll get back to you as soon as possible.")
        
        # Contact form
        with st.form(key='contact_form'):
            sender_email = st.text_input("Your Email")
            subject = st.text_input("Subject")
            message = st.text_area("Message")
            submit_button = st.form_submit_button(label='Send')
            
            if submit_button and sender_email and subject and message:
                # Assuming 'your_email@example.com' is the email you want to receive messages at
                send_email(sender_email, 'your_email@example.com', subject, message)
                st.success("Your query has been sent. We will contact you soon.")

        # Apply red border to input fields
        st.markdown("""
            <style>
                div[data-testid="stTextInput"] input {
                    border: 2px solid red !important;
                    border-radius: 5px;
                    padding: 5px;
                }
                div[data-testid="stTextArea"] textarea {
                    border: 2px solid red !important;
                    border-radius: 5px;
                    padding: 5px;
                }
            </style>
        """, unsafe_allow_html=True)

    

if __name__ == "__main__":
    main()

