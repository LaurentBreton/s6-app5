import os
import csv

def list_files_to_csv(folder_path, output_csv_path):
    
    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                full_path = os.path.join("."+root,filename)
                output_file_name, _ = os.path.splitext(filename)
                output_file_name = os.path.join('./output',output_file_name)
                writer.writerow([full_path, output_file_name + '.png', 480])



if __name__ == '__main__':
    folder_path = './data'
    outptu_csv_file = './data.csv'
    list_files_to_csv(folder_path,outptu_csv_file)
    

