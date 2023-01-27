"""
The abi3info APIs.
"""

from typing import Final, Dict

from abi3info._internal import (
    _DATAS,
    _FEATURE_MACROS,
    _FUNCTIONS,
    _MACROS,
    _STRUCTS,
    _TYPEDEFS,
)
from abi3info.models import (
    Data,
    FeatureMacro,
    Function,
    Macro,
    Struct,
    Symbol,
    Typedef,
)

__version__ = "2022.12.06-2"
"""
The current version of abi3info.
"""

DATAS: Final[Dict[Symbol, Data]] = _DATAS
"""
Data object members of the limited API and stable ABI.
"""

FEATURE_MACROS: Final[Dict[str, FeatureMacro]] = _FEATURE_MACROS
"""
Feature macros that control the availability of limited API members.
"""

FUNCTIONS: Final[Dict[Symbol, Function]] = _FUNCTIONS
"""
Function members of the limited API and stable ABI.
"""

MACROS: Final[Dict[str, Macro]] = _MACROS
"""
Macro members of the limited API.
"""

STRUCTS: Final[Dict[str, Struct]] = _STRUCTS
"""
Struct members of the limited API.
"""

TYPEDEFS: Final[Dict[str, Typedef]] = _TYPEDEFS
"""
Typedef members of the limited API.
"""
