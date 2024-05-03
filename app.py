import streamlit as st

def main():
    st.title('🔍 Discover New Books and Movies!')
    st.markdown("""
    Welcome to your personal recommendation assistant! 🌟📚 Whether you're in the mood for a thrilling mystery, heartwarming romance, or captivating documentary, simply describe your interests and let our app do the rest.
    Just chat with us like you would with a friend, and we'll recommend books and movies tailored just for you. It's that easy!
    """)



    with st.sidebar:
        st.header('🧭 Navigation')
        st.page_link("app.py", label="Home", icon="🏠")
        st.page_link('pages/data.py', label='Data', icon='📊')
        st.page_link('pages/about.py', label='About our team', icon='🌟')
        st.page_link('pages/contact.py', label='Contact us', icon='📧')
        st.page_link('pages/help.py', label='Help', icon='❓')
        st.markdown('---')

    st.warning('⚠️ We incountered errors when deploying the app in Streamlit Sharing.')


    st.button('Click here to see how to run the app on your machine', key='info')
    if st.session_state.info:
        st.write('To view the app, please run the app locally.')
        st.write('1. Clone the repository check our github page:')
        st.page_link('https://github.com/AbdoAnss/Movie-Book-Recommendation',label='Github Repo',icon='🔗')
        st.write('2. Install the required packages:')
        st.code('pip install -r requirements.txt')
        st.write('3. Run the app:')
        st.code('streamlit run app.py')
        st.write('4. Open the app in your browser:')
        st.write('http://localhost:8501')
        st.write('5. Enjoy the app!')
        st.write('If you have any questions, please contact us')
        st.write('Thank you for your understanding.')    


if __name__ == '__main__':
    main()

