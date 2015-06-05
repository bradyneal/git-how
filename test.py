import unittest
from githow import parse_args


class GithowTests(unittest.TestCase):
    
    def get_expected_dict(self, subcommand, message=False):
        return {
            "filename": subcommand,
            "message": message
        }

    def test_parse_args_none(self):
        pass

    def test_parse_args_config(self):
        self.assertDictEqual(self.get_expected_dict("config"),
                             vars(parse_args(["config"])))

    def test_parse_args_create(self):
        self.assertDictEqual(self.get_expected_dict("create"),
                             vars(parse_args(["create"])))

    def test_parse_args_shorthand(self):
        self.assertDictEqual(self.get_expected_dict("shorthand"),
                             vars(parse_args(["shorthand"])))

    def test_parse_args_undo(self):
        self.assertDictEqual(self.get_expected_dict("undo"),
                             vars(parse_args(["undo"])))

    def test_parse_args_append_string_message(self):
        self.assertDictEqual(
            self.get_expected_dict("config", ["test message"]),
            vars(parse_args(["config", "-a" "test message"])))

    def test_parse_args_append_bare_message(self):
        self.assertDictEqual(
            self.get_expected_dict("config", ["test", "message"]),
            vars(parse_args(["config", "-a", "test", "message"])))


if __name__ == '__main__':
    unittest.main()