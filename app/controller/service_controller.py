from flask import Blueprint, Flask, Response, request, jsonify
from extensions import app
import json
from app.models.query_builder import mongo, task_db
from app.models.query_builder import ObjectId
from app.models.query_builder import todo_db, test, task_db, update, delete, get_pagination, task_count
from fastapi import FastAPI

api = Blueprint('user', 'user')


@app.route("/todo", methods=["POST"])
def todo():
    a = request.form['name']
    todo_db(a)
    return jsonify(
        {
            a: "task added"
        })


@app.route('/all_task', methods=['GET'])
def all_task():
    response_data = {
        'status': 404,
        'message': 'Something went wrong.'
    }
    response_data['items'] = task_db()
    response_data['status'] = 200
    response_data['message'] = 'ok'
    return jsonify(response_data)


@app.route('/task/<task_id>', methods=['GET'])
def task(task_id):
    response_data = {
        'status': 404,
        'message': 'Something went wrong.'
    }
    response_data['items'] = test(task_id)
    response_data['status'] = 200
    response_data['message'] = 'ok'
    return jsonify(response_data)


@app.route("/todo1/<task_id>", methods=["PUT"])
def todo1(task_id):
    response_data = {
        'status': 404,
        'message': 'Something went wrong.'
    }
    response_data['items'] = update(task_id, name)
    response_data['status'] = 200
    response_data['message'] = 'ok'
    update(task_id, request.form["name"])
    print(request.form["name"])
    return jsonify(response_data)


@app.route("/task1/<task_id>", methods=["DELETE"])
def task1(task_id):
    delete(task_id)
    return "task by id is successfully deleted"


@app.route('/users/<page_no>/<page_size>', methods=['GET'])
def user_pagination(page_size, page_no):
    response_data = {
        'status': 404,
        'message': 'Something went wrong.'
    }
    response_data['items'] = get_pagination(page_size, page_no)
    response_data['pages'] = (
        {
            "page": page_no,
            "next_page": (int(page_no) + 1),
            "prev_page": (int(page_no) - 1),
            "total_count": task_count()
        })
    response_data['status'] = 200
    response_data['message'] = 'ok'
    return jsonify(response_data)
