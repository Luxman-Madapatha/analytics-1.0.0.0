#!/usr/bin/env python
# coding: utf-8

import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import streamlit.components.v1 as components

def main():
    
    st.set_page_config(layout="wide")
    
    HtmlFile1 = open("analytics.html", 'r', encoding='utf-8')
    source_code1 = HtmlFile1.read()             
    components.html(source_code1, height = 600,width=1200)
    HtmlFile1.close()
    
if __name__ == '__main__':
    main()