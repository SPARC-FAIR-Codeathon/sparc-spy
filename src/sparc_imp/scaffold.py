from typing import List

import pyvista as pv

from sparc_imp import Mesh


class Scaffold(object):
    meshes: List[Mesh]

    def __init__(self, name):
        self._name = name

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