import sys
sys.path.append("../../")
from input_emitter import Input

def handle_help(event):
    print("print help section here-------")

Input.listen("help", handle_help)