import bpy
import os

input_directory = "D:\\Blender-Test\\Input"
output_directory = "D:\\Blender-Test\\Output"

def configure_fbx_settings(filepath):
    """Configures FBX export settings for compatibility with Unreal Engine 5."""
    bpy.ops.export_scene.fbx(
        filepath=filepath,
        use_selection=False,
        global_scale=1.0,
        apply_unit_scale=True,
        bake_space_transform=True,
        mesh_smooth_type='FACE',
        use_custom_props=True,
        add_leaf_bones=False,
    )

def export_blender_file(filepath, output_filepath):
    """Opens a Blender file, configures settings, and exports to FBX."""
    bpy.ops.wm.open_mainfile(filepath=filepath)
    configure_fbx_settings(output_filepath)

for file in os.listdir(input_directory):
    if file.endswith(".blend"):
        filepath = os.path.join(input_directory, file)
        output_filename = os.path.splitext(file)[0] + ".fbx"
        output_filepath = os.path.join(output_directory, output_filename)
        try:
            export_blender_file(filepath, output_filepath)
            print(f"Exported {file} to {output_filename}")
        except Exception as e:
            print(f"Error exporting {file}: {e}")
