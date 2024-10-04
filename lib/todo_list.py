class TodoList:
    
    def __init__(self, *args):
        self.todo = list(args)
    
    def add(self, goal):
        self.todo.append(goal)

    def remove(self, goal):
        self.todo.remove(goal)

    def format(self):
        result = "TODO:\n"

        if len(self.todo) == 0:
            return "Nothing todo!"
        for do in self.todo:
            result += f" - {do}\n"

        return result

    def clear(self):
        self.todo = []
