import csv
import random
from sklearn.model_selection import train_test_split

import os

def load_data(file_name):

    if os.path.exists(file_name):
            with open(file_name, 'r', encoding="utf8") as csvfile:
                csv_reader_object = csv.reader(csvfile, delimiter=',')
                counter = 0
                csv_list = []
                for row in csv_reader_object:
                    #print(row)
                    if counter == 0:
                        pass
                    else:
                        csv_list.append(row+[file_name[7:11]])
                    counter += 1
            
            print(counter-1,"Einträge aus", file_name[7:], "geladen")
            return csv_list        
    else:
        print("Datei", file_name ,"nicht gefunden") 

def main():
    file_folder = "./data/"
    files = ["Fake.csv","True.csv"]

    main_data = []

    for element in files:
        file_name = file_folder+element
        main_data += (load_data(file_name))

    print("Es gibt insgesamt", len(main_data), "Einträge")

    random.shuffle(main_data)
    train_data,test_data = train_test_split(main_data,test_size=0.2) 

    print("Länge train_data:", len(train_data)," und Länge test_data:", len(test_data))
    #print(train_data[0][3])

    return train_data,test_data