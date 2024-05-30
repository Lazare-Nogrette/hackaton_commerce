import streamlit as st
from streamlit_local_storage import LocalStorage
from client.pages.index import (
    LoginPage,
    RegisterPage,
    HomePage,
    DashboardPage
)

# Always set it first !!!!!!!!!!!
st.set_page_config(layout="wide", page_title="Ecommerce")

localStorage = LocalStorage()


def setRoute(route):
    st.query_params.page = route
    st.session_state.route = route


def isLogged():
    return localStorage.getItem('user_id')


def getRole():
    return localStorage.getItem('role')


def logout():
    localStorage.deleteAll()
    # localStorage.deleteItem('user_id')
    # localStorage.deleteItem('role')
    st.session_state.route = 'login'


def startApplication(route='login'):
    # localStorage.deleteAll()
    if 'route' not in st.session_state:
        if localStorage.getItem('user_id'):
            st.session_state.route = 'dashboard' if localStorage.getItem('role') == 'admin' else 'home'
        else:
            setRoute(route)

    print('Current Route: ', st.session_state.route)

    match st.session_state.route:
        case 'login':
            LoginPage(st, setRoute, **{"localStorage": localStorage, "logout": logout})
        case 'register':
            RegisterPage(st, setRoute, **{"localStorage": localStorage, "logout": logout})
        case 'home':
            # print('Role is: ', getRole())
            if isLogged() and getRole() == 'client':
                HomePage(st, setRoute, **{"localStorage": localStorage, "logout": logout})
            else:
                setRoute('dashboard')
        case 'dashboard':
            DashboardPage(st, setRoute, **{"localStorage": localStorage, "logout": logout})
