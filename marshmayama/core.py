import marshmallow
import yaml

from .exceptions import MarshmayamaInvalidField,MarshmayamaInvalidSchemaAttribute 


class Marshmayama:

    VALID_FIELDS = marshmallow.fields.__all__
    VALID_SCHEMA_ATTRIBUTES = list(marshmallow.schema.Schema().__dict__.keys())

    def __init__(self, schema_file: str):

        self.schema_file = schema_file
        self.schema_data = self.__load_yaml_file(schema_file) 

    @staticmethod
    def __load_yaml_file(file: str)-> dict:
        """Method to load a yaml file into a valid python dict."""
        return yaml.load(open(file, 'r'), Loader=yaml.Loader)

    @staticmethod
    def __is_marshamallow_field(field_type :str)-> bool:
        """Method to check if a describe field is implement under marshamallow,
          fields class"""
        if field_type in Marshmayama.VALID_FIELDS:
            return True

        return False
    
    @staticmethod
    def __is_marshmallow_schema_attribute(schema_attribute_name: str)-> bool:
        """Method to check if a describe attribute is implement uner marshmallow
           schema class"""
        if schema_attribute_name in Marshmayama.VALID_SCHEMA_ATTRIBUTES:
            return True
        
        return False
        
    def __get_schema_fields(self):
        """Method to retribe all fields define in the yaml file"""
        try:
            return self.schema_data['schema_fields']
        except KeyError:
            raise KeyError("Yaml file does not follow Marshmayama yaml structure")

    def __get_schema_attributes(self):
        """Method to retrieve all the schea attributes define in the yaml file"""
        try:
            return self.schema_data['schema_attributes']
        except KeyError:
            raise KeyError("Yaml file does not follow Marshmayama yaml structure")

    def __create_schema_fields(self)-> dict:
        """Method to generate a dictionary with marshmallow fields objects."""
        marshmallow_fields = {}
        raw_schema_fields = self.__get_schema_fields()
        for field in raw_schema_fields:
            field_attributes=raw_schema_fields[field]['attributes']
            field_type= raw_schema_fields[field]['type']
            if self.__is_marshamallow_field(field_type):
                marshmallow_fields[field]=getattr(marshmallow.fields,field_type)(
                                                            **field_attributes  
                                                            if field_attributes else {})      
            else:
                raise MarshmayamaInvalidField(f"Field not supported. Supported fields: "
                                              f"{','.join(Marshmayama.VALID_FIELDS)}")

        return marshmallow_fields

    def __set_schema_attributes(self, schema: marshmallow.Schema)-> marshmallow.Schema:
        """Method to create marshmallow schema attributes."""
        schema_attributes = self.__get_schema_attributes()
        for attribute in schema_attributes:
            if self.__is_marshmallow_schema_attribute(schema_attribute_name=attribute):
                setattr(schema, attribute, schema_attributes[attribute])
            else:
                raise MarshmayamaInvalidSchemaAttribute("Schema attr not supported. Supported attributes: "
                                          f"{','.join(Marshmayama.VALID_SCHEMA_ATTRIBUTES)}")

        return schema
    
    def generate_schema(self)-> marshmallow.Schema:
        """Method to generate a Marshmallow schema from a Marshmayama definition"""

        schema_fields = self.__create_schema_fields()
        marshmayama_schema = type('MarshmayamaSchema', (marshmallow.Schema,), schema_fields)()

        if self.__get_schema_attributes():
            self.__set_schema_attributes(marshmayama_schema)
        
        return marshmayama_schema