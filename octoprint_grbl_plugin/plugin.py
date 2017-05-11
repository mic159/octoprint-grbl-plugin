import re
import logging

log = logging.getLogger(__name__)

def unsupported_commands(comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
    """
    Suppress certain commands, because Grbl cant handle them.
    """
    if cmd.startswith('M110 '):
        # Reset line numbers not supported in Grbl
        return None,
    if cmd == 'M105':
        # Translate temperature for "gcode parameters" and "Realtime data"
        return '?$G'
    if cmd == 'M400':
        # Finishes all current moves and and thus clears the buffer.
        # That's identical to G4 P0.
        return 'G4 P0'
    if cmd == 'M114':
        # Get current position
        return '?'


def translate_ok(comm_instance, line, *args, **kwargs):
    """
    This plugin moves Grbl's ok from the end to the start.
    OctoPrint needs the 'ok' to be at the start of the line.
    """
    if 'MPos' in line:
        # <Idle,MPos:0.000,0.000,0.000,WPos:0.000,0.000,0.000,RX:3,0/0>
        match = re.search(r'MPos:([\d\.]+),([\d\.]+),([\d\.]+)', line)
        # OctoPrint records positions in some instances.
        # It needs a different format. Put both on the same line so the GRBL info is not lost
        # and is accessible for "controls" to read.
        return 'ok X:{0} Y:{1} Z:{2} {original}'.format(
            *match.groups(),
            original=line
        )

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
