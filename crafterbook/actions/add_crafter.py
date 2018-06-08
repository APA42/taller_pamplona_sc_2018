# -*- coding: utf-8 -*-


class AddCrafter(object):

    def __init__(self, validator, crafter_management_service):
        self._validator = validator
        self._crafter_management_service = crafter_management_service

    def execute(self, input_data):
        crafter_name_key = 'crafter_name'
        self._validator.raise_error_if_mandatory_parameter_not_exists(input_data, crafter_name_key)

        self._validator.raise_error_if_crafter_name_is_empty(input_data[crafter_name_key])
        self._validator.raise_error_if_crafter_name_is_none(input_data[crafter_name_key])

        self._validator.raise_error_if_crafter_name_exists(input_data[crafter_name_key])

        self._crafter_management_service.add(input_data)
