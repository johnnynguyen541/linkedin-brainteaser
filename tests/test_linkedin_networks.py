# Unit Test
from Person import Person
import unittest
import json

# Network 1
#
#        -> Person 1_1
#
# Jen1   -> Person 1_2
#
#        -> Person 1_3  -> Person 1_3_1
#
# 
# Expected Sets = 2 * 2 * (1+2) = 12
jen1 = Person("Jen")
jen1.add_multiple(3) #
person1_3 = jen1.connections[2]
person1_3.add_connection()
jen1_expected_num = 12


# Network 2
#
# Jen2   -> Person 2_1 -> Person 2_1_1
#
#                      -> Person 2_1_2 -> Person 2_1_2_1
# 
# Expected Sets = 1 + [2 * (1+2)] = 7
jen2 = Person("Jen")
person2_1 = jen2.add_connection()
person2_1.add_connection()
person2_1_2 = person2_1.add_connection()
person2_1_2.add_connection()
jen2_expected_num = 7


# Network 3
#
#        -> Person 3_1
#
# Jen3   -> Person 3_2
#
#        -> Person 3_3
#
#        -> Person 3_4
# 
# Expected Sets = 2 * 2 * 2 * 2 = 16
jen3 = Person("Jen")
jen3.add_multiple(4) #
jen3_expected_num = 16


# Network 4
#
# Jen4
# 
# Expected Sets = 0
jen4 = Person("Jen")
jen4_expected_num = 0


# Network 5
#
#        -> Person 5_1    -> Person 5_1_1
#
# Jen5
#
#        -> Person 5_2    -> Person 5_2_1
#
# 
# Expected Sets = 9
jen5 = Person("Jen")
person5_1 = jen5.add_connection()
person5_1.add_connection()
person5_2 = jen5.add_connection()
person5_2.add_connection()
jen5_expected_num = 9


# Network 6
#                         -> Person 6_1_1
#        -> Person 6_1
#                         -> Person 6_1_1
# Jen6
#                         -> Person 6_2_1
#        -> Person 6_2
#                         -> Person 6_2_2
# 
# Expected Sets = [1 + (2*2)] * [1 + (2*2)] = 25
jen6 = Person("Jen")
person6_1 = jen6.add_connection()
person6_1.add_multiple(2)
person6_2 = jen6.add_connection()
person6_2.add_multiple(2)
jen6_expected_num = 25


class TestLinkedInNetworks(unittest.TestCase):
    def test_network_1(self):
        print("\nNETWORK #1\n")
        print(json.dumps(jen1.get_tree(), indent=2, sort_keys=False))
        self.assertEqual(jen1.get_possible_sets(), jen1_expected_num)

    def test_network_2(self):
        print("\nNETWORK #2\n")
        print(json.dumps(jen2.get_tree(), indent=2, sort_keys=False))
        self.assertEqual(jen2.get_possible_sets(), jen2_expected_num)

    def test_network_3(self):
        print("\nNETWORK #3\n")
        print(json.dumps(jen3.get_tree(), indent=2, sort_keys=False))
        self.assertEqual(jen3.get_possible_sets(), jen3_expected_num)
    
    def test_network_4(self):
        print("\nNETWORK #4\n")
        print(json.dumps(jen4.get_tree(), indent=2, sort_keys=False))
        self.assertEqual(jen4.get_possible_sets(), jen4_expected_num)
    
    def test_network_5(self):
        print("\nNETWORK #5\n")
        print(json.dumps(jen5.get_tree(), indent=2, sort_keys=False))
        self.assertEqual(jen5.get_possible_sets(), jen5_expected_num)

    def test_network_6(self):
        print("\nNETWORK #6\n")
        print(json.dumps(jen6.get_tree(), indent=2, sort_keys=False))
        self.assertEqual(jen6.get_possible_sets(), jen6_expected_num)

if __name__ == '__main__':
    unittest.main()
