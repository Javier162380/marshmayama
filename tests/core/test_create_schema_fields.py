import marshmallow
import pytest

from marshmayama.exceptions  import MarshmayamaInvalidField

def test_create_schema_valid_fields_types(marshmayama_instance):
    expected_results= {"userId": marshmallow.fields.String(attribute='user_id', 
                                                           required=False,
                                                           missing=None), 
                        "anonymousId": marshmallow.fields.String(attribute='anonymous_id',
                                                                 required=True)
                    }
    Marshmayama = marshmayama_instance('simple_schema.yml')
    results = Marshmayama._Marshmayama__create_schema_fields() 
    for field in expected_results:
        assert type(expected_results[field]) == type(results[field])

def test_create_schema_valid_fields_definition(marshmayama_instance):
    expected_results= {"userId": marshmallow.fields.String(attribute='user_id', 
                                                           required=False,
                                                           missing=None), 
                        "anonymousId": marshmallow.fields.String(attribute='anonymous_id',
                                                                 required=False)
                    }
    Marshmayama = marshmayama_instance('simple_schema.yml')
    results = Marshmayama._Marshmayama__create_schema_fields() 
    assert str(expected_results) == str(results)

def test_create_schema_invalid_fields(marshmayama_instance):
    Marshmayama = marshmayama_instance('invalid_schema_field.yml')
    with pytest.raises(MarshmayamaInvalidField):
        Marshmayama._Marshmayama__create_schema_fields() 