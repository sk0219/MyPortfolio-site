from django.shortcuts import render
from .models import Profile, Work, Experience, Skill
from django.views.generic import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by("-id")[0]
        work_data = Work.objects.order_by("-id")
        return render(request, 'app/index.html', {
            'profile_data': profile_data,
            'work_data': work_data,
        })
        

class DetailView(View):
    def get(self, request, *args, **kwargs):
        work_data = Work.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/detail.html', {
            'work_data': work_data,
        })


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by("-id")[0]
        experience_data = Experience.objects.order_by("-id")
        skill_data = Skill.objects.order_by("-id")
        return render(request, 'app/profile.html', {
            'profile_data': profile_data,
            'experience_data': experience_data,
            'skill_data': skill_data,
        })