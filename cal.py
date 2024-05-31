import streamlit as st

# Function to perform calculation based on user input
def calculate(num1, num2, operation):
    if operation == 'Addition':
        return num1 + num2
    elif operation == 'Subtraction':
        return num1 - num2
    elif operation == 'Multiplication':
        return num1 * num2
    elif operation == 'Division':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"


st.title('MUHAMMAD AYAAN')

num1 = st.number_input('Enter the first number:')
num2 = st.number_input('Enter the second number:')
operation = st.selectbox('Select operation:', ['Addition', 'Subtraction', 'Multiplication', 'Division'])


if st.button('Calculate'):
    result = calculate(num1, num2, operation)
    st.write('Result:', result)
