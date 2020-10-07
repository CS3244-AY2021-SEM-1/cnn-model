#!/usr/bin/env bash

jupyter notebook "$@" --port=8889 && tensorboard --logdir=output/tensorboard/runs --bind_all