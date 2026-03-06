import argparse
from pathlib import Path
from loader import load_environment_lists
from treat import make_presence_table
from exporter import export_to_excel, export_to_csv

def main():
    p = argparse.ArgumentParser(__doc__)
    p.add_argument("data_dir", type=Path,
                   help="Directory containing .xlsx/.csv files")
    p.add_argument("--format", choices=["excel","csv"], default="excel")
    p.add_argument("--output", type=Path, default=Path("complist.xlsx"))    
    args = p.parse_args()

    env_lists = load_environment_lists(args.data_dir)
    presence = make_presence_table(env_lists)

    if args.format == "excel":
        export_to_excel(presence, args.output)
    else:
        export_to_csv(presence, args.output)

    print(f"Written presence table to {args.output}")

if __name__ == "__main__":
    main()
