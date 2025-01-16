#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_instance(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, object)
        self.assertIsInstance(my_model.updated_at, object)

    def test_str(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(str(my_model), "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__))

    def test_save(self):
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertIsInstance(my_model_json, dict)
        self.assertIsInstance(my_model_json["created_at"], str)
        self.assertIsInstance(my_model_json["updated_at"], str)
        self.assertIsInstance(my_model_json["__class__"], str)
        self.assertEqual(my_model_json["__class__"], "BaseModel")