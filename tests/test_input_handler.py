from src.input_handler import InputHandler

def test_read_file(tmp_path):
    file_path = tmp_path / "input.txt"
    file_path.write_text("data")
    handler = InputHandler()
    assert handler.read_file(str(file_path)) == "data"

def test_validate_input():
    handler = InputHandler()
    assert handler.validate_input("hello")
    assert not handler.validate_input("   ")

