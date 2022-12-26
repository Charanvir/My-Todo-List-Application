import streamlit as st
import todo_functions

todos = todo_functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    todo_functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo, key=f"{todo}")

new_todo = st.text_input(label="Enter a todo:", placeholder="Todo: ", on_change=add_todo, key="new_todo")

st.session_state
