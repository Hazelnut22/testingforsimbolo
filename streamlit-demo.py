import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number", value=0.0, format="%.2f")
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

result = None
if st.button("Calculate", use_container_width=True):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero!")

    if result is not None:
        st.success(f"Result: {result:.2f}")