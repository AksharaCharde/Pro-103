import sys
import time
import random
import os
import shutil

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

#Adding the path 
from_dir = "C:/Users/Info/Desktop"

#Creating a folder to move all the files
to_dir = "C:/Users/Info/Desktop/Pro_103_Moving_Files"

#Event Handler Class
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.scr_path} has been created")

    def on_deleted(self, event):
        print(f"Opps! Someone deleted {event.scr_path}!")

    def on_modified(self, event):
        print(f"Your {event.scr_path} file is modified.")

    def on_moved(self, event):
        print(f"Your {event.scr_path} file has been successfully moved.")

#Initialize Event Hander Class
event_handler = FileSystemEventHandler()

#Initialize Observer
observer = Observer()

#Schedule the Observer
observer.schedule(event_handler, from_dir, recursive = True)

#Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("Running......")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()