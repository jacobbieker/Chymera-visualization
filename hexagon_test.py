__author__ = 'jacob'
import visit_writer, math

NX = 36
NZ = 12
NY = 36

def BlendPoint(A, B, t):
    return [(1.-t)*A[0] + t*B[0],(1.-t)*A[1] + t*B[1],(1.-t)*A[2] + t*B[2]]

def GetMeshPoints(angle, angle2):
    p = []
    for k in range(NZ):
        z = float(k) / float(NZ-1)
        for j in range(NY):
            y = float(j) / float(NY-1)
            for i in range(NX):
                x = float(i) / float(NX-1)
                A = [y*math.cos(angle),y*math.sin(angle),z]
                B = [y*math.cos(angle2),y*math.sin(angle2),z]
                p += BlendPoint(A,B,x)
    return p

def GetMeshConnectivity():
    c = []
    for k in range(NZ-1):
        for j in range(NY-1):
            for i in range(NX-1):
                # Make a hole
                if i == 1 and j == 2:
                    continue

                i0 = k*NY*NX + j*NX + i
                i1 = k*NY*NX + j*NX + (i+1)
                i2 = k*NY*NX + (j+1)*NX + (i+1)
                i3 = k*NY*NX + (j+1)*NX + i

                i4 = (k+1)*NY*NX + j*NX + i
                i5 = (k+1)*NY*NX + j*NX + (i+1)
                i6 = (k+1)*NY*NX + (j+1)*NX + (i+1)
                i7 = (k+1)*NY*NX + (j+1)*NX + i

                c.append((visit_writer.hexahedron, i0,i1,i2,i3,i4,i5,i6,i7))
    return c

def WriteProxyDataset():
    f = open("test.visit", "wt")
    f.write("!NBLOCKS 360\n")
    # Get the mesh 6 times and add it all up.
    for i in range(360):
        pts = []
        conn = []
        angle = math.radians(float(i) * 1.)
        angle2 = math.radians(float(i+1) *1.)
        pts += GetMeshPoints(angle, angle2)
        conn += GetMeshConnectivity()
        var = []
        for j in range(len(pts)/3):
            var.append(math.cos(pts[j*3]) + math.sin(pts[j*3+1]) + math.sin(pts[j*3+2]))
        # Pass the data to visit_writer
        vars = [("var", 1, 1, var)]
        visit_writer.WriteUnstructuredMesh("test%d.vtk" % i, 1, pts, conn, vars)
        f.write("test%d.vtk\n" % i)
    f.close()

WriteProxyDataset()
