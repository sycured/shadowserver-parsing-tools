"""Specific parser for ssl freak report."""
from csv import DictReader
from library import crate


def freak_processing(file):
    """Parse the file and add each entry to Crate.

    :type file: str
    """
    freak_dict = []
    with open(file, 'r') as csvfile:
        reader = DictReader(csvfile)
        for line in reader:
            freak_dict.append(line)
    for entry in freak_dict:
        data = {'Timestamp': entry['timestamp'],
                'IP_address': entry['ip'],
                'Port': entry['port'],
                'Tag': entry['tag'],
                'Cipher_Suite': entry['cipher_suite']}
        k = list(data.keys())
        v = list(data.values())
        crate.insert(k, v)
