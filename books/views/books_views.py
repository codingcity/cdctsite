from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import BooksForm
from ..models import Books


@login_required(login_url='common:login')
def books_create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            books = form.save(commit=False)
            books.author = request.user  # author 속성에 로그인 계정 저장
            books.register_date = timezone.now()
            books.save()
            return redirect('books:index')
    else:
        form = BooksForm()
    context = {'form': form}
    return render(request, 'books/books_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    pybo 질문수정
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('notice:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('notice:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'notice/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    pybo 질문삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('notice:detail', question_id=question.id)
    question.delete()
    return redirect('notice:index')