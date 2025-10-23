# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
import six

from mypkg import add, safe_div

def test_add_ints():
    assert add(2, 3) == 5

def test_safe_division_behavior():
    # Py2 uses true division due to __future__ import, so 5/2 == 2.5
    assert safe_div(5, 2) == 2.5

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        safe_div(1, 0)

def test_text_type():
    # Ensure text handling is consistent across Py2/3 via six
    s = u"hola"
    assert isinstance(s, six.text_type)
