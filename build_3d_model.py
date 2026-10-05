import bpy
import math

# Clear scene
bpy.ops.wm.read_factory_settings(use_empty=True)

# 1. Core Icosahedron (Geometric Quantum Core)
bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, radius=1.3, location=(0, 0, 0))
core = bpy.context.active_object
core.name = "QuantumCore"

# Core Material (Neon Cyan Emission + Metallic)
mat_core = bpy.data.materials.new(name="Mat_QuantumCore")
mat_core.use_nodes = True
nodes_c = mat_core.node_tree.nodes
nodes_c.clear()
node_out_c = nodes_c.new(type='ShaderNodeOutputMaterial')
node_principled = nodes_c.new(type='ShaderNodeBsdfPrincipled')
node_principled.inputs['Base Color'].default_value = (0.0, 0.94, 1.0, 1.0)
node_principled.inputs['Metallic'].default_value = 0.95
node_principled.inputs['Roughness'].default_value = 0.1
node_principled.inputs['Emission Color'].default_value = (0.0, 0.94, 1.0, 1.0)
node_principled.inputs['Emission Strength'].default_value = 3.5
mat_core.node_tree.links.new(node_principled.outputs['BSDF'], node_out_c.inputs['Surface'])
core.data.materials.append(mat_core)

# 2. Orbital Torus Ring 1 (Inner Gyroscope)
bpy.ops.mesh.primitive_torus_add(major_radius=2.2, minor_radius=0.06, major_segments=64, minor_segments=16)
ring1 = bpy.context.active_object
ring1.name = "OrbitalRing_1"
ring1.rotation_euler = (math.radians(35), math.radians(25), 0)

# Ring 1 Material (Violet Chrome)
mat_ring1 = bpy.data.materials.new(name="Mat_Ring1")
mat_ring1.use_nodes = True
nodes_r1 = mat_ring1.node_tree.nodes
nodes_r1.clear()
node_out_r1 = nodes_r1.new(type='ShaderNodeOutputMaterial')
node_bsdf_r1 = nodes_r1.new(type='ShaderNodeBsdfPrincipled')
node_bsdf_r1.inputs['Base Color'].default_value = (0.65, 0.25, 0.96, 1.0)
node_bsdf_r1.inputs['Metallic'].default_value = 1.0
node_bsdf_r1.inputs['Roughness'].default_value = 0.15
node_bsdf_r1.inputs['Emission Color'].default_value = (0.65, 0.25, 0.96, 1.0)
node_bsdf_r1.inputs['Emission Strength'].default_value = 2.0
mat_ring1.node_tree.links.new(node_bsdf_r1.outputs['BSDF'], node_out_r1.inputs['Surface'])
ring1.data.materials.append(mat_ring1)

# 3. Orbital Torus Ring 2 (Outer Gyroscope)
bpy.ops.mesh.primitive_torus_add(major_radius=2.9, minor_radius=0.08, major_segments=64, minor_segments=16)
ring2 = bpy.context.active_object
ring2.name = "OrbitalRing_2"
ring2.rotation_euler = (math.radians(-45), math.radians(65), math.radians(20))

# Ring 2 Material (Rose Pink Laser)
mat_ring2 = bpy.data.materials.new(name="Mat_Ring2")
mat_ring2.use_nodes = True
nodes_r2 = mat_ring2.node_tree.nodes
nodes_r2.clear()
node_out_r2 = nodes_r2.new(type='ShaderNodeOutputMaterial')
node_bsdf_r2 = nodes_r2.new(type='ShaderNodeBsdfPrincipled')
node_bsdf_r2.inputs['Base Color'].default_value = (0.95, 0.2, 0.45, 1.0)
node_bsdf_r2.inputs['Metallic'].default_value = 0.9
node_bsdf_r2.inputs['Roughness'].default_value = 0.2
node_bsdf_r2.inputs['Emission Color'].default_value = (0.95, 0.2, 0.45, 1.0)
node_bsdf_r2.inputs['Emission Strength'].default_value = 2.5
mat_ring2.node_tree.links.new(node_bsdf_r2.outputs['BSDF'], node_out_r2.inputs['Surface'])
ring2.data.materials.append(mat_ring2)

# Export scene to GLB
output_path = r"C:\Users\RDC\Desktop\VortexIndustriesSite\vortex_core.glb"
bpy.ops.export_scene.gltf(
    filepath=output_path,
    export_format='GLB',
    use_selection=False,
    export_apply=True
)
print("SUCCESS: 3D Vortex Core Model exported to", output_path)
