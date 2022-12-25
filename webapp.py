import streamlit as st
import todo_functions

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

todos = todo_functions.get_todos()
for todo in todos:
    st.checkbox(todo)

new_todo = st.text_input(label="Enter a todo:", placeholder="Todo: ")
print(new_todo)
