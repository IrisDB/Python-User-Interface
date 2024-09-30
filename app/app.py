import logging

from movingpandas import TrajectoryCollection
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from sdk.moveapps_spec import hook_impl
from sdk.moveapps_io import MoveAppsIo

from app.plot import plot_tracks
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
        
        plot_gdf = plot_tracks(data=data_gdf, track_id_col_name=track_id_col_name)
        
        
        
        MyGui(plot_gdf)

        auxiliary_file_a = MoveAppsIo.get_auxiliary_file_path("auxiliary-file-a")
        with open(auxiliary_file_a, 'r') as f:
            logging.info(f.read())

        # return some useful data for next apps in the workflow
        return data
