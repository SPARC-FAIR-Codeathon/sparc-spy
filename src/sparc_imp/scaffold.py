from typing import List
import json
import pyvista as pv

from sparc_imp import Mesh


def populate_metadata(paths):
    """Populate the metadata map for internal use.

    Args:
        dir (str): list of paths of jsons.

    Returns:
        metadata (dict): dictionary containing metadata information.
    """
    metadata = {}
    for path in paths:
        if path.__contains__("metadata"):
            md_cnt = json.load(open(path))  # Loading metadata content.
            if isinstance(md_cnt, list):
                for i in md_cnt:
                    if (i.keys().__contains__('Type') and i.keys().__contains__('URL')) and \
                            (i.keys().__contains__("GroupName") or i.keys().__contains__("RegionPath"))\
                            and i["Type"] != "View":
                        key = i.pop("Type")
                        if isinstance(i["URL"], str):
                            urls = []
                            len_faces = []  # List of elements per line in the faces tag. (Per URL)
                            for url in i["URL"].split(","):
                                urls.append(url)
                                absolute_path = [u for u in paths if u.__contains__(url)][
                                    0]  # Fetching the absolute path of the json from the list of paths.
                                # Splitting the content of the file on the basis of the tag. And then further splitting it on the basis of elements.
                                con = open(absolute_path).read().split("faces")[-1].replace("\t", "").split("\n")[
                                    1].split(",")
                                len_faces.append(len([c for c in con if c != '']))

                            i["URL"] = urls
                            i["face_line_len"] = len_faces
                        if metadata.keys().__contains__(key):
                            metadata[key].append(i)
                        else:
                            metadata[key] = [i]
                    else:
                        print(f"[Error] Missing tags in metadata entry. Value: [{i}]")

    return metadata


class Scaffold(object):
    meshes: List[Mesh]

    def __init__(self, name):
        self._name = name
        # Expected value is a list of path of jsons.
        paths = ['derivatives/*.json']
        self.metadata = populate_metadata(paths)

    def build_scaffold(self, dir: str) -> pv.PolyData:
        """Create Scaffold from existing meshes and geometry.

        Args:
            dir (str): Root directory for derivative files where JSONs are.

        Returns:
            pv.PolyData: Scaffold containing Geometry and meshes
        """
        return

    def plot(self):
        """Plot the scaffold with all meshes along with checkboxes to activate
        or deactivate meshes."""
        return

    def export(self, output_filepath: str = "output.vtk"):
        """Export the scaffold to a .vtk file

        Args:
            output_filepath (str, optional): output_filepath (str): Output file
            path to save .vtk file. Defaults to "output.vtk".
        """

    def get_metadata(self):
        """Show a tabular view of metadata that is important to the user"""
        return

    def add_mesh(self, mesh_name: str, mesh: Mesh):
        """Modify self.meshes and add a new mesh to the list.

        Args:
            mesh_name (str): User defined name for the mesh
            mesh (Mesh): Mesh containing new experimental data
        """
        return

    def get_mesh_ids(self):
        """List all meshes with their corresponding user defined names. These IDs
        could be used later on for different mesh specific tasks."""
        return
