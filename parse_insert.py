#!/usr/bin/env python3
# coding: utf-8
"""Parser for report from ShadowServer and insert it in Crate."""

from glob import glob
from multiprocessing import Pool
from library import botnet, dns, freak, generic, ntp, sinkhole_http, snmp


def dispatch(report):
    """Dispatch the report to the right processing.

    :type report: str
    """
    if 'botnet' in report:
        botnet.botnet_processing(report)
    elif 'dns_openresolver' in report:
        dns.dns_openresolver_processing(report)
    elif 'freak' in report:
        freak.freak_processing(report)
    elif 'ntp' in report:
        ntp.ntp_processing(report)
    elif 'sinkhole_http' in report:
        sinkhole_http.sinkhole_http_processing(report)
    elif 'snmp' in report:
        snmp.snmp_processing(report)
    else:
        generic.generic_processing(report)


if __name__ == '__main__':
    reports_list = glob('*.csv')
    with Pool(processes=None) as pool:
        pool.map(dispatch, reports_list)
