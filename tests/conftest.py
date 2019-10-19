import os
import pytest 

from marshmayama import Marshmayama

fixtures_path = os.path.abspath('tests/fixtures')

@pytest.fixture
def marshmayama_instance():
    def __create_marshmayama_instance(file_name):
        return Marshmayama(schema_file=f'{fixtures_path}/{file_name}')
    return __create_marshmayama_instance
