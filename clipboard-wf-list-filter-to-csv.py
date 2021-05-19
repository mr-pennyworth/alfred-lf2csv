#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import json
import os
import subprocess

alfreditems = {'items': []}

wf_objects = json.loads(
  subprocess.check_output(['./clipboard-wf-list-filter-json'])
)

list_filter_object = None
for obj in wf_objects.get('objects', []):
  if obj['type'] == 'alfred.workflow.input.listfilter':
    list_filter_object = obj

if list_filter_object is None:
  alfreditems['items'].append({
    'title': 'Error: No list filter selected',
    'valid': False,
    'icon': {
      'path': 'error.png',
    },
  })
else:
  csv_filename = 'list-items'
  if list_filter_object['config']['keyword'] != '':
    csv_filename = list_filter_object['config']['keyword']
  csv_filepath = f'/tmp/{csv_filename}.csv'
  items = json.loads(list_filter_object['config']['items'])
  with open(csv_filepath, 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    for item in items:
      csv_writer.writerow([
        item.get('title', ''),
        item.get('subtitle', ''),
        item.get('arg', ''),
      ])
  alfreditems['items'].append({
    'title': os.path.basename(csv_filepath),
    'arg': csv_filepath,
    'subtitle': f'contains {len(items)} list items',
    'type': 'file',
  })
  
print(json.dumps(alfreditems, indent=2))
