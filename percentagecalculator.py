import streamlit as st

# Streamlit app
st.title("Student Percentage Calculator")

# Input for total marks and obtained marks
total_marks = st.number_input("Enter the total marks:", min_value=1, step=1)
obtained_marks = st.number_input("Enter the obtained marks:", min_value=0, step=1)

# Calculate percentage
if total_marks > 0:
    percentage = (obtained_marks / total_marks) * 100
    st.write(f"Percentage: {percentage:.2f}%")
else:
    st.write("Total marks must be greater than zero.")

# Additional Info
st.markdown("""
### How to Use:
1. Enter the total marks for the exam in the first input field.
2. Enter the marks obtained by the student in the second input field.
3. The app will automatically calculate and display the percentage based on the inputs.
""")
