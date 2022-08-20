import streamlit as st
import pandas as pd

def main():
    st.title("Air Passengers Analysis")
    data = pd.read_csv("AirPassengers.csv")
    data['Year'] = data['Month'].apply(lambda x: x.split('-')[0])
    year = st.selectbox('select year', data['Year'].unique())
    button  =  st.button('Show Results')

    if button:
        subset = sata[ data['Year'] == year ]
        st.table(subset)

if __name__== '__main__':
    main()
