@echo off
set HISTORY=history_1
set INPUT=input_1
copy "History\CR\%HISTORY%.xlsx" history.xlsx
copy "Input\CR\%INPUT%.xlsx" input.xlsx
IF EXIST history.xlsx (
    CALL python Main.py
    echo DONE!
	del history.xlsx 
	del input.xlsx
	move output.xlsx "Output\CR\%HISTORY%_out.xlsx"
) ELSE (
    CLS
    echo No File!
    pause > nul
    exit
)


set HISTORY=history_2
set INPUT=input_2
copy "History\CR\%HISTORY%.xlsx" history.xlsx
copy "Input\CR\%INPUT%.xlsx" input.xlsx
IF EXIST history.xlsx (
    CALL python Main.py
    echo DONE!
	del history.xlsx 
	del input.xlsx
	move output.xlsx "Output\CR\%HISTORY%_out.xlsx"
) ELSE (
    CLS
    echo No File!
    pause > nul
    exit
)

set HISTORY=history_3
set INPUT=input_3
copy "History\CR\%HISTORY%.xlsx" history.xlsx
copy "Input\CR\%INPUT%.xlsx" input.xlsx
IF EXIST history.xlsx (
    CALL python Main.py
    echo DONE!
	del history.xlsx 
	del input.xlsx
	move output.xlsx "Output\CR\%HISTORY%_out.xlsx"
) ELSE (
    CLS
    echo No File!
    pause > nul
    exit
)

set HISTORY=history_4
set INPUT=input_4
copy "History\CR\%HISTORY%.xlsx" history.xlsx
copy "Input\CR\%INPUT%.xlsx" input.xlsx
IF EXIST history.xlsx (
    CALL python Main.py
    echo DONE!
	del history.xlsx 
	del input.xlsx
	move output.xlsx "Output\CR\%HISTORY%_out.xlsx"
) ELSE (
    CLS
    echo No File!
    pause > nul
    exit
)

set HISTORY=history_5
set INPUT=input_5
copy "History\CR\%HISTORY%.xlsx" history.xlsx
copy "Input\CR\%INPUT%.xlsx" input.xlsx
IF EXIST history.xlsx (
    CALL python Main.py
    echo DONE!
	del history.xlsx 
	del input.xlsx
	move output.xlsx "Output\CR\%HISTORY%_out.xlsx"
) ELSE (
    CLS
    echo No File!
    pause > nul
    exit
)

set HISTORY=history_6
set INPUT=input_6
copy "History\CR\%HISTORY%.xlsx" history.xlsx
copy "Input\CR\%INPUT%.xlsx" input.xlsx
IF EXIST history.xlsx (
    CALL python Main.py
    echo DONE!
	del history.xlsx 
	del input.xlsx
	move output.xlsx "Output\CR\%HISTORY%_out.xlsx"
) ELSE (
    CLS
    echo No File!
    pause > nul
    exit
)

set HISTORY=history_7
set INPUT=input_7
copy "History\CR\%HISTORY%.xlsx" history.xlsx
copy "Input\CR\%INPUT%.xlsx" input.xlsx
IF EXIST history.xlsx (
    CALL python Main.py
    echo DONE!
	del history.xlsx 
	del input.xlsx
	move output.xlsx "Output\CR\%HISTORY%_out.xlsx"
) ELSE (
    CLS
    echo No File!
    pause > nul
    exit
)

set HISTORY=history_8
set INPUT=input_8
copy "History\CR\%HISTORY%.xlsx" history.xlsx
copy "Input\CR\%INPUT%.xlsx" input.xlsx
IF EXIST history.xlsx (
    CALL python Main.py
    echo DONE!
	del history.xlsx 
	del input.xlsx
	move output.xlsx "Output\CR\%HISTORY%_out.xlsx"
) ELSE (
    CLS
    echo No File!
    pause > nul
    exit
)

set HISTORY=history_9
set INPUT=input_9
copy "History\CR\%HISTORY%.xlsx" history.xlsx
copy "Input\CR\%INPUT%.xlsx" input.xlsx
IF EXIST history.xlsx (
    CALL python Main.py
    echo DONE!
	del history.xlsx 
	del input.xlsx
	move output.xlsx "Output\CR\%HISTORY%_out.xlsx"
) ELSE (
    CLS
    echo No File!
    pause > nul
    exit
)



pause > nul
exit