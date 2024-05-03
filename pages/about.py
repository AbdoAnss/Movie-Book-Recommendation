import streamlit as st

def main():
    st.title("About Us")
    with st.sidebar:
        st.header('🧭 Navigation')
        st.page_link("app.py", label="Home", icon="🏠")
        st.page_link('pages/data.py', label='Data', icon='📊')
        st.page_link('pages/about.py', label='About our team', icon='🌟')
        st.page_link('pages/contact.py', label='Contact us', icon='📧')
        st.page_link('pages/help.py', label='Help', icon='❓')
        st.markdown('---')

    # Define team members with their details
    team_members = [
        {
            "name": "Abdessamad Anssem",
            "role": "Team Lead",
            "bio": "Team lead with a passion for AI and machine learning.",
            "image_url": "https://lablab.ai/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Flablab-static-eu%2Fimages%2Fusers%2Fundefined_picture_xd2acu020r.jpg&w=96&q=75"
        },
        {
            "name": "Achraf Majidi",
            "role": "AI Engineer student",
            "bio": "Experienced software engineer with a focus on AI.",
            "image_url": "https://lablab.ai/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Flablab-static-eu%2Fimages%2Fusers%2Fundefined_picture_jt1yw30l24.jpg&w=96&q=75"
        },
        {
            "name": "Warda Ichaq",
            "role": "Head of Design",
            "bio": "Creative designer with a keen eye for user experience.",
            "image_url": "https://lablab.ai/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Flablab-static-eu%2Fimages%2Fusers%2Fundefined_picture_v114f605wg.jpg&w=96&q=75"
        },
        {
            "name": "Najm Ul Hassan",
            "role": "ML student",
            "bio": "Skilled in digital marketing and brand development.",
            "image_url": "https://lablab.ai/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Flablab-static-eu%2Fimages%2Fusers%2Fundefined_picture_8iv20mg8.jpg&w=96&q=75"
        }
    ]

    # Create multiple columns to display team members horizontally
    cols = st.columns(len(team_members))

    # Display team members in a horizontal layout
    for i, member in enumerate(team_members):
        with cols[i]:
            st.write(f"**{member['name']}**")
            st.write(f"{member['role']}")
            st.image(member['image_url'], width=50, caption=member['bio'], use_column_width=True)


if __name__ == "__main__":
    main()
