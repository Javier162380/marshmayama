import pytest

def test_marshamallow_valid_field(marshmayama_instance):
    Marshmayama = marshmayama_instance('simple_schema.yml')
    expected_results = True
    results = Marshmayama._Marshmayama__is_marshamallow_field('String')
    assert expected_results == results

def test__marshmallow_invalid_field(marshmayama_instance):
    Marshmayama = marshmayama_instance('simple_schema.yml')
    expected_results = False
    results = Marshmayama._Marshmayama__is_marshamallow_field('warefagrefdasfwe')
    assert expected_results == results
