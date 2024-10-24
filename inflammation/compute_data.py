"""Module containing mechanism for calculating standard deviation between datasets.
"""

# import glob
# import os
# import numpy as np
#
# from inflammation import models, views
#
#
# class JSONDataSource:
#     """Loads patient data with inflammation values from JSON files within a specified folder."""
#
#     def __init__(self,dir_path):
#         self.dir_path = dir_path
#
#     def load_inflammation_data(self):
#         """ Function loading inflamation data.
#
#         input
#         -----
#         data_dir: str
#             directory path to inflammation JSON files
#
#         returns
#         -------
#         data: list of 2D NumPy arrays
#             inflammation data loaded from all files found in a  data_dir
#
#         """
#
#         # data_file_paths = glob.glob(os.path.join(data_dir, '{}*.csv'.format(file_names)))
#         data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.json'))
#         if len(data_file_paths) == 0:
#             raise ValueError(f"No inflammation data CSV files found in path {self.dir_path}")
#         data = map(models.load_json, data_file_paths)
#
#         return list(data) # Return the list of 2D NumPy arrays with inflammation data
#
#
# class CSVDataSource:
#     """Loads all the inflammation CSV files within a specified directory."""
#
#     def __init__(self,dir_path):
#         self.dir_path = dir_path
#
#     def load_inflammation_data(self):
#     # def load_inflammation_data(data_dir, file_names = 'inflammation'):
#         """ Function loading inflamation data.
#
#         input
#         -----
#         data_dir: str
#             directory path to inflammation CSV files
#
#         returns
#         -------
#         data: list of 2D NumPy arrays
#             inflammation data loaded from all files found in a  data_dir
#
#         """
#
#         # data_file_paths = glob.glob(os.path.join(data_dir, '{}*.csv'.format(file_names)))
#         data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.csv'))
#         if len(data_file_paths) == 0:
#             raise ValueError(f"No inflammation data CSV files found in path {self.dir_path}")
#         data = map(models.load_csv, data_file_paths)
#
#         return list(data) # Return the list of 2D NumPy arrays with inflammation data
#
#
# def analyse_data(data_source):
#     """Calculates the standard deviation by day between datasets.
#
#     Gets all the inflammation data from CSV files within a directory,
#     works out the mean inflammation value for each day across all datasets,
#     then plots the graphs of standard deviation of these means."""
#
#     data = data_source.load_inflammation_data()
#     daily_standard_deviation = compute_standard_deviation_by_day(data)
#
#     graph_data = {
#         'standard deviation by day': daily_standard_deviation,
#     }
#     # views.visualize(graph_data)
#
#     return daily_standard_deviation
#
#
# def compute_standard_deviation_by_day(data):
#     """Calculates the standard deviation by day"""
#
#     means_by_day = map(models.daily_mean, data)
#     means_by_day_matrix = np.stack(list(means_by_day))
#
#     daily_standard_deviation = np.std(means_by_day_matrix, axis=0)
#
#     return daily_standard_deviation
#
