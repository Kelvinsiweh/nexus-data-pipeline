from tabulate import tabulate
from .models import AggregatedMetrics
from pathlib import Path

class ReportGenerator:
    @staticmethod
    def to_terminal(metrics: AggregatedMetrics) -> str:
        summary_table = [
            ["Total Records Processed", metrics.total_records],
            ["Total Volume (USD)", f"${metrics.total_volume:,.2f}"],
            ["Average Transaction", f"${metrics.average_amount:,.2f}"],
            ["Top Revenue Category", metrics.top_category],
        ]
        out = "\n=== Nexus Pipeline Executive Summary ===\n"
        out += tabulate(summary_table, headers=["Metric", "Value"], tablefmt="fancy_grid") + "\n\n"
        
        cat_table = [[k, f"${v:,.2f}"] for k, v in metrics.category_breakdown.items()]
        out += "--- Category Distribution ---\n"
        out += tabulate(cat_table, headers=["Category", "Total Revenue"], tablefmt="simple") + "\n\n"
        return out

    @staticmethod
    def export_markdown(metrics: AggregatedMetrics, destination: str | Path) -> None:
        path = Path(destination)
        path.parent.mkdir(parents=True, exist_ok=True)
        content = f"# Nexus Pipeline Run Report\n\n"
        content += f"- **Total Records**: {metrics.total_records}\n"
        content += f"- **Total Volume**: ${metrics.total_volume:,.2f}\n"
        content += f"- **Average Amount**: ${metrics.average_amount:,.2f}\n"
        content += f"- **Primary Category**: {metrics.top_category}\n\n"
        content += "## Category Volume\n"
        for cat, val in metrics.category_breakdown.items():
            content += f"- **{cat}**: ${val:,.2f}\n"
        path.write_text(content, encoding="utf-8")
