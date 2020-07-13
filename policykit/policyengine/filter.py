import ast
from policyengine.exceptions import NonWhitelistedCodeError

IMPORT_ERROR_MESSAGE = "module cannot be imported because it is not in the list of whitelisted modules."
FUNCTION_ERROR_MESSAGE = "function cannot be called because it is not in the list of whitelisted modules."

whitelisted_modules = [
    "base64",
    "calendar",
    "copy",
    "datetime",
    "datetime.date",
    "datetime.time",
    "datetime.datetime",
    "datetime.timedelta",
    "datetime.tzinfo",
    "datetime.timezone",
    "itertools",
    "math",
    "random",
    "re",
    "time",
    "urllib",
    "urllib.request",
    "urllib.error",
    "urllib.parse",
]

whitelisted_functions = [
    # Built-ins
    "abs",
    "all",
    "any",
    "bool",
    "bytes",
    "chr",
    "divmod",
    "enumerate",
    "float",
    "hash",
    "hex",
    "id",
    "int",
    "iter",
    "len",
    "list",
    "map",
    "max",
    "min",
    "next",
    "pow",
    "range",
    "round",
    "set",
    "slice",
    "sorted",
    "str",
    "sum",
    "tuple",
    "zip",

    # Base64 library
    "a85encode",
    "a85decode",
    "b16encode",
    "b16decode",
    "b32encode",
    "b32decode",
    "b64encode",
    "b64decode",
    "b85encode",
    "b85decode",
    "standard_b64encode",
    "standard_b64decode",
    "urlsafe_b64encode",
    "urlsafe_b64decode",

    # Calendar library
    "calendar",
    "day_abbr",
    "day_name",
    "firstweekday",
    "isleap",
    "iterweekdays",
    "itermonthdates",
    "itermonthdays",
    "itermonthdays2",
    "itermonthdays3",
    "itermonthdays4",
    "leapdays",
    "month",
    "monthcalendar",
    "monthdatescalendar",
    "monthdays2calendar",
    "monthdayscalendar",
    "monthrange",
    "month_abbr",
    "month_name",
    "setfirstweekday",
    "timegm",
    "weekday",
    "weekheader",
    "yeardatescalendar",
    "yeardays2calendar",
    "yeardayscalendar",

    # Copy library
    "copy",
    "deepcopy",

    # Datetime library
    "MINYEAR",
    "MAXYEAR",

    # Datetime.timedelta library
    "max",
    "min",
    "resolution",
    "total_seconds",

    # Datetime.date library
    "ctime",
    "day",
    "fromisocalendar",
    "fromisoformat",
    "fromordinal",
    "fromtimestamp",
    "isocalendar",
    "isoformat",
    "isoweekday",
    "max",
    "min",
    "month",
    "replace",
    "resolution",
    "timetuple",
    "today",
    "toordinal",
    "weekday",
    "year",

    # Datetime.datetime library
    "astimezone",
    "combine",
    "ctime",
    "date",
    "day",
    "dst",
    "fold",
    "fromisocalendar",
    "fromisoformat",
    "fromordinal",
    "fromtimestamp",
    "hour",
    "isocalendar",
    "isoformat",
    "isoweekday",
    "max",
    "microsecond",
    "min",
    "minute",
    "month",
    "now",
    "replace",
    "resolution",
    "second",
    "time",
    "timestamp",
    "timetuple",
    "timetz",
    "today",
    "toordinal",
    "tzinfo",
    "tzname",
    "utcfromtimestamp",
    "utcnow",
    "utcoffset",
    "utctimetuple",
    "weekday",
    "year",

    # Datetime.time library
    "dst",
    "fold",
    "fromisoformat",
    "hour",
    "isoformat",
    "max",
    "microsecond",
    "min",
    "minute",
    "replace",
    "resolution",
    "second",
    "tzinfo",
    "tzname",
    "utcoffset",

    # Datetime.timezone library
    "dst",
    "fromutc",
    "tzname",
    "utc",
    "utcoffset",

    # Itertools library
    "accumulate",
    "chain",
    "combinations",
    "combinations_with_replacement",
    "compress",
    "count",
    "cycle",
    "dropwhile",
    "filterfalse",
    "groupby",
    "islice",
    "permutations",
    "product",
    "repeat",
    "starmap",
    "takewhile",
    "tee",
    "zip_longest",

    # Math library
    "acos",
    "acosh",
    "asin",
    "asinh",
    "atan",
    "atanh",
    "atan2",
    "ceil",
    "comb",
    "copysign",
    "cos",
    "cosh",
    "degrees",
    "dist",
    "e",
    "erf",
    "erfc",
    "exp",
    "expm1",
    "fabs",
    "factorial",
    "floor",
    "fmod",
    "frexp",
    "fsum",
    "gamma",
    "gcd",
    "hypot",
    "inf",
    "isclose",
    "isfinite",
    "isinf",
    "isnan",
    "isqrt",
    "ldexp",
    "lgamma",
    "log",
    "log1p",
    "log2",
    "log10",
    "modf",
    "nan",
    "perm",
    "pi",
    "pow",
    "prod",
    "radians",
    "remainder",
    "sin",
    "sinh",
    "sqrt",
    "tan",
    "tanh",
    "tau",
    "trunc",

    # Random library
    "betavariate",
    "choice",
    "choices",
    "expovariate",
    "gammavariate",
    "gauss",
    "lognormvariate",
    "normalvariate",
    "paretovariate",
    "randint",
    "random",
    "randrange",
    "sample",
    "seed",
    "shuffle",
    "triangular",
    "uniform",
    "vonmisesvariate",
    "weibullvariate",
]

class Filter(ast.NodeVisitor):
    def visit_Import(self, node):
        for module_alias in node.names:
            if module_alias.name not in whitelisted_modules:
                raise NonWhitelistedCodeError(module_alias.name, IMPORT_ERROR_MESSAGE)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for module_alias in node.names:
            if module_alias.name not in whitelisted_modules:
                raise NonWhitelistedCodeError(module_alias.name, IMPORT_ERROR_MESSAGE)
        self.generic_visit(node)

    def visit_Call(self, node):
        if node.func.id not in whitelisted_functions:
            raise NonWhitelistedCodeError(node.func.id, FUNCTION_ERROR_MESSAGE)
        self.generic_visit(node)

def filter_code(code):
    tree = ast.parse(code)

    filter = Filter()
    filter.visit(tree)
