from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article
from articles.serializers import ArticleSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        article = articles[0]
        serializer = ArticleSerializer(article) #단일
        serializer = ArticleSerializer(articles, many=True) #다중
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(): #유효성 점검
            serializer.save() #DB에 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED) #생성성공
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #요청오류