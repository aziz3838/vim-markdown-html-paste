import subprocess
import html2text
import vim


def paste():
    '''
    Paste html formatted clipboard copy into markdown format
    '''
    # Get clipboard content
    cmd = 'xclip -selection clipboard -o -t TARGETS'
    targets = subprocess.check_output(cmd.split())

    # Check if html exists
    if 'text/html' in targets.split():
        cmd = 'xclip -selection clipboard -o -t text/html'
        content = subprocess.check_output(cmd.split())
    else:
        cmd = 'xclip -selection clipboard -o -t TEXT'
        content = subprocess.check_output(cmd.split())

    # Convert to markdown
    content = content.decode('unicode_escape').encode('ascii', 'ignore')
    h = html2text.HTML2Text()
    formatted_content = h.handle(content).\
        decode('unicode_escape').\
        encode('ascii', 'ignore').\
        replace('\x00', '')

    # Remove null characters
    formatted_content = formatted_content.replace('\x00', '')
    # Paste into buffer
    vim.command("normal! a" + formatted_content)
