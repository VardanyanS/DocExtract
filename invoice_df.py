import pdfplumber
import re
import os
import pandas as pd


def invoice_df(doc_lst):
    full_df = pd.DataFrame()
    for doc in doc_lst:
        pdf = pdfplumber.open(doc)
        df = pd.DataFrame()
        for item in pdf.pages:
            table = item.extract_table()
            dff = pd.DataFrame(table[1::], columns=table[0])
            dff = dff[dff.isnull().sum(axis=1) < 3]
            df = pd.concat([df, dff])
        df.reset_index(inplace=True, drop=True)
        page = pdf.pages[0]
        text = page.extract_text()
        #         print(text)
        document_number = r'№\s+\d+'
        date_pattern = r'[\d]{1,2}.[\d]{1,2}.[\d]{4}'

        document_number = re.findall(document_number, text)
        date_pattern = re.findall(date_pattern, text)
        df['Փաստ №'] = df.apply(lambda x: document_number[0], axis=1)
        df['Ամսաթիվ'] = df.apply(lambda x: date_pattern[3], axis=1)

        sub1 = "Մատակարարը"
        sub2 = "Առաքման գրանցման գիրք 3"
        s = str(re.escape(sub1))
        e = str(re.escape(sub2))
        entity = re.findall(s + "(.*)" + e, text)[0]

        df['Կազմակերպություն'] = df.apply(lambda x: entity, axis=1)

        full_df = pd.concat([full_df, df])
    full_df.reset_index(inplace=True, drop=True)
    return full_df