from weasyprint import HTML, CSS
from markdown import markdown as md

with open('cv.MD', 'r') as f:
    cv = f.read()

css = '''
body{
font-size: 5;
}
'''

html = md(cv)
HTML(string = html).write_pdf(
    'Rejoice_Chinwendu.pdf',
    stylesheets = [CSS(string = css)]
    )

print('all done')