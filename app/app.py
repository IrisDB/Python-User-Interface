from sdk.moveapps_spec import hook_impl
from sdk.moveapps_io import MoveAppsIo
from movingpandas import TrajectoryCollection
import matplotlib.pyplot as plt
from app.GUI import MyGui
import logging


class App(object):

    def __init__(self, moveapps_io):
        self.moveapps_io = moveapps_io

    @hook_impl
    def execute(self, data: TrajectoryCollection, config: dict) -> TrajectoryCollection:
        """Your app code goes here"""
        logging.info(f'Welcome to the {config}')
        
        # Get the column with the track ID
        track_id_col_name = data.get_traj_id_col()
        
        # Transfer the data to a GeoDataFrame
        data_gdf = data.to_point_gdf()
        
        unique_track_ids = data_gdf[track_id_col_name].unique()
        
        # Make a plot of the data
        fig, ax = plt.subplots(figsize = (10,10))
        data_gdf.plot(ax=ax,column=track_id_col_name,alpha=0.5)
        plt.show()
        
        #MyGui()

        auxiliary_file_a = MoveAppsIo.get_auxiliary_file_path("auxiliary-file-a")
        with open(auxiliary_file_a, 'r') as f:
            logging.info(f.read())

        # return some useful data for next apps in the workflow
        return data
