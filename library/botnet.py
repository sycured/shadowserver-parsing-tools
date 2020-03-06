"""Specific parser for botnet report."""
from csv import DictReader
from library import crate


def botnet_processing(file):
    """Parse the file and add each entry to Crate.

    :type file: str
    """
    botnet_dict = []
    with open(file, 'r') as csvfile:
        reader = DictReader(csvfile)
        for line in reader:
            botnet_dict.append(line)
    for entry in botnet_dict:
        data = {'Timestamp': entry['timestamp'],
                'IP_address': entry['ip'],
                'Port': entry['port'],
                'Tag': 'botnet'}
        k = list(data.keys())
        v = list(data.values())
        crate.insert(k, v)
