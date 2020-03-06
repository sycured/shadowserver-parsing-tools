"""Specific parser for snmp report."""
from csv import DictReader
from library import crate


def snmp_processing(file):
    """Parse the file and add each entry to Crate.

    :type file: str
    """
    snmp_dict = []
    with open(file, 'r') as csvfile:
        reader = DictReader(csvfile)
        for line in reader:
            snmp_dict.append(line)
    for entry in snmp_dict:
        data = {'Timestamp': entry['timestamp'],
                'IP_address': entry['ip'],
                'Port': entry['port'],
                'Tag': 'SNMP'}
        k = list(data.keys())
        v = list(data.values())
        crate.insert(k, v)
