from string import Template


t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')
#print(t)
#output: <string.Template object at 0x10e2cf1d0>
print("OS Path")
import time, os.path
photo_files = ['fashion.jpg', 'fashion2.jpg', 'fashion3.jpg']

class BatchRename(Template):
    delimiter = '%'
fmt = input('Enter rename style ($d-date %n-seqnum %f-format): ')

t = BatchRename(fmt)
date = time.strftime('%d%b%y')

for i, filename in enumerate(photo_files):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} ------>{1}'.format(filename, newname))
    
"""Enter rename style ($d-date %n-seqnum %f-format): Ladies_%n%f
fashion.jpg ------>Ladies_0.jpg
fashion2.jpg ------>Ladies_1.jpg
fashion3.jpg ------>Ladies_2.jpg
"""