#!/usr/bin/env python3
"""Dependency-free local catalog lookup; no network, writes or model calls."""
import argparse
import json
import sys
import unicodedata
from pathlib import Path

REFS = Path(__file__).resolve().parents[1] / 'references'

def normalize(value):
    # Lexical search only. Fold accents and Turkish dotted/dotless I.
    value = str(value).replace('ı', 'i').replace('İ', 'I').casefold()
    return ''.join(c for c in unicodedata.normalize('NFKD', value)
                   if not unicodedata.combining(c))

def load_records():
    manifest = json.loads((REFS / 'catalog.json').read_text(encoding='utf-8'))
    records = []
    for collection in manifest['collections']:
        data = json.loads((REFS / collection['file']).read_text(encoding='utf-8'))
        records.extend(data[collection['key']])
    return records

def select(records, query='', kind=None, level=None, target=None, record_id=None):
    terms = normalize(query).split()
    allowed = {'A': {'A'}, 'AA': {'A', 'AA'}, 'AAA': {'A', 'AA', 'AAA'}}
    return [r for r in records
            if (not record_id or r['id'] == record_id)
            and (not kind or r['kind'] == kind)
            and (not level or r.get('level') == level)
            and (not target or r.get('level') in allowed[target])
            and all(t in normalize(json.dumps(r, ensure_ascii=False)) for t in terms)]

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--query', default='', help='Words; all must match, accent-insensitive')
    p.add_argument('--id', dest='record_id', help='Exact stable record ID')
    p.add_argument('--kind', choices=['principle','heuristic','standard','component','workflow'])
    levels = p.add_mutually_exclusive_group()
    levels.add_argument('--level', choices=['A','AA','AAA'], help='Exact WCAG level only')
    levels.add_argument('--target', choices=['A','AA','AAA'], help='WCAG target including lower levels')
    p.add_argument('--json', action='store_true', help='Print full records as JSON')
    args = p.parse_args()
    result = select(load_records(), args.query, args.kind, args.level, args.target, args.record_id)
    if args.json:
        print(json.dumps({'count':len(result),'records':result}, ensure_ascii=False, indent=2))
    else:
        print(f'{len(result)} matching records')
        for r in result:
            print(f"\n{r['id']} — {r['name']} [{r['kind']}{' / '+r['level'] if 'level' in r else ''}]")
            print(r['explanation'])
            print('Action: '+r['action'])
            print('Check: '+r['check'])
            print('Caution: '+r['caution'])
            print('Source: '+r['source_url'])
    return 1 if args.record_id and not result else 0

if __name__ == '__main__':
    sys.exit(main())
