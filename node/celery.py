#!/usr/bin/env python

from __future__ import absolute_import
from celery import Celery
from node import celeryconfig

app = Celery()
app.config_from_object(celeryconfig)

if __name__ == '__main__':
	app.start()

