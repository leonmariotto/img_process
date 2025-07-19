#!/usr/bin/env python3

from scripts.DataStore import DataStore, Key


def test_add_entry():
    ds = DataStore()
    ds.add_entry([Key.BORDER, Key.SIZE], "10")
    assert ds.data["border;size"] == "10"


def test_get_entry():
    ds = DataStore()
    ds.add_entry([Key.BORDER, Key.SIZE], "10")
    ent = ds.get_entry([Key.BORDER, Key.SIZE])
    assert ent == "10"
