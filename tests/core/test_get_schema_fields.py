import pytest

def test_get_valid_fields(marshmayama_instance):
    expected_results = {
            "userId": {
                "attributes":{
                    "required": False,
                    "attribute": "user_id",
                    "missing": None
                },
                "type": "String",
            },
            "anonymousId":{
                "attributes":{
                    "required": False,
                    "attribute": "anonymous_id",
                },
                "type": "String"
            },
        }
    Marshmayama = marshmayama_instance('simple_schema.yml')
    results = Marshmayama._Marshmayama__get_schema_fields()
    assert expected_results == results

def test_get_invalid_fields(marshmayama_instance):
    Marshmayama = marshmayama_instance('invalid_schema_structure.yml')
    with pytest.raises(KeyError):
        Marshmayama._Marshmayama__get_schema_fields()
    