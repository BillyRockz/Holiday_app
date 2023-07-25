from flask import Flask, request

app = Flask(__name__)

from app.apis import endpoints
from app.apis import databases
from . import apis