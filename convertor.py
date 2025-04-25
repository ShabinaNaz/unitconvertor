import streamlit as st
st.markdown(

"""
<style>
body{
 bakground-color: #000000;
 color:blue;
}
.stApp{   
backfround: liner-gradient(135deg, #bcbcbc, #cfe2f3);
padding: 30px;
border-radius: 15px;
box-shadow: 0px 10px 30px rgba(0,0,0,0.3);

}
h1 {
   text-align: center;
   font-size: 36px;
    color: white;

}
.stButton>button{
background: liner-gradient(45deg, #0b5394, #351c75);
color: white;
font-size: 10px 20px;
border-radient: 10px;
transition: 0.3s;
box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
}
.stButton>button:hover{
transform: scale(1.05);
background: liner-gradient(45deg, #92fe9d, #000c9ff);
color: black
}
.result{
font-size: 24px
font-weight: bold;
text-align: center;
background: green;
padding: 25px;
border-radius: 10px;
margin-top: 20px;
box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3
}
.footer{
text-align: center;
margin-top: 50px;
font-size: 14px;
color: black;
}


</style>
""",
unsafe_llow_tml=True
)
st.markdown("<h1> unit converter using python and streamlit </h1>", unsafe_allow_html=True)
st.write("Easily convert units between different units of lenght, weight, and temprature.")


conversion_type= st.sidebar.selectbox("choose conversion type", ["lenght", "weight", "temperature"])
value =st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)
if conversion_type == "Lenght":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilograms", "centimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilograms", "centimeters", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celies", "Fahrenheit", "Kelvin"])
        with col2:
            to_unit = st.selectbox("To",  ["Celies", "Fahrenheit", "Kelvin"])




        #Converted function
        def length_convertor(value, from_unit, to_unit):
            lenght_units = {
                'Meters': 1, 'Kilometers': 0.001, 'Centemeters': 100, 'Milimeters': 1000,
                'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28, 'Inches': 39.37
            }
            return (value / lenght_units[from_unit] * lenght_units[to_unit])
        def weight_convertor(value, from_unit, to_unit):
            weight_units = {
                'Kilograms': 1, 'Grams': 1000, 'Pounds': 2.20462, 'Ounces': 35.274
            }
            return (value / weight_units[from_unit]) * weight_units[to_unit]
        def temperature_convertor(value, from_unit, to_unit):
            if from_unit == "Celsius":
                return (value * 9/5 +32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
            elif from_unit == "Fahrenheit":
                return (value -32) * 5/9 if to_unit == "Celsius" else (value -32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
            elif from_unit == "Kelvin":
                return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
            return value

            #button for conversion

    if st.button ("▶️Convert"):
     if conversion_type == "Lenght":
                    result = length_convertor(valu, from_unit, to_unit)
    elif conversion_type == "weight":
                        result = weight_convertor(value)
    elif conversion_type == "temperature":
        result = temperature_convertor(value, from_unit, to_unit)

        st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
st.markdown("<div class= 'footer>Created by Shabina Naz</div>", unsafe_allow_html=True)

                    
