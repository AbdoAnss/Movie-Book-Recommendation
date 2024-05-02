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
    st.sidebar.title('CineLit')
    
    # Initialize page with a default value
    page = "home"  # Default page
    
    # Navigation buttons
    if st.sidebar.button("Home"):
        page = "home"
    if st.sidebar.button("About Team"):
        page = "about_team"
    if st.sidebar.button("Contact"):
        page = "contact"
    
    # Page content
    if page == "home":
        st.title("Welcome to Our Bot!")
        st.write("Your Favourite bot for movies and books recommendation.")
        
        # Input field for user to input a description
        st.text_input("Enter a description of a movie or book:")
        
    elif page == "about_team":
        st.title("About Our Team")

        # Text before the image
        st.write("Meet our dedicated team of professionals who are passionate about their work and committed to providing the best service to our clients.")

        # Create columns for parallel image display
        col1, col2 = st.columns(2)
        
        # Open and resize images
        image1 = Image.open('images/image1.jpeg')
        resized_image1 = image1.resize((300, 200))  # Adjust width and height as needed
        image2 = Image.open('images/image2.jpeg')
        resized_image2 = image2.resize((300, 200))  
        
        # Display images and captions in parallel columns
        with col1:
            st.image(resized_image1, caption="I'm a Computer Science student who is passionate about ML and Data science. I'm always eager to learn more and expand my knowledge in these fields.", use_column_width=False)
        with col2:
            st.image(resized_image2, caption="👋 Hi, I’m @NajmiHassan. 👀 I’m interested in Python Programming and Machine Learning.🌱 I’m currently a learner in AI. 💞️ I’m looking to collaborate on ML Projects", use_column_width=False)
    

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

if __name__ == "__main__":
    main()
