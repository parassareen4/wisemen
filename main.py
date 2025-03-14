import streamlit as st 
from scrape import scrape_website

st.title("Wisemen")
url = st.text_input("Enter the URL: ")

if st.button("Scrape Site"):
    st.write("Scraping...")
    result = scrape_website(url)
    print(result)