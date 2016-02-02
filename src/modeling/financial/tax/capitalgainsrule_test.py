# -*- coding: utf-8 -*-
"""
This module provides testing code for the
auxi.modeling.financial.tax.capitalgainsrule module.

@author: Ex Mente Technologies (Pty) Ltd
"""

import unittest
from auxi.modeling.financial.tax.capitalgainsrule import CapitalGainsRule

__version__ = "0.2.0"


# =============================================================================
# Types.
# =============================================================================

class TestAllFunctions(unittest.TestCase):
    """
      Tester for the auxi.modeling.financial.tax.capitalgainsrule class.
    """

    def setUp(self):
        self.object = CapitalGainsRule("NameA",
                                       description="DescriptionA",
                                       percentage=1.14)

    def test_constructor(self):
        self.assertEqual(self.object.name, "NameA")
        self.assertEqual(self.object.description, "DescriptionA")
        self.assertEqual(self.object.percentage, 1.14)


# =============================================================================
# Display documentation and run tests.
# =============================================================================
# os.system("cls")

# help(SalesRule)

if __name__ == '__main__':
    unittest.main()
