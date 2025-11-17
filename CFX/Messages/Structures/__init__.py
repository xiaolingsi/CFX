"""
CFX Structures Package

This package contains all structure classes used in CFX messages.
You can import all structures at once using:
    from CFX.Messages.Structures import *

Or import specific structures:
    from CFX.Messages.Structures import Fault, ResourceState, Stage, etc.
"""

import os
import importlib
import pkgutil

# Import all structure classes from subdirectories
from . import Cleaning
from . import SolderApplication
from . import SolderReflow
from . import SolderPastePrinting

# Define __all__ for explicit exports
__all__ = [
    'Cleaning',
    'SolderApplication',
    'SolderReflow',
    'SolderPastePrinting'
]

# Dynamically import all modules in this directory
def _import_modules():
    current_dir = os.path.dirname(__file__)
    
    # Get all Python files in the current directory
    for module_info in pkgutil.iter_modules([current_dir]):
        module_name = module_info.name
        
        # Skip __init__ and private modules
        if module_name.startswith('_') or module_name == '__init__':
            continue
            
        try:
            # Import the module
            module = importlib.import_module(f'.{module_name}', package=__name__)
            
            # Add all classes from the module to globals() and __all__
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                
                # Only add classes (not modules, functions, etc.)
                if isinstance(attr, type) and not attr_name.startswith('_'):
                    globals()[attr_name] = attr
                    __all__.append(attr_name)
        except (ImportError, AttributeError) as e:
            # Skip modules that can't be imported
            pass

# Import all modules
_import_modules()