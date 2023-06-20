import os

import streamlit as st
from PIL import Image
from invoice_df import invoice_df


def simple_ui():
    with st.sidebar:
        image = Image.open('invoice.jpg')
        # image = image.rotate(270)
        st.image(image, caption='Proof of Concepts')
        # st.title("Sedrak Vardanyan")
        choice = st.radio('Navigation', ['InvoiceParser', 'SomethingElse'])
        st.info('DocSense is an document analysis tool that extracts information from PDF type invoices')
    if choice == "InvoiceParser":
        st.title('Upload your Invoices')
        invoice_lst = st.file_uploader('Upload PDF files', accept_multiple_files=True)
        result = invoice_df(invoice_lst)
        if not result.empty:
            st.write(result)

    @st.cache_data
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8-sig')


    csv = convert_df(result)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='results.csv',
        mime='text/csv',
    )



if __name__ == "__main__":
    hide_streamlit_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    simple_ui()
    st.write("Hello i'm here")
    # main()
