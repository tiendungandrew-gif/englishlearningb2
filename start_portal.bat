@echo off
title Learning B2 Portal
echo ===================================================
echo     DANG KHOI CHAY LEARNING B2 PORTAL
echo ===================================================
echo.
echo Mo trinh duyet tai: http://localhost:8080
echo Nhan Ctrl + C trong cua so nay neu muon dung may chu.
echo.
start "" "http://localhost:8080"
python -m http.server 8080
pause
