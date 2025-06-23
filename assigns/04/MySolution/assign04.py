# Task 2
import sys
sys.setrecursionlimit(10000)

class treg:
    prfx = ""
    ntmp = 100
    nfun = 100
    def __init__(self, prfx, sffx):
        self.prfx = prfx; self.sffx = sffx
    def __str__(self):
        return ("treg(" + self.prfx + str(self.sffx) + ")")

def targ_new():
    return treg("arg", 0)
def ttmp_new():
    treg.ntmp += 1
    return treg("tmp", treg.ntmp)
def tfun_new():
    treg.nfun += 1
    return treg("fun", treg.nfun)

class tval:
    ctag = ""
    def __str__(self):
        return ("tval(" + self.ctag + ")")

class tval_int(tval):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TVALint"
    def __str__(self):
        return ("TVALint(" + str(self.arg1) + ")")

class tval_btf(tval):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TVALbtf"
    def __str__(self):
        return ("TVALbtf(" + str(self.arg1) + ")")

class tins:
    ctag = ""
    def __str__(self):
        return ("tins(" + self.ctag + ")")

class tins_mov(tins):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TINSmov"
    def __str__(self):
        return ("tins_mov(" + str(self.arg1) + ";" + str(self.arg2) + ")")

class tins_opr(tins):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TINSopr"
    def __str__(self):
        regs_str = "[" + ", ".join(str(r) for r in self.arg3) + "]"
        return ("tins_opr(" + str(self.arg1) + ";" + str(self.arg2) + ";" + regs_str + ")")

class tins_app(tins):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TINSapp"
    def __str__(self):
        return ("tins_app(" + str(self.arg1) + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")

class tins_if0(tins):
    def __init__(self, arg1, arg2, arg3, arg4):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.ctag = "TINSif0"
    def __str__(self):
        return ("tins_if0(" + str(self.arg1) + ";" + str(self.arg2) + ";" + str(self.arg3) + ";" + str(self.arg4) + ")")

class tins_fun(tins):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TINSfun"
    def __str__(self):
        return ("tins_fun(" + str(self.arg1) + ";" + str(self.arg2) + ")")

class tcmp:
    def __init__(self, inss, treg):
        self.arg1 = inss; self.arg2 = treg
    def __str__(self):
        return ("tcmp([" + ", ".join(str(ins) for ins in self.arg1) + "], " + str(self.arg2) + ")")


def isPrime_comp():
    """
    Manual translation of:
    fun isPrime(n: int): bool =
    let
      fun helper(p: int): bool =
        if p * p > n
        then true else
        (if n % p = 0 then false else helper(p+1))
    in
      if n >= 2 then helper(2) else false
    end
    """
    
    # Main function isPrime
    fun_isPrime = tfun_new()  # fun101
    arg_n = targ_new()        # arg0 - parameter n
    
    # Inner function helper 
    fun_helper = tfun_new()   # fun102  
    arg_p = targ_new()        # arg0 - parameter p (reused)
    
    # Helper function body compilation:
    # if p * p > n then true else (if n % p = 0 then false else helper(p+1))
    
    # p * p
    tmp1 = ttmp_new()  # tmp101
    ins1 = tins_opr(tmp1, "*", [arg_p, arg_p])
    
    # p * p > n  
    tmp2 = ttmp_new()  # tmp102
    ins2 = tins_opr(tmp2, ">", [tmp1, arg_n])
    
    # Inner if: n % p = 0
    tmp3 = ttmp_new()  # tmp103
    ins3 = tins_opr(tmp3, "%", [arg_n, arg_p])
    
    tmp4 = ttmp_new()  # tmp104
    ins4 = tins_mov(tmp4, tval_int(0))
    
    tmp5 = ttmp_new()  # tmp105
    ins5 = tins_opr(tmp5, "=", [tmp3, tmp4])
    
    # helper(p+1)
    tmp6 = ttmp_new()  # tmp106
    ins6 = tins_mov(tmp6, tval_int(1))
    
    tmp7 = ttmp_new()  # tmp107
    ins7 = tins_opr(tmp7, "+", [arg_p, tmp6])
    
    tmp8 = ttmp_new()  # tmp108
    ins8 = tins_app(tmp8, fun_helper, tmp7)
    
    # false
    tmp9 = ttmp_new()  # tmp109
    ins9 = tins_mov(tmp9, tval_btf(False))
    
    # Inner if: if n % p = 0 then false else helper(p+1)
    tmp10 = ttmp_new()  # tmp110
    then_branch_inner = tcmp([ins8], tmp8)  # helper(p+1)
    else_branch_inner = tcmp([ins9], tmp9)  # false
    ins10 = tins_if0(tmp10, tmp5, else_branch_inner, then_branch_inner)
    
    # true
    tmp11 = ttmp_new()  # tmp111
    ins11 = tins_mov(tmp11, tval_btf(True))
    
    # Outer if: if p * p > n then true else (inner if)
    tmp12 = ttmp_new()  # tmp112
    then_branch_outer = tcmp([ins11], tmp11)  # true
    else_branch_outer = tcmp([ins3, ins4, ins5, ins6, ins7, ins10], tmp10)  # inner if
    ins12 = tins_if0(tmp12, tmp2, then_branch_outer, else_branch_outer)
    
    # Helper function definition
    helper_body = tcmp([ins1, ins2, ins12], tmp12)
    helper_def = tins_fun(fun_helper, helper_body)
    
    # Main isPrime body: if n >= 2 then helper(2) else false
    
    # n >= 2
    tmp13 = ttmp_new()  # tmp113
    ins13 = tins_mov(tmp13, tval_int(2))
    
    tmp14 = ttmp_new()  # tmp114
    ins14 = tins_opr(tmp14, ">=", [arg_n, tmp13])
    
    # helper(2)
    tmp15 = ttmp_new()  # tmp115
    ins15 = tins_app(tmp15, fun_helper, tmp13)
    
    # false
    tmp16 = ttmp_new()  # tmp116
    ins16 = tins_mov(tmp16, tval_btf(False))
    
    # Main if: if n >= 2 then helper(2) else false
    tmp17 = ttmp_new()  # tmp117
    then_branch_main = tcmp([ins15], tmp15)  # helper(2)
    else_branch_main = tcmp([ins16], tmp16)  # false
    ins17 = tins_if0(tmp17, tmp14, then_branch_main, else_branch_main)
    
    # isPrime function definition
    isPrime_body = tcmp([helper_def, ins13, ins14, ins17], tmp17)
    isPrime_def = tins_fun(fun_isPrime, isPrime_body)
    
    return tcmp([isPrime_def], fun_isPrime)

if __name__ == "__main__":
    print(isPrime_comp())