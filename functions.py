def get_todos(filepath):
    """
    Read a text file and return the list of to-do items.
    :param filepath:
    """
    with open(filepath, "r") as file:  # read
        todos = file.readlines()
    return todos

def write_todos(todos, filepath):
    """
    Write the to-do items list in the next file.
    :param todos:
    :param filepath:
    """
    with open(filepath, "w") as file:  # write
        file.writelines(todos)

# def count(phrase):
#     return phrase.count('.')

# print(__name__)

# if __name__ == "__main__":
#     print("hello")