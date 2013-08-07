import sublime
import sublime_plugin
import string

class MultiSelectNumbersCommand( sublime_plugin.TextCommand ):
  def run(self, edit):
    view = self.view;
    window = view.window()

    def countThoseSelections(pattern):
      view.run_command( 'multi_select_helper', { 'pattern' : pattern } )
    window.show_input_panel('Count Start:Step', '1:1', countThoseSelections, False, False)


class MultiSelectHelperCommand( sublime_plugin.TextCommand ):
  def run( self, edit, pattern ):
    view = self.view;
    pattern = pattern.split( ':' )
    region_index = int( pattern[0] )

    for region in view.sel():
      replaceRegion = sublime.Region( region.begin() - 1, region.begin() )
      prevChar = view.substr( replaceRegion )
      if( prevChar == '#' ):
        view.replace( edit, replaceRegion, str( region_index ) )
        region_index = region_index + int( pattern[1] )