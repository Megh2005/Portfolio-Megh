import streamlit as st
from forms.contact import contact_form


@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()


col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/pic.png", width=230)
with col2:
    st.title("Megh Deb", anchor=False)
    st.write(
        "Android application developer (KMP-KMM) with a development experience of 3+ years. Interned at several companies."
    )
    if st.button("📧 Contact Me"):
        show_contact_form()


st.write("\n")
st.subheader("Education & Experience", anchor=False)
st.write(
    """
- 3 years experience in android app development
- Strong industry level experience with KMP-KMM
- Knowledge of both SQL and no-SQL databases
- Passed Bachelor's of Technology from Heritage Institute of Technology Kolkata
"""
)


st.write("\n")
st.subheader("Technical Skills", anchor=False)
st.write(
    """
- Programming Languages : C, Python, C++
- Development Frameworks : Kotlin, Ktor, Node, Next.js, React.js
- DevOps Knowledge : Google Cloud Platform, Git, GitHub
- Databse Handling : MongoDB, MySQL, PostgreSQL
"""
)

SOCIAL_MEDIA = {
    "Facebook": "https://facebook.com/iammeghdeb",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com/Megh2005",
    "Twitter": "https://twitter.com/iammeghdeb",
    "Linktree": "https://linktr.ee/meghdeb",
    "Email": "iammeghdeb@gmail.com",
}

st.write("\n")
st.subheader("My Socials", anchor=False)
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
