import visit_writer
import math
 
pts = []
conn = []
celltype = []

nrevolutions = 100
head_size = 1
tube_radius = 0.2
tube_length = 2

arrow_head_angle = math.pi/4

# Make points for the head of the arrow
ptIdTip = len(pts)
z_head = math.sin(arrow_head_angle)*head_size
pts += [0, 0, z_head]
rad_head = math.cos(arrow_head_angle)*head_size

for i in range(nrevolutions):
    angle = 2*math.pi * i / (float(nrevolutions))
    pts += [math.cos(angle)*rad_head, math.sin(angle)*rad_head, 0]


for i in range(nrevolutions):
    p1 = i % nrevolutions
    p2 = (i+1) % nrevolutions
    conn.append((visit_writer.triangle, ptIdTip, ptIdTip+1+p1, ptIdTip+1+p2))

# Make the tube
tube_hits_arrow_at = tube_radius / math.tan(arrow_head_angle)
tube_pts = len(pts)/3

for i in range(nrevolutions):
    angle = 2*math.pi * i / (float(nrevolutions))
    pts += [math.cos(angle)*tube_radius, math.sin(angle)*tube_radius, tube_hits_arrow_at]
    pts += [math.cos(angle)*tube_radius, math.sin(angle)*tube_radius, -tube_hits_arrow_at-tube_length]


for i in range(nrevolutions):
    p1 = tube_pts + 2*(i%nrevolutions)
    p2 = tube_pts + 2*(i%nrevolutions)+1
    p3 = tube_pts + 2*((i+1)%nrevolutions)+1
    p4 = tube_pts + 2*((i+1)%nrevolutions)
    conn.append((visit_writer.quad, p1, p2, p3, p4))


visit_writer.WriteUnstructuredMesh("arrow", 0, pts, conn, [])
import sys
sys.exit()