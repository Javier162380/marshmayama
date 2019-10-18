import pytest

@pytest.fixture
def test_load_yaml_file(marshmayama_valid_instance):

    expected_data = {
        "schema_type":{
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
        "schema_attribute": {
            "unknown": 'exclude'
        }
    }

    parse_data = marshmayama_valid_instance('simple_schema.yml').schema_data
    assert parse_data == expected_data