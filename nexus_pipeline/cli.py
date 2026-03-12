import click
from .extractors import SyntheticExtractor, CsvExtractor
from .transformers import DataTransformer
from .reporters import ReportGenerator

@click.group()
@click.version_option("1.0.0")
def main():
    """Nexus: High performance data processing pipeline."""
    pass

@main.command()
@click.option("--sample", is_flag=True, help="Run pipeline on synthetic enterprise sample data")
@click.option("--input-file", "-i", type=click.Path(exists=True), help="Path to source CSV file")
@click.option("--export-md", type=click.Path(), help="Export markdown report to specified path")
def process(sample: bool, input_file: str, export_md: str):
    """Execute ETL processing and output analytics summary."""
    if sample:
        extractor = SyntheticExtractor(count=60)
        click.echo("Extracting synthetic records...")
    elif input_file:
        extractor = CsvExtractor(input_file)
        click.echo(f"Extracting data from {input_file}...")
    else:
        click.echo("Please specify either --sample or --input-file <path>")
        return

    raw_data = extractor.extract()
    transformer = DataTransformer()
    records = transformer.process(raw_data)
    metrics = transformer.aggregate(records)

    report = ReportGenerator.to_terminal(metrics)
    click.echo(report)

    if export_md:
        ReportGenerator.export_markdown(metrics, export_md)
        click.echo(f"Report saved to {export_md}")

if __name__ == "__main__":
    main()


# Path resolution fix
