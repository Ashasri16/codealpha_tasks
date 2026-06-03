import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translation Tool")

text = st.text_area("Enter Text")

source = st.selectbox(
    "Source Language",
    ["english", "hindi", "telugu"]
)

target = st.selectbox(
    "Target Language",
    ["english", "hindi", "telugu"]
)

if st.button("Translate"):
    translated = GoogleTranslator(
        source=source,
        target=target
    ).translate(text)

    st.success(translated)