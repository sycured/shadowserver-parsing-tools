"""Specific parser for botnet report."""
from csv import DictReader
from library import crate


def dns_openresolver_processing(file):
    """Parse the file and add each entry to Crate.

    :type file: str
    """
    dns_openresolver_dict = []
    with open(file, 'r') as csvfile:
        reader = DictReader(csvfile)
        for line in reader:
            dns_openresolver_dict.append(line)
    for entry in dns_openresolver_dict:
        data = {'Timestamp': entry['timestamp'],
                'IP_address': entry['ip'],
                'Port': entry['port'],
                'Tag': 'dns - openresolver',
                'Min_Amplification': entry['min_amplification']}
        k = list(data.keys())
        v = list(data.values())
        crate.insert(k, v)
