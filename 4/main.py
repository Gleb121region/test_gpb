import os
import shutil
from datetime import datetime
from datetime import timedelta


def create_files():
    os.mkdir("f")
    print(f"Create Dir: f")
    mod_time = datetime(1998, 7, 8, 12, 15, 25)
    with open("f/1.txt", "w") as file:
        print(f"Create: {file.name}")
    os.utime("f/1.txt", (mod_time.timestamp(), mod_time.timestamp()))
    with open("2.txt", "w") as file:
        print(f"Create: {file.name}")
    os.utime("2.txt", (mod_time.timestamp(), mod_time.timestamp()))
    os.utime("f", (mod_time.timestamp(), mod_time.timestamp()))


def delete_old_files(folder_path, days):
    now = datetime.now()
    cutoff_date = now - timedelta(days=days)

    for root, dirs, files in os.walk(folder_path):
        for entry in os.listdir(root):
            entry_path = os.path.join(root, entry)

            try:
                modified_time = os.path.getmtime(entry_path)
                modified_date = datetime.fromtimestamp(modified_time)

                if modified_date < cutoff_date:
                    os.remove(entry_path) if os.path.isfile(entry_path) else shutil.rmtree(entry_path)
                    print(f"Deleted: {entry_path}")
            except OSError as e:
                print(f"Error processing: {entry_path} - {e}")


if __name__ == '__main__':
    create_files()
    delete_old_files('/Users/popovgleb/PycharmProjects/pythonProject/4', 30)
