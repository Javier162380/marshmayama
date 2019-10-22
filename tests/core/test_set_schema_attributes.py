import marshmallow
import pytest

from marshmayama.exceptions import MarshmayamaInvalidSchemaAttribute

def test_set_valid_schema_attributte(marshmayama_instance):
    expected_results = {
        'unknown': 'exclude',
        'ordered': True
    }

    Marshmayama = marshmayama_instance('simple_schema_with_attrs.yml')
    results_schema = Marshmayama._Marshmayama__set_schema_attributes(schema=marshmallow.Schema())

    for result in expected_results:
        assert getattr(results_schema, result) == expected_results[result]

def test_set_invalid_schema_attribute(marshmayama_instance):
    Marshmayama = marshmayama_instance('invalid_schema_attributes.yml')
    with pytest.raises(MarshmayamaInvalidSchemaAttribute):
        Marshmayama._Marshmayama__set_schema_attributes(schema=marshmallow.Schema())

