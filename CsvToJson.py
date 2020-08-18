from os import getcwd
from csv import DictReader
from json import dumps
from glob import glob

class CsvToJson:

    def __init__(self):
        self.inputKey = ""
        self.run()

    def getKey(self,listOfRows):
        self.inputKey = input("[Choose a Key] : ")
        for row in listOfRows:
            listOfKeys = [key for key in row]

        if self.inputKey not in listOfKeys:
            print('That Key Does not exist in your CSV')
            print(f'[CHOICES] : {listOfKeys}')
            self.getKey(listOfRows)

    def run(self):
        csvPath = getcwd()+'/'
        data = {}
        for csvFileName in glob("*.csv"):
            with open(csvFileName, 'r', encoding='utf8') as csvFile:
                csvReader = DictReader(csvFile)

                listOfRows = [rows for rows in csvReader]
                
                for row in listOfRows:
                    listOfKeys = [key for key in row]

                if "Episode_name" in listOfKeys:
                    self.inputKey = "Episode_name"
                else:
                    self.getKey(listOfRows)

                for rows in listOfRows:
                    data[rows[self.inputKey]] = rows

            jsonName = csvPath+csvFileName.split('.')[0]+'.json'
            with open(jsonName, 'w', encoding='utf8') as jsonFile:
                jsonFile.write(dumps(data,indent=4))
            data.clear()

        print(f'[SUCCESSFULLY CONVERTED ALL \'EM CSV FILES]')
        exit()


if __name__ == "__main__":
    CsvToJson()