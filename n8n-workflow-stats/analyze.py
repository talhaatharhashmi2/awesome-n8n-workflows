#!/usr/bin/env python3
"""n8n Workflow Stats Analyzer: scans a folder of n8n workflow JSONs and reports node stats, top integrations, trigger distribution. Usage: python3 analyze.py /path/to/workflows [--out results.json]"""
import json, glob, os, sys
from collections import Counter
from statistics import median
UTIL = {'stickyNote','set','if','switch','code','noOp','merge','splitInBatches','splitOut','filter','wait','limit','sort','html','markdown','respondToWebhook','stopAndError','aggregate','function','executeWorkflow','extractFromFile','convertToFile','readWriteFile','form','redis'}
def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    out = sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == '--out' else None
    files = glob.glob(os.path.join(root, '**/*.json'), recursive=True)
    valid, bad, node_counts = 0, 0, []
    integrations, triggers = Counter(), Counter()
    for f in files:
        try: d = json.load(open(f, encoding='utf-8', errors='ignore'))
        except Exception: bad += 1; continue
        nodes = d.get('nodes') or []
        if not nodes: bad += 1; continue
        valid += 1; node_counts.append(len(nodes))
        for n in nodes:
            t = n.get('type', ''); base = t.split('.')[-1]
            if 'Trigger' in base and base.endswith('Trigger'): triggers[base] += 1
            elif t.startswith('n8n-nodes-base.') and base not in UTIL: integrations[base] += 1
    buckets = Counter()
    for c in node_counts:
        b = min(c // 10 * 10, 50); buckets[f"{b}-{b+9}" if b < 50 else "50+"] += 1
    results = {'files_scanned': len(files), 'valid_workflows': valid, 'invalid': bad,
        'node_stats': {'median': median(node_counts), 'avg': round(sum(node_counts)/len(node_counts), 1), 'min': min(node_counts), 'max': max(node_counts), 'under_20_nodes_pct': round(sum(1 for c in node_counts if c < 20)/len(node_counts)*100, 1), 'distribution': dict(sorted(buckets.items()))},
        'top_integrations': dict(integrations.most_common(20)), 'triggers': dict(triggers.most_common(15))}
    print(json.dumps(results, indent=2))
    if out: json.dump(results, open(out, 'w'), indent=2); print(f"Saved to {out}", file=sys.stderr)
if __name__ == '__main__': main()
