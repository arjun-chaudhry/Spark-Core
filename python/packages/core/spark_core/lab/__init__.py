# Copyright (c) Microsoft. All rights reserved.

"""Lab namespace package for experimental Spark Core integrations.

This module extends the package path so experimental lab integrations can be
distributed in separate packages under the ``spark_core.lab`` namespace.
"""

# This makes spark_core.lab a namespace package
__path__ = __import__("pkgutil").extend_path(__path__, __name__)
