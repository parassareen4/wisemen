import streamlit as st 
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content

st.title("Wisemen")
url = st.text_input("Enter the URL: ")

if st.button("Scrape Site"):
    st.write("Scraping...")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    st.session_state.dom_content = cleaned_content
    
    with st.expander("View Content"):
        st.text_area("DOM Content",cleaned_content,height=300)

