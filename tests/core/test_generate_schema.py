import pytest
import marshmallow

def test_generate_marshmallow_schema(marshmayama_instance):
    MarshInstance = marshmayama_instance('generic_schema.yml')
    Marshschema = MarshInstance.generate_schema()

    assert issubclass(type(Marshschema), type(marshmallow.Schema()))

def test_generate_marshmallow_schema_valid_load(marshmayama_instance):
    MarshInstance = marshmayama_instance('generic_schema.yml')
    expected_results = {
        "user_id":"Kayne",
        "anonymous_id":"Mr West",
        "metadata": {
            "style": "rap"
        }
    }

    MarshSchema = MarshInstance.generate_schema()
    results = MarshSchema.load({
        "userId": "Kayne",
        "anonymousId": "Mr West",
        "metadata": {
            "style": "rap"
        },
        "notwantedevents": "randomness"
    })

    assert expected_results == results

def test_generate_marshmallow_schema_invalid_load(marshmayama_instance):
    MarshInstance = marshmayama_instance('generic_schema.yml')
    MarshSchema = MarshInstance.generate_schema()

    with pytest.raises(marshmallow.ValidationError):
        MarshSchema.load({
        "anonymousId": "Mr West",
        "metadata": {
            "style": "rap"
        },
        "notwantedevents": "randomness"
    })

def test_generate_marshmallow_schema_valid_dump(marshmayama_instance):
    MarshInstance = marshmayama_instance('generic_schema.yml')
    expected_results = {
        "userId":"Kayne",
        "anonymousId":"Mr West",
        "metadata": {
            "style": "rap"
        }
    }

    MarshSchema = MarshInstance.generate_schema()
    results = MarshSchema.dump({
        "user_id": "Kayne",
        "anonymous_id": "Mr West",
        "metadata": {
            "style": "rap"
        }
    })
    assert expected_results == results

def test_generate_marshmallow_schema_invalid_dump(marshmayama_instance):
    MarshInstance = marshmayama_instance('generic_schema.yml')
    expected_results = {
        "user_id":"Kayne",
        "anonymous_id":"Mr West",
        "metadata": {
            "style": "rap"
        }
    }

    MarshSchema = MarshInstance.generate_schema()
    results = MarshSchema.dump({
        "user_id": "Kayne",
        "anonymous_id": "Mr West",
        "metadata": {
            "style": "rap"
        }
    })
    assert expected_results != results
