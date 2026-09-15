#!/usr/bin/env python3
"""Validate source coverage, translations, routes, hashes, and Markdown links."""
import argparse
import hashlib
import json
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--update-hashes", action="store_true", help="Refresh translation hashes after all other checks pass")
args = parser.parse_args()
errors = []
def require(condition, message):
    if not condition:
        errors.append(message)
def read_json(path):
    return json.loads((ROOT / path).read_text())
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def branded_path(path):
    return re.sub(r'(?<![A-Za-z0-9])dust(?![A-Za-z0-9])', 'counso', path, flags=re.I)
def check_title(file, entry):
    if file.suffix == '.json':
        payload = json.loads(file.read_text())
        title = payload.get('info', {}).get('title') or payload.get('info', {}).get('name') or payload.get('name')
        require(entry.get('title') == title, 'Download title differs from artifact: ' + str(file.relative_to(ROOT)))
        return
    headings = re.findall(r'^# (.+)$', file.read_text(), re.M)
    require(len(headings) == 1 and entry.get('title') == headings[0], 'Display title differs from article: ' + str(file.relative_to(ROOT)))
def strip_code(text):
    return re.sub(r'^\s*(```|~~~).*?^\s*\1\s*$', '', text, flags=re.M | re.S)
def canonical_path(row):
    if row['original_repository_path'].endswith('.json'):
        return '/' + branded_path(row['original_repository_path'])
    return branded_path(urllib.parse.urlparse(row['original_url']).path)
def anchors(text):
    names = set(re.findall(r'<(?:a|span)\s+(?:id|name)=[\'"]([^\'"]+)', text))
    counts = Counter()
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', strip_code(text), re.M):
        clean = re.sub(r'<[^>]+>', '', heading)
        clean = re.sub(r'\[([^]]+)\]\([^)]+\)', r'\1', clean)
        clean = re.sub(r'[^\w\-\s]', '', clean.lower()).replace(' ', '-')
        suffix = '' if counts[clean] == 0 else '-' + str(counts[clean])
        counts[clean] += 1
        names.add(clean + suffix)
    return names

data = read_json('translations.json')
index = read_json('source/url-index.json')
manifest = read_json('source/manifest.json')
source_titles = {r['path']: r['title'] for r in manifest}
require(data['schema_version'] == 3, 'Unexpected mapping version')
require(data['publication'].get('route_policy') == 'counso-brand-slugs-with-legacy-redirects', 'Unexpected route policy')
rows = data['pages']
status_counts = Counter(r['status'] for r in rows)
require(set(status_counts) <= {'publish', 'exclude_api', 'exclude_upstream', 'updating'}, 'Unknown publication status')
require(data['counts'] == {'source_files': len(rows), 'sitemap_urls': sum(r['in_sitemap'] for r in rows), **dict(status_counts)}, 'Publication counts differ from page records')
require(len(rows) == len(manifest), 'Source manifest count mismatch')
require(len({r['original_file'] for r in rows}) == len(rows), 'Duplicate original file')
require({r['original_repository_path'] for r in rows} == {r['path'] for r in manifest}, 'Source manifest paths differ')
sitemap = ET.parse(ROOT / 'source/sitemap.xml')
urls = {e.text for e in sitemap.iter() if e.tag.endswith('}loc')}
require(urls == set(index['routes']), 'Source sitemap and URL index differ')
require(urls == {r['original_url'] for r in rows if r['in_sitemap']}, 'Sitemap URL missing from translations')
require(digest(ROOT / 'source/sitemap.xml') == index['source']['sitemap_sha256'], 'Source sitemap hash changed')
expected = set()
notice_files = set()
prepared_files = set()
notice_routes = set()
routes = {}
for row in rows:
    path = row['original_repository_path']
    original = ROOT / row['original_file']
    require(row.get('original_title') == source_titles.get(path), 'Original title differs from source manifest: ' + path)
    require(row['original_file'] == 'source/' + path, 'Original path changed: ' + path)
    require(original.is_file(), 'Original file missing: ' + path)
    if original.is_file():
        require(digest(original) == row['original_sha256'], 'Original hash changed: ' + path)
    if row['in_sitemap']:
        require(index['routes'].get(row['original_url']) == path, 'Peer URL mapping changed: ' + path)
    translations = row['translations']
    if row['status'] == 'updating':
        require(translations is None, 'Updating page must not claim a completed translation: ' + path)
        notice = row.get('notice', {})
        require(set(notice) == {'en', 'zh-cn'}, 'Missing notice language: ' + path)
        require(row['in_sitemap'], 'Notice needs an original page URL: ' + path)
        for lang, t in notice.items():
            require(t['file'] == lang + '/UPDATING.md', 'Unexpected notice file: ' + path)
            file = ROOT / t['file']
            notice_files.add(t['file'])
            require(file.is_file(), 'Notice file missing: ' + t['file'])
            canonical = branded_path(urllib.parse.urlparse(row['original_url']).path)
            require(t['route'] == (canonical if lang == 'en' else '/zh-cn' + canonical), 'Unexpected notice route: ' + path)
            require(t['route'] not in routes, 'Duplicate notice route: ' + t['route'])
            routes[t['route']] = t['file']
            notice_routes.add(t['route'])
            if file.is_file():
                check_title(file, t)
                if args.update_hashes:
                    t['sha256'] = digest(file)
                else:
                    require(digest(file) == t['sha256'], 'Notice hash stale: ' + t['file'])
        prepared = row.get('prepared', {})
        require(set(prepared) == {'en', 'zh-cn'}, 'Missing preparation copy: ' + path)
        for lang, t in prepared.items():
            require(t['file'] == 'prepared/' + lang + '/' + branded_path(path), 'Unexpected prepared path: ' + path)
            require(t['route'] == notice.get(lang, {}).get('route'), 'Prepared route differs from notice: ' + path)
            prepared_files.add(t['file'])
            file = ROOT / t['file']
            require(file.is_file(), 'Prepared article missing: ' + t['file'])
            if file.is_file():
                check_title(file, t)
                if args.update_hashes:
                    t['sha256'] = digest(file)
                else:
                    require(digest(file) == t['sha256'], 'Prepared hash stale: ' + t['file'])
        continue
    if row['status'] != 'publish':
        require(translations is None and bool(row['reason']), 'Excluded source requires a reason and no translations: ' + path)
        require('notice' not in row, 'Excluded source must not promise an update: ' + path)
        require('prepared' not in row, 'Excluded source contains an undeclared preparation copy: ' + path)
        continue
    require('notice' not in row, 'Published article still contains a notice: ' + path)
    require('prepared' not in row, 'Published article contains a duplicate preparation copy: ' + path)
    require(set(translations) == {'en', 'zh-cn'}, 'Missing language: ' + path)
    for lang, t in translations.items():
        file = ROOT / t['file']
        expected.add(t['file'])
        require(t['file'] == lang + '/' + branded_path(path), 'Unexpected translation path: ' + path)
        require(file.is_file(), 'Translation missing: ' + t['file'])
        canonical = canonical_path(row)
        require(t['route'] == (canonical if lang == 'en' else '/zh-cn' + canonical), 'Unexpected route: ' + t['route'])
        require(t['route'] not in routes, 'Duplicate published route: ' + t['route'])
        routes[t['route']] = t['file']
        if file.is_file():
            check_title(file, t)
            if args.update_hashes:
                t['sha256'] = digest(file)
            else:
                require(digest(file) == t['sha256'], 'Translation hash stale: ' + t['file'])
artifact_files = set()
for artifact in data.get('artifacts', []):
    require(set(artifact['translations']) == {'en', 'zh-cn'}, 'Missing artifact language: ' + artifact['id'])
    for lang, t in artifact['translations'].items():
        file = ROOT / t['file']
        artifact_files.add(t['file'])
        require(file.is_file(), 'Missing download: ' + t['file'])
        require(t['route'] not in routes, 'Duplicate download route: ' + t['route'])
        routes[t['route']] = t['file']
        if file.is_file():
            check_title(file, t)
            if args.update_hashes:
                t['sha256'] = digest(file)
            else:
                require(t['sha256'] == digest(file), 'Download hash stale: ' + t['file'])
actual = {str(f.relative_to(ROOT)) for lang in ['en', 'zh-cn'] for f in (ROOT / lang).rglob('*') if f.is_file() and f.suffix in {'.md', '.json'} and f.name != 'SUMMARY.md'}
require(actual == expected | notice_files | artifact_files, 'Unexpected or missing content: ' + str(sorted(actual ^ (expected | notice_files | artifact_files))))
actual_prepared = {str(f.relative_to(ROOT)) for f in (ROOT / 'prepared').rglob('*.md')}
require(actual_prepared == prepared_files, 'Unexpected or missing prepared Markdown: ' + str(sorted(actual_prepared ^ prepared_files)))
redirects = read_json('redirects.json')
seen = set()
for r in redirects['redirects']:
    require(r['from'] not in seen, 'Duplicate redirect: ' + r['from'])
    require(r['to'] in routes, 'Redirect destination absent: ' + r['to'])
    require(r['from'] not in routes, 'Redirect shadows article: ' + r['from'])
    seen.add(r['from'])
redirect_targets = {r['from']: r['to'] for r in redirects['redirects']}
for row in rows:
    if row['status'] not in {'publish', 'updating'}:
        continue
    entries = row['translations'] if row['status'] == 'publish' else row['notice']
    original_path = '/' + row['original_repository_path'] if row['original_repository_path'].endswith('.json') else urllib.parse.urlparse(row['original_url']).path
    for lang, entry in entries.items():
        old_route = original_path if lang == 'en' else '/zh-cn' + original_path
        if old_route != entry['route']:
            require(redirect_targets.get(old_route) == entry['route'], 'Missing legacy brand redirect: ' + old_route)
        require(entry['route'] == branded_path(entry['route']), 'Old brand in published route: ' + entry['route'])

link_count = 0
all_files = sorted({f for f in expected if f.endswith('.md')} | notice_files | prepared_files | {'en/SUMMARY.md', 'zh-cn/SUMMARY.md', 'README.md', 'PUBLICATION-STATUS.md'})
for rel in all_files:
    file = ROOT / rel
    require(file.is_file(), 'Missing index: ' + rel)
    if not file.is_file():
        continue
    text = file.read_text()
    require(len(re.findall(r'^# ', text, re.M)) == 1, 'Expected one main heading: ' + rel)
    if rel not in {'README.md', 'PUBLICATION-STATUS.md'}:
        visible = re.sub(r'\]\([^)]*\)', ']', text)
        # Published package names and executable identifiers must stay executable.
        if rel.endswith(('overview/javascript-sdk.md', 'counso-cli/counso-cli.md', 'developers/client-side-mcp-server.md')):
            visible = visible.replace('@dust-tt/client', '@client/package').replace('@dust-tt/dust-cli', '@cli/package')
            visible = re.sub(r'\bdust(?=\s+(?:login|logout|status|chat|skill:init|cache:clear|help|--help|--version)\b)', 'cli', visible)
            visible = visible.replace('`dust`', '`cli`')
        require(not re.search(r'\bdust\b|\baduster\b|未部署|飞书|Feishu|整改安排|需要适配|待适配|hold_integration|upstream implementation', visible, re.I), 'Brand or scaffolding in copy: ' + rel)
        require(not re.search(r'\bTODO\b|\bTBD\b', strip_code(visible)), 'Unfinished copy: ' + rel)
        require(not re.search(r'https?://(?:[^/\s]+\.)?dust\.tt', text), 'Upstream product link in copy: ' + rel)
    for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^\s)]+)(?:\s+"[^"]*")?\)', strip_code(text)):
        parsed = urllib.parse.urlparse(target.strip('<>'))
        if parsed.scheme or parsed.netloc:
            continue
        link_count += 1
        require(not parsed.path.startswith('/'), 'Use relative Markdown links: ' + rel + ' → ' + target)
        linked = (file.parent / urllib.parse.unquote(parsed.path)).resolve() if parsed.path else file
        require(linked.is_relative_to(ROOT), 'Link leaves repository: ' + rel + ' → ' + target)
        require(linked.exists(), 'Broken file link: ' + rel + ' → ' + target)
        if linked.is_relative_to(ROOT) and (rel in {'en/SUMMARY.md', 'zh-cn/SUMMARY.md'} or rel in expected):
            require(str(linked.relative_to(ROOT)) not in notice_files | prepared_files, 'Unreleased capability linked from user documentation: ' + rel)
        if parsed.fragment and linked.is_file() and linked.suffix == '.md':
            require(urllib.parse.unquote(parsed.fragment) in anchors(linked.read_text()), 'Broken anchor: ' + rel + ' → ' + target)
status_text = (ROOT / 'PUBLICATION-STATUS.md').read_text()
listed_urls = re.findall(r'^\|[^\n]*\| \[(https?://[^\]]+)\]\(', status_text, re.M)
require(Counter(listed_urls) == Counter(r['original_url'] for r in rows if r['status'] != 'publish'), 'Unpublished URL inventory differs from mapping')
api_operations = 0
if data['publication'].get('api') == 'included':
    api_dir = 'docs/developer-platform/counso-api-documentation/'
    spec = read_json('en/' + api_dir + 'openapi.json')
    methods = {'get', 'post', 'put', 'patch', 'delete', 'head', 'options'}
    operations = {(path, method): op for path, item in spec['paths'].items() for method, op in item.items() if method in methods}
    api_operations = len(operations)
    api_rows = {(r['api']['path'], r['api']['method']): r for r in rows if 'api' in r}
    require(set(api_rows) == set(operations), 'API article and specification coverage differ')
    require(len(api_rows) == len([r for r in rows if 'api' in r]), 'Multiple articles claim one API operation')
    def resolve_reference(ref):
        require(ref.startswith('#/'), 'External schema reference: ' + ref)
        if not ref.startswith('#/'):
            return None
        value = spec
        try:
            for part in ref[2:].split('/'):
                value = value[part.replace('~1', '/').replace('~0', '~')]
            return value
        except (KeyError, TypeError):
            require(False, 'Unresolved schema reference: ' + ref)
            return None
    def inspect_schema(value):
        if isinstance(value, dict):
            if '$ref' in value:
                resolve_reference(value['$ref'])
            for child in value.values():
                inspect_schema(child)
        elif isinstance(value, list):
            for child in value:
                inspect_schema(child)
    inspect_schema(spec)
    require(spec['servers'] == [{'url': 'https://app.counso.ai', 'description': 'Counso'}], 'Unexpected API server')
    for (path, method), op in operations.items():
        parameters = spec['paths'][path].get('parameters', []) + op.get('parameters', [])
        path_parameters = {p['name'] for p in parameters if p.get('in') == 'path' and p.get('required')}
        require(set(re.findall(r'\{([^}]+)\}', path)) == path_parameters, 'Path parameter mismatch: ' + method + ' ' + path)
        for lang in ['en', 'zh-cn']:
            article = ROOT / api_rows[(path, method)]['translations'][lang]['file']
            require(method.upper() + ' ' + path in article.read_text(), 'Article endpoint mismatch: ' + str(article))
    for lang in ['en', 'zh-cn']:
        for name in ['openapi.json', 'swagger.json']:
            require(read_json(lang + '/' + api_dir + name) == spec, 'API schemas differ: ' + lang + '/' + name)
        collection = read_json(lang + '/' + api_dir + 'postman.collection.json')
        environment = read_json(lang + '/' + api_dir + 'postman.environment.json')
        for var in environment['values']:
            if var['key'] != 'baseUrl':
                require(var['value'] == '', 'Shared environment contains a value: ' + var['key'])
        requests = [entry['request'] for group in collection['item'] for entry in group['item']]
        request_pairs = []
        for request in requests:
            path = '/' + '/'.join(request['url']['path'])
            path = re.sub(r':([^/]+)', r'{\1}', path)
            pair = (path, request['method'].lower())
            request_pairs.append(pair)
            require(pair in operations, 'Postman request has no matching operation: ' + str(pair))
            if pair not in operations:
                continue
            mode = operations[pair]['x-counso-auth']
            if mode in {'login', 'webhook'}:
                require(request['auth']['type'] == 'noauth', 'Unexpected Bearer auth: ' + path)
            else:
                token = '{{apiKey}}' if mode == 'workspace' else '{{userAccessToken}}'
                require(request['auth'] == {'type': 'bearer', 'bearer': [{'key': 'token', 'value': token, 'type': 'string'}]}, 'Wrong Postman credential type: ' + path)
            require(request['url']['host'] == ['{{baseUrl}}'], 'Hard-coded Postman host: ' + path)
            if request.get('body', {}).get('mode') == 'raw':
                try:
                    json.loads(request['body']['raw'])
                except json.JSONDecodeError:
                    require(False, 'Invalid Postman JSON request body: ' + path)
        require(Counter(request_pairs) == Counter(operations.keys()), 'Postman operation coverage differs: ' + lang)
        raw = json.dumps(collection) + json.dumps(environment) + json.dumps(spec)
        require(not re.search(r'https?://(?:[^/\s"\\]+\.)?dust\.tt|34241185-c7e0fdbe-b2c5-47d5-a923-8244d45cd95e', raw, re.I), 'Upstream API host or Postman collection remains')
summary = {'source_files': len(rows), 'sitemap_urls': len(urls), 'published_pairs': len(expected) // 2, 'article_pairs': len([f for f in expected if f.endswith('.md')]) // 2, 'language_files': len(expected), 'supplementary_downloads': len(artifact_files), 'published_routes': len(routes) - len(notice_routes), 'updating_pages': len(notice_routes) // 2, 'prepared_pairs': len(prepared_files) // 2, 'notice_routes': len(notice_routes), 'redirects': len(seen), 'relative_links_checked': link_count, 'errors': errors}
summary['api_operations'] = api_operations
if args.update_hashes and not errors:
    temporary = ROOT / '.translations.json.tmp'
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(ROOT / 'translations.json')
print(json.dumps(summary, ensure_ascii=False, indent=2))
sys.exit(bool(errors))
