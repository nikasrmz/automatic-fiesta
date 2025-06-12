from etl.extractors import CSVExtractor


def main():
    csv_extr = CSVExtractor()
    for row in csv_extr.extract():
        print(row)
    print(csv_extr.extract())

if __name__ == "__main__":
    main()

