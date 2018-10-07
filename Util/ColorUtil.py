import pandas as pd
import colorcet


def value2heat_color(series: pd.Series, cmap: colorcet, d_min: float = None, d_max: float = None, d_bin: int = None):
    def value2index(value: float, cmap, d_min: float, d_max: float, bin: int):
        return cmap[int(value / ((d_max - d_min) / (bin - 1)))]

    # assert isinstance(cmap, colorcet)

    if d_min is None:
        d_min = min(series)

    if d_max is None:
        d_max = max(series)

    if d_bin is None:
        d_bin = len(cmap)

    if d_min == d_max:
        return cmap[0]

    return series.apply(value2index, cmap=cmap, d_min=d_min, d_max=d_max, bin=d_bin)
