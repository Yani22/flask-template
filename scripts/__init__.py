import os
import importlib

# dynamic importing of scripts
def import_scripts():
    for filename in os.listdir('./scripts'):
        if filename.endswith('.py') and filename != "__init__.py": # exclude __init__.py and __pycache__
            importlib.import_module(f'.{filename[:-3]}', package='.scripts') # get module    
