import numpy as np
import pandas as pd
import geopandas as gpd
from Plot.BasePlot import BasePlot
import bokeh
from bokeh import plotting
import shapely

from Util.ShapeUtil import geometry2patch


class BokehPlot(BasePlot):
    def __init__(self, tooltips=None):
        # super.__init__()
        self.fig = plotting.figure(toolbar_location="left",
                                   plot_width=900,
                                   plot_height=700,
                                   tooltips=tooltips
                                   )
        self.fig.background_fill_color = "grey"
        self.fig.background_fill_alpha = 0.5

    def plot_basemap_geojson(self, geojson_path):
        self.plot_geojson(self.fig, geojson_path=geojson_path, polygon_column='geometry')

    def plot_geojson(self,
                     fig,
                     geojson_path,
                     polygon_column,
                     fill_color='black',
                     line_color='white',
                     line_width=0.5
                     ):
        geojson = self.load_geojson(geojson_path)

        for i, row in geojson.iterrows():
            lons, lats = geometry2patch(row[polygon_column])

            # 各領域を描画 (塗り分けはしない)
            self.fig.patches(lons, lats, fill_color=fill_color, line_color=line_color, line_width=line_width)

    def show(self):
        plotting.show(self.fig)
