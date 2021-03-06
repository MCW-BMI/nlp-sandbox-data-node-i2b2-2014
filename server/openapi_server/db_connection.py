import logging
import os
import os.path
import xml.etree.ElementTree as ET

import psycopg2
import psycopg2.extras

from openapi_server.util.configuration import Config


def load_config():
    """
    Load the configuration file needed by the database from the config class
    :return: None
    """
    db = {}
    db['user'] = Config().sql_user
    db['password'] = Config().sql_password
    db['host'] = Config().sql_host
    db['database'] = Config().sql_db
    db['port'] = Config().sql_port

    return db


def get_connection_local_pg(params):
    """
    Return a Postgres db Connection

    :param db:
    :param config:
    :return:
    """
    # conn_string_no_passwd =  params

    # logging.info(conn_string_no_passwd)
    conn = psycopg2.connect(**params)

    cur = conn.cursor()
    logging.info('PostgreSQL database version:')
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    logging.info(db_version)
    # print(cursor)
    # conn.cursor will return a cursor object, you can use this cursor to
    # perform queries

    return conn


def load_annotations(conn, noteid, name, gold_path):
    """
    Load Annotations into the database frm text files.
    """
    cur = conn.cursor()
    file_path = gold_path + "/" + name.replace("txt", "xml")
    insert_sql = "INSERT INTO pat_annotations (noteid, category, type, " \
                 "pos_id, start, stop, text) VALUES ( %s,%s, %s, %s, %s, " \
                 "%s, %s) RETURNING id"

    if os.path.isfile(file_path):
        # f = open(file_path)
        logging.info(f"Annotation file found for {file_path}")
        tree = ET.parse(file_path)
        root = tree.getroot()
        for tags in root.findall('TAGS'):
            logging.info(f"TAGS {tags}")
            for tag in tags.iter():
                if len(tag.keys()) > 0:
                    logging.info(f"TAG  {tag.tag}  : {tag.attrib}")
                    keys = tag.attrib.keys()
                    logging.info(f" KEYS for tag : {keys}")
                    # os.sys.exit(1)
                    cur.execute(insert_sql, (
                        noteid, tag.attrib["TYPE"], tag.tag, tag.attrib['id'],
                        tag.attrib['start'], tag.attrib['end'],
                        tag.attrib['text']))
                    conn.commit()
    else:
        logging.error(f"Annotation file not found for {file_path}")
        os.sys.exit(1)


def import_data(conn, path, gold_path):
    """
    Create pat_notes and pat_annotation tables in the database if they don't
    exist and truncates them if they have data.
    """
    cur = conn.cursor()
    # create_sql_pat_notes = 'CREATE TABLE IF NOT EXISTS "i2b2_data"."public' \
    #                        '".pat_notes ( id SERIAL NOT NULL, filename ' \
    #                        'VARCHAR, text VARCHAR, PRIMARY KEY (id) )'
    # create_anno = 'CREATE TABLE IF NOT EXISTS "i2b2_data"."public".' \
    #               'pat_annotations ( id SERIAL NOT NULL, noteid INTEGER, ' \
    #               'category CHARACTER VARYING,  type CHARACTER VARYING, ' \
    #               'pos_id CHARACTER VARYING, START  NUMERIC,  STOP  ' \
    #               'NUMERIC, TEXT CHARACTER VARYING, CONSTRAINT ' \
    #               'patannotations_fk1 FOREIGN KEY (noteid) REFERENCES ' \
    #               '"i2b2_data"."public"."pat_notes" ("id") )'
    # res = cur.execute(create_sql_pat_notes)
    # res = cur.execute(create_anno)
    conn.commit()

    # # Truncate table
    # truncate_sql = 'TRUNCATE TABLE "i2b2_data"."public".pat_notes CASCADE'
    # truncate_sql_ann = 'TRUNCATE TABLE "i2b2_data"."public".' \
    #                    'pat_annotations CASCADE'
    # res = cur.execute(truncate_sql_ann)
    # res = cur.execute(truncate_sql)
    # Read files and import
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                logging.info(f"Importing file {entry.name}")
                with open(entry, 'r') as f:
                    data = f.read()
                    insert_sql = 'insert into "i2b2_data"."public".' \
                                 'pat_notes(filename, text) values (%s, %s) ' \
                                 'RETURNING id'
                    cur.execute(insert_sql, (entry.name, data,))
                    row_id = cur.fetchone()[0]
                    logging.info(f"Inserted row {row_id} ")
                    load_annotations(conn, row_id, entry.name, gold_path)
                    conn.commit()

    cur.close()
    conn.commit()
    return None
