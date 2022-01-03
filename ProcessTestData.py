# Routine to set up test data to match the training data structure
from io import StringIO
import shutil, os
import random
import pandas as pd

rows = pd.read_csv(r"C:/Users/andremcq/ML/Data/Test.csv")

for i, row in rows.iterrows():
    img_class = row["ClassId"]
    img_path = row["Path"]
    img_file = img_path.split("/")[1]
    image = r"C:/Users/andremcq/ML/Data/" + img_path
    new_subpath = "C:/Users/andremcq/ML/Data/Test/"
    isExist = os.path.exists(new_subpath + str(img_class))
    if isExist == False:
        os.mkdir(new_subpath + str(img_class))
    new_path = new_subpath + str(img_class) + "/" + img_file
    print(new_path)
    shutil.copy(image, new_path)

