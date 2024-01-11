#!/usr/bin/python3
"""
Unittest for BaseModel class.
"""

import unittest
import json
import os
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class.
    """

    def setUp(self):
        """
        Set up test cases.
        """
        self.model = BaseModel()
        self.model.name = "Test Model"
        self.model.my_number = 42

    def tearDown(self):
        """
        Clean up after each test.
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        """
        Test instance creation and attributes.
        """
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertTrue(hasattr(self.model, 'name'))
        self.assertTrue(hasattr(self.model, 'my_number'))

    def test_save_method(self):
        """
        Test save method.
        """
        self.model.save()
        self.assertNotEqual(self.model.created_at, self.model.updated_at)

    def test_to_dict_method(self):
        """
        Test to_dict method.
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('name', model_dict)
        self.assertIn('my_number', model_dict)

    def test_str_method(self):
        """
        Test __str__ method.
        """
        string_representation = str(self.model)
        self.assertIsInstance(string_representation, str)
        self.assertIn('[BaseModel]', string_representation)
        self.assertIn(str(self.model.id), string_representation)
        self.assertIn(str(self.model.__dict__), string_representation)

    def test_reload_method(self):
        """
        Test reload method.
        """
        self.model.save()
        model_id = self.model.id
        del self.model
        new_storage = BaseModel()
        new_storage.reload()
        self.assertTrue(hasattr(new_storage, 'BaseModel.' + model_id))

if __name__ == "__main__":
    unittest.main()
