A QGIS PLUGIN THAT AUTOMATES LAND SUBDIVISION.
Block refers to polygon subject to subdivision.
Parcel refers to resulting polygons upon subdivision. 
The logic is pretty simple. 

GPS Coordinates of the road incident to the block make up the initial split line to give two polygons.
Using native join computations found in Land surveying, the software offsets "points-pairs" that make up linetsring geometry. 
The offsetting is based on width and length distances to make up a split net of the resulting lines. 
To the split net and input block, the native QGIS algorithm splitwihlines is used to obtain split polygons of user desired area. 

The length and width distances assume a very simple logic. 
Assume desired user length is 3m, where the input polygon length is 10m. First, the software determines the possible length segments. 
That is, 10/3 to get 3.33333 available length segments. It rounds the segments to an integer, now 3. 
Then divides the integer segments, 3, with the polygon length, 10, to obtain the optimal lenght distance, 3.333333.
This is the distance that will result to 3 equal lengths, then offsets this, 3.333333, as the distance.

Feeder Roads are generated via the junction points logic to ensure egress to all resulting parcels. 
Junction points are created based on the condition of odd versus even occurence of the split polygons(parcels).
The condition is that i, i*3, i*5 for odd occurence and i, i*3, i*4 for even occurence where i is the length distance. 
The feeder road length is offset as the distance making up n-1 parcel segments plus half the width distance.
Where n is the total number of parcel segments lying in the input block width. 
