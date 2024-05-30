def LoginPage(st, route, **args):
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
        st.title("Login")

        st.session_state.current_id = user_list['xUI778IDUN']['user_id']

        def on_input():
            if 'current_id' in st.session_state:
                st.session_state.current_id = st.session_state.temp_user_id

        def go_to_home_page():
            on_input()
            if st.session_state.current_id in user_list:
                localStorage.setItem('user_id', st.session_state.current_id, key=st.session_state.current_id)
                localStorage.setItem('role',
                                     user_list[st.session_state.current_id]['role'],
                                     key=f'{st.session_state.current_id}+1'
                                     )
                route('home')

        with st.form("login_form"):
            current_id = st.text_input("Give your user id", value=st.session_state.current_id, key='temp_user_id')
            st.form_submit_button('Login', on_click=go_to_home_page)

        st.write('Current Use Id: ', st.session_state.current_id)

        def go_to_register_page():
            route('register')

        st.button("Go To Register", on_click=go_to_register_page)

    with col3:
        st.subheader("Role : UserId")
        for user_index in user_list:
            st.write(f"{user_list[user_index]['role']} : {user_list[user_index]['user_id']}")
