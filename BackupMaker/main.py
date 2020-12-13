import os
import zipfile


def backup_to_zip(folder):
    folder = os.path.abspath(folder)
    counter = 1

    while True:
        zip_filename = os.path.basename(folder) + "_" + str(counter) + ".zip"
        if not os.path.exists(zip_filename):
            break
        counter += 1

    print("Creating %s..." % (zip_filename))
    backup_zip = zipfile.ZipFile(zip_filename, "w")

    for foldername, subfolders, filenames in os.walk(folder):
        print("Adding files in %s..." % (foldername))
        backup_zip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + "_"
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue
            backup_zip.write(os.path.join(foldername, filename))
    backup_zip.close()
    print("Done.")

# backup_to_zip("C:\\Users\\Romi\\Desktop\\testzip")
