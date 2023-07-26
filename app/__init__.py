from flask import Flask, request

app = Flask(__name__)

from app.models import endpoints
from app.models import databases