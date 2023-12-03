# Streamlit App

## Importantant libraries for the Streamlit app
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


## Web page title
st.markdown(''' # **Exploratory Data Analysis Web App**
This app is developed to give you a quick EDA of your data. 
''')

##uploading a generative image
st.image('image.jpg')

##side bar
with st.sidebar.header(" Upload your dataset(.csv)"): 
    Uploaded_file = st.sidebar.file_uploader("Upload your data (csv)", type=['csv'])
    
    
if Uploaded_file is not None:
    st.cache_resource
    def load_csv():
        csv = pd.read_csv(Uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header(''' **dataset**''')
    st.write(df)
    st.write('---')
    st.header('**Pandas profile report**')
    st_profile_report(pr)

else:
    st.info("Awaiting CSV file")
    if st.button("Press to use the example dataset"):
        def load_data():
            a = pd.DataFrame(np.random.rand(100, 5),
                             columns=["A", "B", "C", "D", "E"]) # creating a dataframe having five columns
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header(''' **dataset**''')
        st.write(df)
        st.write('---')
        st.header('**Pandas profile report**')
        st_profile_report(pr)
            
    

