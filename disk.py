import psutil   
import shutil

total, used, free = shutil.disk_usage('/')

print ("%d GB" % (free // (2**30)))   