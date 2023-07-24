from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

from app import app

if __name__ == "__main__":
    app.run(debug=True)

