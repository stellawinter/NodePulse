# test_nodepulse.py
"""
Tests for NodePulse module.
"""

import unittest
from nodepulse import NodePulse

class TestNodePulse(unittest.TestCase):
    """Test cases for NodePulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodePulse()
        self.assertIsInstance(instance, NodePulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodePulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
