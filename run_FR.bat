@echo off
set HISTORY=history_4
set INPUT=input_4
copy "History\FR\%HISTORY%.xlsx" history.xlsx
copy "Input\FR\%INPUT%.xlsx" input.xlsx
IF EXIST history.xlsx (
    CALL python Main.py
    echo DONE!
	del history.xlsx 
	del input.xlsx
	move output.xlsx "Output\FR\%HISTORY%_out.xlsx"
) ELSE (
    CLS
    echo No File!
    pause > nul
    exit
)


set HISTORY=history_8
set INPUT=input_8
copy "History\FR\%HISTORY%.xlsx" history.xlsx
copy "Input\FR\%INPUT%.xlsx" input.xlsx
IF EXIST history.xlsx (
    CALL python Main.py
    echo DONE!
	del history.xlsx 
	del input.xlsx
	move output.xlsx "Output\FR\%HISTORY%_out.xlsx"
) ELSE (
    CLS
    echo No File!
    pause > nul
    exit
)


set HISTORY=history_12
set INPUT=input_12
copy "History\FR\%HISTORY%.xlsx" history.xlsx
copy "Input\FR\%INPUT%.xlsx" input.xlsx
IF EXIST history.xlsx (
    CALL python Main.py
    echo DONE!
	del history.xlsx 
	del input.xlsx
	move output.xlsx "Output\FR\%HISTORY%_out.xlsx"
) ELSE (
    CLS
    echo No File!
    pause > nul
    exit
)


set HISTORY=history_15
set INPUT=input_15
copy "History\FR\%HISTORY%.xlsx" history.xlsx
copy "Input\FR\%INPUT%.xlsx" input.xlsx
IF EXIST history.xlsx (
    CALL python Main.py
    echo DONE!
	del history.xlsx 
	del input.xlsx
	move output.xlsx "Output\FR\%HISTORY%_out.xlsx"
) ELSE (
    CLS
    echo No File!
    pause > nul
    exit
)


set HISTORY=history_18
set INPUT=input_18
copy "History\FR\%HISTORY%.xlsx" history.xlsx
copy "Input\FR\%INPUT%.xlsx" input.xlsx
IF EXIST history.xlsx (
    CALL python Main.py
    echo DONE!
	del history.xlsx 
	del input.xlsx
	move output.xlsx "Output\FR\%HISTORY%_out.xlsx"
) ELSE (
    CLS
    echo No File!
    pause > nul
    exit
)


set HISTORY=history_21
set INPUT=input_21
copy "History\FR\%HISTORY%.xlsx" history.xlsx
copy "Input\FR\%INPUT%.xlsx" input.xlsx
IF EXIST history.xlsx (
    CALL python Main.py
    echo DONE!
	del history.xlsx 
	del input.xlsx
	move output.xlsx "Output\FR\%HISTORY%_out.xlsx"
) ELSE (
    CLS
    echo No File!
    pause > nul
    exit
)


set HISTORY=history_23
set INPUT=input_23
copy "History\FR\%HISTORY%.xlsx" history.xlsx
copy "Input\FR\%INPUT%.xlsx" input.xlsx
IF EXIST history.xlsx (
    CALL python Main.py
    echo DONE!
	del history.xlsx 
	del input.xlsx
	move output.xlsx "Output\FR\%HISTORY%_out.xlsx"
) ELSE (
    CLS
    echo No File!
    pause > nul
    exit
)

pause > nul
exit