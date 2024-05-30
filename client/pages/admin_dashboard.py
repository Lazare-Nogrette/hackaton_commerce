from streamlit_extras.grid import grid
from streamlit_extras.row import row
import pandas as pd
import numpy as np
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
from server.main import Model



def DashboardPage(st, route, **args):
    localStorage = args['localStorage']
    go_to_logout_page = args['logout']

    model_trained = Model()

    # Function to create an interactive grid
    def dataframe_with_selections(df, key):
        gb = GridOptionsBuilder.from_dataframe(df)
        # selection_mode = multiple or unique
        gb.configure_selection(selection_mode="unique", use_checkbox=True)
        gridOptions = gb.build()

        response = AgGrid(
            df,
            gridOptions=gridOptions,
            enable_enterprise_modules=False,
            height=400,
            update_mode=GridUpdateMode.SELECTION_CHANGED,  # Capture the updated state
            data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
            fit_columns_on_grid_load=True,
            key=key  # Ensure a unique key for each AgGrid instance
        )

        selected_rows = response.get('selected_rows', [])
        return pd.DataFrame(selected_rows)

    st.button("Logout", on_click=go_to_logout_page)
    st.title("Dashboard")

    df_user = model_trained.get_user_record()
    df_product = model_trained.get_product_record()

    # row1 = row([2,6], vertical_align="center")
    col1, col2 = st.columns([4, 8], gap="medium")

    with col1:
        users_selected = dataframe_with_selections(df_user, 'user_id')
        # print(users_selected)
    with col2:
        products_selected = dataframe_with_selections(df_product, 'product_id')
    # row1.line_chart(random_df, use_container_width=True)

    # row2 = row(1, vertical_align="bottom")

    # row2.selectbox("Select Country", ["Germany", "Italy", "Japan", "USA"])
    if not users_selected.empty and not products_selected.empty:
        user_id = users_selected['user_id'].values[0]
        product_id = products_selected['product_id'].values[0]
        st.subheader(f"The user with id: {user_id}, you selected the product id: {product_id}", )
        # st.button("Will buy", type='secondary')
        # row1 = row(8, vertical_align="center")
        purchase = model_trained.will_purchase_product(user_id, product_id)
        yes = (purchase == 1).sum()
        no = (purchase == 0).sum()
        print(f"The purchase: {'Yes' if yes >= no else 'No'}")
        st.button(f"The user {'' if yes >= no else 'Not'} Buy!!!", type='secondary' if yes >= no else 'primary' , use_container_width=True)

    # row2.button("Send", use_container_width=True)

    # st.subheader(f"The user with id {user_id} will buy the product {product_id}")


