import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "colorama"],
                     "excludes": ["tkinter"]}

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "Pokus",                  # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]pokus.exe",   # Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     3,                        # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}

icoPath = ""
if (sys.platform == "win32"):
    icoPath = "docs\\res\img\\favicon.ico"
else:
    icoPath = "docs/res/img/favicon.ico"


base = None

setup(  name="Pokus",
        version = "1.3",
        options = {"build_exe": build_exe_options, "bdist_msi": bdist_msi_options},
        executables = [Executable("pokus.py",
        base=base,
        icon=icoPath,
        shortcutName="Pokus",
        shortcutDir="DesktopFolder")])
