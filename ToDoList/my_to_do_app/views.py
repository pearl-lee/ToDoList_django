from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'my_to_do_app/index.html', content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse("create Todo를 할 거야! => "+user_input_str)

def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    print("완료한 todo의 id", done_todo_id)
    todo = Todo.objects.get(id = done_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))

# 사용자가 url에 접근하여 index 함수를 실행할 때 기본적으로 request를 받아와
# user나 session과 같은 값들을 참조할 수 있게 되고, 
# 이를 render를 통해 사용자에게 웹페이지를 보여줄 떄 그대로 가져감