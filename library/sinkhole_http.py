"""Specific parser for sinkhole http report."""
from csv import DictReader
from library import crate


def sinkhole_http_processing(file):
    """Parse the file and add each entry to Crate.

    :type file: str
    """
    sinkhole_http_dict = []
    with open(file, 'r') as csvfile:
        reader = DictReader(csvfile)
        for line in reader:
            sinkhole_http_dict.append(line)
    for entry in sinkhole_http_dict:
        data = {'Timestamp': entry['timestamp'],
                'IP_address': entry['ip'],
                'Tag': 'Sinkhole HTTP'}
        k = list(data.keys())
        v = list(data.values())
        crate.insert(k, v)
