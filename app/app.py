import logging

from movingpandas import TrajectoryCollection
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from sdk.moveapps_spec import hook_impl
from sdk.moveapps_io import MoveAppsIo

from app.GUI import MyGui



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
        
        # Get the unique track IDS
        unique_track_ids = data_gdf[track_id_col_name].unique()
        
        # Get the updated data from the Gui
        updated_data = MyGui(data_gdf,unique_track_ids,track_id_col_name).save_tracks()
        
        # Transfer data back into a TrajectoryCollection
        return_data = TrajectoryCollection(updated_data,traj_id_col=track_id_col_name)

        # return some useful data for next apps in the workflow
        return return_data
