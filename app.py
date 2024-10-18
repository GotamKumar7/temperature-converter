import streamlit as st

# Conversion functions
def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0 / 9.0

def celsius_to_fahrenheit(c):
    return (c * 9.0 / 5.0) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return fahrenheit_to_celsius(f) + 273.15

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

# App title and description
st.title("🌡️ VIP Temperature Converter")
st.markdown(
    """
    Welcome to the **VIP Temperature Converter**! 🌟 
    Easily convert between different temperature units with a sleek and professional interface.
    """
)

# Temperature unit options
units = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]
conversion_from = st.selectbox("Convert from:", units)
conversion_to = st.selectbox("Convert to:", units)

# Temperature input with slider
temp_input = st.slider("Select the temperature to convert:", min_value=-100.0, max_value=500.0, step=0.5)

# Convert temperature based on user input
if st.button("Convert"):
    if conversion_from == conversion_to:
        st.warning("The units are the same. Please choose different units to convert.")
    else:
        if conversion_from == "Celsius (°C)" and conversion_to == "Fahrenheit (°F)":
            result = celsius_to_fahrenheit(temp_input)
            st.success(f"{temp_input}°C is equal to {result:.2f}°F")
        elif conversion_from == "Celsius (°C)" and conversion_to == "Kelvin (K)":
            result = celsius_to_kelvin(temp_input)
            st.success(f"{temp_input}°C is equal to {result:.2f}K")
        elif conversion_from == "Fahrenheit (°F)" and conversion_to == "Celsius (°C)":
            result = fahrenheit_to_celsius(temp_input)
            st.success(f"{temp_input}°F is equal to {result:.2f}°C")
        elif conversion_from == "Fahrenheit (°F)" and conversion_to == "Kelvin (K)":
            result = fahrenheit_to_kelvin(temp_input)
            st.success(f"{temp_input}°F is equal to {result:.2f}K")
        elif conversion_from == "Kelvin (K)" and conversion_to == "Celsius (°C)":
            result = kelvin_to_celsius(temp_input)
            st.success(f"{temp_input}K is equal to {result:.2f}°C")
        elif conversion_from == "Kelvin (K)" and conversion_to == "Fahrenheit (°F)":
            result = kelvin_to_fahrenheit(temp_input)
            st.success(f"{temp_input}K is equal to {result:.2f}°F")

# Adding a footer for style
st.markdown(
    """
    ---
    **VIP Converter** | Built with ❤️ using Streamlit
    """
)
