import sublime_plugin
from HTSL.line import Line

class HtslSmartIndentCommand( sublime_plugin.TextCommand, ):
#{
	def run( self, edit, ):
	#{
		run(self.view,edit,'indent');
	#}
#}

class HtslSmartUnindentCommand( sublime_plugin.TextCommand, ):
#{
	def run( self, edit, ):
	#{
		run(self.view,edit,'unindent');
	#}
#}

def run( view, edit, method ):
#{
	for region in view.selection :
		firstLine= Line(view,region,);

		lines= [firstLine,];

		if( region.empty() and view.match_selector(region.a,'source.htsl - embedded',) ):
			currentLine= firstLine;
			nextLine= firstLine.getNextLine();

			while( ( nextLine.moreIndentThen(firstLine,)>0 or nextLine.contentMatches(r'\t*<\}',) ) and nextLine.moreIndentThen(currentLine,)<=1 ):
				lines.append(nextLine,);
				currentLine= nextLine;
				nextLine= nextLine.getNextLine();
			#while
		#if

		indentCount= firstLine.getIndentCount()
		for line in lines:
			getattr(line,method)(edit,indentCount,);
		#for
	#for
#}
