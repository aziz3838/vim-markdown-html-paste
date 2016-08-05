" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))


" --------------------------------
"  Ensure python support exists
" --------------------------------
if !has('python')
    finish
endif


" --------------------------------
"  Function(s)
" --------------------------------
function! PasteHtml2Markdown()
python << endOfPython

from vim_markdown_html_paste import paste
paste()

endOfPython
endfunction


" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! PasteHtml2Markdown call PasteHtml2Markdown()
