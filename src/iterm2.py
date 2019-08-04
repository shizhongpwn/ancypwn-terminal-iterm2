import os
import osascript


def _apple_script_string_escape(s):
    return repr(s).replace('"', '\\"')


def _iterm_exec(cmd):
    apple_script = '''tell application "iTerm2"
    tell current session of current window
        select split vertically with default profile
        write text "{}"
    end tell
end tell
'''.format(_apple_script_string_escape(cmd))
    osascript.run(apple_script)


def run(command):
    _iterm_exec(command)
