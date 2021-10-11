from django import forms
from main.models import Courses, Users, Gallery, Teachers, News





class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses()
        fields = '__all__'



class UsersForm(forms.ModelForm):
	class Meta:
		model = Users()
		fields = "__all__"



class GalleryForm(forms.ModelForm):
	class Meta:
		model = Gallery()
		fields = "__all__"


class TeachersForm(forms.ModelForm):
	class Meta:
		model = Teachers()
		fields = "__all__"




class NewsForm(forms.ModelForm):
	class Meta:
		model = News()
		fields = "__all__"