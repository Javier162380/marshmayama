import pytest

def test_get_valid_schema_attributes(marshmayama_instance):
    expected_results = {
            "unknown": 'exclude'
        }
    Marshmayama = marshmayama_instance('simple_schema.yml')
    results = Marshmayama._Marshmayama__get_schema_attributes()
    assert expected_results == results

def test_get_invalid_schema_attributes(marshmayama_instance):
    Marshmayama = marshmayama_instance('invalid_schema_structure.yml')
    with pytest.raises(KeyError):
        Marshmayama._Marshmayama__get_schema_attributes()