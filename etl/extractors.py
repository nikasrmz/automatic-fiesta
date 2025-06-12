from base import BaseExtractor
from csv import DictReader

class CSVExtractor(BaseExtractor):



    def extract(self):
        with open("dummy_data.csv") as f:
            reader = DictReader(f)
            for row in reader:
                yield row







