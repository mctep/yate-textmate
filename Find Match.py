import re
import sublime, sublime_plugin

class FindMatchCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		regions = self.view.sel()

		if len(regions) == 1:
			region = regions[0]
			line = self.view.line(region)

			string = self.view.substr(line).strip()

			m = re.search('^apply ((\.|\/)[^ ]*) ?([0-9a-zA-Z_-]+)?', string)

			if not(m is None):
				jpath = m.group(1)
				if jpath == '.':
					jpath = ''
				else:
					jpath = jpath + ' '
				mode = m.group(3)
				self.view.window().run_command('show_overlay', {'overlay': 'goto', 'text': '@%s%s' % (jpath, mode)})
				return

			f = re.search('^apply (\w+)', string)
			if (not f is None):
				func = f.group(1)
				self.view.window().run_command('show_overlay', {'overlay': 'goto', 'text': '@%s' % func})
				return
