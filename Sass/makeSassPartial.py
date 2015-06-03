import sublime
import sublime_plugin
import os
import functools

class MakeSassPartialCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    filename = self.view.file_name()
    branch, leaf = os.path.split(filename)

    if not os.access(filename, os.W_OK):
        sublime.error_message(leaf + " is read-only")


    renamedFile = leaf;
    if not ( 'scss' in os.path.splitext( leaf )[1] ):
        renamedFile = renamedFile + '.scss'

    if not leaf[0] is '_':
        renamedFile = '_' + renamedFile

    if renamedFile is leaf:
        return


    renamedFile = os.path.join(branch, renamedFile)
    try:
        if len(leaf) is 0:
            sublime.error_message("No filename given")
            return;

        if os.path.exists(renamedFile):
            print(renamedFile)
            sublime.error_message(renamedFile + " already exists")
            return;

        os.rename(filename, renamedFile)

        v = self.view.window().find_open_file(filename)
        if v:
            v.retarget(renamedFile)
            self.view.set_syntax_file( 'Packages/Sass/SCSS.tmLanguage' )
    except Exception as e :
        sublime.status_message("Unable to rename: " + str(e))
