from app import db
from datetime import datetime

class Task(db.Model):

    __tablename__ = 'tasks'

    taskID = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(200))
    todoList_id = db.Column(db.Integer, db.ForeignKey('todoLists.todoListID'), nullable=False)
    task_done = db.Column(db.Boolean, default=False)

    def __init__(self, task_name, task_done):
        self.task_done = task_done
        self.task_name = task_name

    def to_dict(self):
        return dict(
            taskID=self.taskID,
            task_name=self.task_name,
            todoList_id=self.todoList_id,
            task_done=self.task_done
        )

class TodoList(db.Model):
    __tablename__ = 'todoLists'

    todoListID = db.Column(db.Integer, primary_key=True)
    todoList_name = db.Column(db.String(200))
    todoList_done = db.Column(db.Boolean, default=False)
    tasks = db.relationship('Task', backref='todoList', lazy=False)

    def __init__(self,todoList_name, todoList_done):
        self.todoList_name = todoList_name
        self.todoList_done = todoList_done

    def to_dict(self):
        return dict(
            todoListID=self.todoListID,
            todoList_name=self.todoList_name,
            todoList_done=self.todoList_done,
            tasks=[ task.to_dict() for task in self.tasks ]
        )
