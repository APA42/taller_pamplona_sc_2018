# -*- coding: utf-8 -*-


from mamba import description, context, it, before
from doublex import Spy, when, ANY_ARG
from expects import expect, raise_error, equal
from doublex_expects import have_been_called_with


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


with description('Add Crafter Action specs') as self:
    with before.each:
        self.validator = Spy()
        self.crafter_management_service = Spy()
        self.add_crafter_action = AddCrafter(self.validator, self.crafter_management_service)

    with context('when adding a crafter'):
        with context('runs validations for mandatory parameters'):
            with context('with name parameter'):
                with it('calls the validator to raise error if parameter does not exists'):
                    a_json_input_data = {'crafter_name': 'a_crafter_name'}

                    self.add_crafter_action.execute(a_json_input_data)

                    expect(self.validator.raise_error_if_mandatory_parameter_not_exists).to(have_been_called_with(a_json_input_data,
                                                                                                                  'crafter_name'))

                with it('calls the validator to raise error if parameter is empty string'):
                    a_crafter_name = 'a_crafter_name'
                    a_json_input_data = {'crafter_name': a_crafter_name}

                    self.add_crafter_action.execute(a_json_input_data)

                    expect(self.validator.raise_error_if_crafter_name_is_empty).to(have_been_called_with(a_crafter_name))

                with it('calls the validator to raise error if parameter is None'):
                    a_crafter_name = 'a_crafter_name'
                    a_json_input_data = {'crafter_name': a_crafter_name}

                    self.add_crafter_action.execute(a_json_input_data)

                    expect(self.validator.raise_error_if_crafter_name_is_none).to(have_been_called_with(a_crafter_name))

                with it('calls the validator to check crafter_name already exists'):
                    a_crafter_name = 'a_crafter_name'
                    a_json_input_data = {'crafter_name': a_crafter_name}

                    self.add_crafter_action.execute(a_json_input_data)

                    expect(self.validator.raise_error_if_crafter_name_exists).to(have_been_called_with(a_crafter_name))

        with context('when all validations are successful'):
            with it('calls to crafter_management_service to add the crafter'):
                a_crafter_name = 'a_crafter_name'
                a_json_input_data = {'crafter_name': a_crafter_name}

                self.add_crafter_action.execute(a_json_input_data)

                expect(self.crafter_management_service.add).to(have_been_called_with(a_json_input_data))
