import subprocess
from Line_Break import line_break

def Reminders():
    print('DON\'T FORGET THE FOLLOWING:')
    subprocess.run(['sudo', 'qtcreator'])
    print('Select Tools>Options>Verify that Path shows QT5+.')
    line_break()