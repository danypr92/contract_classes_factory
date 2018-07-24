# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # support both Python2 and 3
""" test_mobile_contract_presenter.py

Test for MobileContractPresenter class
"""

# make sure (early) that parent dir (main app) is in path
import unittest2 as unittest
# from mock import patch

from contract_presenter_factory.mobile_contract_presenter import MobileContractPresenter # noqa


class ContractTryton():
    # TODO: In the future this class will be import from trytond lib
    service_type = None


# noinspection PyCompatibility
class MobileContractTests(unittest.TestCase):
    def test_mobile_contract(self):
        """ MobileContractPresenter class creation ok """
        self.assertIsInstance(
                MobileContractPresenter(),
                MobileContractPresenter)

    def test_no_line(self):
        """ MobileContractPresenter class creation ok """
        self.assertIsInstance(
                MobileContractPresenter(),
                MobileContractPresenter)
