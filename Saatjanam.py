import streamlit as st
import pandas as pd

# Initialize an empty DataFrame to store profiles
if 'profiles' not in st.session_state:
    st.session_state.profiles = pd.DataFrame(columns=['Name', 'Age', 'Gender', 'Location', 'Occupation'])

def add_profile(name, age, gender, location, occupation):
    new_profile = pd.DataFrame([[name, age, gender, location, occupation]], columns=['Name', 'Age', 'Gender', 'Location', 'Occupation'])
    st.session_state.profiles = pd.concat([st.session_state.profiles, new_profile], ignore_index=True)

def search_profiles(gender, location):
    filtered_profiles = st.session_state.profiles[(st.session_state.profiles['Gender'] == gender) & (st.session_state.profiles['Location'] == location)]
    return filtered_profiles

# Streamlit app
st.title("Matrimonial App")

st.sidebar.header("Create Profile")
name = st.sidebar.text_input("Name")
age = st.sidebar.number_input("Age", min_value=18, max_value=120, step=1)
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
location = st.sidebar.text_input("Location")
occupation = st.sidebar.text_input("Occupation")

if st.sidebar.button("Add Profile"):
    add_profile(name, age, gender, location, occupation)
    st.sidebar.success("Profile added!")

st.sidebar.header("Search Profiles")
search_gender = st.sidebar.selectbox("Search Gender", ["All", "Male", "Female", "Other"])
search_location = st.sidebar.text_input("Search Location")

if st.sidebar.button("Search"):
    if search_gender == "All":
        search_gender = None
    profiles = search_profiles(search_gender, search_location)
    if profiles.empty:
        st.sidebar.write("No profiles found.")
    else:
        st.sidebar.dataframe(profiles)

st.header("All Profiles")
st.dataframe(st.session_state.profiles)
