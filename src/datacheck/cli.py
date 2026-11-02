import typer

from datacheck import __version__
from datacheck.exceptions import DataCheckError
from datacheck.loader import DatasetLoader

app = typer.Typer(
    name="datacheck",
    help="Automated dataset quality analysis.",
    no_args_is_help=True,
)


@app.command()
def analyze(
    file_path: str = typer.Argument(
        ...,
        help="Path to the CSV dataset.",
    ),
) -> None:
    """Load a dataset and display basic information."""

    typer.echo(f"DataCheck v{__version__}")
    typer.echo(f"\nLoading dataset: {file_path}\n")

    loader = DatasetLoader()

    try:
        dataframe = loader.load(file_path)

    except DataCheckError as exc:
        typer.secho(
            f"Error: {exc}",
            fg=typer.colors.RED,
            err=True,
        )
        raise typer.Exit(code=1) from exc

    row_count, column_count = dataframe.shape

    memory_usage = dataframe.memory_usage(
        index=True,
        deep=True,
    ).sum()

    memory_kb = memory_usage / 1024

    typer.secho(
        "Dataset loaded successfully!",
        fg=typer.colors.GREEN,
        bold=True,
    )

    typer.echo(f"\nRows:    {row_count:,}")
    typer.echo(f"Columns: {column_count:,}")
    typer.echo(f"Memory:  {memory_kb:.2f} KB")

    typer.echo("\nColumns:")

    for column in dataframe.columns:
        typer.echo(f"  - {column}")


@app.command()
def version():
    typer.echo(f"DataCheck v{__version__}")


if __name__ == "__main__":
    app()
