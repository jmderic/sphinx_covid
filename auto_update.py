#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# Copyright J. Mark Deric, 2020.  All rights reserved

import sys, json
from pathlib import Path
from shutil import rmtree, copy
from fileinput import FileInput

def make_new_dir(d):
    if d.is_dir():
        rmtree(d)
    d.mkdir(mode=0o755)

def fmt_num(val, width, pop=None, int_only=False):
    if pop:
        val = val / pop * 1e5
    f = '{{:^{},.{}f}}'
    fmt1 = f.format('', 0)
    str_len = len(fmt1.format(val))
    if str_len < 3 and not int_only:
        fmt = f.format(width, 3 - str_len)
    else:
        fmt = f.format(width, 0)
        
    return fmt.format(val)

def fmt_str(val, width):
    fmt = '{{:^{}s}}'.format(width)
    return fmt.format(val)

def create_html_context_file(top, state):
    html_path_prefix_file = top / 'html_path_prefix.txt'
    html_path_prefix = html_path_prefix_file.read_text().rstrip()
    html_context = {
        'html_path_prefix' : html_path_prefix,
        'asof_date' : state["asof_date"],
    }
    html_json = top / 'html_context_autoX.json'
    with open(html_json, 'w') as f:
        json.dump(html_context, f, sort_keys=True, indent=4)

def create_jinja_contexts_file(top, data_dir, state):
    # setup location toctree, associated .rst files, and plot images
    locs_auto = top / 'website/locs_autoX'
    make_new_dir(locs_auto)
    locs_template = top / 'website/locs/template.rst'
    jinja_json = top / 'jinja_contexts_autoX.json'
    jinja_contexts = { 'file_base' : { 'locations' : [] } }
    fb_locs = jinja_contexts['file_base']['locations']
    ts = state["timestamp"]
    locs = state["locations"]
    for loc in locs:
        LT = locs[loc]
        LD = LT['data']
        fb_locs.append(loc)
        locs_product = locs_auto / f'{loc}.rst'
        copy(locs_template, locs_product)
        with FileInput(locs_product, inplace=True) as f:
            for line in f:
                print(line.replace('<loc>', loc), end='')
        day_heading = f'Latest Daily data: {state["asof_date"]}'
        jinja_contexts[loc] = {
            'web_name' : LT['web_name'],
            'web_detail' : LT['web_detail'],
            'Pop' : LT['Pop'],
            'images' : {
                'Cases' : f'{ts}_{loc}_Cases.svg',
                'Deaths' : f'{ts}_{loc}_Deaths.svg',
                'Active' : f'{ts}_{loc}_Active.svg',
            },
            'day_hdr' : fmt_str(day_heading, 33),
            'case' : {
                'tot' : fmt_num(LD['case_tot'], 9, None, True),
                'tot_p100' : fmt_num(LD['case_tot'], 9, LT['Pop_num']),
                'day' : fmt_num(LD['case_now'], 9, None, True),
                'day_p100' : fmt_num(LD['case_now'], 9, LT['Pop_num']),
                'abk' : fmt_num(LD['case_abk_now'], 11),
                'abk_p100' : fmt_num(LD['case_abk_now'], 11, LT['Pop_num']),
                'ema' : fmt_num(LD['case_ema_now'], 11),
                'ema_p100' : fmt_num(LD['case_ema_now'], 11, LT['Pop_num']),
            },
            'case_pk' : {
                'day' : fmt_num(LD['case_peak']['val'], 10, None, True),
                'day_p100' : fmt_num(LD['case_peak']['val'], 10, LT['Pop_num']),
                'day_date' : fmt_str(LD['case_peak']['date'], 10),
                'abk' : fmt_num(LD['case_abk_peak']['val'], 11),
                'abk_p100' : fmt_num(LD['case_abk_peak']['val'], 11, LT['Pop_num']),
                'abk_date' : fmt_str(LD['case_abk_peak']['date'], 11),
                'ema' : fmt_num(LD['case_ema_peak']['val'], 11),
                'ema_p100' : fmt_num(LD['case_ema_peak']['val'], 11, LT['Pop_num']),
                'ema_date' : fmt_str(LD['case_ema_peak']['date'], 11),
            },
            'death' : {
                'tot' : fmt_num(LD['death_tot'], 9, None, True),
                'tot_p100' : fmt_num(LD['death_tot'], 9, LT['Pop_num']),
                'day' : fmt_num(LD['death_now'], 9, None, True),
                'day_p100' : fmt_num(LD['death_now'], 9, LT['Pop_num']),
                'abk' : fmt_num(LD['death_abk_now'], 11),
                'abk_p100' : fmt_num(LD['death_abk_now'], 11, LT['Pop_num']),
                'ema' : fmt_num(LD['death_ema_now'], 11),
                'ema_p100' : fmt_num(LD['death_ema_now'], 11, LT['Pop_num']),
            },
            'death_pk' : {
                'day' : fmt_num(LD['death_peak']['val'], 10, None, True),
                'day_p100' : fmt_num(LD['death_peak']['val'], 10, LT['Pop_num']),
                'day_date' : fmt_str(LD['death_peak']['date'], 10),
                'abk' : fmt_num(LD['death_abk_peak']['val'], 11),
                'abk_p100' : fmt_num(LD['death_abk_peak']['val'], 11, LT['Pop_num']),
                'abk_date' : fmt_str(LD['death_abk_peak']['date'], 11),
                'ema' : fmt_num(LD['death_ema_peak']['val'], 11),
                'ema_p100' : fmt_num(LD['death_ema_peak']['val'], 11, LT['Pop_num']),
                'ema_date' : fmt_str(LD['death_ema_peak']['date'], 11),
            },
            'active' : {
                'day' : fmt_num(LD['active_now'], 10, None, True),
                'day_p100' : fmt_num(LD['active_now'], 10, LT['Pop_num']),
                'day_date' : fmt_str(state['asof_long'], 10),
            },
            'active_pk' : {
                'day' : fmt_num(LD['active_peak']['val'], 10, None, True),
                'day_p100' : fmt_num(LD['active_peak']['val'], 10, LT['Pop_num']),
                'day_date' : fmt_str(LD['active_peak']['date'], 10),
            },
        }
    images_auto = top / 'website/images_autoX'
    make_new_dir(images_auto)
    image_files = list(data_dir.glob(f'{ts}_*.svg'))
    for image_file in image_files:
        copy(data_dir / image_file, images_auto)
    jinja_contexts['DataSource'] = {
        'asof_date' : state['asof_date'],
        'timestamp' : state['timestamp'],
        'commit_id' : state['commit_id'],
    }
    with open(jinja_json, 'w') as f:
        json.dump(jinja_contexts, f, sort_keys=True, indent=4)
    
def main():
    """
    Setup the jinja json file and html context file
    """
    # open the data source file and get state
    data_dir = Path(sys.argv[1])
    top = Path('.').resolve()
    print(f'data {data_dir}; top: {top}')
    with open(data_dir / 'state.json') as f:
        state = json.load(f)
    ts = state["timestamp"]
    with open(data_dir / f'{ts}_state.json') as f:
        state = json.load(f)
    create_html_context_file(top, state)
    create_jinja_contexts_file(top, data_dir, state)

if __name__ == '__main__':
    main()
