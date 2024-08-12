class Scaffold:
    """
    Scaffold  
    """
    def __init__(self,):
        """
        this is my constructor
        """
        pass

    def read_ds(self, derivative_dir):
        """ 
        Load the scaffold from the .json files in the derivative directory.
        :param derivative_dir: The directory containing the .json files
        :type derivative_dir: str
        :return:
        :rtype:
        """
        pass 

    def plot(self, scaffold_tag=None): 

        """   
        Displays the meshes in the scaffold belonging to the scaffold_tag.
        :param scaffold_tag: The tag of the meshes in the scaffold to be plotted
        :type scaffold_tag: list of str
        :return: 
        :rtype: 
        """ 
        if scaffold_tag is None:  
            assert self.scaffold_tag is not None, "scaffold_tag is not defined" # To-Do: The scaffold tags should be added during loading
            scaffold_tag = self.scaffold_tag
        pass 

    def metadata(self, ): 
        """ 
        Displays the metadata of the scaffold. 
        :return: 
        :rtype: 
        """
        pass 

    def export(self, results_dir): 
        """
        Exports the scaffold to the results directory as VTK files.
        """ 
        pass 

    def add_mesh(self, mesh, label): 
        """
        Adds a mesh to the scaffold.
        :param mesh: The mesh to be added
        :type mesh: Mesh
        """
        pass 

    def get_mesh_ids(self, scaffold_tag): 
        """
        Returns the mesh ids of the scaffold belonging to the scaffold_tag.
        :param scaffold_tag: The tag of the meshes in the scaffold
        :type scaffold_tag: list of str
        :return: 
        :rtype: 
        """
        pass  

    