import sublime, sublime_plugin

'''**
   * Completions for HTSL
   *   Control nodes
   *   Tag nodes
   *'''
class HtslTagCompletions(sublime_plugin.EventListener):
#{
	def __init__(self):
	#{
		self.tag_nodes= self.get_tag_nodes();
		self.ctrl_nodes= self.get_ctrl_nodes();
	#}

	def on_query_completions(self, view, prefix, locations):
	#{
		# Only trigger within HTSL
		if not( view.match_selector(locations[0], "source.htsl") ):
			return [];
		elif( view.match_selector(locations[0], "source.htsl meta.tag coding") ):
			return (self.tag_nodes,sublime.INHIBIT_WORD_COMPLETIONS);
		elif( view.match_selector(locations[0], "source.htsl meta.control-node.switch meta.control-node coding") ):
			return (self.ctrl_nodes['in_switch']+self.ctrl_nodes['common'],sublime.INHIBIT_WORD_COMPLETIONS);
		elif( view.match_selector(locations[0], "source.htsl meta.control-node coding") ):
			return (self.ctrl_nodes['common'],sublime.INHIBIT_WORD_COMPLETIONS);
		else:
			return [];
		#if
	#}

	def get_ctrl_nodes(self):
	#{
		return ({
			'common': [
				('~if\tJudger', '~if( $1 )\n\t'),
				('~for-each\tLoop', '~for-each( ${1:\$array} as ${2:\$${3:key}=>}\$${4:value} )\n\t'),
				('~else\tFollower', '~else\n\t'),
				('~if-not\tJudger', '~if-not( $1 )\n\t'),
				('~else-if\tFollowingJudger', '~else-if( $1 )\n\t'),
				('~else-if-not\tFollowingJudger', '~else-if-not( $1 )\n\t'),
				('~while\tLoop', '~while( $1 )\n\t'),
				('~do-while\tLoop', '~do-while( $1 )\n\t'),
				('~for\tLoop', '~for( $1; $2; $3; )\n\t'),
				('~then\tFollower', '~then\n\t'),
				('~switch\tSwither', '~switch( $1 )\n\t'),
				('~if-all\tJudger', '~if-all( $1; )\n\t'),
				('~if-all-not\tJudger', '~if-all-not( $1; )\n\t'),
				('~if-not-all-not\tJudger', '~if-not-all-not( $1; )\n\t'),
				('~if-not-all\tJudger', '~if-not-all( $1; )\n\t'),
				('~continue\tDirectly', '~continue'),
				('~continue\tWith condition', '~continue( $1 )'),
				('~break\tDirectly', '~break'),
				('~break\tWith condition', '~break( $1 )'),
			],
			'in_switch': [
				('~default\tSwither', '~default\n\t'),
				('~case\tSwither', '~case( $1 )\n\t'),
			],
		});
	#}

	def get_tag_nodes(self):
	#{
		return ([
			('-div\tTag', '-div'),
			('-span\tTag', '-span'),
			('-a\tLink Tag', '-a @${0:link}'),
			('-a\tAnchor Tag', '-a <${1:name}>'),
			('-img\tImage Tag', '-img @${0:link}'),
			('-article\tTag', '-article'),
			('-aside\tTag', '-aside'),
			('-area\tTag', '-area(${1:shape}|${2:coords}) @${0:link}'),
			('-abbr\tTag', '-abbr'),
			('-audio\tTag', '-audio @${0:link}'),
			('-address\tTag', '-address'),
			('-applet\tTag', '-applet'),
			('-acronym\tTag', '-acronym'),
			('-button\tButton Tag', '-button'),
			('-br\tbr Tag', '-br'),
			('-big\tTag', '-big'),
			('-b\tTag', '-b'),
			('-body\tBody Tag', '-body'),
			('-base\tTag', '-base @${0:link}'),
			('-basefont\tTag', '-basefont'),
			('-blockquote\tTag', '-blockquote'),
			('-bdi\tTag', '-bdi'),
			('-bdo\tTag', '-bdo'),
			('-css\tCSS Improt', '-css @${0:link}'),
			('-css\tCSS Embed', '-css{>\n\t $0\n<}'),
			('-charset\tTag', '-charset(${1:utf-8})'),
			('-caption\tTag', '-caption'),
			('-code\tTag', '-code'),
			('-canvas\tTag', '-canvas'),
			('-content\tTag', '-content'),
			('-cite\tTag', '-cite'),
			('-colgroup\tTag', '-colgroup'),
			('-col\tTag', '-col'),
			('-center\tTag', '-center'),
			('-cdata\tTag', '-cdata'),
			('-dl\tTag', '-dl'),
			('-dd\tTag', '-dd'),
			('-dt\tTag', '-dt'),
			('-datalist\tTag', '-datalist'),
			('-data\tTag', '-data'),
			('-dir\tTag', '-dir'),
			('-del\tTag', '-del'),
			('-details\tTag', '-details'),
			('-dfn\tTag', '-dfn'),
			('-em\tTag', '-em'),
			('-equiv\tTag', '-equiv <${1:http-equiv}|${2:content}>'),
			('-embed\tTag', '-embed'),
			('-element\tTag', '-element'),
			('-email\tTag', '-email {1:<${2:name}|${3:value}>}'),
			('-footer\tTag', '-footer'),
			('-fget\tTag', '-fget @${0:link}'),
			('-fpost\tTag', '-fpost @${0:link}'),
			('-fupload\tForm', '-fupload @${0:link}'),
			('-fcheckbox\tTag', '-fcheckbox${1: <${2:name}|${3:value}>}'),
			('-fcolor\tTag', '-fcolor${1: <${2:name}|${3:value}>}'),
			('-fdate\tTag', '-fdate${1: <${2:name}|${3:value}>}'),
			('-fdatetime\tTag', '-fdatetime${1: <${2:name}|${3:value}>}'),
			('-fdatetime-local\tTag', '-fdatetime-local${1: <${2:name}|${3:value}>}'),
			('-fhidden\tHidden Input Tag', '-finput${1: <${2:name}|${3:value}>}'),
			('-fmonth\tTag', '-fmonth${1: <${2:name}|${3:value}>}'),
			('-fpassword\tTag', '-fpassword${1: <${2:name}|${3:value}>}'),
			('-fradio\tTag', '-fradio${1: <${2:name}|${3:value}>}'),
			('-fsearch\tTag', '-fsearch${1: <${2:name}|${3:value}>}'),
			('-ftext\tTag', '-ftext${1: <${2:name}|${3:value}>}'),
			('-ftextarea\tTag', '-ftextarea${1: <$2>}'),
			('-ftel\tTag', '-ftel${1: <${2:name}|${3:value}>}'),
			('-fnumber\tTag', '-number($1|$2|$3) ${4:<$5|$6>}'),
			('-frange\tTag', '-range($1|$2|$3) ${4:<$5|$6>}'),
			('-ftime\tTag', '-ftime${1: <${2:name}|${3:value}>}'),
			('-furl\tTag', '-furl${1: <${2:name}|${3:value}>}'),
			('-fweek\tTag', '-fweek${1: <${2:name}|${3:value}>}'),
			('-ffile\tTag', '-ffile${1: <${2:name}>}'),
			('-fselect\tTag', '-fselect'),
			('-fsubmit\tTag', '-fsubmit'),
			('-freset\tTag', '-freset'),
			('-fieldset\tTag', '-fieldset'),
			('-figure\tTag', '-figure'),
			('-figcaption\tTag', '-figcaption'),
			('-header\tTag', '-header'),
			('-hr\tTag', '-hr'),
			('-head\tTag', '-head'),
			('-h1\tTag', '-h1'),
			('-h2\tTag', '-h2'),
			('-h3\tTag', '-h3'),
			('-h4\tTag', '-h4'),
			('-h5\tTag', '-h5'),
			('-h6\tTag', '-h6'),
			('-iframe\tIframe Tag', '-iframe @${0:link}'),
			('-i\tTag', '-i'),
			('-icon\tTag', '-icon($1) @${0:link}'),
			('-ins\tTag', '-ins'),
			('-isindex\tTag', '-isindex'),
			('-js\tJS Embed', '-js{>\n\t $0\n<}'),
			('-js\tJS Improt', '-js @${0:link}'),
			('-kbd\tTag', '-kbd'),
			('-keygen\tTag', '-keygen'),
			('-li\tTag', '-li'),
			('-label\tTag', '-label'),
			('-legend\tTag', '-legend'),
			('-link\tTag', '-link(${1:rel}) @${0:link}'),
			('-main\tTag', '-main'),
			('-meta\tTag', '-meta <${1:name}|${2:content}>'),
			('-map\tTag', '-map'),
			('-mark\tTag', '-mark'),
			('-meter\tTag', '-meter'),
			('-nav\tTag', '-nav'),
			('-noframes\tTag', '-noframes'),
			('-noscript\tTag', '-noscript'),
			('-optgroup\tTag', '-optgroup'),
			('-option\tTag', '-option <${1:value}>${2: _${3:label}}'),
			('-ol\tTag', '-ol'),
			('-object\tTag', '-object'),
			('-output\tTag', '-output'),
			('-p\tTag', '-p'),
			('-php\tPHP Embed', '-php{>\n\t $0\n<}'),
			('-pre\tTag', '-pre'),
			('-progress\tTag', '-progress(${1:value}|${2:max}>)'),
			('-param\tTag', '-param <${1:name}|${2:value}>'),
			('-q\tTag', '-q'),
			('-rp\tTag', '-rp'),
			('-rt\tTag', '-rt'),
			('-rtc\tTag', '-rtc'),
			('-ruby\tTag', '-ruby'),
			('-section\tTag', '-section'),
			('-strong\tTag', '-strong'),
			('-small\tTag', '-small'),
			('-sub\tTag', '-sub'),
			('-sup\tTag', '-sup'),
			('-s\tTag', '-s'),
			('-shortcut\tTag', '-shortcut @${0:link}'),
			('-script\tTag', '-script(${1:type}){>\n\t $0\n<}'),
			('-source\tTag', '-source(${1:type}) @${0:link}'),
			('-summary\tTag', '-summary'),
			('-shadow\tTag', '-shadow'),
			('-samp\tTag', '-samp'),
			('-table\tTag', '-table'),
			('-tbody\tTag', '-tbody'),
			('-tr\tTag', '-tr'),
			('-td\tTag', '-td'),
			('-th\tTag', '-th'),
			('-thead\tTag', '-thead'),
			('-tfoot\tTag', '-tfoot'),
			('-template\tTag', '-template'),
			('-title\tTag', '-title'),
			('-tt\tTag', '-tt'),
			('-track\tTag', '-track(${1:kind}) @${0:link}'),
			('-ul\tTag', '-ul'),
			('-u\tTag', '-u'),
			('-var\tTag', '-var'),
			('-video\tTag', '-video @${0:link}'),
			('-wbr\tTag', '-wbr'),
		]);
	#}
#}
