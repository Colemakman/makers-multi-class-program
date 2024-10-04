from lib.todo_list import TodoList

def test_format_list():
    todo = TodoList("Clean", "Tidy")
    assert todo.format() == "TODO:\n - Clean\n - Tidy\n"

def test_adding_and_removing():
    todo = TodoList()
    todo.add("Cook")
    todo.add("Shower")
    todo.remove("Cook")
    assert todo.format() == "TODO:\n - Shower\n"

def test_clearing_list():
    todo = TodoList("Clean", "Tidy")
    todo.add("Cook")
    todo.add("Shower")
    todo.clear()
    assert todo.format() == "Nothing todo!"
