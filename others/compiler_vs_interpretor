# Compiler vs Interpretor

## Compiler
- Converts the entire source code to machine code (high level to low level) 
- Conversion may be time consuming, but running the converted code is fast
- C, C++, Go, Rust
- Requires recompilation after code edit

```c++
g++ a.cpp -o test.out  // Need to recompile when there is change in code
./test.out // Run executable file
```

## Interpretor
- Converts and runs source code to machine code line by line
- Fast in the beginning as there is no compilation time, but may take longer for the whole code to execute
- Python
- Does not need recompilation after code edit

```c++
python a.py // runs directly without having to compile and get an executable
```

## JIT Compiler
A mix of compiler and interpretor. Faster due to use of hot spots but uses more memory as compiled codes are cached in memory. 
1. Code Analysis: Scans for hot spots (code which is executed most frequently).
2. Dynamic Compilation: JIT compiler for hot code, interpretor for the rest of code. Done in runtime.
3. Optimization: Use various techniques during compilation (minimize gc overhead, analysis memory access pattern, etc)
4. Execution: Execute machine code. When new hot spots are found, they are also optimized via JIT compiler

JVM, .NET, V8 (node.js).
