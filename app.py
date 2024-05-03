import streamlit as st
from Setup import setup  # This should only set up configurations, not load data.
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
        if 'vector_index' not in st.session_state:
            if st.button('Initialize System', key='init_system'):
                with st.spinner('🔄 Setting up resources...'):
                    st.session_state.vector_index = setup()
                st.success('System initialized successfully! 🎉')


    st.header('📝 Describe Your Interests')

    # Checkbox for selecting search types
    search_types = st.multiselect(
        'I am interested in:',
        ['Movies', 'Books'],
        ['Movies']  # Default selection
    )


    # Validate selection
    if not search_types:
        st.error('Please select at least one search type.')
    else:
        query = st.text_area(
        'Tell us about what you\'re looking for:',
        key='query_input',
    )

        if st.button('Submit', key='submit_query'):
            if 'vector_index' not in st.session_state:
                with st.spinner('🔄 Initializing resources...'):
                    st.session_state.vector_index = setup()

            query_manager = QueryManager(st.session_state.vector_index)
            st.session_state.response = query_manager.perform_query(query)

            feedback_manager = FeedbackManager(query_manager.query_engine)
            st.session_state.records = feedback_manager.record_query(query)

            # Custom HTML styling for response display
            st.markdown(f"**Response:** <div style='background-color:yellow;padding:10px;border-radius:5px;'>{st.session_state.response.response}</div>", unsafe_allow_html=True)
            st.write('Response:', st.session_state.response)
            st.write('Feedback Records:', st.session_state.records)

    manage_dashboard()

def manage_dashboard():
    st.header('🎮 Trulens Eval Dashboard')
    port = 7000
    ip_address = "192.0.0.2"

    if st.button('🚀 Launch TRU Dashboard', key='launch_dashboard'):
        try:
            st.session_state.dashboard_process = st.session_state.tru.run_dashboard(port=port, force=True)
            st.success(f"🌐 Dashboard is now running on [http://{ip_address}:{port}](http://{ip_address}:{port})")
        except Exception as e:
            st.error(f"🚨 Error launching dashboard: {str(e)}")

    if st.button('🛑 Stop TRU Dashboard', key='stop_dashboard'):
        if 'dashboard_process' in st.session_state and st.session_state.dashboard_process is not None:
            st.session_state.dashboard_process.terminate()
            st.success("Dashboard has been stopped. 🛑")

if __name__ == '__main__':
    main()
