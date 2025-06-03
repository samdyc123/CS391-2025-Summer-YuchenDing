print("Hello from [lambda1]!")

# datatype term =
# |TMint of sint
# |TMbtf of bool
# |TMvar of tvar
# |TMlam of (tvar, term)
# |TMapp of (term, term)
# |TMopr of (topr, list(term))
# |TMif0 of (term, term, term)

class term:
    ctag = ""
    def __str__(self):
        return ("term(" + self.ctag + ")")

class term_int(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMint"
    def __str__(self):
        return ("TMint(" + str(self.arg1) + ")")

class term_btf(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMbtf"
    def __str__(self):
        return ("TMbtf(" + str(self.arg1) + ")")

class term_var(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMvar"
    def __str__(self):
        return ("TMvar(" + self.arg1 + ")")

class term_lam(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMlam"
    def __str__(self):
        return ("TMlam(" + self.arg1 + "," + str(self.arg2) + ")")

class term_app(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMapp"
    def __str__(self):
        return ("TMapp(" + str(self.arg1) + "," + str(self.arg2) + ")")

class term_opr(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1  # operator string
        self.arg2 = arg2  # list of terms
        self.ctag = "TMopr"
    def __str__(self):
        terms_str = "[" + ",".join(str(tm) for tm in self.arg2) + "]"
        return ("TMopr(" + self.arg1 + "," + terms_str + ")")

class term_if0(term):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1  # condition
        self.arg2 = arg2  # then branch
        self.arg3 = arg3  # else branch
        self.ctag = "TMif0"
    def __str__(self):
        return ("TMif0(" + str(self.arg1) + "," + str(self.arg2) + "," + str(self.arg3) + ")")

# Common combinators
x = term_var("x")
y = term_var("y")
z = term_var("z")

I = term_lam("x", x)
K = term_lam("x", term_lam("y", x))
S = term_lam("x", term_lam("y", term_lam("z",
                                         term_app(term_app(x, z), term_app(y, z)))))
K1 = term_lam("x", term_lam("y", y))
omega = term_lam("x", term_app(x, x))
Omega = term_app(omega, omega)

print("I =", I)
print("K =", K)
print("S =", S)
print("K1 =", K1)
print("omega =", omega)
print("Omega =", Omega)

# Church numerals
f = term_var("f")
x = term_var("x")
TMone = term_lam("f", term_lam("x", term_app(f, x)))
TMtwo = term_lam("f", term_lam("x", term_app(f, term_app(f, x))))

print("TMone =", TMone)
print("TMtwo =", TMtwo)

# Arithmetic operations
def TMadd(a1, a2):
    return term_opr("+", [a1, a2])

def TMsub(a1, a2):
    return term_opr("-", [a1, a2])

def TMmul(a1, a2):
    return term_opr("*", [a1, a2])

def TMdiv(a1, a2):
    return term_opr("/", [a1, a2])

def TMmod(a1, a2):
    return term_opr("%", [a1, a2])

# Helper functions
x = term_var("x")
TMdbl = term_lam("x", TMadd(x, x))
TMtpl = term_lam("x", TMadd(x, TMadd(x, x)))

print("TMdbl =", TMdbl)
print("TMtpl =", TMtpl)

TMsqr = term_lam("x", TMmul(x, x))
TMcbr = term_lam("x", TMmul(x, TMmul(x, x)))

print("TMsqr =", TMsqr)
print("TMcbr =", TMcbr)

# Substitution function
def term_subst(tm0, x00, sub):
    def subst(tm0):
        return term_subst(tm0, x00, sub)

    if tm0.ctag == "TMint":
        return tm0
    elif tm0.ctag == "TMbtf":
        return tm0
    elif tm0.ctag == "TMvar":
        x01 = tm0.arg1
        return sub if (x00 == x01) else tm0
    elif tm0.ctag == "TMlam":
        x01 = tm0.arg1
        tm1 = tm0.arg2
        return tm0 if (x00 == x01) else term_lam(x01, subst(tm1))
    elif tm0.ctag == "TMapp":
        tm1 = tm0.arg1
        tm2 = tm0.arg2
        return term_app(subst(tm1), subst(tm2))
    elif tm0.ctag == "TMopr":
        f00 = tm0.arg1
        tms = tm0.arg2
        return term_opr(f00, [subst(tm) for tm in tms])
    elif tm0.ctag == "TMif0":
        tm1 = tm0.arg1
        tm2 = tm0.arg2
        tm3 = tm0.arg3
        return term_if0(subst(tm1), subst(tm2), subst(tm3))
    else:
        raise TypeError(tm0)

# Interpreter function
def term_interp(tm0):
    if tm0.ctag == "TMint":
        return tm0
    elif tm0.ctag == "TMbtf":
        return tm0
    elif tm0.ctag == "TMvar":
        return tm0
    elif tm0.ctag == "TMlam":
        return tm0
    elif tm0.ctag == "TMapp":
        tm1 = tm0.arg1
        tm2 = tm0.arg2
        tm1 = term_interp(tm1)
        if tm1.ctag == "TMlam":
            x01 = tm1.arg1
            tmx = tm1.arg2
            return term_interp(term_subst(tmx, x01, tm2))
        else:
            return term_app(tm1, term_interp(tm2))
    elif tm0.ctag == "TMopr":
        pnm = tm0.arg1
        tms = tm0.arg2

        if pnm == "+":
            tm1, tm2 = tms[0], tms[1]
            i01 = term_interp(tm1).arg1
            i02 = term_interp(tm2).arg1
            return term_int(i01 + i02)
        elif pnm == "-":
            tm1, tm2 = tms[0], tms[1]
            i01 = term_interp(tm1).arg1
            i02 = term_interp(tm2).arg1
            return term_int(i01 - i02)
        elif pnm == "*":
            tm1, tm2 = tms[0], tms[1]
            i01 = term_interp(tm1).arg1
            i02 = term_interp(tm2).arg1
            return term_int(i01 * i02)
        elif pnm == "/":
            tm1, tm2 = tms[0], tms[1]
            i01 = term_interp(tm1).arg1
            i02 = term_interp(tm2).arg1
            return term_int(i01 // i02)
        elif pnm == "<":
            tm1, tm2 = tms[0], tms[1]
            i01 = term_interp(tm1).arg1
            i02 = term_interp(tm2).arg1
            return term_btf(i01 < i02)
        elif pnm == ">":
            tm1, tm2 = tms[0], tms[1]
            i01 = term_interp(tm1).arg1
            i02 = term_interp(tm2).arg1
            return term_btf(i01 > i02)
        elif pnm == "=":
            tm1, tm2 = tms[0], tms[1]
            i01 = term_interp(tm1).arg1
            i02 = term_interp(tm2).arg1
            return term_btf(i01 == i02)
        elif pnm == "<=":
            tm1, tm2 = tms[0], tms[1]
            i01 = term_interp(tm1).arg1
            i02 = term_interp(tm2).arg1
            return term_btf(i01 <= i02)
        elif pnm == ">=":
            tm1, tm2 = tms[0], tms[1]
            i01 = term_interp(tm1).arg1
            i02 = term_interp(tm2).arg1
            return term_btf(i01 >= i02)
        elif pnm == "!=":
            tm1, tm2 = tms[0], tms[1]
            i01 = term_interp(tm1).arg1
            i02 = term_interp(tm2).arg1
            return term_btf(i01 != i02)
    elif tm0.ctag == "TMif0":
        tm1 = tm0.arg1
        tm2 = tm0.arg2
        tm3 = tm0.arg3
        tm1 = term_interp(tm1)
        if tm1.ctag == "TMbtf":
            btf = tm1.arg1
            return term_interp(tm2 if btf else tm3)
    else:
        raise TypeError(tm0)

# Test cases
print("TMapp(TMdbl, TMint(10)) =", term_app(TMdbl, term_int(10)))
print("TMapp(TMdbl, TMint(10)) =", term_interp(term_app(TMdbl, term_int(10))))

print("TMapp(TMsqr, TMint(10)) =", term_app(TMsqr, term_int(10)))
print("TMapp(TMsqr, TMint(10)) =", term_interp(term_app(TMsqr, term_int(10))))

print("TMapp(TMapp(TMtwo, TMtpl), TMint(10)) =",
      term_interp(term_app(term_app(TMtwo, TMtpl), term_int(10))))

print("TMapp(TMapp(TMapp(TMtwo, TMtwo), TMtpl), TMint(10)) =",
      term_interp(term_app(term_app(term_app(TMtwo, TMtwo), TMtpl), term_int(10))))

# Y combinator
f = term_var("f")
x = term_var("x")
fomega = term_lam("x", term_app(f, term_app(x, x)))
Y = term_lam("f", term_app(fomega, fomega))

# Comparison operators
def TMlt(tm1, tm2):
    return term_opr("<", [tm1, tm2])

def TMgt(tm1, tm2):
    return term_opr(">", [tm1, tm2])

def TMeq(tm1, tm2):
    return term_opr("=", [tm1, tm2])

def TMlte(tm1, tm2):
    return term_opr("<=", [tm1, tm2])

def TMgte(tm1, tm2):
    return term_opr(">=", [tm1, tm2])

def TMneq(tm1, tm2):
    return term_opr("!=", [tm1, tm2])

# Factorial function
f = term_var("f")
x = term_var("x")
F = term_lam("f", term_lam("x",
                           term_if0(TMlte(x, term_int(0)),
                                    term_int(1),
                                    TMmul(x, term_app(f, TMsub(x, term_int(1)))))))
TMfact = term_app(Y, F)

print("TMapp(TMfact, TMint(5)) =", term_interp(term_app(TMfact, term_int(5))))
