import bpy
import json
import math

# Reset scene
bpy.ops.wm.read_factory_settings(use_empty=True)

# 1. Quantum Microprocessor Core Cube
# Outer structural cube with hollow circuit channels
bpy.ops.mesh.primitive_cube_add(size=3.0, location=(0, 0, 0))
outer_cube = bpy.context.active_object
outer_cube.name = "QuantumChip_Shell"

# 2. Camera Fly-Through Spline Path (Snakes directly through the center of the chip)
# Stage 1: Macro view (Z = 16)
# Stage 2: Outer Matrix Doll-in (Z = 7)
# Stage 3: Direct Core Circuit Injection (Z = 0 -> Z = -18)
# Stage 4: Emergence into Infinite Lattice (Z = -60)
curve_data = bpy.data.curves.new('CameraSpline', type='CURVE')
curve_data.dimensions = '3D'
spline = curve_data.splines.new('BEZIER')

points = [
    (0.0, 0.5, 16.0),     # Stage 01: Macro
    (0.8, -0.4, 7.0),     # Stage 02: Outer Matrix
    (0.0, 0.0, 0.0),      # Stage 03: Chip Center Penetration
    (-0.5, 0.2, -18.0),   # Stage 03b: Logic Tunnel
    (0.0, 0.0, -60.0)     # Stage 04: Infinite Lattice Emergence
]

spline.bezier_points.add(len(points) - 1)
for i, pt in enumerate(points):
    bp = spline.bezier_points[i]
    bp.co = pt
    bp.handle_left_type = 'AUTO'
    bp.handle_right_type = 'AUTO'

curve_obj = bpy.data.objects.new('CameraSplinePath', curve_data)
bpy.context.collection.objects.link(curve_obj)

# Sample 100 interpolation points along the spline for smooth GSAP WebGL camera scrubbing
evaluated_curve = curve_obj.to_curve_eval() if hasattr(curve_obj, "to_curve_eval") else curve_obj.data
samples = []
total_samples = 100
for step in range(total_samples + 1):
    t = step / float(total_samples)
    # Parametric quadratic / cubic interpolation through control points
    # Simple smooth spline interpolation array for WebGL
    idx = min(int(t * (len(points) - 1)), len(points) - 2)
    local_t = (t * (len(points) - 1)) - idx
    p0 = points[idx]
    p1 = points[idx + 1]
    
    # Smooth step
    st = local_t * local_t * (3.0 - 2.0 * local_t)
    x = p0[0] + (p1[0] - p0[0]) * st
    y = p0[1] + (p1[1] - p0[1]) * st
    z = p0[2] + (p1[2] - p0[2]) * st
    samples.append({"x": round(x, 4), "y": round(y, 4), "z": round(z, 4)})

# Export camera path vertices to JSON
json_path = r"C:\Users\RDC\Desktop\VortexIndustriesSite\camera_spline.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(samples, f, indent=2)
print("SUCCESS: Camera Spline Path vertices exported to", json_path)
