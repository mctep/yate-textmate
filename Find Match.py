import re
import sublime, sublime_plugin

class FindMatchCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		regions = self.view.sel()

		if len(regions) == 1:
			region = regions[0]
			line = self.view.line(region)

			string = self.view.substr(line).strip()

			m = re.search('apply (\.|\/)?([^.\[\(\)]+\.)*([^ .\[\(\)]+) ?([0-9a-zA-Z_-]+)?', string)
			print m
			if not(m is None):
				jpath = m.group(3)
				mode = m.group(4)

				if not(jpath is None) and not (mode is None):
					search = '%s %s' % (jpath, mode)
				else: 
					if not (mode is None):
						search = '%s' % (mode)
					else:
						if not (jpath is None):
							search = '%s' % (jpath)
						else:
							return

				self.view.window().run_command('show_overlay', {'overlay': 'goto', 'text': '@%s' % search})
				return
