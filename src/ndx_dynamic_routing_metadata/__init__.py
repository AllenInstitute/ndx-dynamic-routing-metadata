"""
    Type to store metadata for dynamic routing experiments at Allen Institute
"""

import doctest
import importlib.metadata
import logging

from ndx_dynamic_routing_metadata.pynwb import *
from ndx_dynamic_routing_metadata.spec import *

# import functions from submodules here:
# from ndx_dynamic_routing_metadata.utils import *

logger = logging.getLogger(__name__)

__version__ = importlib.metadata.version("ndx_dynamic_routing_metadata")
logger.debug(f"{__name__}.{__version__ = }")


def testmod(**testmod_kwargs) -> doctest.TestResults:
    """
    Run doctests for the module, configured to ignore exception details and
    normalize whitespace.

    Accepts kwargs to pass to doctest.testmod().

    Add to modules to run doctests when run as a script:
    .. code-block:: text
        if __name__ == "__main__":
            from npc_io import testmod
            testmod()

    """
    _ = testmod_kwargs.setdefault(
        "optionflags", doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    )
    return doctest.testmod(**testmod_kwargs)


if __name__ == "__main__":
    testmod()
