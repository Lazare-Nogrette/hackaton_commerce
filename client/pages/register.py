import string
import random


def RegisterPage(st, route, **args):
    localStorage = args['localStorage']

    user_list = {
        'xUI778IDUN': {
            'user_id': 'xUI778IDUN',
            'role': 'client'
        },
        'II898DD8': {
            'user_id': 'II898DD8',
            'role': 'client'
        },
        'xxcUUAA8': {
            'user_id': 'xxcUUAA8',
            'role': 'client'
        },
        'xxcUUIPZ7': {
            'user_id': 'xxcUUIPZ7',
            'role': 'admin'
        },

    }
    col1, col2, col3 = st.columns([4, 8, 4], gap="large")

    with col1:
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col2:
        st.title("Register")

        role = st.selectbox('Role', ['Client', 'Admin', ])

        def go_to_home_page():
            localStorage.setItem('user_id', st.session_state.current_id, key=st.session_state.current_id)
            localStorage.setItem('role', role, key=f'{st.session_state.current_id}+1')
            route('home')

        st.session_state.current_id = ''

        def generate_random_id():
            length = 10
            characters = string.ascii_letters + string.digits
            st.session_state.current_id = ''.join(random.choice(characters) for _ in range(length))

        generate_random_id()

        st.button("Generate Id", on_click=generate_random_id)
        with st.form("login_form"):
            st.session_state.current_id = st.text_input("User Id", value=st.session_state.current_id, disabled=True, key='user_id')
            st.form_submit_button('Register', on_click=go_to_home_page)

        st.write('Current Use Id is:  ', st.session_state.current_id, )
        st.write('Current User Role:  ', role)
        st.write('You can click on [Generate Id] button if you do not Like it!')

        def go_to_login_page():
            route('login')

        st.button("Back to Login", on_click=go_to_login_page)

    with col3:
        st.subheader("")
