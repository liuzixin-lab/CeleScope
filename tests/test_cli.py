# -*- coding: utf-8 -*-


from celescope import cli


def test_cli_template():
    assert cli.cli() is None
