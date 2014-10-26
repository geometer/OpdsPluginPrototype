#!/usr/bin/python

import os, shutil, sys
from argparse import ArgumentParser

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    elif not os.path.isdir(path):
        raise Exception('Cannot create directory %s' % path)

def copy_binary(prototype, dest_dir):
    create_dir(dest_dir)
    shutil.copy('prototype/%s' % prototype, dest_dir)

def copy_and_replace_patterns(prototype, dest_dir, params):
    create_dir(dest_dir)

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    elif not os.path.isdir(dest_dir):
        raise Exception('Cannot create directory %s' % dest_dir)

    with open('%s/%s' % (dest_dir, prototype), 'wt') as target:
        with open('prototype/%s' % prototype, 'rt') as source:
            for line in source:
                target.write(line % params)

def parse_command_line():
    parser = ArgumentParser(
        description='FBReader OPDS plugin code generator'
    )
    parser.add_argument(
        '-d',
        dest='DIR',
        required=True,
        help='directory where to create the project'
    )
    parser.add_argument(
        '-p',
        dest='PACKAGE',
        required=True,
        help='java package prefix, e.g.: com.mycatalog'
    )
    parser.add_argument(
        '-n',
        dest='NAME',
        required=True,
        help='name for android launcher, e.g.: My Catalog'
    )
    parser.add_argument(
        '-u',
        dest='URL',
        required=True,
        help='OPDS catalog URL, e.g.: http://mycatalog.com/opds.xml'
    )
    parser.add_argument(
        '-i',
        dest='ICON',
        help='PNG icon file for android launcher'
    )
    return parser.parse_args(sys.argv[1:]).__dict__

if __name__ == '__main__':
    params = parse_command_line()
    project_dir = params['DIR']
    create_dir(project_dir)

    full_package_name = '%s.fbreader.plugin.opds' % params['PACKAGE']
    src_dir = '%s/src/%s' % (project_dir, full_package_name.replace('.', '/'))
    
    copy_and_replace_patterns('AndroidManifest.xml', project_dir, params)
    copy_and_replace_patterns('project.properties', project_dir, params)
    copy_and_replace_patterns('CatalogActivity.java', src_dir, params)
    copy_and_replace_patterns('CatalogInfo.java', src_dir, params)
    copy_and_replace_patterns('strings.xml', '%s/res/values' % project_dir, params)
    copy_binary('fbreader-opds.jar', '%s/libs' % project_dir)

    drawable_dir = '%s/res/drawable' % project_dir
    icon_name = 'opds_catalog.png'
    if params['ICON']:
        create_dir(drawable_dir)
        shutil.copy(params['ICON'], '%s/%s' % (drawable_dir, icon_name))
    else:
        copy_binary(icon_name, drawable_dir)

    print 'Created sources tree for %s in %s' % (full_package_name, project_dir)
    print 'Please run \'android update project -p %s -n OpdsFBReaderPlugin\' to create build.xml' % project_dir
