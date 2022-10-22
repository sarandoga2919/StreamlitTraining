import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

# st.markdown(
#     """
#     <style>
#     .main {
#         background-color: #f5f5f5
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# as long as the filename doesn't change, 
# the below function is not going to run again st is going to save the results of this actions of this function
# somewhere and when you call it again it's not goint to perform the action, it's just goint to send you 
# the save version automatically
#@st.cache 
#def get_data(filename):
#    data = pd.read_csv(filename)
#    return data

with header:
    # title is the biggest letter format
    st.title("Welcome to my amazing app!")
    # small text format
    st.text("In this project I look into the transactions of taxis in NYC")

with dataset:
    st.header("NYC taxi dataset")
    st.write("this data can be downloaded from [taxi data](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)")

    # read the csv file
    taxi_data_1 = pd.read_csv("Data/data_reports_monthly.csv")
    st.write(taxi_data_1.head(5))

    taxi_data = pd.read_csv("Data/taxi+_zone_lookup.csv")
    st.write(taxi_data.head(10))

    # plotting the service zone
    st.subheader('Number of service zone available')
    service_zone_count = taxi_data['service_zone'].value_counts()
    st.bar_chart(service_zone_count)

    # plotting Avg Hours Per Day Per Driver each month
    # avg_hours_per_day = taxi_data_1['Avg Minutes Per Trip']
    date = taxi_data_1['Month/Year']
    avg_hours = taxi_data_1["         Avg Hours Per Day Per Driver         "]

with features:
    st.header("The features I created")
    st.markdown("* **first feature:**")
    st.markdown("* **second feature:**")


with model_training:
    st.header("Time to train the model")

    sel_col, disp_col = st.columns(2)

    sel_col.slider('What should be the max_depth of the model',min_value=10,max_value=100,value=20)

    n_estimator = sel_col.selectbox("How many trees should there be?", options=[100,200,300, 'No limit'])

    input_feature = sel_col.selectbox('Which feature should be used?', options=taxi_data_1.columns)

    test = disp_col.write(taxi_data_1[input_feature].sort_values(ascending=False).head(7))
