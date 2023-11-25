
import pytest
from src.model import Map, Field

def test_add_a_field_to_a_map():
    # GIVEN an empty map
    world = Map()
    # WHEN adding a new field (x=0, y=0, elevation 5)
    world.add_field(0, 0, 5)

    # THEN the map should contain a field with elevation 5 at (x=0, y=0)
    assert world.get_field(0, 0) == Field(0, 0, 5)

def test_adding_multiple_fields_to_a_map():
    # GIVEN an empty map
    world = Map()
    # WHEN adding a new field (x=0, y=0, elevation 5)
    world.add_field(0, 0, 5)
    # AND adding a new field (x=1, y=0, elevation 3)
    world.add_field(1, 0, 3)

    # THEN the map should contain a field with elevation 5 at (x=0, y=0)
    assert world.get_field(0, 0) == Field(0, 0, 5)

    # AND the map should contain a field with elevation 3 at (x=1, y=0)
    assert world.get_field(1, 0) == Field(1, 0, 3)

def test_create_a_simple_oneline_map_from_string():
    # GIVEN a multiline string
    map_string = """\
ab"""
    # WHEN creating a map from the string
    world = Map.from_string(map_string)
    # THEN the map should contain a field with elevation 0 (=a) at (x=0, y=0)
    assert world.get_field(0, 0) == Field(0, 0, 0)
    # AND the map should contain a field with elevation 1 (=b) at (x=1, y=0)
    assert world.get_field(1, 0) == Field(1, 0, 1)

def test_create_a_simple_twoline_map_from_string():
    # GIVEN a multiline string
    map_string = """\
a
b"""
    # WHEN creating a map from the string
    world = Map.from_string(map_string)
    # THEN the map should contain a field with elevation 0 (=a) at (x=0, y=0)
    assert world.get_field(0, 0) == Field(0, 0, 0)
    # AND the map should contain a field with elevation 1 (=b) at (x=0, y=1)
    assert world.get_field(0, 1) == Field(0, 1, 1)
    

def test_create_a_multiline_map_from_string():
    # GIVEN a multiline string
    multilinestring = """\
abc
def
ghi"""

    # WHEN creating a map from the string
    world = Map.from_string(multilinestring)

    #THEN the map should contain a field with elevation 0 (=a) at (x=0, y=0)
    assert world.get_field(0, 0) == Field(0, 0, 0)
    #THEN the map should contain a field with elevation 1 (=b) at (x=1, y=0)
    assert world.get_field(1, 0) == Field(1, 0, 1)
    #THEN the map should contain a field with elevation 2 (=c) at (x=2, y=0)
    assert world.get_field(2, 0) == Field(2, 0, 2)
    #THEN the map should contain a field with elevation 3 (=d) at (x=0, y=1)
    assert world.get_field(0, 1) == Field(0, 1, 3)
    #THEN the map should contain a field with elevation 4 (=e) at (x=1, y=1)
    assert world.get_field(1, 1) == Field(1, 1, 4)
    #THEN the map should contain a field with elevation 5 (=f) at (x=2, y=1)
    assert world.get_field(2, 1) == Field(2, 1, 5)
    #THEN the map should contain a field with elevation 6 (=g) at (x=0, y=2)
    assert world.get_field(0, 2) == Field(0, 2, 6)
    #THEN the map should contain a field with elevation 7 (=h) at (x=1, y=2)
    assert world.get_field(1, 2) == Field(1, 2, 7)
    #THEN the map should contain a field with elevation 8 (=i) at (x=2, y=2)
    assert world.get_field(2, 2) == Field(2, 2, 8)

def test_neighbour_fields_of_corner_elements():
    # GIVEN a multiline string
    multilinestring = """\
abc
def
ghi"""
    
    # WHEN creating a map from the string 
    map = Map()
    world = map.from_string(multilinestring)

    # THEN the neighbours from a should be b (x = 1, y = 0, elevation = 1) and d (x = 0, y = 1, elevation = 3)
    expected_neighbours = [Field(0, 1, 3), Field(1, 0, 1)]    
    neighbours = world.get_neighbours((0, 0))
    assert expected_neighbours == neighbours

    # THEN the neighbours from c should be b (x = 1, y = 0, elevation = 1) and f (x = 2, y = 1, elevation = 5)   
    expected_neighbours = [Field(2, 1, 5), Field(1, 0, 1)]
    neighbours = world.get_neighbours((2, 0))
    assert expected_neighbours == neighbours

    # THEN the neighbours from g should be d (x = 0, y = 1, elevation = 3) and h (x = 1, y = 2, elevation = 7)   
    expected_neighbours = [Field(0, 1, 3), Field(1, 2, 7)]
    neighbours = world.get_neighbours((0, 2))
    assert expected_neighbours == neighbours

    # THEN the neighbours from i should be h (x = 1, y = 2, elevation = 7) and f (x = 2, y = 1, elevation = 5)   
    expected_neighbours = [Field(2, 1, 5), Field(1, 2, 7)]
    neighbours = world.get_neighbours((2, 2))
    assert expected_neighbours == neighbours

def test_neighbour_fields_of_mid_element():
    # GIVEN a multiline string
    multilinestring = """\
abc
def
ghi"""
    
    # WHEN creating a map from the string 
    map = Map()
    world = map.from_string(multilinestring)

    # THEN the neighbours from e should be b (x = 1, y = 0, elevation = 1), d (x = 0, y = 1, elevation = 3), f (x = 2, y = 1, elevation = 5), h (x = 1, y = 2, elevation = 7)
    expected_neighbours = [Field(1, 0, 1), Field(1, 2, 7), Field(0, 1, 3), Field(2, 1, 5)]    
    neighbours = world.get_neighbours((1, 1))
    assert expected_neighbours == neighbours