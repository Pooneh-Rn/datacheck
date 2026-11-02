"""Custom exceptions used throughout DataCheck."""


class DataCheckError(Exception):
    """Base exception for DataCheck."""


class DatasetNotFoundError(DataCheckError):
    """Raised when the input dataset does not exist."""


class UnsupportedFormatError(DataCheckError):
    """Raised when the input file format is unsupported."""


class DatasetLoadError(DataCheckError):
    """Raised when a dataset cannot be loaded."""


class EmptyDatasetError(DataCheckError):
    """Raised when the input dataset contains no usable data."""
