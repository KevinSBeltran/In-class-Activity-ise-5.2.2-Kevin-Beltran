import streamlit as st

if st.session_state.get("logged_in") == None:
    st.session_state["logged_in"] = False


def login():
    st.session_state.logged_in = True


def logout():
    st.session_state.logged_in = False

company_name = "Fake Company LLC Inc."

st.set_page_config(page_title="About")

st.markdown("# About")
st.sidebar.header("About")

if st.session_state.logged_in:
    st.sidebar.success("Logged in")
    st.sidebar.button("Log out", key="logout", on_click=logout)
else:
    st.sidebar.warning("Not logged in")
    st.sidebar.button("Log in", key="login", on_click=login)

st.sidebar.write(f"This site is copyright {company_name}, 2024")

st.markdown(
    f"""
    {company_name}. is a fake company created in 2024 for the purposes of making a website with a lot of redundant code.

    It produces nothing and has $0 a year in revenue.

    Usually, companies are not called both "LLC" and "Inc." and must choose one, but this is a fake company so it has both just to be funny.

    Here is a logo that I created with Gemini. It has too many "L"s.
    """
)

st.image("./assets/fake_company.png")

with st.expander("Company Info"):
    st.write(
        f"""
        {company_name} is located at 1600 Amphitheatre Parkway Mountain View, CA 94043
    """
    )

with st.expander("Links"):
    st.markdown(
        """
        [Google](https://google.com)

        [Gemini](https://gemini.google.com)

        [Streamlit Docs](https://docs.streamlit.io/)
    """
    )
