#!/usr/bin/python3

import configparser
from datetime import datetime, timedelta

from station import Station, StationNetwork
from seismogram import Seismogram
from save_strategies import FileSaveStrategy

config = configparser.ConfigParser()
config.read('config.ini')

COLOR_YESTERDAY = config.get('colors', 'YESTERDAY')
COLOR_TODAY = config.get('colors', 'TODAY')

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

    save_strategy = FileSaveStrategy('./data/')

    seismogram = Seismogram(station)
    seismogram.create(start_time=yesterday, end_time=now, colors=(COLOR_YESTERDAY, COLOR_TODAY))

    filename = f'{station.name}.{datetime.now().strftime("%Y%m%d")}.png'
    seismogram.save(filename, save_strategy)

if __name__ == '__main__':
    main()
