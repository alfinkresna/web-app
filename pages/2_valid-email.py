import streamlit as st
from requests import get

st.set_page_config(
    page_title='Web App'
)

class validEmail:
    def __init__(self, email: str) -> None:
        self.email = email
        self.rq = get('https://www.disify.com/api/email/' + self.email)

    def show(self):
        return self.rq.text

def main():
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
    <h1 style='text-align: center; color: #EB0869; font-size: 35px; font-weight: 100;'>
    --- Validasi Email ---
    </h1>
    ''', unsafe_allow_html=True)

    user_input = st.text_input("Masukkan alamat email yang ingin Anda validasi :")
    if user_input:
        valid_email = validEmail(user_input)
        data = valid_email.show()
        st.write(f"Hasil validasi email {user_input} :")
        st.json(data)

if __name__ == "__main__":
    main()
