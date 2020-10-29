# import packages
import json, folium, pandas
from matplotlib import pyplot as plt

# read data files
geo_path = "data/skorea-municipalities-2018-geo.json"
geo_data = json.load(open(geo_path, encoding="utf-8"))
stat_path = "data/output.json"
stat_data = json.load(open(stat_path, encoding="utf-8"))
fac_path = "data/count_by_local.json"
fac_data = json.load(open(fac_path, encoding="utf-8"))

# define variables for stats/dataframes
impairment_types = [
    # "지체_비율",
    "뇌병변_비율",
    "시각_비율",
    "청각_비율",
    "언어_비율",
    "지적장애_비율",
    "자폐_비율",
    "정신장애_비율",
    "신장장애_비율",
    "심장장애_비율",
    "호흡기_비율",
    "간_비율",
    "안면_비율",
    "장루요루_비율",
    "뇌전증_비율",
]
percentages = []
ratio_df = {}
district_centroids = []
for i in range(25):
    key = geo_data["features"][i]["properties"]["code"]
    vertices = geo_data["features"][i]["geometry"]["coordinates"][0][0]
    district = geo_data["features"][i]["properties"]["name"]
    _x_list = [v[1] for v in vertices]
    _y_list = [v[0] for v in vertices]
    _len = len(vertices)
    _x = sum(_x_list) / _len
    _y = sum(_y_list) / _len
    district_centroids.append([_x, _y])
    population = int(stat_data[district]["전체"])
    facilities = fac_data[district]
    ratio_df[key] = population / facilities
    _tmp_list = []
    # for j in range(len(impairment_types)):
    for j in range(14):
        _val = stat_data[district][impairment_types[j]]
        _tmp_list.append(_val)
    percentages.append(_tmp_list)
# visualise
visualisation = folium.Map(location=[37.5502, 126.982], zoom_start=12)
# add facility position markers
fac_addr = pandas.read_excel(open("data/address.xlsx", "rb"), header=None, index_col=0)
for i in range(len(fac_addr.index)):
    # print(fac_addr.iloc[i].name)
    lat = fac_addr.iloc[i, 0]
    lon = fac_addr.iloc[i, 1]
    circle_marker = folium.CircleMarker(
        location=[lat, lon],
        radius=4,
        color="lightblue",
        fill_color="blue",
        fill_opacity=1,
    )
    circle_marker.add_to(visualisation)
    visualisation.keep_in_front(circle_marker)

visualisation.choropleth(
    geo_data=geo_data,
    data=ratio_df,
    columns=["district", "ratio"],
    fill_color="YlOrRd",
    key_on="properties.code",
    highlight=True,
    fill_opacity=0.1,
    line_opacity=0.3,
    legend_name="Density of welfare facilities compared to disabled population in (by district)",
)

# # plot and save pie charts
for i in range(25):
    district = geo_data["features"][i]["properties"]["name"]
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 2, 2])
    ax.axis("equal")
    plt.axis("equal")
    ax.pie(percentages[i], labels=impairment_types, autopct="%1.2f%%")
    img_path = "data/img/"
    img_name = img_path + district + ".png"
    plt.savefig(img_name, bbox_inches="tight", transparent=True, pad_inches=0)
    # add custom marker
    if i == 0:
        icon = folium.features.CustomIcon(img_name, icon_size=(780, 600))
        # lat = district_centroids[i][0]
        # lon = district_centroids[i][1]
        # folium.Marker(location=[lat, lon], icon=icon).add_to(visualisation)
        folium.Marker(location=[157, 127], icon=icon).add_to(visualisation)

visualisation.save("visualisation.html")
