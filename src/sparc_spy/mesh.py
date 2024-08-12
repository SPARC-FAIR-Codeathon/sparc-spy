import os 
import shutil
import pyvista as pv
from io import StringIO

class Meshes(object):
    def __init__(self) -> None:
        self.meshes = pv.MultiBlock()  

    def add_mesh(self, label: str, mesh: pv.PolyData): 
        self.meshes.append(label, mesh) 

    def export(self, output_filepath: str = "output.stl", base_path='.'):  
        save_multiblock_stl(self.meshes, output_filepath, base_path) 

    def items(self):
        items = []
        for key in self.meshes.keys():
            items.append((key, self.meshes[key]))
        return items
    

def save_multiblock_stl(multiblock, filename, base_path='.'):

    names = multiblock.keys()
    oname, ext = os.path.splitext(filename)
    assert ext == '.stl'
    
    # each individual stl file saved (output_filenames)
    ofiles = [os.path.join(base_path, f'{oname}_{ii}') + '.stl' for ii in range(len(names))]

    for ii, subpart in enumerate(multiblock):
        subpart.save(ofiles[ii], binary=False)
        change_first_line_of_file(ofiles[ii], f'solid {names[ii]}') # basically changes "solid" to "solid <solid_name>"

    # merge files together
    total_stl = ''
    for fn in ofiles:
        f = open(fn)
        total_stl += f.read()
        f.close()

    # writes total stl file 
    total_file_name = os.path.join(base_path, oname + '.stl')
    with open(total_file_name, 'w') as f:
        f.write(total_stl)

    # deletes previously written stl files
    for fn in ofiles:
        os.remove(fn)

    return

def change_first_line_of_file(filename, new_first_line):

    fr = open(filename, 'r')
    first_line = fr.readline()
    fr.close()
    first_line_len = len(first_line)

    new_first_line_len = len(new_first_line)
    spaces_num = first_line_len - new_first_line_len
    new_first_line = new_first_line + ' '*(spaces_num-1) + '\n'
    fw = StringIO(new_first_line)
    fr = open(filename, 'r+')
    shutil.copyfileobj(fw, fr)
    fr.close()
    fw.close()
    return

