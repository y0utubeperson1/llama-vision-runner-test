#!/bin/bash

if [ -f "/app/.nomodelbuild" ]; then
    echo "Downloading model during runtime..."
    ollama serve & (while ! ollama list | grep -q "NAME"; do sleep 1; done) && ollama pull gemma3:4b
fi

ollama serve & while ! ollama list | grep -q "NAME"; do sleep 1; done
python test_script.py 