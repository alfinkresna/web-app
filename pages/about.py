import streamlit as st

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
<h1 style='text-align: center; color: #fffdfa; font-size: 35px; font-weight: 100;'>
--- About ---
</h1>

<p style='text-align: center;'>
Website ini dibuat hanya untuk test
</p>

<center> <a href="https://www.instagram.com/alfin.kresna_">
My Instagram
</a>
</center>
</div>
''', unsafe_allow_html=True)
