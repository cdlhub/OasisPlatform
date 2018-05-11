import string
from random import choice
# from unittest import TestCase
from flask_testing import TestCase

import os

from src.conf.settings import settings
from src.server.app import create_app
from src.server.models import db


class AppTestCase(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        app = create_app(self.SQLALCHEMY_DATABASE_URI, track_modifications=False)
        return app

    def setup_example(self):
        db.create_all()

    def teardown_example(self, foo):
        db.session.remove()
        db.drop_all()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_input_file(self, path, size_in_bytes=None, data=b''):
        path = os.path.join(settings.get('server', 'INPUTS_DATA_DIRECTORY'), path)

        with open(path, 'wb') as outfile:
            for x in range(size_in_bytes or 0):
                outfile.write(choice(string.ascii_letters).encode())

            outfile.write(data)
