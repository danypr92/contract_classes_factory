# -*- coding: utf-8 -*-


class ADSLContractPresenter(object):

    """ADSL Contract Presenter
    This class is a mapping of our ADSL object in OTRS system.
    TODO: add fields documentation
    """

    def __init__(self, contract=None):
        self.contract = contract
