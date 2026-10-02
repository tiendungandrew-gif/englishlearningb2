@echo off
title VSTEP B2 Master Portal
echo ===================================================
echo     DANG KHOI CHAY VSTEP B2 MASTER LEARNING PORTAL
echo ===================================================
echo.
echo Mo trinh duyet tai: http://localhost:8080
echo Nhan Ctrl + C trong cua so nay neu muon dung may chu.
echo.
start "" "http://localhost:8080"
python -m http.server 8080
pause
