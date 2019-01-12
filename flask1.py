from flask import Flask, render_template, request, escape
from vsearch import vsearch

app = Flask(__name__)


def log_request(req: 'flask_request', res: str)->None:
    with open('vsearch.log', 'a') as log:
        #print(req.form , file = log, end = '|')
        #print(req.remote_addr, file = log, end = '|')
        #print(req.user_agent, file = log, end = '|')
        #print(res, file = log)

        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    letter = request.form['letter']
    phrase = request.form['phrase']
    result = str(vsearch(phrase, letter))
    log_request(request, result)
    title = 'The search result is as follows:'
    if result.__len__ == 0:
        result = "No letters were found!"
    return render_template('result.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letter=letter,
                           the_result=result,)


@app.route('/')
@app.route('/entry')
def do_entry() -> 'html':
    return render_template('entry.html', the_title='Word search on web')


@app.route('/viewlog')
def viewlog() -> str:
        content = []
        with open('vsearch.log') as log:
                for i in log:
                        content.append([])
                        for item in i.split('|'):
                                content[-1].append(escape(item))
        heading = ('Form Data', 'Remote Address', 'User_Agent', 'Results')

        return render_template(
                'viewlog.html',
                the_title = 'View Log',
                the_row_titles = heading,
                the_data = content,)
if __name__ == "__main__":
    app.run(debug=True)
