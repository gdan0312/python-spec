import re

from bs4 import BeautifulSoup


def parse(path_to_file):
    with open(path_to_file, encoding='utf-8') as html_file:
        n_headers, n_lists = 0, 0
        soup = BeautifulSoup(html_file, 'lxml')
        body = soup.find('div', id='bodyContent')
        n_images = len([img for img in body.find_all('img') if int(img.get('width', 0)) >= 200])

        for header in body.find_all(name=re.compile('^h[1-6]')):
            if header.find(text=re.compile('^[ETC]')):
                n_headers += 1

        for list_ in body.find_all(['ul', 'ol']):
            if not list_.find_parent(name=re.compile('^[uo]l')):
                n_lists += 1

        link_sequences = []
        for link in body.find_all('a'):
            links_count = 1
            for sibling in link.find_next_siblings():
                if sibling.name != 'a':
                    break
                links_count += 1
            link_sequences.append(links_count)
        max_sequence = max(link_sequences)
        return [n_images, n_headers, max_sequence, n_lists]
