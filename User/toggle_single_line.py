import sublime, sublime_plugin, re
class ToggleSingleLineCommand(sublime_plugin.TextCommand):
   def run(self,edit):
    for region in reversed(self.view.sel()):
      text = self.view.substr(region)

      # check if the css statement needs to be expanded or collapsed
      if re.match('^.*\{.*}\s*$', text):
        # expand the css statement
        m = re.search('^(?P<key>.*)\{(?P<params>.*)\;\s*}$', text)
        multiline = '%s{\n\t%s;\n}' % (m.group('key'), m.group('params').strip().replace('; ', ';\n\t'))
        self.view.replace(edit, region, multiline)
      else:
        # collapse the css statement
        singleline = ' '.join([x.strip() for x in text.split('\n')])
        self.view.replace(edit, region, singleline)