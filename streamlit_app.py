import streamlit as st
import hsfs

api_key=st.secrets['HOPSWORKS_API_KEY']

connection = hsfs.connection(host="045935c0-1513-11ec-bc0a-3fc6d8d2ac72.cloud.hopsworks.ai",
                             project="demo_fs_meb10180",
                             engine="hive",
                             api_key_value=api_key)

fs = connection.get_feature_store()
teams_features = fs.get_feature_group("teams_features",version=1)

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
