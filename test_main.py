import unittest
from unittest.mock import patch
import io
import sys
from main import main  # Import the main function from main.py

class TestMainFunction(unittest.TestCase):

    @patch("builtins.input", return_value="GR1 GR1 GR1")  # Test Case 1: Mocked input for Cart 1
    def test_main_cart1(self, mock_input):
        """Test main.py with Cart 1 input"""
        expected_output = "Final total price: €6.22"  # Expected result for Cart 1

        captured_output = io.StringIO()
        sys.stdout = captured_output

        main()

        sys.stdout = sys.__stdout__

        self.assertIn(expected_output, captured_output.getvalue())
    
    @patch("builtins.input", return_value="GR1 SR1 SR1 SR1")  # Test Case 2: Mocked input for Cart 2
    def test_main_cart2(self, mock_input):
        """Test main.py with Cart 2 input"""
        expected_output = "Final total price: €16.61"  # Expected result for Cart 2

        captured_output = io.StringIO()
        sys.stdout = captured_output

        main()

        sys.stdout = sys.__stdout__

        self.assertIn(expected_output, captured_output.getvalue())

    @patch("builtins.input", return_value="CF1 CF1 CF1 CF1")  # Test Case 3: Mocked input for Cart 3
    def test_main_cart3(self, mock_input):
        """Test main.py with Cart 3 input"""
        expected_output = "Final total price: €29.95"  # Expected result for Cart 3

        captured_output = io.StringIO()
        sys.stdout = captured_output

        main()

        sys.stdout = sys.__stdout__

        self.assertIn(expected_output, captured_output.getvalue())

    @patch("builtins.input", return_value="GR1 GR1 SR1 SR1 CF1 CF1")  # Test Case 4: Mocked input for Cart 4
    def test_main_cart4(self, mock_input):
        """Test main.py with Cart 4 input"""
        expected_output = "Final total price: €35.57"  # Expected result for Cart 4

        captured_output = io.StringIO()
        sys.stdout = captured_output

        main()

        sys.stdout = sys.__stdout__

        self.assertIn(expected_output, captured_output.getvalue())

    @patch("builtins.input", return_value="GR1 GR1 GR1 SR1 SR1 SR1 CF1 CF1 CF1")  # Test Case 5: Mocked input for Cart 5
    def test_main_cart5(self, mock_input):
        """Test main.py with Cart 5 input"""
        expected_output = "Final total price: €42.18"  # Expected result for Cart 5

        captured_output = io.StringIO()
        sys.stdout = captured_output

        main()

        sys.stdout = sys.__stdout__

        self.assertIn(expected_output, captured_output.getvalue())

if __name__ == "__main__":
    unittest.main()
