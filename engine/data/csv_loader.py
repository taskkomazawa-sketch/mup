import csv


def load_csv(file):
    return list(csv.DictReader(file))