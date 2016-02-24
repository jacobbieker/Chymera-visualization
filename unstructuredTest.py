import visit_writer
import math
import sys
 
nX = 20
nY = 20
conn = []
for i in range(nX-1):
   for j in range(nY-1):
      pt1 = j*(nX) + i;
      pt2 = j*(nX) + i+1;
      pt3 = (j+1)*(nX) + i+1;
      pt4 = (j+1)*(nX) + i;
      conn.append([ "quad", pt1, pt2, pt3, pt4 ])
 
pts = []
rad = []
for i in range(nX):
   for j in range(nY):
      pts.extend([ float(i), float(j), 0 ])
      rad.append( math.sqrt(i*i + j*j) )
 
var_datum = [ "radius", 1, 1, rad ]
vars = [ var_datum ]
visit_writer.WriteUnstructuredMesh("ugrid.vtk", 0, pts, conn, vars)
 
sys.exit()
