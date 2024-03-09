import os
from flask import Flask, render_template, request, session, redirect, url_for
from recipemanager import app

if __name__ == '__main__':
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'True').lower() == 'true'
    app.run(host=host, port=port, debug=debug)