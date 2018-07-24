# -*- coding: utf-8 -*-
from .mobile_contract_presenter import MobileContractPresenter # noqa
from .adsl_contract_presenter import ADSLContractPresenter # noqa
from .fibre_contract_presenter import FibreContractPresenter # noqa


class ContractPresenterFactoryErrors(Exception):
    def __init__(self, message):
        super(ContractPresenterFactoryErrors, self).__init__(message)
        self.message = message


class ContractMissingError(ContractPresenterFactoryErrors):
    pass


class ServiceTypeMissingError(ContractPresenterFactoryErrors):
    pass


class ServiceTypeUnknownError(ContractPresenterFactoryErrors):
    pass


class InternetWithoutSpecification(ContractPresenterFactoryErrors):
    pass


class ContractPresenterFactory(object):

    """Contract Presenter Factory
    This factory return a concrete presenter based on the Contract type
    The possible models returned are:
        - MobileContractPresenter
        - ADSLContractPresenter
        - FibreContractPresenter
    """

    def __init__(self, contract=None):
        """ Early return if not has been passed contract or contract not has service_type.
        In other case, save the factory method """
        if not contract:
            raise ContractMissingError('contract is required!')
        elif not contract.service_type:
            raise ServiceTypeMissingError('contract.service_type is required!')

        self.contract = contract

        # In the Python documentation, '4.1 if Statements', the last paragraph says:
        # `An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages.`
        # https://docs.python.org/2/tutorial/controlflow.html#if-statements
        service_type = contract.service_type
        if service_type == 'mobile':
            self.create_contract_presenter = MobileContractPresenter
        elif service_type == 'internet':
            if self.contract.internet_adsl:
                self.create_contract_presenter = ADSLContractPresenter
            elif self.contract.internet_fibre:
                self.create_contract_presenter = FibreContractPresenter
            else:
                raise InternetWithoutSpecification('Internet contracts need be checked as `adsl` or `fibre`')
        else:
            raise ServiceTypeUnknownError('Service Type not allowed: %s' % str(service_type))

    def to_presenter(self):
        """ Return a presenter of a concrete type """
        return self.create_contract_presenter(self.contract)
