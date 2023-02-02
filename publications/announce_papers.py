#!/usr/bin/env python3

"""This script parses a .bib file, reads in a log file, then announces
papers that are in the first but not the second and updates the log.

The log should be committed to the repository along with the .bib file
(the CI workflow will have to take care of that).

The Twitter part of the code is heavily based on
https://github.com/rseng/jobs-updater/blob/main/find-updates.py

See find-updates.py for more hints.

FIXME: consider adding Mastodon support as in find-updates.py
"""

import copy
import sys
import json
import os

import pybtex.database
import pybtex.backends.plaintext
from pybtex.database import Person
from pybtex.style.template import (field, join, names, sentence)
from pybtex.style.formatting.unsrt import Style as UnsrtStyle

import tweepy

def get_twitter_client():
    envars = {}
    for envar in [
        "TWITTER_API_KEY",
        "TWITTER_API_SECRET",
        "TWITTER_CONSUMER_KEY",
        "TWITTER_CONSUMER_SECRET",
    ]:
        value = os.environ.get(envar)
        if not value:
            raise RuntimeError(f"env variable {envar} is required to deploy to Twitter" % envar)
        envars[envar] = value

    return tweepy.Client(
        consumer_key=envars["TWITTER_CONSUMER_KEY"],
        consumer_secret=envars["TWITTER_CONSUMER_SECRET"],
        access_token=envars["TWITTER_API_KEY"],
        access_token_secret=envars["TWITTER_API_SECRET"],
    )

class ShortStyle(UnsrtStyle):
    """A 'short' style. See individual doc. strings for differences
    compared to 'unsrt'.
    """
    def format_names(self, role, as_sentence=True):
        "Format names. This custom method does *not* use the Oxford comma."
        formatted_names = names(role, sep=', ', sep2 = ' and ', last_sep=' and ')
        if as_sentence:
            return sentence [formatted_names]
        else:
            return formatted_names

    def format_web_refs(self, e):
        "Format Web references, preferring DOI and using only one of [DOI, URL]."
        if 'doi' in e.fields:
            return self.format_doi(e)

        if 'url' in e.fields:
            return self.format_url(e)

    def format_doi(self, e):
        """Format DOI in a way similar to URLs."""
        return join [ 'URL: https://doi.org/', field('doi', raw=True) ]

text_backend = pybtex.backends.plaintext.Backend()

short_style = ShortStyle()

def entry_text(entry, style=short_style, backend=text_backend):
    "Format a bibliographic entry"
    return style.format_entry("", entry).text.render(backend)

def too_long(prefix, text, limit=280):
    "Return True if the prefix + text is too long."
    return len(prefix + text) > limit

def format_entry(entry, message_prefix):
    """Format a bibliographic entry, ensuring that resulting tweet text is
    short enough."""

    # make a copy to avoid modifying the input argument
    e = copy.deepcopy(entry)

    text = entry_text(e)

    # Try switching to the 'misc' type to ignore the publisher,
    # volume, pages, etc
    if too_long(message_prefix, text):
        e.type = "misc"
        text = entry_text(e)

    if 'author' in e.persons:
        # Some publications don't have an author (but may have editors)
        authors = e.persons['author']
        n_authors_dropped = 0
        while too_long(message_prefix, text):
            text = entry_text(e)

            if len(authors) == 1:
                break

            # drop one more author
            authors = authors[:-1]
            n_authors_dropped += 1
            N = f"{n_authors_dropped} " if n_authors_dropped > 1 else ""
            e.persons['author'] = authors + [Person(N + "others")]

    # remove 'note' if we have to
    if too_long(message_prefix, text) and 'note' in e.fields:
        del e.fields['note']
        text = entry_text(e)

    return text

def send_tweet(text):
    """Send a tweet"""
    assert len(tweet) <= 280

    # FIXME: this should actually send the tweet
    print(len(tweet), tweet)

if __name__ == "__main__":
    # input file name: the .bib file containing PISM publications (read only)
    input_filename = sys.argv[1]
    # log file name: this file contains a JSON-formatted list of
    # papers that were announced already. We read it in, tweet about
    # papers in input_filename but not in log_filename, then update
    # log_filename, i.e. this one is read-write.
    log_filename = sys.argv[2]

    # parse the .bib file
    data = pybtex.database.parse_file(input_filename)

    # Read the log
    try:
        with open(log_filename, "r") as f:
            already_announced = json.load(f)
    except:
        already_announced = []

    message_prefix = "New publication: "

    for key, entry in data.entries.items():
        if not (key in already_announced):
            tweet = message_prefix + format_entry(entry, message_prefix)
            send_tweet(tweet)

            already_announced += [key]

    already_announced.sort()

    # Write the updated log using separators that make diffs easier to
    # read.
    with open(log_filename, "w") as f:
        json.dump(already_announced, f, separators=(",\n", ": "))
