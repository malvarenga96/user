from unittest import TestCase

from flake8.api import legacy as flake8


class CodeTest(TestCase):
    def test_code(self):
        style_guide = flake8.get_style_guide()
        report = style_guide.check_files(['user'])

        self.assertEqual(report.total_errors, 0)
