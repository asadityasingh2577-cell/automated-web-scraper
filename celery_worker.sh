#!/usr/bin/env bash
# Make sure Redis is running first
celery -A tasks.celery_app worker --loglevel=info -B
