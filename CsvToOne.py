import pickle
from os import getcwd,makedirs
from csv import DictReader, DictWriter
from glob import glob
from pathlib import Path
from datetime import date


class CsvToOne:

    OUTPUT_PATH = getcwd()+'/CsvToOne/'

    def __init__(self):
        if not Path(self.OUTPUT_PATH).exists():
            makedirs(self.OUTPUT_PATH)

        self.run()


    def run(self):
        csvPath = getcwd()+'/'
        COMBINED_ROWS = []
        TODAY = str(date.today())

        # Sort the data and retrieve keys
        for csvFileName in glob("*.csv"):
            with open(csvFileName, 'r', encoding='utf8') as csvFile:
                csvReader = DictReader(csvFile)
                FILE_ROWS = []

                for rows in csvReader:
                    COMBINED_ROWS.append(rows)
                    FILE_ROWS.append(rows)
                
                for row in COMBINED_ROWS:
                    listOfKeys = [key for key in row]

            singlePickelName = self.OUTPUT_PATH+csvFileName.split('.')[0]+'.pickle'

            with open(singlePickelName, 'wb') as handle:
                pickle.dump(FILE_ROWS, handle, protocol=pickle.HIGHEST_PROTOCOL)

        fileName = TODAY+".csv"
        pickelName = TODAY+".pickle"

        with open(self.OUTPUT_PATH+pickelName, 'wb') as handle:
            pickle.dump(COMBINED_ROWS, handle, protocol=pickle.HIGHEST_PROTOCOL)

        # How to read a Pickeled file
        # with open('filename.pickle', 'rb') as handle:
        #     data = pickle.load(handle)
            
        with open(self.OUTPUT_PATH+fileName, "w",encoding="utf8",newline="") as f:
            writer = DictWriter(f, fieldnames=listOfKeys)
            writer.writeheader()
            for row in COMBINED_ROWS:
                writer.writerow(row)


if __name__ == "__main__":
    CsvToOne()