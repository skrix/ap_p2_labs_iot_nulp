import unittest
from src.lab8.level2.parser import Parser
from src.lab8.level2.max_flow import MaxFlow

class TestMaxFlow(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()
        self.service = MaxFlow()

    def _run_test_case(self, filename, expected_flow):
        farms, shops, roads, all_nodes = self.parser.parse_roads_csv(filename)
        max_flow = self.service.calculate_max_flow(farms, shops, roads, all_nodes)
        self.assertEqual(max_flow, expected_flow, f"Failed for {filename}")

    def test_case_1(self):
        self._run_test_case("tests/lab8/fixtures/test_roads_1.csv", 3)

    def test_case_2(self):
        self._run_test_case("tests/lab8/fixtures/test_roads_2.csv", 17)

    def test_case_3(self):
        self._run_test_case("tests/lab8/fixtures/test_roads_3.csv", 30)

    def test_case_4(self):
        self._run_test_case("tests/lab8/fixtures/test_roads_4.csv", 15)

    def test_case_5(self):
        self._run_test_case("tests/lab8/fixtures/test_roads_5.csv", 0)

    def test_case_5(self):
        self._run_test_case("tests/lab8/fixtures/test_roads_6.csv", 58)

if __name__ == "__main__":
    unittest.main()
