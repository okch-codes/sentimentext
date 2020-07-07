![Python application](https://github.com/trimalcione/sentimentext/workflows/Python%20application/badge.svg)

# Sentimentext (alpha)


> Sentimentext is a browser extension that automatically warns users about those news articles that linguistically resemble the style of a fake news.

> Check the emotional content of your news

## Logo

![Sentimentext Logo](https://github.com/trimalcione/sentimentext/blob/master/res/logo.png?raw=true)

## Description


Sentimentext is a browser extension that automatically warns users about those news articles that linguistically resemble the style of a fake news. Sentimentext scans the content of a webpage and analyses how emotionally loaded such content is by looking at its narrative style, the pattern of adjectives and syntaxes used. Sentimentext does not tell whether a news is fake or not: we do not want to tell people what to think, but give them a tool that helps them to think.

Fake news are found to purposefully employ emotional jargon and emotional narratives to hamper logical-thinking and foster emotional responses istead. They want to make you feel something. The emotional load of a text is usually analysed with a machine learning technique called sentiment analysis, which scores text based on two values: polarity and subjectivity. Several studies show how fake news are likely to have negative polarity [Kapusta et al. 2020] and high subjectivity [Volkova et al. 2017]. We want to use this distinctive emotional content of fake news to fight misinformation and provide citizens with a simple tool which alerts them of such possible suspicious behaviour.

## Getting started

#### Requirements
- Python >= 3.7.x
- Google Chrome

#### Backend deployment

1) Place in the project directory
2) Install dependencies with ``` pip install -r requirements.txt ```
3) launch the REST services with ```python nlp\__init__.py```


#### Chrome Extension Installation

1) Go to chrome://extensions
2) Enable _Developer mode_
3) Click on _Load unpacked_ and browse to the folder where it's placed _manifest.json_


## Sentimentext's Chrome extension notification preview

![Screenshot](https://github.com/trimalcione/sentimentext/blob/master/res/screenshot.jpg?raw=true)


---

## Software License

Copyright (c) the respective contributors, as shown by the AUTHORS file.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
