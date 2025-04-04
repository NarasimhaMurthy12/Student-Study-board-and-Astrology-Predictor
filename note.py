import subprocess as sp
def no():
    programName = "notepad.exe"
    fileName = "file.txt"
    sp.Popen([programName, fileName])

