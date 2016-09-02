import ConfigParser

from doit.action import CmdAction


def load_configuration():
    config = ConfigParser.RawConfigParser()
    config.read('conf/unit_test.conf')
    return config


def task_run_unit_test_with_reports():
    """Running unit tests with xml reports"""

    def execute_cmd_test():
        config = load_configuration()
        return "py.test -v --junitxml={0} --cov-report {1} --cov {2} {3}".format(
            config.get("unit_test", "junitxml_file"),
            config.get("unit_test", "coverage_type"),
            config.get("unit_test", "coverage_module"),
            config.get("unit_test", "unit_test_dir"),
        )

    return {
        'actions': [
            CmdAction(execute_cmd_test)
        ],
        'verbosity': 1
    }


def task_run_unit_test():
    """Running unit tests"""

    def execute_cmd_test():
        config = load_configuration()
        return "py.test -v --cov {0} {1}".format(
            config.get("unit_test", "coverage_module"),
            config.get("unit_test", "unit_test_dir"),
        )

    return {
        'actions': [
            CmdAction(execute_cmd_test)
        ],
        'verbosity': 2
    }

