import os


def annotate_orfs(orfs):
    for number, orf in enumerate(orfs, start=1):
        orf_id = f"BFG_{number:03d}"
        if isinstance(orf, dict):
            orf["id"] = orf_id
        else:
            orf.id = orf_id
    return orfs


def write_report(orfs, output_directory):
    os.makedirs(output_directory, exist_ok=True)
    report_path = os.path.join(output_directory, "report.txt")

    with open(report_path, "w", encoding="utf-8") as report:
        for orf in orfs:
            status = "Complete" if _value(orf, "is_complete") else "Incomplete"
            report.write(f"ID: {_value(orf, 'id')}\n")
            report.write(f"Strand: {_value(orf, 'strand')}\n")
            report.write(f"Frame: {_value(orf, 'frame')}\n")
            report.write(f"Start Position: {_value(orf, 'start_pos')}\n")
            report.write(f"Protein: {_value(orf, 'protein')}\n")
            report.write(f"Status: {status}\n\n")

    return report_path


def _value(orf, name):
    if isinstance(orf, dict):
        return orf[name]
    return getattr(orf, name)
