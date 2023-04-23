from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from articles.models import Article
from articles.serializers import ArticleSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def articleAPI(request):
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

@api_view(['GET', 'PUT', 'DELETE'])
def articleDetailAPI(request,article_id):
    if request.method == 'GET':
        # article = Article.objects.get(id=article_id) # 작동은 하나 id값이 유효하지 않으면 에러
        article = get_object_or_404(Article,id=article_id) # 에러처리를 위해 조회에 주로 사용!
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        article = get_object_or_404(Article,id=article_id)         
        serializer = ArticleSerializer(article, data=request.data) #조회한 데이터에 입력받은 데이터 덮어쓰기
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article = get_object_or_404(Article,id=article_id)         
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)