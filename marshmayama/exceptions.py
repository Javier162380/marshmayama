class MarshmayamaInvalidField(Exception):
    """Raise when the schema field define is not a valid Marshmallow shcema field """
    pass

class MarshmayamaInvalidSchemaAttribute(Exception):
    """Raise when the schema attribute define is not a valid Marshmallow schema attribute"""