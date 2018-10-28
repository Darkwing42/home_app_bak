from flask import request
from flask_restful import Resource
from todo.models import TodoList, Task
from app import db

class TodoListsApi(Resource):
    def get(self):
        todo = TodoList.query.all()

        return {'todoLists': [t.to_dict() for t in todo] }, 201

    def post(self):
        data = request.get_json()

        task_lst = []
        for task in data['tasks']:
            obj = Task(
                task_name=task['task_name'],
                task_done=task['task_done']
                )
            task_lst.append(obj)

        todoList = TodoList(
            todoList_name=data['todoList_name'],
            todoList_done=data['todoList_done'],
        )
        todoList.tasks = task_lst
        db.session.add(todoList)
        db.session.commit()

        return {'message': 'Successfully saved new data'}, 201




class TodoListApi(Resource):
    def get(self, id):
        pass

    def post(self):
        pass

    def put(self, id):
        pass
