from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article
from articles.serializers import ArticleSerializer

# Create your views here.


@api_view(['GET'])
def index(request):
    articles = Article.objects.all()
    article = articles[0]
    serializer = ArticleSerializer(article) #단일
    serializer = ArticleSerializer(articles, many=True) #다중
    return Response(serializer.data)