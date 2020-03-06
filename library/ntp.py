"""Specific parser for ntp report."""
from csv import DictReader
from library import crate


def ntp_processing(file):
    """Parse the file and add each entry to Crate.

    :type file: str
    """
    ntp_dict = []
    with open(file, 'r') as csvfile:
        reader = DictReader(csvfile)
        for line in reader:
            ntp_dict.append(line)
    for entry in ntp_dict:
        data = {'Timestamp': entry['timestamp'],
                'IP_address': entry['ip'],
                'Port': entry['port'],
                'Tag': 'ntp'}
        k = list(data.keys())
        v = list(data.values())
        crate.insert(k, v)
