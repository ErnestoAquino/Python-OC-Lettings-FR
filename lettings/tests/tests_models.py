import pytest

from lettings.models import Address
from lettings.models import Letting


@pytest.mark.django_db
def test_address_creation():
    """
    Test the creation and retrieval of an Address instance.
    """

    address = Address.objects.create(
        number=123,
        street="Test Street",
        city="Anytown",
        state="AN",
        zip_code=123456,
        country_iso_code='ATC'
    )

    # Retrieve the address from the database
    retrieved_address = Address.objects.get(pk=address.pk)

    # Check the address from the database
    assert retrieved_address.number == 123
    assert retrieved_address.street == "Test Street"
    assert retrieved_address.city == "Anytown"
    assert retrieved_address.state == "AN"
    assert retrieved_address.zip_code == 123456
    assert retrieved_address.country_iso_code == "ATC"


@pytest.mark.django_db
def test_address_str_method():
    """
    Test the __str__ method of the Address model.
    """
    address = Address.objects.create(
        number=123,
        street="Test Street",
        city="Anytown",
        state="AN",
        zip_code=123456,
        country_iso_code='ATC'
    )

    assert str(address) == "123 Test Street"


@pytest.mark.django_db
def test_letting_creation():
    """
    Test the creation and retrieval of a Letting instance.
    """
    address = Address.objects.create(
        number=123,
        street="Test Street",
        city="Anytown",
        state="AN",
        zip_code=123456,
        country_iso_code='ATC'
    )
    letting = Letting.objects.create(title="Test Letting", address=address)

    # Retrieve the letting from the database
    retrieved_letting = Letting.objects.get(pk=letting.pk)

    # Check the letting's attributes
    assert retrieved_letting.title == "Test Letting"
    assert retrieved_letting.address == address


@pytest.mark.django_db
def test_letting_str_method():
    """
    Test the __str__ method of the Letting model.
    """
    address = Address.objects.create(
        number=123,
        street="Test Street",
        city="Anytown",
        state="AN",
        zip_code=123456,
        country_iso_code='ATC'
    )

    letting = Letting.objects.create(
        title='Test Letting',
        address=address
    )

    assert str(letting) == 'Test Letting'
