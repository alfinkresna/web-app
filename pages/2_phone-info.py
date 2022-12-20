import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import streamlit as st

class PhoneNumber:
    def __init__(self, number):
        self.number = phonenumbers.parse(number)
    
    def get_international_format(self):
        return phonenumbers.format_number(self.number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    
    def get_local_format(self):
        return phonenumbers.format_number(self.number, phonenumbers.PhoneNumberFormat.NATIONAL)
    
    def get_country_code(self):
        return self.number.country_code

    def get_provider(self):
        return carrier.name_for_number(self.number, "id")
    
    def get_location(self):
        return geocoder.description_for_number(self.number, "id")

    def get_area(self):
        return geocoder.description_for_number(self.number, "id")
    
    def get_time_zone(self):
        return timezone.time_zones_for_number(self.number)[0]

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
    --- Nomor Telepon ---
    </h1>
    ''', unsafe_allow_html=True)

    phone_number = st.text_input("Masukkan Nomor Telepon Dengan Kode Negara (Contoh : +628):")
    if phone_number:
        try:
            pn = PhoneNumber(phone_number)
            st.write("Format Internasional : ", pn.get_international_format())
            st.write("Format Lokal : ", pn.get_local_format())
            st.write("Provider : ", pn.get_provider())
            st.write("Kode Negara : ", pn.get_country_code())
            st.write("Lokasi : ", pn.get_location())
            st.write("Area : ", pn.get_area())
            st.write("Zona Waktu : ", pn.get_time_zone())
        except phonenumbers.phonenumberutil.NumberParseException as e:
            st.write(e)

if __name__ == '__main__':
    main()
