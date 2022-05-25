import customer_base.validators as validate
import re

from rest_framework import serializers
from django.test import TestCase


class ClientTestCase(TestCase):
    # FORMAT
    # Testing format with VALID inputs
    def test_valid_unmasked_cpf(self) -> None:
        cpf = "98654661046"
        self.assertEqual(validate.cpf_number(cpf), cpf)

    def test_valid_masked_cpf(self) -> None:
        cpf = "673.903.650-05"
        self.assertEqual(validate.cpf_number(cpf), self.unmask_cpf(cpf))

    # Testing format with INVALID inputs
    def test_invalid_cpf(self) -> None:
        # Setting invalid formats of cpfs
        cpfs = self.create_invalid_cpfs()

        for cpf in cpfs:
            try:
                self.assertRaises(
                    serializers.ValidationError,
                    validate.cpf_number, cpf
                )
            except AssertionError as e:
                raise AssertionError(f"{e}, CPF:{cpf}")

    @staticmethod
    def unmask_cpf(cpf) -> str:
        return re.sub(r'\W', '', cpf)

    @staticmethod
    def create_invalid_cpfs() -> []:
        all_equal = "00000000000"
        letters = "qwertyuiopa"
        masked_letters = "qwe.rty.uio-pa"
        wrong_length = "123456789"
        unmasked = "12345678900"
        masked = "306.539.380-77"
        masked_all_equal = "000.000.000-00"

        cpfs = [
            all_equal, letters, masked_letters, wrong_length, unmasked, masked,
            masked_all_equal
        ]

        return cpfs
