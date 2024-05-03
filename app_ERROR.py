import streamlit as st
from Setup import setup
from Setup_book import setup1  # This should only set up configurations, not load data.
from User_query_management import QueryManager
from Feedback import FeedbackManager
from trulens_eval import Tru

def initialize_tru():
    if 'tru' not in st.session_state:
        st.session_state.tru = Tru()

def main():
    st.title('🔍 Discover New Books and Movies!')
    st.markdown("""
    Welcome to your personal recommendation assistant! 🌟📚 Whether you're in the mood for a thrilling mystery, heartwarming romance, or captivating documentary, simply describe your interests and let our app do the rest.
    Just chat with us like you would with a friend, and we'll recommend books and movies tailored just for you. It's that easy!
    """)


    initialize_tru()

    with st.sidebar:
        st.header('🧭 Navigation')
        st.page_link("app.py", label="Home", icon="🏠")
        st.page_link('pages/data.py', label='Data', icon='📊')
        st.page_link('pages/about.py', label='About our team', icon='🌟')
        st.page_link('pages/contact.py', label='Contact us', icon='📧')
        st.page_link('pages/help.py', label='Help', icon='❓')
        st.markdown('---')
        st.header('⚙️ Configuration')
        st.caption("Adjust system settings and initialize resources as needed.")
        search_type = st.radio('Search for:', ['Movies', 'Books'], index=0)
        st.session_state.search_type = search_type
        if 'vector_index' not in st.session_state:
            if st.button('Initialize System', key='init_system'):
                with st.spinner('🔄 Setting up resources...'):
                    if st.session_state.search_type == 'Movies':
                        st.session_state.vector_index = setup()
                    elif st.session_state.search_type == 'Books':
                        st.session_state.vector_index = setup1()
                st.success('System initialized successfully! 🎉')


    st.header('📝 Describe Your Interests')


    


    # Validate selection
    
    query = st.text_area(
    'Tell us about what you\'re looking for:',
    key='query_input',
)

    if st.button('Submit', key='submit_query'):
        if 'vector_index' not in st.session_state:
            with st.spinner('🔄 Initializing resources...'):
                if st.session_state.search_type == 'Movies':
                    st.session_state.vector_index = setup()
                elif st.session_state.search_type == 'Books':
                    st.session_state.vector_index = setup1()

        query_manager = QueryManager(st.session_state.vector_index)
        st.session_state.response = query_manager.perform_query(query)

        feedback_manager = FeedbackManager(query_manager.query_engine)
        st.session_state.records = feedback_manager.record_query(query)

        # Custom HTML styling for response display
        st.markdown(f"**Response:** <div style='background-color:yellow;padding:10px;border-radius:5px;'>{st.session_state.response.response}</div>", unsafe_allow_html=True)
        st.write('Response:', st.session_state.response)
        st.write('Feedback Records:', st.session_state.records)

    manage_dashboard()

def start_dashboard(port):
    return Tru().run_dashboard(port=port)

def stop_dashboard(process):
    # Add code here to stop the dashboard process
    pass

def manage_dashboard():
    st.header('🎮 Dashboard Management')
    port = 7000
    ip_address = "192.0.0.2"



    if st.button('🚀 Launch TRU Dashboard', key='launch_dashboard'):
        try:
            port = 8502  # Specify the port for the dashboard
            dashboard_process = start_dashboard(port)
            ip_address = 'localhost'  # Specify the IP address for the dashboard
            st.success(f"🌐 Dashboard is now running on http://{ip_address}:{port}")
            st.session_state.dashboard_process = dashboard_process
        except Exception as e:
            st.error(f"🚨 Error launching dashboard: {str(e)}")

    if st.button('🛑 Stop TRU Dashboard', key='stop_dashboard'):
        if 'dashboard_process' in st.session_state and st.session_state.dashboard_process is not None:
            st.session_state.dashboard_process.terminate()
            st.success("Dashboard has been stopped. 🛑")
        

    

if __name__ == '__main__':
    main()

