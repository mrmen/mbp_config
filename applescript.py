#!/usr/bin/env python3

import subprocess

def asrun(  "Run the given AppleScript and return the standard output and error."

  osa = subprocess.Popen(['osascript', '-'],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE)
  return osa.communicate(ascript)[0]

def asquote(astr):
  "Return the AppleScript equivalent of the given string."
  
  astr = astr.replace('"', '" & quote & "')
  return '"{}"'.format(astr)

