import sublime
import re

class Line:
#{
	def __init__( self, view, region, ):
	#{
		self.view= view;
		self.lineIndex= self.view.rowcol(view.line(region,).begin(),)[0]

		self.loadIndentations();
	#}

	def getRegion( self, ):
	#{
		return self.view.line(self.view.text_point(self.lineIndex,0,),);
	#}

	def contentMatches( self, regexp, ):
	#{
		return not not re.match(regexp,self.view.substr(self.getRegion(),),);
	#}

	def loadIndentations( self, ):
	#{
		self.indentations= list(map(lambda x:len(x),re.match(r'\t*(?: \t*)*',self.view.substr(self.getRegion(),),).group().split(' ',),),);
	#}

	def getNextLine( self, ):
	#{
		region= self.view.line(self.view.text_point(self.lineIndex+1,0,),);

		while( region.empty() ):
			next= self.view.line(self.view.text_point(self.view.rowcol(region.begin(),)[0]+1,0,),);
			if( next.begin()==region.begin() ):
				break;
			#if
			region= next;
		#while

		return Line(self.view,region);
	#}

	def moreIndentThen( self, line, ):
	#{
		selfIndentCount= len(self.indentations);
		lineIndentCount= len(line.indentations);

		for x in range(min(selfIndentCount,lineIndentCount,),):
			if( self.indentations[x]!=line.indentations[x] ):
				return self.indentations[x]-line.indentations[x];
			#if
		#for

		return 0;
	#}

	def getIndentCount( self, ):
	#{
		return len(self.indentations);
	#}

	def indent( self, edit, indentNum=1, ):
	#{
		indentations= self.indentations[0:indentNum];
		self.view.insert(edit,self.getRegion().begin()+sum(indentations)+len(indentations)-1,'\t');
	#}

	def unindent( self, edit, indentNum=1, ):
	#{
		indentations= self.indentations[0:indentNum];
		if( indentations[-1]>0 ):
			posation= self.getRegion().begin()+sum(indentations)+len(indentations)-1;
			self.view.erase(edit,sublime.Region(posation-1,posation),);
		#if
	#}
#}
