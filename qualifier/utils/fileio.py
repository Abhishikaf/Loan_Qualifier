# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(csvpath, header,qualifying_loans):
    """ Save the qualifying loan data to a CSV file. 
    
    Args:
        csvpath (Filepath): Path to the file where the qualifying loan data is to be saved

        header (list): List of Headers for the csv data

        qualifying_loans (list of lists): A list of all the qualifying bank loans
    
    """
    with open(csvpath, 'w', newline = "") as csvfile:
        csvwriter = csv.writer(csvfile)

        # Write the CSV header
        csvwriter.writerow(header)

        # Write the CSV data
        for row in qualifying_loans:
            csvwriter.writerow(row)
    return