# -*- coding: utf-8 -*-


from mamba import description, context, it, before
from doublex import Spy, when, ANY_ARG
from expects import expect, raise_error, equal
from doublex_expects import have_been_called_with

from crafterbook.actions.add_crafter import AddCrafter



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

        with context('when validation fails'):
            with it('raises an Exception'):
                when(self.validator).raise_error_if_mandatory_parameter_not_exists(ANY_ARG).raises(Exception)

                def add_crafter_action_with_wrong_data():
                    wrong_input_data = {}
                    self.add_crafter_action.execute(wrong_input_data)

                expect(add_crafter_action_with_wrong_data).to(raise_error(Exception))
