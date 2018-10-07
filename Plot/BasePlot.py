import numpy as np
import pandas as pd
import geopandas as gpd


class BasePlot:

    def __init__(self, ):
        pass

    @staticmethod
    def load_geojson(file_name):
        return gpd.read_file(file_name)

    def plot_geojson(self, fig, geojson_path, polygon):
        raise NotImplementedError

    def show(self):
        raise NotImplementedError

