import streamlit as st
import functions

todos = functions.get_todos("todos.txt")

def add_todos():
    todo = st.session_state["new_todo"]
    todos.append(todo+"\n")
    functions.write_todos(todos,"todos.txt")
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your prokuctivity")


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{index}-checkbox")
    if checkbox == True:
        todos.pop(index)
        functions.write_todos(todos, "todos.txt")
        del st.session_state[f"{index}-checkbox"]
        st.rerun()


st.session_state

st.text_input(label="",placeholder="Add new todo...",
              on_change=add_todos, key='new_todo')



