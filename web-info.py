import streamlit as st
from whois import whois

st.set_page_config(
    page_title='Web Info'
)

def sc():
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


def main():

    sc()

    form = st.form(key='form')

    f = form.text_input(label='Masukkan Nama Domain Web (Contoh : www.google.com)')

    submit = form.form_submit_button(label='Check')

    with st.spinner("Tunggu Sebentar..."):
        if submit:
            st.write(f'''
    Domain ID : {whois(f).domain_id}

    Nama Domain : {whois(f).domain_name}

    Tanggal Pembuatan : {whois(f).creation_date}

    Tanggal Diperbarui : {whois(f).updated_date}

    Tanggal Kedaluwarsa : {whois(f).expiration_date}

    Nama : {whois(f).name}

    Email : {whois(f).emails}

    Organisasi : {whois(f).org}

    Alamat : {whois(f).address}

    Kota : {whois(f).city}

    Negara Bagian : {whois(f).state}

    Negara : {whois(f).country}

    Dnssec : {whois(f).dnssec}

    Nama Server : {whois(f).name_servers}

    Referral URL : {whois(f).referral_url}

    Status : {whois(f).status}

    Registrar : {whois(f).registrar}

    Kota Registrar : {whois(f).registrar_city}

    Kode Pos Registrar : {whois(f).registrar_postal_code}

    Negara Registrar : {whois(f).registrar_country}

    Nomor Telephone Registrar : {whois(f).registrar_phone}

    Email Registrar : {whois(f).registrar_email}

    ID Registrant : {whois(f).registrant_id}

    Nama Registrant : {whois(f).registrant_name}

    Organisasi Registrant : {whois(f).registrant_org}

    Alamat Registrant : {whois(f).registrant_address}

    Alamat 2 : {whois(f).registrant_address2}

    Alamat 3 : {whois(f).registrant_address3}

    Kota Registrant : {whois(f).registrant_city}

    Negara Registrant : {whois(f).registrant_country}

    Kode Pos Registrant : {whois(f).registrant_postal_code}

    Nomor Telephone Registrant : {whois(f).registrant_phone}

    Registrant Fax : {whois(f).registrant_fax}

    Email Registrant : {whois(f).registrant_email}
    ''')


if __name__ == "__main__" :
    main()