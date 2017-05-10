from octoprint_grbl_plugin.plugin import unsupported_commands, translate_ok

__plugin_name__ = 'Grbl support'
__plugin_hooks__ = {
    'octoprint.comm.protocol.gcode.sending': unsupported_commands,
    'octoprint.comm.protocol.gcode.received': translate_ok,
}
