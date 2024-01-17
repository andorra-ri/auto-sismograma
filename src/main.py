#!/usr/bin/python3

import os
from datetime import datetime, timedelta
from dotenv import load_dotenv # pylint: disable=import-error
import toml # pylint: disable=import-error

from station import Station
from seismogram import Seismogram
from save_strategies import SupabaseSaveStrategy

load_dotenv()

def main():
    config = toml.load('config.toml')

    now = datetime.now()
    yesterday = now - timedelta(days=1)

    colors = (config['colors']['YESTERDAY'], config['colors']['TODAY'])

    to_supabase = SupabaseSaveStrategy(
        supabase_id=os.environ['SUPABASE_ID'],
        token=os.environ['SUPABASE_TOKEN'],
        bucket=config['supabase']['BUCKET'],
    )

    for options in config['stations'].values():
        station = Station.from_dict(options)

        seismogram = Seismogram(station)
        seismogram.create(start_time=yesterday, end_time=now, colors=colors)

        filename = f'{station.name}.latest.png'
        seismogram.save(filename, to_supabase)

    print(f"Created seismograms at {now.strftime('%d/%m/%Y %H:%M')}")


if __name__ == '__main__':
    main()
