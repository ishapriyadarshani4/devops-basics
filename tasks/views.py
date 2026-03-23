from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Task

@csrf_exempt
@require_http_methods(["GET"])
def get_tasks(request):
    tasks = Task.objects.all()
    data = [{"id": t.id, "title": t.title, "done": t.done} for t in tasks]
    return JsonResponse(data, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def add_task(request):
    body = json.loads(request.body)
    task = Task.objects.create(title=body["title"])
    return JsonResponse({"id": task.id, "title": task.title, "done": task.done})

@csrf_exempt
@require_http_methods(["PUT"])
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.done = True
    task.save()
    return JsonResponse({"id": task.id, "title": task.title, "done": task.done, "message": "Task created successfully"})