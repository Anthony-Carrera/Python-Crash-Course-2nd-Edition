"""
8-15. Printing Models: Put the functions for the example printing_models.py in a
separate file called printing_functions.py. Write an import statement at the top of
printing_models.py, and modify the file to use the imported functions.
"""

#This is imports the script printing_functions
import printing_functions as pf
#This is a list of desgin
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
#This called the script and it function than prints it out.
pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)