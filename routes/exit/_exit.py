import sys
sys.path.append("../../")
from input_emitter import Input
from state import STATE


def handle_exit(event):
    STATE.exit_application()


Input.listen("exit", handle_exit)