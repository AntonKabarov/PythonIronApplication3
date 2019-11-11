#import sys
from cx_Freeze import setup,Executable
#build_exe_options={"package":["os"],"excludes":["tkinter"]}
#executables=[Executable('WindowsApplication2.py')]
#base=None
#if sys.platform=="win32":
#    base="Win32GUI"

exe = Executable(script="WindowsApplication2.py",base="Win32GUI")
setup(name='WindowsApplication2',
       version='0.0.1',
       description='WindowsApplication',
#      options={'build_exe':build_exe_options},
      executables=[exe]
      )  