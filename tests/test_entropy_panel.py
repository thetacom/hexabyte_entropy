"""Unit test suite for Entropy Panel."""

from hexabyte_entropy.widgets.entropy_panel import EntropyPanel


def test_entropy_panel_creation():
    """Test the creation of an info panel."""
    panel = EntropyPanel("Test Panel")
    assert panel is not None
