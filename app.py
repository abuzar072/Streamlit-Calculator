import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮")

st.title("🧮 Simple Calculator App")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

operation = st.selectbox(
    "Select operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"]
)

# Perform calculation
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
    elif operation == "Subtraction (-)":
        result = num1 - num2
    elif operation == "Multiplication (×)":
        result = num1 * num2
    elif operation == "Division (÷)":
        if num2 == 0:
            st.error("❌ Cannot divide by zero!")
            result = None
        else:
            result = num1 / num2

    if result is not None:
        st.success(f"### ✅ Result: `{result}`")
