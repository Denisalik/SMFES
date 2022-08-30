"""
Python model 'Predator_Prey.py'
Translated using PySD
"""

from pathlib import Path

from scipy import interpolate

from pysd.py_backend.statefuls import Integ

__pysd_version__ = "2.2.4"

__data = {"scope": None, "time": lambda: 0}

_root = Path(__file__).parent

_subscript_dict = {}

_namespace = {
    "TIME": "time",
    "Time": "time",
    "Area": "area",
    "Initial Lynx Population": "initial_lynx_population",
    "Initial Hare Population": "initial_hare_population",
    "Lynx Births": "lynx_births",
    "Lynx Deaths": "lynx_deaths",
    "Lynx Mortality": "lynx_mortality",
    "Lynx Natality": "lynx_natality",
    "Lynx": "lynx",
    "Hare": "hare",
    "Hare Births": "hare_births",
    "Hare Deaths": "prey_deaths",
    "Hare Natality": "hare_natality",
    "FINAL TIME": "final_time",
    "INITIAL TIME": "initial_time",
    "SAVEPER": "saveper",
    "TIME STEP": "time_step",
    "q1": "q1",
    "q2": "q2",
    "Lynx Hunted": "lynx_hunted",
    "Hare Hunted": "hare_hunted",
    "Initial Wolves Population": "initial_wolves_population",
    "Wolves": "wolves",
    "Wolves Birth Rate": "wolves_birth_rate",
    "Wolves Deaths": "wolves_deaths",
    "Translate Population To Density": "translate_population_to_density",
    "Lynx Deaths By Wolves Efficiency": "lynx_deaths_by_wolves_efficiency",
    "Hare Deaths By Wolves Efficiency": "hare_deaths_by_wolves_efficiency",
    "Lynx Deaths By Wolves": "lynx_deaths_by_wolves",
    "Hare Deaths By Wolves": "hare_deaths_by_wolves",
    "r": "r",
    "Lynx Births By Scavenging": "lynx_births_by_scavenging"
}

_dependencies = {
    "r": {},
    "lynx_births_by_scavenging": {"r": 1, "wolves_deaths": 1},
    "lynx_deaths_by_wolves": {"lynx_deaths_by_wolves_efficiency": 1, "wolves": 1},
    "hare_deaths_by_wolves": {"hare_deaths_by_wolves_efficiency": 1, "wolves": 1},
    "lynx_deaths_by_wolves_efficiency": {},
    "hare_deaths_by_wolves_efficiency": {},
    "initial_wolves_population": {},
    "translate_population_to_density": {"hare": 1, "lynx": 1, "area": 1},
    "wolves": {"_integ_wolves": 1},
    "_integ_wolves": {
        "initial": {"initial_wolves_population": 1},
        "step": {"wolves_birth_rate": 1, "wolves_deaths": 1}
    },
    "wolves_birth_rate": {},
    "wolves_deaths": {"translate_population_to_density": 1, "wolves": 1},
    "lynx_hunted": {"q1": 1, "lynx": 1},
    "hare_hunted": {"q2": 1, "hare": 1},
    "q1": {},
    "q2": {},
    "area": {},
    "initial_lynx_population": {},
    "initial_hare_population": {},
    "lynx_births": {
        "lynx": 1,
        "lynx_natality": 1,
    },
    "lynx_deaths": {
        "lynx": 1,
        "lynx_mortality": 1,
    },
    "lynx_mortality": {"hare_density": 1},
    "lynx_natality": {},
    "lynx": {"_integ_lynx": 1},
    "hare": {"_integ_hare": 1},
    "hare_births": {"hare": 1, "hare_natality": 1},
    "hare_deaths": {"hare_density": 1, "lynx": 1},
    "hare_density": {"hare": 1, "area": 1},
    "hare_natality": {},
    "final_time": {},
    "initial_time": {},
    "saveper": {"time_step": 1},
    "time_step": {},
    "_integ_lynx": {
        "initial": {"initial_lynx_population": 1},
        "step": {"lynx_births": 1, "lynx_births_by_scavenging": 1, "lynx_deaths": 1, "lynx_hunted": 1,
                 "lynx_deaths_by_wolves": 1},
    },
    "_integ_hare": {
        "initial": {"initial_hare_population": 1},
        "step": {"hare_births": 1, "hare_deaths": 1, "hare_hunted": 1, "hare_deaths_by_wolves": 1},
    },
}

##########################################################################
#                            CONTROL VARIABLES                           #
##########################################################################

_control_vars = {
    "initial_time": lambda: 0,
    "final_time": lambda: 50,
    "time_step": lambda: 0.0625,
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
    Original Eqn: 50
    Units: Day
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
    Units: Day
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
    Units: Day
    Limits: (0.0, None)
    Type: component
    Subs: None

    The frequency with which output is stored.
    """
    return __data["time"].saveper()


def time_step():
    """
    Real Name: TIME STEP
    Original Eqn: 0.0625
    Units: Day
    Limits: (0.0, None)
    Type: constant
    Subs: None

    The time step for the simulation.
    """
    return __data["time"].time_step()


##########################################################################
#                             MODEL VARIABLES                            #
##########################################################################

x_points = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
y_points = [0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0.005]
tck = interpolate.splrep(x_points, y_points)

# tabular function for wolves
x_points_wolves = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
y_points_wolves = [i / 2 for i in y_points]
tck_wolves = interpolate.splrep(x_points_wolves, y_points_wolves)


def q1():
    return 0.1


def q2():
    return 0.1


def r():
    return 0.1


def lynx_hunted():
    """
    Real Name: Lynx Deaths caused by hunters
    Original Eqn: Lynx * Coefficient of Lynx Mortality Caused By Hunters
    Units: Lynx/Year
    Limits: (None, None)
    Type: component
    Subs: None

    """
    return q1() * lynx()


def lynx_births_by_scavenging():
    """
    Real Name: Lynx Feed By Scavenging Wolves
    Original Eqn: r * Death Number Of Wolves Now
    Units: Lynx/Year
    Limits: (None, None)
    Type: component
    Subs: None

    """
    return r() * wolves_deaths()


def hare_hunted():
    """
    Real Name: Hares Deaths caused by hunters
    Original Eqn: Hares * Coefficient of Hares Mortality Caused By Hunters
    Units: Hares/Year
    Limits: (None, None)
    Type: component
    Subs: None

    """
    return q2() * hare()


def initial_wolves_population():
    return 150


def wolves():
    return _integ_wolves()


def wolves_birth_rate():
    return 10


def wolves_deaths():
    if translate_population_to_density() > 100:
        deaths = y_points_wolves[-1]
    elif translate_population_to_density() >= 0:
        deaths = interpolate.splev(translate_population_to_density(), tck_wolves)
    else:
        deaths = y_points_wolves[0]
    # number of wolves cannot be negative
    return min(deaths * wolves(), wolves())


def translate_population_to_density():
    return (hare() + 10 * lynx()) / area()


def lynx_deaths_by_wolves_efficiency():
    return 0.01


def hare_deaths_by_wolves_efficiency():
    return 0.1


def lynx_deaths_by_wolves():
    """
    Real Name: Lynx Deaths caused by hunters
    Original Eqn: Lynx * Coefficient of Lynx Mortality Caused By Hunters
    Units: Lynx/Year
    Limits: (None, None)
    Type: component
    Subs: None

    """
    return lynx_deaths_by_wolves_efficiency() * wolves()


def hare_deaths_by_wolves():
    """
    Real Name: Hares Deaths caused by hunters
    Original Eqn: Hares * Coefficient of Hares Mortality Caused By Hunters
    Units: Hares/Year
    Limits: (None, None)
    Type: component
    Subs: None

    """
    return hare_deaths_by_wolves_efficiency() * wolves()


def area():
    """
    Real Name: Area
    Original Eqn: 100
    Units:
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 100


def initial_lynx_population():
    """
    Real Name: Initial Lynx Population
    Original Eqn: 125
    Units:
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 125


def initial_hare_population():
    """
    Real Name: Initial Hare Population
    Original Eqn: 6000
    Units:
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 6000


def lynx_births():
    """
    Real Name: Lynx Births
    Original Eqn: Lynx * Lynx Natality
    Units: Lynx/Year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return lynx() * lynx_natality()


def lynx_deaths():
    """
    Real Name: Lynx Deaths
    Original Eqn: Lynx * Lynx Mortality
    Units: Lynx/Year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return lynx() * lynx_mortality()


def lynx_mortality():
    """
    Real Name: Lynx Mortality
    Original Eqn: Table Function
    Units: Years
    Limits: (0.005, 0.5)
    Type: component
    Subs: None


    """
    if hare_density() > 100:
        return 0.005
    elif hare_density() >= 0:
        return interpolate.splev(hare_density(), tck)
    else:
        return 0.5


def lynx_natality():
    """
    Real Name: Lynx Natality
    Original Eqn: 0.25
    Units: Lynx/Lynx/Year
    Limits: 0.25
    Type: constant
    Subs: None

    """
    return 0.25


def lynx():
    """
    Real Name: Lynx
    Original Eqn: INTEG (Lynx Births-Lynx Deaths, Initial Lynx Population)
    Units: Lynx
    Limits: (0.0, None)
    Type: component
    Subs: None


    """
    return _integ_lynx()


def hare():
    """
    Real Name: Hare
    Original Eqn: INTEG (Hare Births-Hare Deaths, Initial Hare Population)
    Units: Hares
    Limits: (0.0, None)
    Type: component
    Subs: None


    """
    return _integ_hare()


def hare_births():
    """
    Real Name: Hare Births
    Original Eqn: Hare * Hare Natality
    Units: Hares/Year
    Limits: (0.0, None)
    Type: component
    Subs: None


    """
    return max(hare(), 0) * hare_natality()


def hare_deaths():
    """
    Real Name: Hare Deaths
    Original Eqn: Hare Density * Lynx
    Units: Hares/Year
    Limits: (0.0, None)
    Type: component
    Subs: None


    """
    return hare_density() * lynx()


def hare_density():
    """
    Real Name: Hare Density
    Original Eqn: Hare / Area
    Units: Hares/Square
    Limits: (0.0, None)
    Type: component
    Subs: None


    """
    return hare() / area()


def hare_natality():
    """
    Real Name: Hare Natality
    Original Eqn: 1.25
    Units: Hare/Hare/Year
    Limits: 1.25
    Type: constant
    Subs: None

    """
    return 1.25


_integ_lynx = Integ(
    lambda: lynx_births() + lynx_births_by_scavenging() - lynx_deaths() - lynx_hunted() - lynx_deaths_by_wolves(),
    lambda: initial_lynx_population(),
    "_integ_prey_population"
)

_integ_hare = Integ(
    lambda: hare_births() - hare_deaths() - hare_hunted() - hare_deaths_by_wolves(),
    lambda: initial_hare_population(),
    "_integ_predator_population",
)

_integ_wolves = Integ(
    lambda: wolves_birth_rate() - wolves_deaths(),
    lambda: initial_wolves_population(),
    "_integ_wolves_population",
)
