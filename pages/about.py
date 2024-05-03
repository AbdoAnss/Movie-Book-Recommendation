import streamlit as st

def main():
    st.title("About Us")

    # Define team members with their details
    team_members = [
        {
            "name": "John Doe",
            "role": "Co-Founder & CEO",
            "bio": "Passionate about innovation and technology.",
            "image_url": "https://source.unsplash.com/400x400/?person"
        },
        {
            "name": "Jane Smith",
            "role": "CTO",
            "bio": "Experienced software engineer with a focus on AI.",
            "image_url": "https://source.unsplash.com/400x400/?woman"
        },
        {
            "name": "Michael Johnson",
            "role": "Head of Design",
            "bio": "Creative designer with a keen eye for user experience.",
            "image_url": "https://source.unsplash.com/400x400/?man"
        },
        {
            "name": "Emily Brown",
            "role": "Marketing Manager",
            "bio": "Skilled in digital marketing and brand development.",
            "image_url": "https://source.unsplash.com/400x400/?girl"
        }
    ]

    # Display team members in a vertical layout
    for member in team_members:
        st.subheader(f"{member['name']} - {member['role']}")
        st.image(member['image_url'], caption=member['bio'], use_column_width=True)
        st.write(" ")  # Add space between team members

if __name__ == "__main__":
    main()
