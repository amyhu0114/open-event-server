import unittest

from app.api.helpers.db import save_to_db, get_count
from app.api.helpers.events import create_custom_forms_for_attendees
from app.factories.event import EventFactoryBasic
from app.models.custom_form import CustomForms
from tests.all.integration.utils import OpenEventTestCase


class TestEventUtilities(OpenEventTestCase):

    def test_should_create_attendee_forms(self):
        """Method to test custom forms for attendees of an event."""
        with self.app.test_request_context():
            event = EventFactoryBasic()
            save_to_db(event)
            create_custom_forms_for_attendees(event)
            self.assertEqual(get_count(CustomForms.query), 3)


if __name__ == '__main__':
    unittest.main()
