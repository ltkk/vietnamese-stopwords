from smart_open import smart_open
import json
from data_prep import TextPreprocess

"""
firstly, parse xml.gz file to json.gz file with following command:
```
python -m gensim.scripts.segment_wiki -i -f wiki_data/viwiki-latest-pages-articles.xml.bz2 -o wiki_data/viwiki-latest-pages-articles.json.gz
```

And then use this code, parse json to txt and preprocess

"""


class WikiParser:
    def __init__(self, wiki_json_dump_file, output_file):
        self.wiki_json_dump_file = wiki_json_dump_file
        self.output_file = output_file
        self.tp = TextPreprocess()

    def parse_txt(self):
        i = 0
        with open(self.output_file, 'w', encoding='utf8') as writer:
            for line in smart_open(self.wiki_json_dump_file):
                article = json.loads(line.decode('utf8'))
                # each article has a "title",
                # a mapping of interlinks and a list of "section_titles" and "section_texts".
                texts = [article['title']]
                for section_title, section_text in zip(article['section_titles'], article['section_texts']):
                    texts.append(section_title)
                    texts.append(section_text)
                article_text = self.tp.preprocess(' '.join(texts), tokenize=True)
                writer.write(article_text + '\n')
                i += 1
                if i % 100000 == 0:
                    print('Process #', i, 'articles!')


if __name__ == '__main__':
    wiki_parser = WikiParser('wiki_data/viwiki-latest-pages-articles.json.gz',
                             'wiki_data/viwiki-latest-pages-articles.txt')

    wiki_parser.parse_txt()
