from os import system
from wsgiref.types import WSGIApplication
from waitress import serve
import wsgi
serve(wsgi, listen='*:8080')