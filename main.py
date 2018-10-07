import pandas as pd
import colorcet

from Plot.BokehPlot import BokehPlot
from Util.MeshUtil import mesh_code2lon_lat
from Util.ColorUtil import value2heat_color

basemap_geojson_path = './GeoJson/japan.geojson'
sample_data = './Data/Census-MeshTest2005_3.csv'

if __name__ == '__main__':
    bokeh_plot = BokehPlot()

    # plot basemap
    bokeh_plot.plot_basemap_geojson(basemap_geojson_path)

    data = pd.read_csv(sample_data)
    # pre processing
    data['coordinate'] = data['mesh3_code'].apply(mesh_code2lon_lat)
    data['lat'] = data['coordinate'].apply(lambda x: x[0])
    data['lon'] = data['coordinate'].apply(lambda x: x[1])
    data['color'] = value2heat_color(data['value'], colorcet.fire)

    # bokeh_plot.fig.scatter(data['lat'], data['lon'], color=data['color'], radius=0.0045, fill_alpha=0.9)
    bokeh_plot.fig.scatter('lat', 'lon', source=data, color='color', radius=0.0045, fill_alpha=0.9)
    bokeh_plot.show()
