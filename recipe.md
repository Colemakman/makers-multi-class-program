## 1. Describe the Problem

- As a user
- So that I can record my experiences
- I want to keep a regular diary

Done

- As a user
- So that I can reflect on my experiences
- I want to read my past diary entries

Done

- As a user
- So that I can reflect on my experiences in my busy day
- I want to select diary entries to read based on how much time I have and my reading speed

Done

- As a user
- So that I can keep track of my tasks
- I want to keep a todo list along with my diary



- As a user
- So that I can keep track of my contacts
- I want to see a list of all of the mobile phone numbers in all my diary entries

Done

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class Diary

class Diary_Entry




```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

