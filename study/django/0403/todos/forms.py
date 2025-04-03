from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    content = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'class': 'work',
                'placeholder': '할일을 등록해 주세요.',
                'rows': 4, 'cols': 15,
            }
        )
    )

    class Meta:
        model = Todo
        fields = '__all__'
        