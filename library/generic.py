"""Parser for other report that doesn't need a specific parser."""
from csv import DictReader
from library import crate


def generic_processing(file):
    """Parse the file and add each entry to Crate.

    :type file: str
    """
    generic_dict = []
    with open(file, 'r') as csvfile:
        reader = DictReader(csvfile)
        for line in reader:
            generic_dict.append(line)
    for entry in generic_dict:
        data = {'Timestamp': entry['timestamp'],
                'IP_address': entry['ip'],
                'Port': entry['port'],
                'Tag': entry['tag']}
        k = list(data.keys())
        v = list(data.values())
        crate.insert(k, v)
