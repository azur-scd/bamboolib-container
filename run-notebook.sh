#!/bin/bash
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

jupyter notebook --notebook-dir="./bamboolib-notebooks" --ip=0.0.0.0 --no-browser --allow-root --port=8888 --NotebookApp.token='123456' --NotebookApp.base_url='/bamboolib-notebooks'