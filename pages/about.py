import streamlit as st

st.set_page_config(
    page_title='Web App'
)

def about():
    hide = '''
    <style>
    #MainMenu {visibility: hidden;}
    #header {visibility: hidden;}
    .css-1lsmgbg.egzxvld0
    {
        visibility: hidden;
    }
    </style>
    '''

    st.markdown(hide, unsafe_allow_html=True)

    st.markdown('''
    <div class='container'>
    <h1 style='text-align: center; color: #EB0869; font-size: 35px; font-weight: 100;'>
    --- About ---
    </h1>

    <p style='text-align: center;'>
    Website ini dibuat hanya untuk test
    </p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown(
    '<center><a href="https://www.instagram.com/alfin.kresna_">'
    '<img src="https://www.instagram.com/static/images/ico/favicon-192.png/68d99ba29cc8.png" '
    'style="width: 32px; height: 32px; margin: 10px; font-size: 10px;">My Instagram</a></center>',
    unsafe_allow_html=True,)

def main():
    about()

if __name__.__eq__("__main__"):
    main()
