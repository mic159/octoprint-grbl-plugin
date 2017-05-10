import logging

log = logging.getLogger(__name__)

def unsupported_commands(comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
    """
    Suppress certain commands, because Grbl cant handle them.
    
    M110 (reset line number)
    M105 (get temperature)
    """
    if cmd.startswith('M110 '):
        return None,
    if cmd.startswith('M105'):
        # Translate temperature for "gcode parameters" and "Realtime data"
        return '?$G'


def translate_ok(comm_instance, line, *args, **kwargs):
    """
    This plugin moves Grbl's ok from the end to the start.
    OctoPrint needs the 'ok' to be at the start of the line.
    """
    if not line.rstrip().endswith('ok'):
        return line

    if line.startswith('{'):
        # Regular ACKs
        # {0/0}ok
        # {5/16}ok
        return 'ok'

    elif '{' in line:
        # Ack with return data
        # F300S1000{0/0}ok
        before, _, _ = line.partition('{')
        return 'ok ' + before
    else:
        return 'ok'
