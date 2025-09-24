"""
Tap configuration related stuff
"""

from __future__ import annotations

from voluptuous import All, Optional, Required, Schema

# Define the table schema separately
TABLE_SCHEMA = Schema({
    Required("table_name"): str,
    Required("search_pattern"): str,
    Optional("key_properties"): [str],
    Optional("search_prefix"): str,
    Optional("date_overrides"): [str],
    Optional("string_overrides"): [str],
    Optional("datatype_overrides"): object,
    Optional("guess_types"): bool,
    Optional("delimiter"): str,
    Optional("table_suffix"): str,
    Optional("remove_character"): str,
    Optional("s3_proxies"): object,
    Optional("encoding"): str,
    Optional("set_empty_values_null"): bool,
    Optional("escapechar"): str,
})

# Use All() to validate each item in the list
CONFIG_CONTRACT = Schema(All([TABLE_SCHEMA]))
