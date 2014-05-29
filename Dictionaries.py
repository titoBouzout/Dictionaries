import sublime, sublime_plugin

import fnmatch, os.path

def find_resources(pattern):
	resources = []
	if hasattr(sublime, 'find_resources'):
		resources = sublime.find_resources(pattern)
	else:
		for root, dir_names, file_names in os.walk(sublime.packages_path()):
			if ".git" in root:
				continue
			for file_name in file_names:
				rel_path = os.path.relpath(os.path.join(root, file_name), sublime.packages_path())
				if fnmatch.fnmatch(rel_path.lower(), "*" + pattern.lower()):
					resources += [os.path.join('Packages', rel_path).replace(os.sep, "/")]
	return resources


class DicSetViewLanguageCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		items = find_resources("*.dic")

		def on_done(i):
			if i >= 0:
				settings = self.view.settings()
				settings.set("dictionary", items[i])

		self.view.window().show_quick_panel(items, on_done)


class DicSetLanguageCommand(sublime_plugin.WindowCommand):

	def run(self):
		items = find_resources("*.dic")

		def on_done(i):
			if i >= 0:
				settings = sublime.load_settings("Preferences.sublime-settings")
				settings.set("dictionary", items[i])
				sublime.save_settings("Preferences.sublime-settings")

		self.window.show_quick_panel(items, on_done)

class FixBug268And295Command(sublime_plugin.EventListener):

	def on_post_text_command(self, view, command_name, args):
		if command_name == "ignore_word" and not 'ignore' in args:
			if args['word'] == '':
				view = sublime.active_window().active_view()
				args['word'] = view.substr(view.word(view.sel()[0].a))
				view.run_command("ignore_word", {"word": args['word'], 'ignore':True})
			s = sublime.load_settings("Preferences.sublime-settings")
			ignored_words = s.get("ignored_words", [])
			ignored_words.append(args['word'])
			s.set("ignored_words", list(set(ignored_words)))
			view.settings().set("ignored_words", list(set(ignored_words)))
			sublime.save_settings("Preferences.sublime-settings")