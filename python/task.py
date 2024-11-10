from flask import Flask, request, jsonify

TaskManagementSystem = Flask(__name__)

Tasks = [
        {
          "id": 1,
          "title": "Buy groceries",
          "description": "Milk, Cheese, Pizza, Fruit",
          "done": False
        },
        {
          "id": 2,
          "title": "Learn Python",
          "description": "Need to find a good Python tutorial on the web",
          "done": False
        }
      ]

#Scope
max_id = max(task['id'] for task in Tasks) if Tasks else 0

@TaskManagementSystem.route('/tasks')
def TaskManagementSystemoperation():
    return (Tasks)

@TaskManagementSystem.route('/tasks/<taskID>', methods=['GET'])
def TaskManagementSystemSearch(taskID):
    for Task in Tasks:        
        if (Task['id']) == int(taskID):
            return jsonify(Task)
    return jsonify({"Error":404})

@TaskManagementSystem.route('/tasks/', methods=['POST'])
def TaskManagementSystemCreate():
    global max_id
    Task = request.json
    # max_id = max(task['id'] for task in Tasks) if Tasks else 0
    Task['id'] = max_id + 1
    Tasks.append(Task)
    return jsonify(Tasks)

@TaskManagementSystem.route('/tasks/<task_id>', methods=['PUT'])
def TaskManagementSystemUpdate(task_id):
    Task = request.json
    for data in Tasks:
        if data["id"] == int(task_id):
            data["title"] = Task["title"],
            data["description"] = Task["description"],
            data["done"] = Task["done"],
            return jsonify(Tasks)
    return jsonify({"Error":404})

if __name__ == '__main__':
    TaskManagementSystem.run(debug=True)