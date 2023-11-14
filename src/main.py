#!/usr/bin/python3

from datetime import datetime, timedelta

from station import Station, StationNetwork
from seismogram import Seismogram

COLOR_YESTERDAY = '#cccccc'
COLOR_TODAY = '#dd3344'

def main():
    now = datetime.now()
    yesterday = now - timedelta(days=1)

    station = Station(
        name='PAND',
        network=StationNetwork.FR,
        location='00',
        channel='HHZ',
        amplification=80000
    )

    seismogram = Seismogram(station)
    seismogram.create(start_time=yesterday, end_time=now, colors=(COLOR_YESTERDAY, COLOR_TODAY))

if __name__ == '__main__':
    main()
