# GDB

- Full name: GNU Debugger
- A debugging tool for UNIX and UNIX-like systems
- Can debug C, C++, asm, minimal, D, Fortran, Objective-C, Go, Java, Pascal

## Start Debugging

- `gdb file`: Add the executable file after gdb
- After seeing `(gdb)`, you can use gdb debugging commands

## Debugging After Program Runs

- `gdb attach pid`: The parameter pid is the program's **process id**
 - Use the ps command to get the **process id**

## Debugging After gdb

- `r`: Start the program
- `c`: Continue execution
- `l`: View source code
- `b`: Set breakpoint
- `rb`: Set breakpoint matching regular expression
- `p`: View variable name
 - `set print pretty`: Beautify print
  
### Set Breakpoint

- `break file:line`: Set breakpoint at line number in executable file
- `break +/-num`: Set offset, set breakpoint num lines above/below current line
- `break file:line if i == 0`: When executing to line, if i == 0, then interrupt program
- `break func if a == 0`: When calling function func, if parameter a == 0, then terminate program
- `break function_name`: Pause program when calling function
 - For multiple classes with inheritance, since virtual functions are also same-named functions, as long as function name matches, breakpoints will be set
 - `break class1::func1`: Use scope operator to specify which class member function to set breakpoint
 - `break func(int)`: Set breakpoint at function named func with int parameter
- `rbreak regular_expression`: Set breakpoint before function names matching regular expression
- `break *0x0000f`: Set breakpoint at instruction address
- `tbreak file:line/func`: Set temporary breakpoint
- `info b`: View breakpoint number
- `disable breakNum` 禁用断点
- `enable breakNum` 启用断点

### 查看变量

- `print variable_name` 查看变量variable_name的值
- `display variable_name` 每次程序中断时显示变量variable_name的值

### problem

- [Cannot evaluate function -- may be inlined](https://stackoverflow.com/questions/22163730/cannot-evaluate-function-may-be-inlined)