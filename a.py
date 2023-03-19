import bpy

# Delete default cube
bpy.ops.object.delete(use_global=False)

# Create base shape
bpy.ops.mesh.primitive_cube_add(
    size=2, enter_editmode=False, location=(0, 0, 0))

# Scale the base shape to create the laptop body
bpy.ops.transform.resize(value=(1.5, 0.8, 0.2))

# Create the screen by extruding from the top face of the laptop body
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_mode(type='FACE')
bpy.ops.mesh.select_nth(nth=2)
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, 0.5)})
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.object.mode_set(mode='OBJECT')

# Add materials and textures
mat_body = bpy.data.materials.new('Body')
mat_screen = bpy.data.materials.new('Screen')
tex_body = bpy.data.textures.new('Body', 'IMAGE')
tex_screen = bpy.data.textures.new('Screen', 'IMAGE')
img_body = bpy.data.images.load('1.jpg')
img_screen = bpy.data.images.load('2.jpg')
mat_body.texture_slots.add()
mat_body.texture_slots[0].texture = tex_body
mat_body.texture_slots[0].texture_coords = 'UV'
mat_body.texture_slots[0].uv_layer = 'UVMap'
mat_body.texture_slots[0].mapping = 'FLAT'
mat_body.texture_slots[0].texture.image = img_body
mat_screen.texture_slots.add()
mat_screen.texture_slots[0].texture = tex_screen
mat_screen.texture_slots[0].texture_coords = 'UV'
mat_screen.texture_slots[0].uv_layer = 'UVMap'
mat_screen.texture_slots[0].mapping = 'FLAT'
mat_screen.texture_slots[0].texture.image = img_screen
bpy.context.object.data.materials.append(mat_body)
bpy.context.object.data.materials.append(mat_screen)

# Set the camera position and orientation
camera = bpy.data.objects['Camera']
camera.location = (0, -10, 1)
camera.rotation_euler = (1.0472, 0, -1.5708)

# Render the image
bpy.ops.render.render(write_still=True)
