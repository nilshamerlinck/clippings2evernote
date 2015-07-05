#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs, locale, os, sys
import traceback
if sys.stdout.encoding != 'UTF-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

# cf https://github.com/evernote/evernote-sdk-python
    
from evernote.api.client import EvernoteClient
from evernote.api.client import NoteStore
import evernote.edam.type.ttypes as Types

from parser import MyClippingsParser

def create_note(note_store, notebook_guid, title, content):
    note = Types.Note()
    note.notebookGuid = notebook_guid
    note.title = title.encode('utf-8')
    note.content = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">
<en-note>
<caption>%s</caption>
</en-note>''' % content.encode('utf-8')

    createdNote = note_store.createNote(note)

    return True

def clippings2evernote(filename, token, notebook_guid, debug=False, verbose=False):
    parser = MyClippingsParser(filename)

    client = EvernoteClient(token=token, sandbox=False)
    note_store = client.get_note_store()

    notes = {}

    for c in parser.parse():
        if c and c['type'] == 'surlignement':
            k = c['title'] + ' | ' + c['author']
            if k not in notes:
                notes[k] = []

            notes[k].append(c['content'])

    # FIXME:
    # en regroupant par clé, on perd l'ordre chronologique

    for k in sorted(notes.keys()):
        title = '#kindle ' + k
        content = '\n--\n'.join(notes[k])
        content = content.replace('\n', '<br/>').replace('&', '&amp;')

        if verbose:
            print title, content

        if debug:
            continue

        try:
            create_note(note_store, notebook_guid, title, content)
        except Exception, e:
            print 'Error:', title, content
            print e

    return 0

def main():
    import sys
    from optparse import OptionParser

    usage="""
Usage: $ ./clippings2evernote.py /media/Kindle/documents/My\ Clippings.txt EVERNOTE_TOKEN NOTEBOOK_GUID
  """[1:-3]
    
    parser = OptionParser(usage=usage)
    parser.add_option('--debug',
                      help='ne rien faire vraiment',
                      default=False,
                      action='store_true',
                      dest='debug')
    parser.add_option('--verbose',
                      help='verbose',
                      default=False,
                      action='store_true',
                      dest='verbose')
    parser.add_option('--log',
                      help='log errors to file',
                      default=False,
                      action='store_true',
                      dest='log')
                                                                    
    options, args = parser.parse_args()
    
    if len(args) != 3:
        print usage
        return -1

    if options.log:
        sys.stderr = codecs.open(os.path.join(options.output_dir, 'err.log'), 'w', 'utf-8')
        
    return clippings2evernote(filename=args[0],
                              token=args[1],
                              notebook_guid=args[2],
                              debug=options.debug,
                              verbose=options.verbose)
        
if __name__ == '__main__':
    sys.exit(main())
