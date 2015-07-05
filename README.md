# Kindle Clippings to Evernote

This script will parse the `My Clippings.txt` file from your Kindle and regroup highlights one note per document in the given Evernote notebook.

## Prerequisites

The script uses the [official Evernote SDK](https://github.com/evernote/evernote-sdk-python) :

	$ pip install evernote

You need to get a developer token from https://www.evernote.com/api/DeveloperToken.action

You also need to get the GUID of the target notebook. The easiest way to do so is to extract it from its URL in the Evernote webapp : `https://www.evernote.com/Home.action#b=f9cb26c5-1a01-4y53-a05a-3231e1efe9f0&st=p` for example.

## Usage

	$ ./clippings2evernote.py /media/Kindle/documents/My\ Clippings.txt EVERNOTE_TOKEN NOTEBOOK_GUID

