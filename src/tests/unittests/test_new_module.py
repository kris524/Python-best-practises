
import pytest
from first_module.main import SpecificProduct1

def test_product():
    assert SpecificProduct1.operation() == "This is Specific Product 1"