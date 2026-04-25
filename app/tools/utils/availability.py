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
    """Available when real EKS credentials are present OR a fixture backend is injected."""
    eks = sources.get("eks", {})
    return bool(eks.get("connection_verified") or eks.get("_backend"))


def datadog_available_or_backend(sources: dict[str, dict]) -> bool:
    """Available when real Datadog credentials are present OR a fixture backend is injected."""
    dd = sources.get("datadog", {})
    return bool(dd.get("connection_verified") or dd.get("_backend"))


def cloudwatch_is_available(sources: dict[str, dict]) -> bool:
    """Available when real CloudWatch credentials are present OR a fixture backend is injected."""
    cw = sources.get("cloudwatch", {})
    return bool(cw.get("connection_verified") or cw.get("_backend"))
