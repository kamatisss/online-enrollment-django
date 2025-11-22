from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from formtools.wizard.views import SessionWizardView
from .forms import PersonalForm, EducationForm, FamilyForm, CourseForm, TuitionForm

FORMS = [
    ("personal", PersonalForm),
    ("education", EducationForm),
    ("family", FamilyForm),
    ("course", CourseForm),
    ("tuition", TuitionForm),
]

TEMPLATES = {
    "personal": "enrollment/personal.html",
    "education": "enrollment/education.html",
    "family": "enrollment/family.html",
    "course": "enrollment/course.html",
    "tuition": "enrollment/tuition.html",
}

@method_decorator(login_required, name='dispatch')
class EnrollmentWizard(SessionWizardView):
    form_list = FORMS

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        # Save each form separately
        for form in form_list:
            form.save()

        return render(self.request, "enrollment/enroll.html", {
            "form_data": [form.cleaned_data for form in form_list]
        })



def enroll_user(request):
    return render(request,'enrollment/enroll.html')

