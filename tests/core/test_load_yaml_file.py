import pytest

def test_load_yaml_file(marshmayama_instance):

    expected_results = {
        "schema_fields":{
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
        },
        "schema_attributes": {
            "unknown": 'exclude'
        }
    }

    results = marshmayama_instance('simple_schema.yml').schema_data
    assert results == expected_results