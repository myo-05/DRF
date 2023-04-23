from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from articles.models import Article
from articles.serializers import ArticleSerializer
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class ArticleList(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True) #다중
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ArticleSerializer)
    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(): #유효성 점검
            serializer.save() #DB에 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED) #생성성공
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #요청오류


class ArticleDetail(APIView):

    def get(self, request, article_id, format=None):
        article = get_object_or_404(Article,id=article_id) # 에러처리를 위해 조회에 주로 사용!
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, article_id, format=None):
        article = get_object_or_404(Article,id=article_id)         
        serializer = ArticleSerializer(article, data=request.data) #조회한 데이터에 입력받은 데이터 덮어쓰기
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, format=None):
        article = get_object_or_404(Article,id=article_id)         
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)