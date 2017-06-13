import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"build_exe":"../dist", "include_files": ["assets/music/theme.wav", 'assets/text/credit.png',
                 'assets/text/creditsarrow.png','assets/text/exitarrow.png',
                 'assets/text/instructionarrow.png', 'assets/text/playarrow.png',
                 'assets/text/presskey.png', 'assets/bario.png', 'assets/barioflip.png',
                 'assets/barioflipwalk1.png', 'assets/barioflipwalk2.png',
                 'assets/bariowalk1.png', 'assets/bariowalk2.png',
                 'assets/boomba.png', 'assets/bricktemplate.png', 'assets/charactersel.png',
                 'assets/instruction1.png', 'assets/instruction2.png', 'assets/instruction3.png',
                 'assets/loseScreen.png', 'assets/mainmenu.png',
                 'assets/pause.png', 'assets/winScreen.png', 'assets/text/nohighscore.png']}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable('amazing_bario_cousins.py', base=base)
]

setup(  name='AmazingBarioCousins',
        version='1.0.0',
        description='An homage to the classic video game Super Mario Brothers.',
        options = {"build_exe": build_exe_options},
        executables = executables)
