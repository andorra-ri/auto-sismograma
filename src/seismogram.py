from typing import Tuple, Any
from datetime import datetime, timedelta

from obspy.clients.fdsn import Client # pylint: disable=import-error
from obspy.core import UTCDateTime # pylint: disable=import-error

from station import Station
from save_strategies import SaveStrategy

class Seismogram:
    TAPER_MAX_PERCENT = 0.05
    WAVE_FILTER_HZ = 2

    client: Client
    station: Station
    plot: Any

    def __init__(self, station: Station):
        self.client = Client("RESIF")
        self.station = station

    def create(
        self,
        start_time: datetime,
        end_time: datetime,
        width: int = 1920,
        height: int = 1080,
        colors: Tuple[str, str] = ('black', 'black'),
        interval: int = 60
    ) -> None:
        channel = self.client.get_waveforms(
            network=self.station.network.value,
            station=self.station.name,
            location=self.station.location,
            channel=self.station.channel,
            starttime=UTCDateTime(start_time),
            endtime=UTCDateTime(end_time),
            attach_response=True
        )
        channel.taper(self.TAPER_MAX_PERCENT)
        channel.filter('highpass', freq=self.WAVE_FILTER_HZ, corners=3)

        start_bound = UTCDateTime(start_time.replace(minute=0, second=0))
        end_bound = UTCDateTime(end_time.replace(minute=0, second=0) + timedelta(hours=1))

        date_format = "%d/%m/%Y %H:%M"

        period = f'De {start_time.strftime(date_format)} a {end_time.strftime(date_format)}'
        high_pass = f"High pass filtered @ {self.WAVE_FILTER_HZ}Hz"
        amplification = f"Amplification: 1/{self.station.amplification}"

        yesterday_colors = [colors[0] for i in range(24 - end_time.hour)]
        today_colors = [colors[1] for i in range(end_time.hour + 1)]

        self.plot = channel.plot(
            type='dayplot',
            size=(width, height),
            title=f'Últimes 24h: {period}  |  {channel[0].id} {high_pass} - {amplification}',
            starttime=start_bound,
            endtime=end_bound,
            title_size=14,
            x_labels_size=12,
            y_labels_size=12,
            one_tick_per_line=True,
            tick_format='%H:%M',
            linewidth=0.3,
            color=tuple(yesterday_colors + today_colors),
            vertical_scaling_range=self.station.amplification,
            interval=interval,
        )

        copy = f"© {datetime.now().year} Andorra Recerca + Innovació. Tots els drets reservats."
        self.plot.text(1, -0.1, copy, ha='right', transform=self.plot.gca().transAxes, fontsize=10)

    def save(self, name: str, save_strategy: SaveStrategy):
        save_strategy.save(name, self.plot)
