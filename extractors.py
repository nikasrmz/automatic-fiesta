from base import BaseExtractor

class CSVExtractor(BaseExtractor):

    def extract(self):
        with open("dummy_data") as f:
            print