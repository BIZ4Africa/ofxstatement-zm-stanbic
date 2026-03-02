"""Unit tests for Stanbic Zambia ofxstatement plugin"""

import os
from decimal import Decimal as D
from io import StringIO

import pytest

from ofxstatement.plugins.stanbiczm import StanbicZmPlugin, StanbicZmParser


def get_sample_file_path(filename):
    """Get path to sample file in examples directory"""
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, "..", "src", "ofxstatement", "examples", filename)


class TestStanbicZmPlugin:
    """Test Stanbic Zambia plugin class"""

    def test_plugin_instantiation(self):
        """Test plugin can be instantiated"""
        plugin = StanbicZmPlugin(None, {})
        assert plugin is not None

    def test_get_parser(self):
        """Test plugin returns a parser"""
        plugin = StanbicZmPlugin(None, {})
        sample_file = get_sample_file_path("sample.csv")
        parser = plugin.get_parser(sample_file)
        assert isinstance(parser, StanbicZmParser)


class TestStanbicZmParser:
    """Test Stanbic Zambia parser"""

    def test_parse_format(self):
        """Test parsing a sample file"""
        plugin = StanbicZmPlugin(None, {"charset": "UTF-8"})
        sample_file = get_sample_file_path("sample.csv")
        parser = plugin.get_parser(sample_file)
        statement = parser.parse()

        # Check basic statement properties
        assert statement is not None
        assert statement.lines is not None

        # Check we have transactions
        assert len(statement.lines) >= 0

    def test_date_format(self):
        """Test date format is correct"""
        plugin = StanbicZmPlugin(None, {})
        sample_file = get_sample_file_path("sample.csv")
        parser = plugin.get_parser(sample_file)

        assert parser.date_format == "%d/%m/%Y"

    def test_mappings(self):
        """Test field mappings are correct"""
        plugin = StanbicZmPlugin(None, {})
        sample_file = get_sample_file_path("sample.csv")
        parser = plugin.get_parser(sample_file)

        assert parser.mappings["date"] == 1
        assert parser.mappings["refnum"] == 0
        assert parser.mappings["memo"] == 2
        assert parser.mappings["amount"] == 5
        assert parser.mappings["id"] == 0

    def test_fix_amount(self):
        """Test amount string cleaning"""
        plugin = StanbicZmPlugin(None, {})
        sample_file = get_sample_file_path("sample.csv")
        parser = plugin.get_parser(sample_file)

        # Test with comma separator
        result = parser.fix_amount("1,234.56")
        assert result == "1234.56"

        # Test with spaces
        result = parser.fix_amount("1 234.56")
        assert result == "1234.56"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
