from pathlib import Path

import pandas as pd

from datacheck.exceptions import (
    DatasetLoadError,
    DatasetNotFoundError,
    EmptyDatasetError,
    UnsupportedFormatError,
)


class DatasetLoader:

    SUPPORTED_FORMATS = {".csv"}

    def load(self, file_path: str | Path) -> pd.DataFrame:
        """Load a CSV dataset and return a pandas DataFrame."""

        path = Path(file_path)

        # 1. Validate file existence.
        if not path.exists():
            raise DatasetNotFoundError(
                f"Dataset not found: {path}"
            )

        # 2. Validate that the path points to a file.
        if not path.is_file():
            raise DatasetLoadError(
                f"Input path is not a file: {path}"
            )

        # 3. Validate file format.
        if path.suffix.lower() not in self.SUPPORTED_FORMATS:
            raise UnsupportedFormatError(
                f"Unsupported file format: {path.suffix}. "
                "Currently supported: CSV."
            )

        # 4. Check whether the file is empty.
        if path.stat().st_size == 0:
            raise EmptyDatasetError(
                f"Dataset is empty: {path}"
            )

        # 5. Load the dataset.
        try:
            dataframe = pd.read_csv(
                path,
                encoding="utf-8-sig",
            )

        except pd.errors.EmptyDataError as exc:
            raise EmptyDatasetError(
                f"No tabular data found in: {path}"
            ) from exc

        except UnicodeDecodeError as exc:
            raise DatasetLoadError(
                "Unable to decode CSV using UTF-8 encoding. "
                "Please check the file encoding."
            ) from exc

        except pd.errors.ParserError as exc:
            raise DatasetLoadError(
                f"Unable to parse CSV file: {path}"
            ) from exc

        except OSError as exc:
            raise DatasetLoadError(
                f"Unable to read file: {path}"
            ) from exc

        # 6. Validate the resulting DataFrame.
        if len(dataframe.columns) == 0:
            raise EmptyDatasetError(
                "Dataset does not contain any columns."
            )

        return dataframe