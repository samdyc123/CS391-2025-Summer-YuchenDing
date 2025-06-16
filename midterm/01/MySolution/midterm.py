import sys
sys.setrecursionlimit(1000000000)

# ============================================================================
# Task 1
# ============================================================================

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

# | STtup of (styp, styp) # for pairs
class styp_tup:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "STtup"
    def __str__(self):
        return ("STtup(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(styp_tup(styp))

# | STfun of (styp, styp) # for functions
class styp_fun:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "STfun"
    def __str__(self):
        return ("STfun(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(styp_fun(styp))

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

# | TMtup of (term, term) # tuple construction
class term_tup(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMtup"
    def __str__(self):
        return ("TMtup(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(term_tup(term))

# | TMfst of term # first projection
class term_fst(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMfst"
    def __str__(self):
        return ("TMfst(" + str(self.arg1) + ")")
# end-of-class(term_fst(term))

# | TMsnd of term # second projection
class term_snd(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMsnd"
    def __str__(self):
        return ("TMsnd(" + str(self.arg1) + ")")
# end-of-class(term_snd(term))

# | TMlet of (strn(*x*), term(*t1*), term(*t2*))
class term_let(term):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TMlet"
    def __str__(self):
        return ("TMlet(" + self.arg1 + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")
# end-of-class(term_let(term))


# TMlet is not used - replaced with direct lambda applications
# | TMlet of (strn(*x*), term(*t1*), term(*t2*)) - equivalent to (lam x. t2)(t1)

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
term_print = lambda a1: term_opr("print", a1)

# Proper type definitions using styp classes
styp_int = styp_bas("int")
styp_bool = styp_bas("bool")
styp_void = styp_bas("void")

# Constant N = 8
N = term_int(8)

int_invalid = term_int(-1)
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


# Type for int8 (8-tuple of integers) - represented as nested pairs
# int8 = (int, (int, (int, (int, (int, (int, (int, int)))))))
styp_board = styp_tup(styp_int,
            styp_tup(styp_int,
            styp_tup(styp_int,
            styp_tup(styp_int,
            styp_tup(styp_int,
            styp_tup(styp_int,
            styp_tup(styp_int, styp_int)))))))

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


def print_dots(i):
    if i > 0:
        print(". ", end="")
        print_dots(i - 1)

def print_row(i):
    print_dots(i)
    print("Q ", end="")
    print_dots(term_eval00(N).arg1 - i - 1)
    print()

def print_board(board):
    board_tval = term_eval00(board)
    positions = tval_to_board_list(board_tval)
    for row in range(8):
        queen_col = positions[row]
        print_row(queen_col)

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

# safety_test1: tests if two queens can capture each other
# fun safety_test1 (i0: int, j0: int, i: int, j: int) : bool =
#   j0 != j andalso abs (i0 - i) != abs (j0 - j)
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

# safety_test2: tests if a queen can capture any other pieces on the board
# fun safety_test2 (i0: int, j0: int, bd: int8, i: int) : bool =
#   if i >= 0 then
#     if safety_test1 (i0, j0, i, board_get (bd, i))
#       then safety_test2 (i0, j0, bd, i-1) else false
#   else true
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

# Main search function for 8-queen puzzle
# This is the core DFS algorithm
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
                                            term_print([var_board, var_nsol]),
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


# ============================================================================
# Task 2
# ============================================================================

# datatype tval =
# | TVint of int
# | TVbtf of bool
# | TVclo of (term, xenv)
# | TVtup of (tval, tval)  # for tuple values

class tval:
    ctag = ""
    def __str__(self):
        return ("tval(" + self.ctag + ")")
# end-of-class(tval)

class tval_int(tval):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TVint"
    def __str__(self):
        return ("TVint(" + str(self.arg1) + ")")
# end-of-class(tval_int(tval))

class tval_btf(tval):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TVbtf"
    def __str__(self):
        return ("TVbtf(" + str(self.arg1) + ")")
# end-of-class(tval_btf(tval))

class tval_clo(tval):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TVclo"
    def __str__(self):
        return ("TVclo(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(tval_clo(tval))

class tval_tup(tval):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TVtup"
    def __str__(self):
        return ("TVtup(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(tval_tup(tval))

# datatype xenv =
# | EVnil of ()
# | EVcons of (strn, tval, xenv)

class xenv:
    ctag = ""
    def __str__(self):
        return ("xenv(" + self.ctag + ")")
# end-of-class(xenv)

class xenv_nil(xenv):
    def __init__(self):
        self.ctag = "EVnil"
    def __str__(self):
        return ("EVnil(" + ")")
# end-of-class(xenv_nil(xenv))

class xenv_cons(xenv):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "EVcons"
    def __str__(self):
        return ("EVcons(" + self.arg1 + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")
# end-of-class(xenv_cons(xenv))

# Environment search function
def xenv_search(env, x00):
    if env.ctag == "EVnil":
        return None
    if env.ctag == "EVcons":
        if env.arg1 == x00:
            return env.arg2
        else:
            return xenv_search(env.arg3, x00)
    raise TypeError(env)

# Main evaluation function
def term_eval00(tm0):
    return term_eval01(tm0, xenv_nil())

def term_eval01(tm0, env):
    # print("term_eval01: tm0 = " + str(tm0))
    if (tm0.ctag == "TMint"):
        return tval_int(tm0.arg1)
    if (tm0.ctag == "TMbtf"):
        return tval_btf(tm0.arg1)
    if (tm0.ctag == "TMlam"):
        return tval_clo(tm0, env)
    if (tm0.ctag == "TMfix"):
        return tval_clo(tm0, env)
    if (tm0.ctag == "TMvar"):
        tv0 = xenv_search(env, tm0.arg1)
        assert tv0 is not None, f"Unbound variable: {tm0.arg1}"
        return tv0
    if (tm0.ctag == "TMtup"):
        tv1 = term_eval01(tm0.arg1, env)
        tv2 = term_eval01(tm0.arg2, env)
        return tval_tup(tv1, tv2)
    if (tm0.ctag == "TMfst"):
        tv1 = term_eval01(tm0.arg1, env)
        assert tv1.ctag == "TVtup", f"Expected tuple, got {tv1.ctag}"
        return tv1.arg1
    if (tm0.ctag == "TMsnd"):
        tv1 = term_eval01(tm0.arg1, env)
        assert tv1.ctag == "TVtup", f"Expected tuple, got {tv1.ctag}"
        return tv1.arg2
    if (tm0.ctag == "TMlet"):
        # TMlet(x, t1, t2) is equivalent to (lam x. t2)(t1)
        tv1 = term_eval01(tm0.arg2, env)  # evaluate t1
        env_new = xenv_cons(tm0.arg1, tv1, env)  # bind x to tv1
        return term_eval01(tm0.arg3, env_new)  # evaluate t2 in new environment
    if (tm0.ctag == "TMopr"):
        pnm = tm0.arg1
        ags = tm0.arg2 # list of arguments
        if (pnm == "+"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_int(tv1.arg1 + tv2.arg1)
        if (pnm == "-"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_int(tv1.arg1 - tv2.arg1)
        if (pnm == "*"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_int(tv1.arg1 * tv2.arg1)
        if (pnm == "%"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_int(tv1.arg1 % tv2.arg1)
        if (pnm == "/"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_int(tv1.arg1 // tv2.arg1)
        if (pnm == "<"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_btf(tv1.arg1 < tv2.arg1)
        if (pnm == ">"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_btf(tv1.arg1 > tv2.arg1)
        if (pnm == "="):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_btf(tv1.arg1 == tv2.arg1)
        if (pnm == "<="):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_btf(tv1.arg1 <= tv2.arg1)
        if (pnm == ">="):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_btf(tv1.arg1 >= tv2.arg1)
        if (pnm == "!="):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_btf(tv1.arg1 != tv2.arg1)
        if (pnm == "abs"):
            assert len(ags) == 1
            tv1 = term_eval01(ags[0], env)
            assert tv1.ctag == "TVint"
            return tval_int(abs(tv1.arg1))
        if (pnm == "and"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVbtf"
            assert tv2.ctag == "TVbtf"
            return tval_btf(tv1.arg1 and tv2.arg1)
        if (pnm == "or"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVbtf"
            assert tv2.ctag == "TVbtf"
            return tval_btf(tv1.arg1 or tv2.arg1)
        if (pnm == "print"):
            print_values = []
            for arg in ags:
                tv = term_eval01(arg, env)
                if tv.ctag == "TVint":
                    print_values.append(str(tv.arg1))
                elif tv.ctag == "TVbtf":
                    print_values.append(str(tv.arg1))
                elif tv.ctag == "TVtup":
                    # Handle tuple printing (useful for board representation)
                    try:
                        board_list = tval_to_board_list(tv)
                        print_values.append(str(board_list))
                    except:
                        print_values.append(str(tv))
                else:
                    print_values.append(str(tv))

            # Print all values separated by spaces
            print(" ".join(print_values))

            # Return a unit value (represented as integer 0)
            return tval_int(0)
        raise TypeError(f"Unsupported operator: {pnm}")
    if (tm0.ctag == "TMapp"):
        tm1 = tm0.arg1
        tv1 = term_eval01(tm1, env)
        assert tv1.ctag == "TVclo", f"Expected closure, got {tv1.ctag}"
        tm2 = tm0.arg2
        tv2 = term_eval01(tm2, env)
        tmf = tv1.arg1
        env_clo = tv1.arg2
        if tmf.ctag == "TMlam":
            x01 = tmf.arg1
            # tmf.arg2 is the type, tmf.arg3 is the body
            env_new = xenv_cons(x01, tv2, env_clo)
            return term_eval01(tmf.arg3, env_new)
        if tmf.ctag == "TMfix":
            f00 = tmf.arg1
            x01 = tmf.arg2
            # tmf.arg3 and tmf.arg4 are types, tmf.arg5 is the body
            env_new = xenv_cons(f00, tv1, env_clo)
            env_new = xenv_cons(x01, tv2, env_new)
            return term_eval01(tmf.arg5, env_new)
        raise TypeError(f"Invalid closure: {tmf.ctag}")
    if (tm0.ctag == "TMif0"):
        tm1 = tm0.arg1
        tv1 = term_eval01(tm1, env)
        assert tv1.ctag == "TVbtf", f"Expected boolean, got {tv1.ctag}"
        if tv1.arg1:
            return term_eval01(tm0.arg2, env) # then
        else:
            return term_eval01(tm0.arg3, env) # else
    raise TypeError(f"Unsupported term: {tm0.ctag}")


# helper function
def tval_to_board_list(board_tval):
    """Convert a board tuple value to a list of 8 integers"""
    assert board_tval.ctag == "TVtup"

    result = []
    current = board_tval

    for i in range(7):
        assert current.ctag == "TVtup", f"Expected tuple at position {i}"
        first = current.arg1
        assert first.ctag == "TVint", f"Expected int at position {i}"
        result.append(first.arg1)
        current = current.arg2

    # Last element should be an int
    assert current.ctag == "TVint", f"Expected int at last position"
    result.append(current.arg1)

    return result

if __name__ == "__main__":
    test_board = term_tup(
        int_0, term_tup(
            int_1, term_tup(
                int_2, term_tup(
                    int_3, term_tup(
                        int_4, term_tup(
                            int_5, term_tup(
                                int_6,
                                int_7
                            )
                        )
                    )
                )
            )
        )
    )

    # Test board_get
    test_board_get = term_app(term_app(board_get, test_board), int_3)
    result = term_eval00(test_board_get)
    print(f"board_get(test_board, 3) = {result.arg1}")

    # Test board_set
    # Set position 3 to value 6 in test_board
    test_board_updated = term_app(term_app(term_app(board_set, test_board), int_3), int_6)
    print_board(test_board_updated)

    test_updated_get = term_app(term_app(board_get, test_board_updated), int_3)
    result_updated = term_eval00(test_updated_get)
    print(f"After board_set(test_board, 3, 6), board_get(updated_board, 3) = {result_updated.arg1}")


    # Test safety_test1
    # Test if two queens can capture each other
    # safety_test1(0, 0, 1, 1) should be False (diagonal capture)
    test_safety_test1_capture = term_app(
        term_app(
            term_app(
                term_app(safety_test1, int_0),
                int_0
            ),
            int_1
        ),
        int_1
    )
    result_capture = term_eval00(test_safety_test1_capture)
    print(f"safety_test1(0, 0, 1, 1) = {result_capture.arg1} (should be False - diagonal capture)")

    # safety_test1(0, 0, 0, 1) should be True (same row, different column - safe)
    test_safety_test1_safe = term_app(
        term_app(
            term_app(
                term_app(safety_test1, int_0),
                int_0
            ),
            int_0
        ),
        int_1
    )
    result_safe = term_eval00(test_safety_test1_safe)
    print(f"safety_test1(0, 0, 0, 1) = {result_safe.arg1} (should be True - safe)")

    # Test safety_test2
    # Create a test board with a queen at position (0,0)
    test_board_with_queen = term_tup(
        int_0, term_tup(  # Queen at row 0, column 0
            int_2, term_tup(  # No queen at row 1
                int_invalid, term_tup(
                    int_invalid, term_tup(
                        int_invalid, term_tup(
                            int_invalid, term_tup(
                                int_invalid,
                                int_invalid
                            )
                        )
                    )
                )
            )
        )
    )

    # Test safety_test2: check if queen at (1,1) is safe from queen at (0,0)
    test_safety_test2_args = term_tup(
        int_2,  # i0 (row of new queen)
        term_tup(
            int_3,  # j0 (column of new queen)
            term_tup(
                test_board_with_queen,  # board
                int_1  # check from row 0
            )
        )
    )
    test_safety_test2 = term_app(safety_test2, test_safety_test2_args)
    result_safety2 = term_eval00(test_safety_test2)
    print(f"safety_test2(1, 1, board_with_queen_at_0_0, 0) = {result_safety2.arg1} (should be False - diagonal capture)")

    # The main program call: search(initial_board, 0, 0, 0)
    eight_queen_solution = term_app(
        search,
        term_tup(
            initial_board,
            term_tup(
                int_0,  # start from row 0
                term_tup(
                    int_0,  # start from column 0
                    int_0  #  nsol starts at 0
                )
            )
        )
    )
    result = term_eval00(eight_queen_solution)
    print(f"eight_queen_solution = {result.arg1}")

    '''
    output:
    
board_get(test_board, 3) = 3
Q . . . . . . . 
. Q . . . . . . 
. . Q . . . . . 
. . . . . . Q . 
. . . . Q . . . 
. . . . . Q . . 
. . . . . . Q . 
. . . . . . . Q 
After board_set(test_board, 3, 6), board_get(updated_board, 3) = 6
safety_test1(0, 0, 1, 1) = False (should be False - diagonal capture)
safety_test1(0, 0, 0, 1) = True (should be True - safe)
safety_test2(1, 1, board_with_queen_at_0_0, 0) = False (should be False - diagonal capture)
[0, 4, 7, 5, 2, 6, 1, 0] 0
[0, 5, 7, 2, 6, 3, 1, 0] 1
[0, 6, 3, 5, 7, 1, 4, 0] 2
[0, 6, 4, 7, 1, 3, 5, 0] 3
[1, 3, 5, 7, 2, 0, 6, 0] 4
[1, 4, 6, 0, 2, 7, 5, 0] 5
[1, 4, 6, 3, 0, 7, 5, 0] 6
[1, 5, 0, 6, 3, 7, 2, 0] 7
[1, 5, 7, 2, 0, 3, 6, 0] 8
[1, 6, 2, 5, 7, 4, 0, 0] 9
[1, 6, 4, 7, 0, 3, 5, 0] 10
[1, 7, 5, 0, 2, 4, 6, 0] 11
[2, 0, 6, 4, 7, 1, 3, 0] 12
[2, 4, 1, 7, 0, 6, 3, 0] 13
[2, 4, 1, 7, 5, 3, 6, 0] 14
[2, 4, 6, 0, 3, 1, 7, 0] 15
[2, 4, 7, 3, 0, 6, 1, 0] 16
[2, 5, 1, 4, 7, 0, 6, 0] 17
[2, 5, 1, 6, 0, 3, 7, 0] 18
[2, 5, 1, 6, 4, 0, 7, 0] 19
[2, 5, 3, 0, 7, 4, 6, 0] 20
[2, 5, 3, 1, 7, 4, 6, 0] 21
[2, 5, 7, 0, 3, 6, 4, 0] 22
[2, 5, 7, 0, 4, 6, 1, 0] 23
[2, 5, 7, 1, 3, 0, 6, 0] 24
[2, 6, 1, 7, 4, 0, 3, 0] 25
[2, 6, 1, 7, 5, 3, 0, 0] 26
[2, 7, 3, 6, 0, 5, 1, 0] 27
[3, 0, 4, 7, 1, 6, 2, 0] 28
[3, 0, 4, 7, 5, 2, 6, 0] 29
[3, 1, 4, 7, 5, 0, 2, 0] 30
[3, 1, 6, 2, 5, 7, 0, 0] 31
[3, 1, 6, 2, 5, 7, 4, 0] 32
[3, 1, 6, 4, 0, 7, 5, 0] 33
[3, 1, 7, 4, 6, 0, 2, 0] 34
[3, 1, 7, 5, 0, 2, 4, 0] 35
[3, 5, 0, 4, 1, 7, 2, 0] 36
[3, 5, 7, 1, 6, 0, 2, 0] 37
[3, 5, 7, 2, 0, 6, 4, 0] 38
[3, 6, 0, 7, 4, 1, 5, 0] 39
[3, 6, 2, 7, 1, 4, 0, 0] 40
[3, 6, 4, 1, 5, 0, 2, 0] 41
[3, 6, 4, 2, 0, 5, 7, 0] 42
[3, 7, 0, 2, 5, 1, 6, 0] 43
[3, 7, 0, 4, 6, 1, 5, 0] 44
[3, 7, 4, 2, 0, 6, 1, 0] 45
[4, 0, 3, 5, 7, 1, 6, 0] 46
[4, 0, 7, 3, 1, 6, 2, 0] 47
[4, 0, 7, 5, 2, 6, 1, 0] 48
[4, 1, 3, 5, 7, 2, 0, 0] 49
[4, 1, 3, 6, 2, 7, 5, 0] 50
[4, 1, 5, 0, 6, 3, 7, 0] 51
[4, 1, 7, 0, 3, 6, 2, 0] 52
[4, 2, 0, 5, 7, 1, 3, 0] 53
[4, 2, 0, 6, 1, 7, 5, 0] 54
[4, 2, 7, 3, 6, 0, 5, 0] 55
[4, 6, 0, 2, 7, 5, 3, 0] 56
[4, 6, 0, 3, 1, 7, 5, 0] 57
[4, 6, 1, 3, 7, 0, 2, 0] 58
[4, 6, 1, 5, 2, 0, 3, 0] 59
[4, 6, 1, 5, 2, 0, 7, 0] 60
[4, 6, 3, 0, 2, 7, 5, 0] 61
[4, 7, 3, 0, 2, 5, 1, 0] 62
[4, 7, 3, 0, 6, 1, 5, 0] 63
[5, 0, 4, 1, 7, 2, 6, 0] 64
[5, 1, 6, 0, 2, 4, 7, 0] 65
[5, 1, 6, 0, 3, 7, 4, 0] 66
[5, 2, 0, 6, 4, 7, 1, 0] 67
[5, 2, 0, 7, 3, 1, 6, 0] 68
[5, 2, 0, 7, 4, 1, 3, 0] 69
[5, 2, 4, 6, 0, 3, 1, 0] 70
[5, 2, 4, 7, 0, 3, 1, 0] 71
[5, 2, 6, 1, 3, 7, 0, 0] 72
[5, 2, 6, 1, 7, 4, 0, 0] 73
[5, 2, 6, 3, 0, 7, 1, 0] 74
[5, 3, 0, 4, 7, 1, 6, 0] 75
[5, 3, 1, 7, 4, 6, 0, 0] 76
[5, 3, 6, 0, 2, 4, 1, 0] 77
[5, 3, 6, 0, 7, 1, 4, 0] 78
[5, 7, 1, 3, 0, 6, 4, 0] 79
[6, 0, 2, 7, 5, 3, 1, 0] 80
[6, 1, 3, 0, 7, 4, 2, 0] 81
[6, 1, 5, 2, 0, 3, 7, 0] 82
[6, 2, 0, 5, 7, 4, 1, 0] 83
[6, 2, 7, 1, 4, 0, 5, 0] 84
[6, 3, 1, 4, 7, 0, 2, 0] 85
[6, 3, 1, 7, 5, 0, 2, 0] 86
[6, 4, 2, 0, 5, 7, 1, 0] 87
[7, 1, 3, 0, 6, 4, 2, 0] 88
[7, 1, 4, 2, 0, 6, 3, 0] 89
[7, 2, 0, 5, 1, 4, 6, 0] 90
[7, 3, 0, 2, 5, 1, 6, 0] 91
eight_queen_solution = 92
    '''
