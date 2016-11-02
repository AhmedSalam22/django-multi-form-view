#pylint: disable=function-redefined, no-name-in-module, import-error
from behave import given
from behave import then
from behave import when

from base.models import Photo, Record


@given('that a user fills in the form with valid input')
def step_impl(context):
    image = open('test.png', 'r')

    context.values = {
        "title": "Test title",
        "description": "Test description",
        "tag": Photo.UNKNOWN,
        "image": image,
    }

@when('the user submits the form')
def step_impl(context):
    context.response = context.test.client.post(
        context.get_url('/records/new/'),
        context.values,
        follow=True,
    )

@then('a Record and Photo instance are created')
def step_impl(context):
    assert context.response.status_code == 200
    assert Photo.objects.count() == 1
    assert Record.objects.count() == 1
