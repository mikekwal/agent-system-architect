#!/usr/bin/env python3
"""Validate that the portable package is coherent and example JSON conforms to schemas.
Requires jsonschema (pip install jsonschema), otherwise standard-library checks still run.
This script performs no network requests or external mutations.
"""
from pathlib import Path
import json, re, sys
base=Path(__file__).resolve().parent.parent
required=['README.md','00_START_HERE.md','AGENTIC_AI_ANATOMY.md',
'contracts/agent-spec.schema.json','contracts/agent-spec.example.json',
'contracts/run-result.schema.json','contracts/run-result.example.json',
'claude-code/HANDOFF_PROMPT.md','diagrams/01_NINE_PART_SPINE.mmd']
for p in required:
    assert (base/p).is_file(), f'missing {p}'
for p in (base/'contracts').glob('*.json'):
    json.loads(p.read_text(encoding='utf-8'))
try:
    from jsonschema import Draft202012Validator, validate
except ImportError:
    print('jsonschema unavailable; only JSON syntax validated')
else:
    for name in ['agent-spec','run-result']:
        schema=json.loads((base/'contracts'/f'{name}.schema.json').read_text(encoding='utf-8'))
        example=json.loads((base/'contracts'/f'{name}.example.json').read_text(encoding='utf-8'))
        Draft202012Validator.check_schema(schema)
        validate(instance=example,schema=schema)
        print('schema valid:',name)
for p in list(base.rglob('*.md'))+list(base.rglob('*.yaml')):
    content=p.read_text(encoding='utf-8')
    for bad in ['AI BDR','Content OS','social media marketing','MK-Way']:
        assert bad.lower() not in content.lower(), f'domain-bound phrase {bad!r} in {p}'
print('PASS — package is neutral, examples valid, core assets present')
