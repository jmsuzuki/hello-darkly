from enum import Enum
from abc import ABCMeta, abstractmethod


class IFeature(metaclass=ABCMeta):
    FEATURE_NAME: str

    # @abstractmethod
    # def ingest(self, *args, **kwargs):
    #     pass


