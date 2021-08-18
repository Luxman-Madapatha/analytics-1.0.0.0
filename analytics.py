#!/usr/bin/env python
# coding: utf-8

import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import streamlit.components.v1 as components
import pandas as pd
from pandas_profiling import ProfileReport

def main():
    
    st.set_page_config(layout="wide")
    
    HtmlFile1 = open("analytics.html", 'r', encoding='utf-8')
    source_code1 = HtmlFile1.read()             
    components.html(source_code1, height = 600,width=1200)
    HtmlFile1.close()
    
    
    df = pd.read_excel("new operational report August 2021_.xlsx", sheet_name="PRODUCTION STATUS", skiprows=[0])
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    
    
    df2 = pd.DataFrame()
    df2["SKU"] = df.columns[1:]
    
    for a,b in enumerate(df["SKU"][0:9]):    
        df2[b] = df.iloc[a:a+1,1:].values.reshape(1,-1)[0]
    
    df3 = df2.drop(['Overall Achievement', 'SKU'], axis=1)
    profile = ProfileReport(df3, explorative=True)    
    st.write("Please wait a moment while the Data Profile Report loads..")
    st.write(df3)
    st_profile_report(profile)
    profile_report = profile.to_file("EDAreport.html")
    
    
if __name__ == '__main__':
    main()