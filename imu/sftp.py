from subprocess import check_output
import shutil
import time
import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
inPath="/home/pi/upload"
outPath="/home/pi/reUpload/RPiIMU"

if len(os.listdir(inPath)) != 0:
        for filename in os.listdir(inPath):
            print("Moviendo "+filename)
            shutil.move(inPath+"/"+filename, outPath+"/"+filename)

def on_created(event):
    print("\nArchivo nuevo: "+os.path.basename(event.src_path))
    try:
        info=check_output(["/bin/bash","/home/pi/sftp.sh",event.src_path])
        print(info)
        os.remove(event.src_path)
        print("Subido")
    except Exception as e:
        print("Error subiendo archivo "+event.src_path+"\n")
        shutil.move(event.src_path,outPath+"/"+os.path.basename(event.src_path))

# Watchdog de archivos nuevos
if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(
        patterns, ignore_patterns, ignore_directories, case_sensitive)


my_event_handler.on_created = on_created
path = inPath
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
