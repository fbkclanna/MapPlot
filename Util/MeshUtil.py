def mid(text: str, n: int, m: int) -> str:
    return text[n: n + m]


def mesh_code2lon_lat(mesh_code: str):
    mesh_code = str(mesh_code)
    lon = float(mid(mesh_code, 2, 2)) + 100
    lat = float(mid(mesh_code, 0, 2)) / 1.5

    # 1次メッシュ
    if len(mesh_code) == 4:
        return lon, lat

    lon += ((float(mid(mesh_code, 5, 1)) * 7.5) / 100) / 60 * 100
    lat += ((float(mid(mesh_code, 4, 1)) * 5) / 100) / 60 * 100

    # 2次メッシュ
    if len(mesh_code) == 6:
        return lon, lat

    lon += ((float(mid(mesh_code, 7, 1)) * 45) / 10000) / (60 * 60) * 10000
    lat += ((float(mid(mesh_code, 6, 1)) * 30) / 10000) / (60 * 60) * 10000

    # 3次メッシュ
    if len(mesh_code) == 8:
        return lon, lat
