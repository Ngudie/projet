import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response

class NewsScrapeView(APIView):
    def get(self, request):
        url = 'https://www.vaticannews.va/fr/eglise.html'  # URL du site
        
        # URL De chaque onglet du site
        tabs = ['https://www.vaticannews.va/fr/pape.html', 'https://www.vaticannews.va/fr/vatican.html', 'https://www.vaticannews.va/fr/eglise.html', 'https://www.vaticannews.va/fr/monde.html']
        data = {}

        # La boucle qui parcours les onglet
        for tab in tabs:
            tab_url = url + '/' + tab
            response = requests.get(tab_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            div_class= soup.find_all('div', class_='div class')

            news_list = []
            for news in news_items:
                title = news.find('<a href')
                content = news.find('p').text  #
                news_list.append({'title': title, 'content': content})

            data[tab] = news_list

        return Response(json.dumps(data))


