"""Main entry point for godbolt_link and python -m godbolt_link"""
from .lib import make_godbolt_url


def main():
    """Main command line entry point"""

    # TODO: replace harcoded strings with proper CLI
    url_template = "https://godbolt.org/#g:!((g:!((g:!((h:codeEditor,i:(filename:'1',fontScale:14,fontUsePx:'0',j:1,lang:c%2B%2B,selection:(endColumn:22,endLineNumber:1,positionColumn:22,positionLineNumber:1,selectionStartColumn:22,selectionStartLineNumber:1,startColumn:22,startLineNumber:1),source:'@place_the_code_here@'),l:'5',n:'0',o:'C%2B%2B+source+%231',t:'0')),k:50,l:'4',n:'0',o:'',s:0,t:'0'),(g:!((g:!((h:compiler,i:(compiler:g122,deviceViewOpen:'1',filters:(b:'0',binary:'1',commentOnly:'0',demangle:'0',directives:'0',execute:'0',intel:'0',libraryCode:'1',trim:'1'),flagsViewOpen:'1',fontScale:14,fontUsePx:'0',j:1,lang:c%2B%2B,libs:!(),options:'-O+-std%3Dc%2B%2B17',selection:(endColumn:1,endLineNumber:1,positionColumn:1,positionLineNumber:1,selectionStartColumn:1,selectionStartLineNumber:1,startColumn:1,startLineNumber:1),source:1),l:'5',n:'0',o:'+x86-64+gcc+12.2+(Editor+%231)',t:'0')),k:50,l:'4',m:50,n:'0',o:'',s:0,t:'0'),(g:!((h:output,i:(editorid:1,fontScale:14,fontUsePx:'0',j:1,wrap:'1'),l:'5',n:'0',o:'Output+of+x86-64+gcc+12.2+(Compiler+%231)',t:'0')),header:(),l:'4',m:50,n:'0',o:'',s:0,t:'0')),k:50,l:'3',n:'0',o:'',t:'0')),l:'2',n:'0',o:'',t:'0')),version:4"

    source_code = '\n'.join(r"""
#include <iostream>

int main()
{
    std::cout << "Hello world!" << '\n';
}
""".splitlines()[1:])

    print(make_godbolt_url(url_template, source_code))


if __name__ == '__main__':
    main()
