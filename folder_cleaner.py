import os

files = os.listdir()
os.mkdir("Documents")

for file in files:
    if file.endswith(".txt"):
        print("Text file found:", file)
        