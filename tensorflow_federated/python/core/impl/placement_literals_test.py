# Lint as: python3
# Copyright 2018, The TensorFlow Federated Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for placement_literals.py."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl.testing import absltest

from tensorflow_federated.python.common_libs import test
from tensorflow_federated.python.core.impl import placement_literals


class PlacementLiteralsTest(absltest.TestCase):

  def test_something(self):
    self.assertNotEqual(
        str(placement_literals.CLIENTS), str(placement_literals.SERVER))
    for literal in [placement_literals.CLIENTS, placement_literals.SERVER]:
      self.assertIs(
          placement_literals.uri_to_placement_literal(literal.uri), literal)

  def test_comparators_and_hashing(self):
    self.assertEqual(placement_literals.CLIENTS, placement_literals.CLIENTS)
    self.assertNotEqual(placement_literals.CLIENTS, placement_literals.SERVER)
    self.assertEqual(
        hash(placement_literals.CLIENTS), hash(placement_literals.CLIENTS))
    self.assertNotEqual(
        hash(placement_literals.CLIENTS), hash(placement_literals.SERVER))
    foo = {placement_literals.CLIENTS: 10, placement_literals.SERVER: 20}
    self.assertEqual(foo[placement_literals.CLIENTS], 10)
    self.assertEqual(foo[placement_literals.SERVER], 20)

  def test_placement_literals_equality(self):
    foo = placement_literals.PlacementLiteral('name', 'uri', 'desc')
    foo_eq = placement_literals.PlacementLiteral('name', 'uri', 'desc')
    foo_ne_attr1 = placement_literals.PlacementLiteral('dummy', 'uri', 'desc')
    foo_ne_attr2 = placement_literals.PlacementLiteral('name', 'dummy', 'desc')
    foo_ne_attr3 = placement_literals.PlacementLiteral('name', 'uri', 'dummy')
    # pylint: disable=g-generic-assert
    # Equal
    self.assertTrue(foo == foo)
    self.assertFalse(foo == 1)
    self.assertTrue(foo == test.EQUALS_EVERYTHING)
    self.assertFalse(foo == test.EQUALS_NOTHING)
    self.assertTrue(foo == foo_eq)
    self.assertTrue(foo_eq == foo)
    self.assertTrue(foo == foo_ne_attr1)
    self.assertTrue(foo_ne_attr1 == foo)
    self.assertFalse(foo == foo_ne_attr2)
    self.assertFalse(foo_ne_attr2 == foo)
    self.assertTrue(foo == foo_ne_attr3)
    self.assertTrue(foo_ne_attr3 == foo)
    # NotEqual
    self.assertFalse(foo != foo)
    self.assertTrue(foo != 1)
    self.assertFalse(foo != test.EQUALS_EVERYTHING)
    self.assertTrue(foo != test.EQUALS_NOTHING)
    self.assertFalse(foo != foo_eq)
    self.assertFalse(foo_eq != foo)
    self.assertFalse(foo != foo_ne_attr1)
    self.assertFalse(foo_ne_attr1 != foo)
    self.assertTrue(foo != foo_ne_attr2)
    self.assertTrue(foo_ne_attr2 != foo)
    self.assertFalse(foo != foo_ne_attr3)
    self.assertFalse(foo_ne_attr3 != foo)
    # pylint: enable=g-generic-assert


if __name__ == '__main__':
  absltest.main()
