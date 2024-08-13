from sparc_spy import Scaffold

scaffold = Scaffold("rat_gut", derivative_dir="example_data/files/derivative")
scaffold.get_mesh_details()
scaffold.plot()
scaffold.update_mesh_label(original_name="unnamed", new_name="whole_stomach")
scaffold.plot()
scaffold.export("output.stl")

scaffold = Scaffold("rat_intervension", derivative_dir="example_data/derivative/sub-112")
scaffold.plot()
