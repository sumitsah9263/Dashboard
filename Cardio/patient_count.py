import os
import pickle

def patient_count():
    files = folders = 0
    dirs = []

    filename = "count_data.pkl"

    if os.path.isfile(filename):
        with open(filename,'rb') as file:
            dirs_dict = pickle.load(file)
    else:
        dirs_dict = {}

    path = "/home/pi/Downloads/larkai/patient_Data" #path for patient_data folder

    for _, dirnames, _ in os.walk(path):
        folders += len(dirnames)
        dirs += dirnames

    for i in dirs:
        if i in dirs_dict:
            dirs_dict[i] += 1
        else:
            dirs_dict[i] = 1


    with open(filename,'wb') as file:
        pickle.dump(dirs_dict, file)
        file.close()

    print(folders,"folders")
    
patient_count()
