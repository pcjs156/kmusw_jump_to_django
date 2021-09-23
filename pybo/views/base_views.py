from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404

from pybo.models import Question, Answer


def index(request):
    """
    pybo 목록 출력
    """
    # 페이지
    page = request.GET.get('page', '1')
    # 검색어
    kw = request.GET.get('kw', '')
    # 정렬 기준
    so = request.GET.get('so', 'recent')
    # 카테고리
    category = request.GET.get('category', 'whole')

    if category == 'whole':
        question_list = Question.objects.all()
    elif category in list(map(lambda e: e[0], Question.CATEGORY_CHOICES)):
        question_list = Question.objects.filter(category=category)
    else:
        question_list = Question.objects.all()

    # 조회 및 정렬
    if so == 'recommend':
        question_list = question_list.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = question_list.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = question_list.order_by('-create_date')

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    # 페이징 (페이지 당 10건)
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'category': category}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)

    ordering = request.GET.get('ordering', 'create_date')
    page = request.GET.get('page', '1')

    if ordering == 'create_date' or ordering not in ('create_date', 'vote'):
        answers = question.answer_set.order_by('-create_date')
    elif ordering == 'vote':
        answers = question.answer_set.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')

    paginator = Paginator(answers, 10)
    page_obj = paginator.get_page(page)

    # 조회 수 증가
    question.view_count += 1
    question.save()

    context = {'question': question, 'answers': page_obj, 'ordering': ordering}
    return render(request, 'pybo/question_detail.html', context)
