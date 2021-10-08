from django import forms
from books.models import Books, Rental #, Comment





class BooksForm(forms.ModelForm):
    class Meta:
        model = Books  # 사용할 모델
        fields = ['title', 'Writer','publisher','content']  # QuestionForm에서 사용할 Question 모델의 속성
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'Writer': forms.TextInput(attrs={'class': 'form-control'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'title': '도서제목',
            'Writer': '저자',
            'publisher': '출판사',
            'content': '내용',
        }

"""

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }

"""