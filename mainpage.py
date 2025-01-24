import streamlit as st
import pandas as pd

st.set_page_config(page_title="Covid-19 Cases: Team Presentation", page_icon="🦠")


st.title("Covid-19 Cases")


st.markdown("""
    *An overview of COVID-19 cases and their impacts.*
    
    This presentation includes insights about the Covid-19 pandemic, its effects, 
    and the various aspects associated with it such as affected age groups, comorbidities, 
    and other significant findings.
""")


team_members = {
    "Azzam": "https://www.linkedin.com/in/awangkuazzam",
    "Fahmi": "https://www.linkedin.com/in/ahmad-fahmi32",
    "Adawiyah": "https://www.linkedin.com/in/adawiyahtumiran",
    "Ainaa": "https://www.linkedin.com/in/nrlainaa"
}


if "show_team" not in st.session_state:
    st.session_state.show_team = False


col1, col2, col3 = st.columns(3)
with col2:
    if st.button("Meet the Team"):
        st.session_state.show_team = not st.session_state.show_team  


if st.session_state.show_team:
    st.subheader("Team Members")
    for member, url in team_members.items():
        st.markdown(f'''
            <div class="team-member">
                <a href="{url}" target="_blank" class="team-member-link">{member}</a>
            </div>
        ''', unsafe_allow_html=True)


st.markdown('<div class="footer">© 2025 Covid-19 Presentation Team. All Rights Reserved.</div>', unsafe_allow_html=True)