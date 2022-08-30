"""
Python model 'bass.py'
Translated using PySD
"""

from pathlib import Path

from pysd.py_backend.statefuls import Integ

__pysd_version__ = "2.2.1"

__data = {"scope": None, "time": lambda: 0}

_root = Path(__file__).parent

_subscript_dict = {}

_namespace = {
    "TIME": "time",
    "Time": "time",
    "our clients": "our_clients",
    "competitor clients": "competitor_clients",
    "potential clients": "potential_clients",
    "our clients initial": "our_clients_initial",
    "competitor clients initial": "competitor_clients_initial",
    "potential clients initial": "potential_clients_initial",

    "sociability": "sociability",
    "word of mouth efficiency": "word_of_mouth_efficiency",
    "marketing efficiency": "marketing_efficiency",
    "k": "k",
    "tr": "tr",
    "total population": "total_population",
    "p11": "p11",
    "p13": "p13",
    "p21": "p21",
    "p23": "p23",

    "pc cl": "pc_cl",
    "cl pc": "cl_pc",
    "comp pc": "comp_pc",
    "pc comp": "pc_comp",
    "comp cl": "comp_cl",
    "cl comp": "cl_comp",

    "competitors population": "competitors_population",
    "potential population": "potential_population",
    "our population": "our_population",
    
    "time final": "time_final",
    "FINAL TIME": "final_time",
    "INITIAL TIME": "initial_time",
    "SAVEPER": "saveper",
    "TIME STEP": "time_step",
}

_dependencies = {
    "sociability": {},
    "word_of_mouth_efficiency": {},
    "marketing_efficiency": {},
    "tr": {},
    "total_population": {"_integ_clients": 1, "_integ_potential_clients": 1, "_integ_competitor_clients": 1},
    "k": {"word_of_mouth_efficiency": 1, "marketing_efficiency": 1},
    "p11": {},
    "p13": {},
    "p21": {},
    "p23": {},

    "pc_cl": {"marketing_efficiency": 1, "_integ_potential_clients": 1, "word_of_mouth_efficiency": 1, "sociability": 1, "_integ_potential_clients": 1, "_integ_clients": 1, "p11": 1},
    "cl_pc": {"_integ_clients": 1, "p13": 1, "k": 1},
    "comp_pc": {"_integ_competitor_clients": 1, "p23": 1, "k": 1},
    "pc_comp": {"marketing_efficiency": 1, "_integ_potential_clients": 1, "word_of_mouth_efficiency": 1, "sociability": 1, "_integ_potential_clients": 1, "_integ_competitor_clients": 1, "p21": 1},

    "comp_cl": {"tr": 1, "k": 1, "word_of_mouth_efficiency": 1, "sociability": 1, "_integ_competitor_clients": 1, "p21": 1, "_integ_clients": 1, "p11": 1, "p23": 1, "total_population": 1},

    "cl_comp": {"tr": 1, "k": 1, "word_of_mouth_efficiency": 1, "sociability": 1, "_integ_competitor_clients": 1, "p21": 1, "_integ_clients": 1, "p11": 1, "p13": 1, "total_population": 1},

    "time_final": {},
    "final_time": {},
    "initial_time": {},
    "saveper": {"time_step": 1},
    "time_step": {},
    
    "our_clients": {"pc_cl": 1, "cl_pc": 1, "comp_cl": 1, "cl_comp": 1},
    "competitor_clients": {"pc_comp": 1, "comp_pc": 1, "comp_cl": 1, "cl_comp": 1},
    "potential_clients": {"pc_cl": 1, "cl_pc": 1, "comp_pc": 1, "pc_comp": 1},
    "our_clients_initial": {},
    "competitor_clients_initial": {},
    "potential_clients_initial": {},
    
    "competitors_population": {"_integ_competitor_clients": 1},
    "potential_population": {"_integ_potential_clients": 1},
    "our_population": {"_integ_clients": 1},
    
    "_integ_competitor_clients": {"initial": {"competitor_clients_initial": 1}, "step": {"competitor_clients": 1}},
    "_integ_potential_clients": {"initial": {"potential_clients_initial": 1}, "step": {"potential_clients": 1}},
    "_integ_clients": {"initial": {"our_clients_initial": 1}, "step": {"our_clients": 1}}
}

##########################################################################
#                            CONTROL VARIABLES                           #
##########################################################################

_control_vars = {
    "initial_time": lambda: 0,
    "final_time": lambda: time_final(),
    "time_step": lambda: 1,
    "saveper": lambda: time_step(),
}


def _init_outer_references(data):
    for key in data:
        __data[key] = data[key]


def time():
    return __data["time"]()


def final_time():
    """
    Real Name: FINAL TIME
    Original Eqn: 100
    Units: Month
    Limits: (None, None)
    Type: constant
    Subs: None

    The final time for the simulation.
    """
    return __data["time"].final_time()


def initial_time():
    """
    Real Name: INITIAL TIME
    Original Eqn: 0
    Units: Month
    Limits: (None, None)
    Type: constant
    Subs: None

    The initial time for the simulation.
    """
    return __data["time"].initial_time()


def saveper():
    """
    Real Name: SAVEPER
    Original Eqn: TIME STEP
    Units: Month
    Limits: (None, None)
    Type: component
    Subs: None

    The frequency with which output is stored.
    """
    return __data["time"].saveper()


def time_step():
    """
    Real Name: TIME STEP
    Original Eqn: 1
    Units: Month
    Limits: (None, None)
    Type: constant
    Subs: None

    The time step for the simulation.
    """
    return __data["time"].time_step()


##########################################################################
#                             MODEL VARIABLES                            #
##########################################################################
def time_final():
    return 100

def total_population():
    return _integ_clients() + _integ_potential_clients() + _integ_competitor_clients()

def our_clients():
    return pc_cl() - cl_pc() + comp_cl() - cl_comp()

def competitor_clients():
    return pc_comp() - comp_pc() - comp_cl() + cl_comp()

def potential_clients():
    return comp_pc() - pc_comp() + cl_pc() - pc_cl()

def competitors_population():
    return _integ_competitor_clients()

def potential_population():
    return _integ_potential_clients()

def our_population():
    return _integ_clients()


def sociability():
    return 100
def word_of_mouth_efficiency():
    return 0.015

def marketing_efficiency():
    return 0.011

def k():
    return marketing_efficiency() / (marketing_efficiency() + word_of_mouth_efficiency())

def tr():
    return word_of_mouth_efficiency() / (marketing_efficiency() + word_of_mouth_efficiency())

def pc_cl():
    return marketing_efficiency() * _integ_potential_clients() + word_of_mouth_efficiency() * sociability() * _integ_potential_clients() * _integ_clients() * p11() / total_population()

def pc_comp():
    return marketing_efficiency() * _integ_potential_clients() + word_of_mouth_efficiency() * sociability() * _integ_potential_clients() * _integ_competitor_clients() * p21() / total_population()

def cl_pc():
    return _integ_clients() * p13() * k()

def comp_pc():
    return _integ_competitor_clients() * p23() * k()

def cl_comp():
    return tr() * word_of_mouth_efficiency() * sociability() * _integ_competitor_clients() * p21() * _integ_clients() * (1 - p11() - k() * p13() ) / total_population()

def comp_cl():
    return tr() * word_of_mouth_efficiency() * sociability() * _integ_competitor_clients() * p11() * _integ_clients() * (1 - p21() - k() * p23() ) / total_population()


def p11():
    return 0.5
def p13():
    return 0.5
def p21():
    return 0.5
def p23():
    return 0.5

def our_clients_initial():
    return 0

def potential_clients_initial():
    return 100_000

def competitor_clients_initial():
    return 0


_integ_clients = Integ(lambda: our_clients(), lambda: our_clients_initial(), "_integ_clients")
_integ_potential_clients = Integ(lambda: potential_clients(), lambda: potential_clients_initial(), "_integ_potential_clients")
_integ_competitor_clients = Integ(lambda: competitor_clients(), lambda: competitor_clients_initial(), "_integ_competitor_clients")
