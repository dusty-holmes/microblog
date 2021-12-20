from flask import Flask
from config import Config
import logging

app = Flask(__name__)
app.config.from_object(Config)
app.logger.setLevel(logging.INFO)

from app import routes