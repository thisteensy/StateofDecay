#!/usr/bin/env python3
"""
Normalize and merge CCC protest data from three phases into ccc_normalized.csv.
- 2017-2020: static file committed to repo (ccc_compiled_20172020_utf8.csv)
- 2021-2024: downloaded from Harvard Dataverse (file ID 10822959)
- 2025-present: downloaded from Harvard Dataverse (file ID 13448233)
"""

import csv
import io
import os
import sys
import urllib.request
from datetime import datetime

DATAVERSE_BASE = "https://dataverse.harvard.edu/api/access/datafile"
FILE_2021_2024 = "10822959"
FILE_2025 = "13448233"

FIELDNAMES = ['date', 'city', 'state', 'event_type', 'macro_event',
              'size_low', 'size_high', 'arrests', 'lat', 'lon', 'claims']


def parse_date(d):
    if not d or d.strip() in ('NA', ''):
        return ''
    d = d.strip()
    for fmt in ('%Y-%m-%d', '%m/%d/%Y', '%Y/%m/%d'):
        try:
            return datetime.strptime(d, fmt).strftime('%Y-%m-%d')
        except ValueError:
            continue
    return ''


def normalize_2017(row):
    return {
        'date': parse_date(row.get('date', '')),
        'city': row.get('locality', ''),
        'state': row.get('state', ''),
        'event_type': row.get('type', ''),
        'macro_event': row.get('macroevent', ''),
        'size_low': row.get('size_low', ''),
        'size_high': row.get('size_high', ''),
        'arrests': row.get('arrests', ''),
        'lat': row.get('lat', ''),
        'lon': row.get('lon', ''),
        'claims': row.get('claims', ''),
    }


def normalize_2021(row):
    return {
        'date': parse_date(row.get('date', '')),
        'city': row.get('locality', ''),
        'state': row.get('state', ''),
        'event_type': row.get('type', ''),
        'macro_event': row.get('macroevent', ''),
        'size_low': row.get('size_low', ''),
        'size_high': row.get('size_high', ''),
        'arrests': row.get('arrests', ''),
        'lat': row.get('lat', ''),
        'lon': row.get('lon', ''),
        'claims': row.get('claims_verbatim', ''),
    }


def normalize_2025(row):
    return {
        'date': parse_date(row.get('date', '')),
        'city': row.get('locality', ''),
        'state': row.get('state', ''),
        'event_type': row.get('event_type', ''),
        'macro_event': row.get('macroevent', ''),
        'size_low': row.get('size_low', ''),
        'size_high': row.get('size_high', ''),
        'arrests': row.get('arrests', ''),
        'lat': row.get('lat', ''),
        'lon': row.get('lon', ''),
        'claims': row.get('claims_verbatim', ''),
    }


def read_local(path, normalizer, delimiter=','):
    rows = []
    with open(path, encoding='utf-8', errors='replace') as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        for row in reader:
            rows.append(normalizer(row))
    print(f"  {path}: {len(rows)} rows")
    return rows


def download_and_read(file_id, normalizer, delimiter='\t'):
    url = f"{DATAVERSE_BASE}/{file_id}"
    print(f"  Downloading file ID {file_id} from Dataverse...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=120) as response:
        raw = response.read().decode('utf-8', errors='replace')
    reader = csv.DictReader(io.StringIO(raw), delimiter=delimiter)
    rows = [normalizer(row) for row in reader]
    print(f"  File ID {file_id}: {len(rows)} rows")
    return rows


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    static_2017 = os.path.join(script_dir, 'ccc_compiled_20172020_utf8.csv')
    output_path = os.path.join(script_dir, 'ccc_normalized.csv')

    all_rows = []

    # 2017-2020: static local file
    print("Reading 2017-2020 static file...")
    all_rows += read_local(static_2017, normalize_2017, delimiter=',')

    # 2021-2024: download from Dataverse
    print("Downloading 2021-2024 data...")
    try:
        all_rows += download_and_read(FILE_2021_2024, normalize_2021, delimiter='\t')
    except Exception as e:
        print(f"  ERROR downloading 2021-2024: {e}", file=sys.stderr)
        sys.exit(1)

    # 2025-present: download from Dataverse
    print("Downloading 2025-present data...")
    try:
        all_rows += download_and_read(FILE_2025, normalize_2025, delimiter=',')
    except Exception as e:
        print(f"  ERROR downloading 2025-present: {e}", file=sys.stderr)
        sys.exit(1)

    # Write output
    print(f"\nWriting {len(all_rows)} rows to {output_path}...")
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(all_rows)

    # Summary
    dates = [r['date'] for r in all_rows if r['date']]
    print(f"Date range: {min(dates)} to {max(dates)}")
    print("Done.")


if __name__ == '__main__':
    main()