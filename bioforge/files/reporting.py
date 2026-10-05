import os


def annotate_orfs(orfs):
    number = 1
    for orf in orfs:
        orf.id = f"BFG_{number:03d}"
        number = number + 1


def write_report(orfs, output_directory, run_id):
    os.makedirs(output_directory, exist_ok=True)
    report_name = f"report_{run_id}.txt"
    report_path = os.path.join(output_directory, report_name)

    with open(report_path, "w", encoding="utf-8") as report:
        for orf in orfs:
            if orf.is_complete:
                status = "Complete"
            else:
                status = "Incomplete"

            report.write(f"ID: {orf.id}\n")
            report.write(f"Strand: {orf.strand}\n")
            report.write(f"Frame: {orf.frame}\n")
            report.write(f"Start Position: {orf.start_pos}\n")
            report.write(f"Protein: {orf.protein}\n")
            report.write(f"Status: {status}\n\n")
