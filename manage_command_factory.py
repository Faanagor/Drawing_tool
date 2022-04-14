from abc import ABC, abstractmethod


class ManageCommandFactory(ABC):
    @abstractmethod
    def find_points(self):
        """find points from list_command to create """
        raise NotImplementedError

    @abstractmethod
    def create(self):
        """Create drawingTool o write in drawingTool"""
        raise NotImplementedError

    @abstractmethod
    def print_canvas(self):
        """Print Canvas created
        """
        raise NotImplementedError
