"""Shared availability and error response helpers for tools."""

from __future__ import annotations

from typing import Any


def unavailable(source: str, empty_key: str, error: str, **extra: Any) -> dict[str, Any]:
    """Standardised unavailable response for tools.

    Ensures a consistent shape for 'available: False' responses, including
    source identifier, error message, and an empty list for the primary
    result key to keep downstream parsers happy.
    """
    return {"source": source, "available": False, "error": error, empty_key: [], **extra}


def eks_available_or_backend(sources: dict[str, dict]) -> bool:
    """Check if EKS is available or if we are using a synthetic backend."""
    eks = sources.get("eks", {})
    is_verified = bool(eks.get("connection_verified"))
    has_backend = bool(eks.get("_backend"))
    return is_verified or has_backend


def datadog_available_or_backend(sources: dict[str, dict]) -> bool:
    """Check if Datadog is available or if we are using a synthetic backend."""
    dd = sources.get("datadog", {})
    is_verified = bool(dd.get("connection_verified"))
    has_backend = bool(dd.get("_backend"))
    return is_verified or has_backend


def cloudwatch_is_available(sources: dict[str, dict]) -> bool:
    """Check if CloudWatch is verified."""
    return bool(sources.get("cloudwatch", {}).get("connection_verified"))
