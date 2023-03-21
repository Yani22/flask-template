from app import app
import os
import importlib

# NOTE: This will only work if module name and blueprint name is the same
def register_blueprints():
    for filename in os.listdir('./routes'):
        if filename.endswith('.py') and filename != "__init__.py": # exclude __init__.py and __pycache__
            route = filename[:-3] # url prefix
            module = importlib.import_module(f'.{route}', package='.routes') # get module
            blueprint = getattr(module, route) # get blueprint
            app.register_blueprint(blueprint, url_prefix=f'/{route}') # dynamic blueprint registration 
    
    