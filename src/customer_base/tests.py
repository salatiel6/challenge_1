import customer_base.validators as validate
import re
import django.db
import django.core.exceptions

from customer_base.models import Client
from customer_base.exceptions import InvalidCpfException
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
                    InvalidCpfException,
                    validate.cpf_number, cpf
                )
            except Exception:
                raise Exception(f"Exception not thrown for this CPF: "
                                f"{cpf}")

    def test_input_same_cpf(self) -> None:
        with self.assertRaises(django.db.utils.IntegrityError):
            Client.objects.create(
                name="Chester Bennington",
                cpf="98654661046",
                birth_date="1976-03-20"
            )

            # Creating another client with the same cpf
            Client.objects.create(
                name="Mike Shinoda",
                cpf="98654661046",
                birth_date="1975-11-02"
            )

    def test_invalid_birth_date(self) -> None:
        # Setting invalid formats of birth_date.
        # Only format accepted is YYYY-MM-DD
        invalid_dates = self.create_invalid_birth_dates()

        for birth_date in invalid_dates:
            try:
                self.assertRaises(
                    django.core.exceptions.ValidationError,
                    Client.objects.create,
                    name="Chester Bennington",
                    cpf="98654661046",
                    birth_date=birth_date
                )

            except Exception:
                raise Exception(f"Exception not thrown for this BIRTH_DATE: "
                                f"{birth_date}")

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

    @staticmethod
    def create_invalid_birth_dates() -> []:
        invalid_dates = [
            "saddsfadfg", "", "12-01-19", "01-12-19", "19-12-01", "2022-30-30",
            "2022/01/01"
        ]

        return invalid_dates
