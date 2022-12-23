import streamlit as st
from whois import whois

st.set_page_config(
    page_title='Web App', initial_sidebar_state="expanded"
)

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
    --- Website Info ---
    </h1>
    ''', unsafe_allow_html=True)

class WebInfo:
    def __init__(self):
        self.form = st.form(key='form')
        self.domain_name = self.form.text_input(label='Masukkan Nama Domain Web (Contoh : www.google.com)')
        self.submit = self.form.form_submit_button(label='Check')

    def display_info(self):
        with st.spinner("Tunggu Sebentar..."):
            if self.submit:
                st.write(f'''
    Domain ID : {whois(self.domain_name).domain_id}

    Nama Domain : {whois(self.domain_name).domain_name}

    Tanggal Pembuatan : {whois(self.domain_name).creation_date}

    Tanggal Diperbarui : {whois(self.domain_name).updated_date}

    Tanggal Kedaluwarsa : {whois(self.domain_name).expiration_date}

    Nama : {whois(self.domain_name).name}

    Email : {whois(self.domain_name).emails}

    Organisasi : {whois(self.domain_name).org}

    Alamat : {whois(self.domain_name).address}

    Kota : {whois(self.domain_name).city}

    Negara Bagian : {whois(self.domain_name).state}

    Negara : {whois(self.domain_name).country}

    Dnssec : {whois(self.domain_name).dnssec}

    Nama Server : {whois(self.domain_name).name_servers}

    Referral URL : {whois(self.domain_name).referral_url}

    Status : {whois(self.domain_name).status}

    Registrar : {whois(self.domain_name).registrar}

    Kota Registrar : {whois(self.domain_name).registrar_city}

    Kode Pos Registrar : {whois(self.domain_name).registrar_postal_code}

    Negara Registrar : {whois(self.domain_name).registrar_country}

    Nomor Telephone Registrar : {whois(self.domain_name).registrar_phone}

    Email Registrar : {whois(self.domain_name).registrar_email}

    ID Registrant : {whois(self.domain_name).registrant_id}

    Nama Registrant : {whois(self.domain_name).registrant_name}

    Organisasi Registrant : {whois(self.domain_name).registrant_org}

    Alamat Registrant : {whois(self.domain_name).registrant_address}

    Alamat 2 : {whois(self.domain_name).registrant_address2}

    Alamat 3 : {whois(self.domain_name).registrant_address3}

    Kota Registrant : {whois(self.domain_name).registrant_city}

    Negara Registrant : {whois(self.domain_name).registrant_country}

    Kode Pos Registrant : {whois(self.domain_name).registrant_postal_code}

    Nomor Telephone Registrant : {whois(self.domain_name).registrant_phone}

    Registrant Fax : {whois(self.domain_name).registrant_fax}

    Email Registrant : {whois(self.domain_name).registrant_email}
    ''')

def main():
    web_info = WebInfo()
    web_info.display_info()

if __name__ == "__main__" :
    main()
