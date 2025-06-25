##################################################################
import sys
sys.setrecursionlimit(10000)
##################################################################

# datatype styp =
# | STbas of strn # int, bool, ...
# | STtup of (styp, styp) # for pairs
# | STfun of (styp, styp) # for functions

class styp:
    ctag = ""
    def __str__(self):
        return ("styp(" + self.ctag + ")")
# end-of-class(styp)

# | STbas of strn # int, bool, ...
class styp_bas:
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "STbas"
    def __str__(self):
        return ("STbas(" + self.arg1 + ")")
# end-of-class(styp_bas(styp))

styp_int = styp_bas("int")
styp_bool = styp_bas("bool")

# | STtup of (styp, styp) # for pairs
class styp_tup:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "STtup"
    def __str__(self):
        return ("STtup(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(styp_tup(styp))

styp_int2 = styp_tup(styp_int, styp_int)

# 8-tuple type for chess board (simplified as nested pairs)
styp_board = styp_tup(styp_int,
            styp_tup(styp_int,
            styp_tup(styp_int,
            styp_tup(styp_int,
            styp_tup(styp_int,
            styp_tup(styp_int,
            styp_tup(styp_int, styp_int)))))))

# | STfun of (styp, styp) # for functions
class styp_fun:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "STfun"
    def __str__(self):
        return ("STfun(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(styp_fun(styp))

styp_fun_int_int = styp_fun(styp_int, styp_int)

print("styp_int2 = " + str(styp_int2))
print("styp_fun_int_int = " + str(styp_fun_int_int))

def styp_equal(st1, st2):
    if (st1.ctag == "STbas"):
        return st2.ctag == "STbas" and st1.arg1 == st2.arg1
    if (st1.ctag == "STtup"):
        return st2.ctag == "STtup" \
            and styp_equal(st1.arg1, st2.arg1) and styp_equal(st1.arg2, st2.arg2)
    if (st1.ctag == "STfun"):
        return st2.ctag == "STfun" \
            and styp_equal(st1.arg1, st2.arg1) and styp_equal(st1.arg2, st2.arg2)
    raise TypeError(st1) # HX-2025-06-10: should be deadcode!

##################################################################

# datatype term =
# | TMint of int
# | TMbtf of bool
# | TMvar of strn
# | TMlam of (strn, styp, term)
# | TMapp of (term, term)
# | TMopr of (strn(*opr*), list(term))
# | TMif0 of (term, term, term)
# | TMfix of (strn(*f*), strn(*x*), styp, styp, term)
# | TMtup of (term, term)
# | TMfst of (term)
# | TMsnd of (term)
# | TMlet of (strn, term, term)

class term:
    ctag = ""
    def __str__(self):
        return ("term(" + self.ctag + ")")
# end-of-class(term)

# | TMint of int
class term_int(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMint"
    def __str__(self):
        return ("TMint(" + str(self.arg1) + ")")
# end-of-class(term_int(term))

# | TMbtf of bool
class term_btf(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMbtf"
    def __str__(self):
        return ("TMbtf(" + str(self.arg1) + ")")
# end-of-class(term_btf(term))

# | TMvar of strn
class term_var(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMvar"
    def __str__(self):
        return ("TMvar(" + self.arg1 + ")")
# end-of-class(term_var(term))

# | TMlam of (strn(*var*), styp, term)
class term_lam(term):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TMlam"
    def __str__(self):
        return ("TMlam(" + self.arg1 + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")
# end-of-class(term_lam(term))

# | TMapp of (term, term)
class term_app(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMapp"
    def __str__(self):
        return ("TMapp(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(term_app(term))

# | TMopr of (strn(*opr*), list(term))
class term_opr(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMopr"
    def __str__(self):
        return ("TMopr(" + self.arg1 + ";" + str(self.arg2) + ")")
# end-of-class(term_opr(term))

# | TMif0 of (term, term, term)
class term_if0(term):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TMif0"
    def __str__(self):
        return ("TMif0(" + str(self.arg1) + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")
# end-of-class(term_if0(term))

var_x = term_var("x")

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

term_dbl = term_lam("x", styp_int, term_add(var_x, var_x))
print("term_dbl = " + str(term_dbl))

# Duplicate definitions removed - using the ones defined above

# TMfix of
# (strn(*f*), strn(*x*), styp(*arg*), styp(*res*), term)
class term_fix(term):
    def __init__(self, arg1, arg2, arg3, arg4, arg5):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.arg5 = arg5
        self.ctag = "TMfix"
    def __str__(self):
        return ("TMfix(" + self.arg1 + ";" + self.arg2 + ";" + str(self.arg3) + str(self.arg4) + ";" + str(self.arg5) + ")")
# end-of-class(term_fix(term))

# | TMtup of (term, term)
class term_tup(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMtup"
    def __str__(self):
        return ("TMtup(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(term_tup(term))

# | TMfst of (term)
class term_fst(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMfst"
    def __str__(self):
        return ("TMfst(" + str(self.arg1) + ")")
# end-of-class(term_fst(term))

# | TMsnd of (term)
class term_snd(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMsnd"
    def __str__(self):
        return ("TMsnd(" + str(self.arg1) + ")")
# end-of-class(term_snd(term))

# | TMlet of (strn, term, term)
class term_let(term):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TMlet"
    def __str__(self):
        return ("TMlet(" + self.arg1 + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")
# end-of-class(term_let(term))

##################################################################

# datatype tctx =
# | CXnil of ()
# | CXcons of (strn, styp, tctx)

class tctx:
    ctag = ""
    def __str__(self):
        return ("tctx(" + self.ctag + ")")
# end-of-class(tctx)

class tctx_nil(tctx):
    def __init__(self):
        self.ctag = "CXnil"
    def __str__(self):
        return ("CXnil(" + ")")
# end-of-class(tctx_nil(tctx))

class tctx_cons(tctx):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "CXcons"
    def __str__(self):
        return ("CXcons(" + self.arg1 + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")
# end-of-class(tctx_cons(tctx))

##################################################################

# #extern
# fun
# term_tpck00(tm0: term): tval
# #extern
# fun
# term_tpck01(tm0: term, ctx: tctx): tval

def term_tpck00(tm0):
    return term_tpck01(tm0, tctx_nil())

def tctx_search(ctx, x00):
    if ctx.ctag == "CXnil":
        return None
    if ctx.ctag == "CXcons":
        if ctx.arg1 == x00:
            return ctx.arg2
        else:
            return tctx_search(ctx.arg3, x00)
    raise TypeError(ctx) # HX-2025-06-10: deadcode!

def term_tpck01(tm0, ctx):
    # print("term_tpck01: tm0 = " + str(tm0))
    if (tm0.ctag == "TMint"):
        return styp_bas("int")
    if (tm0.ctag == "TMbtf"):
        return styp_bas("bool")
    if (tm0.ctag == "TMvar"):
        st0 = tctx_search(ctx, tm0.arg1)
        assert st0 is not None
        return st0
    if (tm0.ctag == "TMlam"):
        x01 = tm0.arg1
        st1 = tm0.arg2
        tmx = tm0.arg3
        ctx = tctx_cons(x01, st1, ctx)
        stx = term_tpck01(tmx, ctx)
        return styp_fun(st1, stx)
    if (tm0.ctag == "TMapp"):
        tm1 = tm0.arg1
        tm2 = tm0.arg2
        st1 = term_tpck01(tm1, ctx)
        st2 = term_tpck01(tm2, ctx)
        assert st1.ctag == "STfun"
        assert styp_equal(st1.arg1, st2)
        return st1.arg2
    if (tm0.ctag == "TMopr"):
        pnm = tm0.arg1
        ags = tm0.arg2 # list of arguments
        if (pnm == "+"):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_int
        if (pnm == "-"):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_int
        if (pnm == "*"):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_int
        if (pnm == "<"):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_bool
        if (pnm == ">"):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_bool
        if (pnm == "="):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_bool
        if (pnm == "<="):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_bool
        if (pnm == ">="):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_bool
        if (pnm == "!="):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_bool
        if (pnm == "cmp"):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_int
        if (pnm == "/"):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_int
        if (pnm == "%"):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_int
        if (pnm == "and"):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            assert styp_equal(st1, styp_bool)
            assert styp_equal(st2, styp_bool)
            return styp_bool
        if (pnm == "abs"):
            assert len(ags) == 1
            st1 = term_tpck01(ags[0], ctx)
            assert styp_equal(st1, styp_int)
            return styp_int
        if (pnm == "print"):
            assert len(ags) == 1
            st1 = term_tpck01(ags[0], ctx)
            return styp_int  # print returns an int (like 0 for success)
        raise TypeError(pnm) # HX-2025-06-10: unsupported!
    if (tm0.ctag == "TMif0"):
        tm1 = tm0.arg1
        st1 = term_tpck01(tm1, ctx)
        assert styp_equal(st1, styp_bool)
        st2 = term_tpck01(tm0.arg2, ctx) # then
        st3 = term_tpck01(tm0.arg3, ctx) # else
        assert styp_equal(st2, st3)
        return st2
    # TMfix of
    # (strn(*f*), strn(*x*), styp(*arg*), styp(*res*), term)
    if (tm0.ctag == "TMfix"):
        f00 = tm0.arg1
        x01 = tm0.arg2
        st1 = tm0.arg3 # type for x01
        st2 = tm0.arg4 # type for tmx
        tmx = tm0.arg5
        stf = styp_fun(st1, st2) # type for f00
        ctx = tctx_cons(f00, stf, ctx)
        ctx = tctx_cons(x01, st1, ctx)
        stx = term_tpck01(tmx, ctx)
        assert styp_equal(st2, stx)
        return stf
    if (tm0.ctag == "TMtup"):
        st1 = term_tpck01(tm0.arg1, ctx)
        st2 = term_tpck01(tm0.arg2, ctx)
        return styp_tup(st1, st2)
    if (tm0.ctag == "TMfst"):
        st1 = term_tpck01(tm0.arg1, ctx)
        assert st1.ctag == "STtup"
        return st1.arg1
    if (tm0.ctag == "TMsnd"):
        st1 = term_tpck01(tm0.arg1, ctx)
        assert st1.ctag == "STtup"
        return st1.arg2
    if (tm0.ctag == "TMlet"):
        x01 = tm0.arg1
        tm1 = tm0.arg2
        tm2 = tm0.arg3
        st1 = term_tpck01(tm1, ctx)
        ctx = tctx_cons(x01, st1, ctx)
        st2 = term_tpck01(tm2, ctx)
        return st2
    raise TypeError(tm0) # HX-2025-06-10: should be deadcode!

int_invalid = term_int(-1)
int_0 = term_int(0)
int_1 = term_int(1)
int_2 = term_int(2)
btf_t = term_btf(True)
btf_f = term_btf(False)
print("tpck(int_1) = " + str(term_tpck00(int_1)))
print("tpck(btf_t) = " + str(term_tpck00(btf_t)))
print("tpck(term_add(int_1, int_1)) = " + str(term_tpck00(term_add(int_1, int_1))))
print("tpck(term_lte(int_1, int_1)) = " + str(term_tpck00(term_lte(int_1, int_1))))
# HX: this one is ill-typed:
# print("tpck(term_add(int_1, btf_t)) = " + str(term_tpck00(term_add(int_1, btf_t))))
print("tpck(term_dbl) = " + str(term_tpck00(term_dbl)))

int_0 = term_int( 0 )
int_1 = term_int( 1 )
var_f = term_var("f")
var_n = term_var("n")
int_3 = term_int(3)
int_5 = term_int(5)
int_10 = term_int(10)
term_fact = \
  term_fix("f", "n", styp_int, styp_int, \
    term_if0(term_lte(var_n, int_0), \
      int_1, \
      term_mul(var_n, term_app(var_f, term_sub(var_n, int_1)))))

print("tpck(term_fact) = " + str(term_tpck00(term_fact)))

##################################################################

CHNUM3 = \
  term_lam("f", styp_fun_int_int, \
    term_lam("x", styp_int, term_app(var_f, term_app(var_f, term_app(var_f, var_x)))))

print("tpck(CHNUM3) = " + str(term_tpck00(CHNUM3)))

##################################################################

# datatype treg =
# TREG of (strn(*prfx*), sint(*sffx*))

class treg:
    prfx = ""
    ntmp = 100
    nfun = 100
    def __init__(self, prfx, sffx):
        self.prfx = prfx; self.sffx = sffx
    def __str__(self):
        return ("treg(" + self.prfx + str(self.sffx) + ")")
# end-of-class(treg)

def targ_new():
    return treg("arg", 0)
def ttmp_new():
    treg.ntmp += 1
    return treg("tmp", treg.ntmp)
def tfun_new():
    treg.nfun += 1
    return treg("fun", treg.nfun)

# arg0 = targ_new()
# tmp1 = ttmp_new()
# tmp2 = ttmp_new()
# fun1 = tfun_new()
# fun2 = tfun_new()
# print("arg0 = " + str(arg0))
# print("tmp1 = " + str(tmp1))
# print("tmp2 = " + str(tmp2))
# print("fun1 = " + str(fun1))
# print("fun2 = " + str(fun2))

##################################################################

# datatype tval =
# | TVALint of sint
# | TVALbtf of bool
# | TVALchr of char
# | TVALstr of strn
# | TVALreg of treg

class tval:
    ctag = ""
    def __str__(self):
        return ("tval(" + self.ctag + ")")
# end-of-class(tval)

class tval_int(tval):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TVALint"
    def __str__(self):
        return ("TVALint(" + str(self.arg1) + ")")
# end-of-class(tval_int(tval))

class tval_btf(tval):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TVALbtf"
    def __str__(self):
        return ("TVALbtf(" + str(self.arg1) + ")")
# end-of-class(tval_btf(tval))

# datatype tins =
# | TINSmov of (treg(*dst*), tval(*src*))
# | TINSapp of (treg(*res*), treg(*fun*), treg(*arg*))
# | TINSopr of (treg(*res*), strn(*opr*), list(treg))
# | TINSfun of (treg(*f00*), tcmp(*body*))
# | TINSif0 of (treg(*res*), treg(*test*), tcmp(*then*), tcmp(*else*))
# | TINStup of (treg(*res*), treg(*fst*), treg(*snd*))
# | TINSfst of (treg(*res*), treg(*tup*))
# | TINSsnd of (treg(*res*), treg(*tup*))

# datatype tcmp =
# | TCMP of (list(tins), treg(*res*))

class tins:
    ctag = ""
    def __str__(self):
        return ("tins(" + self.ctag + ")")
# end-of-class(tins)

class tins_mov(tins):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TINSmov"
    def __str__(self):
        return ("tins_mov(" + str(self.arg1) + ";" + str(self.arg2) + ")")

# | TINSopr of (treg(*res*), strn(*opr*), list(treg))
class tins_opr(tins):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TINSopr"
    def __str__(self):
        return ("tins_opr(" + str(self.arg1) + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")

# | TINSapp of (treg(*res*), treg(*fun*), treg(*arg*))
class tins_app(tins):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TINSapp"
    def __str__(self):
        return ("tins_app(" + str(self.arg1) + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")

# | TINSif0 of (treg(*res*), treg(*test*), tcmp(*then*), tcmp(*else*))
class tins_if0(tins):
    def __init__(self, arg1, arg2, arg3, arg4):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.ctag = "TINSif0"
    def __str__(self):
        return ("tins_if0(" + str(self.arg1) + ";" + str(self.arg2) + ";" + str(self.arg3) + ";" + str(self.arg4) + ")")

# | TINSfun of (treg(*f00*), tcmp(*body*), strn(*param_name*))
class tins_fun(tins):
    def __init__(self, arg1, arg2, arg3=None):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3  # parameter name
        self.ctag = "TINSfun"
    def __str__(self):
        param_str = f";{self.arg3}" if self.arg3 else ""
        return ("tins_fun(" + str(self.arg1) + ";" + str(self.arg2) + param_str + ")")

# | TINStup of (treg(*res*), treg(*fst*), treg(*snd*))
class tins_tup(tins):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TINStup"
    def __str__(self):
        return ("tins_tup(" + str(self.arg1) + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")

# | TINSfst of (treg(*res*), treg(*tup*))
class tins_fst(tins):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TINSfst"
    def __str__(self):
        return ("tins_fst(" + str(self.arg1) + ";" + str(self.arg2) + ")")

# | TINSsnd of (treg(*res*), treg(*tup*))
class tins_snd(tins):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TINSsnd"
    def __str__(self):
        return ("tins_snd(" + str(self.arg1) + ";" + str(self.arg2) + ")")

# datatype tcmp =
# | TCMP of (list(tins), treg)

class tcmp:
    def __init__(self, inss, treg):
        self.arg1 = inss; self.arg2 = treg
    def __str__(self):
        return ("tcmp(" + "..." + ";" + str(self.arg2) + ")")
# end-of-class(tcmp)

##################################################################

# datatype cenv =
# | CENVnil of ()
# | CENVcons of (strn, treg, cenv)

class cenv:
    ctag = ""
    def __str__(self):
        return ("cenv(" + self.ctag + ")")
# end-of-class(cenv)

class cenv_nil(cenv):
    def __init__(self):
        self.ctag = "CENVnil"
    def __str__(self):
        return ("CENVnil(" + ")")
# end-of-class(cenv_nil(cenv))

class cenv_cons(cenv):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "CENVcons"
    def __str__(self):
        return ("CENVcons(" + self.arg1 + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")
# end-of-class(cenv_cons(cenv))

##################################################################

def term_comp00(tm0): # "computation"
    return term_comp01(tm0, cenv_nil())

def cenv_search(env, x00):
    if env.ctag == "CENVnil":
        return None
    if env.ctag == "CENVcons":
        if env.arg1 == x00:
            return env.arg2
        else:
            return cenv_search(env.arg3, x00)
    raise TypeError(env) # HX-2025-06-10: deadcode!

def term_comp01(tm0, cenv):
    if (tm0.ctag == "TMint"):
        ttmp = ttmp_new()
        ins0 = tins_mov(ttmp, tval_int(tm0.arg1))
        return tcmp([ins0], ttmp)
    if (tm0.ctag == "TMbtf"):
        ttmp = ttmp_new()
        ins0 = tins_mov(ttmp, tval_btf(tm0.arg1))
        return tcmp([ins0], ttmp)
    if (tm0.ctag == "TMvar"):
        x01 = tm0.arg1
        tmp1 = cenv_search(cenv, x01)
        if tmp1 is None:
            raise ValueError(f"Variable {x01} not found in environment")
        return tcmp([], tmp1)
    if (tm0.ctag == "TMopr"):
        pnm = tm0.arg1
        ags = tm0.arg2 # list of arguments
        if (pnm == "+"):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "+", [tmp1, tmp2])]
            return tcmp(inss, ttmp)

        ##################################################################
        # Task 1:
        ##################################################################

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
        raise TypeError(pnm) # HX-2025-06-18: unsupported!
    if (tm0.ctag == "TMapp"):
        cmp1 = term_comp01(tm0.arg1, cenv)
        cmp2 = term_comp01(tm0.arg2, cenv)
        ins1 = cmp1.arg1
        tmp1 = cmp1.arg2
        ins2 = cmp2.arg1
        tmp2 = cmp2.arg2
        ttmp = ttmp_new()
        inss = ins1 + ins2 + [tins_app(ttmp, tmp1, tmp2)]
        return tcmp(inss, ttmp)
    if (tm0.ctag == "TMif0"):
        cmp1 = term_comp01(tm0.arg1, cenv) # test
        cmp2 = term_comp01(tm0.arg2, cenv) # then
        cmp3 = term_comp01(tm0.arg3, cenv) # else
        ins1 = cmp1.arg1
        tmp1 = cmp1.arg2
        ttmp = ttmp_new()
        ins0 = tins_if0(ttmp, tmp1, cmp2, cmp3)
        inss = ins1 + [ins0]
        return tcmp(inss, ttmp)
    if (tm0.ctag == "TMlam"):
        x01 = tm0.arg1
        fun0 = tfun_new()
        # Create a parameter register with the actual parameter name
        param_reg = treg(x01, 0)  # Use parameter name as prefix
        cenv = cenv_cons(x01, param_reg, cenv)
        cmp1 = term_comp01(tm0.arg3, cenv)
        inss = [tins_fun(fun0, cmp1, x01)]  # Pass parameter name
        return tcmp(inss, fun0)
    if (tm0.ctag == "TMfix"):
        f00 = tm0.arg1
        x01 = tm0.arg2
        fun0 = tfun_new()
        arg0 = targ_new()
        cenv = cenv_cons(f00, fun0, cenv)
        cenv = cenv_cons(x01, arg0, cenv)
        cmp1 = term_comp01(tm0.arg5, cenv)
        inss = [tins_fun(fun0, cmp1, x01)]  # Pass parameter name
        return tcmp(inss, fun0)
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
    raise TypeError(tm0) # HX-2025-06-18: unsupported!

print("comp00(int_1) = " + str(term_comp00(int_1)))
print("comp00(btf_t) = " + str(term_comp00(btf_t)))
print("comp00(term_add(int_1, int_2)) = " + str(term_comp00(term_add(int_1, int_2))))
print("comp00(term_dbl) = " + str(term_comp00(term_dbl)))
print("comp00(term_fact) = " + str(term_comp00(term_fact)))

test_tup = term_tup(int_1, int_2)
print("comp00(test_tup) = " + str(term_comp00(test_tup)))

test_fst = term_fst(test_tup)
print("comp00(test_fst) = " + str(term_comp00(test_fst)))

test_snd = term_snd(test_tup)
print("comp00(test_snd) = " + str(term_comp00(test_snd)))

test_let = term_let("x", int_5, term_add(term_var("x"), int_1))
print("comp00(test_let) = " + str(term_comp00(test_let)))

# Test additional operators
test_sub = term_sub(int_5, int_2)
print("comp00(test_sub) = " + str(term_comp00(test_sub)))

test_mul = term_mul(int_2, int_3)
print("comp00(test_mul) = " + str(term_comp00(test_mul)))

test_gt = term_gt0(int_5, int_2)
print("comp00(test_gt) = " + str(term_comp00(test_gt)))

test_eq = term_eq0(int_2, int_2)
print("comp00(test_eq) = " + str(term_comp00(test_eq)))

test_neq = term_neq(int_1, int_2)
print("comp00(test_neq) = " + str(term_comp00(test_neq)))

# Test new operators
test_div = term_div(int_10, int_2)
print("comp00(test_div) = " + str(term_comp00(test_div)))

test_mod = term_mod(int_10, int_3)
print("comp00(test_mod) = " + str(term_comp00(test_mod)))

test_and = term_and(btf_t, btf_f)
print("comp00(test_and) = " + str(term_comp00(test_and)))

test_abs = term_abs(term_sub(int_2, int_5))  # abs(-3)
print("comp00(test_abs) = " + str(term_comp00(test_abs)))

test_print = term_print(int_5)
print("comp00(test_print) = " + str(term_comp00(test_print)))

##################################################################
# Task 2: Python Code Emission
##################################################################

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

def tins_pyemit(ins, param_mapping=None):
    """
    Emit Python code for a single instruction.
    param_mapping: dict mapping register names to parameter names
    """
    if param_mapping is None:
        param_mapping = {}
    
    def get_name(reg):
        """Get the appropriate name for a register, using parameter mapping if available"""
        reg_name = f"{reg.prfx}{reg.sffx}"
        return param_mapping.get(reg_name, reg_name)
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
            elif opr == "*":
                return f"{res_name} = {arg1_name} * {arg2_name}"
            elif opr == "/":
                return f"{res_name} = {arg1_name} // {arg2_name}"  # Integer division
            elif opr == "%":
                return f"{res_name} = {arg1_name} % {arg2_name}"
            elif opr == "<":
                return f"{res_name} = {arg1_name} < {arg2_name}"
            elif opr == ">":
                return f"{res_name} = {arg1_name} > {arg2_name}"
            elif opr == "=":
                return f"{res_name} = {arg1_name} == {arg2_name}"
            elif opr == "<=":
                return f"{res_name} = {arg1_name} <= {arg2_name}"
            elif opr == ">=":
                return f"{res_name} = {arg1_name} >= {arg2_name}"
            elif opr == "!=":
                return f"{res_name} = {arg1_name} != {arg2_name}"
            elif opr == "and":
                return f"{res_name} = {arg1_name} and {arg2_name}"
            elif opr == "cmp":
                return f"{res_name} = -1 if {arg1_name} < {arg2_name} else (1 if {arg1_name} > {arg2_name} else 0)"
            else:
                return f"{res_name} = {opr}({arg1_name}, {arg2_name})"
        
        elif len(args) == 1:
            arg1_name = get_name(args[0])
            
            if opr == "abs":
                return f"{res_name} = abs({arg1_name})"
            elif opr == "print":
                return f"print({arg1_name}); {res_name} = 0"
            else:
                return f"{res_name} = {opr}({arg1_name})"
    
    elif ins.ctag == "TINStup":
        res_reg = ins.arg1
        fst_reg = ins.arg2
        snd_reg = ins.arg3
        res_name = get_name(res_reg)
        fst_name = get_name(fst_reg)
        snd_name = get_name(snd_reg)
        return f"{res_name} = ({fst_name}, {snd_name})"
    
    elif ins.ctag == "TINSfst":
        res_reg = ins.arg1
        tup_reg = ins.arg2
        res_name = get_name(res_reg)
        tup_name = get_name(tup_reg)
        return f"{res_name} = {tup_name}[0]"
    
    elif ins.ctag == "TINSsnd":
        res_reg = ins.arg1
        tup_reg = ins.arg2
        res_name = get_name(res_reg)
        tup_name = get_name(tup_reg)
        return f"{res_name} = {tup_name}[1]"
    
    elif ins.ctag == "TINSapp":
        res_reg = ins.arg1
        fun_reg = ins.arg2
        arg_reg = ins.arg3
        res_name = get_name(res_reg)
        fun_name = get_name(fun_reg)
        arg_name = get_name(arg_reg)
        return f"{res_name} = {fun_name}({arg_name})"
    
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
    
    else:
        return f"# Unsupported instruction: {ins.ctag}"

# Test the Python code emission
print("\n" + "="*50)
print("Testing Python Code Emission (Task 2)")
print("="*50)

# Test simple arithmetic
test_add_comp = term_comp00(term_add(int_1, int_2))
print("Python code for 1 + 2:")
print(tcmp_pyemit(test_add_comp))
print()

test_mul_comp = term_comp00(term_mul(int_3, int_2))
print("Python code for 3 * 2:")
print(tcmp_pyemit(test_mul_comp))
print()

# Test tuple operations
test_tup_comp = term_comp00(term_tup(int_3, int_5))
print("Python code for tuple (3, 5):")
print(tcmp_pyemit(test_tup_comp))
print()

# Test tuple access
test_fst_comp = term_comp00(term_fst(term_tup(int_3, int_5)))
print("Python code for fst((3, 5)):")
print(tcmp_pyemit(test_fst_comp))
print()

# Test let expression
test_let_comp = term_comp00(term_let("x", int_5, term_add(term_var("x"), int_1)))
print("Python code for let x = 5 in x + 1:")
print(tcmp_pyemit(test_let_comp))
print()

# Test complex expression: let pair = (3, 5) in fst(pair) + snd(pair)
var_pair = term_var("pair")
test_complex = term_let("pair", term_tup(int_3, int_5), 
                       term_add(term_fst(var_pair), term_snd(var_pair)))
test_complex_comp = term_comp00(test_complex)
print("Python code for complex tuple expression:")
print(tcmp_pyemit(test_complex_comp))
print()

print("Task 2 (Python Code Emission) completed successfully!")

# Test function compilation (like factorial)
print("Python code for factorial function:")
fact_comp = term_comp00(term_fact)
print(tcmp_pyemit(fact_comp))
print()

# Test function application
print("Python code for doubling function:")
dbl_comp = term_comp00(term_dbl)
print(tcmp_pyemit(dbl_comp))
print()

# Test function application: dbl(5)
print("Python code for function application dbl(5):")
app_comp = term_comp00(term_app(term_dbl, int_5))
print(tcmp_pyemit(app_comp))
print()

# Test a simple lambda function: lambda y: y * 2
print("Python code for lambda y: y * 2:")
simple_lambda = term_lam("y", styp_int, term_mul(term_var("y"), int_2))
simple_comp = term_comp00(simple_lambda)
print(tcmp_pyemit(simple_comp))
print()

##################################################################
# Testing with 8-Queen Puzzle Components
##################################################################

print("="*60)
print("Testing Python Code Emission with 8-Queen Puzzle Functions")
print("="*60)

int_invalid = term_int(-1)
N = term_int(8)
int_0 = term_int(0)
int_1 = term_int(1)
int_2 = term_int(2)
int_3 = term_int(3)
int_4 = term_int(4)
int_5 = term_int(5)
int_6 = term_int(6)
int_7 = term_int(7)
int_8 = term_int(8)
int_9 = term_int(9)
int_10 = term_int(10)
var_i = term_var("i")
var_j = term_var("j")
var_i0 = term_var("i0")
var_j0 = term_var("j0")
var_board = term_var("board")
var_x0 = term_var("x0")
var_x1 = term_var("x1")
var_x2 = term_var("x2")
var_x3 = term_var("x3")
var_x4 = term_var("x4")
var_x5 = term_var("x5")
var_x6 = term_var("x6")
var_x7 = term_var("x7")
var_unit = term_var("unit")
var_args = term_var("args")
var_nsol = term_var("nsol")

btf_t = term_btf(True)
btf_f = term_btf(False)


initial_board = term_tup(
    int_0, term_tup(
        int_0, term_tup(
            int_0, term_tup(
                int_0, term_tup(
                    int_0, term_tup(
                        int_0, term_tup(
                            int_0,
                            int_0
                        )
                    )
                )
            )
        )
    )
)

initial_board_comp = term_comp00(initial_board)
print("Python code for initial board:")
print(tcmp_pyemit(initial_board_comp))
print()


board_get = term_lam(
    "board", styp_board,
    term_lam(
        "i", styp_int,
        term_if0(
            term_eq0(var_i, int_0), \
            term_fst(var_board),  # bd.0 - first element
            term_if0(
                term_eq0(var_i, int_1), \
                term_fst(term_snd(var_board)),  # bd.1 - second element
                term_if0(
                    term_eq0(var_i, int_2), \
                    term_fst(term_snd(term_snd(var_board))),  # bd.2
                    term_if0(
                        term_eq0(var_i, int_3), \
                        term_fst(term_snd(term_snd(term_snd(var_board)))),  # bd.3
                        term_if0(
                            term_eq0(var_i, int_4), \
                            term_fst(term_snd(term_snd(term_snd(term_snd(var_board))))),  # bd.4
                            term_if0(
                                term_eq0(var_i, int_5), \
                                term_fst(term_snd(term_snd(term_snd(term_snd(term_snd(var_board)))))),  # bd.5
                                term_if0(
                                    term_eq0(var_i, int_6), \
                                    term_fst(term_snd(term_snd(term_snd(term_snd(term_snd(term_snd(var_board))))))),  # bd.6
                                    term_if0(
                                        term_eq0(var_i, int_7), \
                                        term_snd(term_snd(term_snd(term_snd(term_snd(term_snd(term_snd(var_board))))))),  # bd.7
                                        int_invalid
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)
board_get_comp = term_comp00(board_get)
print("Python code for board get:")
print(tcmp_pyemit(board_get_comp))
print()

board_set = term_lam(
    "board", styp_board,
    term_lam(
        "i", styp_int,
        term_lam(
            "j", styp_int,
            term_let(
                "x0", term_fst(var_board),  # bd.0
                term_let(
                    "x1", term_fst(term_snd(var_board)),  # bd.1
                    term_let(
                        "x2", term_fst(term_snd(term_snd(var_board))),  # bd.2
                        term_let(
                            "x3", term_fst(term_snd(term_snd(term_snd(var_board)))),  # bd.3
                            term_let(
                                "x4", term_fst(term_snd(term_snd(term_snd(term_snd(var_board))))),  # bd.4
                                term_let(
                                    "x5", term_fst(term_snd(term_snd(term_snd(term_snd(term_snd(var_board)))))),  # bd.5
                                    term_let(
                                        "x6", term_fst(term_snd(term_snd(term_snd(term_snd(term_snd(term_snd(var_board))))))),  # bd.6
                                        term_let(
                                            "x7", term_snd(term_snd(term_snd(term_snd(term_snd(term_snd(term_snd(var_board))))))),  # bd.7
                                            term_if0(
                                                term_eq0(var_i, int_0), \
                                                # i = 0: update x0
                                                term_tup(var_j, term_tup(var_x1, term_tup(var_x2, term_tup(var_x3, term_tup(var_x4, term_tup(var_x5, term_tup(var_x6, var_x7))))))),
                                                term_if0(
                                                    term_eq0(var_i, int_1), \
                                                    # i = 1: update x1
                                                    term_tup(var_x0, term_tup(var_j, term_tup(var_x2, term_tup(var_x3, term_tup(var_x4, term_tup(var_x5, term_tup(var_x6, var_x7))))))),
                                                    term_if0(
                                                        term_eq0(var_i, int_2), \
                                                        # i = 2: update x2
                                                        term_tup(var_x0, term_tup(var_x1, term_tup(var_j, term_tup(var_x3, term_tup(var_x4, term_tup(var_x5, term_tup(var_x6, var_x7))))))),
                                                        term_if0(
                                                            term_eq0(var_i, int_3), \
                                                            # i = 3: update x3
                                                            term_tup(var_x0, term_tup(var_x1, term_tup(var_x2, term_tup(var_j, term_tup(var_x4, term_tup(var_x5, term_tup(var_x6, var_x7))))))),
                                                            term_if0(
                                                                term_eq0(var_i, int_4), \
                                                                # i = 4: update x4
                                                                term_tup(var_x0, term_tup(var_x1, term_tup(var_x2, term_tup(var_x3, term_tup(var_j, term_tup(var_x5, term_tup(var_x6, var_x7))))))),
                                                                term_if0(
                                                                    term_eq0(var_i, int_5), \
                                                                    # i = 5: update x5
                                                                    term_tup(var_x0, term_tup(var_x1, term_tup(var_x2, term_tup(var_x3, term_tup(var_x4, term_tup(var_j, term_tup(var_x6, var_x7))))))),
                                                                    term_if0(
                                                                        term_eq0(var_i, int_6), \
                                                                        # i = 6: update x6
                                                                        term_tup(var_x0, term_tup(var_x1, term_tup(var_x2, term_tup(var_x3, term_tup(var_x4, term_tup(var_x5, term_tup(var_j, var_x7))))))),
                                                                        term_if0(
                                                                            term_eq0(var_i, int_7), \
                                                                            # i = 7: update x7
                                                                            term_tup(var_x0, term_tup(var_x1, term_tup(var_x2, term_tup(var_x3, term_tup(var_x4, term_tup(var_x5, term_tup(var_x6, var_j))))))),
                                                                            # else: return original board
                                                                            var_board
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)

board_set_comp = term_comp00(board_set)
print("Python Code for board_set")
print(tcmp_pyemit(board_set_comp))
print()

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


safety_test2 = term_fix(
    "safety_test2", "args", styp_board,  styp_bool,
    term_let(
        "i0", term_fst(var_args),
        term_let(
            "j0", term_fst(term_snd(var_args)),
            term_let(
                "board", term_fst(term_snd(term_snd(var_args))),
                term_let(
                    "i", term_snd(term_snd(term_snd(var_args))),
                    term_if0(
                        term_gte(var_i, int_0), \
                        term_if0(
                            term_app(
                                term_app(
                                    term_app(
                                        term_app(safety_test1, var_i0),
                                        var_j0
                                    ),
                                    var_i
                                ),
                                term_app(
                                    term_app(board_get, var_board),
                                    var_i
                                )
                            ), \
                            term_app(
                                term_var("safety_test2"),
                                term_tup(
                                    var_i0,
                                    term_tup(
                                        var_j0,
                                        term_tup(
                                            var_board,
                                            term_sub(var_i, int_1)
                                        )
                                    )
                                )
                            ),
                            btf_f
                        ),
                        btf_t
                    )
                )
            )
        )
    )
)

safety_test2_comp = term_comp00(safety_test2)
print("Python Code for safety_test2")
print(tcmp_pyemit(safety_test2_comp))
print()


search = term_fix(
    "search", "args", styp_board, styp_int,
    term_let(
        "board", term_fst(var_args),
        term_let(
            "i", term_fst(term_snd(var_args)),
            term_let(
                "j", term_fst(term_snd(term_snd(var_args))),
                term_let(
                    "nsol", term_snd(term_snd(term_snd(var_args))),
                    term_if0(
                        term_lt0(var_j, N),
                        # j < N case
                        term_let(
                            "test",
                            term_app(
                                safety_test2,
                                term_tup(
                                    var_i,
                                    term_tup(
                                        var_j,
                                        term_tup(
                                            var_board,
                                            term_sub(var_i, int_1)
                                        )
                                    )
                                )
                            ),
                            term_if0(
                                term_var("test"),
                                # test is true - place queen
                                term_let(
                                    "bd1",
                                    term_app(
                                        term_app(
                                            term_app(board_set, var_board),
                                            var_i
                                        ),
                                        var_j
                                    ),
                                    term_if0(
                                        term_eq0(
                                            term_add(var_i, int_1), N
                                        ),
                                        # Found a solution
                                        term_let(
                                            "_solution_print",
                                            term_print(term_tup(var_board, var_nsol)),
                                            term_app(
                                                term_var("search"),
                                                term_tup(
                                                    var_board,
                                                    term_tup(
                                                        var_i,
                                                        term_tup(
                                                            term_add(var_j, int_1),
                                                            term_add(var_nsol, int_1),
                                                        )
                                                    )
                                                )
                                            )
                                        ),
                                        # Continue to next row
                                        term_app(
                                            term_var("search"),
                                            term_tup(
                                                term_var("bd1"),
                                                term_tup(
                                                    term_add(var_i, int_1),
                                                    term_tup(
                                                        int_0,
                                                        term_var("nsol")
                                                    )
                                                )
                                            )
                                        )
                                    )
                                ),
                                # test is false, try next column
                                term_app(
                                    term_var("search"),
                                    term_tup(
                                        var_board,
                                        term_tup(
                                            var_i,
                                            term_tup(
                                                term_add(var_j, int_1),
                                                term_var("nsol")
                                            )
                                        )
                                    )
                                )
                            )
                        ),
                        # j >= N case - backtrack
                        term_if0(
                            term_gt0(var_i, int_0),
                            term_app(
                                term_var("search"),
                                term_tup(
                                    var_board,
                                    term_tup(
                                        term_sub(var_i, int_1),
                                        term_tup(
                                            term_add(
                                                term_app(
                                                    term_app(board_get, var_board),
                                                    term_sub(var_i, int_1)
                                                ),
                                                int_1
                                            ),
                                            var_nsol
                                        )
                                    )
                                )
                            ),
                            var_nsol
                        )
                    )
                )
            )
        )
    )
)

search_comp = term_comp00(search)
print("Python Code for search_comp")
print(tcmp_pyemit(search_comp))
print()

##################################################################
# end of [CS391-2025-Summer/lectures/lecture-06-03/lambda3.py]
##################################################################
