import sys
import termios
import select
from constants import ESC
import time
from enum import Enum

"""
From https://manpages.debian.org/bookworm/manpages-dev/termios.3.en.html

c_lflag flag constants:

ISIG
    When any of the characters INTR, QUIT, SUSP, or DSUSP are received, generate the corresponding signal.
ICANON
    Enable canonical mode (described below).
XCASE
    (not in POSIX; not supported under Linux) If ICANON is also set, terminal is uppercase only. Input is converted to lowercase, except for characters preceded by \. On output, uppercase characters are preceded by \ and lowercase characters are converted to uppercase. [requires _BSD_SOURCE or _SVID_SOURCE or _XOPEN_SOURCE]
ECHO
    Echo input characters.
ECHOE
    If ICANON is also set, the ERASE character erases the preceding input character, and WERASE erases the preceding word.
ECHOK
    If ICANON is also set, the KILL character erases the current line.
ECHONL
    If ICANON is also set, echo the NL character even if ECHO is not set.
ECHOCTL
    (not in POSIX) If ECHO is also set, terminal special characters other than TAB, NL, START, and STOP are echoed as ^X, where X is the character with ASCII code 0x40 greater than the special character. For example, character 0x08 (BS) is echoed as ^H. [requires _BSD_SOURCE or _SVID_SOURCE]
ECHOPRT
    (not in POSIX) If ICANON and ECHO are also set, characters are printed as they are being erased. [requires _BSD_SOURCE or _SVID_SOURCE]
ECHOKE
    (not in POSIX) If ICANON is also set, KILL is echoed by erasing each character on the line, as specified by ECHOE and ECHOPRT. [requires _BSD_SOURCE or _SVID_SOURCE]
DEFECHO
    (not in POSIX) Echo only when a process is reading. (Not implemented on Linux.)
FLUSHO
    not in POSIX; not supported under Linux) Output is being flushed. This flag is toggled by typing the DISCARD character. [requires _BSD_SOURCE or _SVID_SOURCE]
NOFLSH
    Disable flushing the input and output queues when generating signals for the INT, QUIT, and SUSP characters.
TOSTOP
    Send the SIGTTOU signal to the process group of a background process which tries to write to its controlling terminal.
PENDIN
    (not in POSIX; not supported under Linux) All characters in the input queue are reprinted when the next character is read. (bash(1) handles typeahead this way.) [requires _BSD_SOURCE or _SVID_SOURCE]
IEXTEN
    Enable implementation-defined input processing. This flag, as well as ICANON must be enabled for the special characters EOL2, LNEXT, REPRINT, WERASE to be interpreted, and for the IUCLC flag to be effective.

"""

class SnakeKeys(Enum):
    UP_ARROW    = ESC + "A"
    DOWN_ARROW  = ESC + "B"
    RIGHT_ARROW = ESC + "C"
    LEFT_ARROW  = ESC + "D"
    UP          = "w"
    DOWN        = "s"
    RIGHT       = "d"
    LEFT        = "a"

# This class only handles unix like OS
class KeyPoller:
    def __enter__(self):
        self.fd           = sys.stdin.fileno()
        self.old_attrs    = termios.tcgetattr(self.fd)
        self.new_attrs    = termios.tcgetattr(self.fd)

        # new_attrs[3] is the local mode flag in termios so we are controlling
        self.new_attrs[3] &= ~termios.ICANON # Immediate input with every keystroke
        self.new_attrs[3] &= ~termios.ECHO # Don't echo input to self.fd out to console

        termios.tcsetattr(sys.stdin.fileno(),termios.TCSAFLUSH,self.new_attrs)

        return self
    
    def __exit__(self,_type,value,traceback):
        termios.tcsetattr(sys.stdin.fileno(),termios.TCSAFLUSH,self.old_attrs)

    def poll(self):
        dr, dw, de = select.select([sys.stdin.fileno()],[],[],0)
        if dr == []:
            return

        _input = sys.stdin.read(1)
        if _input == "\x1b":
            _input += sys.stdin.read(2)
        
        return _input


if __name__ == "__main__":

    with KeyPoller() as poller:
        while True:
            char = poller.poll()
            match char:
                case SnakeKeys.UP_ARROW.value | SnakeKeys.UP.value:
                    print("UP")
                case SnakeKeys.DOWN_ARROW.value | SnakeKeys.DOWN.value:
                    print("DOWN")
                case SnakeKeys.RIGHT_ARROW.value | SnakeKeys.RIGHT.value:
                    print("RIGHT")
                case SnakeKeys.LEFT_ARROW.value | SnakeKeys.LEFT.value:
                    print("LEFT")
                case "q":
                    break
                case None:
                    pass
                case _:
                    print(char)

            time.sleep(1/60)
