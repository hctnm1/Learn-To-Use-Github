#! /usr/bin/python
# -*- coding: utf-8 -*-

import argparse

from ..basic.runner import PygameRunner

__author__ = 'fyabc'


class AntSpider(PygameRunner):
    def main_loop(self):
        pass

    def draw(self):
        pass

    def draw_background(self):
        pass


def real_main(options):
    pass


def build_parser():
    parser = argparse.ArgumentParser(prog='antspider', description='A simple game of ants and spiders.')

    return parser


def main():
    parser = build_parser()

    options = parser.parse_args()

    real_main(options)
