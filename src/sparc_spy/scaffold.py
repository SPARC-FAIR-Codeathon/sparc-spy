import json
import os
from typing import Dict

import numpy as np
import pyvista as pv

from sparc_spy import Mesh


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
                    if (
                        (i.keys().__contains__("Type") and i.keys().__contains__("URL"))
                        and (i.keys().__contains__("GroupName") or i.keys().__contains__("RegionPath"))
                        and i["Type"] != "View"
                    ):
                        key = i.pop("Type")
                        if isinstance(i["URL"], str):
                            urls = []
                            len_faces = []  # List of elements per line in the faces tag. (Per URL)
                            for url in i["URL"].split(","):
                                urls.append(url)

                                # Adding a hard-coded check for the code to skip "splited" json files.
                                if not url.__contains__("split"):
                                    absolute_path = [u for u in paths if u.__contains__(url)][
                                        0
                                    ]  # Fetching the absolute path of the json from the list of paths.
                                    # Splitting the content of the file on the basis of the tag. And then further splitting it on the basis of elements.
                                    con = (
                                        open(absolute_path)
                                        .read()
                                        .split("faces")[-1]
                                        .replace("\t", "")
                                        .split("\n")[1]
                                        .split(",")
                                    )
                                    len_faces.append(len([c for c in con if c != ""]))

                            i["URL"] = urls
                            i["face_line_len"] = len_faces

                        groupName, regionPath = "", ""
                        if i.keys().__contains__("GroupName"):
                            groupName = i.pop("GroupName")
                        if i.keys().__contains__("RegionPath"):
                            regionPath = i.pop("RegionPath")

                        if groupName != "" and regionPath != "":
                            label = groupName + "_" + regionPath

                            if groupName.lower() == regionPath.lower():
                                label = groupName
                        elif groupName != "":
                            label = groupName
                        else:
                            label = regionPath

                        i["label"] = label

                        if metadata.keys().__contains__(key):
                            metadata[key].append(i)
                        else:
                            metadata[key] = [i]
                    else:
                        print(f"[Error] Missing tags in metadata entry. Value: [{i}]")

    return metadata


class Scaffold(object):
    meshes: Dict

    def __init__(self, name, derivative_dir: str):
        self.name = name
        self.meshes = {}
        self.metadata = populate_metadata(self.__read_jsons(derivative_dir))
        self.geometry = self.build_scaffold(derivative_dir)

    def __read_jsons(self, dir: str):
        return [os.path.join(dir, file) for file in os.listdir(dir) if file.endswith(".json")]

    def build_scaffold(self, derivative_dir: str):
        """Create Scaffold from existing meshes and geometry.

        Args:
            derivative_dir (str): Derivative directory containing JSON files.
        """
        for surface in self.metadata["Surfaces"]:
            label = surface["label"].replace(" ", "_") if surface["label"] != "" else "unnamed"

            for i, url in enumerate(surface["URL"]):
                path = os.path.join(derivative_dir, url)
                n_elem = surface["face_line_len"][i]
                with open(path, "r") as f:
                    data = json.load(f)

                faces = np.array(data["faces"])
                faces = faces.reshape(-1, n_elem)
                faces = faces[:, 1:4]
                faces = np.hstack([np.full((faces.shape[0], 1), 3), faces])  # All faces are triangular

                vertices = np.array(data["vertices"])
                vertices = vertices.reshape(-1, 3)

                mesh = pv.PolyData(vertices, faces)
                self.meshes[label] = mesh

    def plot(self):
        pv.global_theme.color_cycler = ["#DA627D", "#33658A", "#86BBD8", "#06969A", "#9A348E"]
        pl = pv.Plotter()
        for label, mesh in self.meshes.items():
            pl.add_mesh(mesh, label=label)
        pl.add_legend()
        pl.show()

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

    def get_mesh_details(self):
        """List all meshes with their corresponding user defined names. These IDs
        could be used later on for different mesh specific tasks."""
        print("Avaialable meshes are:")
        for key in self.meshes.keys():
            print(f"   {key}")
        print()

    def update_mesh_label(self, original_name: str, new_name: str):
        """Update an auto defined mesh name.

        Args:
            original_name (str): Label to update
            new_name (str): New name for the label
        """
        self.meshes[new_name] = self.meshes[original_name]
        del self.meshes[original_name]
