@echo off

REM This Batch file is attempting to pull serial and DXDIAG logs, 
REM combine them, and output to a new .txt file.
REM The intention is to save time during DVT by making OS Testing
REM more automated.

REM set both files to output as TEMP until combination
set "output_file=Windows_OS_Test.txt"

REM get baseboard serial and output
echo "############### S E R I A L   C H E C K ###############"
echo ############### S E R I A L   C H E C K ############### >> %output_file%
wmic baseboard get serialnumber > "%output_file%"

REM run DxDiag and output
echo "############### D X D I A G ###############"
echo ############### D X D I A G ############### >> %output_file%
dxdiag /t >> %output_file%


echo "############### P I N G   T E S T ###############"
echo ############### P I N G   T E S T ############### >> %output_file%
REM perform ping Test
ping www.google.com >> %output_file%

REM Open Device Manager for Device Bang Check
echo "############### D E V I C E   M A N A G E R ###############"
echo ############### D E V I C E   M A N A G E R ############### >> %output_file%
start devmgmt.msc