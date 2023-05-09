
import os

def delete_files():
    dextension = [".aux",".bbl",".lof",".log",".lot",".out",".toc"]

    files = os.listdir()
    dfiles= []

    for file in files:
        if file[len(file)-4:] in dextension:
            dfiles.append(file)

    for file in dfiles:
        os.remove(file)

    print("Files with the extensions {} are successfully deleted.".format(dextension))

delete_files()