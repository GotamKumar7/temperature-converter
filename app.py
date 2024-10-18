import streamlit as st

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0 / 9.0

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9.0 / 5.0) + 32

# Streamlit App
st.title("Temperature Converter")

# Select conversion option
option = st.radio(
    "Select the conversion direction:",
    ("Fahrenheit to Celsius", "Celsius to Fahrenheit")
)

# Input field for temperature
temp = st.number_input("Enter the temperature:", step=1.0, format="%.1f")

# Perform conversion based on user selection
if option == "Fahrenheit to Celsius":
    result = fahrenheit_to_celsius(temp)
    st.write(f"{temp}°F is equal to {result:.2f}°C")
else:
    result = celsius_to_fahrenheit(temp)
    st.write(f"{temp}°C is equal to {result:.2f}°F")

