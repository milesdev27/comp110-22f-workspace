"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730615836"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, cells: Point) -> int:
        """Calculates the distance between two cells."""
        x_value: int = (self.x - cells.x) ** 2
        y_value: int = (self.y - cells.y) ** 2
        return sqrt(x_value + y_value)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Moves through the simulation."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness == constants.RECOVERY_PERIOD:
            self.immunize()

    def contract_disease(self):
        """Assigns sickness to INFECTED."""
        self.sickness = constants.INFECTED

    def immunize(self):
        """Assigns sickness to IMMUNE."""
        self.sickness = constants.IMMUNE

    def is_vulnerable(self):
        """Returns if a cell is vulnerable."""
        if self.sickness == 0:
            return True
        else:
            return False

    def is_infected(self):
        """Returns if a cell is infected."""
        if self.sickness >= 1:
            return True
        else:
            return False

    def is_immune(self):
        """Returns if a cell is immune."""
        if self.sickness <= -1:
            return True
        else:
            return False

    def color(self) -> None:
        """Assigns colors to different types of cells."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "orange"
        elif self.is_immune():
            return "green"

    def contact_with(self, cell: Point) -> None:
        """Infects a vulnerable cell if it comes in contact with an infected cell."""
        if self.is_vulnerable() and cell.is_infected():
            self.contract_disease()
        if self.is_infected() and cell.is_vulnerable():
            cell.contract_disease()
    

class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        if infected <= 0:
            raise ValueError("Number of infected cells is less than 0.")
        if immune < 0:
            raise ValueError("Number of immune cells is less than 0.")
        if infected + immune >= len(self.population):
            raise ValueError("Number of infected and immune cells is greater than the total number of cells.")
        for i in range(infected):
            self.population[i].contract_disease()
        for j in range(immune):
            self.population[j].immunize()
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self):
        """Checks if two cells come into contact."""
        for i in range(0, len(self.population)):
            for j in range(i + 1, len(self.population)):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        result: bool = False
        for i in self.population:
            if i.is_infected():
                result = False
                return result
            else:
                result = True
        return result