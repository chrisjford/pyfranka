import pytest
from pyfranka import Gripper  # Assuming `Gripper` is a class in `pyfranka` that uses `libfranka`

def test_gripper_initialization():
    try:
        gripper = Gripper()
        assert gripper is not None
    except Exception as e:
        pytest.fail(f"Gripper initialization failed: {e}")

def test_gripper_open():
    gripper = Gripper()
    result = gripper.open()
    assert result is True  # Assuming `open` returns True on success