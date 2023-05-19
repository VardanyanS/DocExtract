import os

import streamlit as st
from PIL import Image
from invoice_df import invoice_df


def simple_ui():
    with st.sidebar:
        image = Image.open('IMG_6473.jpg')
        st.image(image, caption='ML Proof of Concepts')
        # st.title("Sedrak Vardanyan")
        choice = st.radio('Navigation', ['InvoiceParsern', 'SomethingElse'])
        st.info('DocSense is an AI-powered document analysis tool that extracts valuable information from PDFs')
    if choice == "InvoiceParsern":
        st.title('Upload your PDFs')
        img_lst = st.file_uploader('Upload PDFs', accept_multiple_files=True)
        result = invoice_df(img_lst)
        if not result.empty:
            st.write(result)




if __name__ == "__main__":
    simple_ui()
    st.write("Hello i'm here")
    # main()
