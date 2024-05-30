def HomePage(st, route, **args):
    localStorage = args['localStorage']
    go_to_logout_page = args['logout']

    st.button("Logout", on_click=go_to_logout_page)
    st.title("Home")

    def on_input():
        if 'temp_input' in st.session_state:
            st.session_state.search_input = st.session_state.temp_input

    search_product = st.text_input("Give your user id", value='product name', on_change=on_input, key='temp_input')

    col1, col2 = st.columns([4, 8,], gap="medium")

    with col1:
        with st.container():
            st.write("Menu")

    with col2:
        with st.container():
            st.write("Product")

            if 'search_input' in st.session_state:
                st.write("Searching.... ", st.session_state.search_input)

