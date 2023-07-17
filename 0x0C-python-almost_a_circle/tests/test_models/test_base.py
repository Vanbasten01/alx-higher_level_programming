#!/usr/bin/python3
"""Unit tests for testing the Base class."""

import unittest

from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Unit tests for testing the Base class."""

    def test_base_1_using_id(self):
        """""Test initializing Base instance with a specific ID."""
        b1 = Base(344)
        self.assertEqual(b1.id, 344)

    def test_base_2_id_default(self):
        """Test initializing Base instance with default id."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_3_many_instances(self):
        """test multiple instances"""
        b3 = Base()
        b4 = Base(23)
        b5 = Base()
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 23)
        self.assertEqual(b5.id, 4)

    def test_base_4_to_json_string_method(self):
        """test to_json_string method """
        self.assertEqual(Base.to_json_string([]), "[]")
        ld1 = Base.to_json_string([{'id': 34, 'name': True}])
        self.assertEqual(ld1, '[{"id": 34, "name": true}]')
        ld2 = Base.to_json_string([
            {"id": 34, "name": "Yasin"},
            {"id": 28, "name": "Vanbasten"}
            ])
        self.assertEqual(
                ld2, '[{"id": 34, "name": "Yasin"}, '
                '{"id": 28, "name": "Vanbasten"}]'
                )
        self.assertIsInstance(ld2, str)

    def test_base_5_from_json_string_method(self):
        """test the from_json_string """
        self.assertEqual(Base.to_json_string(""), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        ld1 = Base.from_json_string('[{"id": 34, "name": true}]')
        self.assertEqual(ld1, [{'id': 34, 'name': True}])
        ld2 = Base.from_json_string(
                '[{"id": 34, "name": "Yasin"}, '
                '{"id": 28, "name": "Vanbasten"}]'
                )
        self.assertEqual(ld2, [{
            "id": 34, "name": "Yasin"},
                {"id": 28, "name": "Vanbasten"}])
