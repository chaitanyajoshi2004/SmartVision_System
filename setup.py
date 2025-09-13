import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Program Files\Python311\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Program Files\Python311\tcl\tk8.6"

executables = [cx_Freeze.Executable("login.py", base=base, icon="hack.ico")]


cx_Freeze.setup(
    name = "Facial Recognition Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["hack.ico",'tcl86t.dll','tk86t.dll', 'Images','fphotos','database','attendance_report']}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace System | Developed By Chaitanya Joshi",
    executables = executables
    )
