from pathlib import Path
import pytest


@pytest.fixture(autouse=True) 
def setup_input_file():
    """Ensures the input file exists for validation checks if needed."""
    input_path = Path("/app/input.txt")
    # If it doesn't exist (e.g. during certain environment checks), create a standard mock file
    if not input_path.exists():
        mock_content = (
            "Harbor is an amazing framework\n"
            "\n"
            "for building terminal benchmarks\n"
            "   \n"
            "and testing intelligent agents"
        )
        input_path.write_text(mock_content)


def test_example_file_exists():
    """Test that the expected output file exists."""
    output_path = Path("/app/output.txt")
    assert output_path.exists(), f"File {output_path} does not exist"


def test_example_file_content():
    """Test that the output file contains the expected word count."""
    output_path = Path("/app/output.txt")
    
    # Based on the setup fixture text:
    # "Harbor is an amazing framework" (5)
    # "for building terminal benchmarks" (4)
    # "and testing intelligent agents" (4)
    # Total expected words = 13
    expected_content = "13"

    assert output_path.read_text().strip() == expected_content, (
        f"Expected '{expected_content}' but got '{output_path.read_text().strip()}'"
    )