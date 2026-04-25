"""Unit tests for data masking utilities."""

import pytest

from app.masking import MaskingContext, MaskingPolicy, find_identifiers


def test_masking_context_basic():
    """Test basic masking and unmasking flow."""
    ctx = MaskingContext(MaskingPolicy(enabled=True))
    original = "My IP is 192.168.1.1 and my email is test@example.com"

    masked = ctx.mask(original)
    assert "192.168.1.1" not in masked
    assert "test@example.com" not in masked
    assert "<IP_ADDRESS_0>" in masked or "<EMAIL_1>" in masked

    unmasked = ctx.unmask(masked)
    assert unmasked == original


def test_detect_builtin_entities():
    """Test detection of built-in entities (Email, IP)."""
    text = "Contact me at test@example.com or 10.0.0.5"
    policy = MaskingPolicy(enabled=True)
    identifiers = find_identifiers(text, policy)

    kinds = [i.kind for i in identifiers]
    assert "email" in kinds
    assert "ip_address" in kinds


def test_mask_value_recursive():
    """Test masking complex data structures (lists, dicts)."""
    ctx = MaskingContext(MaskingPolicy(enabled=True))
    data = {
        "user": "alice@example.com",
        "metadata": {"ip": "1.1.1.1", "tags": ["prod", "arn:aws:s3:::my-bucket"]},
    }

    masked = ctx.mask_value(data)

    assert "@example.com" not in str(masked)
    assert "1.1.1.1" not in str(masked)
    assert "arn:aws:s3" not in str(masked)

    unmasked = ctx.unmask_value(masked)
    assert unmasked == data
