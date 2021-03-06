#!/usr/bin/env python3
import click
import openapi_server.db_connection as db
import logging
import os


@click.group()
def cli():
    """Initialize a DB with the 2014 i2b2 NLP de-id data."""


@cli.command()
def populate_db():
    """Populate the DB with 2014 i2b2 NLP de-id data."""
    values = db.load_config()
    conn = db.get_connection_local_pg(values)
    # logging.info("Finished import ")
    if (not os.path.isdir("/tmp/data/2014-i2b2-nlp-evaluation-data-txt")):
        logging.exception("Data not downloaded, run the command : "
                          "load_database.py get_data first  ")
        os.sys.exit(1)
    db.import_data(conn, "/tmp/data/2014-i2b2-nlp-evaluation-data-txt",
                   "/tmp/data/testing-PHI-Gold-fixed")


if __name__ == "__main__":
    cli()
