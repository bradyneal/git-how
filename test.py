import unittest
from githow import parse_args


class GithowTests(unittest.TestCase):
    
    def get_expected_dict(self, subcommand, print_all=False, message=None):
        return {
            "all": print_all,
            "filename": subcommand,
            "message": message
        }

    def test_parse_args_none(self):
        pass

    def test_parse_args_config(self):
        self.assertDictEqual(self.get_expected_dict("config"),
                             parse_args(["config"]))

    def test_parse_args_create(self):
        self.assertDictEqual(self.get_expected_dict("create"),
                             parse_args(["create"]))

    def test_parse_args_shorthand(self):
        self.assertDictEqual(self.get_expected_dict("shorthand"),
                             parse_args(["shorthand"]))

    def test_parse_args_undo(self):
        self.assertDictEqual(self.get_expected_dict("undo"),
                             parse_args(["undo"]))

    def test_parse_args_append_string_message(self):
        self.assertDictEqual(
            self.get_expected_dict("config", message=["test message"]),
            parse_args(["config", "-a" "test message"]))

    def test_parse_args_append_bare_message(self):
        self.assertDictEqual(
            self.get_expected_dict("config", message=["test", "message"]),
            parse_args(["config", "-a", "test", "message"]))


if __name__ == '__main__':
    unittest.main()