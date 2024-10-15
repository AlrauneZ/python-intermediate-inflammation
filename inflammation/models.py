"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np
import os
import json
import glob


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def load_json(filename):
    """Load a numpy array from a JSON document.


    Expected format:
    [
        {
            observations: [0, 1]
        },
        {
            observations: [0, 2]
        }
    ]

    :param filename: Filename of CSV to load

    """
    with open(filename, 'r', encoding='utf-8') as file:
        data_as_json = json.load(file)
        return [np.array(entry['observations']) for entry in data_as_json]


class CSVDataSource:
    """Loads all the inflammation CSV files within a specified directory."""

    def __init__(self,dir_path):
        self.dir_path = dir_path

    def load_inflammation_data(self):
    # def load_inflammation_data(data_dir, file_names = 'inflammation'):
        """ Function loading inflamation data.

        input
        -----
        data_dir: str
            directory path to inflammation CSV files

        returns
        -------
        data: list of 2D NumPy arrays
            inflammation data loaded from all files found in a  data_dir

        """

        # data_file_paths = glob.glob(os.path.join(data_dir, '{}*.csv'.format(file_names)))
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.dir_path}")
        data = map(load_csv, data_file_paths)

        return list(data) # Return the list of 2D NumPy arrays with inflammation data


class JSONDataSource:
    """Loads patient data with inflammation values from JSON files within a specified folder."""

    def __init__(self,dir_path):
        self.dir_path = dir_path

    def load_inflammation_data(self):
        """ Function loading inflamation data.

        input
        -----
        data_dir: str
            directory path to inflammation JSON files

        returns
        -------
        data: list of 2D NumPy arrays
            inflammation data loaded from all files found in a  data_dir

        """

        # data_file_paths = glob.glob(os.path.join(data_dir, '{}*.csv'.format(file_names)))
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.dir_path}")
        data = map(load_json, data_file_paths)

        return list(data) # Return the list of 2D NumPy arrays with inflammation data


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

    :param data: 2D array with inflammation data (rows
    contain measurements for patients across all days)
    :return: array of mean values (over all patients) for each day
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.

    :param data: 2D array with inflammation data (rows
    contain measurements for patients across all days)
    :return: array of maximum values (over all patients) for each day
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.

    :param data: 2D array with inflammation data (rows
    contain measurements for patients across all days)
    :return: array of minimum values (over all patients) for each day
    """
    return np.min(data, axis=0)
  

def compute_standard_deviation_by_day(data):
    """Calculates the standard deviation by day"""

    means_by_day = map(daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    return daily_standard_deviation


def analyse_data(data_source):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""

    data = data_source.load_inflammation_data()
    daily_standard_deviation = compute_standard_deviation_by_day(data)

    return daily_standard_deviation

class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)


class Person:
    """A person."""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name, observations = None):
        super().__init__(name)
        if observations is None:
            self.observations = []
        else:
            self.observations = observations

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(day, value)
        self.observations.append(new_observation)
        return new_observation

    @property
    def last_observation(self):
        return self.observations[-1]


class Doctor(Person):
    """A doctor in an inflammation study."""
    def __init__(self, name):
        super().__init__(name)
        self.patients = []

    def add_patient(self,new_patient):
        for patient in self.patients:
            if patient.name == new_patient.name:
                return
        #new_patient = Patient(name_partient)
        self.patients.append(new_patient)

        return new_patient