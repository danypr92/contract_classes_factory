# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # support both Python2 and 3
""" test_mobile_contract_presenter.py

Test for MobileContractPresenter class
"""

# make sure (early) that parent dir (main app) is in path
import unittest2 as unittest
# from mock import patch

from contract_presenter_factory.contract_presenter_factory import ContractMissingError # noqa
from contract_presenter_factory.contract_presenter_factory import ServiceTypeMissingError # noqa
from contract_presenter_factory.contract_presenter_factory import ServiceTypeUnknownError # noqa
from contract_presenter_factory.contract_presenter_factory import InternetWithoutSpecification # noqa
from contract_presenter_factory.contract_presenter_factory import ContractPresenterFactory # noqa

from contract_presenter_factory.adsl_contract_presenter import ADSLContractPresenter # noqa
from contract_presenter_factory.fibre_contract_presenter import FibreContractPresenter # noqa
from contract_presenter_factory.mobile_contract_presenter import MobileContractPresenter # noqa


class ContractTryton():
    # TODO: In the future this class will be import from trytond lib
    service_type = None
    internet_fibre = None
    internet_adsl = None


# noinspection PyCompatibility
class ContractFactoryTests(unittest.TestCase):
    def test_no_contract(self):
        """ If not contract has been passed, raise an exception."""
        self.assertRaises(ContractMissingError, ContractPresenterFactory)

    def test_contract_no_service_type(self):
        """ If not contract service_type has been passed, raise an exception."""
        contract = ContractTryton()
        self.assertRaises(
                ServiceTypeMissingError,
                ContractPresenterFactory,
                contract)

    def test_uknown_type_contract(self):
        """ If the contract.service_type passed is unknown,
        then raise an exception saying 'This service type is not allowed."""
        contract = ContractTryton()
        contract.service_type = 'rabbit'
        self.assertRaisesRegex(
                ServiceTypeUnknownError,
                "Service Type not allowed: *",
                ContractPresenterFactory,
                contract)

    def test_mobile_contract(self):
        """ MobileContractPresenter class was returned if type is 'mobile' """
        contract = ContractTryton()
        contract.service_type = 'mobile'
        self.assertIsInstance(
                ContractPresenterFactory(contract).to_presenter(),
                MobileContractPresenter)

    def test_internet_no_adsl_no_fibre_contract(self):
        """ Internet presenters need a check of 'fibre' or 'adsl' """
        contract = ContractTryton()
        contract.service_type = 'internet'
        self.assertRaises(
                InternetWithoutSpecification,
                ContractPresenterFactory,
                contract)

    def test_adsl_contract(self):
        """ ADSLContractPresenter class was returned if type is 'adsl' """
        contract = ContractTryton()
        contract.service_type = 'internet'
        contract.internet_adsl = True
        self.assertIsInstance(
                ContractPresenterFactory(contract).to_presenter(),
                ADSLContractPresenter)

    def test_fibre_contract(self):
        """ FibreContractPresenter class was returned if type is 'fibre' """
        contract = ContractTryton()
        contract.service_type = 'internet'
        contract.internet_fibre = True
        self.assertIsInstance(
                ContractPresenterFactory(contract).to_presenter(),
                FibreContractPresenter)
