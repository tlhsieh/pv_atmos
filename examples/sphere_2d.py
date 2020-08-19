### plot (lon, lat, time) data on a sphere ###
# To use this script in Paraview: Tools -> Python Shell -> Run Script

pv_atmos_path = '/Users/hsiehtl/code/pv_atmos/'
execfile(pv_atmos_path + 'basic.py')
execfile(pv_atmos_path + 'grids.py')

def sphere2d(ncpath, varname):
    _, data = LoadData(ncpath, ncDims=['lon','lat'], aspectRatios=[1,1], logCoords=[], basis=[])
    c2p = CellDatatoPointData(data)
    map2d = Make3D(varname, expandDir='-z', aspectRatios=[1,1,1e-5], logCoords=[], src=c2p)
    sphere = LonLat2Polar(alpha=1, src=map2d, cutLat=-90)
    return sphere

file_name = '/Users/hsiehtl/Research_old/itcz-rce_6yr_vort850.nc'
variable_name = 'vort850'

sphere = sphere2d(file_name, variable_name)
h = Show(sphere)

# add colors
ColorBy(h, ('POINTS', variable_name))
repLUT = GetColorTransferFunction(variable_name)
repLUT.RescaleTransferFunction(-1e-4, 1e-4) # set color map limits

Render()

# To play movie: View -> Time Inspector
# To change color map: Color Map Editor -> Choose Preset
