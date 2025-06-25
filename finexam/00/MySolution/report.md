# Compiler Implementation Report

## 1. Introduction and Motivation

As a student with limited prior compiler experience and knowledge about functional programming, this project provided an excellent opportunity to understand the fundamental concepts of language translation and code generation. 

### 1.1 Compiler Architecture Overview

The implemented compiler follows a traditional multi-phase design:
1. **Compilation Phase**: Translates LAMBDA terms into an intermediate representation (term_comp00)
2. **Code Generation Phase**: Converts the intermediate representation to executable Python code (tcmp_pyemit)

## 2. Task 1: Intermediate Code Generation

To test it:
```shell
python3 finexam.py
```

### 2.1 Completion of Missing Cases

In task1 of this final exam, I need to complete the implementation `term_comp01`. Almost code has already finished according to lecture-06-18/lambda3.py, so I only need to implement TMtup, TMfst, TMsnd, TMlet, and TMopr.


**TMtup Implementation:**
```python
if (tm0.ctag == "TMtup"):
    cmp1 = term_comp01(tm0.arg1, cenv)
    cmp2 = term_comp01(tm0.arg2, cenv)
    ins1 = cmp1.arg1
    tmp1 = cmp1.arg2
    ins2 = cmp2.arg1
    tmp2 = cmp2.arg2
    ttmp = ttmp_new()
    inss = ins1 + ins2 + [tins_tup(ttmp, tmp1, tmp2)]
    return tcmp(inss, ttmp)
```

This implementation compiles both tuple elements, combines their instruction sequences, and generates a tuple creation instruction.

**TMfst and TMsnd Implementation:**
These operators extract the first and second elements of tuples, respectively. The implementation follows a similar pattern of compiling the tuple expression and generating appropriate extraction instructions.

```python
if (tm0.ctag == "TMfst"):
    cmp1 = term_comp01(tm0.arg1, cenv)
    ins1 = cmp1.arg1
    tmp1 = cmp1.arg2
    ttmp = ttmp_new()
    inss = ins1 + [tins_fst(ttmp, tmp1)]
    return tcmp(inss, ttmp)
if (tm0.ctag == "TMsnd"):
    cmp1 = term_comp01(tm0.arg1, cenv)
    ins1 = cmp1.arg1
    tmp1 = cmp1.arg2
    ttmp = ttmp_new()
    inss = ins1 + [tins_snd(ttmp, tmp1)]
    return tcmp(inss, ttmp)
```

**TMlet Implementation:**

Let expressions provide local variable binding. The implementation creates a new environment entry mapping the variable name to its compiled result:

```python
if (tm0.ctag == "TMlet"):
    x01 = tm0.arg1
    cmp1 = term_comp01(tm0.arg2, cenv)
    ins1 = cmp1.arg1
    tmp1 = cmp1.arg2
    cenv = cenv_cons(x01, tmp1, cenv)
    cmp2 = term_comp01(tm0.arg3, cenv)
    ins2 = cmp2.arg1
    tmp2 = cmp2.arg2
    inss = ins1 + ins2
    return tcmp(inss, tmp2)
```

**TMopr Implementation:**

I implemented comprehensive support for arithmetic operators (-, *, /, %), comparison operators (!=, >=, <=), logical operators (and), and utility functions (abs). Each operator follows a consistent pattern of compiling operands and generating appropriate instruction sequences.

First of all, following the pattern of previous lectures, I use lambda to create TMopr function

```python
term_add = lambda a1, a2: term_opr("+", [a1, a2])
term_sub = lambda a1, a2: term_opr("-", [a1, a2])
term_mul = lambda a1, a2: term_opr("*", [a1, a2])
term_div = lambda a1, a2: term_opr("/", [a1, a2])
term_mod = lambda a1, a2: term_opr("%", [a1, a2])
term_lt0 = lambda a1, a2: term_opr("<", [a1, a2])
term_gt0 = lambda a1, a2: term_opr(">", [a1, a2])
term_eq0 = lambda a1, a2: term_opr("=", [a1, a2])
term_lte = lambda a1, a2: term_opr("<=", [a1, a2])
term_gte = lambda a1, a2: term_opr(">=", [a1, a2])
term_neq = lambda a1, a2: term_opr("!=", [a1, a2])
term_cmp = lambda a1, a2: term_opr("cmp", [a1, a2])
term_and = lambda a1, a2: term_opr("and", [a1, a2])
term_abs = lambda a1: term_opr("abs", [a1])
term_print = lambda a1: term_opr("print", [a1])

```

Then complete the code in TMopr case of `term_comp01`:

```python
        if (pnm == "-"):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "-", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "*"):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "*", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "<"):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "<", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == ">"):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, ">", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "="):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "=", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "<="):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "<=", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == ">="):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, ">=", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "!="):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "!=", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "cmp"):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "cmp", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "/"):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "/", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "%"):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "%", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "and"):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "and", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "abs"):
            assert len(ags) == 1
            cmp1 = term_comp01(ags[0], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ttmp = ttmp_new()
            inss = ins1 + [tins_opr(ttmp, "abs", [tmp1])]
            return tcmp(inss, ttmp)
        if (pnm == "print"):
            assert len(ags) == 1
            cmp1 = term_comp01(ags[0], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ttmp = ttmp_new()
            inss = ins1 + [tins_opr(ttmp, "print", [tmp1])]
            return tcmp(inss, ttmp)

```

### 2.2 Variable Scoping Problem Fix

A potencial bug was discovered and fixed in the nested lambda function compilation. The original implementation used generic `arg0` registers for all parameters, causing variable name conflicts in nested functions. The fix involved:

Original code:

```python
if (tm0.ctag == "TMlam"):
    x01 = tm0.arg1
    fun0 = tfun_new()
    arg0 = targ_new()
    cenv = cenv_cons(x01, arg0, cenv)
    cmp1 = term_comp01(tm0.arg3, cenv)
    inss = [tins_fun(fun0, cmp1)]
    return tcmp(inss, fun0)
```

Here `arg0 = targ_new()` could be wrong in nested lambda function compilation. E.g.:
```python
safety_test1 = term_lam(
    "i0", styp_int,
    term_lam(
        "j0", styp_int,
        term_lam(
            "i", styp_int,
            term_lam(
                "j", styp_int,
                term_and(
                    term_neq(var_j0, var_j),
                    term_neq(
                        term_abs(
                            term_sub(var_i0, var_i)
                        ),
                        term_abs(
                            term_sub(var_j0, var_j),
                        )
                    ),
                )
            )
        )
    )
)

safety_test1_comp = term_comp00(safety_test1)
print("Python Code for safety_test1")
print(tcmp_pyemit(safety_test1_comp))
print()
```
The output is:
```shell
def fun112(i0):
    # Generated Python code from LAMBDA compilation
    def fun113(j0):
        # Generated Python code from LAMBDA compilation
        def fun114(i):
            # Generated Python code from LAMBDA compilation
            def fun115(j):
                # Generated Python code from LAMBDA compilation
                tmp385 = j != j
                tmp386 = j - j
                tmp387 = abs(tmp386)
                tmp388 = j - j
                tmp389 = abs(tmp388)
                tmp390 = tmp387 != tmp389
                tmp391 = tmp385 and tmp390
                # Result is in tmp391
                return tmp391
            # Result is in fun115
            return fun115
        # Result is in fun114
        return fun114
    # Result is in fun113
    return fun113
# Result is in fun112
return fun112
```
The logic inside fun115 is not correct.

The fixed version is:
```python
if (tm0.ctag == "TMlam"):
    x01 = tm0.arg1
    fun0 = tfun_new()
    # Create a parameter register with the actual parameter name
    param_reg = treg(x01, 0)  # Use parameter name as prefix
    cenv = cenv_cons(x01, param_reg, cenv)
    cmp1 = term_comp01(tm0.arg3, cenv)
    inss = [tins_fun(fun0, cmp1, x01)]  # Pass parameter name
    return tcmp(inss, fun0)
```

We need use `param_reg = treg(x01, 0)` to fetch actual parameter name. After this modification, the output is:
```shell
def fun112(i0):
    # Generated Python code from LAMBDA compilation
    def fun113(j0):
        # Generated Python code from LAMBDA compilation
        def fun114(i):
            # Generated Python code from LAMBDA compilation
            def fun115(j):
                # Generated Python code from LAMBDA compilation
                tmp385 = j0 != j
                tmp386 = i0 - i
                tmp387 = abs(tmp386)
                tmp388 = j0 - j
                tmp389 = abs(tmp388)
                tmp390 = tmp387 != tmp389
                tmp391 = tmp385 and tmp390
                # Result is in tmp391
                return tmp391
            # Result is in fun115
            return fun115
        # Result is in fun114
        return fun114
    # Result is in fun113
    return fun113
# Result is in fun112
```
The problem was fixed.

## 3. Task 2: Python Code Generation

I have already copy the generated Python code of `search` function in midterm/01/MySolution/midterm.py into the test.py file

To test it:
```shell
python3 test.py
```

### 3.1 Implementation Strategy

The `tcmp_pyemit` function translates intermediate representations into executable Python code. The implementation handles:

- **Instruction Translation**: Each intermediate instruction maps to corresponding Python statements
- **Register Management**: Temporary variables are properly named and managed
- **Control Flow**: Conditional expressions and function calls are correctly translated
- **Parameter Mapping**: Function parameters maintain their original names in generated code

```python
def tcmp_pyemit(comp, param_mapping=None):
    """
    Takes a tcmp (computation) object and emits Python code that implements it.
    Returns a string containing the Python code.
    param_mapping: dict mapping register names to parameter names
    """
    if not isinstance(comp, tcmp):
        raise TypeError("Expected tcmp object")
    
    if param_mapping is None:
        param_mapping = {}
    
    instructions = comp.arg1
    result_reg = comp.arg2
    
    # Generate Python code
    code_lines = []
    code_lines.append("# Generated Python code from LAMBDA compilation")
    code_lines.append("")
    
    # Process each instruction
    for ins in instructions:
        code_line = tins_pyemit(ins, param_mapping)
        if code_line:
            code_lines.append(code_line)
    
    # Return the result
    result_name = param_mapping.get(f"{result_reg.prfx}{result_reg.sffx}", f"{result_reg.prfx}{result_reg.sffx}")
    code_lines.append(f"# Result is in {result_name}")
    code_lines.append(f"return {result_name}")
    
    return "\n".join(code_lines)
```

To process each instruction, we extract the `tins_pyemit` function, but it's too long to put in this report, so please access finexam/00/MySolution/finexam.py for the details.

Inside `tins_pyemit`, the main logic is how to deal with different type of `tins`:

**TINSmov Implementation:**
```python
if ins.ctag == "TINSmov":
    dst_reg = ins.arg1
    src_val = ins.arg2
    dst_name = get_name(dst_reg)
    
    if src_val.ctag == "TVALint":
        return f"{dst_name} = {src_val.arg1}"
    elif src_val.ctag == "TVALbtf":
        return f"{dst_name} = {str(src_val.arg1)}"
    else:
        return f"{dst_name} = {src_val}"
```

**TINSopr Implementation:**
```python
elif ins.ctag == "TINSopr":
    res_reg = ins.arg1
    opr = ins.arg2
    args = ins.arg3
    res_name = get_name(res_reg)
    
    if len(args) == 2:
        arg1_name = get_name(args[0])
        arg2_name = get_name(args[1])
        
        if opr == "+":
            return f"{res_name} = {arg1_name} + {arg2_name}"
        elif opr == "-":
            return f"{res_name} = {arg1_name} - {arg2_name}"
        
        # Other operations ...
```

**TINSapp Implementation:**
```python
elif ins.ctag == "TINSapp":
    res_reg = ins.arg1
    fun_reg = ins.arg2
    arg_reg = ins.arg3
    res_name = get_name(res_reg)
    fun_name = get_name(fun_reg)
    arg_name = get_name(arg_reg)
    return f"{res_name} = {fun_name}({arg_name})"
```

**TINSfun Implementation:**
```python
elif ins.ctag == "TINSfun":
    fun_reg = ins.arg1
    body_comp = ins.arg2
    param_name = ins.arg3 if ins.arg3 else "arg0"  # Use original parameter name
    fun_name = get_name(fun_reg)
    
    # Create parameter mapping for the function body
    body_param_mapping = param_mapping.copy()
    body_param_mapping["arg0"] = param_name  # Map arg0 to the actual parameter name
    body_param_mapping[f"{param_name}0"] = param_name  # Map parameter register to parameter name
    
    # Generate function definition
    body_code = tcmp_pyemit(body_comp, body_param_mapping)
    # Indent the body code
    indented_body = "\n".join("    " + line for line in body_code.split("\n") if line.strip())
    
    return f"def {fun_name}({param_name}):\n{indented_body}"
```

**TINSif0 Implementation:**

```python
elif ins.ctag == "TINSif0":
    res_reg = ins.arg1
    test_reg = ins.arg2
    then_comp = ins.arg3
    else_comp = ins.arg4
    res_name = get_name(res_reg)
    test_name = get_name(test_reg)
    
    then_code = tcmp_pyemit(then_comp, param_mapping)
    else_code = tcmp_pyemit(else_comp, param_mapping)
    
    # Indent the branch codes
    indented_then = "\n".join("    " + line for line in then_code.split("\n") if line.strip())
    indented_else = "\n".join("    " + line for line in else_code.split("\n") if line.strip())
    
    then_result_name = param_mapping.get(f"{then_comp.arg2.prfx}{then_comp.arg2.sffx}", f"{then_comp.arg2.prfx}{then_comp.arg2.sffx}")
    return f"if {test_name}:\n{indented_then}\nelse:\n{indented_else}\n{res_name} = {then_result_name}"

```