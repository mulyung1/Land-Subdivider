import math
## Your list of points (replace with your actual points)
points = []

#GPS coodinates
a = QgsPointXY(37.050538, -1.232178)
b = QgsPointXY(37.051722, -1.233861)
c = QgsPointXY(37.053617, -1.232516)
d = QgsPointXY(37.052436, -1.230831)

#UtM coordinates
a = QgsPointXY(283081.40, 9863727.70)
b = QgsPointXY(283213.36, 9863541.73)
c = QgsPointXY(283424.88, 9863690.58)
d = QgsPointXY(283292.59, 9863876.87)

az = d.azimuth(c)
print(az)
points.append(a)
points.append(b)
points.append(c)
points.append(d)



polygon = QgsGeometry.fromPolygonXY([points])

# Create a memory vector layer with polygon geometry
vlayer = QgsVectorLayer("Polygon?crs=EPSG:32737", "Study", "memory")

# Get the data provider of the layer
provider = vlayer.dataProvider()

# Create an empty feature
feature = QgsFeature()

# Set the feature geometry to the polygon
feature.setGeometry(polygon)

# Add the feature to the layer
provider.addFeature(feature)

# Update the layer extent
vlayer.updateExtents()

# Add the layer to the project
QgsProject.instance().addMapLayer(vlayer)