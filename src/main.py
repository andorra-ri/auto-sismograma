#!/usr/bin/python3

import os
import configparser
from datetime import datetime, timedelta
from dotenv import load_dotenv # pylint: disable=import-error

from station import Station, StationNetwork
from seismogram import Seismogram
from save_strategies import SupabaseSaveStrategy

load_dotenv()

config = configparser.ConfigParser()
config.read('config.ini')

SUPABASE_BUCKET = config.get('supabase', 'BUCKET')
COLOR_YESTERDAY = config.get('colors', 'YESTERDAY')
COLOR_TODAY = config.get('colors', 'TODAY')

def main(stations):
    now = datetime.now()
    yesterday = now - timedelta(days=1)

    to_supabase = SupabaseSaveStrategy(
        supabase_id=os.environ['SUPABASE_ID'],
        token=os.environ['SUPABASE_TOKEN'],
        bucket=SUPABASE_BUCKET,
    )

    for station in stations:
        seismogram = Seismogram(station)
        seismogram.create(start_time=yesterday, end_time=now, colors=(COLOR_YESTERDAY, COLOR_TODAY))

        filename = f'{station.name}.{datetime.now().strftime("%Y%m%d")}.png'
        seismogram.save(filename, to_supabase)

        filename = f'{station.name}.latest.png'
        seismogram.save(filename, to_supabase)


if __name__ == '__main__':

    pand = Station(
        name='PAND',
        network=StationNetwork.FR,
        location='00',
        channel='HHZ',
        amplification=80000
    )

    main([pand])
