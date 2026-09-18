@echo off
title AgriFlow Server
echo ==============================================================
echo Starting AgriFlow - Agricultural Produce Discovery Platform
echo URL: http://127.0.0.1:8000
echo ==============================================================
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
pause
