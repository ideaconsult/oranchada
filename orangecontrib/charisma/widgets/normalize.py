from Orange.widgets import gui
from .rc2_base import RC2_Filter


class Normalize(RC2_Filter):
    name = "Normalize"
    description = "Normalize"
    icon = "icons/spectra.svg"

    def __init__(self):
        super().__init__()
        self.method = 'minmax'
        box = gui.widgetBox(self.controlArea, self.name)
        gui.comboBox(box, self, 'method', sendSelectedValue=True,
                     items=['unity', 'min_unity', 'unity_density', 'minmax'],
                     label='Normalization method', callback=self.auto_process)

    def process(self, spe):
        return spe.normalize(self.method)
