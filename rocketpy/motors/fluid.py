from dataclasses import dataclass

from ..mathutils.function import Function, funcify_method
from ..plots.fluid_plots import _FluidPlots
from ..prints.fluid_prints import _FluidPrints


@dataclass
class Fluid:
    """Class that represents a fluid.

    Attributes
    ----------
    name : str
        Name of the fluid.
    density : Function
        Density of the fluid in kg/m³ over s.
    """
    name: str
    density : Function

    def __init__(self, name, density):
        """Initialization method."""

        if not isinstance(name, str):
            raise ValueError("The name must be a string.")

        # ... (Any other validation you need for the density)

        self.name = name
        self.density = Function(
            density,
            inputs="Time (s)",
            outputs="Density (kg/m^3)",
            interpolation="linear",
            extrapolation="zero",
        )

    def __post_init__(self):
        """Post initialization method.

        Raises
        ------
        ValueError
            If the name is not a string.
        ValueError
            If the density is not a positive number.
        """

        if not isinstance(self.name, str):
            raise ValueError("The name must be a string.")
        if self.density < 0:
            raise ValueError("The density must be a positive number.")

        # Initialize plots and prints object
        self.prints = _FluidPrints(self)
        self.plots = _FluidPlots(self)
        return None

    def __repr__(self):
        """Representation method.

        Returns
        -------
        str
            String representation of the class.
        """

        return f"Fluid(name={self.name}, density={self.density})"

    def __str__(self):
        """String method.

        Returns
        -------
        str
            String representation of the class.
        """

        return f"Fluid: {self.name}"
