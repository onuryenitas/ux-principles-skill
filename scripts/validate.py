"""Offline release-integrity and behavioral lookup checks (standard library only)."""
import importlib.util
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse, unquote
root = Path(__file__).resolve().parents[1]
skill = root / 'skills/ux-principles'
refs = skill / 'references'
manifest = json.loads((refs/'catalog.json').read_text())
assert (root/'VERSION').read_text().strip() == manifest['version']
records=[]
for c in manifest['collections']:
    path=(refs/c['file']).resolve()
    assert path.is_relative_to(refs.resolve())
    rows=json.loads(path.read_text())[c['key']]
    assert len(rows)==c['count'],c['file']
    assert all(r['kind']==c['kind'] for r in rows)
    records.extend(rows)
assert len(records)==manifest['total_records']
by_id={r['id']:r for r in records}
assert len(by_id)==len(records),'Duplicate IDs'
allowed={'lawsofux.com','www.nngroup.com','www.w3.org','design-system.service.gov.uk','www.gov.uk','web.dev','www.microsoft.com'}
for r in records:
    for k in ['id','kind','name','category','explanation','action','check','caution','source_url','reviewed_on']:
        assert isinstance(r.get(k),str) and r[k].strip(),(r['id'],k)
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}',r['reviewed_on'])
    u=urlparse(r['source_url']);assert u.scheme=='https' and u.netloc in allowed,r['id']
    if r['kind']=='workflow':
        assert len(r['states'])>=3 and r['aliases'],r['id']
        assert r['related_ids'] and all(i in by_id for i in r['related_ids']),r['id']
wc=[r for r in records if r['kind']=='standard']
assert dict(Counter(r['level'] for r in wc))==manifest['wcag_levels']
assert 'wcag-4.1.1' not in by_id
assert len([r for r in wc if r['level'] in ['A','AA']])==55
for r in wc:
    assert r['id']=='wcag-'+r['criterion']
    assert urlparse(r['source_url']).fragment
    assert r['understanding_url'].startswith('https://www.w3.org/WAI/WCAG22/Understanding/')
evidence=json.loads((root/'docs/coverage-evidence.json').read_text())
assert set(evidence['wcag_active_ids'])=={r['criterion'] for r in wc}
assert set(evidence['apg_pattern_ids'])=={r['id'] for r in records if r['kind']=='component'}
assert {r['id']:r['source_url'] for r in evidence['records']}=={r['id']:r['source_url'] for r in records}
comparison=json.loads((refs/'source-comparison.json').read_text())['matches']
assert len(comparison)==len({r['principle_id'] for r in comparison})==21
assert all(r['principle_id'] in by_id for r in comparison)
articles=json.loads((refs/'articles.json').read_text())['articles']
assert len(articles)==manifest['reading_routes']
assert all(a['principle_ids'] and all(by_id[i]['kind']=='principle' for i in a['principle_ids']) for a in articles)
for path in root.rglob('*.md'):
    content=path.read_text()
    for target in re.findall(r'\]\(([^)]+)\)',content):
        if '://' in target or target.startswith('#'):continue
        local=(path.parent/unquote(target.split('#')[0])).resolve()
        assert local.is_relative_to(root.resolve()) and local.exists(),(path,target)
    assert '/Users/' not in content and '/tmp/' not in content,path
spec=importlib.util.spec_from_file_location('lookup',skill/'scripts/lookup.py')
lookup=importlib.util.module_from_spec(spec);spec.loader.exec_module(lookup)
loaded=lookup.load_records()
assert len(lookup.select(loaded,target='AA'))==55
assert len(lookup.select(loaded,level='AA'))==24
assert len(lookup.select(loaded,target='AAA'))==86
assert lookup.select(loaded,record_id='wcag-2.5.8')[0]['level']=='AA'
assert lookup.select(loaded,record_id='wcag-2.5.5')[0]['level']=='AAA'
assert {r['id'] for r in lookup.select(loaded,query='ŞİFRE')}=={'flow-authentication'}
assert {r['id'] for r in lookup.select(loaded,query='şifre')}=={'flow-authentication'}
assert {r['id'] for r in lookup.select(loaded,query='YAPAY ZEKA')}=={'flow-ai-interaction'}
assert not lookup.select(loaded,query='zzzznoresult')
assert not lookup.select(loaded,kind='principle',target='AA')
# Invoke from outside repository: resolution must not depend on working directory.
result=subprocess.run([sys.executable,str(skill/'scripts/lookup.py'),'--target','AA','--json'],cwd=root.parent,capture_output=True,text=True,check=True)
assert json.loads(result.stdout)['count']==55
missing=subprocess.run([sys.executable,str(skill/'scripts/lookup.py'),'--id','missing','--json'],capture_output=True,text=True)
assert missing.returncode==1 and json.loads(missing.stdout)['count']==0
cases=json.loads((root/'evals/cases.json').read_text())['cases']
assert len({c['id'] for c in cases})==len(cases)
assert all(c['prompt'] and c['criteria'] for c in cases)
print(f'PASS: {len(records)} records, {len(articles)} article routes, 21 source matches; coverage, IDs, links, portability, WCAG level semantics and CLI behavior.')
