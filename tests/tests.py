import unittest
import os

import pandas as pd

from app.io.input import read_from_file, read_with_pandas


class TestReadFromFile(unittest.TestCase):

    def test_file_exists(self):
        self.assertTrue(os.path.exists("input.txt"))

    def test_file_content(self):
        expected_content = "Input file with text"
        self.assertEqual(read_from_file("input.txt"), expected_content)


class TestReadWithPandas(unittest.TestCase):

    def test_file_exists(self):
        # Перевірка наявності файлу для зчитування
        self.assertTrue(os.path.exists("input.csv"))

    def test_dataframe_type(self):
        # Перевірка типу поверненого значення
        self.assertIsInstance(read_with_pandas("input.csv"), pd.DataFrame)

    def test_dataframe_columns(self):
        # Перевірка наявності очікуваних стовпців у DataFrame
        expected_columns = {'column1', 'column2', 'column3'}
        self.assertEqual(set(read_with_pandas("input.csv").columns), expected_columns)
