from Orange.widgets import gui
from Orange.widgets.settings import Setting
from scipy import signal

from ..base_widget import FilterWidget


class Resample_NUDFT(FilterWidget):
    name = "Resample NUDFT"
    description = "Resample Non-Uniform Discrete Fourier Transform"
    icon = "icons/spectra.svg"

    xmin = Setting(0)
    xmax = Setting(4000)
    nbins = Setting(100)
    window_function = Setting('blackmanharris')

    def __init__(self):
        super().__init__()
        box = gui.widgetBox(self.controlArea, self.name)
        gui.spin(box, self, 'xmin', -1000, 10000, callback=self.auto_process, label='x-min')
        gui.spin(box, self, 'xmax', -1000, 10000, callback=self.auto_process, label='x-max')
        gui.spin(box, self, 'nbins', 1, 10000, callback=self.auto_process, label='n-bins')
        gui.comboBox(box, self, 'window_function', label='window', sendSelectedValue=True,
                     items=['barthann',
                            'bartlett',
                            'blackman',
                            'blackmanharris',
                            'bohman',
                            'boxcar',
                            'hamming',
                            'hann',
                            'nuttall',
                            'parzen',
                            'triang',
                            ], callback=self.auto_process)

    def process(self, spe):
        self.out_spe = list()
        for spe in self.in_spe:
            self.out_spe.append(
                spe.resample_NUDFT_filter(x_range=(self.xmin, self.xmax), xnew_bins=self.nbins,
                                          window=getattr(signal.windows, self.window_function))
                )
        self.send_outputs()
