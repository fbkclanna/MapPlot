import shapely


def geometry2patch(polygons):
    # "各領域の x 座標 (経度) のリスト" のリスト
    xs = []

    # "各領域の y 座標 (緯度) のリスト" のリスト
    ys = []

    if isinstance(polygons, shapely.geometry.multipolygon.MultiPolygon):
        # MultiPolygon に含まれる Polygon を取り出す
        polygons = [x for x in polygons]
    elif isinstance(polygons, shapely.geometry.polygon.Polygon):
        polygons = [polygons]
    else:
        raise ValueError

    for p in polygons:
        # 境界の各点を経度、緯度に分割
        lons, lats = zip(*list(p.exterior.coords))
        xs.append(lons)
        ys.append(lats)

    return xs, ys
